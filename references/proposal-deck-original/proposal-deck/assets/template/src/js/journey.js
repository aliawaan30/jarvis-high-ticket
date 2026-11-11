/* ═══ #how — the Verified Buyer Funnel: a six-moment strip, then two live shows (her phone → her CRM record → your sales team's phone) ═══ */
(function () {
  const S = document.getElementById('how'); if (!S) return;
  const CALM = /noanim/.test(location.search) || matchMedia('(prefers-reduced-motion: reduce)').matches;
  const seen = (el, fn) => {                      /* "on screen enough": 45% of it, or half the viewport for tall blocks */
    if (!('IntersectionObserver' in window)) return;
    new IntersectionObserver(es => es.forEach(x => {
      const need = Math.min(x.boundingClientRect.height * .45, innerHeight * .5);
      fn(x.isIntersecting && x.intersectionRect.height >= need);
    }), {threshold: Array.from({length: 21}, (_, i) => i / 20)}).observe(el);
  };

  /* ── 1 · the strip: each phone plays in turn, the line fills, then it loops ── */
  (function () {
    const Z = S.querySelector('.hz'); if (!Z || CALM) return;      /* at rest every phone shows its finished screen */
    const st = [...Z.querySelectorAll('.hz-s')], N = st.length, STEP = 2900, HOLD = 2600;
    let i = -1, T = null, vis = false;
    Z.classList.add('hzgo'); Z.style.setProperty('--hzp', 0);
    function set(n) {
      i = n;
      st.forEach((s, k) => { s.classList.remove('on'); s.classList.toggle('done', k < n); });
      void Z.offsetWidth;
      if (st[n]) st[n].classList.add('on');
      Z.style.setProperty('--hzp', Math.max(0, n) / (N - 1));
    }
    function tick() {
      clearTimeout(T); if (!vis) return;
      if (i < N - 1) { set(i + 1); T = setTimeout(tick, STEP); }
      else { st.forEach(s => { s.classList.remove('on'); s.classList.add('done'); });
        T = setTimeout(() => { if (!vis) return; st.forEach(s => s.classList.remove('done')); Z.style.setProperty('--hzp', 0); i = -1; T = setTimeout(tick, 700); }, HOLD); }
    }
    seen(Z, v => { if (v === vis) return; vis = v; if (v) { if (i < 0) tick(); else T = setTimeout(tick, 400); } else clearTimeout(T); });
    addEventListener('beforeprint', () => { clearTimeout(T); Z.classList.remove('hzgo'); st.forEach(s => s.classList.remove('on', 'done')); Z.style.setProperty('--hzp', 1); });
    addEventListener('afterprint', () => { Z.classList.add('hzgo'); if (vis) { i = -1; tick(); } });
  })();

  /* ── 2 · the films: six chapters on one clock — camera, captions, scrubber, hover-to-explain, optional sound ── */
  /* the soundtrack: a music bed only, never a voice. It plays assets/film-music.mp3; where that file can't load
     (the single-file artifact), a small Web Audio band plays the same warm progression instead. User-started only. */
  let AC = null, padNodes = null, soundOwner = null, muted = false, MUSIC = null, useSyn = false, fadeT = null;
  function mus() {
    if (MUSIC || useSyn) return MUSIC;
    try { MUSIC = new Audio(asset('assets/film-music.mp3')); MUSIC.preload = 'auto'; MUSIC.loop = true; MUSIC.volume = 0;
      MUSIC.addEventListener('error', () => { const was = MUSIC && !MUSIC.paused; useSyn = true; MUSIC = null; if (padNodes && soundOwner) synOn(); }); }
    catch (e) { useSyn = true; MUSIC = null; }
    return MUSIC;
  }
  function fade(to, ms, then) {
    clearInterval(fadeT); if (!MUSIC) { if (then) then(); return; } const from = MUSIC.volume, t0 = performance.now();
    fadeT = setInterval(() => { if (!MUSIC) return clearInterval(fadeT); const u = Math.min(1, (performance.now() - t0) / ms); MUSIC.volume = from + (to - from) * u; if (u >= 1) { clearInterval(fadeT); if (then) then(); } }, 40);
  }
  function musicAt(ms) { const m = mus(); if (!m) return; try { const d = m.duration || 50.5; m.currentTime = (ms / 1000) % d; } catch (e) {} }
  function musicGo() {
    if (!padNodes) return;
    const m = mus(); if (!m) { synOn(); return; }
    const p = m.play(); if (p && p.catch) p.catch(() => { useSyn = true; MUSIC = null; synOn(); }); fade(.45, 1600);
  }
  function musicHold() { synOff(); fade(0, 450, () => { if (MUSIC) MUSIC.pause(); }); }

  /* the fallback bed — the same as the file: 76 bpm, Fmaj9 · Dm9 · B♭maj9 · Csus→C, soft keys over a slow pad and a round bass, nothing on top */
  const SYN = {on: false, timer: null, next: 0, step: 0, out: null, lp: null};
  const B8 = 60 / 76 / 2, mf = m => 440 * Math.pow(2, (m - 69) / 12);
  const CHORDS = [[57, 60, 64, 67], [57, 60, 64, 65], [57, 58, 62, 65], [55, 60, 62, 67]], BASS = [41, 38, 46, 36];
  function tone(m, t, dur, g, type, dest, att) {
    const o = AC.createOscillator(), v = AC.createGain(); o.type = type || 'sine'; o.frequency.value = mf(m);
    v.gain.setValueAtTime(.0001, t); v.gain.exponentialRampToValueAtTime(g, t + (att || .015)); v.gain.exponentialRampToValueAtTime(.0001, t + dur);
    o.connect(v); v.connect(dest || SYN.lp); o.start(t); o.stop(t + dur + .05);
  }
  function bar8(step, t) {
    const k = Math.floor(step / 8) % 4, c = CHORDS[k], b = step % 8;
    if (b === 0) { c.forEach((m, i) => tone(m, t + i * .018, 3.2, .05, 'sine')); c.slice(1).forEach(m => tone(m - 12, t, 4.6, .022, 'triangle', null, 1.4)); tone(BASS[k], t, 2.6, .12, 'sine', null, .03); }
    if (b === 4) { (k === 3 ? [60, 64, 67] : c.slice(1)).forEach((m, i) => tone(m, t + i * .014, 2.4, .028, 'sine')); tone(k === 3 ? 43 : BASS[k] + 7, t, 2, .06, 'sine', null, .03); }
  }
  function synOn() {
    if (!AC || SYN.on) return;
    try {
      SYN.on = true; SYN.out = AC.createGain(); SYN.out.gain.value = .0001; SYN.out.connect(AC.destination);
      SYN.lp = AC.createBiquadFilter(); SYN.lp.type = 'lowpass'; SYN.lp.frequency.value = 1800; SYN.lp.connect(SYN.out);
      SYN.out.gain.exponentialRampToValueAtTime(.9, AC.currentTime + 1.4);
      SYN.next = AC.currentTime + .08;
      SYN.timer = setInterval(() => { while (SYN.on && SYN.next < AC.currentTime + .3) { bar8(SYN.step, SYN.next); SYN.next += B8; SYN.step++; } }, 70);
    } catch (e) { SYN.on = false; }
  }
  function synOff() {
    if (!SYN.on) return; SYN.on = false; clearInterval(SYN.timer);
    const o = SYN.out; try { o.gain.cancelScheduledValues(AC.currentTime); o.gain.setValueAtTime(o.gain.value, AC.currentTime); o.gain.exponentialRampToValueAtTime(.0001, AC.currentTime + .5); setTimeout(() => o.disconnect(), 700); } catch (e) {}
  }
  function padOn() {
    try { AC = AC || new (window.AudioContext || window.webkitAudioContext)(); if (AC.state === 'suspended') AC.resume(); } catch (e) { AC = null; }
    padNodes = true; mus();
  }
  function padOff() { padNodes = null; musicHold(); }
  function blip(f) {
    if (!padNodes || !AC) return;
    try { const o = AC.createOscillator(), g = AC.createGain(); o.frequency.value = f || 880; g.gain.value = .0001; o.connect(g); g.connect(AC.destination);
      g.gain.exponentialRampToValueAtTime(.014, AC.currentTime + .02); g.gain.exponentialRampToValueAtTime(.0001, AC.currentTime + .25); o.start(); o.stop(AC.currentTime + .3); } catch (e) {}
  }
  function chime() {                                           /* a soft two-note turn at each new chapter */
    if (!padNodes || !AC) return;
    try { const t = AC.currentTime + .02, d = AC.destination; [[84, 0], [88, .09]].forEach(([m, dt]) => tone(m, t + dt, 1.2, .022, 'sine', d)); } catch (e) {}
  }


  /* ── the thumb: a scripted, seekable run through the form — every frame is a pure function of film time ──
     acts (global ms): ['pg',t,i] page · ['sy',t,key,dur,frac] scroll · ['tap',t,key] · ['ty',t,key,text,[offsets]] typing
                       ['km',t,mode] / ['kb',t0,t1] keyboard · ['nf',t,key,dur] banner · ['on',t,key] */
  function puppet(R, A) {
    const K = k => R.querySelector('[data-k="' + k + '"]');
    const of = n => A.filter(a => a[0] === n);
    const taps = of('tap'), tys = of('ty'), sys = of('sy'), pgs = of('pg'), kms = of('km'), kbs = of('kb'), nfs = of('nf'), ons = of('on');
    const fg = R.querySelector('.fx-fg'), rp = R.querySelector('.fx-rp'), kb = R.querySelector('.fx-kb');
    const pages = [...R.querySelectorAll('.fx-pg')], docs = [...R.querySelectorAll('.fx-doc')], groups = [...R.querySelectorAll('[data-g]')];
    const ease = u => u < .5 ? 2 * u * u : 1 - Math.pow(-2 * u + 2, 2) / 2, cl = (v, a, b) => Math.max(a, Math.min(b, v));
    const docY = new Map(), aim = {};
    let lastHit = null;
    function off(el, stop) { let x = 0, y = 0, n = el; while (n && n !== stop) { x += n.offsetLeft; y += n.offsetTop; n = n.offsetParent; } return {x, y, ok: n === stop}; }
    function target(s) {                                   /* where a scroll lands: the element near the top, clamped to the page */
      if (aim[s[2]] != null) return aim[s[2]];
      const el = K(s[2]), d = el && el.closest('.fx-doc'); if (!d) return 0;
      const o = off(el, d), vp = d.parentElement; if (!o.ok || !vp.clientHeight) return 0;
      const y = cl(o.y - s[4] * vp.clientHeight - (+d.dataset.top || 0), 0, Math.max(0, d.offsetHeight - vp.clientHeight));
      return (aim[s[2]] = Math.round(y));
    }
    function pos(k) {                                      /* an element's centre on her screen, as it sits right now */
      const el = K(k); if (!el) return null;
      const o = off(el, R); if (!o.ok) return null;
      const d = el.closest('.fx-doc'), px = +(el.dataset.px || .5);
      return {x: o.x + el.offsetWidth * px, y: o.y + el.offsetHeight / 2 - (d ? docY.get(d) || 0 : 0)};
    }
    function win(T, t0, t1, ms) { return T < t0 ? 0 : T < t0 + ms ? (T - t0) / ms : t1 == null || T < t1 ? 1 : T < t1 + ms ? 1 - (T - t1) / ms : 0; }
    return function render(T) {
      if (!R.offsetWidth) return;
      /* pages slide across */
      let cur = 0, prev = 0, u = 1;
      pgs.forEach(p => { if (p[1] <= T) { prev = cur; cur = p[2]; u = cl((T - p[1]) / 380, 0, 1); } });
      const e = ease(u);
      pages.forEach((pg, i) => { const x = (i - prev) * (1 - e) + (i - cur) * e; pg.style.transform = 'translateX(' + (x * 100).toFixed(2) + '%)'; pg.style.visibility = Math.abs(x) < 1 ? '' : 'hidden'; });
      /* scroll: each page eases from its last resting point to the next */
      docs.forEach(d => docY.set(d, 0));
      const last = new Map();
      sys.forEach(s => { if (s[1] > T) return; const el = K(s[2]), d = el && el.closest('.fx-doc'); if (!d) return;
        const from = last.has(d) ? last.get(d) : 0, to = target(s); last.set(d, to);
        docY.set(d, from + (to - from) * ease(cl((T - s[1]) / s[3], 0, 1))); });
      docs.forEach(d => { d.style.transform = 'translateY(' + (-(docY.get(d) || 0)).toFixed(1) + 'px)'; });
      /* answers chosen, boxes ticked, buttons pressed */
      const pick = {}, done = new Set(); let focus = null;
      taps.forEach(a => { if (a[1] <= T) { const el = K(a[2]); if (!el) return; focus = a[2]; done.add(a[2]); if (el.dataset.g) pick[el.dataset.g] = a[2]; } });
      groups.forEach(el => el.classList.toggle('sel', pick[el.dataset.g] === el.dataset.k));
      R.querySelectorAll('.fx-ck').forEach(el => el.classList.toggle('on', done.has(el.dataset.k)));
      R.querySelectorAll('.fx-btn').forEach(el => { const a = taps.find(x => x[2] === el.dataset.k); el.classList.toggle('prs', !!a && T >= a[1] - 40 && T < a[1] + 240); });
      ons.forEach(a => { const el = K(a[2]); if (el) el.classList.toggle('on', T >= a[1]); });
      /* typing, a character at a time */
      let hit = null, typing = false;
      tys.forEach(a => {
        const el = K(a[2]); if (!el) return;
        const offs = a[4]; let n = 0; while (n < offs.length && a[1] + offs[n] <= T) n++;
        const txt = a[3].slice(0, n);
        if (el.classList.contains('fx-code')) [...el.children].forEach((b, i) => { const c = txt[i] || ''; if (b.textContent !== c) b.textContent = c; b.classList.toggle('fl', !!c); b.classList.toggle('cu', i === n && n < 6); });
        else { const tx = el.querySelector('.fx-tx'); if (tx && tx.textContent !== txt) tx.textContent = txt; el.classList.toggle('fil', n > 0); }
        if (n > 0 && n <= offs.length && T - (a[1] + offs[n - 1]) < 110 && T < a[1] + offs[offs.length - 1] + 110) hit = a[3][n - 1];
        if (T >= a[1] - 150 && T < a[1] + offs[offs.length - 1] + 200) typing = true;
      });
      R.querySelectorAll('.fx-fi, .lf-fi, .lp-fi, .fx-code').forEach(el => el.classList.toggle('foc', !!focus && el.dataset.k === focus));
      /* the keyboard: up while she types, in letters or numbers */
      if (kb) {
        let v = 0; kbs.forEach(w => { v = Math.max(v, win(T, w[1], w[2], 300)); });
        let m = 'a'; kms.forEach(k => { if (k[1] <= T) m = k[2]; }); if (kb.dataset.m !== m) kb.dataset.m = m;
        kb.style.transform = 'translateY(' + ((1 - ease(v)) * 105).toFixed(1) + '%)';
        const key = hit != null ? kb.querySelector('.kb-' + m + ' [data-c="' + (hit === '"' ? '' : hit.toLowerCase()) + '"]') : null;
        if (key !== lastHit) { if (lastHit) lastHit.classList.remove('hit'); if (key) key.classList.add('hit'); lastHit = key; }
      }
      /* the codes arriving */
      nfs.forEach(a => { const el = K(a[2]); if (!el) return; const v = ease(win(T, a[1], a[1] + a[3], 350));
        el.style.opacity = v.toFixed(3); el.style.transform = 'translateY(' + (-140 * (1 - v)).toFixed(1) + '%)'; });
      /* her thumb: glides to the next thing, presses, lifts away */
      if (!fg) return;
      let pi = -1; taps.forEach((a, i) => { if (a[1] <= T) pi = i; });
      const P = taps[pi], N = taps[pi + 1], MOVE = 650;
      let at = null, vis = 0, press = 0;
      const W = R.offsetWidth, H = R.offsetHeight, home = {x: W * .78, y: H + 40};
      if (N && T >= N[1] - MOVE) {
        const to = pos(N[2]), fresh = !P || N[1] - P[1] > 2600, from = fresh ? home : pos(P[2]) || home;
        if (to) { const k = ease(cl((T - (N[1] - MOVE)) / (MOVE - 110), 0, 1)); at = {x: from.x + (to.x - from.x) * k, y: from.y + (to.y - from.y) * k};
          vis = fresh ? cl((T - (N[1] - MOVE)) / 220, 0, 1) : 1; }
      } else if (P && T - P[1] < 900) { at = pos(P[2]); vis = 1 - cl((T - P[1] - 480) / 380, 0, 1); }
      if (typing) vis = 0;
      [P, N].forEach(a => { if (a) press = Math.max(press, 1 - Math.abs(T - a[1]) / 150); });
      press = cl(press, 0, 1);
      if (at && vis > 0) { fg.style.opacity = vis.toFixed(3); fg.style.transform = 'translate(' + at.x.toFixed(1) + 'px,' + at.y.toFixed(1) + 'px) scale(' + (1 - .22 * press).toFixed(3) + ')'; }
      else fg.style.opacity = 0;
      const rpu = P ? (T - P[1]) / 520 : 2, rpo = P && rpu >= 0 && rpu < 1 ? pos(P[2]) : null;
      if (rp) { if (rpo) { rp.style.opacity = ((1 - rpu) * .9).toFixed(3); rp.style.transform = 'translate(' + rpo.x.toFixed(1) + 'px,' + rpo.y.toFixed(1) + 'px) scale(' + (.5 + 1.4 * rpu).toFixed(3) + ')'; } else rp.style.opacity = 0; }
    };
  }

  S.querySelectorAll('.xj').forEach((J, jIdx) => {
    const box = J.querySelector('.xshow'), steps = [...J.querySelectorAll('.xstep')], play = J.querySelector('.xplay');
    const view = box && box.querySelector('.xview'), rig = box && box.querySelector('.xrig');
    if (!box || !play || !steps.length || !rig) return;
    const N = steps.length, DUR = JSON.parse(J.dataset.dur || '[]'), EV = JSON.parse(J.dataset.ev || '{}'), CC = JSON.parse(J.dataset.cc || '{}'), REST = +(J.dataset.rest || 1);
    Object.keys(EV).forEach(k => EV[k].sort((a, b) => a[0] - b[0]));
    const START = DUR.map((d, i) => DUR.slice(0, i).reduce((a, b) => a + b, 0)), TOTAL = DUR.reduce((a, b) => a + b, 0);
    const lab = play.querySelector('span'), svg = rig.querySelector('.xwires');
    const W = {}; ['L', 'R', 'C'].forEach(k => W[k] = svg && svg.querySelector('.w' + k));
    const ring = box.querySelector('.xr-sc'), ringN = ring && ring.querySelector('b'), gph = box.querySelector('.xph.gr'), xgr = box.querySelector('.xgr');
    const kb = box.querySelector('.xr-kb');
    const doc = box.querySelector('.lp-doc'), vid = box.querySelector('.lp-vid');
    const video = vid && (vid.querySelector('video') || (vid.dataset.len ? stills(vid) : null));
    const frs = vid ? [...vid.querySelectorAll('.lv-fr')] : [], subs = vid && vid.dataset.subs ? vid.dataset.subs.split('|') : null, sub = vid && vid.querySelector('.lv-cc');
    const ccBox = box.querySelector('.xcc'), ccSpan = ccBox && ccBox.querySelector('span'), ccBtn = box.querySelector('.xccb'), sndBtn = box.querySelector('.xsnd');
    const scrub = box.querySelector('.xscrub'), sFill = box.querySelector('.xsf'), sHead = box.querySelector('.xsh'), tmEl = box.querySelector('.xtm'), rp = box.querySelector('.xrp');
    const tip = box.querySelector('.xtip');
    const FX = JSON.parse(J.dataset.fx || 'null'), fxR = FX && box.querySelector('.xbuy .fx-root'), thumb = fxR ? puppet(fxR, FX) : null;
    const q = location.search.match(new RegExp('howstep' + (jIdx ? '2' : '') + '=(\\d+)'));   /* QA hooks: ?howstep=N, ?howstep2=N */
    const calm = CALM || /howstep/.test(location.search);
    let cur = 1, t = 0, fi = 0, ci = -1, playing = false, held = false, ended = false, onScreen = false, raf = 0, last = 0, scoreV = 0, scoreRaf = null, focus = 'W';
    const fmt = s => Math.floor(s / 60) + ':' + String(Math.floor(s % 60)).padStart(2, '0');

    /* geometry in the rig's own (untransformed) coordinates, so the camera can move everything together */
    function rel(el) { let x = 0, y = 0, n = el; while (n && n !== rig) { x += n.offsetLeft; y += n.offsetTop; n = n.offsetParent; } const w = el.offsetWidth, h = el.offsetHeight; return {l: x, t: y, w, h, r: x + w, b: y + h}; }
    function geo() {
      if (!svg || !rig.offsetWidth) return;
      svg.setAttribute('viewBox', '0 0 ' + rig.offsetWidth + ' ' + rig.offsetHeight);
      const sp = rel(box.querySelector('.xbuy .xph')), gp = rel(box.querySelector('.xgr .xph')), rc = rel(box.querySelector('.xrec'));
      const stacked = rc.l < sp.r - 4 || gp.t > rc.b;
      box.classList.toggle('stacked', stacked);
      if (stacked) { cam('W'); return; }
      const y1 = sp.t + sp.h * .46, y2 = rc.t + rc.h * .42, y3 = gp.t + gp.h * .46, m1 = (sp.r + rc.l) / 2, m2 = (rc.r + gp.l) / 2;
      W.L.setAttribute('d', `M${sp.r - 6},${y1} C${m1},${y1} ${m1},${y2} ${rc.l},${y2}`);
      W.R.setAttribute('d', `M${rc.r},${y2} C${m2},${y2} ${m2},${y3} ${gp.l + 6},${y3}`);
      const by = Math.max(sp.b, gp.b) + 26, gx = gp.l + gp.w * .5, sx = sp.l + sp.w * .5;
      W.C.setAttribute('d', `M${gx},${gp.b - 8} C${gx},${by} ${sx},${by} ${sx},${sp.b - 8}`);
    }
    /* the camera: push in on one of the three, pull back wide */
    function cam(k, instant) {
      focus = k || 'W';
      if (!view) return;
      if (box.classList.contains('stacked') || calm) { view.dataset.focus = 'W'; rig.style.transform = ''; return; }
      view.dataset.focus = focus;
      if (instant) rig.style.transition = 'none';
      if (focus === 'W') rig.style.transform = '';
      else {
        const el = box.querySelector(focus === 'L' ? '.xbuy' : focus === 'R' ? '.xgr' : '.xmid'); if (!el) return;
        const r = rel(el), VW = rig.offsetWidth, VH = rig.offsetHeight, s = Math.max(1.04, Math.min(1.18, (VH - 8) / (r.h + 8)));
        let tx = VW / 2 - s * (r.l + r.w / 2), ty = VH / 2 - s * (r.t + r.h / 2);
        tx = Math.min(0, Math.max(VW - s * VW, tx)); ty = Math.min(0, Math.max(VH - s * VH, ty));
        rig.style.transform = `translate(${tx.toFixed(1)}px,${ty.toFixed(1)}px) scale(${s})`;
      }
      if (instant) { void rig.offsetWidth; rig.style.transition = ''; }
    }
    function send(k, text, rev, ms) {                        /* a data packet travels the wire */
      const p = W[k]; if (!p || box.classList.contains('stacked')) return;
      const len = p.getTotalLength(); if (!len) return;
      ms = ms || (k === 'C' ? 1500 : 820);
      const el = document.createElement('div'); el.className = 'xpk'; el.innerHTML = '<i></i>' + text; rig.appendChild(el);
      p._n = (p._n || 0) + 1; p.classList.add('hot'); p.classList.toggle('rev', !!rev);
      const t0 = performance.now();
      const go = now => {
        if (!el.isConnected) return;
        const u = Math.min(1, (now - t0) / ms), e = u < .5 ? 2 * u * u : 1 - Math.pow(-2 * u + 2, 2) / 2;
        const pt = p.getPointAtLength((rev ? 1 - e : e) * len);
        el.style.transform = 'translate(' + pt.x + 'px,' + pt.y + 'px) translate(-50%,-50%)';
        if (u < 1) requestAnimationFrame(go);
        else { el.classList.add('fade'); setTimeout(() => el.remove(), 260); if (--p._n <= 0) { p._n = 0; p.classList.remove('hot', 'rev'); } }
      };
      requestAnimationFrame(go);
    }
    function score(v, anim) {
      if (!ring) return;
      cancelAnimationFrame(scoreRaf);
      ring.style.setProperty('--p', v);
      const from = scoreV; scoreV = v;
      if (!anim || !v) { ringN.textContent = v ? v : '–'; return; }
      const t0 = performance.now();
      const f = now => { const u = Math.min(1, (now - t0) / 480); ringN.textContent = Math.round(from + (v - from) * u); if (u < 1) scoreRaf = requestAnimationFrame(f); };
      scoreRaf = requestAnimationFrame(f);
      ring.classList.remove('pop'); void ring.offsetWidth; ring.classList.add('pop'); setTimeout(() => ring.classList.remove('pop'), 500);
    }
    function pipe(c) { if (!kb) return; kb.dataset.col = c; if (c >= 0) kb.style.setProperty('--col', c); }
    function scrollTo(name, anim) {
      if (!doc) return;
      const tg = name && doc.querySelector('[data-sy="' + name + '"]');
      const vp = doc.parentElement, max = Math.max(0, doc.scrollHeight - vp.clientHeight);
      const y = tg ? Math.min(max, Math.max(0, tg.offsetTop - 46)) : 0;
      doc.style.transition = anim ? '' : 'none';
      doc.style.setProperty('--sy', y);
      if (!anim) { void doc.offsetWidth; doc.style.transition = ''; }
    }
    function buzz() {
      [gph, xgr].forEach(x => { if (x) { x.classList.remove('buzz'); void x.offsetWidth; x.classList.add('buzz'); } });
      blip(220); setTimeout(() => blip(220), 160);
    }
    /* the film on the landing page: a real <video> where there is one; otherwise a stills film (data-len seconds of
       .lv-fr frames, data-s → data-e each) that behaves like a muted, looping video — slow Ken Burns, a soft cut between stills */
    function stills(el) {
      const len = +el.dataset.len || 48, ls = {}; let at = 0, t0 = 0, on = false;
      const now = () => on ? at + (performance.now() - t0) / 1000 : at;
      const emit = n => (ls[n] || []).forEach(f => f());
      return {
        get duration() { return len; }, get paused() { return !on; },
        get currentTime() { return now() % len; },
        set currentTime(x) { at = Math.max(0, +x || 0) % len; t0 = performance.now(); },
        play() { if (!on) { at = now(); t0 = performance.now(); on = true; emit('play'); } return Promise.resolve(); },
        pause() { if (on) { at = now() % len; on = false; emit('pause'); } },
        addEventListener(n, f) { (ls[n] = ls[n] || []).push(f); },
        getAttribute() { return 'stills'; }, dataset: {}, load() {}
      };
    }
    function frames(vt) {
      frs.forEach((f, i) => {
        const s = +f.dataset.s, e = +f.dataset.e, u = Math.max(0, Math.min(1, (vt - s) / Math.max(1, e - s)));
        const o = i === 0 ? 1 : vt < s ? 0 : Math.min(1, (vt - s) / .8);
        f.style.opacity = o.toFixed(3);
        const im = f.firstElementChild; if (im) im.style.transform = 'scale(' + (1.04 + .1 * u).toFixed(4) + ') translateX(' + ((i % 2 ? -1.6 : 1.6) * u).toFixed(2) + '%)';
      });
    }
    let vRaf = null;
    function vPaint() {
      if (!video) return;
      const d = video.duration || 48, vt = video.currentTime || 0, u = vt / d;
      const fill = vid.querySelector('.lp-fill'), tm = vid.querySelector('.lp-tm');
      if (fill) fill.style.width = (u * 100) + '%';
      if (tm) tm.textContent = fmt(vt) + ' / ' + fmt(d);
      const c = Math.min(3, Math.floor(u * 4));
      box.querySelectorAll('.lp-ch li').forEach((li, k) => li.classList.toggle('on', k === c));
      if (frs.length) frames(vt);
      if (subs && sub && sub.dataset.c !== String(c)) { sub.textContent = subs[c] || ''; sub.dataset.c = c; }
    }
    function vLoop() { vPaint(); if (video && !video.paused) vRaf = requestAnimationFrame(vLoop); else vRaf = null; }
    function vLoad() { if (video && !video.getAttribute('src') && video.dataset.src) { video.src = video.dataset.src; video.load(); } }
    function vPlay(at, force) {
      if (!video || (CALM && !force)) return;
      vLoad();
      if (at != null) { try { video.currentTime = at; } catch (e) {} }
      const p = video.play(); if (p && p.catch) p.catch(() => {});
    }
    function vPause() { if (video && !video.paused) video.pause(); }
    if (video) {
      video.addEventListener('play', () => { vid.classList.add('playing'); if (!vRaf) vRaf = requestAnimationFrame(vLoop); });
      video.addEventListener('pause', () => { vid.classList.remove('playing'); vPaint(); });
      video.addEventListener('loadedmetadata', vPaint);
    }
    const tmrs = [...box.querySelectorAll('.tmr')];
    const mm = v => String(Math.floor(v / 60)).padStart(2, '0') + ':' + String(v % 60).padStart(2, '0');
    function timers(final) {                                 /* call clocks run off the film clock */
      tmrs.forEach(el => {
        const sc = el.closest('.xscr, .gscr'), live = sc && getComputedStyle(sc).display !== 'none';
        const u = final || !live ? 1 : Math.max(0, Math.min(1, (t - +el.dataset.tmAt) / +el.dataset.tmLen));
        el.textContent = mm(Math.round(+el.dataset.tm * u));
      });
    }
    function instant(e) { if (e[1] === 'sc') score(e[2], false); else if (e[1] === 'pl') pipe(e[2]); else if (e[1] === 'sy') scrollTo(e[2], false); else if (e[1] === 'cm') cam(e[2], true); }
    function fire(e) {
      if (e[1] === 'pk') send(e[2], e[3], e[4]);
      else if (e[1] === 'sc') score(e[2], true);
      else if (e[1] === 'bz') buzz();
      else if (e[1] === 'pl') pipe(e[2]);
      else if (e[1] === 'sy') scrollTo(e[2], true);
      else if (e[1] === 'cm') cam(e[2]);
      else if (e[1] === 'vd' && playing) vPlay(0);
    }
    function clearPk() {
      rig.querySelectorAll('.xpk').forEach(x => x.remove());
      Object.values(W).forEach(p => { if (p) { p._n = 0; p.classList.remove('hot', 'rev'); } });
    }
    const anims = () => (view || rig).getAnimations ? (view || rig).getAnimations({subtree: true}).filter(a => !(window.CSSTransition && a instanceof CSSTransition)) : [];

    /* enter a chapter: everything earlier is applied at once; this chapter's cues fire as the clock passes them */
    function enter(n) {
      cur = n; t = 0; fi = 0; ci = -1; box.dataset.step = n; clearPk();
      if (ccSpan) { ccSpan.innerHTML = ''; ccBox.classList.remove('has'); }
      if (playing && soundOwner === J && n > 1) chime();
      score(0, false); pipe(-1); scrollTo(null, false);
      for (let k = 1; k < n; k++) (EV[k] || []).forEach(instant);
      const from = [...box.querySelectorAll('[data-from]')];
      from.forEach(el => { el.classList.toggle('on', n >= +el.dataset.from); el.classList.remove('now'); });
      void box.offsetWidth;
      from.forEach(el => { if (+el.dataset.from === n) el.classList.add('now'); });
      box.querySelectorAll('[data-at]').forEach(el => el.classList.toggle('on', +el.dataset.at === n));
      const scr = box.querySelector('.xbuy .xscr.s' + n); box.classList.toggle('dark', !!(scr && scr.classList.contains('t-call')));
      steps.forEach((b, i) => { b.classList.toggle('on', i + 1 === n); b.classList.toggle('done', i + 1 < n); if (i + 1 === n) b.setAttribute('aria-current', 'step'); else b.removeAttribute('aria-current'); });
      if (video && n !== 2) vPause();
      if (calm) { (EV[n] || []).forEach(instant); fi = 1e9; timers(true); vPaint(); if (thumb) thumb(START[n - 1] + DUR[n - 1] - 1); }
      caption();
    }
    function caption() {
      if (!ccBox) return;
      const cs = CC[cur] || []; let k = -1; cs.forEach((c, j) => { if (t >= c[0]) k = j; });
      if (k === ci) return; ci = k;
      ccSpan.innerHTML = k < 0 ? '' : cs[k][1]; ccBox.classList.toggle('has', k >= 0);
      ccBox.classList.remove('pop'); void ccBox.offsetWidth; ccBox.classList.add('pop');
    }
    function paint() {
      const T = START[cur - 1] + t;
      steps.forEach((b, i) => { const f = b.querySelector('.pf'); if (f) f.style.transform = 'scaleX(' + (i + 1 < cur ? 1 : i + 1 > cur ? 0 : Math.min(1, t / DUR[cur - 1]).toFixed(4)) + ')'; });
      if (sFill) sFill.style.transform = 'scaleX(' + Math.min(1, T / TOTAL).toFixed(4) + ')';
      if (sHead) sHead.style.left = (Math.min(1, T / TOTAL) * 100).toFixed(3) + '%';
      if (tmEl) tmEl.textContent = fmt(T / 1000) + ' / ' + fmt(TOTAL / 1000);
      const evs = EV[cur] || [];
      while (fi < evs.length && evs[fi][0] <= t) { if (playing) fire(evs[fi]); else instant(evs[fi]); fi++; }
      timers(calm); caption();
      if (thumb && !calm) thumb(T);
    }
    function loop(now) {
      raf = 0; if (!playing) return;
      t += Math.min(100, Math.max(0, now - last)); last = now;
      if (t >= DUR[cur - 1]) { if (cur < N) enter(cur + 1); else { t = DUR[cur - 1]; paint(); finish(); return; } }
      paint(); raf = requestAnimationFrame(loop);
    }
    function setBtn() {
      lab.textContent = playing ? 'Pause' : ended ? 'Replay' : 'Play';
      play.setAttribute('aria-label', playing ? 'Pause the film' : ended ? 'Play the film again' : 'Play the film');
      J.classList.toggle('playing', playing); J.classList.toggle('ended', ended);
    }
    function start() {
      if (playing) return;
      if (ended) { ended = false; enter(1); }
      geo(); playing = true; setBtn(); unTip();
      anims().forEach(a => { try { a.play(); } catch (e) {} });
      if (cur === 2 && video && video.getAttribute('src')) vPlay(null);
      if (soundOwner === J) { musicAt(START[cur - 1] + t); musicGo(); }
      last = performance.now(); if (!raf) raf = requestAnimationFrame(loop);
    }
    function pause() {
      playing = false; setBtn(); clearPk();
      anims().forEach(a => { try { a.pause(); } catch (e) {} });
      vPause(); if (soundOwner === J) musicHold();
      if (raf) { cancelAnimationFrame(raf); raf = 0; }
    }
    function finish() { pause(); ended = true; setBtn(); cam('W'); }
    /* seek anywhere: enter that chapter, apply its cues up to the moment, and wind every animation to it */
    function seek(T) {
      T = Math.max(0, Math.min(TOTAL - 1, T));
      let n = 1; while (n < N && T >= START[n]) n++;
      ended = false; enter(n); t = T - START[n - 1];
      const evs = EV[n] || []; while (fi < evs.length && evs[fi][0] <= t) { instant(evs[fi]); fi++; }
      anims().forEach(a => { try { a.currentTime = t; if (!playing) a.pause(); } catch (e) {} });
      if (video && n === 2 && t > 500) { if (playing) vPlay((t - 500) / 1000); else { vLoad(); try { video.currentTime = (t - 500) / 1000; } catch (e) {} vPaint(); } }
      paint(); setBtn();
      if (soundOwner === J) musicAt(T);
    }
    box.querySelectorAll('.snk-pdf').forEach(b => b.addEventListener('click', () => { if (playing) { held = true; pause(); } }));   /* the call script opens over a paused film */
    const qt = location.search.match(new RegExp('howt' + (jIdx ? '2' : '') + '=(\\d+)'));   /* QA hook: ?howt=<ms>, ?howt2=<ms> — park the film at that moment */
    const jump = n => { held = false; seek(START[n - 1]); if (!playing) start(); };

    /* hover anything — or tap it — to see what it does */
    let pinned = null;
    function showTip(el) {
      if (!tip || !el) return;
      tip.innerHTML = el.dataset.tip; const b = box.getBoundingClientRect(), r = el.getBoundingClientRect();
      tip.classList.add('on');
      const tw = tip.offsetWidth, th = tip.offsetHeight;
      let x = r.left - b.left + r.width / 2 - tw / 2, y = r.top - b.top - th - 10;
      if (y < 6) y = Math.min(b.height - th - 6, r.bottom - b.top + 10);
      x = Math.max(8, Math.min(b.width - tw - 8, x));
      tip.style.left = x + 'px'; tip.style.top = y + 'px';
    }
    function unTip() { if (tip) tip.classList.remove('on'); if (pinned) pinned.classList.remove('tipped'); pinned = null; }
    box.querySelectorAll('[data-tip]').forEach(el => {
      el.addEventListener('mouseenter', ev => { ev.stopPropagation(); if (!pinned) showTip(el); });
      el.addEventListener('mouseleave', () => { if (!pinned && tip) tip.classList.remove('on'); const p = el.parentElement && el.parentElement.closest('[data-tip]'); if (!pinned && p && p.matches(':hover')) showTip(p); });
      el.addEventListener('click', ev => {
        ev.stopPropagation();
        if (pinned === el) { unTip(); if (!calm) { held = false; start(); } return; }
        unTip(); pinned = el; el.classList.add('tipped'); showTip(el);
        if (playing) { held = true; pause(); }
        if (el === vid && video) { if (video.paused) vPlay(null, true); else vPause(); }
      });
    });

    /* controls */
    play.addEventListener('click', () => { if (calm) return; if (playing) { held = true; pause(); } else { held = false; if (soundOwner !== J && !muted) sound(true); start(); } });
    if (rp) rp.addEventListener('click', () => { if (!calm) jump(1); });
    steps.forEach((b, i) => b.addEventListener('click', () => { if (calm) { enter(i + 1); return; } jump(i + 1); }));
    if (scrub) {
      const at = ev => { const r = scrub.getBoundingClientRect(); return Math.max(0, Math.min(1, (ev.clientX - r.left) / r.width)) * TOTAL; };
      let drag = false;
      scrub.addEventListener('pointerdown', ev => { if (calm) return; drag = true; try { scrub.setPointerCapture(ev.pointerId); } catch (e) {} held = true; if (playing) pause(); seek(at(ev)); });
      scrub.addEventListener('pointermove', ev => { if (drag) seek(at(ev)); });
      scrub.addEventListener('pointerup', () => { if (!drag) return; drag = false; held = false; start(); });
      scrub.addEventListener('keydown', ev => { if (ev.key === 'ArrowRight' || ev.key === 'ArrowLeft') { ev.preventDefault(); ev.stopPropagation(); seek(START[cur - 1] + t + (ev.key === 'ArrowRight' ? 5000 : -5000)); } });
    }
    if (ccBtn) ccBtn.addEventListener('click', () => { const on = !ccBox.classList.contains('on'); ccBox.classList.toggle('on', on); ccBtn.classList.toggle('on', on); ccBtn.setAttribute('aria-pressed', on); });
    function sound(on) {
      S.querySelectorAll('.xsnd').forEach(b => { b.classList.remove('on'); b.setAttribute('aria-pressed', 'false'); b.querySelector('span').textContent = 'Music on'; });
      if (on) { soundOwner = J; padOn(); if (sndBtn) { sndBtn.classList.add('on'); sndBtn.setAttribute('aria-pressed', 'true'); sndBtn.querySelector('span').textContent = 'Music off'; } if (playing) { musicAt(START[cur - 1] + t); musicGo(); } }
      else { soundOwner = null; padOff(); }
    }
    if (sndBtn) sndBtn.addEventListener('click', () => {
      const on = soundOwner !== J; muted = !on; sound(on);
      if (on && !playing && !calm) { held = false; start(); }
    });

    /* at rest: the QA step, or the fullest frame of the story, plus the storyboard */
    const rest = q ? Math.min(N, Math.max(1, +q[1])) : (calm ? REST : 1);
    enter(rest); if (calm) paint();
    requestAnimationFrame(geo);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(geo);
    let rz; addEventListener('resize', () => { clearTimeout(rz); rz = setTimeout(() => { geo(); cam(focus, true); }, 120); });
    if (!calm) {
      anims().forEach(a => { try { a.pause(); } catch (e) {} }); paint();
      seen(box, v => {
        if (v === onScreen) return; onScreen = v;
        if (v) { geo(); vLoad(); if (!held && !ended) start(); }
        else { if (playing) pause(); if (soundOwner === J) { soundOwner = null; padOff(); if (sndBtn) { sndBtn.classList.remove('on'); sndBtn.querySelector('span').textContent = 'Music on'; } } }
      });
      document.addEventListener('visibilitychange', () => { if (document.hidden && playing) pause(); else if (!document.hidden && onScreen && !held && !ended) start(); });
    }
    if (/[?&]qa\b/.test(location.search)) (window.__how = window.__how || [])[jIdx] = {seek: ms => { held = true; if (playing) pause(); geo(); seek(ms); }, play: () => { held = false; start(); }, total: TOTAL, starts: START};
    if (qt && !calm) { held = true; requestAnimationFrame(() => requestAnimationFrame(() => { geo(); seek(+qt[1]); })); }
    addEventListener('beforeprint', () => { if (playing) pause(); enter(REST); (EV[REST] || []).forEach(instant); cam('W', true); timers(true); if (thumb) thumb(START[REST - 1] + DUR[REST - 1] - 1);
      steps.forEach((b, i) => { const f = b.querySelector('.pf'); if (f) f.style.transform = 'scaleX(' + (i + 1 <= REST ? 1 : 0) + ')'; }); });
  });
})();
