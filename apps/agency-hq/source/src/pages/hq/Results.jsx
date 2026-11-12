import React, { useMemo } from 'react';
import AppShell, { useProfile, panel, label } from '@/components/hq/AppShell';
import { C, MONO, useRows, money, parseSignals } from '@/lib/hq';

const RANK = { 'new lead': 0, contacted: 1, replied: 2, 'call booked': 3, 'call done': 3, 'proposal sent': 4, won: 5 };

function Bars({ items, color }) {
  const max = Math.max(1, ...items.map((i) => i.n));
  return items.map((i) => (
    <div key={i.label} style={{ display: 'flex', alignItems: 'center', gap: 12, marginTop: 12, fontSize: 14 }}>
      <span style={{ width: 190, flex: 'none' }}>{i.label}</span>
      <div style={{ flex: 1, height: 14, borderRadius: 4, background: '#142233', overflow: 'hidden' }}><div className="hq-barx" style={{ height: '100%', width: `${i.n / max * 100}%`, background: color }} /></div>
      <span style={{ fontFamily: MONO, width: 30, textAlign: 'right' }}>{i.n}</span>
    </div>));
}

export default function Results() {
  const profile = useProfile();
  const accounts = useRows('Account');
  const deals = useRows('Deal');
  const r = useMemo(() => {
    const acc = accounts.rows.filter((a) => a.status !== 'do not contact');
    const reached = (k) => acc.filter((a) => (RANK[a.status] ?? -1) >= k).length;
    const F = [['Leads', acc.length], ['Contacted', reached(1)], ['Replied', reached(2)], ['Call booked', reached(3)], ['Proposal', reached(4)], ['Won', reached(5)]];
    const funnel = F.map((x, i) => ({ label: x[0], n: x[1], conv: i === 0 || !F[i - 1][1] ? '' : Math.round(x[1] / F[i - 1][1] * 100) + '%' }));
    const drops = funnel.slice(1).map((f, i) => ({ from: funnel[i].label, to: f.label, lost: funnel[i].n - f.n })).sort((a, b) => b.lost - a.lost);
    const booked = deals.rows.filter((d) => ['call booked', 'call done', 'proposal sent', 'won'].includes(d.stage));
    const tally = (key) => { const m = {}; booked.forEach((d) => { const k = d[key] || 'Unknown'; m[k] = (m[k] || 0) + 1; }); return Object.entries(m).map(([label, n]) => ({ label, n })).sort((a, b) => b.n - a.n); };
    const value = ['new lead', 'contacted', 'replied', 'call booked', 'proposal sent'].map((s) => ({ label: s, v: acc.filter((a) => a.status === s).reduce((t, a) => t + (Number(a.value_estimate) || 0), 0) }));
    const months = []; const now = new Date();
    for (let i = 5; i >= 0; i--) { const d = new Date(now.getFullYear(), now.getMonth() - i, 1); const key = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`; months.push({ key, label: d.toLocaleString('en-GB', { month: 'short' }), v: deals.rows.filter((x) => x.stage === 'won' && String(x.won_date || '').slice(0, 7) === key).reduce((t, x) => t + (Number(x.proposed_price) || 0), 0) }); }
    return { funnel, drop: drops[0], bySignal: tally('booked_via_signal'), byChannel: tally('booked_via_channel'), value, months };
  }, [accounts.rows, deals.rows]);
  const maxV = Math.max(1, ...r.value.map((x) => x.v)); const maxM = Math.max(1, ...r.months.map((x) => x.v));
  const best = [...r.months].sort((a, b) => b.v - a.v)[0];
  const tied = r.months.filter((m) => m.v === best?.v && m.v > 0);
  return (
    <AppShell profile={profile}>
      <div><div style={label}>RESULTS</div><h1 style={{ margin: '6px 0 0', fontSize: 30, fontWeight: 600 }}>What is working</h1></div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(min(420px,100%),1fr))', gap: 18, marginTop: 20 }}>
        <section style={panel}><div style={label}>THE FUNNEL</div>
          {r.funnel.map((f) => (<div key={f.label} style={{ display: 'flex', alignItems: 'center', gap: 12, marginTop: 12, fontSize: 14 }}><span style={{ width: 110, flex: 'none' }}>{f.label}</span><div style={{ flex: 1, height: 22, borderRadius: 4, background: '#142233', overflow: 'hidden' }}><div className="hq-barx" style={{ height: '100%', width: `${r.funnel[0].n ? f.n / r.funnel[0].n * 100 : 0}%`, background: f.label === 'Won' ? C.green : C.cyan }} /></div><span style={{ fontFamily: MONO, width: 40, textAlign: 'right' }}>{f.n}</span><span style={{ fontFamily: MONO, width: 52, textAlign: 'right', color: C.muted, fontSize: 12 }}>{f.conv}</span></div>))}
          <div style={{ fontSize: 13, color: C.soft, marginTop: 14 }}>{r.drop && r.drop.lost > 0 ? `Biggest drop: ${r.drop.from.toLowerCase()} to ${r.drop.to.toLowerCase()}.` : 'Not enough data yet.'}</div>
        </section>
        <section style={panel}><div style={label}>BOOKED CALLS BY SIGNAL</div>
          {r.bySignal.length ? <Bars items={r.bySignal} color={C.cyan} /> : <div style={{ marginTop: 10, color: C.muted, fontSize: 14 }}>No booked calls yet.</div>}
          <div style={{ ...label, marginTop: 20 }}>BY CHANNEL</div>
          {r.byChannel.length ? <Bars items={r.byChannel} color={C.amber} /> : <div style={{ marginTop: 10, color: C.muted, fontSize: 14 }}>No booked calls yet.</div>}
        </section>
        <section style={panel}><div style={label}>PIPELINE VALUE BY STAGE</div>
          <div style={{ display: 'flex', alignItems: 'flex-end', gap: 14, height: 180, marginTop: 16 }}>
            {r.value.map((x) => (<div key={x.label} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6, height: '100%', justifyContent: 'flex-end' }}><span style={{ fontFamily: MONO, fontSize: 12, color: C.soft }}>{money(x.v)}</span><div className="hq-bary" style={{ width: '100%', height: Math.max(2, x.v / maxV * 130), borderRadius: '4px 4px 0 0', background: C.cyan }} /><span style={{ fontSize: 12, color: C.muted, textAlign: 'center', textTransform: 'capitalize' }}>{x.label}</span></div>))}
          </div>
        </section>
        <section style={panel}><div style={label}>CASH COLLECTED BY MONTH</div>
          <div style={{ display: 'flex', alignItems: 'flex-end', gap: 14, height: 180, marginTop: 16 }}>
            {r.months.map((x) => (<div key={x.key} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 6, height: '100%', justifyContent: 'flex-end' }}><span style={{ fontFamily: MONO, fontSize: 12, color: C.soft }}>{money(x.v)}</span><div className="hq-bary" style={{ width: '100%', height: Math.max(2, x.v / maxM * 130), borderRadius: '4px 4px 0 0', background: C.amber }} /><span style={{ fontSize: 12, color: C.muted }}>{x.label}</span></div>))}
          </div>
          <div style={{ fontSize: 13, color: C.soft, marginTop: 14 }}>{tied.length > 1 ? `${tied.map((t) => t.label).join(' and ')} tied at ${money(best.v)}.` : best && best.v > 0 ? `${best.label} is your best month so far.` : 'No cash collected yet.'}</div>
        </section>
      </div>
    </AppShell>
  );
}
