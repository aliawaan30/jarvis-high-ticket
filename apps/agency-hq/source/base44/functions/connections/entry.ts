import { createClientFromRequest } from 'npm:@base44/sdk@0.8.49';
import { secrets } from 'base44:runtime';
import { keySource, getKey, saveKey } from '../../shared/keys.ts';

// Settings, Connections. Owner only. Saves keys into the locked Vault table,
// reports status (never a full key), creates the HUD key automatically, and
// builds the Jarvis voice agent in the owner's Retell account in one step.
// Every value is checked; nothing is logged.

const RETELL = 'https://api.retellai.com';
const SAVABLE = ['JARVIS_NATIVE_TOKEN', 'RETELL_API_KEY', 'FISH_API_KEY'];
const AGENT_NAME = 'Jarvis (Agency HQ)';
const PROMPT = `Live briefing from the owner's Agency HQ CRM (use it for any question about leads, replies, calls due, deals, missions or the goal, and never invent CRM facts that aren't in it): {{context_summary}}

HOW WORK GETS DONE: You are the voice of Jarvis. During the call you talk, answer from the live CRM briefing, and capture requests. The owner's full Jarvis does all real work automatically right after this call ends, from the call transcript, with every skill he has: finding leads, building offers, writing emails, research, call cards, CRM updates, proposals and more.

So for ANY request you can't answer right now from the briefing:
1. Never say you can't do it.
2. Confirm it in one short sentence with the key details (what, how many, where, by when). Ask one quick question only if something essential is missing.
3. Call add_task with a clear title and all the details.
4. Then say: "Got it. I'll start on that as soon as we hang up and message you when it's done."
5. Carry on with the conversation.

Only decline things that are truly unsafe or not allowed, like contacting a lead or client on the owner's behalf during this call. Never claim work is already finished.

HOW YOU SPEAK: You are Jarvis, the owner's AI agency partner. Keep every reply short and natural, one to three spoken sentences. One question at a time. Plain words, no lists or markdown. Use the owner's first name now and then. When the owner says goodbye or that's all, say a short goodbye and end the call with end_call.`;

function json(body, status = 200) { return Response.json(body, { status, headers: { 'Cache-Control': 'no-store' } }); }

async function retell(path, apiKey, method = 'GET', body) {
  const res = await fetch(RETELL + path, {
    method, redirect: 'manual', signal: AbortSignal.timeout(25_000),
    headers: { Authorization: 'Bearer ' + apiKey, 'Content-Type': 'application/json' },
    body: body ? JSON.stringify(body) : undefined,
  });
  let data = null; try { data = await res.json(); } catch { /* empty body */ }
  return { ok: res.ok, status: res.status, data };
}
function retellError(step, r) {
  const msg = (r.data && (r.data.message || r.data.error)) || ('HTTP ' + r.status);
  if (r.status === 401 || r.status === 403) return 'Retell did not accept the key. Check it in Retell, Settings, API Keys, and save it again.';
  return 'Retell said no at ' + step + ': ' + String(msg).slice(0, 200);
}
function randomHex(n) { const b = new Uint8Array(n); crypto.getRandomValues(b); return Array.from(b, (x) => x.toString(16).padStart(2, '0')).join(''); }

async function ensureHudKey(base44) {
  const now = await keySource('HUD_KEY', base44);
  if (now.source !== 'none') return now;
  await saveKey(base44, 'HUD_KEY', randomHex(16));
  return keySource('HUD_KEY', base44);
}

async function status(base44) {
  const hud = await ensureHudKey(base44);
  const out = { HUD_KEY: hud };
  for (const k of SAVABLE) out[k] = await keySource(k, base44);
  const profile = (await base44.asServiceRole.entities.Profile.list('-updated_date', 1).catch(() => []))[0] || {};
  return { ok: true, keys: out, voice: { agent_id: profile.retell_agent_id || '', from_number: profile.retell_from_number || '', provider: profile.voice_provider || 'base44' } };
}

async function setupVoice(base44, origin, language) {
  const apiKey = await getKey('RETELL_API_KEY', base44);
  if (!apiKey) return json({ ok: false, step: 'key', message: 'Save your Retell key first.' }, 400);
  const hudKey = await getKey('HUD_KEY', base44) || (await ensureHudKey(base44), await getKey('HUD_KEY', base44));
  const fn = (name) => origin + '/functions/' + name;
  const Profile = base44.asServiceRole.entities.Profile;
  const profile = (await Profile.list('-updated_date', 1).catch(() => []))[0] || null;

  // Already built? Reuse it rather than creating a second Jarvis agent.
  if (profile && profile.retell_agent_id) {
    const existing = await retell('/get-agent/' + encodeURIComponent(profile.retell_agent_id), apiKey);
    if (existing.ok && existing.data && existing.data.agent_name === AGENT_NAME) {
      return json({ ok: true, reused: true, agent_id: profile.retell_agent_id, message: 'Your Jarvis voice is already set up.' });
    }
  }

  // 1. The voice: reuse one named Jarvis, else import the course voice.
  const voices = await retell('/list-voices', apiKey);
  if (!voices.ok) return json({ ok: false, step: 'voice', message: retellError('list voices', voices) }, 502);
  const list = Array.isArray(voices.data) ? voices.data : (voices.data && voices.data.voices) || [];
  let voiceId = (list.find((v) => v && v.voice_name === 'Jarvis') || {}).voice_id;
  if (!voiceId) {
    const add = await retell('/add-community-voice', apiKey, 'POST', { voice_provider: 'fish_audio', provider_voice_id: '612b878b113047d9a770c069c8b4fdfe', voice_name: 'Jarvis' });
    if (!add.ok || !add.data || !add.data.voice_id) return json({ ok: false, step: 'voice', message: retellError('import the Jarvis voice', add) }, 502);
    voiceId = add.data.voice_id;
  }

  // 2. The LLM with the three HUD tools and end_call.
  const custom = (name, path, description, parameters, speak) => ({
    type: 'custom', name, description, url: fn(path), method: 'POST', args_at_root: true, timeout_ms: 8000,
    headers: { 'x-hud-key': hudKey, 'Content-Type': 'application/json' },
    speak_during_execution: !!speak, execution_message_description: speak ? 'One sec.' : undefined, parameters,
  });
  const tools = [
    custom('add_task', 'upsertTask', 'Add a task for the owner\'s full Jarvis to do after the call.', { type: 'object', properties: { title: { type: 'string', description: 'What to do, with every detail: what, how many, where, by when.' }, notes: { type: 'string' }, due_date: { type: 'string', description: 'YYYY-MM-DD if a date was given.' }, priority: { type: 'string', enum: ['low', 'normal', 'high'] }, execution_owner: { type: 'string', enum: ['jarvis', 'owner'] } }, required: ['title'] }, true),
    custom('remember', 'remember', 'Save a fact, decision or outcome the owner shared.', { type: 'object', properties: { text: { type: 'string' }, kind: { type: 'string', enum: ['fact', 'decision', 'event', 'question', 'outcome'] }, subject: { type: 'string' } }, required: ['text'] }, true),
    custom('get_context', 'getContext', 'Read more of the owner\'s CRM, for example their leads.', { type: 'object', properties: { section: { type: 'string', enum: ['leads'] }, limit: { type: 'integer' } } }, false),
    { type: 'end_call', name: 'end_call', description: 'End the call when the owner says goodbye or that is all.' },
  ];
  const llm = await retell('/create-retell-llm', apiKey, 'POST', { model: 'claude-4.5-haiku', model_temperature: 0.3, start_speaker: 'agent', begin_message: 'Hey {{first_name}}, how can I help you today?', default_dynamic_variables: { context_summary: 'unavailable', first_name: 'there' }, general_prompt: PROMPT, general_tools: tools });
  if (!llm.ok || !llm.data || !llm.data.llm_id) return json({ ok: false, step: 'llm', message: retellError('create the voice brain', llm) }, 502);

  // 3. The agent: create with the proven minimal body, then apply the tuning.
  const agent = await retell('/create-agent', apiKey, 'POST', { agent_name: AGENT_NAME, response_engine: { type: 'retell-llm', llm_id: llm.data.llm_id }, voice_id: voiceId, webhook_url: fn('retellWebhook') });
  if (!agent.ok || !agent.data || !agent.data.agent_id) return json({ ok: false, step: 'agent', message: retellError('create the agent', agent) }, 502);
  const agentId = agent.data.agent_id;
  const tune = await retell('/update-agent/' + encodeURIComponent(agentId), apiKey, 'PATCH', {
    voice_model: 's2.1-pro', voice_temperature: 0.6, voice_speed: 1, fallback_voice_ids: ['11labs-Anthony'], language: language || 'en-US',
    responsiveness: 1, interruption_sensitivity: 0.8, enable_backchannel: true, max_call_duration_ms: 3600000, allow_user_dtmf: true,
  });
  const warnings = tune.ok ? [] : ['Some voice tuning was not accepted by Retell (' + retellError('tune', tune) + '). The agent works with Retell defaults.'];

  // 4. Publish, then save the agent on the Profile.
  const pub = await retell('/publish-agent-version/' + encodeURIComponent(agentId), apiKey, 'POST', {});
  if (!pub.ok) warnings.push('Publishing did not confirm (' + retellError('publish', pub) + '). Open the agent in Retell and press Publish.');
  try {
    if (profile && profile.id) await Profile.update(profile.id, { retell_agent_id: agentId, retell_greets: true });
    else await Profile.create({ retell_agent_id: agentId, retell_greets: true });
  } catch { warnings.push('Could not save the agent on your profile. Open Settings, Voice, and pick it.'); }

  if (profile && profile.retell_agent_id && profile.retell_agent_id !== agentId) warnings.push('Your previous Retell agent was left untouched. You can delete it in Retell if you no longer use it.');
  return json({ ok: true, agent_id: agentId, webhook: fn('retellWebhook'), published: pub.ok, warnings });
}

export default async function(req) {
  try {
    if (req.method !== 'POST') return json({ ok: false, error: 'method_not_allowed' }, 405);
    let base44, user;
    try { base44 = createClientFromRequest(req); user = await base44.auth.me(); } catch { return json({ ok: false, error: 'unauthorized' }, 401); }
    const ownerEmail = secrets.get('OWNER_EMAIL');
    const isOwner = user && (user.role === 'admin' || (ownerEmail && user.email && String(user.email).toLowerCase() === String(ownerEmail).toLowerCase()));
    if (!isOwner) return json({ ok: false, error: 'forbidden' }, 403);

    let body = {};
    try { const raw = await req.text(); body = raw && raw.trim() ? JSON.parse(raw) : {}; } catch { return json({ ok: false, error: 'invalid_json' }, 400); }
    const action = String(body.action || 'status');

    if (action === 'status') return json(await status(base44));

    if (action === 'save') {
      const name = String(body.name || '');
      const value = String(body.value || '').trim();
      if (!SAVABLE.includes(name)) return json({ ok: false, error: 'unknown_key' }, 400);
      if (value.length < 8 || value.length > 400 || /\s/.test(value)) return json({ ok: false, error: 'That does not look like a key. Copy it again, with nothing before or after it.' }, 400);
      const saved = await saveKey(base44, name, value);
      return json({ ok: true, name, last4: saved.last4 });
    }

    if (action === 'hud_key_for_jarvis') {
      // Shown once, to the owner, so they can hand it to Jarvis.
      await ensureHudKey(base44);
      return json({ ok: true, hud_key: await getKey('HUD_KEY', base44) });
    }

    if (action === 'test_retell') {
      const apiKey = await getKey('RETELL_API_KEY', base44);
      if (!apiKey) return json({ ok: false, message: 'No Retell key saved yet.' });
      const r = await retell('/v2/list-agents', apiKey, 'POST', { limit: 1, filter_criteria: { channel: { op: 'eq', value: 'voice' } } });
      return json(r.ok ? { ok: true, message: 'Retell accepted the key.' } : { ok: false, message: retellError('check the key', r) });
    }

    if (action === 'test_jarvis') {
      const token = await getKey('JARVIS_NATIVE_TOKEN', base44);
      if (!token) return json({ ok: false, message: 'Save your Jarvis access token first.' });
      const profile = (await base44.asServiceRole.entities.Profile.list('-updated_date', 1).catch(() => []))[0] || {};
      const agentId = String(profile.superagent_id || '').trim();
      if (!/^[a-f0-9]{24}$/i.test(agentId)) return json({ ok: false, message: 'Add your Jarvis agent ID below first: the 24 characters after /agents/ in Jarvis, Agent settings, Developer.' });
      let r;
      try {
        r = await fetch('https://app.base44.com/api/apps/' + agentId + '/user-agent/conversations/v2', {
          method: 'POST', redirect: 'manual', signal: AbortSignal.timeout(15_000),
          headers: { Authorization: 'Bearer ' + token, 'Content-Type': 'application/json' }, body: JSON.stringify({ metadata: { source: 'hud-connection-test' } }),
        });
      } catch { return json({ ok: false, message: 'Could not reach Jarvis. Try again in a moment.' }); }
      if (r.ok) return json({ ok: true, message: 'Jarvis is connected. Message Jarvis and Talk will work.' });
      if (r.status === 401 || r.status === 403) return json({ ok: false, message: 'Jarvis did not accept the access token. Make a new one (One app or Superagent, the Agent entry, Full access) and save it above.' });
      if (r.status === 404) return json({ ok: false, message: 'No Jarvis agent with that ID. Check the agent ID below.' });
      return json({ ok: false, message: 'Jarvis answered with error ' + r.status + '. Send Jarvis a screenshot of this.' });
    }

    if (action === 'setup_voice') {
      let origin = '';
      try { const u = new URL(String(body.origin || '')); if (u.protocol === 'https:') origin = u.origin; } catch { /* invalid */ }
      if (!origin) return json({ ok: false, message: 'Open Settings from your published app and try again.' }, 400);
      return await setupVoice(base44, origin, typeof body.language === 'string' ? body.language.slice(0, 10) : '');
    }

    return json({ ok: false, error: 'unknown_action' }, 400);
  } catch (e) {
    return json({ ok: false, error: 'connections_error', message: String(e && e.message || e).slice(0, 200) }, 500);
  }
}
