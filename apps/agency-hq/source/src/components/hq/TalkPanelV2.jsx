import '@/components/hq/hq.css';
import React, { useEffect, useRef, useState } from 'react';
import { base44 } from '@/api/base44Client';
import { HUD } from '@/lib/jarvis';

// Talk to Jarvis out loud from the dashboard.
// Retell owners: a live web call with the real Jarvis voice, no phone needed.
// Base44 owners: free push to talk. The browser hears the owner, the message
// goes to their own Jarvis, and the reply is read aloud by the browser voice.

const POLL_MS = 1200;
const MAX_WAIT_MS = 180_000;
const btn = 'font-mono text-[10px] tracking-[0.18em] uppercase px-3 py-2 border border-hud-border bg-transparent text-hud-text2 hover:bg-hud-panel hover:text-hud-text transition-colors duration-200 focus:outline-none focus-visible:border-hud-accent disabled:opacity-50';
const btnMain = 'font-mono text-[11px] tracking-[0.2em] uppercase px-5 py-3 border border-hud-accent text-hud-text bg-transparent hover:bg-hud-panel transition-colors duration-200 focus:outline-none focus-visible:border-hud-text disabled:opacity-50';

const STATUS_LABEL = {
  idle: 'Ready',
  connecting: 'Connecting…',
  listening: 'Listening…',
  thinking: 'Jarvis is thinking…',
  speaking: 'Jarvis is speaking',
  live: 'Live, just talk',
  ended: 'Chat ended',
  error: 'Something went wrong',
};

function getRecognition() {
  if (typeof window === 'undefined') return null;
  return window.SpeechRecognition || window.webkitSpeechRecognition || null;
}

// Clean text for the browser voice: no markdown, no links read out letter by letter.
function forSpeech(text) {
  let t = String(text || '');
  t = t.replace(/```[\s\S]*?```/g, ' ');
  t = t.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1');
  t = t.replace(/https?:\/\/\S+/g, 'the link in your chat');
  t = t.replace(/[*_#>`|~]/g, ' ');
  t = t.replace(/^\s*[-•]\s+/gm, '');
  t = t.replace(/\s+/g, ' ').trim();
  return t.length > 700 ? t.slice(0, 700).replace(/\s\S*$/, '') + '. The rest is on screen.' : t;
}

// Light cleanup for the on-screen text: keep the words and links, drop markdown marks.
function forScreen(text) {
  return String(text || '').replace(/\*\*|__|`/g, '').replace(/^#+\s*/gm, '').trim();
}

function pickVoice() {
  if (typeof window === 'undefined' || !window.speechSynthesis) return null;
  const all = window.speechSynthesis.getVoices() || [];
  // Voices installed on the device play reliably; online voices can fail silently.
  const local = all.filter((x) => x.localService);
  const pools = [local, all];
  const prefer = ['Daniel', 'Arthur', 'Oliver', 'Microsoft Ryan', 'Microsoft George', 'Google UK English Male'];
  for (const voices of pools) {
    for (const name of prefer) {
      const v = voices.find((x) => x.name && x.name.includes(name));
      if (v) return v;
    }
    const en = voices.find((x) => /^en(-|_)GB/i.test(x.lang)) || voices.find((x) => /^en/i.test(x.lang));
    if (en) return en;
  }
  return null;
}

// Instant spoken acknowledgment while full Jarvis works on the real answer.
// It must fit what was asked: small talk gets a friendly "one sec", only real
// data questions get "let me check your CRM".
function ackFor(text) {
  const t = String(text || '').toLowerCase().replace(/[’']/g, "'");
  const task = /\b(find|get|search|look for|pull|add|create|update|mark|move|change|set|log|book|delete|remove|schedule|remind|draft|write|send|email|call card|proposal)\b/;
  const data = /\b(leads?|pipeline|crm|status|repl(y|ies)|deals?|clients?|campaigns?|numbers|missions?|due|how many|how far|goal|revenue|booked|what should i (do|focus)|what's (on|next)|plan for today)\b/;
  if (/\b(find|get|search|look for|pull)\b.*\b(leads?|businesses|companies|plumb\w*|hvac|prospects?)\b/.test(t)) return "On it. I'm finding them now, and they'll show up in your pipeline as I save them.";
  if (/\b(draft|write|email|message|text|call card|proposal)\b/.test(t)) return "Sure, I'm writing that now. One moment.";
  if (/\b(add|create|update|mark|move|change|set|log|book|delete|remove|schedule|remind)\b/.test(t)) return "On it. Give me a few seconds.";
  if (data.test(t)) return "Let me check your CRM. Give me a few seconds for the accurate numbers.";
  if (!task.test(t) && /\b(thanks|thank you|cheers)\b/.test(t)) return "Anytime. One sec.";
  if (!task.test(t) && /\b(hey|hi|hello|yo|morning|afternoon|evening|how are you|how's it going|how is it going|what's up)\b/.test(t)) return "Hey! Give me a second.";
  return "One sec.";
}

function errorMessage(e, fallback) {
  const data = e?.response?.data || e?.data;
  return (data && data.message) || fallback;
}

export default function TalkPanelV2({ open, onClose, voiceProvider = 'base44' }) {
  const useRetell = voiceProvider === 'retell';
  const [status, setStatus] = useState('idle');
  const [lines, setLines] = useState([]);
  const [note, setNote] = useState('');
  const [typed, setTyped] = useState('');
  const [handsFree, setHandsFree] = useState(true);
  const [autoSend, setAutoSend] = useState(false);
  const autoSendRef = useRef(false);
  const conversationRef = useRef('');
  const retellRef = useRef(null);
  const recRef = useRef(null);
  const aliveRef = useRef(true);
  const busyRef = useRef(false);
  const spokeLastRef = useRef(false);
  const handsFreeRef = useRef(true);
  const listRef = useRef(null);
  const Recognition = getRecognition();

  useEffect(() => { handsFreeRef.current = handsFree; }, [handsFree]);
  useEffect(() => { autoSendRef.current = autoSend; }, [autoSend]);
  useEffect(() => { aliveRef.current = true; return () => { aliveRef.current = false; stopAll(); }; }, []);
  useEffect(() => { if (!open) stopAll(); }, [open]);
  useEffect(() => { if (listRef.current) listRef.current.scrollTop = listRef.current.scrollHeight; }, [lines]);
  useEffect(() => {
    if (typeof window === 'undefined' || !window.speechSynthesis) return undefined;
    const warm = () => window.speechSynthesis.getVoices();
    warm();
    window.speechSynthesis.addEventListener?.('voiceschanged', warm);
    return () => window.speechSynthesis.removeEventListener?.('voiceschanged', warm);
  }, []);

  function stopAll() {
    try { recRef.current?.abort(); } catch { /* not listening */ }
    recRef.current = null;
    try { window.speechSynthesis?.cancel(); } catch { /* nothing playing */ }
    if (retellRef.current) {
      try { retellRef.current.stopCall(); } catch { /* already ended */ }
      retellRef.current = null;
    }
    busyRef.current = false;
    if (aliveRef.current) setStatus((s) => (s === 'error' ? s : 'idle'));
  }

  const addLine = (who, text) => setLines((prev) => [...prev, { who, text }]);

  // ---------------------------------------------------------------- Retell
  async function startRetell() {
    setNote('');
    setStatus('connecting');
    let token;
    try {
      const res = await base44.functions.invoke('talkStart', {});
      token = res?.data?.access_token;
      if (!token) throw new Error('no_token');
    } catch (e) {
      setStatus('error');
      setNote(errorMessage(e, 'The voice chat could not be started. Try again.'));
      return;
    }
    try {
      const { RetellWebClient } = await import('retell-client-js-sdk');
      const client = new RetellWebClient();
      retellRef.current = client;
      client.on('call_started', () => aliveRef.current && setStatus('live'));
      client.on('agent_start_talking', () => aliveRef.current && setStatus('speaking'));
      client.on('agent_stop_talking', () => aliveRef.current && setStatus('live'));
      client.on('update', (update) => {
        if (!aliveRef.current || !Array.isArray(update?.transcript)) return;
        setLines(update.transcript
          .filter((t) => (t.role === 'agent' || t.role === 'user') && t.content)
          .map((t) => ({ who: t.role === 'agent' ? 'jarvis' : 'you', text: t.content })));
      });
      client.on('call_ended', () => {
        retellRef.current = null;
        if (!aliveRef.current) return;
        setStatus('ended');
        setNote('Anything you agreed on is picked up from the transcript within about five minutes, same as a phone call.');
      });
      client.on('error', () => {
        try { client.stopCall(); } catch { /* ignore */ }
        retellRef.current = null;
        if (!aliveRef.current) return;
        setStatus('error');
        setNote('The voice chat dropped. Check your microphone permission and try again.');
      });
      await client.startCall({ accessToken: token });
    } catch {
      retellRef.current = null;
      setStatus('error');
      setNote('Your browser blocked the microphone, or the voice service did not load. Allow the microphone and try again.');
    }
  }

  function endRetell() {
    if (retellRef.current) {
      try { retellRef.current.stopCall(); } catch { /* ignore */ }
    }
  }

  // ---------------------------------------------------------------- Base44
  // Safari (Mac and every iPhone) only lets a page speak after a tap has
  // unlocked audio. Call this inside every tap handler (Talk, Send, typing).
  const unlockedRef = useRef(false);
  function unlockSpeech() {
    const synth = typeof window !== 'undefined' ? window.speechSynthesis : null;
    if (!synth || unlockedRef.current || typeof SpeechSynthesisUtterance === 'undefined') return;
    try {
      const u = new SpeechSynthesisUtterance(' ');
      u.volume = 0;
      synth.speak(u);
      unlockedRef.current = true;
    } catch { /* speaking stays best effort */ }
  }

  // Safari can swallow an utterance spoken straight after cancel(): wait a beat.
  function sayNow(u) {
    const synth = window.speechSynthesis;
    try { synth.cancel(); } catch { /* ignore */ }
    setTimeout(() => { try { synth.resume(); synth.speak(u); } catch { /* ignore */ } }, 120);
  }

  function speakAck(text) {
    const synth = typeof window !== 'undefined' ? window.speechSynthesis : null;
    if (!synth || typeof SpeechSynthesisUtterance === 'undefined') return;
    const u = new SpeechSynthesisUtterance(text);
    const v = pickVoice();
    if (v) { u.voice = v; u.lang = v.lang; }
    u.rate = 1.05;
    sayNow(u);
  }

  function speak(text) {
    const synth = typeof window !== 'undefined' ? window.speechSynthesis : null;
    const spoken = forSpeech(text);
    if (!synth || !spoken || typeof SpeechSynthesisUtterance === 'undefined') { afterSpeaking(); return; }
    // Chrome stops long utterances after about 15 seconds: speak sentence by sentence.
    const parts = (spoken.match(/[^.!?]+[.!?]*\s*/g) || [spoken]).reduce((acc, p) => {
      const last = acc[acc.length - 1];
      if (last && (last + p).length < 180) acc[acc.length - 1] = last + p; else acc.push(p);
      return acc;
    }, []).map((p) => p.trim()).filter(Boolean);
    const v = pickVoice();
    let i = 0;
    let done = false;
    let started = false;
    const finish = (failed) => {
      if (done) return; done = true; clearTimeout(safety);
      if (failed && !started) {
        if (aliveRef.current) { setStatus('idle'); setNote(`I answered on screen, but this browser didn't play my voice (${failed}). Check the volume, or try Chrome or Safari.`); }
        return;
      }
      afterSpeaking();
    };
    const safety = setTimeout(() => finish(started ? '' : 'no sound started'), Math.max(8000, spoken.length * 110));
    const next = () => {
      if (done) return;
      if (i >= parts.length) { finish(''); return; }
      const u = new SpeechSynthesisUtterance(parts[i++]);
      if (v) { u.voice = v; u.lang = v.lang; }
      u.rate = 1.02;
      u.onstart = () => { started = true; };
      u.onend = () => next();
      u.onerror = (e) => {
        const why = e?.error || 'error';
        if (why === 'interrupted' || why === 'canceled') { finish(''); return; }
        finish(why);
      };
      if (i === 1) sayNow(u); else { try { synth.speak(u); } catch { finish('could not speak'); } }
    };
    setStatus('speaking');
    next();
  }

  function afterSpeaking() {
    if (!aliveRef.current) return;
    setStatus('idle');
    if (handsFreeRef.current && spokeLastRef.current && Recognition && open) setTimeout(() => { if (aliveRef.current && !busyRef.current) listen(); }, 350);
  }

  // Keeps listening through short pauses. Sends after SILENCE_MS of silence,
  // or straight away when the member taps "Done talking".
  const SILENCE_MS = 3000;
  const MAX_LISTEN_MS = 90000;
  function listen() {
    if (!Recognition || busyRef.current) return;
    unlockSpeech();
    try { window.speechSynthesis?.cancel(); } catch { /* ignore */ }
    const rec = new Recognition();
    recRef.current = rec;
    rec.lang = navigator.language || 'en-US';
    rec.interimResults = true;
    rec.continuous = true;
    let finalText = '';
    let interimText = '';
    let lastHeard = Date.now();
    let stopping = false;
    let silenceTimer = null;
    const startedAt = Date.now();
    const auto = autoSendRef.current;
    const armSilence = () => {
      if (silenceTimer) clearTimeout(silenceTimer);
      const wait = auto ? SILENCE_MS : Math.max(1000, MAX_LISTEN_MS - (Date.now() - startedAt));
      silenceTimer = setTimeout(() => { stopping = true; try { rec.stop(); } catch { /* ignore */ } }, wait);
    };
    rec.manualStop = () => { stopping = true; if (silenceTimer) clearTimeout(silenceTimer); try { rec.stop(); } catch { /* ignore */ } };
    rec.onresult = (event) => {
      let interim = '';
      for (let i = event.resultIndex; i < event.results.length; i++) {
        const r = event.results[i];
        if (r.isFinal) finalText += (finalText ? ' ' : '') + r[0].transcript.trim(); else interim += r[0].transcript;
      }
      interimText = interim.trim();
      lastHeard = Date.now();
      armSilence();
      const shown = (finalText + ' ' + interimText).trim();
      setNote(shown ? '\u201c' + shown + '\u201d' : '');
    };
    rec.onerror = (event) => {
      if (event?.error === 'no-speech' && !finalText) {
        stopping = true; recRef.current = null; if (silenceTimer) clearTimeout(silenceTimer);
        if (!aliveRef.current) return;
        setStatus('idle'); setNote('I did not hear anything. Tap Talk and speak.');
        return;
      }
      if (event?.error === 'not-allowed' || event?.error === 'service-not-allowed') {
        stopping = true; recRef.current = null; if (silenceTimer) clearTimeout(silenceTimer);
        if (!aliveRef.current) return;
        setStatus('error'); setNote('The microphone is blocked. Allow it in your browser, or type below.');
      }
    };
    rec.onend = () => {
      if (!aliveRef.current) return;
      // Some browsers end the session on their own during a pause: keep listening.
      if (!stopping && (auto ? Date.now() - lastHeard < SILENCE_MS : Date.now() - startedAt < MAX_LISTEN_MS)) {
        try { rec.start(); return; } catch { /* fall through and send what we have */ }
      }
      if (silenceTimer) clearTimeout(silenceTimer);
      recRef.current = null;
      setNote('');
      const said = (finalText + ' ' + interimText).trim();
      if (said) { spokeLastRef.current = true; send(said); } else setStatus((st) => (st === 'listening' ? 'idle' : st));
    };
    setNote('');
    setStatus('listening');
    armSilence();
    try { rec.start(); } catch { setStatus('idle'); }
  }

  async function send(text) {
    if (busyRef.current) return;
    busyRef.current = true;
    addLine('you', text);
    const ack = ackFor(text);
    addLine('ack', ack);
    setStatus('thinking');
    setNote('');
    try { speakAck(ack); } catch { /* speaking the acknowledgment is optional */ }
    try {
      const res = await base44.functions.invoke('talkSend', { text, conversation_id: conversationRef.current || undefined });
      const data = res?.data || {};
      if (!data.turn_id) throw new Error('no_turn');
      if (data.conversation_id) conversationRef.current = data.conversation_id;
      const started = Date.now();
      while (aliveRef.current && Date.now() - started < MAX_WAIT_MS) {
        await new Promise((r) => setTimeout(r, POLL_MS));
        if (!aliveRef.current || !busyRef.current) return;
        let reply;
        try { reply = (await base44.functions.invoke('talkReply', { turn_id: data.turn_id }))?.data; } catch { reply = null; }
        if (reply?.state === 'answered') {
          busyRef.current = false;
          addLine('jarvis', forScreen(reply.reply));
          speak(reply.reply);
          return;
        }
        if (reply?.state === 'failed') {
          busyRef.current = false;
          setStatus('idle');
          setNote(reply.error || 'Jarvis could not answer that. Try again.');
          return;
        }
      }
      busyRef.current = false;
      setStatus('idle');
      setNote('Jarvis is taking a while. The answer will be in your Base44 chat.');
    } catch (e) {
      busyRef.current = false;
      setStatus('idle');
      setNote(errorMessage(e, 'That did not go through. Try again.'));
    }
  }

  function submitTyped(e) {
    e.preventDefault();
    const t = typed.trim();
    if (!t) return;
    unlockSpeech();
    setTyped('');
    spokeLastRef.current = false;
    send(t);
  }

  if (!open) return null;

  const live = useRetell && ['connecting', 'live', 'speaking'].includes(status);
  const ringActive = ['listening', 'speaking', 'live', 'thinking'].includes(status);
  const ringColor = status === 'error' ? '#F08C82' : status === 'speaking' ? '#F5B74A' : '#5FD4EA';
  const showWave = status === 'listening' || status === 'speaking' || status === 'live';
  const pill = { minHeight: 44, padding: '0 16px', borderRadius: 22, border: '1px solid #1E4458', background: 'rgba(13,26,43,.8)', color: '#E6EEF5', font: "500 14px 'Space Grotesk', sans-serif", cursor: 'pointer' };
  const main = { ...pill, minHeight: 56, minWidth: 180, padding: '0 26px', borderRadius: 28, border: 0, background: status === 'listening' ? '#F5B74A' : '#5FD4EA', color: '#061018', fontWeight: 600, fontSize: 16, display: 'inline-flex', alignItems: 'center', justifyContent: 'center', gap: 10 };
  const mic = <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3" /><path d="M5 11a7 7 0 0 0 14 0M12 18v3" /></svg>;

  return (
    <div role="dialog" aria-modal="true" aria-labelledby="talk-title" style={{ position: 'fixed', inset: 0, zIndex: 60, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: 12, background: 'rgba(3,6,12,.72)', backdropFilter: 'blur(4px)' }}>
      <div className="hq-rise" style={{ width: '100%', maxWidth: 520, maxHeight: '88vh', display: 'flex', flexDirection: 'column', borderRadius: 18, border: '1px solid #1E4458', background: 'radial-gradient(600px 360px at 50% 0%, #10233A 0%, #0A1626 70%)', boxShadow: '0 30px 80px rgba(0,0,0,.55)', color: '#E6EEF5', fontFamily: "'Space Grotesk', system-ui, sans-serif" }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, padding: '16px 18px', borderBottom: '1px solid #16263A' }}>
          <span className="hq-dot" style={{ width: 8, height: 8, borderRadius: '50%', background: ringColor, boxShadow: `0 0 10px ${ringColor}` }} />
          <h2 id="talk-title" style={{ margin: 0, fontSize: 16, fontWeight: 600, letterSpacing: '.24em', whiteSpace: 'nowrap' }}>TALK TO JARVIS</h2>
          <span className="hq-talk-provider" style={{ marginLeft: 'auto', fontFamily: "'JetBrains Mono', monospace", fontSize: 11, letterSpacing: '.14em', color: '#8FA3B8', whiteSpace: 'nowrap' }}>{useRetell ? 'RETELL VOICE' : 'BASE44 VOICE'}</span>
          <button type="button" className="hq-talk-close" aria-label="Close" onClick={() => { stopAll(); onClose(); }} style={{ ...pill, minWidth: 44, padding: 0, fontSize: 18 }}>×</button>
        </div>

        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 10, padding: '22px 18px 12px' }}>
          <div aria-hidden="true" className={ringActive ? 'hq-core-working' : 'hq-core-idle'} style={{ position: 'relative', width: 128, height: 128, borderRadius: '50%', border: `2px solid ${ringColor}`, display: 'flex', alignItems: 'center', justifyContent: 'center', boxShadow: ringActive ? `0 0 34px ${ringColor}55, inset 0 0 24px ${ringColor}22` : 'none' }}>
            <div className={ringActive ? 'hq-spin-med' : ''} style={{ position: 'absolute', inset: 8, borderRadius: '50%', border: `1px dashed ${ringColor}66`, transformOrigin: '50% 50%' }} />
            {showWave ? (
              <div style={{ display: 'flex', alignItems: 'center', height: 50 }}>
                {[0, .15, .3, .45, .3, .15, 0].map((d, i) => <span key={i} className="hq-bar" style={{ height: 40, width: 5, background: ringColor, animationDelay: `${d}s` }} />)}
              </div>
            ) : (
              <svg width="52" height="52" viewBox="0 0 100 100" aria-hidden="true"><polygon points="50,14 90,84 10,84" fill="none" stroke={ringColor} strokeWidth="6" strokeLinejoin="round" /><polygon points="50,44 68,76 32,76" fill={ringColor} fillOpacity=".85" /></svg>
            )}
          </div>
          <div aria-live="polite" style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 12, letterSpacing: '.18em', color: ringColor, textTransform: 'uppercase' }}>{STATUS_LABEL[status] || ''}</div>
          {note && <div aria-live="polite" style={{ fontSize: 14, color: '#C9D6E2', textAlign: 'center', maxWidth: 400, lineHeight: 1.5 }}>{note}</div>}
          {status === 'listening' && !autoSend && <div style={{ fontSize: 12, color: '#8FA3B8' }}>Take your time. Tap Send when you're done.</div>}
        </div>

        <div ref={listRef} style={{ flex: 1, minHeight: 80, overflowY: 'auto', padding: '4px 18px 14px', display: 'flex', flexDirection: 'column', gap: 10 }}>
          {lines.length === 0 && status !== 'listening' && (
            <div style={{ fontSize: 14, color: '#94A7BA', textAlign: 'center', lineHeight: 1.5 }}>
              {useRetell ? 'Press Start and talk like you would on a call. Jarvis answers in his own voice.' : 'Tap Talk, say what you need, and Jarvis answers out loud. He can still do real work while you talk.'}
            </div>
          )}
          {lines.map((l, i) => (
            l.who === 'ack' ? (
              <div key={i} className="hq-rise" style={{ alignSelf: 'flex-start', maxWidth: '85%', fontSize: 14, color: '#8FD9EA', fontStyle: 'italic', padding: '2px 4px' }}>Jarvis: {l.text}</div>
            ) : <div key={i} className="hq-rise" style={{ maxWidth: '85%', alignSelf: l.who === 'you' ? 'flex-end' : 'flex-start', padding: '10px 14px', borderRadius: 14, borderBottomRightRadius: l.who === 'you' ? 4 : 14, borderBottomLeftRadius: l.who === 'you' ? 14 : 4, background: l.who === 'you' ? 'rgba(95,212,234,.14)' : 'rgba(13,26,43,.9)', border: `1px solid ${l.who === 'you' ? '#2E6A85' : '#1E4458'}` }}>
              <div style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 10, letterSpacing: '.16em', color: '#8FA3B8' }}>{l.who === 'you' ? 'YOU' : 'JARVIS'}</div>
              <div style={{ fontSize: 15, lineHeight: 1.45, whiteSpace: 'pre-wrap', wordBreak: 'break-word', marginTop: 2 }}>{l.text}</div>
            </div>
          ))}
        </div>

        <div style={{ borderTop: '1px solid #16263A', padding: '16px 18px', display: 'flex', flexDirection: 'column', gap: 12 }}>
          {useRetell ? (
            <div style={{ display: 'flex', justifyContent: 'center' }}>
              {live
                ? <button type="button" style={main} onClick={endRetell}>End chat</button>
                : <button type="button" style={main} onClick={startRetell}>{mic}{status === 'ended' ? 'Start again' : 'Start talking'}</button>}
            </div>
          ) : (
            <>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 10 }}>
                {Recognition && (status === 'listening'
                  ? <button type="button" style={main} onClick={() => { unlockSpeech(); try { recRef.current?.manualStop ? recRef.current.manualStop() : recRef.current?.stop(); } catch { /* ignore */ } }}><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="M22 2 11 13" /><path d="M22 2 15 22l-4-9-9-4 20-7z" /></svg>Send</button>
                  : <button type="button" style={{ ...main, opacity: status === 'thinking' ? 0.6 : 1 }} onClick={listen} disabled={status === 'thinking'}>{mic}{status === 'thinking' ? 'Thinking...' : 'Talk'}</button>)}
                {status === 'speaking' && <button type="button" style={pill} onClick={() => { try { window.speechSynthesis?.cancel(); } catch { /* ignore */ } setStatus('idle'); }}>Stop voice</button>}
              </div>
              <form onSubmit={submitTyped} style={{ display: 'flex', gap: 8 }}>
                <label htmlFor="talk-typed" className="sr-only">Type to Jarvis</label>
                <input id="talk-typed" value={typed} onChange={(e) => setTyped(e.target.value)} placeholder={Recognition ? 'Or type here' : 'Type to Jarvis, he answers out loud'} disabled={status === 'thinking'}
                  style={{ flex: 1, minWidth: 0, minHeight: 44, padding: '0 14px', borderRadius: 22, border: '1px solid #1E4458', background: '#0A1626', color: '#E6EEF5', font: "400 14px 'Space Grotesk', sans-serif" }} />
                <button type="submit" style={{ ...pill, opacity: (status === 'thinking' || !typed.trim()) ? 0.5 : 1 }} disabled={status === 'thinking' || !typed.trim()}>Send</button>
              </form>
              {!Recognition && <div style={{ fontSize: 13, color: '#94A7BA', textAlign: 'center' }}>This browser can't hear you. Use Chrome, Edge or Safari to talk, or type.</div>}
            </>
          )}
        </div>
      </div>
    </div>
  );
}
