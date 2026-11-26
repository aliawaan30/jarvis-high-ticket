(() => {
  'use strict';
  const cfg = window.HUB_CONFIG || {};
  const DEMO = !cfg.supabaseUrl || new URLSearchParams(location.search).has('demo');
  const $app = document.getElementById('app');
  let SITE, sb, session, member, progress = {};
  const openStep = {}; // page slug -> step id the student opened

  const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const toast = (msg) => { const t = document.getElementById('toast'); t.textContent = msg; t.classList.add('show'); clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('show'), 2200); };
  const kb = (n) => n > 1048576 ? (n / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(n / 1024)) + ' KB';

  // ---------- data ----------
  const store = {
    async load() {
      if (DEMO) {
        try { progress = JSON.parse(localStorage.getItem('hub-demo') || '{}'); } catch { progress = {}; }
        member = { email: 'demo@example.com', name: 'Demo', update_code: '00000000-0000-0000-0000-000000000000' };
        return;
      }
      const [m, p] = await Promise.all([
        sb.from('members').select('email,name,update_code').maybeSingle(),
        sb.from('progress').select('item,value'),
      ]);
      member = m.data || { email: session.user.email };
      progress = Object.fromEntries((p.data || []).map((r) => [r.item, r.value]));
    },
    async set(item, value) {
      if (value === null) delete progress[item]; else progress[item] = value;
      if (DEMO) { try { localStorage.setItem('hub-demo', JSON.stringify(progress)); } catch {} return; }
      const q = value === null
        ? sb.from('progress').delete().eq('item', item)
        : sb.from('progress').upsert({ user_id: session.user.id, item, value, updated_at: new Date().toISOString() });
      const { error } = await q;
      if (error) toast('Could not save. Check your connection.');
    },
    async ticket(t) {
      if (DEMO) return true;
      const { error } = await sb.from('tickets').insert({ user_id: session.user.id, ...t });
      return !error;
    },
    async download(pack) {
      if (window.__SITE) return toast('Downloads work on the live hub.');
      if (DEMO) { location.href = 'demo-packs/' + pack.file; return; }
      const r = await fetch('/api/pack?pack=' + encodeURIComponent(pack.id), { headers: { Authorization: 'Bearer ' + session.access_token } });
      const j = await r.json().catch(() => ({}));
      if (!r.ok || !j.url) return toast(j.error || 'Download failed. Try again.');
      location.href = j.url;
    },
  };

  // ---------- helpers ----------
  const origin = () => (/^https?:/.test(location.origin) ? location.origin : 'https://your-hub.netlify.app');
  const updateLink = () => member?.update_code ? `${origin()}/api/pack?code=${member.update_code}` : '';
  const embedUrl = (u) => {
    let m;
    if ((m = u.match(/loom\.com\/(?:share|embed)\/([\w-]+)/))) return `https://www.loom.com/embed/${m[1]}`;
    if ((m = u.match(/(?:youtube\.com\/watch\?v=|youtu\.be\/)([\w-]+)/))) return `https://www.youtube.com/embed/${m[1]}`;
    if ((m = u.match(/vimeo\.com\/(\d+)/))) return `https://player.vimeo.com/video/${m[1]}`;
    return u;
  };
  const video = (u, cap) => `<figure class="media"><div class="video"><iframe src="${esc(embedUrl(u))}" allow="fullscreen; picture-in-picture" allowfullscreen loading="lazy"></iframe></div>${cap ? `<figcaption>${esc(cap)}</figcaption>` : ''}</figure>`;
  const LOGO = `<svg class="logo" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="18" fill="none" stroke="#52b5ff" stroke-width="2.2" stroke-dasharray="7 3"/><circle cx="20" cy="20" r="12.5" fill="none" stroke="#52b5ff" stroke-opacity=".35" stroke-width="1"/><path d="M20 11.5 L28.5 26.5 H11.5 Z" fill="none" stroke="#f5b13d" stroke-width="2.2" stroke-linejoin="round"/><path d="M20 18 L24.6 25 H15.4 Z" fill="#f5b13d"/></svg>`;

  // The Jarvis core as a progress ring: blue arc = progress, amber triangle in the middle.
  function core(pct, size = 220) {
    const r = 82, c = 2 * Math.PI * r, arc = (c * pct) / 100;
    const ticks = Array.from({ length: 60 }, (_, i) => {
      const a = (i / 60) * 2 * Math.PI, r1 = 104, r2 = i % 5 ? 108 : 112;
      return `<line x1="${120 + r1 * Math.sin(a)}" y1="${120 - r1 * Math.cos(a)}" x2="${120 + r2 * Math.sin(a)}" y2="${120 - r2 * Math.cos(a)}"/>`;
    }).join('');
    return `<svg class="core" width="${size}" height="${size}" viewBox="0 0 240 240" aria-hidden="true">
      <defs><linearGradient id="coreGrad" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#32d09f"/><stop offset="1" stop-color="#8b5cf6"/></linearGradient></defs>
      <g class="core-ticks">${ticks}</g>
      <circle cx="120" cy="120" r="${r}" class="core-track"/>
      <circle cx="120" cy="120" r="${r}" class="core-arc" stroke-dasharray="${arc} ${c}" transform="rotate(-90 120 120)"/>
      <circle cx="120" cy="120" r="58" class="core-inner"/>
      <path d="M120 86 L150 140 H90 Z" class="core-tri"/><path d="M120 110 L136 137 H104 Z" class="core-tri-fill"/>
    </svg>`;
  }

  const packById = (id) => SITE.packs.find((p) => p.id === id);
  const stepKey = (page, step) => `step:${page.slug}:${step.id}`;
  const isSoon = (s) => /coming soon/i.test(s.time);
  const tracked = (page) => page.track !== 'no';
  const pageDone = (page) => {
    const req = tracked(page) ? page.steps.filter((s) => !s.optional && !isSoon(s)) : [];
    const done = req.filter((s) => progress[stepKey(page, s)]).length;
    return { done, total: req.length, pct: req.length ? Math.round((100 * done) / req.length) : 0 };
  };
  const needsUpdate = (pack) => progress['pack:' + pack.id] && progress['pack:' + pack.id] !== pack.version;
  const pageNeedsUpdate = (page) => page.packs.some((id) => needsUpdate(packById(id)));
  const modules = () => SITE.pages.filter((p) => p.module > 0).sort((a, b) => a.module - b.module);
  const nextStep = (p) => !tracked(p) ? null : p.steps.find((s) => !isSoon(s) && !s.optional && !progress[stepKey(p, s)])
    || p.steps.find((s) => !isSoon(s) && !progress[stepKey(p, s)]);
  const status = (p) => { const d = pageDone(p); return d.total && d.done === d.total ? 'done' : d.done ? 'doing' : 'todo'; };
  const totals = () => modules().map(pageDone).reduce((a, c) => ({ done: a.done + c.done, total: a.total + c.total }), { done: 0, total: 0 });

  // Where the student should be right now.
  function resume() {
    const newPage = SITE.pages.find((p) => p.slug === 'new');
    if (progress.path === 'new' && newPage && status(newPage) !== 'done') return { page: newPage, step: nextStep(newPage) };
    const p = modules().find((m) => status(m) !== 'done') || modules()[modules().length - 1];
    return { page: p, step: nextStep(p) };
  }

  // ---------- blocks ----------
  function blocks(list) {
    return list.map((b) => {
      switch (b.type) {
        case 'p': return `<p>${b.html}</p>`;
        case 'list': return `<ol>${b.items.map((i) => `<li>${i}</li>`).join('')}</ol>`;
        case 'see': return `<div class="note see"><b>You'll see</b>${b.html}</div>`;
        case 'fix': return `<div class="note fix"><b>If it looks different</b>${b.html}</div>`;
        case 'prompt': {
          const text = b.text.replace(/\{\{update_link\}\}/g, updateLink() || '[your update link]');
          return `<div class="prompt"><div class="prompt-head"><span>${esc(b.label)}</span><button data-copy>Copy</button></div><pre>${esc(text)}</pre></div>`;
        }
        case 'pack': {
          const p = packById(b.id);
          const installed = progress['pack:' + p.id];
          const badge = needsUpdate(p) ? `<span class="badge update">Update available</span>` : installed ? `<span class="badge installed">Installed</span>` : '';
          const skills = p.skills.length ? `${p.skills.length} skills, ` : '';
          return `<div class="pack"><div class="pack-icon">ZIP</div><div class="pack-info"><b>${esc(p.title)}${badge}</b><small>${skills}version ${esc(p.version)}, ${kb(p.size)}. Don't unzip it.</small></div><button class="btn primary" data-dl="${esc(p.id)}">Download</button></div>`;
        }
        case 'link': {
          const target = SITE.pages.find((x) => x.slug === b.id);
          return `<div class="linkcard"><a class="btn" href="#/${esc(b.id)}">Open the ${esc(target ? target.title : b.id)} page</a></div>`;
        }
        case 'ext': return `<div class="linkcard"><a class="btn primary" href="${esc(b.url)}" target="_blank" rel="noopener">${esc(b.label)}</a></div>`;
        case 'image': return `<figure class="media${b.phone ? ' phone' : ''}"><img src="${esc(b.src)}" alt="${esc(b.caption)}" loading="lazy">${b.caption ? `<figcaption>${esc(b.caption)}</figcaption>` : ''}</figure>`;
        case 'video': return video(b.url, b.caption);
        case 'updatelink': return `<div class="updatelink">${esc(updateLink() || 'Sign in to see your link')}</div>`;
        default: return '';
      }
    }).join('');
  }

  // ---------- sidebar ----------
  function nav(current) {
    const extra = SITE.pages.filter((p) => p.module === 0 && p.slug !== 'new');
    const newPage = SITE.pages.find((p) => p.slug === 'new');
    const showNew = newPage && progress.path !== 'existing';
    const t = totals();
    const item = (p, label) => {
      const d = pageDone(p), st = status(p);
      return `<a href="#/${p.slug}" class="${current === p.slug ? 'on' : ''} ${st}"><span class="num">${st === 'done' ? '&#10003;' : label}</span><span class="nt">${esc(p.title)}</span>${pageNeedsUpdate(p) ? '<span class="dot" title="Update available"></span>' : ''}${d.total && st !== 'done' ? `<span class="mini-ring" style="--p:${d.pct}"></span>` : ''}</a>`;
    };
    return `<aside class="side">
      <a class="brand" href="#/welcome">${LOGO}<span>${esc(SITE.site.name)}</span></a>
      ${DEMO ? '<div class="demo-banner">Preview mode. Ticks save in this browser only. <a href="#/login">See the sign in screen</a></div>' : ''}
      <div class="overall"><div class="overall-row"><span>Your progress</span><b>${t.total ? Math.round((100 * t.done) / t.total) : 0}%</b></div><div class="bar"><i style="width:${t.total ? Math.round((100 * t.done) / t.total) : 0}%"></i></div></div>
      <nav class="nav">
        <a href="#/welcome" class="${current === 'welcome' ? 'on' : ''}"><span class="num">&#9679;</span><span class="nt">Start here</span></a>
        ${showNew ? item(newPage, 'N') : ''}
        <div class="nav-label">Modules</div>
        ${modules().map((p) => item(p, p.module)).join('')}
        <div class="nav-label">Any time</div>
        ${extra.map((p) => item(p, p.slug === 'help' ? '?' : 'W')).join('')}
      </nav>
      <div class="side-foot">${esc(member?.email || '')}${DEMO ? '' : '<br><button data-signout>Sign out</button>'}</div>
    </aside>`;
  }

  // ---------- welcome ----------
  function welcome() {
    const s = SITE.site, t = totals(), pct = t.total ? Math.round((100 * t.done) / t.total) : 0;
    const name = member?.name ? `, ${esc(member.name)}` : '';
    const r = resume();
    const started = t.done > 0 || (progress.path === 'new' && SITE.pages.find((p) => p.slug === 'new') && pageDone(SITE.pages.find((p) => p.slug === 'new')).done > 0);
    const where = r.page.module ? `Module ${r.page.module}` : r.page.title;

    const heroAction = !progress.path
      ? `<div class="hero-q"><p>First, one question. Have you already set up Jarvis from the free course?</p>
          <div class="cta"><button class="btn light" data-path="existing">Yes, I have Jarvis</button><button class="btn ghost" data-path="new">No, I'm new to Jarvis</button></div></div>`
      : `<div class="hero-next"><small>${started ? 'Pick up where you left off' : 'Your first step'}</small>
          <b>${esc(r.step ? r.step.title : r.page.title)}</b><span>${esc(where)}${r.step && r.step.time ? ' · ' + esc(r.step.time) : ''}</span>
          <div class="cta"><a class="btn light" href="#/${r.page.slug}">${started ? 'Continue' : 'Start now'}</a><button class="btn ghost" data-path="">Change my answer</button></div></div>`;

    let given = false;
    const journey = modules().map((p) => {
      let st = status(p);
      if (st !== 'done' && !given) { st = st === 'todo' ? 'next' : st; given = true; }
      const d = pageDone(p);
      const label = { done: 'Done', doing: 'In progress', next: 'Up next', todo: '' }[st];
      return `<a class="jrow ${st}" href="#/${p.slug}">
        <span class="jnum">${st === 'done' ? '&#10003;' : String(p.module).padStart(2, '0')}</span>
        <span class="jbody"><b>${esc(p.title)}</b><span>${esc(p.short)}</span></span>
        <span class="jside">${label ? `<em>${label}</em>` : ''}<span class="jbar"><i style="width:${d.pct}%"></i></span><small>${esc(p.time)}</small></span></a>`;
    }).join('');

    return `<section class="hero-band">
        <div class="hero-copy"><div class="eyebrow">Jarvis 2.0 programme</div><h1>Welcome${name}.</h1>
        <p class="lede">${esc(s.programme)}. Every file, every message and every step, in order.</p>${heroAction}</div>
        <div class="hero-core">${core(pct)}<div class="core-label"><b>${pct}%</b><span>${t.done} of ${t.total} steps</span></div></div>
      </section>
      ${s.video_url ? video(s.video_url, 'Start here: a quick welcome') : ''}
      <div class="block-title"><h2>Your journey</h2><span>7 modules to your first client live</span></div>
      <div class="journey">${journey}</div>
      ${s.sections.map((sec) => `<div class="section"><h2>${esc(sec.title)}</h2>${blocks(sec.blocks)}</div>`).join('')}`;
  }

  // ---------- module page ----------
  function page(p) {
    const ordered = modules(), idx = ordered.indexOf(p);
    const prev = idx > 0 ? ordered[idx - 1] : null, next = idx >= 0 && idx < ordered.length - 1 ? ordered[idx + 1] : null;
    const d = pageDone(p);
    const current = nextStep(p);
    const open = openStep[p.slug] ?? (current ? current.id : tracked(p) ? null : p.steps[0]?.id);
    const eyebrow = p.module ? `Module ${p.module}` : p.slug === 'new' ? 'Before Module 1' : 'Any time';
    const facts = [['Time', p.time], ['Ready when', p.gate], ['You get', p.outcome], ['Missions', p.missions]]
      .filter(([, v]) => v && v !== 'none' && v !== 'None.').map(([k, v]) => `<div class="fact"><b>${k}</b><span>${esc(v)}</span></div>`).join('');

    let n = 0;
    const steps = p.steps.map((s) => {
      const key = stepKey(p, s), done = !!progress[key], soon = isSoon(s), isOpen = s.id === open, isNext = current && s.id === current.id;
      n += 1;
      const tags = [s.time && !soon ? `<span class="tag">${esc(s.time)}</span>` : '', s.optional ? '<span class="tag">Optional</span>' : '', soon ? '<span class="tag">Coming soon</span>' : '', isNext && !isOpen ? '<span class="tag next">Up next</span>' : ''].join('');
      return `<section class="step ${done ? 'is-done' : ''} ${isOpen ? 'is-open' : ''} ${isNext ? 'is-next' : ''}" id="${esc(s.id)}">
        <button class="step-head" data-open="${esc(s.id)}" aria-expanded="${isOpen}"><span class="step-n">${done ? '&#10003;' : n}</span><span class="step-title">${esc(s.title)}${tags}</span><span class="chev"></span></button>
        ${isOpen ? `<div class="step-body">${blocks(s.blocks)}</div>
        ${soon || !tracked(p) ? '' : `<div class="step-actions">
          <button class="btn ${done ? 'ok' : 'primary'}" data-tick="${esc(key)}" data-step="${esc(s.id)}">${done ? '&#10003; Done' : 'Mark as done'}</button>
          <button class="btn link" data-stuck="${esc(s.title)}">I'm stuck</button></div>`}` : ''}
      </section>`;
    }).join('');

    const complete = d.total && d.done === d.total;
    return `<section class="hero-band small">
        <div class="hero-copy">${p.module ? `<div class="hero-num">${String(p.module).padStart(2, '0')}</div>` : ''}<div class="eyebrow">${esc(eyebrow)}</div>
        <h1>${esc(p.title)}</h1><p class="lede">${esc(p.short)}</p>
        ${d.total ? `<div class="segs" aria-label="${d.done} of ${d.total} steps done">${p.steps.filter((x) => !x.optional && !isSoon(x)).map((x) => `<i class="${progress[stepKey(p, x)] ? 'on' : ''}"></i>`).join('')}</div>` : ''}</div>
        ${d.total ? `<div class="hero-core">${core(d.pct, 170)}<div class="core-label"><b>${d.done}/${d.total}</b><span>${complete ? 'complete' : 'steps done'}</span></div></div>` : ''}
      </section>
      <div class="facts">${facts}</div>
      ${p.intro.length ? `<div class="intro">${blocks(p.intro)}</div>` : ''}
      ${complete ? `<div class="complete"><b>${esc(eyebrow)} complete.</b> ${next ? `Next: ${esc(next.title)}.` : 'Nice work.'} ${next ? `<a class="btn primary" href="#/${next.slug}">Go to Module ${next.module}</a>` : ''}</div>` : ''}
      <div class="steps">${steps}</div>
      <div class="nextbar">${prev ? `<a class="btn" href="#/${prev.slug}">Module ${prev.module}</a>` : '<span></span>'}${next ? `<a class="btn primary" href="#/${next.slug}">Next: Module ${next.module}</a>` : ''}</div>`;
  }

  function render(keepScroll) {
    document.querySelectorAll('.modal').forEach((m) => m.remove());
    const slug = (location.hash.replace(/^#\/?/, '') || 'welcome').split('/')[0];
    const p = SITE.pages.find((x) => x.slug === slug);
    const y = window.scrollY;
    document.title = (p ? (p.module ? `Module ${p.module}: ${p.title}` : p.title) : 'Start here') + ' | ' + SITE.site.name;
    $app.innerHTML = `<div class="shell">${nav(p ? p.slug : 'welcome')}<main class="main">${p ? page(p) : welcome()}</main></div>`;
    window.scrollTo(0, keepScroll ? y : 0);
  }
  const scrollToStep = (id) => setTimeout(() => {
    const el = document.getElementById(id);
    if (el) window.scrollTo({ top: el.getBoundingClientRect().top + window.scrollY - 24, behavior: 'smooth' });
  }, 30);

  // ---------- events ----------
  document.addEventListener('click', async (e) => {
    const t = e.target.closest('button');
    if (!t) return;
    const slug = (location.hash.replace(/^#\/?/, '') || 'welcome').split('/')[0];
    if (t.hasAttribute('data-copy')) {
      const text = t.closest('.prompt').querySelector('pre').textContent;
      try { await navigator.clipboard.writeText(text); t.textContent = 'Copied'; setTimeout(() => { t.textContent = 'Copy'; }, 1500); } catch { toast('Select the text and copy it'); }
    } else if (t.dataset.open) {
      openStep[slug] = openStep[slug] === t.dataset.open ? '' : t.dataset.open;
      render(true);
      if (openStep[slug]) scrollToStep(t.dataset.open);
    } else if (t.dataset.dl) {
      store.download(packById(t.dataset.dl));
    } else if (t.dataset.tick) {
      const key = t.dataset.tick;
      const p = SITE.pages.find((x) => x.slug === key.split(':')[1]), s = p.steps.find((x) => x.id === t.dataset.step);
      const on = !progress[key];
      await store.set(key, on ? new Date().toISOString() : null);
      for (const b of s.blocks.filter((b) => b.type === 'pack')) await store.set('pack:' + b.id, on ? packById(b.id).version : null);
      if (on) {
        const nx = nextStep(p);
        openStep[p.slug] = nx ? nx.id : '';
        render(true);
        if (nx) scrollToStep(nx.id);
        toast(nx ? 'Done. Next step is open.' : 'Module complete.');
      } else { render(true); }
    } else if (t.dataset.path !== undefined) {
      await store.set('path', t.dataset.path || null);
      if (t.dataset.path === 'new') location.hash = '#/new';
      else if (t.dataset.path === 'existing') location.hash = '#/jarvis';
      else render();
    } else if (t.dataset.stuck) {
      stuck(t.dataset.stuck);
    } else if (t.hasAttribute('data-signout')) {
      await sb.auth.signOut(); location.hash = ''; location.reload();
    }
  });

  function stuck(stepTitle) {
    const slug = (location.hash.replace(/^#\/?/, '') || 'welcome');
    const p = SITE.pages.find((x) => x.slug === slug);
    const m = document.createElement('div');
    m.className = 'modal';
    m.innerHTML = `<div class="modal-box"><h3>Stuck on "${esc(stepTitle)}"?</h3>
      <p>Tell us what you see. A screenshot helps: post it in your Discord channel after sending this.</p>
      <textarea placeholder="What happened, and what did Jarvis say?"></textarea>
      <div class="row"><button class="btn" data-x>Cancel</button><button class="btn primary" data-send>Send to the team</button></div></div>`;
    document.body.appendChild(m);
    m.querySelector('textarea').focus();
    m.addEventListener('click', async (e) => {
      if (e.target === m || e.target.hasAttribute('data-x')) return m.remove();
      if (e.target.hasAttribute('data-send')) {
        const message = m.querySelector('textarea').value.trim();
        if (!message) return toast('Add a short note first');
        const ok = await store.ticket({ module: p ? (p.module ? 'Module ' + p.module : p.title) : 'Start here', step: stepTitle, message, page: location.href });
        m.remove();
        toast(ok ? 'Sent. The team will reply in Discord.' : 'Could not send. Post in Discord instead.');
      }
    });
  }

  // ---------- login ----------
  function login(errMsg = '') {
    const name = cfg.siteName || (SITE && SITE.site.name) || 'Jarvis 2.0 Onboarding';
    $app.innerHTML = `<div class="login-wrap"><div class="login">
      <div class="login-segs"><i class="on"></i><i></i></div>
      ${LOGO}
      <h1>Sign in to Jarvis 2.0</h1>
      <p class="login-lede">Pop in the email you joined the programme with and we'll send you a six digit sign in code. No password to remember.</p>
      <form id="f1" novalidate><label for="em">Your email</label>
        <input id="em" type="email" name="email" placeholder="you@example.com" required autocomplete="email" autofocus>
        <button class="btn primary">Send my code</button></form>
      <form id="f2" hidden novalidate><label for="cd">Your 6 digit code</label>
        <input id="cd" name="code" class="code" inputmode="numeric" pattern="[0-9]*" maxlength="6" placeholder="000000" required autocomplete="one-time-code">
        <button class="btn primary">Sign in</button>
        <div class="login-alt"><button type="button" class="btn link" data-resend>Resend code</button><button type="button" class="btn link" data-other>Use a different email</button></div></form>
      <p class="err" role="alert">${esc(errMsg)}</p>
      <p class="login-foot">Only programme members can sign in. Trouble? Ask in your Discord channel.${DEMO ? ' <a href="#/welcome">Back to the preview</a>' : ''}</p>
    </div></div>`;
    let email = '', cooldown = 0, timer;
    const $ = (q) => $app.querySelector(q);
    const err = (m) => { $('.err').textContent = m; };
    const busy = (btn, on, label) => { btn.disabled = on; if (label) btn.textContent = label; };
    const tick = () => {
      const r = $('[data-resend]'); if (!r) return;
      if (cooldown > 0) { r.disabled = true; r.textContent = `Resend code in ${cooldown}s`; cooldown -= 1; timer = setTimeout(tick, 1000); }
      else { r.disabled = false; r.textContent = 'Resend code'; }
    };
    const send = async () => {
      if (DEMO) return { error: null };
      return sb.auth.signInWithOtp({ email, options: { shouldCreateUser: true, emailRedirectTo: location.origin } });
    };
    $('#f1').onsubmit = async (e) => {
      e.preventDefault();
      email = e.target.email.value.trim().toLowerCase();
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return err('Enter a valid email address.');
      const btn = e.target.querySelector('button'); busy(btn, true, 'Sending...');
      const { error } = await send();
      busy(btn, false, 'Send my code');
      if (error) return err(/database|not_a_member|signups/i.test(error.message)
        ? "We couldn't find that email on the programme list. Use the email you paid with, or ask in your Discord channel."
        : /rate|seconds|many/i.test(error.message) ? 'Too many attempts. Wait a minute, then try again.' : error.message);
      e.target.hidden = true; $('#f2').hidden = false; err('');
      $('.login-segs').innerHTML = '<i class="on"></i><i class="on"></i>';
      $('.login h1').textContent = 'Check your email';
      $('.login-lede').textContent = `We sent a 6 digit code to ${email}. It can take a minute. Check spam too. You can also click the link in the email.`;
      $('#cd').focus(); cooldown = 60; tick();
    };
    $('#cd').oninput = (e) => { e.target.value = e.target.value.replace(/\D/g, '').slice(0, 6); if (e.target.value.length === 6) $('#f2').requestSubmit(); };
    $('#f2').onsubmit = async (e) => {
      e.preventDefault();
      const token = e.target.code.value.trim();
      if (token.length !== 6) return err('Enter all 6 digits.');
      if (DEMO) return toast('Preview only: sign in works on the live hub.');
      const btn = e.target.querySelector('button.primary'); busy(btn, true, 'Checking...');
      const { error } = await sb.auth.verifyOtp({ email, token, type: 'email' });
      busy(btn, false, 'Sign in');
      if (error) return err(/expired/i.test(error.message) ? 'That code has expired. Press Resend code for a new one.' : "That code didn't work. Check the digits, or press Resend code.");
    };
    $('[data-resend]').onclick = async () => {
      if (cooldown > 0) return;
      const { error } = await send();
      if (error) return err('Could not resend yet. Wait a minute, then try again.');
      err(''); toast('New code sent'); cooldown = 60; tick();
    };
    $('[data-other]').onclick = () => { clearTimeout(timer); login(); };
  }

  // ---------- start ----------
  async function loadSite(token) {
    const r = await fetch('/api/site', { headers: { Authorization: 'Bearer ' + token }, cache: 'no-store' });
    if (r.status === 401 || r.status === 403) return null;
    if (!r.ok) throw new Error('site ' + r.status);
    return r.json();
  }

  async function start() {
    window.addEventListener('hashchange', () => {
      if (DEMO && location.hash === '#/login') return login();
      if ((DEMO || session) && SITE) render();
    });
    if (DEMO) {
      SITE = window.__SITE || await (await fetch('data/site.json', { cache: 'no-store' })).json();
      if (location.hash === '#/login') return login();
      await store.load(); render(); return;
    }
    sb = window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseAnonKey);
    let started = false, lastErr = '';
    const go = async (s) => {
      session = s;
      if (!s) { started = false; SITE = null; const m = lastErr; lastErr = ''; return login(m); }
      if (started) return;
      started = true;
      // The programme content only loads after sign in, for members.
      SITE = await loadSite(s.access_token);
      if (!SITE) { started = false; lastErr = "This email doesn't have access. Ask in your Discord channel."; await sb.auth.signOut(); return; }
      await store.load(); render();
    };
    sb.auth.onAuthStateChange((evt, s) => { if (evt === 'SIGNED_IN' || evt === 'SIGNED_OUT') go(s); });
    const { data } = await sb.auth.getSession();
    go(data.session);
  }
  start().catch(() => { $app.innerHTML = '<p class="loading">Could not load the hub. Refresh the page.</p>'; });
})();
