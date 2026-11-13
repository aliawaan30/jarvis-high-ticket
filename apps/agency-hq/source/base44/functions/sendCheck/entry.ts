import { method405, readBody, authorizeWrite } from '../../shared/hud.ts';
import { sendCheck } from '../../shared/send-check.ts';

// Function 19: the send gate. Jarvis calls it with POST JSON
// { email, account, settings, recipientLocalHour, sentTodayFromInbox } and the x-hud-key header,
// and sends only when it returns ok true. Plain code, no AI.
export default async function(req) {
  try {
    const m405 = method405(req);
    if (m405) return m405;
    const auth = await authorizeWrite(req);
    if (!auth.ok) return Response.json({ ok: false, reasons: ['unauthorised'] }, { status: 401 });
    const parsed = await readBody(req);
    if (!parsed.ok) return Response.json({ ok: false, reasons: [parsed.error] }, { status: parsed.status });
    return Response.json(sendCheck(parsed.body));
  } catch (e) {
    return Response.json({ ok: false, reasons: ['gate error: ' + String(e?.message || e)] }, { status: 500 });
  }
}
