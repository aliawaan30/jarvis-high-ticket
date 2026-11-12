import React, { useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import AppShell, { useProfile, label, Chip, Empty } from '@/components/hq/AppShell';
import { C, MONO, useRows, STAGE_LABEL, statusStyle, isReady, todayISO } from '@/lib/hq';

const FILTERS = ['All', 'Due today', 'Tier A', 'Email ready', 'Found by activity', 'Do not contact'];
const TH = { textAlign: 'left', fontFamily: MONO, fontSize: 11, letterSpacing: '.14em', color: C.faint, fontWeight: 500, padding: '12px 14px', borderBottom: `1px solid ${C.line}`, whiteSpace: 'nowrap' };
const TD = { padding: '12px 14px', borderBottom: '1px solid #12202F', fontSize: 14, verticalAlign: 'top' };

export default function Leads() {
  const profile = useProfile();
  const { rows, loading, error } = useRows('Account');
  const touches = useRows('Touch', '-updated_date', 1000);
  const [q, setQ] = useState('');
  const [filter, setFilter] = useState('All');
  const today = todayISO();
  const due = useMemo(() => new Set(touches.rows.filter((t) => t.status === 'planned' && t.due_date && t.due_date <= today).map((t) => t.account_id)), [touches.rows, today]);
  const shown = rows.filter((a) => {
    const dnc = a.status === 'do not contact';
    if (filter === 'Do not contact') { if (!dnc) return false; } else if (dnc) return false;
    if (filter === 'Due today' && !(due.has(a.id) || a.status === 'replied')) return false;
    if (filter === 'Tier A' && a.tier !== 'A') return false;
    if (filter === 'Email ready' && !isReady(a.email_status)) return false;
    if (filter === 'Found by activity' && !String(a.source || '').toLowerCase().includes('activity')) return false;
    const s = q.trim().toLowerCase();
    return !s || String(a.business_name || '').toLowerCase().includes(s) || String(a.owner_name || '').toLowerCase().includes(s);
  });
  return (
    <AppShell profile={profile}>
      <div style={{ display: 'flex', flexWrap: 'wrap', alignItems: 'flex-end', gap: '16px 24px' }}>
        <div><div style={label}>LEADS</div><h1 style={{ margin: '6px 0 0', fontSize: 30, fontWeight: 600 }}>{shown.length} of {rows.length} leads</h1></div>
        <label className="hq-search" style={{ marginLeft: 'auto', display: 'flex', flexDirection: 'column', gap: 6, fontSize: 13, color: C.muted }}>Search
          <input type="search" value={q} onChange={(e) => setQ(e.target.value)} placeholder="Business or owner" style={{ minHeight: 42, width: 260, padding: '0 12px', borderRadius: 8, border: `1px solid ${C.line2}`, background: '#0A1626', color: C.text, font: `400 14px 'Space Grotesk', sans-serif` }} />
        </label>
      </div>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, marginTop: 16 }}>
        {FILTERS.map((f) => <button key={f} type="button" onClick={() => setFilter(f)} style={{ minHeight: 40, padding: '0 14px', borderRadius: 20, border: `1px solid ${f === filter ? '#2E6A85' : C.line}`, background: f === filter ? 'rgba(95,212,234,.14)' : 'transparent', color: f === filter ? C.text : C.muted, font: `500 13px 'Space Grotesk', sans-serif`, cursor: 'pointer' }}>{f}</button>)}
      </div>
      {error && <div style={{ marginTop: 16, color: C.red }}>{error}</div>}
      {!loading && !error && rows.length === 0 ? (
        <div style={{ marginTop: 18 }}><Empty>No leads yet. Ask Jarvis: "Find me 5 leads", and they land here with their signals, owner and contact details.</Empty></div>
      ) : (
        <>
        <div className="hq-mobile-only" style={{ flexDirection: 'column', gap: 10, marginTop: 16 }}>
          {shown.map((a) => {
            const st = statusStyle(a.status);
            const isDue = due.has(a.id) || a.status === 'replied';
            return (
              <Link key={a.id} to={`/leads/${a.id}`} className="hq-card" style={{ display: 'block', textDecoration: 'none', color: C.text, border: `1px solid ${isDue ? '#6B5320' : C.line}`, background: 'rgba(13,26,43,.85)', borderRadius: 12, padding: 14 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                  <span style={{ fontSize: 16, fontWeight: 600, flex: 1, minWidth: 0 }}>{a.business_name}</span>
                  {a.tier && <Chip text={a.tier} bg={a.tier === 'A' ? 'rgba(95,212,234,.16)' : 'rgba(148,167,186,.14)'} color={a.tier === 'A' ? C.cyan : C.soft} />}
                </div>
                <div style={{ fontSize: 13, color: C.muted, marginTop: 4 }}>{[a.city, a.state].filter(Boolean).join(', ')}{a.owner_name ? ' · ' + a.owner_name : ''}</div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 10, flexWrap: 'wrap' }}>
                  <Chip text={STAGE_LABEL[a.status] || a.status || 'New lead'} bg={st.bg} color={st.color} />
                  <span style={{ fontSize: 13, color: isDue ? C.amber : C.soft }}>{a.status === 'replied' ? 'Call now' : (a.next_action || '')}</span>
                </div>
              </Link>
            );
          })}
        </div>
        <div className="hq-desktop-only" style={{ overflowX: 'auto', marginTop: 16, border: `1px solid ${C.line}`, borderRadius: 12, background: C.panel }}>
          <table style={{ width: '100%', minWidth: 1100, borderCollapse: 'collapse' }}>
            <thead><tr>{['BUSINESS', 'OWNER', 'TIER', 'STATUS', 'EMAIL', 'FOUND BY', 'NEXT STEP', 'LAST TOUCH'].map((h) => <th key={h} style={TH}>{h}</th>)}</tr></thead>
            <tbody>
              {shown.map((a) => {
                const st = statusStyle(a.status);
                const ready = isReady(a.email_status);
                const isDue = due.has(a.id) || a.status === 'replied';
                return (
                  <tr key={a.id} className="hq-row">
                    <td style={TD}><Link to={`/leads/${a.id}`} style={{ fontWeight: 600, textDecoration: 'none' }}>{a.business_name}</Link><div style={{ fontSize: 12, color: C.muted, marginTop: 2 }}>{[a.city, a.state].filter(Boolean).join(', ')}</div></td>
                    <td style={{ ...TD, color: a.owner_name && !/not found|confirm/i.test(a.owner_name) ? C.text : C.amber }}>{a.owner_name || 'not found'}</td>
                    <td style={TD}>{a.tier ? <Chip text={a.tier} bg={a.tier === 'A' ? 'rgba(95,212,234,.16)' : 'rgba(148,167,186,.14)'} color={a.tier === 'A' ? C.cyan : C.soft} /> : '-'}</td>
                    <td style={TD}><Chip text={STAGE_LABEL[a.status] || a.status || 'New lead'} bg={st.bg} color={st.color} /></td>
                    <td style={TD}><div>{a.email || '-'}</div><div style={{ fontSize: 12, color: ready ? C.green : C.muted, marginTop: 2, textTransform: 'uppercase' }}>{a.email_status || 'unknown'}</div></td>
                    <td style={{ ...TD, fontFamily: MONO, fontSize: 12, color: C.muted, textTransform: 'uppercase' }}>{a.source || '-'}</td>
                    <td style={{ ...TD, color: isDue ? C.amber : C.soft }}>{a.status === 'replied' ? 'Call now' : (a.next_action || '-')}</td>
                    <td style={{ ...TD, color: C.muted, whiteSpace: 'nowrap' }}>{a.last_touch_date || 'Not yet'}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
        </>
      )}
    </AppShell>
  );
}
