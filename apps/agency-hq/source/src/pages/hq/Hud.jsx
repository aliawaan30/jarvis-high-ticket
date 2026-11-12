import React, { useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import VoiceStage, { primeVoice } from '@/components/hq/VoiceStage';
import AppShell, { useProfile, panel, label } from '@/components/hq/AppShell';
import { C, MONO, useRows, todayISO, money, STAGES, STAGE_LABEL } from '@/lib/hq';

function arc(r, a0, a1) {
  const p = (a) => { const rad = (a - 90) * Math.PI / 180; return [250 + r * Math.cos(rad), 250 + r * Math.sin(rad)]; };
  const [x0, y0] = p(a0), [x1, y1] = p(a1);
  return `M${x0.toFixed(2)} ${y0.toFixed(2)} A${r} ${r} 0 ${a1 - a0 > 180 ? 1 : 0} 1 ${x1.toFixed(2)} ${y1.toFixed(2)}`;
}

// First money amount in the goal text: "$10k/mo by 1 Mar 2027" is 10000.
function goalAmount(text) {
  const m = String(text || '').match(/\$?\s*(\d[\d,]*(?:\.\d+)?)\s*(k|m)?\b/i);
  if (!m) return 0;
  const n = parseFloat(m[1].replace(/,/g, ''));
  const mult = /k/i.test(m[2] || '') ? 1000 : /m/i.test(m[2] || '') ? 1000000 : 1;
  return Math.round(n * mult);
}

const TICKS = Array.from({ length: 72 }, (_, i) => {
  const a = (i * 5 - 90) * Math.PI / 180, major = i % 6 === 0, r1 = 232, r2 = major ? 244 : 238;
  return { k: i, x1: 250 + r1 * Math.cos(a), y1: 250 + r1 * Math.sin(a), x2: 250 + r2 * Math.cos(a), y2: 250 + r2 * Math.sin(a), major };
});

export default function Hud() {
  const profile = useProfile();
  const accounts = useRows('Account');
  const touches = useRows('Touch', '-updated_date', 1000);
  const deals = useRows('Deal');
  const missions = useRows('Mission', 'number', 50);
  const weeks = useRows('WeekNumbers', '-week_start', 10);
  const logs = useRows('ActivityLog', '-created_date', 30);
  const tasks = useRows('Task', '-updated_date', 200);
  const [talkOpen, setTalkOpen] = useState(false);

  const d = useMemo(() => {
    const today = todayISO();
    const acc = accounts.rows.filter((a) => a.status !== 'do not contact');
    const callNow = acc.filter((a) => a.status === 'replied');
    const plannedToday = touches.rows.filter((t) => t.status === 'planned' && t.due_date && t.due_date <= today);
    const callsToday = touches.rows.filter((t) => t.channel === 'call' && t.status === 'logged' && t.date === today).length;
    const emailsDue = plannedToday.filter((t) => t.channel === 'email').length;
    const week = weeks.rows[0];
    const targetCalls = Number(week?.target_calls) || 5;
    const ms = missions.rows;
    const done = ms.filter((m) => m.status === 'done').length;
    const active = ms.find((m) => m.status === 'active') || ms.find((m) => m.status !== 'done');
    const monthKey = today.slice(0, 7);
    const wonMonth = deals.rows.filter((x) => x.stage === 'won' && String(x.won_date || x.updated_date || '').slice(0, 7) === monthKey);
    const cash = wonMonth.reduce((s, x) => s + (Number(x.proposed_price) || 0), 0);
    const target = goalAmount(profile?.goal_90_day) || 10000;
    const stageCounts = STAGES.map((s) => ({ s, n: acc.filter((a) => a.status === s).length }));
    const working = tasks.rows.some((t) => t.status === 'doing');
    const feed = [
      ...touches.rows.filter((t) => t.status !== 'planned' && t.status !== 'cancelled' && (t.summary || t.outcome)).slice(0, 12).map((t) => ({ at: t.updated_date || t.created_date, kind: (t.direction === 'in' ? 'REPLY' : (t.channel || 'note').toUpperCase()), text: `${t.account_name || ''}: ${t.summary || t.outcome || ''}`, color: t.direction === 'in' ? C.amber : C.cyan })),
      ...logs.rows.slice(0, 12).map((l) => ({ at: l.created_date, kind: String(l.type || 'note').toUpperCase(), text: l.message || l.task_title || '', color: C.cyan })),
    ].filter((f) => f.text && f.text.trim() !== ':').sort((a, b) => String(b.at).localeCompare(String(a.at))).slice(0, 7);
    return { callNow, plannedToday, callsToday, emailsDue, targetCalls, done, active, total: ms.length || 19, cash, target, stageCounts, working, feed };
  }, [accounts.rows, touches.rows, deals.rows, missions.rows, weeks.rows, logs.rows, tasks.rows, profile]);

  const needs = d.callNow.length > 0 && !talkOpen;
  const working = d.working && !needs && !talkOpen;
  const stateColor = needs ? C.amber : C.cyan;
  const stateText = talkOpen ? 'LISTENING. SPEAK TO JARVIS' : needs ? `NEEDS YOU: ${d.callNow.length === 1 ? 'A LEAD' : d.callNow.length + ' LEADS'} REPLIED` : working ? 'WORKING ON YOUR TASKS' : 'STANDING BY. ALL CAUGHT UP';
  const coreClass = needs ? 'hq-core-needs' : working ? 'hq-core-working' : 'hq-core-idle';
  const total = d.total, activeNum = d.active?.number || (d.done + 1);
  const segments = Array.from({ length: total }, (_, i) => {
    const n = i + 1, a0 = i * (360 / total) + 1.6, a1 = (i + 1) * (360 / total) - 1.6;
    const doneSeg = n <= d.done;
    return { k: n, d: arc(205, a0, a1), color: doneSeg ? C.cyan : n === activeNum ? C.amber : '#18293C', cls: n === activeNum && !doneSeg ? 'hq-active-seg' : '' };
  });
  const moneyPct = Math.min(1, d.cash / d.target);
  const lead = d.callNow[0];

  const tile = (value, title, sub, color) => (
    <div style={{ ...panel, display: 'flex', alignItems: 'center', gap: 16, padding: '16px 18px' }}>
      <div style={{ fontFamily: MONO, fontSize: 30, color, minWidth: 74 }}>{value}</div>
      <div style={{ flex: 1 }}><div style={{ fontSize: 15, fontWeight: 500 }}>{title}</div><div style={{ fontSize: 13, color: C.muted, marginTop: 2 }}>{sub}</div></div>
    </div>
  );

  return (
    <AppShell alert={needs} profile={profile}>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 24, alignItems: 'flex-start' }}>
        <section aria-label="Today" className="hq-col-today" style={{ flex: '1 1 280px', minWidth: 0, maxWidth: 360, display: 'flex', flexDirection: 'column', gap: 16 }}>
          <div style={label}>TODAY</div>
          <div style={panel}>
            {d.active ? (<>
              <div style={{ fontSize: 13, color: C.muted }}>Mission {d.active.number} of {total}</div>
              <div style={{ fontSize: 22, fontWeight: 600, marginTop: 4 }}>{d.active.name}</div>
            </>) : (<div style={{ fontSize: 15, color: C.muted }}>Missions appear once Jarvis 2.0 sets them up.</div>)}
            <div style={{ height: 6, borderRadius: 3, background: '#142233', marginTop: 14, overflow: 'hidden' }}><div style={{ height: '100%', width: `${Math.round(d.done / total * 100)}%`, background: `linear-gradient(90deg,#2EA8C4,${C.cyan})` }} /></div>
            <div style={{ fontSize: 13, color: C.muted, marginTop: 8 }}>{d.done} of {total} done.</div>
          </div>
          {tile(`${d.callsToday}/${d.targetCalls}`, 'Calls today', d.callsToday >= d.targetCalls ? 'Target hit. Nice.' : `${d.targetCalls - d.callsToday} to go to hit today`, C.cyan)}
          {tile(d.emailsDue, 'Emails due', d.emailsDue ? 'From your outreach plans' : 'Nothing due right now', C.text)}
          {tile(d.callNow.length, d.callNow.length === 1 ? 'Reply waiting' : 'Replies waiting', lead ? `${lead.business_name}: call them` : 'No replies waiting', C.amber)}
          <div style={panel}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'baseline' }}><span style={{ fontSize: 13, color: C.muted }}>This month</span><span style={{ fontFamily: MONO, fontSize: 12, color: C.faint }}>TARGET {money(d.target)}</span></div>
            <div style={{ fontFamily: MONO, fontSize: 34, color: C.amber, marginTop: 6 }}>{money(d.cash)}</div>
            <div style={{ height: 6, borderRadius: 3, background: '#142233', marginTop: 12, overflow: 'hidden' }}><div style={{ height: '100%', width: `${Math.round(moneyPct * 100)}%`, background: `linear-gradient(90deg,#C98A22,${C.amber})` }} /></div>
          </div>
        </section>

        <section aria-label="Jarvis" className="hq-col-core" style={{ flex: '2 1 460px', minWidth: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 10 }}>
          <div style={{ width: '100%', maxWidth: 520, position: 'relative' }}>
            <svg viewBox="0 0 500 500" role="img" aria-label={`Jarvis: ${stateText}`} style={{ width: '100%', height: 'auto', display: 'block' }}>
              <g className="hq-spin-slow">{TICKS.map((t) => <line key={t.k} x1={t.x1} y1={t.y1} x2={t.x2} y2={t.y2} stroke={t.major ? C.cyan : '#1E3A50'} strokeWidth={t.major ? 2 : 1} />)}</g>
              <circle cx="250" cy="250" r="226" fill="none" stroke={C.line} />
              {segments.map((s) => <path key={s.k} d={s.d} fill="none" stroke={s.color} strokeWidth="10" className={s.cls} />)}
              <g className="hq-spin-rev"><circle cx="250" cy="250" r="178" fill="none" stroke={C.cyan} strokeOpacity=".35" strokeWidth="2" strokeDasharray="2 10" /></g>
              <g className="hq-spin-med">
                <path d={arc(160, 10, 80)} fill="none" stroke={C.cyan} strokeOpacity=".8" strokeWidth="3" />
                <path d={arc(160, 130, 170)} fill="none" stroke={C.cyan} strokeOpacity=".45" strokeWidth="3" />
                <path d={arc(160, 230, 250)} fill="none" stroke={C.amber} strokeOpacity=".8" strokeWidth="3" />
              </g>
              <circle cx="250" cy="250" r="122" fill="none" stroke="#142233" strokeWidth="8" />
              {moneyPct > 0.005 && <path d={arc(122, 0, Math.max(1, moneyPct * 359))} fill="none" stroke={C.amber} strokeWidth="8" strokeLinecap="round" />}
              {working && <g className="hq-sweep"><path d="M250 250 L250 140" stroke={C.cyan} strokeOpacity=".7" strokeWidth="2" /></g>}
              <circle cx="250" cy="250" r="96" fill="#0A1626" stroke={C.line2} />
              {!talkOpen && (
                <g className={coreClass}>
                  <polygon points="250,192 302,282 198,282" fill="none" stroke={stateColor} strokeWidth="5" strokeLinejoin="round" />
                  <polygon points="250,226 274,268 226,268" fill={stateColor} fillOpacity=".85" />
                </g>
              )}
            </svg>
            {talkOpen && (
              <div aria-hidden="true" style={{ position: 'absolute', left: '50%', top: '50%', transform: 'translate(-50%,-50%)', display: 'flex', alignItems: 'center', height: 70 }}>
                {[0, .15, .3, .45, .3, .15, 0].map((dl, i) => <span key={i} className="hq-bar" style={{ animationDelay: `${dl}s` }} />)}
              </div>
            )}
          </div>
          <div style={{ textAlign: 'center' }}>
            <div style={{ fontSize: 30, fontWeight: 500, letterSpacing: '.38em', paddingLeft: '.38em' }}>J.A.R.V.I.S.</div>
            <div aria-live="polite" style={{ fontFamily: MONO, fontSize: 13, letterSpacing: '.14em', color: stateColor, marginTop: 8 }}>{stateText}</div>
            <button type="button" className="hq-btn" onClick={() => { primeVoice(); setTalkOpen(true); }} style={{ marginTop: 14, minHeight: 44, padding: '0 20px', borderRadius: 22, border: `1px solid ${C.line2}`, background: 'rgba(13,26,43,.8)', color: C.text, font: `500 14px 'Space Grotesk', sans-serif`, cursor: 'pointer' }}>Talk to Jarvis</button>
          </div>
          <div aria-label="Pipeline flow" style={{ width: '100%', maxWidth: 640, marginTop: 14 }}>
            <div style={{ position: 'relative', height: 2, background: `linear-gradient(90deg,${C.line},${C.line2},${C.line})`, margin: '0 28px' }}>
              {[0, 1.5, 3, 4.5].map((dl, i) => <span key={i} className="hq-particle" style={{ animationDelay: `${dl}s`, ...(i === 3 ? { background: C.amber, boxShadow: `0 0 10px ${C.amber}` } : {}) }} />)}
            </div>
            <div className="hq-stages" style={{ display: 'grid', gridTemplateColumns: `repeat(${d.stageCounts.length}, minmax(0,1fr))`, gap: 8, marginTop: 14, textAlign: 'center' }}>
              {d.stageCounts.map((x) => (
                <Link key={x.s} to="/pipeline" style={{ textDecoration: 'none', color: 'inherit' }}>
                  <div style={{ fontFamily: MONO, fontSize: 22, color: x.s === 'won' || x.s === 'call booked' ? C.amber : x.s === 'replied' ? C.cyan : C.text }}>{x.n}</div>
                  <div style={{ fontSize: 11, letterSpacing: '.12em', color: C.muted, marginTop: 2, textTransform: 'uppercase' }}>{STAGE_LABEL[x.s]}</div>
                </Link>
              ))}
            </div>
          </div>
        </section>

        <section aria-label="Live" className="hq-col-live" style={{ flex: '1 1 320px', minWidth: 0, maxWidth: 420, display: 'flex', flexDirection: 'column', gap: 16 }}>
          {lead && (
            <div className="hq-rise" style={{ border: '1px solid #6B5320', background: 'linear-gradient(180deg,rgba(245,183,74,.14),rgba(245,183,74,.04))', borderRadius: 12, padding: 18 }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8, fontFamily: MONO, fontSize: 12, letterSpacing: '.18em', color: C.amber }}><span className="hq-dot" style={{ width: 8, height: 8, borderRadius: '50%', background: C.amber }} />CALL NOW</div>
              <div style={{ fontSize: 20, fontWeight: 600, marginTop: 8 }}>{lead.business_name} replied</div>
              {lead.next_action && <div style={{ fontSize: 14, color: C.soft, marginTop: 6, lineHeight: 1.5 }}>{lead.next_action}</div>}
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10, marginTop: 14 }}>
                <Link to={`/leads/${lead.id}`} style={{ display: 'inline-flex', alignItems: 'center', minHeight: 44, padding: '0 16px', borderRadius: 8, background: C.amber, color: '#1A1206', fontWeight: 600, fontSize: 14, textDecoration: 'none' }}>Open call card</Link>
                {lead.phone && <a href={`tel:${lead.phone.replace(/[^0-9+]/g, '')}`} style={{ display: 'inline-flex', alignItems: 'center', minHeight: 44, padding: '0 16px', borderRadius: 8, border: '1px solid #6B5320', color: C.amber, textDecoration: 'none', fontSize: 14 }}>Call {lead.phone}</a>}
              </div>
            </div>
          )}
          <div style={label}>LIVE FEED</div>
          <div style={{ border: `1px solid ${C.line}`, borderRadius: 12, overflow: 'hidden', background: 'rgba(13,26,43,.5)' }}>
            {d.feed.length === 0 && <div style={{ padding: 16, fontSize: 14, color: C.muted }}>Nothing yet. Jarvis's work shows up here as it happens.</div>}
            {d.feed.map((f, i) => (
              <div key={i} className="hq-row" style={{ display: 'flex', gap: 12, padding: '13px 16px', borderBottom: '1px solid #12202F' }}>
                <span style={{ flex: 'none', width: 8, height: 8, borderRadius: '50%', marginTop: 7, background: f.color }} />
                <div style={{ minWidth: 0 }}>
                  <div style={{ fontFamily: MONO, fontSize: 11, letterSpacing: '.14em', color: C.faint }}>{f.kind}{f.at ? ' · ' + new Date(f.at).toLocaleString('en-GB', { day: 'numeric', month: 'short', hour: '2-digit', minute: '2-digit' }) : ''}</div>
                  <div style={{ fontSize: 14, color: '#DCE6EF', marginTop: 3, lineHeight: 1.45 }}>{f.text}</div>
                </div>
              </div>
            ))}
          </div>
        </section>
      </div>
      <VoiceStage open={talkOpen} onClose={() => setTalkOpen(false)} voiceProvider={profile?.voice_provider || 'base44'} ownerName={profile?.owner_name || ''} />
    </AppShell>
  );
}
