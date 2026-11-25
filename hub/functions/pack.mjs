// Pack downloads and the update manifest.
// Signed in student (browser):  GET /api/pack?pack=offer   with Authorization: Bearer <supabase token>  -> { url }
// Jarvis, with the update link:  GET /api/pack?code=<update code>&manifest=1   -> pack list with versions
//                                GET /api/pack?code=<update code>&pack=offer   -> redirect to the zip
const SB = (process.env.SUPABASE_URL || '').replace(/\/$/, '');
const KEY = process.env.SUPABASE_SERVICE_ROLE_KEY || '';

const json = (status, body) => new Response(JSON.stringify(body), {
  status, headers: { 'content-type': 'application/json', 'cache-control': 'no-store' },
});

async function sb(path, init = {}) {
  const r = await fetch(`${SB}${path}`, {
    ...init,
    headers: { apikey: KEY, Authorization: `Bearer ${KEY}`, 'content-type': 'application/json', ...(init.headers || {}) },
  });
  if (!r.ok) throw new Error(`supabase ${r.status}`);
  return r.json();
}

async function memberByCode(code) {
  if (!/^[0-9a-f-]{36}$/i.test(code)) return null;
  const rows = await sb(`/rest/v1/members?update_code=eq.${code}&active=eq.true&select=email`);
  return rows[0] || null;
}

async function memberByToken(token) {
  const r = await fetch(`${SB}/auth/v1/user`, { headers: { apikey: KEY, Authorization: `Bearer ${token}` } });
  if (!r.ok) return null;
  const user = await r.json();
  const email = encodeURIComponent((user.email || '').toLowerCase());
  const rows = await sb(`/rest/v1/members?email=eq.${email}&active=eq.true&select=email`);
  return rows[0] || null;
}

async function signedUrl(row) {
  const s = await sb(`/storage/v1/object/sign/packs/${row.path}`, {
    method: 'POST', body: JSON.stringify({ expiresIn: 300 }),
  });
  return `${SB}/storage/v1${s.signedURL}&download=${encodeURIComponent(row.file)}`;
}

export default async (req) => {
  if (!SB || !KEY) return json(503, { error: 'The hub is not connected to Supabase yet.' });
  const q = new URL(req.url).searchParams;
  const code = q.get('code') || '';
  const token = (req.headers.get('authorization') || '').replace(/^Bearer\s+/i, '');
  try {
    const member = code ? await memberByCode(code) : token ? await memberByToken(token) : null;
    if (!member) return json(401, { error: 'This link or login is not active. Ask in your Discord channel.' });

    const rows = await sb('/rest/v1/pack_versions?select=id,title,module,version,note,file,path&order=module');
    if (q.get('manifest')) {
      return json(200, {
        packs: rows.map(({ id, title, module, version, note, file }) => ({ id, title, module, version, note, file })),
        how_to_update: 'For each installed pack with a newer version, fetch this link with &pack=<id> added and reinstall every skill in the zip.',
      });
    }
    const row = rows.find((r) => r.id === q.get('pack'));
    if (!row) return json(404, { error: 'Unknown pack.' });
    const url = await signedUrl(row);
    return code ? Response.redirect(url, 302) : json(200, { url, version: row.version });
  } catch (e) {
    return json(500, { error: 'Download failed. Try again in a minute.' });
  }
};

export const config = { path: '/api/pack' };
