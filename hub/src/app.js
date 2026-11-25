(() => {
  'use strict';
  const cfg = window.HUB_CONFIG || {};
  const DEMO = !cfg.supabaseUrl || new URLSearchParams(location.search).has('demo');
  const $app = document.getElementById('app');
  let SITE, sb, session, member, progress = {};

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
      if (DEMO) { location.href = 'demo-packs/' + pack.file; return; }
      const r = await fetch('/api/pack?pack=' + encodeURIComponent(pack.id), { headers: { Authorization: 'Bearer ' + session.access_token } });
      const j = await r.json().catch(() => ({}));
      if (!r.ok || !j.url) return toast(j.error || 'Download failed. Try again.');
      location.href = j.url;
    },
  };

  const updateLink = () => member?.update_code ? `${location.origin}/api/pack?code=${member.update_code}` : '';
  const packById = (id) => SITE.packs.find((p) => p.id === id);
  const stepKey = (page, step) => `step:${page.slug}:${step.id}`;
  const pageDone = (page) => {
    const req = page.steps.filter((s) => !s.optional && !/coming soon/i.test(s.time));
    const done = req.filter((s) => progress[stepKey(page, s)]).length;
    return { done, total: req.length };
  };
  const needsUpdate = (pack) => progress['pack:' + pack.id] && progress['pack:' + pack.id] !== pack.version;
  const pageNeedsUpdate = (page) => page.packs.some((id) => needsUpdate(packById(id)));

  // ---------- rendering ----------
  function blocks(list, page) {
    return list.map((b) => {
      switch (b.type) {
        case 'p': return `<p>${b.html}</p>`;
        case 'list': return `<ol>${b.items.map((i) => `<li>${i}</li>`).join('')}</ol>`;
        case 'see': return `<div class="note see"><b>You'll see:</b>${b.html}</div>`;
        case 'fix': return `<div class="note fix"><b>If it looks different:</b>${b.html}</div>`;
        case 'prompt': {
          const text = b.text.replace(/\{\{update_link\}\}/g, updateLink() || '[your update link]');
          return `<div class="prompt"><div class="prompt-head"><span>${esc(b.label)}</span><button data-copy>Copy</button></div><pre>${esc(text)}</pre></div>`;
        }
        case 'pack': {
          const p = packById(b.id);
          const installed = progress['pack:' + p.id];
          const badge = needsUpdate(p) ? `<span class="badge update">Update available</span>`
            : installed ? `<span class="badge installed">Installed</span>` : '';
          const skills = p.skills.length ? `${p.skills.length} skills, ` : '';
          return `<div class="pack"><div class="pack-info"><b>${esc(p.title)}${badge}</b><small>${skills}version ${esc(p.version)}, ${kb(p.size)}. Don't unzip it.</small></div><button class="btn primary" data-dl="${esc(p.id)}">Download</button></div>`;
        }
        case 'link': {
          const target = SITE.pages.find((x) => x.slug === b.id);
          return `<div class="linkcard"><a class="btn" href="#/${esc(b.id)}">Open the ${esc(target ? target.title : b.id)} page</a></div>`;
        }
        case 'updatelink': return `<div class="updatelink">${esc(updateLink() || 'Sign in to see your link')}</div>`;
        default: return '';
      }
    }).join('');
  }

  function nav(current) {
    const mods = SITE.pages.filter((p) => p.module > 0).sort((a, b) => a.module - b.module);
    const extra = SITE.pages.filter((p) => p.module === 0);
    const all = mods.map(pageDone).reduce((a, c) => ({ done: a.done + c.done, total: a.total + c.total }), { done: 0, total: 0 });
    const item = (p, label) => {
      const d = pageDone(p);
      const cls = [current === p.slug ? 'on' : '', d.total && d.done === d.total ? 'done' : ''].join(' ');
      return `<a href="#/${p.slug}" class="${cls}"><span class="num">${label}</span>${esc(p.title)}${pageNeedsUpdate(p) ? '<span class="dot" title="Update available"></span>' : ''}<span class="count">${d.total ? `${d.done}/${d.total}` : ''}</span></a>`;
    };
    return `<aside class="side">
      <div class="brand">${esc(SITE.site.name)}</div>
      <div class="brand-sub">${esc(SITE.site.programme)}</div>
      ${DEMO ? '<div class="demo-banner">Preview mode. Ticks save in this browser only.</div>' : ''}
      <div class="overall"><div class="bar"><i style="width:${all.total ? Math.round(100 * all.done / all.total) : 0}%"></i></div><small>${all.done} of ${all.total} steps done</small></div>
      <nav class="nav">
        <a href="#/welcome" class="${current === 'welcome' ? 'on' : ''}"><span class="num">0</span>Start here</a>
        <div class="nav-label">Modules</div>
        ${mods.map((p) => item(p, p.module)).join('')}
        <div class="nav-label">Any time</div>
        ${extra.map((p) => item(p, p.slug === 'help' ? '?' : 'W')).join('')}
      </nav>
      <div class="side-foot">${esc(member?.email || '')}<br>${DEMO ? '' : '<button data-signout>Sign out</button>'}</div>
    </aside>`;
  }

  function welcome() {
    const s = SITE.site;
    const mods = SITE.pages.filter((p) => p.module > 0).sort((a, b) => a.module - b.module);
    const first = mods.find((p) => { const d = pageDone(p); return d.done < d.total; }) || mods[0];
    const name = member?.name ? `, ${esc(member.name)}` : '';
    return `<div class="eyebrow">Start here</div>
      <h1>Welcome${name}</h1>
      <p class="lede">${esc(s.programme)}. Everything you need, in order.</p>
      <div class="cta">
        <a class="btn primary" href="#/${first.slug}">${progress[stepKey(mods[0], mods[0].steps[0])] ? 'Continue' : 'Start'} with Module ${first.module}</a>
        ${s.booking_url && !s.booking_url.includes('REPLACE') ? `<a class="btn" href="${esc(s.booking_url)}" target="_blank" rel="noopener">Book your onboarding call</a>` : ''}
        ${s.discord_url && !s.discord_url.includes('REPLACE') ? `<a class="btn" href="${esc(s.discord_url)}" target="_blank" rel="noopener">Open Discord</a>` : ''}
      </div>
      ${s.sections.map((sec) => `<div class="section"><h2>${esc(sec.title)}</h2>${blocks(sec.blocks)}</div>`).join('')}
      <div class="section"><h2>The modules</h2><div class="grid">
        ${mods.map((p) => { const d = pageDone(p); return `<a class="mcard" href="#/${p.slug}"><small>Module ${p.module}</small><b>${esc(p.title)}</b><span>${esc(p.short)}</span><div class="bar"><i style="width:${d.total ? Math.round(100 * d.done / d.total) : 0}%"></i></div></a>`; }).join('')}
      </div></div>`;
  }

  function page(p) {
    const ordered = SITE.pages.filter((x) => x.module > 0).sort((a, b) => a.module - b.module);
    const idx = ordered.indexOf(p);
    const prev = idx > 0 ? ordered[idx - 1] : null, next = idx >= 0 && idx < ordered.length - 1 ? ordered[idx + 1] : null;
    const facts = [['Time', p.time], ['Ready when', p.gate], ['You get', p.outcome], ['Missions', p.missions]]
      .filter(([, v]) => v && v !== 'none' && v !== 'None.').map(([k, v]) => `<div class="fact"><b>${k}</b><span>${esc(v)}</span></div>`).join('');
    let n = 0;
    const steps = p.steps.map((s) => {
      const key = stepKey(p, s), done = !!progress[key], soon = /coming soon/i.test(s.time);
      n += 1;
      const tags = [s.time && !soon ? `<span class="tag">${esc(s.time)}</span>` : '', s.optional ? '<span class="tag">Optional</span>' : '', soon ? '<span class="tag">Coming soon</span>' : ''].join('');
      return `<section class="step ${done ? 'is-done' : ''}" id="${esc(s.id)}">
        <div class="step-head"><div class="step-n">${done ? '&#10003;' : n}</div><h2>${esc(s.title)}${tags}</h2></div>
        <div class="step-body">${blocks(s.blocks, p)}</div>
        ${soon ? '' : `<div class="step-actions">
          <button class="btn ${done ? 'ok' : ''}" data-tick="${esc(key)}" data-step="${esc(s.id)}">${done ? 'Done' : 'Mark as done'}</button>
          <button class="btn link" data-stuck="${esc(s.title)}">I'm stuck</button></div>`}
      </section>`;
    }).join('');
    return `<div class="eyebrow">${p.module ? 'Module ' + p.module : 'Any time'}</div>
      <h1>${esc(p.title)}</h1><p class="lede">${esc(p.short)}</p>
      <div class="facts">${facts}</div>
      <div class="intro">${blocks(p.intro, p)}</div>
      ${steps}
      <div class="nextbar">${prev ? `<a class="btn" href="#/${prev.slug}">Module ${prev.module}</a>` : '<span></span>'}${next ? `<a class="btn primary" href="#/${next.slug}">Next: Module ${next.module}</a>` : ''}</div>`;
  }

  function render() {
    const slug = (location.hash.replace(/^#\/?/, '') || 'welcome').split('/')[0];
    const p = SITE.pages.find((x) => x.slug === slug);
    document.querySelectorAll('.modal').forEach((m) => m.remove());
    $app.innerHTML = `<div class="shell">${nav(p ? p.slug : 'welcome')}<main class="main">${p ? page(p) : welcome()}</main></div>`;
    window.scrollTo(0, 0);
  }

  // ---------- events ----------
  document.addEventListener('click', async (e) => {
    const t = e.target.closest('button');
    if (!t) return;
    if (t.hasAttribute('data-copy')) {
      const text = t.closest('.prompt').querySelector('pre').textContent;
      try { await navigator.clipboard.writeText(text); toast('Copied'); } catch { toast('Select the text and copy it'); }
    } else if (t.dataset.dl) {
      store.download(packById(t.dataset.dl));
    } else if (t.dataset.tick) {
      const key = t.dataset.tick, slug = key.split(':')[1];
      const p = SITE.pages.find((x) => x.slug === slug), s = p.steps.find((x) => x.id === t.dataset.step);
      const on = !progress[key];
      await store.set(key, on ? new Date().toISOString() : null);
      for (const b of s.blocks.filter((b) => b.type === 'pack')) {
        await store.set('pack:' + b.id, on ? packById(b.id).version : null);
      }
      const y = window.scrollY; render(); window.scrollTo(0, y);
      if (on) toast('Nice. Saved.');
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
    $app.innerHTML = `<div class="login"><h1>${esc(SITE.site.name)}</h1>
      <p>Sign in with the email you joined the programme with. We'll email you a 6 digit code.</p>
      <form id="f1"><input type="email" name="email" placeholder="you@example.com" required autocomplete="email"><button class="btn primary">Email me a code</button></form>
      <form id="f2" hidden><input name="code" inputmode="numeric" placeholder="6 digit code" required autocomplete="one-time-code"><button class="btn primary">Sign in</button></form>
      <p class="err">${esc(errMsg)}</p></div>`;
    let email = '';
    const err = (m) => { $app.querySelector('.err').textContent = m; };
    $app.querySelector('#f1').onsubmit = async (e) => {
      e.preventDefault();
      email = e.target.email.value.trim().toLowerCase();
      e.target.querySelector('button').disabled = true;
      const { error } = await sb.auth.signInWithOtp({ email, options: { shouldCreateUser: true, emailRedirectTo: location.origin } });
      e.target.querySelector('button').disabled = false;
      if (error) return err(/database|not_a_member|signups/i.test(error.message)
        ? "This email isn't on the programme list. Use the email you paid with, or ask in your Discord channel."
        : error.message);
      e.target.hidden = true; $app.querySelector('#f2').hidden = false; err('');
      $app.querySelector('p').textContent = `Code sent to ${email}. Check your inbox and spam folder. You can also click the link in the email.`;
    };
    $app.querySelector('#f2').onsubmit = async (e) => {
      e.preventDefault();
      const { error } = await sb.auth.verifyOtp({ email, token: e.target.code.value.trim(), type: 'email' });
      if (error) return err('That code did not work. Check it, or send a new one by reloading the page.');
    };
  }

  // ---------- start ----------
  async function start() {
    SITE = await (await fetch('data/site.json', { cache: 'no-store' })).json();
    if (DEMO) { await store.load(); render(); window.addEventListener('hashchange', render); return; }
    sb = window.supabase.createClient(cfg.supabaseUrl, cfg.supabaseAnonKey);
    const go = async (s) => {
      session = s;
      if (!s) return login();
      await store.load(); render();
    };
    sb.auth.onAuthStateChange((evt, s) => { if (evt === 'SIGNED_IN' || evt === 'SIGNED_OUT') go(s); });
    const { data } = await sb.auth.getSession();
    go(data.session);
    window.addEventListener('hashchange', () => session && render());
  }
  start().catch(() => { $app.innerHTML = '<p class="loading">Could not load the hub. Refresh the page.</p>'; });
})();
