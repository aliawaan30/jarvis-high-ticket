import { createClientFromRequest } from 'npm:@base44/sdk@0.8.49';

// Talk mode, Base44 path. Reports whether Jarvis has answered a turn sent by
// talkSend. Read only.
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;

function json(body, status) {
  return Response.json(body, { status, headers: { 'Cache-Control': 'no-store' } });
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
      input = raw && raw.trim() ? JSON.parse(raw) : {};
    } catch { return json({ error: 'invalid_json' }, 400); }
    const turnId = typeof input?.turn_id === 'string' ? input.turn_id : '';
    if (!UUID.test(turnId)) return json({ error: 'invalid_turn' }, 400);

    const rows = await base44.asServiceRole.entities.TalkTurn.filter({ turn_id: turnId }, '-created_date', 1);
    const turn = rows && rows[0];
    if (!turn) return json({ state: 'unknown' }, 404);
    return json({ state: turn.state || 'sending', reply: turn.reply || '', error: turn.error || '' }, 200);
  } catch {
    return json({ error: 'talk_failed' }, 500);
  }
}
