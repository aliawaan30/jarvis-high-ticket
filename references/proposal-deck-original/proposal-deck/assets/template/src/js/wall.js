/* ═══ the buyer campaign: tap a location on the map → its audience and its ads; products × locations × ads = live ads ═══
   All the words, photos and counts come from the JSON that build/gen_builds.py writes into the slide (.bx-data) — edit them there.
   D.n = {P products, L locations, ANG angles, F formats, ADS = ANG × F, SETS = P × L, TOTAL = SETS × ADS, rt = retargeting index or null} */
(function(){
  const S = document.getElementById('structure'); if (!S) return;
  const con = S.querySelector('.bx-con'), dEl = S.querySelector('.bx-data'), body = S.querySelector('.bx-body'), grid = S.querySelector('.bx-ads');
  if (!con || !dEl || !body) return;
  const D = JSON.parse(dEl.textContent), N = D.n;
  const calm = /noanim/.test(location.search) || matchMedia('(prefers-reduced-motion: reduce)').matches;
  const st = {r:0, p:0};
  const loc = r => D.locs[r][4].replace('&middot;', '·');
  const isRT = r => r === N.rt;
  const pl = (n, w) => n + ' ' + w + (n === 1 ? '' : 's');

  /* four layouts per format family (photo · carousel · short video · story), one per angle — sixteen different layouts in a
     4 × 4 ad set, no two alike; angles past the fourth reuse them in turn. The row is the angle, the column is the format.
     Photos are the client's own, picked per creative (P[5].s, index angle × F + format) so the picture matches the line;
     each location takes the next candidate. */
  const strip = h => h.replace(/<[^>]+>/g, '');
  function creative(P, a, f, r) {
    const A = D.ang[P[0]][a], L = D.locs[r];
    const one = c => c && c.length ? 'url(' + asset('assets/' + c[r % c.length]) + ')' : 'none';
    const img = n => one(P[5].s[n]);
    const pic = img(a * N.F + f), hook = P[6][a], ang = P[4][a], cta = P[7];
    const hd = () => '<div class="hd"><i></i><div><b>' + D.site.page + '</b><small>Sponsored</small></div></div>';
    const ct = '<div class="ct"><span>' + cta[0] + '</span><em>' + cta[1] + '</em></div>';
    const where = isRT(r) ? 'Australia' : strip(L[4]).replace('ACT · TAS · NT', 'ACT·TAS·NT');
    const dots = '<div class="cdt"><i></i><i></i><i></i><i></i><i></i></div>';
    const v = a % 4;                                         /* the layout variant */
    switch (D.fam[f] + v) {
      /* photo */
      case 'ph0': return hd() + '<div class="md"><div class="fill" style="background-image:' + pic + '"></div><span class="lk"></span><div class="t">' + hook + '</div></div>' + ct;
      case 'ph1': return hd() + '<div class="md"><div class="pn"><b>' + hook + '</b><small>' + ang + '</small></div><div class="ph" style="background-image:' + pic + '"></div></div>' + ct;
      case 'ph2': return hd() + '<div class="md"><div class="fill" style="background-image:' + pic + '"></div>' + (A.pre ? '<div class="l pre">' + A.pre + '</div>' : '') + '<div class="n' + (strip(A.num).length > 5 ? ' sm' : '') + '">' + A.num + '</div><div class="l">' + A.numL + '</div><span class="lk"></span></div>' + ct;
      case 'ph3': return hd() + '<div class="md"><div class="ph" style="background-image:' + pic + '"></div><div class="cd"><b>' + ang + '</b>' + A.checks.map(x => '<p>' + x + '</p>').join('') + '<span class="lk d"></span></div></div>' + ct;
      /* carousel */
      case 'ca0': return hd() + '<div class="tr"><div class="cd2"><div class="ph" style="background-image:' + pic + '"></div><span class="nn">1/5</span><div class="t">' + hook + '</div></div><div class="cd2 pk"><div class="ph" style="position:absolute;inset:0;background-image:' + one(P[5].k) + '"></div></div></div>' + dots + ct;
      case 'ca1': return hd() + '<div class="tr"><div class="cd2"><small>' + (A.sl || 'Step one') + '</small><u>01</u><b>' + A.steps[0] + '</b></div><div class="cd2 pk"><u>02</u><b>' + A.steps[1] + '</b></div></div>' + dots + ct;
      case 'ca2': return hd() + '<div class="tr"><div class="cd2"><span class="pin">&#128205; ' + D.site.pin + '</span><svg viewBox="39 15 26 20" aria-hidden="true"><path d="' + D.bali + '"/><circle cx="52.9" cy="29.3" r="1.1"/></svg><div class="t">' + hook + '</div></div><div class="cd2 pk"><div class="ph" style="position:absolute;inset:0;background-image:' + pic + '"></div></div></div>' + dots + ct;
      case 'ca3': return hd() + '<div class="tr"><div class="cd2"><u>Q.</u><b>' + A.qa[0] + '</b><span class="qs">Swipe for the answer &rarr;</span></div><div class="cd2 pk"><u>A.</u><b>' + A.qa[1] + '</b></div></div>' + dots + ct;
      /* short video */
      case 'vi0': { const w = strip(hook).split(' '); const on = Math.min(w.length - 1, 2 + v);
        return '<div class="fill" style="background-image:' + pic + '"></div>' + hd() + '<div class="kw">' + w.map((x, i) => '<span' + (i === on ? ' class="on"' : '') + '>' + x + '</span>').join('') + '</div><span class="snd">&#128263;</span><span class="tm">0:' + (14 + v * 7) + '</span><span class="pb"></span>'; }
      case 'vi1': return '<div class="fill" style="background-image:' + pic + '"></div>' + hd() + '<div class="ch"><span class="cq">' + A.chat[0] + '</span><span class="ca">' + A.chat[1] + '</span><em>Delivered</em></div><span class="snd">&#128263;</span><span class="tm">0:21</span><span class="pb"></span>';
      case 'vi2': return '<div class="fill" style="background-image:' + pic + '"></div>' + hd() + '<div class="bp"><div class="top"><span class="lk"></span><small>BOARDING PASS</small></div><div class="rt"><b>' + D.orig[L[0]] + '</b><i>&#9992;</i><b>' + D.site.dest[0] + '</b></div>'
        + '<div class="rw"><span>From<b>' + where + '</b></span><span>To<b>' + D.site.dest[1] + '</b></span><span>Seat<b>1A</b></span></div><p>' + hook + '</p></div><span class="tm">0:28</span><span class="pb"></span>';
      case 'vi3': return '<div class="pn"><b>' + ang + '</b><small>' + hook + '</small></div><div class="ph" style="background-image:' + pic + '"></div>' + hd() + '<span class="pl"></span><span class="pb"></span>';
      /* story */
      case 'st0': return '<div class="fill" style="background-image:' + pic + '"></div><div class="sg"><i></i><i></i><i></i></div>' + hd() + '<div class="poll"><b>' + A.poll[0] + '</b><span style="--v:0%">' + A.poll[1] + '</span><span style="--v:0%">' + A.poll[2] + '</span></div><span class="up">' + cta[1] + '</span>';
      case 'st1': return '<div class="fill" style="background-image:' + pic + '"></div><div class="sg"><i></i><i></i><i></i></div>' + hd() + '<div class="ask"><b>' + A.ask + '</b><span>Type something&hellip;</span></div><span class="up">' + cta[1] + '</span>';
      case 'st2': return '<div class="sg"><i></i><i></i><i></i></div>' + hd() + '<div class="cir" style="background-image:' + pic + '"></div><div class="t">' + hook + '</div><span class="lk"></span><span class="up">' + cta[1] + '</span>';
      default: /* st3 */ return '<div class="fill" style="background-image:' + pic + '"></div><div class="sg"><i></i><i></i><i></i></div>' + hd() + '<span class="loc">&#128205; ' + D.site.sticker + '</span><div class="t"><span>' + hook + '</span></div><span class="up">' + cta[1] + '</span>';
    }
  }
  const FCLS = {ph: '', ca: '', vi: 'vv', st: 'sv'}, LCLS = {ph: 'p', ca: 'c', vi: 'v', st: 's'};
  /* where a zoomed creative grows from, so it stays over the grid: the tuned values for four columns / rows, else evenly spread */
  const org = (i, n, four) => n === 4 ? four[i] : (n > 1 ? Math.round(i / (n - 1) * 100) : 50) + '%';

  function render(fresh) {
    const L = D.locs[st.r], P = D.prods[st.p];
    con.dataset.r = st.r; con.dataset.p = st.p;
    S.querySelectorAll('.bx-tab').forEach(b => { const on = +b.dataset.p === st.p; b.classList.toggle('on', on); b.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    S.querySelectorAll('.bx-chip').forEach(b => b.classList.toggle('on', +b.dataset.r === st.r));
    S.querySelector('.bx-lk').innerHTML = 'Location ' + (st.r + 1) + ' of ' + N.L + ' &middot; ' + (isRT(st.r) ? 'every state' : pl(N.P, 'ad set'));
    S.querySelector('.bx-dh h3').innerHTML = (isRT(st.r) ? 'Retargeting' : L[1]) + ' &times; <em>' + P[1] + '</em>';
    S.querySelector('.bx-m').innerHTML = (L[3] === 'Warm' ? L[2] + ' &middot; every state' : L[2]);
    S.querySelector('.bx-who ul').innerHTML = D.T[L[0]][P[0]].map((x, i) => '<li><i>' + (i + 1) + '</i><span>' + x + '</span></li>').join('');
    S.querySelector('.bx-who p').innerHTML = P[3];
    S.querySelector('.bx-as').innerHTML = '<b>Ad set ' + (st.r * N.P + st.p + 1) + ' of ' + N.SETS + '</b> &middot; ' + pl(N.ANG, 'angle') + ' &times; ' + pl(N.F, 'format') + ' = ' + pl(N.ADS, 'ad') + ' &middot; always on';
    let h = '';
    for (let a = 0; a < N.ANG; a++) {
      h += '<div class="bx-an"><small>Angle ' + (a + 1) + '</small>' + P[4][a] + '</div>';
      for (let f = 0; f < N.F; f++) h += '<div class="bx-cell" style="--k:' + (a * N.F + f) + '"><div class="bx-ad f' + f + ' ' + FCLS[D.fam[f]] + ' ' + LCLS[D.fam[f]] + (a % 4) + '" style="--ox:' + org(f, N.F, ['0%', '30%', '70%', '100%']) + ';--oy:' + org(a, N.ANG, ['0%', '35%', '65%', '100%'])
        + '" tabindex="0" role="img" aria-label="' + D.formats[f] + ' ad: ' + P[4][a].replace(/&[a-z]+;/g, "'") + '">' + creative(P, a, f, st.r) + '</div></div>';
    }
    body.innerHTML = h;
    const pc = D.panel[P[0]]; grid.style.setProperty('--pc', pc[0]); grid.style.setProperty('--pt', pc[1]);
    if (fresh && !calm) { grid.classList.remove('fresh'); void grid.offsetWidth; grid.classList.add('fresh'); }
  }
  const pick = (o, fresh) => { Object.assign(st, o); render(fresh); };
  /* in view? — IntersectionObserver where it works, plus a scroll check so it never silently fails */
  const seen = (el, f) => { const r = el.getBoundingClientRect(), h = innerHeight || 800; return r.top < h * (1 - f) && r.bottom > h * f; };
  const watch = (el, f, cb) => {
    let last = null;
    const check = () => { const v = seen(el, f); if (v !== last) { last = v; cb(v); } };
    if ('IntersectionObserver' in window) new IntersectionObserver(check, {threshold:[0, .15, .3, .5]}).observe(el);
    addEventListener('scroll', check, {passive:true}); addEventListener('resize', check); setTimeout(check, 300);
  };

  /* the auto-tour: walks every location, then the next product (wrapping round both) — until someone takes over */
  const tour = S.querySelector('.bx-tour'), STEP = 3800;
  let auto = null, playing = !calm, inView = false;
  const setBtn = () => { if (!tour) return; tour.setAttribute('aria-pressed', playing ? 'true' : 'false'); tour.querySelector('span').textContent = (playing || calm) ? 'Auto-tour' : 'Resume tour'; };
  const tick = () => { if (!tour) return; tour.classList.remove('run'); void tour.offsetWidth; if (playing && inView) { tour.style.setProperty('--t', STEP + 'ms'); tour.classList.add('run'); } };
  const run = () => {
    clearInterval(auto); tick();
    if (!playing || !inView) return;
    auto = setInterval(() => { const r = (st.r + 1) % N.L; pick({r, p: r === 0 ? (st.p + 1) % N.P : st.p}, true); tick(); }, STEP);
  };
  const stop = () => { playing = false; setBtn(); run(); };
  if (tour) tour.addEventListener('click', () => { playing = !playing; setBtn(); run(); });
  setBtn();
  if (!calm) watch(con, .2, v => { inView = v; run(); });

  S.querySelectorAll('.bx-tab').forEach(b => b.addEventListener('click', () => { stop(); pick({p:+b.dataset.p}, true); }));
  S.querySelectorAll('.bx-chip, .bx-hit, .bx-rt').forEach(b => {
    b.addEventListener('click', () => { stop(); pick({r:+b.dataset.r}, true); });
    b.addEventListener('keydown', ev => { if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); stop(); pick({r:+b.dataset.r}, true); } });
  });
  body.addEventListener('click', ev => {                     /* tap to zoom (touch) — tap again or elsewhere to close */
    const c = ev.target.closest('.bx-cell'); stop();
    S.querySelectorAll('.bx-cell.z').forEach(x => { if (x !== c) x.classList.remove('z'); });
    if (c) c.classList.toggle('z');
  });
  document.addEventListener('click', ev => { if (!ev.target.closest('#structure .bx-cell')) S.querySelectorAll('.bx-cell.z').forEach(x => x.classList.remove('z')); });
  body.addEventListener('pointerenter', ev => { if (ev.pointerType === 'mouse') stop(); });
  render(false);

  /* the multiplication — P products → × L = SETS ad sets → × ADS = TOTAL live ads; plays once on arrival, replays on demand */
  const mx = S.querySelector('.bx-mx'), big = S.querySelector('.bx-total');
  if (mx) {
    mx.querySelectorAll('.bx-blk').forEach(b => b.addEventListener('click', () => {
      stop(); pick({r:+b.dataset.r, p:+b.dataset.p}, true);
      con.scrollIntoView({behavior:calm ? 'auto' : 'smooth', block:'start'});
    }));
    let timers = [];
    const play = () => {
      timers.forEach(clearTimeout); timers = [];
      mx.dataset.s = '0'; if (big) big.textContent = '0';
      const at = (fn, t) => timers.push(setTimeout(fn, t));
      at(() => mx.dataset.s = '1', 250); at(() => mx.dataset.s = '2', 1350); at(() => mx.dataset.s = '3', 2450); at(() => mx.dataset.s = '4', 4800);
      at(() => { const t0 = performance.now(); const f = now => { const p = Math.min(1, (now - t0) / 1300), e = 1 - Math.pow(1 - p, 3); if (big) big.textContent = Math.round(N.TOTAL * e); if (p < 1) requestAnimationFrame(f); }; requestAnimationFrame(f); }, 2450);
      at(() => { mx.dataset.s = '4'; if (big) big.textContent = String(N.TOTAL); }, 6000);   /* belt and braces: always lands on the final state */
    };
    const rp = mx.querySelector('.bx-replay'); if (rp) rp.addEventListener('click', () => calm ? null : play());
    if (!calm) { let done = false; watch(mx, .15, v => { if (v && !done) { done = true; play(); } }); }
    addEventListener('beforeprint', () => { timers.forEach(clearTimeout); mx.dataset.s = '4'; if (big) big.textContent = String(N.TOTAL); });
  }
  const q = location.search.match(/loc=(\w+)/); if (q) { const i = D.locs.findIndex(l => l[0] === q[1]); if (i >= 0) pick({r:i}, false); }   /* QA hook */
  const qp = location.search.match(/prod=(\d)/); if (qp) pick({p:+qp[1]}, false);
  const qz = location.search.match(/zoom=(\d+)/); if (qz) { const c = S.querySelectorAll('.bx-cell')[+qz[1]]; if (c) c.classList.add('z'); }
})();
