import React, { useCallback, useEffect, useState } from 'react';
import { base44 } from '@/api/base44Client';
import { useAuth } from '@/lib/AuthContext';
import VoiceProviderSetting from '@/components/jarvis/VoiceProviderSetting';
import JarvisAgentSetting from '@/components/jarvis/JarvisAgentSetting';
import AppShell, { panel, label } from '@/components/hq/AppShell';
import { C, useRows } from '@/lib/hq';

const DEFAULT_OPT_OUT = "Not interested? Reply no thanks and I won't email again.";

function Row({ title, note, value, placeholder, onSave, canEdit, readOnly, suffix }) {
  const [v, setV] = useState(value ?? '');
  const [state, setState] = useState('');
  useEffect(() => { setV(value ?? ''); }, [value]);
  const dirty = String(v ?? '') !== String(value ?? '');
  async function save() {
    setState('saving');
    const ok = await onSave(v);
    setState(ok ? 'saved' : 'error');
    if (ok) setTimeout(() => setState(''), 1600);
  }
  return (
    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '6px 16px', padding: '14px 0', borderBottom: '1px solid #12202F' }}>
      <div className="hq-row-label" style={{ width: 200, flex: 'none', fontSize: 14, color: C.muted, paddingTop: readOnly ? 0 : 12 }}>{title}</div>
      <div style={{ flex: 1, minWidth: 0 }}>
        {readOnly ? <div style={{ fontSize: 14 }}>{value || <span style={{ color: C.muted }}>{placeholder}</span>}</div> : (
          <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
            <input value={v} placeholder={placeholder} disabled={!canEdit} onChange={(e) => setV(e.target.value)} onKeyDown={(e) => { if (e.key === 'Enter' && dirty) save(); }}
              style={{ flex: 1, minWidth: 0, minHeight: 44, padding: '0 12px', borderRadius: 8, border: `1px solid ${C.line2}`, background: '#0A1626', color: C.text, font: "400 14px 'Space Grotesk', sans-serif" }} />
            {suffix && <span style={{ fontSize: 13, color: C.muted }}>{suffix}</span>}
            <button type="button" onClick={save} disabled={!canEdit || !dirty || state === 'saving'} style={{ minHeight: 44, padding: '0 16px', borderRadius: 8, border: `1px solid ${C.line2}`, background: 'transparent', color: dirty ? C.text : C.dim, font: "500 13px 'Space Grotesk', sans-serif", cursor: dirty ? 'pointer' : 'default' }}>{state === 'saving' ? 'Saving' : state === 'saved' ? 'Saved' : 'Save'}</button>
          </div>
        )}
        {state === 'error' && <div style={{ fontSize: 12, color: C.red, marginTop: 4 }}>Could not save. Try again.</div>}
        {note && <div style={{ fontSize: 12, color: C.faint, marginTop: 6, lineHeight: 1.5 }}>{note}</div>}
      </div>
    </div>
  );
}

export default function Settings() {
  const { isAuthenticated, user } = useAuth();
  const canEdit = isAuthenticated && user?.role === 'admin';
  const [profile, setProfile] = useState(null);
  const [loaded, setLoaded] = useState(false);
  const [error, setError] = useState('');
  const settings = useRows('AgencySettings', '-updated_date', 1, 60000);
  const accounts = useRows('Account', '-updated_date', 500, 60000);
  const s = settings.rows[0] || {};

  const loadProfile = useCallback(async () => {
    try { const list = await base44.entities.Profile.list('-updated_date', 1); setProfile(list[0] || null); } catch { /* best effort */ }
    setLoaded(true);
  }, []);
  useEffect(() => { loadProfile(); }, [loadProfile]);

  // Used by the agent and voice settings (unchanged components).
  const onSaveProfile = useCallback(async (update) => {
    if (!canEdit) return profile;
    try {
      const fields = update || {};
      if (profile?.id) { if (Object.keys(fields).length) await base44.entities.Profile.update(profile.id, fields); }
      else if (Object.keys(fields).length) { await base44.entities.Profile.create(fields); }
      const list = await base44.entities.Profile.list('-updated_date', 1);
      setProfile(list[0] || null);
      return list[0] || null;
    } catch { setError('Could not save that setting.'); return profile; }
  }, [canEdit, profile]);

  async function saveSetting(field, value) {
    try {
      if (s.id) await base44.entities.AgencySettings.update(s.id, { [field]: value });
      else await base44.entities.AgencySettings.create({ [field]: value });
      await settings.reload();
      return true;
    } catch { return false; }
  }
  const num = (v) => { const n = Number(String(v).replace(/[^0-9.]/g, '')); return Number.isFinite(n) && String(v).trim() !== '' ? n : null; };
  const dnc = accounts.rows.filter((a) => a.status === 'do not contact');
  const dncDomains = String(s.do_not_contact || '').split(/[\n,]/).map((x) => x.trim()).filter(Boolean);

  return (
    <AppShell profile={profile}>
      <div style={label}>SETTINGS</div>
      <h1 style={{ margin: '6px 0 0', fontSize: 30, fontWeight: 600 }}>Settings</h1>
      {error && <div style={{ marginTop: 12, color: C.red }}>{error}</div>}
      {!canEdit && loaded && <div style={{ marginTop: 12, color: C.muted }}>Sign in as the owner to change settings.</div>}

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(min(440px, 100%), 1fr))', gap: 18, marginTop: 20 }}>
        <section aria-label="Sending" style={panel}>
          <div style={label}>SENDING</div>
          <Row title="Inbox" readOnly value={s.inbox_email} placeholder="Not connected yet. Ask Jarvis: connect my Gmail." note="Connected through Jarvis. A test email confirms the From address." />
          <Row title="Daily cap" value={s.daily_cap ?? 10} canEdit={canEdit} suffix="a day" note="Start at 10, never more than 15 on Gmail. Follow ups go first. More needs Instantly." onSave={(v) => { const n = num(v); return n === null ? Promise.resolve(false) : saveSetting('daily_cap', Math.min(15, Math.max(1, n))); }} />
          <Row title="Send window" value={`${s.send_window_start ?? 8} to ${s.send_window_end ?? 17}`} canEdit={canEdit} note="Hours in each lead's own time zone, for example 8 to 17." onSave={(v) => { const m = String(v).match(/(\d{1,2})\D+(\d{1,2})/); if (!m) return Promise.resolve(false); return saveSetting('send_window_start', Number(m[1])).then((ok) => ok && saveSetting('send_window_end', Number(m[2]))); }} />
          <Row title="Send gate" readOnly value="On. Every email is checked before it goes." note="Gate receipts are saved on every sent email." />
        </section>

        <section aria-label="Your details in every email" style={panel}>
          <div style={label}>YOUR DETAILS IN EVERY EMAIL</div>
          <Row title="Postal address" value={s.postal_address} placeholder="Business address, PO box or virtual mailbox" canEdit={canEdit} note="Required by law in cold emails. A PO box or virtual mailbox is fine." onSave={(v) => saveSetting('postal_address', v.trim())} />
          <Row title="Opt out line" value={s.opt_out_line || DEFAULT_OPT_OUT} canEdit={canEdit} onSave={(v) => saveSetting('opt_out_line', v.trim())} />
          <Row title="Booking page" value={s.booking_page} placeholder="https://cal.com/your-name/15min" canEdit={canEdit} note="Optional. Without it, Jarvis offers two times by email." onSave={(v) => saveSetting('booking_page', v.trim())} />
        </section>

        <section aria-label="Jarvis" style={panel}>
          <div style={label}>JARVIS</div>
          <Row title="Goal" value={profile?.goal_90_day} placeholder="$10,000 a month by 1 March 2027" canEdit={canEdit} note="Shown as your objective at the top of every page." onSave={async (v) => { const r = await onSaveProfile({ goal_90_day: v.trim() }); return !!r; }} />
          <Row title="Morning brief" value={s.brief_time || '8:00am, Monday to Friday'} canEdit={canEdit} onSave={(v) => saveSetting('brief_time', v.trim())} />
          <Row title="Working hours" value={s.working_hours || '9am to 6pm, Monday to Friday'} canEdit={canEdit} note="Reply alerts come straight away inside these hours." onSave={(v) => saveSetting('working_hours', v.trim())} />
          <Row title="Paused" readOnly value="Paused workflows stay paused until you say resume." />
          <Row title="Retell public key" value={s.retell_public_key} placeholder="public_key_..." canEdit={canEdit} note="For the live transcript in Retell voice mode. Retell dashboard, API Keys, Public Keys: create one and allow this app's web address. It is safe in the browser." onSave={(v) => saveSetting('retell_public_key', v.trim())} />
        </section>

        <section aria-label="Do not contact" style={panel}>
          <div style={label}>DO NOT CONTACT</div>
          <div style={{ fontSize: 14, color: C.soft, marginTop: 10, lineHeight: 1.5 }}>Leads marked do not contact are never contacted again. This can't be undone in the app.</div>
          {dnc.length === 0 && dncDomains.length === 0 && <div style={{ fontSize: 14, color: C.muted, padding: '14px 0' }}>Nobody on the list.</div>}
          {dnc.map((a) => (<div key={a.id} style={{ display: 'flex', justifyContent: 'space-between', gap: 12, padding: '12px 0', borderBottom: '1px solid #12202F', fontSize: 14 }}><span>{a.business_name}{a.email ? ` (${a.email})` : ''}</span><span style={{ color: C.muted }}>{a.updated_date ? new Date(a.updated_date).toLocaleDateString('en-GB', { day: 'numeric', month: 'short' }) : ''}</span></div>))}
          {dncDomains.map((d) => (<div key={d} style={{ display: 'flex', justifyContent: 'space-between', padding: '12px 0', borderBottom: '1px solid #12202F', fontSize: 14 }}><span>{d}</span><span style={{ color: C.muted }}>whole address or domain</span></div>))}
        </section>
      </div>

      <section aria-label="Jarvis connection" style={{ ...panel, marginTop: 18 }}>
        <div style={label}>JARVIS CONNECTION AND VOICE</div>
        <div className="hq-settings" style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(min(420px, 100%), 1fr))', gap: 18, marginTop: 14 }}>
          <JarvisAgentSetting profile={profile} canEdit={canEdit} loaded={loaded} onSaveProfile={onSaveProfile} />
          <VoiceProviderSetting profile={profile} canEdit={canEdit} loaded={loaded} onSaveProfile={onSaveProfile} />
        </div>
      </section>
    </AppShell>
  );
}
