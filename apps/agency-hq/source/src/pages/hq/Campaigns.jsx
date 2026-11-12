import React from 'react';
import { Link, useParams } from 'react-router-dom';
import AppShell, { useProfile, panel, label, Chip, Empty } from '@/components/hq/AppShell';
import { C, MONO, useRows, STAGE_LABEL, statusStyle, todayISO } from '@/lib/hq';

const TH = { textAlign: 'left', fontFamily: MONO, fontSize: 11, letterSpacing: '.14em', color: C.faint, fontWeight: 500, padding: '12px 14px', borderBottom: `1px solid ${C.line}`, whiteSpace: 'nowrap' };
const TD = { padding: '12px 14px', borderBottom: '1px solid #12202F', fontSize: 14, verticalAlign: 'top' };
const ST = { live: ['rgba(95,224,180,.14)', C.green], approved: ['rgba(95,224,180,.14)', C.green], draft: ['rgba(245,183,74,.14)', C.amber], paused: ['rgba(148,167,186,.14)', C.soft], done: ['rgba(148,167,186,.14)', C.soft] };

export default function Campaigns() {
  const profile = useProfile();
  const { rows, loading, error } = useRows('Campaign');
  return (
    <AppShell profile={profile}>
      <div><div style={label}>CAMPAIGNS</div><h1 style={{ margin: '6px 0 0', fontSize: 30, fontWeight: 600 }}>{rows.length} campaigns, {rows.filter((c) => c.status === 'live').length} live</h1></div>
      {error && <div style={{ marginTop: 16, color: C.red }}>{error}</div>}
      {!loading && !error && rows.length === 0 ? <div style={{ marginTop: 18 }}><Empty>No campaigns yet. Once you have leads, ask Jarvis to set up a campaign. You approve it once, and it shows up here.</Empty></div> : (
        <div style={{ overflowX: 'auto', marginTop: 18, border: `1px solid ${C.line}`, borderRadius: 12, background: C.panel }}>
          <table style={{ width: '100%', minWidth: 980, borderCollapse: 'collapse' }}>
            <thead><tr>{['CAMPAIGN', 'STATUS', 'SENT', 'REPLIES', 'BOOKED', 'REPLY RATE', 'APPROVED'].map((h) => <th key={h} style={TH}>{h}</th>)}</tr></thead>
            <tbody>{rows.map((c) => { const s = ST[c.status] || ST.draft; const sent = Number(c.sent) || 0; return (
              <tr key={c.id} className="hq-row">
                <td style={TD}><Link to={`/campaigns/${c.id}`} style={{ fontWeight: 600, textDecoration: 'none' }}>{c.name}</Link>{c.can_pay_rule && <div style={{ fontSize: 12, color: C.muted, marginTop: 2 }}>{c.can_pay_rule}</div>}</td>
                <td style={TD}><Chip text={c.status || 'draft'} bg={s[0]} color={s[1]} /></td>
                <td style={{ ...TD, fontFamily: MONO }}>{sent}</td>
                <td style={{ ...TD, fontFamily: MONO, color: C.cyan }}>{Number(c.replies) || 0}</td>
                <td style={{ ...TD, fontFamily: MONO, color: C.amber }}>{Number(c.booked) || 0}</td>
                <td style={{ ...TD, fontFamily: MONO }}>{sent ? Math.round((Number(c.replies) || 0) / sent * 100) + '%' : 'n/a'}</td>
                <td style={{ ...TD, color: C.muted, whiteSpace: 'nowrap' }}>{c.approved_date || (c.status === 'draft' ? 'Waiting for your OK' : '-')}</td>
              </tr>); })}</tbody>
          </table>
        </div>
      )}
    </AppShell>
  );
}

export function CampaignDetail() {
  const { id } = useParams();
  const profile = useProfile();
  const camps = useRows('Campaign');
  const accounts = useRows('Account');
  const touches = useRows('Touch', '-updated_date', 1000);
  const c = camps.rows.find((x) => x.id === id);
  if (!c) return <AppShell profile={profile}>{camps.loading ? <div style={{ color: C.muted }}>Loading...</div> : <Empty>Campaign not found. <Link to="/campaigns">Back to campaigns</Link></Empty>}</AppShell>;
  const today = todayISO();
  const leads = accounts.rows.filter((a) => a.campaign === c.name);
  const stat = (v, t, col) => <div style={{ border: `1px solid ${C.line}`, borderRadius: 10, padding: '12px 14px' }}><div style={{ fontFamily: MONO, fontSize: 26, color: col }}>{v}</div><div style={{ fontSize: 13, color: C.muted, marginTop: 2 }}>{t}</div></div>;
  return (
    <AppShell profile={profile}>
      <Link to="/campaigns" style={{ fontSize: 14, textDecoration: 'none' }}>Back to campaigns</Link>
      <div style={{ marginTop: 12 }}><div style={label}>CAMPAIGN</div><h1 style={{ margin: '6px 0 0', fontSize: 30, fontWeight: 600 }}>{c.name}</h1></div>
      <section style={{ ...panel, marginTop: 18 }}>
        <div style={{ fontSize: 14, color: C.soft, lineHeight: 1.5 }}>{c.can_pay_rule || 'No rule saved.'}</div>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit,minmax(140px,1fr))', gap: 12, marginTop: 16 }}>
          {stat(leads.length, 'Leads in campaign', C.text)}{stat(Number(c.sent) || 0, 'Emails sent', C.text)}{stat(Number(c.replies) || 0, 'Replies', C.cyan)}{stat(Number(c.booked) || 0, 'Calls booked', C.amber)}{stat(c.daily_limit || 10, 'Daily limit', C.text)}
        </div>
      </section>
      <section style={{ ...panel, marginTop: 18 }}>
        <div style={label}>LEADS IN THIS CAMPAIGN</div>
        {leads.length === 0 ? <div style={{ marginTop: 10, color: C.muted, fontSize: 14 }}>No leads linked to this campaign yet.</div> : (
          <div style={{ overflowX: 'auto', marginTop: 8 }}>
            <table style={{ width: '100%', minWidth: 760, borderCollapse: 'collapse' }}>
              <thead><tr>{['BUSINESS', 'NEXT STEP', 'DUE', 'STATUS'].map((h) => <th key={h} style={TH}>{h}</th>)}</tr></thead>
              <tbody>{leads.map((a) => {
                const next = touches.rows.filter((t) => t.account_id === a.id && t.status === 'planned').sort((x, y) => String(x.due_date).localeCompare(String(y.due_date)))[0];
                const st = statusStyle(a.status);
                return (<tr key={a.id} className="hq-row">
                  <td style={TD}><Link to={`/leads/${a.id}`} style={{ fontWeight: 600, textDecoration: 'none' }}>{a.business_name}</Link></td>
                  <td style={{ ...TD, color: next && next.due_date <= today ? C.amber : C.soft, textTransform: 'capitalize' }}>{a.status === 'replied' ? 'Call now' : (next?.step || '-')}</td>
                  <td style={{ ...TD, color: C.muted }}>{next?.due_date || '-'}</td>
                  <td style={TD}><Chip text={STAGE_LABEL[a.status] || 'New lead'} bg={st.bg} color={st.color} /></td>
                </tr>);
              })}</tbody>
            </table>
          </div>
        )}
      </section>
    </AppShell>
  );
}
