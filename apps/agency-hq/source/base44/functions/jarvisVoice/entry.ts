import { createClientFromRequest } from 'npm:@base44/sdk@0.8.49';
import { secrets } from 'base44:runtime';

// Speaks text in the Jarvis voice through Fish Audio and returns MP3 audio as
// base64. Used by Talk (Base44 brain) so replies sound like Jarvis instead of
// the browser voice. Needs the FISH_API_KEY secret; without it the app falls
// back to the browser voice. The voice defaults to Blake's public Jarvis model.
const FISH_URL = 'https://api.fish.audio/v1/tts';
const DEFAULT_VOICE = '612b878b113047d9a770c069c8b4fdfe';
const MAX_CHARS = 900;

function json(body, status) {
  return Response.json(body, { status, headers: { 'Cache-Control': 'no-store' } });
}

function toBase64(buf) {
  const bytes = new Uint8Array(buf);
  let s = '';
  for (let i = 0; i < bytes.length; i += 0x8000) s += String.fromCharCode(...bytes.subarray(i, i + 0x8000));
  return btoa(s);
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

    const apiKey = secrets.get('FISH_API_KEY');
    if (typeof apiKey !== 'string' || !apiKey.trim()) {
      return json({ error: 'missing_secret', message: 'Add the FISH_API_KEY secret to use the Jarvis voice.' }, 503);
    }

    let body = {};
    try { body = await req.json(); } catch { /* empty */ }
    let text = typeof body?.text === 'string' ? body.text.replace(/\s+/g, ' ').trim() : '';
    if (!text) return json({ error: 'no_text' }, 400);
    if (text.length > MAX_CHARS) text = text.slice(0, MAX_CHARS).replace(/\s\S*$/, '') + '.';

    const profile = (await base44.asServiceRole.entities.Profile.list('-updated_date', 1).catch(() => []))[0];
    const voice = typeof profile?.jarvis_voice_id === 'string' && profile.jarvis_voice_id.trim() ? profile.jarvis_voice_id.trim() : DEFAULT_VOICE;

    let response;
    try {
      response = await fetch(FISH_URL, {
        method: 'POST',
        redirect: 'manual',
        signal: AbortSignal.timeout(20_000),
        headers: { Authorization: 'Bearer ' + apiKey.trim(), 'Content-Type': 'application/json', model: 's2-pro' },
        body: JSON.stringify({ text, reference_id: voice, format: 'mp3', normalize: true, latency: 'balanced' }),
      });
    } catch {
      return json({ error: 'fish_unreachable', message: 'Could not reach the voice service. Using the browser voice.' }, 502);
    }
    if (!response.ok) {
      let reason = '';
      try { reason = (await response.text()).replace(/\s+/g, ' ').trim().slice(0, 160); } catch { /* none */ }
      return json({ error: 'fish_rejected', status: response.status, message: `Fish Audio said ${response.status}${reason ? ': ' + reason : ''}` }, 502);
    }
    const buf = await response.arrayBuffer();
    if (!buf.byteLength) return json({ error: 'fish_empty', message: 'The voice service returned no audio.' }, 502);
    return json({ ok: true, mime: 'audio/mpeg', audio: toBase64(buf) }, 200);
  } catch {
    return json({ error: 'voice_failed', message: 'The Jarvis voice could not be generated.' }, 500);
  }
}
