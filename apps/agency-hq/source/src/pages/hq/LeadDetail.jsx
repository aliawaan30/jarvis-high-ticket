import React, { useMemo, useState } from 'react';
import { Link, useNavigate, useParams } from 'react-router-dom';
import { base44 } from '@/api/base44Client';
import AppShell, { useProfile, panel, label, Chip, Empty } from '@/components/hq/AppShell';
import { C, MONO, useRows, STAGE_LABEL, statusStyle, parseSignals, isReady, todayISO, logTouch } from '@/lib/hq';

const STEP_ORDER = ['email 1', 'email 2', 'call 1', 'email 3', 'last call', 'call now'];

export default function LeadDetail() {
  const { id } = useParams();
  const nav = useNavigate();
  const profile = useProfile();
  const accounts = useRows('Account');
  const touches = useRows('Touch', '-updated_date', 1000);
  const [more, setMore] = useState(false);
  const [confirm, setConfirm] = useState('');
  const [copied, setCopied] = useState(false);
  const [busy, setBusy] = useState(false);
  const a = accounts.rows.find((x) => x.id === id);
  const mine = useMemo(() => touches.rows.filter((t) => t.account_id === id), [touches.rows, id]);
  const plan = mine.filter((t) => t.step).sort((x, y) => (STEP_ORDER.indexOf(String(x.step).toLowerCase()) - STEP_ORDER.indexOf(String(y.step).toLowerCase())) || String(x.due_date).localeCompare(String(y.due_date)));
  const timeline = mine.filter((t) => t.status !== 'planned' && t.status !== 'cancelled').sort((x, y) => String(y.updated_date || y.created_date).localeCompare(String(x.updated_date || x.created_date)));
  const today = todayISO();

  if (!a) {
    return <AppShell profile={profile}>{accounts.loading ? <div style={{ color: C.muted }}>Loading lead...</div> : <Empty>This lead isn't here anymore. <Link to="/leads">Back to leads</Link></Empty>}</AppShell>;
  }

  const st = statusStyle(a.status);
  // Jarvis sometimes writes several numbers or a note into one field: show the first clean one.
  const phoneMatch = String(a.phone || '').match(/\+?\(?\d[\d\s().-]{8,}\d/);
  const phone = phoneMatch ? phoneMatch[0].trim() : '';
  const phoneExtra = phone && String(a.phone).trim() !== phone ? String(a.phone).trim() : '';
  const emailMatch = String(a.email || '').match(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i);
  const email = emailMatch ? emailMatch[0] : '';
  const emailExtra = email && String(a.email).trim() !== email ? String(a.email).trim() : '';
  const phoneHref = phone ? 'tel:' + phone.replace(/[^0-9+]/g, '') : '';
  const scores = [['Can pay', a.can_pay_score], ['Has the problem now', a.problem_score], ['Reachable', a.reachable_score]];

  async function doDelete() {
    setBusy(true);
    try {
      for (const t of mine) { await base44.entities.Touch.delete(t.id); }
      await base44.entities.Account.delete(a.id);
      nav('/leads');
    } catch { setConfirm('Could not delete it. Nothing was removed.'); setBusy(false); }
  }
  async function doDnc() {
    setBusy(true);
    try {
      await base44.entities.Account.update(a.id, { status: 'do not contact' });
      for (const t of mine.filter((t) => t.status === 'planned')) { await base44.entities.Touch.update(t.id, { status: 'cancelled', cancelled_reason: 'do not contact ' + today }); }
      await logTouch(a, 'Marked do not contact. Never contacted again.');
      await accounts.reload(); await touches.reload();
      setConfirm('Done. They will never be contacted again.'); setMore(false);
    } catch { setConfirm('Could not update. Nothing changed.'); }
    setBusy(false);
  }
  function copyCard() {
    navigator.clipboard?.writeText(`${a.business_name} ${phone || ''}\n\n${a.call_card || ''}`).then(() => { setCopied(true); setTimeout(() => setCopied(false), 1600); }).catch(() => {});
  }

  return (
    <AppShell profile={profile} alert={a.status === 'replied'}>
      <Link to="/leads" style={{ fontSize: 14, textDecoration: 'none' }}>Back to leads</Link>
      <div style={{ display: 'flex', flexWrap: 'wrap', alignItems: 'flex-start', gap: '16px 24px', marginTop: 14 }}>
        <div style={{ flex: '1 1 420px', minWidth: 0 }}>
          <div style={{ display: 'flex', flexWrap: 'wrap', alignItems: 'center', gap: 10 }}>
            <h1 style={{ margin: 0, fontSize: 32, fontWeight: 600 }}>{a.business_name}</h1>
            {a.tier && <Chip text={'Tier ' + a.tier} bg="rgba(95,212,234,.16)" color={C.cyan} />}
            <Chip text={STAGE_LABEL[a.status] || 'New lead'} bg={st.bg} color={st.color} />
          </div>
          <div style={{ fontSize: 15, color: C.muted, marginTop: 6 }}>{[a.niche, [a.city, a.state].filter(Boolean).join(', '), a.source ? 'found by ' + a.source : ''].filter(Boolean).join(' · ')}</div>
        </div>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 10, position: 'relative' }}>
          {phoneHref && <a href={phoneHref} style={{ display: 'inline-flex', alignItems: 'center', minHeight: 44, padding: '0 18px', borderRadius: 8, background: C.amber, color: '#1A1206', textDecoration: 'none', fontWeight: 600, fontSize: 15 }}>Call {phone}</a>}
          <button type="button" aria-label="More actions" onClick={() => { setMore(!more); setConfirm(''); }} style={{ minWidth: 44, minHeight: 44, borderRadius: 8, border: `1px solid ${C.line2}`, background: 'transparent', color: C.text, fontSize: 20, cursor: 'pointer' }}>···</button>
          {more && (
            <div style={{ position: 'absolute', right: 0, top: 52, zIndex: 5, width: 280, border: `1px solid ${C.line2}`, background: '#0A1626', borderRadius: 10, padding: 6 }}>
              <button type="button" disabled={busy} onClick={() => setConfirm('delete')} style={{ display: 'block', width: '100%', textAlign: 'left', minHeight: 44, padding: '0 12px', border: 0, borderRadius: 6, background: 'transparent', color: C.text, font: `500 14px 'Space Grotesk'`, cursor: 'pointer' }}>Delete lead</button>
              <button type="button" disabled={busy} onClick={() => setConfirm('dnc')} style={{ display: 'block', width: '100%', textAlign: 'left', minHeight: 44, padding: '0 12px', border: 0, borderRadius: 6, background: 'transparent', color: C.red, font: `500 14px 'Space Grotesk'`, cursor: 'pointer' }}>Do not contact</button>
              {confirm === 'delete' && <div style={{ borderTop: `1px solid ${C.line}`, marginTop: 6, padding: 12, fontSize: 13, color: C.soft }}>Delete {a.business_name} and its whole history? This can't be undone.<button type="button" onClick={doDelete} disabled={busy} style={{ display: 'block', marginTop: 10, minHeight: 40, padding: '0 14px', borderRadius: 8, border: 0, background: C.red, color: '#1A0806', fontWeight: 600, cursor: 'pointer' }}>Delete</button></div>}
              {confirm === 'dnc' && <div style={{ borderTop: `1px solid ${C.line}`, marginTop: 6, padding: 12, fontSize: 13, color: C.soft }}>Never contact {a.business_name} again? This can't be undone in the app.<button type="button" onClick={doDnc} disabled={busy} style={{ display: 'block', marginTop: 10, minHeight: 40, padding: '0 14px', borderRadius: 8, border: 0, background: C.red, color: '#1A0806', fontWeight: 600, cursor: 'pointer' }}>Do not contact</button></div>}
            </div>
          )}
        </div>
      </div>
      {confirm && confirm !== 'delete' && confirm !== 'dnc' && <div role="status" style={{ marginTop: 12, color: C.soft }}>{confirm}</div>}

      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 20, marginTop: 22, alignItems: 'flex-start' }}>
        <div style={{ flex: '1 1 360px', minWidth: 0, display: 'flex', flexDirection: 'column', gap: 16 }}>
          <section aria-label="Scores" style={panel}>
            <div style={label}>SCORES</div>
            {scores.map(([t, v]) => (
              <div key={t} style={{ marginTop: 12 }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 14 }}><span>{t}</span><span style={{ fontFamily: MONO, color: (v || 0) >= 4 ? C.cyan : C.amber }}>{v ?? '-'} / 5</span></div>
                <div style={{ height: 6, borderRadius: 3, background: '#142233', marginTop: 6, overflow: 'hidden' }}><div className="hq-barx" style={{ height: '100%', width: `${((Number(v) || 0) / 5) * 100}%`, background: (v || 0) >= 4 ? C.cyan : C.amber }} /></div>
              </div>
            ))}
          </section>
          <section aria-label="Contact" style={{ ...panel, fontSize: 14, lineHeight: 1.6 }}>
            <div style={label}>CONTACT</div>
            <div style={{ marginTop: 10 }}>{phoneHref ? <a href={phoneHref}>{phone}</a> : 'No phone found'}</div>
            {phoneExtra && <div style={{ fontSize: 12, color: C.faint, lineHeight: 1.5 }}>{phoneExtra}</div>}
            <div>{email || 'No email'} {a.email_status && <Chip text={a.email_status} bg={isReady(a.email_status) ? 'rgba(95,224,180,.14)' : 'rgba(148,167,186,.14)'} color={isReady(a.email_status) ? C.green : C.soft} />}</div>
            {emailExtra && <div style={{ fontSize: 12, color: C.faint, lineHeight: 1.5 }}>{emailExtra}</div>}
            <div style={{ marginTop: 8 }}>Owner: <span style={{ color: a.owner_name && !/not found|confirm/i.test(a.owner_name) ? C.text : C.amber }}>{a.owner_name || 'not found'}</span>{a.owner_source_url && <> · <a href={a.owner_source_url} target="_blank" rel="noopener noreferrer">source</a></>}</div>
            <div>Email allowed: {a.email_allowed || 'unknown'} · Calls allowed: {a.call_allowed || 'unknown'}</div>
            {a.channel_reason && <div style={{ color: C.muted }}>{a.channel_reason}</div>}
            <div style={{ display: 'flex', gap: 14, marginTop: 6 }}>
              {a.owner_linkedin_url && <a href={a.owner_linkedin_url} target="_blank" rel="noopener noreferrer">Owner on LinkedIn</a>}
              {a.company_linkedin_url && <a href={a.company_linkedin_url} target="_blank" rel="noopener noreferrer">Company on LinkedIn</a>}
              {a.website && <a href={a.website.startsWith('http') ? a.website : 'https://' + a.website} target="_blank" rel="noopener noreferrer">Website</a>}
            </div>
          </section>
          <section aria-label="Signals" style={panel}>
            <div style={label}>SIGNALS</div>
            {parseSignals(a.signals).length === 0 && <div style={{ marginTop: 10, color: C.muted, fontSize: 14 }}>No signals saved.</div>}
            {parseSignals(a.signals).map((s, i) => (
              <div key={i} style={{ display: 'flex', gap: 10, marginTop: 12, fontSize: 14, lineHeight: 1.45 }}>
                <span style={{ flex: 'none', width: 7, height: 7, borderRadius: '50%', marginTop: 7, background: C.cyan }} />
                <div><div>{s.label}</div>{s.url && <a href={s.url} target="_blank" rel="noopener noreferrer" style={{ fontSize: 12 }}>source</a>}</div>
              </div>
            ))}
          </section>
        </div>

        <div style={{ flex: '1.3 1 440px', minWidth: 0, display: 'flex', flexDirection: 'column', gap: 16 }}>
          <section aria-label="Outreach plan" style={panel}>
            <div style={label}>OUTREACH PLAN</div>
            {plan.length === 0 && <div style={{ marginTop: 10, color: C.muted, fontSize: 14 }}>No plan yet. It's written when you approve a campaign with this lead in it.</div>}
            <div style={{ marginTop: 12 }}>
              {plan.map((t) => {
                const kind = t.status === 'cancelled' ? 'cancelled' : (t.status === 'sent' || t.status === 'logged') ? 'done' : (t.due_date && t.due_date < today) ? 'overdue' : (t.due_date === today) ? 'due' : 'upcoming';
                const col = { done: C.green, due: C.amber, overdue: C.red, upcoming: C.cyan, cancelled: C.dim }[kind];
                const tag = { done: 'DONE', due: 'DUE TODAY', overdue: 'OVERDUE', upcoming: 'UPCOMING', cancelled: 'CANCELLED' }[kind];
                return (
                  <div key={t.id} style={{ display: 'flex', gap: 14 }}>
                    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', flex: 'none' }}>
                      <span style={{ width: 14, height: 14, borderRadius: '50%', border: `2px solid ${col}`, background: kind === 'cancelled' || kind === 'upcoming' ? 'transparent' : col }} />
                      <span style={{ width: 2, height: 34, background: C.line }} />
                    </div>
                    <div style={{ flex: 1, minWidth: 0, paddingBottom: 8 }}>
                      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px 12px', alignItems: 'baseline' }}>
                        <span style={{ fontSize: 15, fontWeight: 500, textTransform: 'capitalize', textDecoration: kind === 'cancelled' ? 'line-through' : 'none', color: kind === 'cancelled' ? C.faint : C.text }}>{t.step}</span>
                        <span style={{ fontFamily: MONO, fontSize: 12, color: C.faint }}>{t.due_date || ''}</span>
                        <Chip text={tag} bg="rgba(148,167,186,.12)" color={col} />
                      </div>
                      <div style={{ fontSize: 13, color: C.muted, marginTop: 2 }}>{t.status === 'cancelled' ? (t.cancelled_reason || 'cancelled') : (t.summary || (t.gate_result ? 'Gate: ' + t.gate_result : ''))}</div>
                    </div>
                  </div>
                );
              })}
            </div>
          </section>
          <section aria-label="Call card" style={{ border: '1px solid #6B5320', background: 'linear-gradient(180deg,rgba(245,183,74,.10),rgba(245,183,74,.02))', borderRadius: 12, padding: 18 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
              <div style={{ fontFamily: MONO, fontSize: 12, letterSpacing: '.18em', color: C.amber }}>CALL CARD{a.call_card_date ? ' · ' + a.call_card_date : ''}</div>
              {a.call_card && <button type="button" onClick={copyCard} style={{ marginLeft: 'auto', minHeight: 40, padding: '0 14px', borderRadius: 8, border: '1px solid #6B5320', background: 'transparent', color: C.amber, font: `500 13px 'Space Grotesk'`, cursor: 'pointer' }}>{copied ? 'Copied' : 'Copy card'}</button>}
            </div>
            <div style={{ marginTop: 12, fontSize: 14, lineHeight: 1.6, color: '#DCE6EF', whiteSpace: 'pre-wrap' }}>{a.call_card || 'No call card yet. Ask Jarvis: "Prepare a call card for ' + a.business_name + '."'}</div>
          </section>
          <section aria-label="Timeline" style={panel}>
            <div style={label}>TIMELINE</div>
            {timeline.length === 0 && <div style={{ marginTop: 10, color: C.muted, fontSize: 14 }}>Nothing yet.</div>}
            {timeline.map((t) => (
              <details key={t.id} style={{ borderBottom: '1px solid #12202F', padding: '12px 0' }}>
                <summary style={{ cursor: 'pointer', listStyle: 'none' }}>
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px 10px', alignItems: 'baseline' }}>
                    <span style={{ fontFamily: MONO, fontSize: 11, letterSpacing: '.12em', color: t.direction === 'in' ? C.amber : C.cyan, textTransform: 'uppercase' }}>{t.direction === 'in' ? 'reply' : (t.step || t.channel || 'note')}</span>
                    {t.status === 'draft' && <Chip text="Draft" bg="rgba(245,183,74,.14)" color={C.amber} />}
                    <span style={{ fontFamily: MONO, fontSize: 11, color: C.faint }}>{t.date || ''}</span>
                    {t.gate_result && <span style={{ fontFamily: MONO, fontSize: 11, color: C.dim, marginLeft: 'auto' }}>GATE: {String(t.gate_result).toUpperCase()}</span>}
                  </div>
                  <div style={{ fontSize: 14, color: '#DCE6EF', marginTop: 4, lineHeight: 1.5 }}>{t.summary || t.outcome || ''}</div>
                </summary>
                {t.full_text && <div style={{ marginTop: 8, fontSize: 14, color: C.soft, whiteSpace: 'pre-wrap', lineHeight: 1.55 }}>{t.full_text}</div>}
              </details>
            ))}
          </section>
        </div>
      </div>
    </AppShell>
  );
}
