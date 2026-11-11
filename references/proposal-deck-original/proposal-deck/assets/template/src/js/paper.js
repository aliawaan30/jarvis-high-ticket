/* ═══ the strategy on paper — eight A4 pages; they deal out from a stack, tap one to read it full size ═══ */
(function(){
  const S = document.getElementById('paper'); if (!S) return;
  const still = /noanim/.test(location.search) || (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches);
  const docs = [...S.querySelectorAll('.mkp-doc')], cards = [...S.querySelectorAll('.mkp-card')];
  const grid = S.querySelector('.mkp-grid');
  const dlg = S.querySelector('.mkp-dlg'), view = S.querySelector('.mkp-view');
  const tabs = [...S.querySelectorAll('.mkp-dtabs button')];
  const prev = S.querySelector('.mkp-prev'), next = S.querySelector('.mkp-next');
  if (!docs.length || !dlg || !view) return;

  /* thumbnails: scale the 600px artboard to the card width */
  function fit() { docs.forEach(d => { const w = d.clientWidth; if (w) d.style.setProperty('--mkp-s', (w / 600).toFixed(4)); }); }
  fit(); if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
  let rt; addEventListener('resize', () => { clearTimeout(rt); rt = setTimeout(() => { fit(); if (cur > -1) size(); }, 100); });

  /* deal-in: stacked in the middle of the desk, then fanned out to the grid (once) */
  function stack() {
    const g = grid.getBoundingClientRect(), cx = g.left + g.width / 2, cy = g.top + g.height / 2;
    cards.forEach((c, i) => {
      c.style.transition = 'none';
      const r = c.getBoundingClientRect();
      c.style.transform = `translate(${cx - (r.left + r.width / 2)}px, ${cy - (r.top + r.height / 2)}px) rotate(${(i - 3.5) * 2.4}deg)`;
      c.style.zIndex = String(10 - i);
    });
    grid.offsetHeight; // commit
    cards.forEach(c => { c.style.transition = ''; });
  }
  function deal() { cards.forEach(c => { c.style.transform = ''; }); setTimeout(() => cards.forEach(c => { c.style.zIndex = ''; }), 1400); }
  if (!still && 'IntersectionObserver' in window) {
    let done = false;
    requestAnimationFrame(stack);
    const io = new IntersectionObserver(es => { es.forEach(e => { if (e.isIntersecting && !done) { done = true; setTimeout(deal, 350); io.disconnect(); } }); }, { threshold: 0.3 });
    io.observe(grid);
    addEventListener('beforeprint', () => { if (!done) { done = true; io.disconnect(); } cards.forEach(c => { c.style.transition = 'none'; c.style.transform = ''; c.style.zIndex = ''; }); });
  }

  /* reader dialog with prev / next */
  let cur = -1, s = 1, lastFocus = null;
  function size() {
    const inn = view.firstElementChild; if (!inn) return;
    if (innerWidth <= 520) { view.style.width = view.style.height = ''; inn.style.transform = ''; return; }
    const bar = S.querySelector('.mkp-bar').offsetHeight || 56;
    s = Math.min((innerWidth - 150) / 600, (innerHeight - bar - 26) / 848, 1.35);
    s = Math.max(s, 0.5);
    view.style.width = Math.round(600 * s) + 'px'; view.style.height = Math.round(848 * s) + 'px';
    inn.style.transform = `scale(${s})`;
  }
  function show(i) {
    cur = Math.max(0, Math.min(docs.length - 1, i));
    view.innerHTML = docs[cur].querySelector('.mkp-in').outerHTML;
    size();
    tabs.forEach((t, k) => { t.classList.toggle('on', k === cur); t.setAttribute('aria-current', k === cur ? 'page' : 'false'); });
    const t = tabs[cur]; if (t && t.scrollIntoView) t.scrollIntoView({ block: 'nearest', inline: 'nearest' });
    prev.disabled = cur === 0; next.disabled = cur === docs.length - 1;
    S.querySelector('.mkp-stage').scrollTop = 0;
  }
  function open(i) {
    lastFocus = document.activeElement;
    dlg.classList.add('on'); dlg.setAttribute('aria-hidden', 'false');
    document.documentElement.style.overflow = 'hidden';
    show(i);
    S.querySelector('.mkp-x').focus({ preventScroll: true });
  }
  function shut() {
    if (cur < 0) return;
    dlg.classList.remove('on'); dlg.setAttribute('aria-hidden', 'true');
    document.documentElement.style.overflow = '';
    view.innerHTML = ''; cur = -1;
    if (lastFocus && lastFocus.focus) lastFocus.focus({ preventScroll: true });
  }
  docs.forEach((d, i) => {
    d.addEventListener('click', () => open(i));
    d.addEventListener('keydown', ev => { if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); open(i); } });
  });
  tabs.forEach((t, k) => t.addEventListener('click', () => show(k)));
  prev.addEventListener('click', () => show(cur - 1));
  next.addEventListener('click', () => show(cur + 1));
  S.querySelector('.mkp-x').addEventListener('click', shut);
  dlg.addEventListener('click', ev => { if (ev.target === dlg || ev.target.classList.contains('mkp-stage')) shut(); });
  addEventListener('keydown', ev => {
    if (cur < 0) return;
    if (ev.key === 'Escape') shut();
    else if (ev.key === 'ArrowRight') { ev.preventDefault(); show(cur + 1); }
    else if (ev.key === 'ArrowLeft') { ev.preventDefault(); show(cur - 1); }
  });
  /* swipe between pages on touch screens */
  let tx = null, ty = 0;
  view.addEventListener('touchstart', ev => { const t = ev.touches[0]; tx = t.clientX; ty = t.clientY; }, { passive: true });
  view.addEventListener('touchend', ev => {
    if (tx === null) return; const t = ev.changedTouches[0], dx = t.clientX - tx, dy = t.clientY - ty; tx = null;
    if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.5) show(cur + (dx < 0 ? 1 : -1));
  }, { passive: true });
  addEventListener('beforeprint', () => { shut(); fit(); });
})();
