import { buildCrmBriefing } from '../../shared/crm-context.ts';
import { createClientFromRequest } from 'npm:@base44/sdk@0.8.49';
import { secrets } from 'base44:runtime';
import { buildRevenueLines } from '../../shared/call-context.ts';
import { getKey } from '../../shared/keys.ts';

// Talk mode, Retell path. Creates a Retell web call for the owner's own Jarvis
// voice agent and returns the short lived access token the browser needs to
// join it. No phone number is used. The call ends up at retellWebhook like any
// other call from this agent, so the after-call bridge still runs agreed tasks.
// Retell retired v2 web calls (deprecation notice 2026-09-30); v3 takes the same body.
const RETELL_URL = 'https://api.retellai.com/v3/create-web-call';

function json(body, status) {
  return Response.json(body, { status, headers: { 'Cache-Control': 'no-store' } });
}

function buildContextSummary(profile, tasks, revenueLines, crmLines = []) {
  const doing = tasks.filter((t) => t.status === 'doing').map((t) => t.title).filter(Boolean).slice(0, 5);
  const waiting = tasks.filter((t) => t.status === 'todo').map((t) => t.title).filter(Boolean).slice(0, 5);
  const lines = ['The owner opened a live voice chat from the dashboard. This is not a phone call. They want to talk, so keep turns short and let them lead.'];
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

    const apiKey = await getKey('RETELL_API_KEY', base44);
    if (typeof apiKey !== 'string' || !apiKey.trim()) {
      return json({ error: 'missing_secret', message: 'Retell is not set up yet. Open Settings and pick Retell Jarvis to finish setup.' }, 503);
    }

    const profile = (await base44.asServiceRole.entities.Profile.list('-updated_date', 1))[0];
    const agentId = typeof profile?.retell_agent_id === 'string' ? profile.retell_agent_id.trim() : '';
    if (!agentId) {
      return json({ error: 'missing_profile_field', message: 'Retell is not set up yet. Open Settings and pick Retell Jarvis to finish setup.' }, 400);
    }

    // Read everything at once: the greeting waits on the slowest read, not the sum.
    const [tasks, revenueLines, crmLines] = await Promise.all([
      base44.asServiceRole.entities.Task.list('-updated_date', 200).catch(() => []),
      buildRevenueLines(base44.asServiceRole.entities.Lead).catch(() => ''),
      buildCrmBriefing(base44.asServiceRole.entities, profile).catch(() => []),
    ]);
    const context_summary = buildContextSummary(profile, tasks || [], revenueLines, crmLines);

    let response;
    try {
      response = await fetch(RETELL_URL, {
        method: 'POST',
        redirect: 'manual',
        signal: AbortSignal.timeout(15_000),
        headers: { Authorization: 'Bearer ' + apiKey, 'Content-Type': 'application/json' },
        body: JSON.stringify({
          agent_id: agentId,
          retell_llm_dynamic_variables: {
            context_summary,
            first_name: (typeof profile?.owner_name === 'string' && profile.owner_name.trim() ? profile.owner_name.trim().split(/\s+/)[0] : 'there'),
          },
          metadata: { source: 'hud_talk' },
        }),
      });
    } catch {
      return json({ error: 'retell_unreachable', message: 'Could not reach Retell right now. Try again in a moment.' }, 502);
    }
    if (!response.ok) {
      // Show Retell's own reason (status and its short message), never the key.
      let reason = '';
      try {
        const body = await response.text();
        try { const j = JSON.parse(body); reason = String(j?.message || j?.error_message || j?.error || body); } catch { reason = body; }
      } catch { /* no body */ }
      reason = reason.replace(/key_[A-Za-z0-9_-]+/g, '[hidden]').replace(/\s+/g, ' ').trim().slice(0, 160);
      const hint = response.status === 401 || response.status === 403 ? ' Check the RETELL_API_KEY secret in this app.'
        : response.status === 404 ? ' The Retell agent was not found: re-pick it in Settings, Voice provider.'
        : response.status === 402 ? ' Add a payment method or credit in your Retell account.'
        : '';
      return json({ error: 'retell_rejected', status: response.status, message: `Retell said ${response.status}${reason ? ': ' + reason : ''}.${hint}` }, 502);
    }

    let data = {};
    try { data = await response.json(); } catch { /* handled below */ }
    if (typeof data?.access_token !== 'string' || !data.access_token) {
      return json({ error: 'retell_no_token', message: 'Retell could not start the voice chat. Try again.' }, 502);
    }

    // Log without making the caller wait for it.
    base44.asServiceRole.entities.ActivityLog.create({
      type: 'note', task_title: 'Voice chat', message: 'Owner started a voice chat from the dashboard.',
    }).catch(() => {});

    // The access token is single use and expires about 30 seconds after creation.
    // v3 returns connection details: the browser SDK 3.x needs all four to connect.
    return json({
      ok: true, provider: 'retell',
      access_token: data.access_token,
      call_id: data.call_id || '',
      transport: typeof data.transport === 'string' ? data.transport : undefined,
      ice_servers: Array.isArray(data.ice_servers) ? data.ice_servers : undefined,
    }, 200);
  } catch {
    return json({ error: 'talk_failed', message: 'The voice chat could not be started. Try again.' }, 500);
  }
}
