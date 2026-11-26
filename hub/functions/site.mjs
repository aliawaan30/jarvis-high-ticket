// Programme content for signed in members only. The build bundles the content into this function,
// so the public site holds no lesson text, prompts or file details.
import SITE from '../build/site-data.mjs';

const SB = (process.env.SUPABASE_URL || '').replace(/\/$/, '');
const KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || '';
const json = (status, body) => new Response(JSON.stringify(body), {
  status, headers: { 'content-type': 'application/json', 'cache-control': 'private, no-store' },
});

export default async (req) => {
  if (!SB || !KEY) return json(503, { error: 'The hub is not connected to Supabase yet.' });
  const token = (req.headers.get('authorization') || '').replace(/^Bearer\s+/i, '');
  if (!token) return json(401, { error: 'Sign in first.' });
  const u = await fetch(`${SB}/auth/v1/user`, { headers: { apikey: KEY, Authorization: `Bearer ${token}` } });
  if (!u.ok) return json(401, { error: 'Session expired. Sign in again.' });
  const email = encodeURIComponent(((await u.json()).email || '').toLowerCase());
  const r = await fetch(`${SB}/rest/v1/members?email=eq.${email}&active=eq.true&select=email`, {
    headers: { apikey: KEY, Authorization: `Bearer ${KEY}` },
  });
  const rows = r.ok ? await r.json() : [];
  if (!rows.length) return json(403, { error: 'No access.' });
  return json(200, SITE);
};

export const config = { path: '/api/site' };
