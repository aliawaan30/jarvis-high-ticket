import '@/components/hq/hq.css';
import React, { useEffect, useRef, useState } from 'react';
import JarvisOrb from '@/components/hq/JarvisOrb';
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
  const data = /\b(leads?|pipeline|crm|status|repl(y|ies|ied)|deals?|clients?|campaigns?|numbers|missions?|due|how many|how far|goal|revenue|booked|what should i (do|focus)|what's (on|next)|plan for today)\b/;
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

// One AudioContext for the Jarvis voice, created and resumed inside a tap so
// Safari and iPhones allow playback.
let sharedCtx = null;
function getCtx() {
  try {
    if (!sharedCtx) { const AC = window.AudioContext || window.webkitAudioContext; if (AC) sharedCtx = new AC(); }
    return sharedCtx;
  } catch { return null; }
}

// Load the Retell voice library in advance, so tapping Talk does not wait for the download.
let retellSdk = null;
export function preloadRetell() { if (!retellSdk) retellSdk = import('retell-client-js-sdk').catch(() => { retellSdk = null; return null; }); return retellSdk; }

// The greeting is prepared in the Jarvis voice when the HUD loads, so tapping Talk
// plays it instantly instead of waiting for Retell to connect or a voice to load.
const greetCache = { text: '', buffer: null, pending: null };
export function greetingText(ownerName) {
  const first = String(ownerName || '').trim().split(/\s+/)[0];
  return `Hey${first ? ' ' + first : ''}, how can I help you today?`;
}
function prepareGreeting(text) {
  if (greetCache.text === text && (greetCache.buffer || greetCache.pending)) return greetCache.pending || Promise.resolve(greetCache.buffer);
  greetCache.text = text; greetCache.buffer = null;
  greetCache.pending = (async () => {
    try {
      const res = await base44.functions.invoke('jarvisVoice', { text });
      const audio = res?.data?.audio;
      const ctx = getCtx();
      if (!audio || !ctx) return null;
      const bin = atob(audio); const arr = new Uint8Array(bin.length);
      for (let i = 0; i < bin.length; i++) arr[i] = bin.charCodeAt(i);
      const buf = await ctx.decodeAudioData(arr.buffer);
      if (greetCache.text === text) greetCache.buffer = buf;
      return buf;
    } catch { return null; } finally { greetCache.pending = null; }
  })();
  return greetCache.pending;
}

// Call inside the click that opens voice mode: Safari only lets a page speak after a tap.
export function primeVoice() {
  try { const c = getCtx(); if (c && c.state === 'suspended') c.resume(); } catch { /* best effort */ }
  try {
    if (typeof window === 'undefined' || !window.speechSynthesis || typeof SpeechSynthesisUtterance === 'undefined') return;
    const u = new SpeechSynthesisUtterance(' '); u.volume = 0; window.speechSynthesis.speak(u);
  } catch { /* best effort */ }
}

function skillFor(text) {
  const t = String(text || '').toLowerCase();
  if (/\b(find|get|search|look for|pull)\b.*\b(leads?|businesses|companies|plumb\w*|hvac|prospects?)\b/.test(t)) return 'LEAD HUNTER';
  if (/\b(draft|write|email|message|text|proposal)\b/.test(t)) return 'WRITING';
  if (/\b(call card)\b/.test(t)) return 'CALL CARD';
  if (/\b(leads?|pipeline|crm|status|repl(y|ies|ied)|deals?|clients?|campaigns?|missions?|due|goal|focus|today)\b/.test(t)) return 'CRM';
  return '';
}

export default function VoiceStage({ open, onClose, voiceProvider = 'base44', ownerName = '', agentGreets = false }) {
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
  // Orb drive: levelRef is the live voice level (0..1), modeRef is what the orb should show.
  const levelRef = useRef(0);
  const modeRef = useRef('idle');
  const statusRef = useRef('idle');
  const agentLevelRef = useRef(0);
  const micLevelRef = useRef(0);
  const callIdRef = useRef('');
  const greetingPlayingRef = useRef(false);
  const orbReadyRef = useRef(null);
  const [greeting, setGreeting] = useState(false);

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
    try { stopFish(); playSeqRef.current++; } catch { /* nothing playing */ }
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
    let token, conn = {};
    try {
      const res = await base44.functions.invoke('talkStart', {});
      token = res?.data?.access_token;
      conn = res?.data || {};
      callIdRef.current = conn.call_id || '';
      if (!token) throw new Error('no_token');
    } catch (e) {
      setStatus('error');
      setNote(errorMessage(e, 'The voice chat could not be started. Try again.'));
      return;
    }
    try {
      const mod = (await preloadRetell()) || (await import('retell-client-js-sdk'));
      const { RetellWebClient } = mod;
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
      client.on('audio', (samples) => {
        if (!samples || !samples.length) return;
        let s = 0; for (let i = 0; i < samples.length; i++) s += samples[i] * samples[i];
        const rms = Math.sqrt(s / samples.length);
        const lv = Math.min(1, Math.max(0, (rms - 0.01) * 6.5));
        const cur = agentLevelRef.current;
        agentLevelRef.current = cur + (lv - cur) * (lv > cur ? 0.35 : 0.06);
      });
      const cfg = { accessToken: token, emitRawAudioSamples: true };
      if (conn.call_id) cfg.callId = conn.call_id;
      if (conn.transport) cfg.transport = conn.transport;
      if (Array.isArray(conn.ice_servers)) cfg.iceServers = conn.ice_servers;
      await client.startCall(cfg);
      try { await client.startAudioPlayback(); } catch { /* playback already allowed */ }
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

  function speakAckBrowser(text) {
    const synth = typeof window !== 'undefined' ? window.speechSynthesis : null;
    if (!synth || typeof SpeechSynthesisUtterance === 'undefined') return;
    const u = new SpeechSynthesisUtterance(text);
    const v = pickVoice();
    if (v) { u.voice = v; u.lang = v.lang; }
    u.rate = 1.05;
    sayNow(u);
  }

  function speakBrowser(text) {
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

  // ---------------------------------------------------------------- Jarvis voice (Fish Audio)
  const fishOkRef = useRef(null); // null: not tried yet, true: works, false: no key, use the browser voice
  const fishSrcRef = useRef(null);
  const fishPlayingRef = useRef(false);
  const playSeqRef = useRef(0);
  function stopFish() {
    try { fishSrcRef.current?.stop(); } catch { /* already stopped */ }
    fishSrcRef.current = null; fishPlayingRef.current = false;
  }
  // Plays text in the Jarvis voice. Resolves true when it played to the end (or was
  // replaced by newer speech), false when the Jarvis voice is not available.
  async function playFish(text) {
    if (fishOkRef.current === false) return false;
    const spoken = forSpeech(text);
    if (!spoken) return false;
    const my = ++playSeqRef.current;
    let data;
    try { const res = await base44.functions.invoke('jarvisVoice', { text: spoken }); data = res?.data; }
    catch (e) { data = e?.response?.data || e?.data; }
    if (!data?.audio) { if (data?.error === 'missing_secret') fishOkRef.current = false; return false; }
    fishOkRef.current = true;
    const ctx = getCtx();
    if (!ctx) return false;
    try { if (ctx.state === 'suspended') await ctx.resume(); } catch { /* ignore */ }
    let buffer;
    try {
      const bin = atob(data.audio); const arr = new Uint8Array(bin.length);
      for (let i = 0; i < bin.length; i++) arr[i] = bin.charCodeAt(i);
      buffer = await ctx.decodeAudioData(arr.buffer);
    } catch { return false; }
    if (my !== playSeqRef.current || !aliveRef.current) return true;
    stopFish();
    try { window.speechSynthesis?.cancel(); } catch { /* ignore */ }
    const src = ctx.createBufferSource(); src.buffer = buffer;
    const an = ctx.createAnalyser(); an.fftSize = 1024;
    src.connect(an); an.connect(ctx.destination);
    fishSrcRef.current = src; fishPlayingRef.current = true;
    const buf = new Float32Array(an.fftSize); let raf = 0;
    const tick = () => {
      an.getFloatTimeDomainData(buf);
      let sum = 0; for (let i = 0; i < buf.length; i++) sum += buf[i] * buf[i];
      const lv = Math.min(1, Math.max(0, (Math.sqrt(sum / buf.length) - 0.01) * 6.5));
      const cur = agentLevelRef.current;
      agentLevelRef.current = cur + (lv - cur) * (lv > cur ? 0.35 : 0.06);
      raf = requestAnimationFrame(tick);
    };
    return new Promise((resolve) => {
      src.onended = () => {
        cancelAnimationFrame(raf);
        if (fishSrcRef.current === src) { fishSrcRef.current = null; fishPlayingRef.current = false; }
        agentLevelRef.current = 0;
        resolve(true);
      };
      src.start(); tick();
    });
  }
  function speak(text) {
    setStatus('speaking');
    (async () => {
      const played = await playFish(text);
      if (!aliveRef.current) return;
      if (played) afterSpeaking(); else speakBrowser(text);
    })();
  }
  function speakAck(text) {
    (async () => { const played = await playFish(text); if (!played && aliveRef.current) speakAckBrowser(text); })();
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


  useEffect(() => { statusRef.current = status; }, [status]);
  useEffect(() => { if (useRetell) preloadRetell(); }, [useRetell]);
  useEffect(() => { prepareGreeting(greetingText(ownerName)); }, [ownerName]);

  // Plays the prepared greeting at once. Returns false if it is not ready.
  function playGreeting(onDone) {
    const buf = greetCache.text === greetingText(ownerName) ? greetCache.buffer : null;
    const ctx = getCtx();
    if (!buf || !ctx) return false;
    try { if (ctx.state === 'suspended') ctx.resume(); } catch { /* ignore */ }
    const src = ctx.createBufferSource(); src.buffer = buf;
    const an = ctx.createAnalyser(); an.fftSize = 1024;
    src.connect(an); an.connect(ctx.destination);
    const data = new Float32Array(an.fftSize); let raf = 0;
    const tick = () => {
      an.getFloatTimeDomainData(data);
      let sum = 0; for (let i = 0; i < data.length; i++) sum += data[i] * data[i];
      const lv = Math.min(1, Math.max(0, (Math.sqrt(sum / data.length) - 0.01) * 6.5));
      agentLevelRef.current += (lv - agentLevelRef.current) * (lv > agentLevelRef.current ? 0.35 : 0.06);
      raf = requestAnimationFrame(tick);
    };
    greetingPlayingRef.current = true; setGreeting(true);
    src.onended = () => {
      cancelAnimationFrame(raf); greetingPlayingRef.current = false; agentLevelRef.current = 0;
      if (aliveRef.current) setGreeting(false);
      onDone && onDone();
    };
    src.start(); tick();
    return true;
  }


  // Microphone level for the orb while the member speaks (separate from speech recognition).
  useEffect(() => {
    if (!open || typeof navigator === 'undefined' || !navigator.mediaDevices?.getUserMedia) return undefined;
    let stream = null, ctx = null, raf = 0, cancelled = false;
    (async () => {
      try {
        stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        if (cancelled) { stream.getTracks().forEach((tr) => tr.stop()); return; }
        ctx = new (window.AudioContext || window.webkitAudioContext)();
        const an = ctx.createAnalyser(); an.fftSize = 1024;
        ctx.createMediaStreamSource(stream).connect(an);
        const data = new Uint8Array(an.fftSize);
        const tick = () => {
          an.getByteTimeDomainData(data);
          let s = 0; for (let i = 0; i < data.length; i++) { const v = (data[i] - 128) / 128; s += v * v; }
          const lv = Math.min(1, Math.max(0, (Math.sqrt(s / data.length) - 0.02) * 6.5));
          micLevelRef.current += (lv - micLevelRef.current) * 0.3;
          raf = requestAnimationFrame(tick);
        };
        tick();
      } catch { /* no mic: the orb still breathes and follows Jarvis */ }
    })();
    return () => {
      cancelled = true; cancelAnimationFrame(raf);
      try { stream && stream.getTracks().forEach((tr) => tr.stop()); } catch { /* ignore */ }
      try { ctx && ctx.close(); } catch { /* ignore */ }
      micLevelRef.current = 0;
    };
  }, [open]);

  // Combine into one level and one mode for the orb.
  useEffect(() => {
    if (!open) return undefined;
    let raf = 0; const t0 = performance.now();
    const tick = (now) => {
      const st = statusRef.current, t = (now - t0) / 1000;
      if (greetingPlayingRef.current) {
        modeRef.current = 'speaking'; levelRef.current = agentLevelRef.current;
      } else if (useRetell && (st === 'live' || st === 'speaking')) {
        // v3 calls send no talking events: Jarvis is speaking when his audio is audible.
        const agent = agentLevelRef.current;
        if (agent > 0.06) { modeRef.current = 'speaking'; levelRef.current = agent; }
        else { modeRef.current = 'listening'; levelRef.current = micLevelRef.current; }
        agentLevelRef.current = agent * 0.97;
      } else if (st === 'speaking') {
        modeRef.current = 'speaking';
        levelRef.current = fishPlayingRef.current ? agentLevelRef.current : 0.22 + 0.38 * (0.5 + 0.5 * Math.sin(t * 2.1) * Math.sin(t * 0.9 + 1.3));
      } else if (st === 'thinking' || st === 'connecting') {
        modeRef.current = 'thinking'; levelRef.current = 0.08;
      } else if (st === 'listening' || st === 'live') {
        modeRef.current = 'listening'; levelRef.current = micLevelRef.current;
      } else {
        modeRef.current = 'idle'; levelRef.current = micLevelRef.current * 0.5;
      }
      raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [open, useRetell]);

  // Opening voice mode: Jarvis greets the member, then listens.
  useEffect(() => {
    if (!open) return;
    setLines([]); setNote('');
    const greet = greetingText(ownerName);
    let cancelled = false;
    // Retell starts connecting on the tap, so its connection time hides behind the transition.
    if (useRetell) startRetell();
    else { spokeLastRef.current = true; addLine('jarvis', greet); setStatus('connecting'); }
    // Greet once the stage is really there: the orb has drawn, the transition has settled,
    // and the greeting audio is ready. Each wait is bounded so a slow device still greets.
    const wait = (ms) => new Promise((r) => setTimeout(r, ms));
    const orbReady = new Promise((resolve) => { orbReadyRef.current = resolve; });
    (async () => {
      await Promise.all([Promise.race([orbReady, wait(1800)]), wait(700)]);
      if (greetCache.text !== greet || !greetCache.buffer) await Promise.race([prepareGreeting(greet), wait(1500)]);
      if (cancelled || !aliveRef.current) return;
      if (useRetell) {
        // Agents built by Set up my voice greet in their own voice; older agents let the user speak first, so the HUD greets.
        if (agentGreets) return;
        if (!playGreeting()) speakAckBrowser(greet);
      } else {
        setStatus('speaking');
        if (!playGreeting(() => { if (aliveRef.current) afterSpeaking(); })) speak(greet);
      }
    })();
    return () => { cancelled = true; };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [open]);

  if (!open) return null;

  const lastJarvis = [...lines].reverse().find((l) => l.who === 'jarvis' || l.who === 'ack');
  const lastYou = [...lines].reverse().find((l) => l.who === 'you');
  const listening = status === 'listening';
  const live = useRetell && ['connecting', 'live', 'speaking'].includes(status);
  const stateText = greeting ? 'JARVIS IS SPEAKING' : { listening: 'LISTENING', thinking: 'THINKING', speaking: 'JARVIS IS SPEAKING', live: 'LIVE WITH JARVIS', connecting: 'CONNECTING', error: 'SOMETHING WENT WRONG', ended: 'CALL ENDED' }[status] || 'READY';
  const stateColor = greeting || status === 'speaking' ? '#F5B74A' : status === 'error' ? '#F08C82' : '#5FD4EA';
  const skill = status === 'thinking' ? skillFor(lastYou?.text) : '';
  const close = () => { stopAll(); onClose(); };
  const pill = { minHeight: 54, padding: '0 26px', borderRadius: 27, font: "600 15px 'Space Grotesk', sans-serif", cursor: 'pointer', border: 0 };
  const ghost = { ...pill, background: 'rgba(13,26,43,.8)', color: '#94A7BA', border: '1px solid #1E4458' };
  const mic = <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3" /><path d="M5 11a7 7 0 0 0 14 0M12 18v3" /></svg>;

  return (
    <div role="dialog" aria-modal="true" aria-label="Talk to Jarvis" className="hq-voice-stage" onKeyDown={(e) => { if (e.key === 'Escape') close(); }}
      style={{ position: 'fixed', inset: 0, zIndex: 70, background: 'radial-gradient(900px 600px at 50% 46%, rgba(20,48,72,.55) 0%, rgba(6,10,18,.0) 70%), rgba(6,10,18,.96)', backdropFilter: 'blur(12px)', WebkitBackdropFilter: 'blur(12px)', color: '#E6EEF5', fontFamily: "'Space Grotesk', system-ui, sans-serif", overflow: 'hidden' }}>
      <JarvisOrb levelRef={levelRef} modeRef={modeRef} active={open} onReady={() => { if (orbReadyRef.current) { orbReadyRef.current(); orbReadyRef.current = null; } }} />
      <div aria-hidden="true" style={{ position: 'absolute', inset: 0, pointerEvents: 'none', background: 'radial-gradient(ellipse at center, rgba(0,0,0,0) 45%, rgba(0,0,0,.65) 100%)' }} />

      <div style={{ position: 'absolute', top: 'calc(18px + env(safe-area-inset-top, 0px))', left: 0, right: 0, textAlign: 'center' }}>
        <div aria-live="polite" style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 13, letterSpacing: '.3em', color: stateColor }}>{stateText}</div>
        <div style={{ fontSize: 15, letterSpacing: '.5em', paddingLeft: '.5em', color: '#94A7BA', marginTop: 6 }}>J.A.R.V.I.S</div>
        {skill && <div className="hq-rise" style={{ display: 'inline-block', marginTop: 10, fontFamily: "'JetBrains Mono', monospace", fontSize: 11, letterSpacing: '.2em', color: '#5FD4EA', border: '1px solid rgba(95,212,234,.4)', background: 'rgba(95,212,234,.08)', padding: '5px 10px', borderRadius: 14 }}>USING · {skill}</div>}
      </div>

      <div aria-live="polite" style={{ position: 'absolute', left: '50%', transform: 'translateX(-50%)', bottom: 'calc(170px + env(safe-area-inset-bottom, 0px))', width: 'min(760px, 90vw)', textAlign: 'center' }}>
        {note && <div style={{ fontSize: 14, color: '#C9D6E2', marginTop: 8, textShadow: '0 2px 12px rgba(0,0,0,.6)' }}>{note}</div>}
      </div>

      <div style={{ position: 'absolute', left: 0, right: 0, bottom: 'calc(40px + env(safe-area-inset-bottom, 0px))', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 12 }}>
        <div style={{ display: 'flex', gap: 12, justifyContent: 'center', flexWrap: 'wrap' }}>
          {useRetell ? (
            live
              ? <button type="button" style={{ ...pill, background: '#F5B74A', color: '#1A1206' }} onClick={() => { endRetell(); }}>End call</button>
              : <button type="button" style={{ ...pill, background: '#5FD4EA', color: '#061018', display: 'inline-flex', alignItems: 'center', gap: 10 }} onClick={() => { primeVoice(); startRetell(); }}>{mic}{status === 'ended' ? 'Talk again' : 'Start talking'}</button>
          ) : listening ? (
            <button type="button" style={{ ...pill, background: '#F5B74A', color: '#1A1206' }} onClick={() => { unlockSpeech(); try { recRef.current?.manualStop ? recRef.current.manualStop() : recRef.current?.stop(); } catch { /* ignore */ } }}>Done talking</button>
          ) : (
            <button type="button" disabled={status === 'thinking' || status === 'speaking' || !Recognition} style={{ ...pill, background: '#5FD4EA', color: '#061018', display: 'inline-flex', alignItems: 'center', gap: 10, opacity: (status === 'thinking' || status === 'speaking') ? 0.5 : 1 }} onClick={listen}>{mic}{status === 'thinking' ? 'Thinking...' : 'Talk'}</button>
          )}
          <button type="button" style={ghost} onClick={close}>End</button>
        </div>
        {!useRetell && (
          <form onSubmit={submitTyped} style={{ display: 'flex', gap: 8, width: 'min(460px, 90vw)' }}>
            <label htmlFor="voice-typed" className="sr-only">Type to Jarvis</label>
            <input id="voice-typed" value={typed} onChange={(e) => setTyped(e.target.value)} placeholder={Recognition ? 'Or type to Jarvis' : 'Type to Jarvis, he answers out loud'} disabled={status === 'thinking'}
              style={{ flex: 1, minWidth: 0, minHeight: 40, padding: '0 14px', borderRadius: 20, border: '1px solid #1E4458', background: 'rgba(10,22,38,.8)', color: '#E6EEF5', font: "400 14px 'Space Grotesk', sans-serif" }} />
            <button type="submit" disabled={status === 'thinking' || !typed.trim()} style={{ ...ghost, minHeight: 40, padding: '0 14px', opacity: (status === 'thinking' || !typed.trim()) ? 0.5 : 1 }}>Send</button>
          </form>
        )}
      </div>
    </div>
  );
}
