import React, { useEffect, useRef, useState } from 'react';
import { base44 } from '@/api/base44Client';
import VoiceStage, { primeVoice, prewarmRetellCall } from '@/components/hq/VoiceStage';
import { C, MONO } from '@/lib/hq';

// Same backend calls as the classic HeaderActions (callMe, callMeRetell, callStatus, TalkPanel),
// restyled for Agency HQ v2. Settings lives in the main menu, so it is not repeated here.
const POLL_MS = 3000, MAX_POLL_MS = 180000, IN_FLIGHT_MS = 10000, TOAST_MS = 5000;

export default function HeaderActionsV2({ voiceProvider = 'base44', ownerName = '', agentGreets = false }) {
  const [calling, setCalling] = useState(false);
  const [talkOpen, setTalkOpen] = useState(false);
  const [toast, setToast] = useState(null);
  const [telegramUrl, setTelegramUrl] = useState('');
  const pending = useRef(false), mounted = useRef(true), t = useRef(null), pollT = useRef(null), flightT = useRef(null);

  useEffect(() => {
    let on = true;
    base44.entities.Profile.list('-updated_date', 1).then((l) => { if (on) setTelegramUrl((l && l[0] && l[0].telegram_url) || ''); }).catch(() => {});
    return () => { on = false; };
  }, []);
  useEffect(() => { mounted.current = true; return () => { mounted.current = false; [t, pollT, flightT].forEach((r) => r.current && clearTimeout(r.current)); }; }, []);

  const show = (msg, red = false) => { if (!mounted.current) return; setToast({ msg, red }); if (t.current) clearTimeout(t.current); t.current = setTimeout(() => mounted.current && setToast(null), TOAST_MS); };
  const release = () => { if (flightT.current) clearTimeout(flightT.current); flightT.current = null; pending.current = false; if (mounted.current) setCalling(false); };
  const start = () => { pending.current = true; setCalling(true); if (flightT.current) clearTimeout(flightT.current); flightT.current = setTimeout(release, IN_FLIGHT_MS); };

  const poll = async (requestId) => {
    const began = Date.now();
    while (Date.now() - began < MAX_POLL_MS) {
      await new Promise((r) => { pollT.current = setTimeout(r, POLL_MS); });
      if (!mounted.current) return;
      let res, data;
      try { res = await base44.functions.invoke('callStatus', { request_id: requestId }); data = res?.data; } catch (e) { res = e?.response; data = res?.data; }
      if (!mounted.current) return;
      if (data?.state === 'submitted') return show('Call request sent to Jarvis.');
      if (data?.state === 'failed') return show('Call request was not accepted. Check the call service.', true);
      if (data?.state === 'unknown' || res?.status === 409) return show('A call is already in progress.');
      if (res?.status === 401) return show('Sign in to check call status.', true);
      if (res?.status === 403) return show('Admin only.', true);
    }
  };

  const callMe = async () => {
    if (pending.current || !mounted.current) return;
    start(); show('Requesting a call...');
    try {
      if (voiceProvider === 'retell') {
        let res; try { res = await base44.functions.invoke('callMeRetell', {}); } catch (e) { res = e?.response; }
        if (!mounted.current) return; release();
        const data = res?.data;
        if (res?.status === 202 && data?.call_id) return show('Retell call started.');
        if (res?.status === 409) return show('A call is already in progress.');
        return show(data?.message || 'Retell call could not be started. Try again.', true);
      }
      let res; try { res = await base44.functions.invoke('callMe', {}); } catch (e) { res = e?.response; }
      if (!mounted.current) return;
      const data = res?.data; release();
      if (res?.status === 202 && data?.request_id) { show('Call request queued. Jarvis is preparing your call.'); poll(data.request_id); return; }
      if (res?.status === 409) return show('A call is already in progress.');
      if (res?.status === 401) return show('Sign in to call.', true);
      if (res?.status === 403) return show('Admin only.', true);
      show(data?.message || 'Jarvis call service is unavailable. Try again later.', true);
    } catch { release(); show('Call request failed. Try again.', true); }
  };

  const btn = { display: 'inline-flex', alignItems: 'center', gap: 8, minHeight: 40, padding: '0 14px', borderRadius: 20, border: `1px solid ${C.line2}`, background: 'rgba(13,26,43,.8)', color: C.text, font: "500 13px 'Space Grotesk', sans-serif", cursor: 'pointer' };
  return (
    <div style={{ position: 'relative', display: 'flex', alignItems: 'center', gap: 8 }}>
      <button type="button" className="hq-btn" onPointerEnter={() => { if (voiceProvider === 'retell') prewarmRetellCall(); }} onClick={() => { primeVoice(); setTalkOpen(true); }} aria-label="Talk to Jarvis" style={btn}>
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3" /><path d="M5 11a7 7 0 0 0 14 0M12 18v3" /></svg>
        <span className="hq-act-label">Talk</span>
      </button>
      <button type="button" className="hq-btn" onClick={callMe} disabled={calling} aria-label="Call me" style={{ ...btn, opacity: calling ? 0.6 : 1 }}>
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z" /></svg>
        <span className="hq-act-label">{calling ? 'Calling...' : 'Call me'}</span>
      </button>
      {telegramUrl && <button type="button" className="hq-btn" onClick={() => window.open(telegramUrl, '_blank', 'noopener,noreferrer')} style={btn}>Text</button>}
      <VoiceStage open={talkOpen} onClose={() => setTalkOpen(false)} voiceProvider={voiceProvider} ownerName={ownerName} agentGreets={agentGreets} />
      <div aria-live="polite" style={{ position: 'absolute', right: 0, top: '100%', marginTop: 8, zIndex: 50, pointerEvents: 'none' }}>
        {toast && <div style={{ maxWidth: 320, fontFamily: MONO, fontSize: 12, background: '#0A1626', border: `1px solid ${toast.red ? 'rgba(240,140,130,.5)' : C.line2}`, color: toast.red ? C.red : C.text, borderRadius: 8, padding: '8px 12px' }}>{toast.msg}</div>}
      </div>
    </div>
  );
}
