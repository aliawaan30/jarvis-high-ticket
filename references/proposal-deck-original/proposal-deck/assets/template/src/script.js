/* ═══ asset(path) — every asset path built in JavaScript goes through this. In index.html it returns the path unchanged;
   in standalone.html (one self-contained file) it returns the inlined copy, so each photo is stored once. ═══ */
function asset(p) { return (window.__ASSETS && window.__ASSETS[p]) || p; }

/* ═══ CONFIG — edit these and the whole document follows ═══ */
const CFG = {
  qual: 0.65,       // share of verified enquiries expected to score "call first"
  days: 30,         // a 90-day quarter: three months of 30 days
  price: 24000,     // the quarter, all in: A$12,000 Meta ad spend (A$4,000 × 3) + our A$12,000 fee. One quarter, paid on signing.
                    // If the client pays Meta on their own card instead, see references/offer-and-pricing.md → "Who pays for the ads".
  budgetM: 4000,    // Kestrel's monthly ad spend, as they told us
  paceC: 25,        // the planned AD cost per verified enquiry (ad spend only, not our fee): A$4,000 ÷ $25 = 160 a month
  stackBase: 46300, // the value stack, less the ad spend line (which follows the dial)
  locale: 'en-AU',  // number formatting
  cur: '$',         // currency symbol on money figures
  curShort: 'A$',   // the short form used where the currency must be explicit (e.g. the forecast's average sale)
  avgSale: 240000,  // the forecast's average sale if the page has no #sP slider (e.g. one flat price or fee)
};

const $  = q => document.querySelector(q);
const $$ = q => [...document.querySelectorAll(q)];
const aud = n => (n < 0 ? '\u2212' : '') + CFG.cur + Math.round(Math.abs(n)).toLocaleString(CFG.locale);
const set = (id, v) => { const el = document.getElementById(id); if (el) el.textContent = v; };

/* ═══ calculator — three linked dials: monthly budget, enquiries a day, cost per enquiry ═══
   budget = enquiries a day × cost per enquiry × 30. Move the budget or the cost and the enquiries follow;
   move the enquiries and the budget follows. */
const sB = $('#sB'), sE = $('#sE'), sC = $('#sC');
const INCLUDED = CFG.budgetM * 3;                                  /* the ad spend inside the price */
const FEE = CFG.price - INCLUDED;                                  /* our fee: everything else */
const oneDp = n => (Math.round(n * 10) / 10).toString();
function media() {
  const b = sB ? +sB.value : CFG.budgetM, c = sC ? +sC.value : CFG.paceC;
  const perMonth = Math.round(b / c);
  const daily = b / CFG.days;
  return { b, c, daily, e: daily / c, monthly: b, quarter: b * 3, perMonth, perQuarter: perMonth * 3,
           extra: Math.max(0, b * 3 - INCLUDED) };
}
function calc() {
  const m = media();
  set('vB', aud(Math.round(m.b / 10) * 10)); set('vC', '$' + m.c); set('vE', oneDp(m.e));
  if (sE && document.activeElement !== sE) sE.value = Math.min(+sE.max, Math.max(+sE.min, m.e)).toFixed(1);
  set('oDay', aud(m.daily));
  set('oL', m.perMonth.toLocaleString(CFG.locale));
  set('oM', aud(Math.round(m.monthly / 10) * 10));
  set('oQ', m.perQuarter.toLocaleString(CFG.locale));
  set('oT', aud(Math.round(m.quarter / 10) * 10));
  /* every dial-derived number anywhere in the deck: <span data-live="key"> follows the dials */
  const price = FEE + Math.round(m.quarter / 10) * 10;             /* all in: our fixed fee + the ad spend the dials set */
  const LIVE = {
    cpe: aud(m.c), daily: aud(m.daily), month: m.perMonth.toLocaleString(CFG.locale),
    quarterN: m.perQuarter.toLocaleString(CFG.locale), spendM: aud(Math.round(m.monthly / 10) * 10), spendQ: aud(Math.round(m.quarter / 10) * 10),
    price: aud(price), fee: aud(FEE), perAll: aud(price / Math.max(1, m.perQuarter)),
    callFirst: Math.round(m.perMonth * CFG.qual).toLocaleString(CFG.locale),
    incG: aud(Math.round(m.quarter / 10) * 10),
    wkN: Math.round(m.e * 7).toLocaleString(CFG.locale),          /* the example weekly report: a week at the pace on the dials */
    wk: aud(Math.round(m.e * 7) * m.c), cpq: aud(m.c / CFG.qual),
    stack: aud(CFG.stackBase + Math.round(m.quarter / 10) * 10), save: aud(CFG.stackBase + m.quarter - price),
  };
  $$('[data-live]').forEach(el => { const v = LIVE[el.dataset.live]; if (v !== undefined) el.textContent = v; });
  $$('#numbers .chip').forEach(ch => ch.classList.toggle('on', +ch.dataset.b === m.b && +ch.dataset.c === m.c));
  earn();
}
if (sB) {
  sB.addEventListener('input', calc);
  sC.addEventListener('input', calc);                              /* the budget holds; the enquiries a day follow */
  if (sE) sE.addEventListener('input', () => {                     /* the cost holds; the budget follows */
    const c = +sC.value;
    const b = Math.min(+sB.max, Math.max(+sB.min, +sE.value * c * CFG.days));
    sB.value = b;
    calc();
  });
  if (sE) sE.addEventListener('change', calc);
  $$('#numbers .chip').forEach(ch => ch.addEventListener('click', () => { sB.value = ch.dataset.b; sC.value = ch.dataset.c; calc(); }));
}

/* ═══ the forecast — their numbers only: enquiries in, sales value out ═══ */
function earn() {
  if (!$('#sS')) return;
  const m = media();
  const per   = +$('#sS').value;
  const price = $('#sP') ? +$('#sP').value * 1000 : CFG.avgSale;   /* no slider (one flat price) → CFG.avgSale */
  const q = m.perQuarter;
  const salesQ = q / per;
  const gross  = Math.round(salesQ * price / 100) * 100;
  set('vQ', q.toLocaleString(CFG.locale));
  set('qMo', '\u2248 ' + m.perMonth.toLocaleString(CFG.locale) + ' a month');
  set('vS', per);
  set('vP', CFG.curShort + Math.round(price / 1000) + 'k');
  set('regTot', q.toLocaleString(CFG.locale));
  set('regCopy', q.toLocaleString(CFG.locale));
  set('fSale', salesQ.toFixed(1));
  set('fPer', aud(price));
  set('fComm', aud(gross));
  set('fAd', '\u2212' + aud(m.quarter));
  set('fAdPer', aud(m.quarter / Math.max(0.1, salesQ)));
  set('fNet', aud(gross - m.quarter));
  set('fRoas', Math.round(gross / Math.max(1, m.quarter)) + '\u00d7');
}
['#sS', '#sP'].forEach(id => { if ($(id)) $(id).addEventListener('input', earn); });
calc();

/* ═══ summary — each stage opens for the detail ═══ */
$$('#summary .stage').forEach(st => {
  const flip = () => st.classList.toggle('open');
  st.addEventListener('click', ev => { if (ev.target.closest('a')) return; flip(); });
  st.addEventListener('keydown', ev => { if (ev.target !== st) return; if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); ev.stopPropagation(); flip(); } });
});

/* ═══ count-ups — <b class="cup" data-to="1630000" data-sep="1" data-pre="$" data-suf="+" data-dec="0"> counts up once on arrival ═══ */
(function(){
  const cups = [...document.querySelectorAll('.cup[data-to]')];
  if (!cups.length || /noanim/.test(location.search) || matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver(es => es.forEach(x => {
    if (!x.isIntersecting) return; io.unobserve(x.target);
    const el = x.target, to = +el.dataset.to, dec = +(el.dataset.dec || 0), suf = el.dataset.suf || '', pre = el.dataset.pre || '';
    const t0 = performance.now(), D = 1600;
    const tick = now => { const p = Math.min(1, (now - t0) / D), e = 1 - Math.pow(1 - p, 3);
      el.textContent = pre + (el.dataset.sep ? Math.round(to * e).toLocaleString(CFG.locale) : (to * e).toFixed(dec)) + suf; if (p < 1) requestAnimationFrame(tick); };
    requestAnimationFrame(tick);
  }), {threshold:.6});
  cups.forEach(c => io.observe(c));
})();



/* ═══ the weekly report — the attachment opens it ═══ */
(function(){
  const btn = document.getElementById('attachBtn'), doc = document.getElementById('reportDoc');
  if (!btn || !doc) return;
  btn.addEventListener('click', () => { const open = doc.classList.toggle('open'); btn.classList.toggle('on', open); });
  addEventListener('beforeprint', () => doc.classList.add('open'));
})();

/* ═══ reach — the map actually changes to the selected band ═══ */
const BAND = {
  A: {rings:['rA'], cities:['cPer'], tot:'2.9M+', totL:'Cumulative reach · tier one', tag:'TIER ONE · PERTH & WESTERN AUSTRALIA'},
  B: {rings:['rA','rB'], cities:['cPer','cBri'], tot:'8.5M+', totL:'Cumulative reach · tiers one–two', tag:'TIER TWO · + BRISBANE & THE GOLD COAST'},
  C: {rings:['rA','rB','rC'], cities:['cPer','cBri','cSyd','cMel'], tot:'24.0M+', totL:'Cumulative reach · tiers one–three', tag:'TIER THREE · + SYDNEY & MELBOURNE'},
  D: {rings:['rA','rB','rC','rD'], cities:['cPer','cBri','cSyd','cMel','cAde'], tot:'25.9M+', totL:'Cumulative reach · tiers one–four', tag:'TIER FOUR · + ADELAIDE'},
  E: {rings:['rA','rB','rC','rD','rE'], cities:['cPer','cBri','cSyd','cMel','cAde','cDar'], tot:'26.2M+', totL:'Cumulative reach · tiers one–five', tag:'TIER FIVE · + DARWIN'},
  F: {rings:['rA','rB','rC','rD','rE','rF'], cities:['cPer','cBri','cSyd','cMel','cAde','cDar','cCan','cHob'], tot:'27.2M+', totL:'Cumulative reach · every state and territory', tag:'TIER SIX · ALL OF AUSTRALIA'},
};
/* every ring and city id named in BAND — edit BAND (and the map's ids) and nothing else */
const RINGS = [...new Set(Object.values(BAND).flatMap(b => b.rings))];
const CITIES = [...new Set(Object.values(BAND).flatMap(b => b.cities))];
function setReach(k) {
  const b = BAND[k];
  $$('.rc').forEach(c => c.classList.toggle('on', c.dataset.r === k));
  RINGS.forEach(id => {
    const el = document.getElementById(id);
    if (!el) return;
    const on = b.rings.includes(id);
    el.style.opacity = on ? '1' : '.12';
    el.setAttribute('fill-opacity', on ? '1' : '.25');
  });
  CITIES.forEach(id => {
    const el = document.getElementById(id);
    if (!el) return;
    const inside = b.cities.includes(id);
    el.classList.toggle('inr', inside);
    el.classList.toggle('outr', !inside);
  });
  const t = $('#rTot'); if (t) t.textContent = b.tot;
  const tl = $('#rTotL'); if (tl) tl.textContent = b.totL;
  const tag = $('#bandTagT'); if (tag) tag.textContent = b.tag;
}
$$('.rc').forEach(c => c.addEventListener('click', () => setReach(c.dataset.r)));
if ($('.rc')) setReach(Object.keys(BAND)[0]);

/* ═══ instant form → the card your sales team receives (used by optional/s13a_leadform.html) ═══ */
/* The lead score, out of 100. Keys: the question index ('0'–'5', the option's data-q) → the option's data-v text,
   character for character (· middle dot, – en dash). If a question or an option changes, change it here, in the
   form's data-v, in facts.md and in the film, or that answer silently scores 0.
   The weighting: timeframe and funding weigh most (32 + 25 = 57 of the 100), because together they say whether
   this buyer can and will buy this quarter. Budget and suite say how big the sale is (14 + 11). The purpose and a
   past stay with the operator are fit and trust signals (8 + 10).
   Best answers: 11 + 8 + 14 + 32 + 25 + 10 = 100.
   The demo buyer, Sarah Mitchell: Garden Suite 7 + a bit of both 8 + around A$250k 6 + next 3 months 32
   + savings ready 25 + stayed many times 10 = 88 → "Call first" (72 and up).
   "Just researching" with every other answer at its best is 70, so a researcher never reaches "Call first". */
const SCORES = {
  /* 1. which suite: naming one means they know what they want; the Ocean Suite is the bigger sale */
  '0': {'Garden Suite · from US$165k':7, 'Ocean Suite · US$260k':11, 'Not sure yet':4},
  /* 2. what it's for: "a bit of both" uses the rental side and the Owners' Club, the fullest fit */
  '1': {'Rental income':6, 'Holidays':6, 'A bit of both':8},
  /* 3. budget (AUD): every band fits a suite; more room means more choice and a bigger sale */
  '2': {'Around A$250k':6, 'A$250k–A$400k':11, 'A$400k+':14},
  /* 4. timeframe: weighs most, because a buyer inside three months is the one to ring first */
  '3': {'In the next 3 months':32, '3–6 months':20, 'Just researching':2},
  /* 5. funding: second heaviest, because money ready is a buyer who can reserve now */
  '4': {'Savings or equity, ready':25, 'Arranging finance':14, 'Selling something first':8},
  /* 6. stayed at a Tidewater venue: knowing the operator is trust already earned */
  '5': {'Many times':10, 'Once or twice':7, 'Not yet':4},
};
function leadScore() {
  let s = 0;
  for (const q of ['0','1','2','3','4','5']) {
    const sel = document.querySelector(`.opt.sel[data-q="${q}"]`);
    if (sel) s += (SCORES[q] && SCORES[q][sel.dataset.v]) || 0;
  }
  const bar = document.getElementById('kScoreBar'), n = document.getElementById('kScoreN'), pri = $('#kPri');
  if (bar) bar.style.width = s + '%';
  if (n) n.textContent = s;
  if (pri) {
    const call = s >= 72, mid = s >= 48 && s < 72;
    pri.innerHTML = '<i></i>' + (call ? 'Call first' : mid ? 'Same-day follow-up' : 'Guide & nurture');
    pri.style.background = call ? 'rgba(181,122,46,.16)' : 'rgba(237,234,226,.07)';
    pri.style.borderColor = call ? 'rgba(181,122,46,.5)' : 'rgba(237,234,226,.22)';
    pri.style.color = call ? '#E2B872' : 'rgba(237,234,226,.6)';
  }
}
$$('.opt').forEach(o => o.addEventListener('click', () => {
  const qi = o.dataset.q;
  $$(`.opt[data-q="${qi}"]`).forEach(x => x.classList.remove('sel'));
  o.classList.add('sel');
  const cell = document.getElementById('k' + qi);
  if (cell) {
    const GOLD = {'2': /A\$250k–A\$400k|A\$400k\+/, '3': /next 3 months|3–6 months/, '4': /ready/, '5': /Many times/};
    cell.className = 'r' + (GOLD[qi] && GOLD[qi].test(o.dataset.v) ? ' gold' : '');
    cell.textContent = o.dataset.v;
    cell.animate([{opacity:.25},{opacity:1}], {duration:340, easing:'ease-out'});
  }
  leadScore();
}));
leadScore();

/* ═══ nav dots, scrollspy, progress ═══ */
const NAMES = { cover:'Cover', summary:'Summary', bridge:'The System', case:'Case Study', cases:'Past Results',
  ch1:'One · Opportunity', whynow:'Why Now', gap:'Why Kestrel Bay', catchment:'The Reach', numbers:'The Pace',
  forecast:'Your Numbers',
  ch2:'Two · The Campaign', how:'The Funnel', structure:'The Buyer Campaign', ads1:'Ads · Own at Kestrel Bay', ads2:'Ads · The Doubts',
  ads3:'Ads · The Owners\' Club', ads4:'Ads · Still Deciding', stories:'Stories', paper:'On Paper', reporting:'Your Report',
  ch3:'Three · The Case', included:'The Package',
  leadform:'The Form', decision:'Next Steps', finale:'Close' };
const DARK = new Set(['cover','ch1','ch2','ch3','finale']);
const secs = $$('.slide');
const dots = $('#dots');
secs.forEach(s => {
  const a = document.createElement('a');
  a.href = '#' + s.id;
  a.dataset.for = s.id;
  a.innerHTML = '<i>' + (NAMES[s.id] || s.id) + '</i>';
  a.addEventListener('click', ev => {
    ev.preventDefault();
    s.scrollIntoView({behavior:'instant', block:'start'});
    try { history.replaceState(null, '', '#' + s.id); } catch(e) {}
  });
  dots.appendChild(a);
});
function spy() {
  const y = scrollY + innerHeight * .4;
  let cur = secs[0];
  secs.forEach(s => { if (s.offsetTop <= y) cur = s; });
  $$('#dots a').forEach(a => a.classList.toggle('on', a.dataset.for === cur.id));
  dots.classList.toggle('light', DARK.has(cur.id));
  $('#bar').style.width = (scrollY / (document.documentElement.scrollHeight - innerHeight) * 100) + '%';
}
addEventListener('scroll', spy, {passive:true});
addEventListener('resize', spy);
spy();

/* QA hook — ?ovf writes any element that pokes outside the viewport into <body data-ovf> (headless overflow check) */
if (/[?&]ovf/.test(location.search)) setTimeout(() => {
  const W = innerWidth, bad = new Set();
  document.querySelectorAll('.slide *').forEach(el => { const r = el.getBoundingClientRect(); if (!(r.width > 0 && (r.right > W + 1 || r.left < -1))) return;
    let p = el.parentElement, clip = false;
    while (p && p !== document.body) { const cs = getComputedStyle(p); if (cs.overflowX !== 'visible' || cs.overflow === 'hidden') { const pr = p.getBoundingClientRect(); if (pr.right <= W + 1 && pr.left >= -1) { clip = true; break; } } p = p.parentElement; }
    if (!clip) bad.add((el.closest('.slide') || {}).id + ' ' + el.tagName.toLowerCase() + '.' + String(el.className && el.className.baseVal === undefined ? el.className : 'svg').split(' ').slice(0, 2).join('.')); });
  document.body.dataset.ovf = JSON.stringify({W, docW: document.documentElement.scrollWidth, bad: [...bad].slice(0, 30)});
}, 1500);
/* QA hook — ?offs writes every slide's top and height into <body data-offs> (headless screenshot planning) */
if (/[?&]offs/.test(location.search)) setTimeout(() => {
  const o = {}; document.querySelectorAll('section.slide').forEach(s => { o[s.id] = [s.offsetTop, s.offsetHeight]; });
  document.body.dataset.offs = JSON.stringify(o);
}, 1500);
/* QA hook — ?qa pins the cover to 900px so tall headless windows keep real offsets */
if (/[?&]qa/.test(location.search)) { const c = document.getElementById('cover'); if (c) c.style.minHeight = '900px'; }
/* QA hook — ?shift=<px> paints the page offset without scrolling (headless screenshots) */
(function(){const m=location.search.match(/shift=(\d+)/); if(m){document.documentElement.style.cssText+=';overflow:hidden;height:auto;'; document.body.style.cssText+=';transform:translateY(-'+m[1]+'px);';}})();
/* ═══ reveal on scroll — opt-in, so print and no-JS still show everything ═══ */
if ('IntersectionObserver' in window) {
  if (!location.href.includes('noanim')) document.body.classList.add('anim');
  const io = new IntersectionObserver(es => es.forEach(x => {
    if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); }
  }), {threshold:.08, rootMargin:'0px 0px -50px 0px'});
  $$('.rv').forEach(el => io.observe(el));
  addEventListener('beforeprint', () => $$('.rv').forEach(el => el.classList.add('in')));
}

/* ═══ keys: arrows step slides · n toggles presenter notes ═══ */
addEventListener('keydown', ev => {
  if (/INPUT|TEXTAREA/.test(document.activeElement.tagName)) return;
  if (ev.key === 'n' || ev.key === 'N') { document.body.classList.toggle('notes'); return; }
  const next = secs.find(s => s.offsetTop > scrollY + 12);
  const prev = secs.filter(s => s.offsetTop < scrollY - 12).pop();
  if ((ev.key === 'ArrowDown' || ev.key === 'PageDown' || ev.key === ' ') && next) {
    ev.preventDefault(); next.scrollIntoView({behavior:'smooth'});
  }
  if ((ev.key === 'ArrowUp' || ev.key === 'PageUp') && prev) {
    ev.preventDefault(); prev.scrollIntoView({behavior:'smooth'});
  }
});


