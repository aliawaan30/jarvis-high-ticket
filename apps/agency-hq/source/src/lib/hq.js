import { useCallback, useEffect, useRef, useState } from 'react';
import { base44 } from '@/api/base44Client';

export const C = {
  bg: '#060A12', panel: 'rgba(13,26,43,.6)', line: '#16263A', line2: '#1E4458',
  text: '#E6EEF5', soft: '#C9D6E2', muted: '#94A7BA', faint: '#8FA3B8', dim: '#6F8296',
  cyan: '#5FD4EA', amber: '#F5B74A', green: '#5FE0B4', red: '#F08C82',
};
export const MONO = "'JetBrains Mono', ui-monospace, monospace";
export const SANS = "'Space Grotesk', system-ui, sans-serif";

export const STAGES = ['new lead', 'contacted', 'replied', 'call booked', 'proposal sent', 'won'];
export const STAGE_LABEL = { 'new lead': 'New lead', contacted: 'Contacted', replied: 'Replied', 'call booked': 'Call booked', 'call done': 'Call done', 'proposal sent': 'Proposal sent', won: 'Won', lost: 'Lost', 'not now': 'Not now', 'do not contact': 'Do not contact' };
export const CLIENT_STAGES = ['Kickoff', 'Build', 'Test', 'Handover', 'Live'];

export function statusStyle(status) {
  if (status === 'won') return { bg: 'rgba(95,224,180,.14)', color: C.green };
  if (['replied', 'call booked', 'call done', 'proposal sent'].includes(status)) return { bg: 'rgba(245,183,74,.14)', color: C.amber };
  if (status === 'contacted') return { bg: 'rgba(95,212,234,.12)', color: C.cyan };
  if (status === 'do not contact' || status === 'lost') return { bg: 'rgba(240,140,130,.12)', color: C.red };
  return { bg: 'rgba(148,167,186,.14)', color: C.soft };
}

export function todayISO(d = new Date()) {
  const p = (n) => String(n).padStart(2, '0');
  return `${d.getFullYear()}-${p(d.getMonth() + 1)}-${p(d.getDate())}`;
}

export function money(n) {
  const v = Number(n) || 0;
  return '$' + v.toLocaleString('en-US', { maximumFractionDigits: 0 });
}

export function parseSignals(text) {
  return String(text || '').split('\n').map((l) => l.trim()).filter(Boolean).map((l) => {
    const i = l.lastIndexOf('|');
    if (i < 0) return { label: l, url: '' };
    return { label: l.slice(0, i).trim(), url: l.slice(i + 1).trim() };
  });
}

export function isReady(email_status) {
  return email_status === 'published' || email_status === 'verified';
}

// Load an entity list and keep it fresh. Polls every `every` ms while the tab is visible.
export function useRows(entity, sort = '-updated_date', limit = 500, every = 15000) {
  const [rows, setRows] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const alive = useRef(true);
  const load = useCallback(async () => {
    try {
      const list = await base44.entities[entity].list(sort, limit);
      if (alive.current) { setRows(Array.isArray(list) ? list : []); setError(''); }
    } catch (e) {
      if (alive.current) setError('Could not load ' + entity + '. Check this app has the ' + entity + ' table.');
    } finally {
      if (alive.current) setLoading(false);
    }
  }, [entity, sort, limit]);
  useEffect(() => {
    alive.current = true;
    load();
    const t = setInterval(() => { if (document.visibilityState === 'visible') load(); }, every);
    return () => { alive.current = false; clearInterval(t); };
  }, [load, every]);
  return { rows, setRows, loading, error, reload: load };
}

export async function logTouch(account, summary, extra = {}) {
  try {
    await base44.entities.Touch.create({
      account_id: account.id, account_name: account.business_name, date: todayISO(),
      channel: 'note', direction: 'out', status: 'logged', summary, ...extra,
    });
  } catch { /* a missing timeline note must never block the move */ }
}
