import { buildCrmBriefing } from '../../shared/crm-context.ts';
import { createClientFromRequest } from 'npm:@base44/sdk@0.8.49';
import { secrets } from 'base44:runtime';
import { buildRevenueLines } from '../../shared/call-context.ts';
import { getKey } from '../../shared/keys.ts';

const CONTROL_NAME = 'owner_native_call';
const IN_FLIGHT_MS = 10_000;
const RETELL_URL = 'https://api.retellai.com/v2/create-phone-call';
// Retell call configuration lives on the Profile record, not in secrets.
const RETELL_PROFILE_FIELDS = ['retell_agent_id', 'retell_from_number', 'owner_phone'];

function json(body, status) {
  return Response.json(body, { status, headers: { 'Cache-Control': 'no-store' } });
}

// Secret-derived values are never returned in full; only a short tail for diagnostics.
function mask(value) {
  if (typeof value !== 'string' || !value) return value ?? null;
  if (value.length <= 4) return 'set (' + value.length + ' chars)';
  return '…' + value.slice(-4);
}

// Short context summary with the doing / waiting labels the Retell prompt expects,
// and the revenue lines shared with the base44 call route.
function buildContextSummary(profile, tasks, revenueLines, crmLines = []) {
  const doing = tasks.filter((t) => t.status === 'doing').map((t) => t.title).filter(Boolean).slice(0, 5);
  const waiting = tasks.filter((t) => t.status === 'todo').map((t) => t.title).filter(Boolean).slice(0, 5);
  const lines = [];
  if (profile?.goal_90_day) lines.push('goal: ' + profile.goal_90_day);
  lines.push('doing: ' + (doing.length ? doing.join('; ') : 'nothing in progress'));
  lines.push('waiting: ' + (waiting.length ? waiting.join('; ') : 'nothing waiting'));
  if (revenueLines) lines.push(revenueLines);
  if (crmLines.length) { lines.push('AGENCY HQ (live CRM, use this for anything about leads, replies, calls, deals, missions or the goal):'); lines.push(...crmLines); }
  return lines.join('\n').slice(0, 3800);
}

export default async function(req) {
  try {
    if (req.method !== 'POST') return json({ error: 'method_not_allowed' }, 405);

    let base44, user;
    try {
      base44 = createClientFromRequest(req);
      user = await base44.auth.me();
    } catch { return json({ error: 'unauthorized' }, 401); }
    if (!user) return json({ error: 'unauthorized' }, 401);
    if (user.role !== 'admin') return json({ error: 'forbidden' }, 403);

    let input = {};
    try {
      const raw = await req.text();
      if (raw && raw.trim()) input = JSON.parse(raw);
    } catch { return json({ error: 'invalid_json' }, 400); }
    const dryRun = input?.dry_run === true;
    const message = typeof input?.message === 'string' ? input.message.slice(0, 400) : '';

    const apiKey = await getKey('RETELL_API_KEY', base44);
    if (typeof apiKey !== 'string' || !apiKey.trim()) {
      return json({ error: 'missing_secret', message: 'Retell is not set up yet. Open Settings and pick Retell Jarvis to finish setup.' }, 503);
    }

    // Plain 400 naming the missing Profile field(s). Retell config is not read from secrets.
    const profile = (await base44.asServiceRole.entities.Profile.list('-updated_date', 1))[0];
    const missing = [];
    for (const field of RETELL_PROFILE_FIELDS) {
      const v = profile ? profile[field] : undefined;
      if (typeof v !== 'string' || !v.trim()) missing.push(field);
    }
    if (missing.length) {
      const onlyMobile = missing.length === 1 && missing[0] === 'owner_phone';
      return json({
        error: 'missing_profile_field',
        message: onlyMobile ? 'Add your mobile number in Settings first.' : 'Retell is not set up yet. Open Settings and pick Retell Jarvis to finish setup.',
      }, 400);
    }

    const tasks = await base44.asServiceRole.entities.Task.list('-updated_date', 500);
    const revenueLines = await buildRevenueLines(base44.asServiceRole.entities.Lead).catch(() => '');
    const crmLines = await buildCrmBriefing(base44.asServiceRole.entities, profile).catch(() => []);
    const context_summary = message
      ? ('Jarvis is calling because: ' + message + (revenueLines ? '\n' + revenueLines : '') + (crmLines.length ? '\nAGENCY HQ (live CRM):\n' + crmLines.join('\n') : '')).slice(0, 3800)
      : buildContextSummary(profile, tasks, revenueLines, crmLines);

    const payload = {
      from_number: profile.retell_from_number.trim(),
      to_number: profile.owner_phone.trim(),
      override_agent_id: profile.retell_agent_id.trim(),
      retell_llm_dynamic_variables: { context_summary },
    };

    if (dryRun) {
      // Stops before the Retell POST. No dial. Values are masked.
      return json({
        dry_run: true,
        dialed: false,
        provider: 'retell',
        api_key: 'redacted',
        profile_fields: {
          retell_agent_id: mask(profile.retell_agent_id),
          retell_from_number: mask(profile.retell_from_number),
          owner_phone: mask(profile.owner_phone),
        },
        would_send: {
          from_number: mask(payload.from_number),
          to_number: mask(payload.to_number),
          override_agent_id: mask(payload.override_agent_id),
          retell_llm_dynamic_variables: { context_summary },
        },
      }, 200);
    }

    // Reuse the existing CallControl in-flight lock so base44 and Retell cannot double-dial.
    const controls = base44.asServiceRole.entities.CallControl;
    const rows = await controls.filter({ name: CONTROL_NAME }, '-created_date', 2);
    if (rows.length !== 1) return json({ error: rows.length ? 'control_not_unique' : 'control_not_initialized' }, 503);
    const control = rows[0];
    if (['submitting', 'unknown'].includes(control.dispatch_state)) return json({ error: 'dispatch_unknown' }, 409);

    const requestId = crypto.randomUUID();
    const now = Date.now();
    const claim = await controls.updateMany(
      { id: control.id, lock_until_ms: { $lte: now }, dispatch_state: { $nin: ['submitting', 'unknown'] } },
      { $set: { request_id: requestId, lock_until_ms: now + IN_FLIGHT_MS, dispatch_state: 'claimed', conversation_id: '', message_id: '' } },
    );
    if (!claim?.success || claim.updated !== 1) return json({ error: 'cooldown_active' }, 429);

    const release = async (state, lockUntilMs) => {
      try {
        await controls.updateMany({ id: control.id, request_id: requestId }, { $set: { dispatch_state: state, lock_until_ms: lockUntilMs } });
      } catch { /* self-heals after the cooldown expires */ }
    };

    let response;
    try {
      response = await fetch(RETELL_URL, {
        method: 'POST',
        redirect: 'manual',
        signal: AbortSignal.timeout(20_000),
        headers: { Authorization: 'Bearer ' + apiKey, 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });
    } catch {
      await release('failed', now);
      return json({ error: 'retell_unreachable', message: 'Could not reach Retell right now. Try again in a moment.' }, 502);
    }

    if (!response.ok) {
      await release('failed', now);
      // Show Retell's own reason (status and its short message), never the key.
      let reason = '';
      try { const body = await response.text(); try { const j = JSON.parse(body); reason = String(j?.message || j?.error_message || j?.error || body); } catch { reason = body; } } catch { /* no body */ }
      reason = reason.replace(/key_[A-Za-z0-9_-]+/g, '[hidden]').replace(/\s+/g, ' ').trim().slice(0, 160);
      const hint = response.status === 401 || response.status === 403 ? ' Check the RETELL_API_KEY secret in this app.'
        : response.status === 404 ? ' Check your Retell number and agent in Settings, Voice provider.'
        : response.status === 402 ? ' Add a payment method or credit in your Retell account.'
        : '';
      return json({ error: 'retell_rejected', status: response.status, message: `Retell said ${response.status}${reason ? ': ' + reason : ''}.${hint}` }, 502);
    }

    let data = {};
    try { data = await response.json(); } catch { /* handled below */ }
    const callId = data?.call_id;
    if (typeof callId !== 'string' || !callId) {
      await release('failed', now);
      return json({ error: 'retell_no_call_id', message: 'Retell could not start the call. Try again.' }, 502);
    }

    await release('submitted', 0);
    return json({ ok: true, provider: 'retell', call_id: callId, request_id: requestId }, 202);
  } catch {
    return json({ error: 'call_failed', message: 'Retell call could not be started. Try again.' }, 500);
  }
}
