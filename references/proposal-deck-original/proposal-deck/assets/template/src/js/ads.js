/* ═══ the ads — flip for the strategy, swipe the carousel, count the number ═══ */
(function () {
  const calm = /noanim/.test(location.search) || matchMedia('(prefers-reduced-motion: reduce)').matches;
  ['ads1', 'ads2', 'ads3', 'ads4'].forEach(id => {
    const S = document.getElementById(id); if (!S) return;
    S.querySelectorAll('.adcell').forEach(cell => {
      const flip = () => cell.classList.toggle('flipped');
      cell.querySelectorAll('.whyb, .wback').forEach(b => b.addEventListener('click', flip));
      const back = cell.querySelector('.adback');
      if (back) new MutationObserver(() => back.setAttribute('aria-hidden', cell.classList.contains('flipped') ? 'false' : 'true'))
        .observe(cell, { attributes: true, attributeFilter: ['class'] });
    });
    S.querySelectorAll('.xa-car').forEach(car => {
      const track = car.querySelector('.xa-car-in'); if (!track) return;
      const step = () => { const c = track.querySelector('.xa-cc'); return c ? c.getBoundingClientRect().width + 6 : 200; };
      const pv = car.querySelector('.xa-prev'), nx = car.querySelector('.xa-next');
      if (pv) pv.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: 'smooth' }));
      if (nx) nx.addEventListener('click', () => track.scrollBy({ left: step(), behavior: 'smooth' }));
      /* hide the arrow that has nowhere to go, so it never sits over the first or last card */
      const ends = () => { car.classList.toggle('at-start', track.scrollLeft < 24);   /* snap rests ~11px in, on the track padding */
        car.classList.toggle('at-end', track.scrollLeft + track.clientWidth >= track.scrollWidth - 24); };
      track.addEventListener('scroll', ends, { passive: true }); ends();
    });
  });
  /* the big A$ number counts up once, the first time it is seen */
  const S2 = document.getElementById('ads2'); if (!S2) return;
  const el = S2.querySelector('.xa-num .u-n');
  if (!el || calm || !('IntersectionObserver' in window)) return;
  const to = +el.dataset.to || 240000, pre = el.dataset.pre || '$';
  const io = new IntersectionObserver(es => es.forEach(x => {
    if (!x.isIntersecting) return; io.disconnect();
    const t0 = performance.now(), D = 1600, delay = 500;
    const tick = now => {
      const p = Math.max(0, Math.min(1, (now - t0 - delay) / D)), e = 1 - Math.pow(1 - p, 3);
      el.textContent = pre + Math.round(to * e).toLocaleString(CFG.locale);
      if (p < 1) requestAnimationFrame(tick); else el.textContent = pre + to.toLocaleString(CFG.locale);
    };
    requestAnimationFrame(tick);
  }), { threshold: .5 });
  io.observe(el);
})();
