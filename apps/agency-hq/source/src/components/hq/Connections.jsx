import React, { useCallback, useEffect, useState } from 'react';
import { base44 } from '@/api/base44Client';
import { panel, label } from '@/components/hq/AppShell';
import { C } from '@/lib/hq';

// Settings, Connections: every key in one place. Keys go to the app's locked
// Vault through the connections function and are never shown again, only
// their last 4 characters. Keys already in Base44 Secrets keep working.

const HELP = {
  JARVIS_NATIVE_TOKEN: {
    title: 'Jarvis access',
    what: 'Lets your HUD hand jobs to Jarvis, like a task you give it by voice. Free.',
    steps: ['Open your Jarvis agent, then Settings, then Developer.', 'Click Create access token.', 'Choose One app or Superagent, pick the entry with the Agent badge, choose Full access, then copy it and paste it here.'],
  },
  RETELL_API_KEY: {
    title: 'Live voice (Retell add-on)',
    what: 'A real-time voice call with Jarvis from your HUD, and Jarvis phoning you. Optional. Retell bills by the minute; check their pricing first. Without it, Talk still works with the Base44 voice.',
    steps: ['Sign up at dashboard.retellai.com/?ref=blake9a and add a card.', 'Open Settings, then API Keys, and copy your key.', 'Paste it here, then press Set up my voice. The app builds everything else.'],
  },
  FISH_API_KEY: {
    title: 'Jarvis voice in Base44 mode',
    what: 'Optional. Gives Base44 voice mode the Jarvis voice instead of your browser\u2019s voice.',
    steps: ['Sign up at fish.audio.', 'Open API Keys and copy your key.', 'Paste it here.'],
  },
};

const pill = (kind) => ({
  display: 'inline-block', font: "500 11px 'JetBrains Mono', monospace", letterSpacing: '.12em', padding: '3px 9px', borderRadius: 999,
  color: kind === 'ok' ? C.green : kind === 'warn' ? C.amber : C.muted,
  border: `1px solid ${kind === 'ok' ? 'rgba(95,224,180,.45)' : kind === 'warn' ? 'rgba(245,183,74,.45)' : C.line2}`,
});
const btn = (primary) => ({
  minHeight: 40, padding: '0 14px', borderRadius: 8, cursor: 'pointer', font: "600 13px 'Space Grotesk', sans-serif",
  border: primary ? 'none' : `1px solid ${C.line2}`, background: primary ? C.cyan : 'transparent', color: primary ? '#04131B' : C.text,
});

function StatusPill({ k }) {
  if (!k || k.source === 'none') return <span style={pill('none')}>NOT CONNECTED</span>;
  return <span style={pill('ok')}>{k.source === 'secret' ? 'CONNECTED IN BASE44 SECRETS' : `CONNECTED, ENDS ${k.last4}`}</span>;
}

function Card({ name, status, canEdit, onSaved, children }) {
  const h = HELP[name];
  const [open, setOpen] = useState(false);
  const [v, setV] = useState('');
  const [msg, setMsg] = useState(null);
  async function save() {
    setMsg({ kind: 'busy', text: 'Saving...' });
    let res; try { res = await base44.functions.invoke('connections', { action: 'save', name, value: v.trim() }); } catch (e) { res = e?.response; }
    const d = res?.data || {};
    if (d.ok) { setV(''); setMsg({ kind: 'ok', text: `Saved. Ends ${d.last4}.` }); onSaved(); }
    else setMsg({ kind: 'err', text: d.error && d.error.length > 20 ? d.error : 'Could not save. Copy the key again and paste it with nothing before or after it.' });
  }
  return (
    <div style={{ padding: '16px 0', borderBottom: '1px solid #12202F' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 10, flexWrap: 'wrap' }}>
        <span style={{ fontSize: 15, fontWeight: 600 }}>{h.title}</span>
        <button type="button" aria-expanded={open} aria-label={`What is ${h.title}?`} onClick={() => setOpen(!open)}
          style={{ width: 24, height: 24, borderRadius: '50%', border: `1px solid ${C.line2}`, background: 'transparent', color: C.cyan, cursor: 'pointer', font: "600 13px 'Space Grotesk', sans-serif" }}>?</button>
        <span style={{ flex: 1 }} />
        <StatusPill k={status} />
      </div>
      {open && (
        <div style={{ marginTop: 10, fontSize: 13.5, color: C.soft, lineHeight: 1.55, background: '#0A1626', border: `1px solid ${C.line}`, borderRadius: 10, padding: '12px 14px' }}>
          <div>{h.what}</div>
          <ol style={{ margin: '8px 0 0', paddingLeft: 18 }}>{h.steps.map((s) => <li key={s} style={{ marginBottom: 4 }}>{s}</li>)}</ol>
        </div>
      )}
      <div style={{ display: 'flex', gap: 8, marginTop: 12 }}>
        <input type="password" autoComplete="off" value={v} disabled={!canEdit} onChange={(e) => setV(e.target.value)} onKeyDown={(e) => { if (e.key === 'Enter' && v.trim()) save(); }}
          placeholder={status && status.source !== 'none' ? 'Paste a new key to replace it' : 'Paste the key here'}
          style={{ flex: 1, minWidth: 0, minHeight: 40, padding: '0 12px', borderRadius: 8, border: `1px solid ${C.line2}`, background: '#0A1626', color: C.text, font: "400 14px 'JetBrains Mono', monospace" }} />
        <button type="button" onClick={save} disabled={!canEdit || !v.trim()} style={btn(true)}>Save</button>
      </div>
      {msg && <div style={{ fontSize: 13, marginTop: 8, color: msg.kind === 'err' ? C.red : msg.kind === 'ok' ? C.green : C.muted }}>{msg.text}</div>}
      {children}
    </div>
  );
}

export default function Connections({ canEdit, onVoiceReady }) {
  const [st, setSt] = useState(null);
  const [voiceMsg, setVoiceMsg] = useState(null);
  const [hudMsg, setHudMsg] = useState(null);
  const load = useCallback(async () => {
    let res; try { res = await base44.functions.invoke('connections', { action: 'status' }); } catch (e) { res = e?.response; }
    setSt(res?.data?.ok ? res.data : { error: true });
  }, []);
  useEffect(() => { if (canEdit) load(); }, [canEdit, load]);

  async function copyHudKey() {
    setHudMsg({ kind: 'busy', text: 'Getting it...' });
    let res; try { res = await base44.functions.invoke('connections', { action: 'hud_key_for_jarvis' }); } catch (e) { res = e?.response; }
    const key = res?.data?.hud_key;
    if (!key) { setHudMsg({ kind: 'err', text: 'Could not get it. Try again.' }); return; }
    const text = `Save this as my Agency HQ HUD key, as a secret: ${key}`;
    try { await navigator.clipboard.writeText(text); setHudMsg({ kind: 'ok', text: 'Copied. Paste it into your Jarvis chat and send it. Jarvis saves it as a secret.' }); }
    catch { setHudMsg({ kind: 'ok', text }); }
  }
  async function testRetell() {
    setVoiceMsg({ kind: 'busy', text: 'Checking with Retell...' });
    let res; try { res = await base44.functions.invoke('connections', { action: 'test_retell' }); } catch (e) { res = e?.response; }
    const d = res?.data || {}; setVoiceMsg({ kind: d.ok ? 'ok' : 'err', text: d.message || 'Could not check.' });
  }
  async function setupVoice() {
    setVoiceMsg({ kind: 'busy', text: 'Building your Jarvis voice in Retell. About 20 seconds...' });
    let res; try { res = await base44.functions.invoke('connections', { action: 'setup_voice', origin: window.location.origin, language: navigator.language || 'en-US' }); } catch (e) { res = e?.response; }
    const d = res?.data || {};
    if (d.ok) {
      const extra = (d.warnings || []).join(' ');
      setVoiceMsg({ kind: extra ? 'warn' : 'ok', text: (d.reused ? 'Your Jarvis voice is already set up.' : 'Done. Your Jarvis voice is built and published.') + ' Now choose Retell under Voice below.' + (extra ? ' ' + extra : '') });
      load(); if (onVoiceReady) onVoiceReady();
    } else setVoiceMsg({ kind: 'err', text: d.message || 'Could not set it up. Try again, or send Jarvis a screenshot.' });
  }

  if (!canEdit) return null;
  const k = st?.keys || {};
  const retellReady = k.RETELL_API_KEY && k.RETELL_API_KEY.source !== 'none';
  const color = (m) => (m?.kind === 'err' ? C.red : m?.kind === 'ok' ? C.green : m?.kind === 'warn' ? C.amber : C.muted);
  return (
    <section aria-label="Connections" style={{ ...panel, marginTop: 18 }}>
      <div style={label}>CONNECTIONS</div>
      <div style={{ fontSize: 14, color: C.soft, marginTop: 8, lineHeight: 1.5 }}>Everything your HUD connects to, in one place. Keys are saved securely and never shown again. Press ? on any line for what it is and where to get it.</div>
      {st?.error && <div style={{ marginTop: 12, color: C.red, fontSize: 14 }}>Could not load your connections. Publish the app, then reload this page.</div>}

      <div style={{ padding: '16px 0', borderBottom: '1px solid #12202F' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, flexWrap: 'wrap' }}>
          <span style={{ fontSize: 15, fontWeight: 600 }}>HUD key</span><span style={{ flex: 1 }} /><StatusPill k={k.HUD_KEY} />
        </div>
        <div style={{ fontSize: 13.5, color: C.soft, marginTop: 8, lineHeight: 1.5 }}>Created for you automatically. It lets Jarvis and voice calls write to your HUD safely. Jarvis needs a copy once.</div>
        <div style={{ marginTop: 10 }}><button type="button" onClick={copyHudKey} style={btn(false)}>Copy for Jarvis</button></div>
        {hudMsg && <div style={{ fontSize: 13, marginTop: 8, color: color(hudMsg), wordBreak: 'break-all' }}>{hudMsg.text}</div>}
      </div>

      <Card name="JARVIS_NATIVE_TOKEN" status={k.JARVIS_NATIVE_TOKEN} canEdit={canEdit} onSaved={load} />
      <Card name="RETELL_API_KEY" status={k.RETELL_API_KEY} canEdit={canEdit} onSaved={load}>
        <div style={{ display: 'flex', gap: 8, marginTop: 10, flexWrap: 'wrap' }}>
          <button type="button" onClick={testRetell} disabled={!retellReady} style={btn(false)}>Test key</button>
          <button type="button" onClick={setupVoice} disabled={!retellReady} style={btn(true)}>Set up my voice</button>
          {st?.voice?.agent_id && <span style={{ ...pill('ok'), alignSelf: 'center' }}>VOICE AGENT READY</span>}
        </div>
        {voiceMsg && <div style={{ fontSize: 13, marginTop: 8, color: color(voiceMsg) }}>{voiceMsg.text}</div>}
      </Card>
    </section>
  );
}
