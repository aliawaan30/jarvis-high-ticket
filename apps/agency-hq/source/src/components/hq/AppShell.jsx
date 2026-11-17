import React, { useEffect, useState } from 'react';
import { NavLink } from 'react-router-dom';
import HeaderActionsV2 from '@/components/hq/HeaderActionsV2';
import { base44 } from '@/api/base44Client';
import { C, MONO, SANS } from '@/lib/hq';
import './hq.css';

const NAV = [
  ['HUD', '/'], ['Pipeline', '/pipeline'], ['Leads', '/leads'], ['Campaigns', '/campaigns'],
  ['Clients', '/clients'], ['Results', '/results'], ['Settings', '/settings'],
];

export function useProfile() {
  const [profile, setProfile] = useState(null);
  useEffect(() => {
    let on = true;
    base44.entities.Profile.list('-updated_date', 1).then((l) => { if (on) setProfile((l && l[0]) || null); }).catch(() => {});
    return () => { on = false; };
  }, []);
  return profile;
}

export default function AppShell({ children, alert = false, profile }) {
  const [now, setNow] = useState(new Date());
  useEffect(() => { const t = setInterval(() => setNow(new Date()), 1000); return () => clearInterval(t); }, []);
  const goal = profile?.goal_90_day ? String(profile.goal_90_day).trim() : '';
  const dot = alert ? C.amber : C.cyan;
  return (
    <div style={{ minHeight: '100vh', background: `radial-gradient(1200px 700px at 50% 30%, #0D1A2B 0%, ${C.bg} 70%)`, color: C.text, fontFamily: SANS, paddingBottom: 28 }}>
      <header style={{ borderBottom: `1px solid ${C.line}` }}>
        <div className="hq-top" style={{ display: 'flex', flexWrap: 'wrap', alignItems: 'center', gap: '12px 22px', padding: '14px 28px 10px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
            <span className="hq-dot" style={{ width: 8, height: 8, borderRadius: '50%', background: dot, boxShadow: `0 0 10px ${dot}` }} />
            <span style={{ fontSize: 18, fontWeight: 600, letterSpacing: '.32em' }}>J.A.R.V.I.S</span>
          </div>
          <span className="hq-clock" style={{ fontFamily: MONO, fontSize: 15, color: '#8FD9EA' }}>{now.toLocaleTimeString('en-GB', { hour12: false })}</span>
          {goal && <span className="hq-objective" style={{ border: '1px solid #6B5320', background: 'rgba(245,183,74,.08)', color: C.amber, fontFamily: MONO, fontSize: 12, letterSpacing: '.1em', padding: '7px 12px', borderRadius: 6, textTransform: 'uppercase', maxWidth: 360, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }} title={goal}>Objective: {goal}</span>}
          <div className="hq-actions" style={{ marginLeft: 'auto' }}><HeaderActionsV2 voiceProvider={profile?.voice_provider || 'base44'} ownerName={profile?.owner_name || ''} agentGreets={!!profile?.retell_greets} /></div>
        </div>
        <nav aria-label="Agency HQ" className="hq-nav" style={{ display: 'flex', flexWrap: 'wrap', gap: 4, padding: '0 22px 10px' }}>
          {NAV.map(([label, to]) => (
            <NavLink key={to} to={to} end={to === '/'} style={{ textDecoration: 'none', color: C.muted, padding: '8px 14px', borderRadius: 6, fontSize: 14, border: '1px solid transparent' }}>{label}</NavLink>
          ))}
        </nav>
      </header>
      <main className="hq-main" style={{ maxWidth: 1440, margin: '0 auto', padding: '22px 28px 0' }}>{children}</main>
    </div>
  );
}

export const panel = { border: `1px solid ${C.line}`, background: C.panel, borderRadius: 12, padding: 18 };
export const label = { fontFamily: MONO, fontSize: 12, letterSpacing: '.2em', color: C.faint };
export function Chip({ text, bg, color }) {
  return <span style={{ fontFamily: MONO, fontSize: 11, padding: '2px 7px', borderRadius: 4, background: bg, color, whiteSpace: 'nowrap', textTransform: 'uppercase' }}>{text}</span>;
}
export function Empty({ children }) {
  return <div style={{ border: `1px dashed ${C.line}`, borderRadius: 12, padding: 22, color: C.muted, fontSize: 14, lineHeight: 1.6 }}>{children}</div>;
}
