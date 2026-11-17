import { secrets } from 'base44:runtime';

// Connection keys: Base44 Secrets first (anyone already set up keeps working),
// then the locked Vault table that Settings, Connections writes to.
// Values are never returned to the browser or logged.
export const KEY_NAMES = ['HUD_KEY', 'JARVIS_NATIVE_TOKEN', 'RETELL_API_KEY', 'FISH_API_KEY'];

export async function vaultRow(base44, name) {
  if (!base44) return null;
  try {
    const rows = await base44.asServiceRole.entities.Vault.filter({ name });
    return (rows && rows[0]) || null;
  } catch { return null; }
}

export async function getKey(name, base44) {
  const fromSecrets = secrets.get(name);
  if (fromSecrets) return fromSecrets;
  const row = await vaultRow(base44, name);
  return row && row.value ? String(row.value) : null;
}

export async function keySource(name, base44) {
  const s = secrets.get(name);
  if (s) return { source: 'secret', last4: String(s).slice(-4) };
  const row = await vaultRow(base44, name);
  if (row && row.value) return { source: 'vault', last4: row.last4 || String(row.value).slice(-4) };
  return { source: 'none', last4: '' };
}

export async function saveKey(base44, name, value) {
  const v = String(value || '').trim();
  const now = new Date().toISOString();
  const data = { name, value: v, last4: v.slice(-4), saved_at: now };
  const row = await vaultRow(base44, name);
  if (row) await base44.asServiceRole.entities.Vault.update(row.id, data);
  else await base44.asServiceRole.entities.Vault.create(data);
  return { last4: data.last4, saved_at: now };
}
