import React, { useEffect, useRef, useState } from 'react';
import { base44 } from '@/api/base44Client';
import { HUD } from '@/lib/jarvis';

// Talk to Jarvis out loud from the dashboard.
// Retell owners: a live web call with the real Jarvis voice, no phone needed.
// Base44 owners: free push to talk. The browser hears the owner, the message
// goes to their own Jarvis, and the reply is read aloud by the browser voice.

const POLL_MS = 2500;
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
  const voices = window.speechSynthesis.getVoices() || [];
  const prefer = ['Daniel', 'Google UK English Male', 'Arthur', 'Oliver', 'Microsoft Ryan', 'Microsoft George'];
  for (const name of prefer) {
    const v = voices.find((x) => x.name && x.name.includes(name));
    if (v) return v;
  }
  return voices.find((x) => /^en(-|_)GB/i.test(x.lang)) || voices.find((x) => /^en/i.test(x.lang)) || null;
}

function errorMessage(e, fallback) {
  const data = e?.response?.data || e?.data;
  return (data && data.message) || fallback;
}

export default function TalkPanel({ open, onClose, voiceProvider = 'base44' }) {
  const useRetell = voiceProvider === 'retell';
  const [status, setStatus] = useState('idle');
  const [lines, setLines] = useState([]);
  const [note, setNote] = useState('');
  const [typed, setTyped] = useState('');
  const [handsFree, setHandsFree] = useState(true);
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
  function speak(text) {
    const synth = typeof window !== 'undefined' ? window.speechSynthesis : null;
    const spoken = forSpeech(text);
    if (!synth || !spoken) { afterSpeaking(); return; }
    try { synth.cancel(); } catch { /* ignore */ }
    const u = new SpeechSynthesisUtterance(spoken);
    const v = pickVoice();
    if (v) { u.voice = v; u.lang = v.lang; }
    u.rate = 1.02;
    // Some browsers never fire onend (no voices installed, tab in background).
    // A safety timer makes sure the panel never sticks on "speaking".
    let done = false;
    const finish = () => { if (done) return; done = true; clearTimeout(safety); afterSpeaking(); };
    const safety = setTimeout(finish, Math.max(5000, spoken.length * 90));
    u.onend = finish;
    u.onerror = finish;
    setStatus('speaking');
    synth.speak(u);
  }

  function afterSpeaking() {
    if (!aliveRef.current) return;
    setStatus('idle');
    if (handsFreeRef.current && spokeLastRef.current && Recognition && open) setTimeout(() => { if (aliveRef.current && !busyRef.current) listen(); }, 350);
  }

  function listen() {
    if (!Recognition || busyRef.current) return;
    try { window.speechSynthesis?.cancel(); } catch { /* ignore */ }
    const rec = new Recognition();
    recRef.current = rec;
    rec.lang = navigator.language || 'en-US';
    rec.interimResults = true;
    rec.continuous = false;
    let finalText = '';
    rec.onresult = (event) => {
      let interim = '';
      for (let i = event.resultIndex; i < event.results.length; i++) {
        const r = event.results[i];
        if (r.isFinal) finalText += r[0].transcript; else interim += r[0].transcript;
      }
      setNote(interim ? '“' + interim.trim() + '”' : '');
    };
    rec.onerror = (event) => {
      recRef.current = null;
      if (!aliveRef.current) return;
      if (event?.error === 'not-allowed' || event?.error === 'service-not-allowed') {
        setStatus('error');
        setNote('The microphone is blocked. Allow it in your browser, or type below.');
      } else if (event?.error === 'no-speech') {
        setStatus('idle');
        setNote('I did not hear anything. Tap the button and talk.');
      } else {
        setStatus('idle');
      }
    };
    rec.onend = () => {
      recRef.current = null;
      if (!aliveRef.current) return;
      setNote('');
      const said = finalText.trim();
      if (said) { spokeLastRef.current = true; send(said); } else setStatus((s) => (s === 'listening' ? 'idle' : s));
    };
    setNote('');
    setStatus('listening');
    try { rec.start(); } catch { setStatus('idle'); }
  }

  async function send(text) {
    if (busyRef.current) return;
    busyRef.current = true;
    addLine('you', text);
    setStatus('thinking');
    setNote('');
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
    setTyped('');
    spokeLastRef.current = false;
    send(t);
  }

  if (!open) return null;

  const live = useRetell && ['connecting', 'live', 'speaking'].includes(status);
  const ringActive = ['listening', 'speaking', 'live', 'thinking'].includes(status);

  return (
    <div className="fixed inset-0 z-[60] flex items-end sm:items-center justify-center bg-black/60 p-3" role="dialog" aria-modal="true" aria-labelledby="talk-title">
      <div className="w-full max-w-[460px] bg-hud-bg border border-hud-border flex flex-col max-h-[85vh]">
        <div className="flex items-center gap-3 px-4 h-12 border-b border-hud-border">
          <span className="hud-pulse w-2 h-2 rounded-full bg-hud-accent" />
          <h2 id="talk-title" className="font-body text-[14px] tracking-[0.3em] text-hud-text">TALK TO JARVIS</h2>
          <span className="ml-auto font-mono text-[10px] tracking-[0.16em] uppercase text-hud-faint">{useRetell ? 'Retell voice' : 'Base44'}</span>
          <button type="button" className={btn} onClick={() => { stopAll(); onClose(); }}>Close</button>
        </div>

        <div className="flex flex-col items-center gap-3 px-4 pt-5 pb-3">
          <div
            aria-hidden="true"
            className={'w-24 h-24 rounded-full border-2 flex items-center justify-center ' + (ringActive ? 'hud-pulse' : '')}
            style={{ borderColor: status === 'error' ? HUD.red : status === 'speaking' ? HUD.amber : HUD.accent, boxShadow: ringActive ? '0 0 28px rgba(82,181,255,0.35)' : 'none' }}
          >
            <div className="w-10 h-10 rounded-full" style={{ background: status === 'speaking' ? 'rgba(232,180,90,0.35)' : 'rgba(82,181,255,0.25)' }} />
          </div>
          <div className="font-mono text-[11px] tracking-[0.18em] uppercase text-hud-text2" aria-live="polite">{STATUS_LABEL[status] || ''}</div>
          {note && <div className="font-body text-[13px] text-hud-text2 text-center max-w-[380px]" aria-live="polite">{note}</div>}
        </div>

        <div ref={listRef} className="flex-1 min-h-[80px] overflow-y-auto px-4 pb-3 flex flex-col gap-2">
          {lines.length === 0 && (
            <div className="font-body text-[13px] text-hud-faint text-center">
              {useRetell ? 'Press Start and talk like you would on a call. Jarvis answers in his own voice.' : 'Tap Talk, say what you need, and Jarvis answers out loud. He can still do real work while you talk.'}
            </div>
          )}
          {lines.map((l, i) => (
            <div key={i} className={'max-w-[85%] px-3 py-2 border ' + (l.who === 'you' ? 'self-end border-hud-border' : 'self-start border-hud-accent')}>
              <div className="font-mono text-[9px] tracking-[0.16em] uppercase text-hud-faint">{l.who === 'you' ? 'You' : 'Jarvis'}</div>
              <div className="font-body text-[14px] text-hud-text leading-snug whitespace-pre-wrap break-words">{l.text}</div>
            </div>
          ))}
        </div>

        <div className="border-t border-hud-border px-4 py-3 flex flex-col gap-2">
          {useRetell ? (
            <div className="flex justify-center">
              {live
                ? <button type="button" className={btnMain} onClick={endRetell}>End chat</button>
                : <button type="button" className={btnMain} onClick={startRetell}>{status === 'ended' ? 'Start again' : 'Start talking'}</button>}
            </div>
          ) : (
            <>
              <div className="flex items-center justify-center gap-2">
                {Recognition && (status === 'listening'
                  ? <button type="button" className={btnMain} onClick={() => { try { recRef.current?.stop(); } catch { /* ignore */ } }}>Done talking</button>
                  : <button type="button" className={btnMain} onClick={listen} disabled={status === 'thinking'}>Talk</button>)}
                {status === 'speaking' && <button type="button" className={btn} onClick={() => { try { window.speechSynthesis?.cancel(); } catch { /* ignore */ } setStatus('idle'); }}>Stop voice</button>}
              </div>
              <form onSubmit={submitTyped} className="flex gap-2">
                <label htmlFor="talk-typed" className="sr-only">Type to Jarvis</label>
                <input
                  id="talk-typed"
                  value={typed}
                  onChange={(e) => setTyped(e.target.value)}
                  placeholder={Recognition ? 'Or type here' : 'Type to Jarvis, he answers out loud'}
                  className="flex-1 min-w-0 font-body text-[14px] bg-hud-panel border border-hud-border text-hud-text px-3 py-2 focus:outline-none focus-visible:border-hud-accent"
                  disabled={status === 'thinking'}
                />
                <button type="submit" className={btn} disabled={status === 'thinking' || !typed.trim()}>Send</button>
              </form>
              {Recognition && (
                <label className="flex items-center gap-2 font-mono text-[10px] tracking-[0.14em] uppercase text-hud-faint self-center">
                  <input id="talk-handsfree" type="checkbox" checked={handsFree} onChange={(e) => setHandsFree(e.target.checked)} />
                  Keep listening after each answer
                </label>
              )}
              {!Recognition && <div className="font-mono text-[10px] text-hud-faint text-center">This browser can't hear you. Use Chrome, Edge or Safari to talk, or type.</div>}
            </>
          )}
        </div>
      </div>
    </div>
  );
}
