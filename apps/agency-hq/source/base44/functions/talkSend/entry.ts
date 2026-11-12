import { buildCrmBriefing } from '../../shared/crm-context.ts';
import { createClientFromRequest } from 'npm:@base44/sdk@0.8.49';
import { secrets, waitUntil } from 'base44:runtime';
import { hudBaseUrl } from '../../shared/after-call-bridge.ts';

// Talk mode, Base44 path. The browser turns the owner's speech into text and
// sends it here. This posts it to the owner's own Jarvis in a voice chat
// conversation and returns at once with a turn id. The reply is collected in
// the background and saved on a TalkTurn row, which talkReply reads.
const ID = /^[a-f0-9]{24}$/;
const MAX_TEXT = 2000;
const POST_TIMEOUT_MS = 170_000;
const FALLBACK_POLL_MS = 4_000;
const FALLBACK_MAX_MS = 150_000;

const VOICE_INTRO =
  '[Voice chat from the HUD] I am talking to you out loud through my dashboard, and your reply will be read aloud to me. ' +
  'Answer in plain spoken sentences, usually one to three, unless I ask for detail. No markdown, lists, tables, links or emoji. ' +
  'You can still use your tools and do real work as normal; say briefly what you did. Here is what I said: ';
const VOICE_TAG = '[Voice] ';

function json(body, status) {
  return Response.json(body, { status, headers: { 'Cache-Control': 'no-store' } });
}

function messageContent(message) {
  if (typeof message?.content === 'string') return message.content;
  if (Array.isArray(message?.content)) {
    return message.content.map((part) => (typeof part === 'string' ? part : (typeof part?.text === 'string' ? part.text : ''))).join(' ');
  }
  if (typeof message?.text === 'string') return message.text;
  return '';
}

async function readMessages(baseUrl, token, conversationId) {
  const response = await fetch(`${baseUrl}/user-agent/conversations/${conversationId}/messages?limit=50`, {
    method: 'GET', redirect: 'manual', signal: AbortSignal.timeout(8_000), headers: { Authorization: `Bearer ${token}` },
  });
  if (!response.ok) return null;
  const data = await response.json();
  const messages = Array.isArray(data) ? data : data?.messages;
  if (!Array.isArray(messages)) return null;
  return messages
    .map((m, index) => ({ m, index, at: Date.parse(m?.created_at || m?.created_date || '') }))
    .sort((a, b) => (Number.isFinite(a.at) && Number.isFinite(b.at) && a.at !== b.at ? a.at - b.at : a.index - b.index))
    .map((x) => x.m);
}

// The last non-empty assistant text after our own message, or '' if none yet.
function replyAfter(messages, messageId) {
  if (!Array.isArray(messages)) return '';
  const at = messages.findIndex((m) => m?.id === messageId);
  if (at < 0) return '';
  let reply = '';
  for (const m of messages.slice(at + 1)) {
    if (m?.role !== 'assistant') continue;
    const text = messageContent(m).trim();
    if (text) reply = text;
  }
  return reply;
}

async function collectReply({ turns, turnRowId, baseUrl, token, conversationId, messageId, content }) {
  const finish = (data) => turns.update(turnRowId, data).catch(() => {});
  let posted = 'unknown';
  try {
    const response = await fetch(`${baseUrl}/user-agent/conversations/${conversationId}/messages`, {
      method: 'POST',
      redirect: 'manual',
      signal: AbortSignal.timeout(POST_TIMEOUT_MS),
      headers: { Authorization: `Bearer ${token}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ id: messageId, role: 'user', hidden: false, content }),
    });
    if (response.ok) posted = 'accepted';
    else if (response.status >= 400 && response.status < 500 && response.status !== 408) posted = 'rejected';
  } catch { posted = 'unknown'; }

  if (posted === 'rejected') return finish({ state: 'failed', error: 'Jarvis did not accept the message. Check your Jarvis agent ID and access token in Settings.' });

  // The send either finished (Jarvis has answered) or timed out. Either way,
  // read the conversation until a reply after our message holds steady.
  const started = Date.now();
  let last = '';
  let steady = 0;
  while (Date.now() - started < FALLBACK_MAX_MS) {
    let reply = '';
    try { reply = replyAfter(await readMessages(baseUrl, token, conversationId), messageId); } catch { reply = ''; }
    if (reply) {
      if (posted === 'accepted') return finish({ state: 'answered', reply: reply.slice(0, 6000) });
      if (reply === last) steady += 1; else { last = reply; steady = 0; }
      if (steady >= 2) return finish({ state: 'answered', reply: reply.slice(0, 6000) });
    }
    await new Promise((resolve) => setTimeout(resolve, FALLBACK_POLL_MS));
  }
  if (last) return finish({ state: 'answered', reply: last.slice(0, 6000) });
  return finish({ state: 'failed', error: 'Jarvis is still working on that. Check the chat in Base44 for the answer.' });
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
      if (raw.length > 16_000) return json({ error: 'body_too_large' }, 413);
      input = raw.trim() ? JSON.parse(raw) : {};
    } catch { return json({ error: 'invalid_json' }, 400); }
    const text = typeof input?.text === 'string' ? input.text.trim().slice(0, MAX_TEXT) : '';
    if (!text) return json({ error: 'empty', message: 'I did not catch anything. Try again.' }, 400);

    const token = secrets.get('JARVIS_NATIVE_TOKEN');
    if (!token) return json({ error: 'native_token_not_configured', message: 'Add your JARVIS_NATIVE_TOKEN secret first.' }, 503);

    const profile = (await base44.asServiceRole.entities.Profile.list('-updated_date', 1))[0] || null;
    const superagentId = typeof profile?.superagent_id === 'string' ? profile.superagent_id.trim() : '';
    if (!superagentId) return json({ error: 'no_agent', message: 'Add your Jarvis agent ID in Settings first.' }, 400);
    const baseUrl = hudBaseUrl(superagentId);

    let conversationId = typeof input?.conversation_id === 'string' && ID.test(input.conversation_id) ? input.conversation_id : '';
    const isNew = !conversationId;
    if (isNew) {
      try {
        const response = await fetch(baseUrl + '/user-agent/conversations/v2', {
          method: 'POST',
          redirect: 'manual',
          signal: AbortSignal.timeout(15_000),
          headers: { Authorization: 'Bearer ' + token, 'Content-Type': 'application/json' },
          body: JSON.stringify({ metadata: {} }),
        });
        if (!response.ok) return json({ error: 'conversation_failed', message: 'Could not open a chat with Jarvis. Check your Jarvis agent ID and access token in Settings.' }, 502);
        const data = await response.json();
        if (typeof data?.id !== 'string' || !ID.test(data.id)) throw new Error('invalid_conversation');
        conversationId = data.id;
      } catch {
        return json({ error: 'conversation_failed', message: 'Could not reach Jarvis right now. Try again in a moment.' }, 502);
      }
    }

    const turnId = crypto.randomUUID();
    const messageId = crypto.randomUUID();
    // Every voice turn carries a fresh Agency HQ briefing, so Jarvis answers from the live CRM.
    let briefing = '';
    try {
      const profile = (await base44.asServiceRole.entities.Profile.list('-updated_date', 1))[0];
      const lines = await buildCrmBriefing(base44.asServiceRole.entities, profile);
      if (lines.length) briefing = '[Live Agency HQ briefing, use it for anything about my leads, replies, calls, deals, missions or goal. For anything not in it, look it up in my Agency HQ app rather than guessing:]\n' + lines.join('\n').slice(0, 2500) + '\n[End of briefing]\n';
    } catch { /* answer without the briefing rather than fail */ }
    const content = (isNew ? VOICE_INTRO.replace('Here is what I said: ', '') + '\n' : VOICE_TAG) + briefing + 'Here is what I said: ' + text;
    const turns = base44.asServiceRole.entities.TalkTurn;
    const row = await turns.create({ turn_id: turnId, conversation_id: conversationId, message_id: messageId, state: 'sending', started_ms: Date.now() });

    if (isNew) {
      await base44.asServiceRole.entities.ActivityLog.create({
        type: 'note', task_title: 'Voice chat', message: 'Owner started a voice chat from the dashboard.',
      }).catch(() => {});
    }

    // Answer the browser now; the reply is collected in the background.
    waitUntil(new Promise((resolve) => setTimeout(() => resolve(collectReply({ turns, turnRowId: row.id, baseUrl, token, conversationId, messageId, content })), 0)));
    return json({ ok: true, turn_id: turnId, conversation_id: conversationId }, 202);
  } catch {
    return json({ error: 'talk_failed', message: 'That did not go through. Try again.' }, 500);
  }
}
