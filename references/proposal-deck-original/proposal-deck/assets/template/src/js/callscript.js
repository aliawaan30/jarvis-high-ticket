/* ═══ the call script — opens as a page over the deck, no download needed ═══ */
(function(){
  const css = `
  .csp{position:fixed;inset:0;z-index:9999;display:flex;align-items:center;justify-content:center;padding:24px 16px;
    background:rgba(10,22,32,.72);backdrop-filter:blur(3px);opacity:0;transition:opacity .25s ease}
  .csp.on{opacity:1}
  .csp-in{position:relative;display:flex;flex-direction:column;max-height:100%;width:min(640px,100%);background:#fff;border-radius:12px;
    box-shadow:0 24px 60px rgba(0,0,0,.4);overflow:hidden}
  .csp-bar{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 12px 10px 18px;background:#13283A;color:#FBF7F0;
    font:600 12px/1.2 'Jost',system-ui,sans-serif;letter-spacing:.06em}
  .csp-bar span{opacity:.7;font-weight:400;margin-left:8px}
  .csp-x{border:0;background:rgba(255,255,255,.12);color:#fff;width:30px;height:30px;border-radius:50%;font-size:17px;line-height:1;cursor:pointer}
  .csp-x:hover{background:rgba(255,255,255,.25)}
  .csp-pg{overflow:auto;-webkit-overflow-scrolling:touch}
  .csp-pg img{display:block;width:100%;height:auto}
  @media print{.csp{display:none!important}}`;
  let box = null;
  const close = () => { if (!box) return; const b = box; box = null; b.classList.remove('on'); setTimeout(() => b.remove(), 250); document.removeEventListener('keydown', onKey); };
  const onKey = e => { if (e.key === 'Escape') close(); };
  const open = () => {
    if (box) return;
    if (!document.getElementById('csp-css')) { const s = document.createElement('style'); s.id = 'csp-css'; s.textContent = css; document.head.appendChild(s); }
    box = document.createElement('div'); box.className = 'csp'; box.setAttribute('role', 'dialog'); box.setAttribute('aria-label', 'Call script');
    box.innerHTML = '<div class="csp-in"><div class="csp-bar"><div>The call script<span>Kestrel Bay Resort &middot; new enquiry call &middot; one page</span></div>'
      + '<button type="button" class="csp-x" aria-label="Close">&times;</button></div>'
      + '<div class="csp-pg"><img src="' + asset('assets/call-script.jpg') + '" alt="The Kestrel Bay Resort enquiry call script: call within the first minute, send the pack while on the phone, book a private video call with the sales team for tomorrow"></div></div>';
    box.addEventListener('click', e => { if (e.target === box || e.target.closest('.csp-x')) close(); });
    document.body.appendChild(box); requestAnimationFrame(() => box && box.classList.add('on'));
    document.addEventListener('keydown', onKey); box.querySelector('.csp-x').focus();
  };
  document.addEventListener('click', e => { const b = e.target.closest('[data-pop="callscript"]'); if (b) { e.preventDefault(); open(); } });
})();
