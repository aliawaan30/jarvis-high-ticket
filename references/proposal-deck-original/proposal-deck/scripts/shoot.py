#!/usr/bin/env python3
"""Python twin of shoot.mjs, for environments with Python but no Node: one JPG per slide, or a QA check.

    python3 shoot.py <deck-dir> [out-dir] [--ids cover,summary] [--width 1440] [--scale 1] [--file index.html] [--notes] [--check]

Needs Playwright:  pip install playwright  then either  playwright install chromium  (downloads a browser)
or set CHROME_CHANNEL=chrome to drive an installed Google Chrome instead.
The deck folder is served on a private local port for the run; nothing else needs to be running.
"""
import argparse, functools, http.server, json, os, re, socketserver, sys, threading, time

ap = argparse.ArgumentParser()
ap.add_argument('deck'); ap.add_argument('out', nargs='?')
ap.add_argument('--ids'); ap.add_argument('--width', type=int, default=1440); ap.add_argument('--scale', type=float, default=1)
ap.add_argument('--file', default='index.html'); ap.add_argument('--notes', action='store_true'); ap.add_argument('--check', action='store_true')
a = ap.parse_args()
DECK = os.path.abspath(a.deck); OUT = os.path.abspath(a.out or os.path.join(DECK, 'shots'))
if not os.path.exists(os.path.join(DECK, a.file)):
    sys.exit(f'No {a.file} in {DECK} — run build/build.py first.')
try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit('Install Playwright first:  pip install playwright && playwright install chromium')

class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *x): pass
    def do_GET(self):
        if self.path.startswith('/favicon'):
            self.send_response(204); self.end_headers(); return
        return super().do_GET()
httpd = socketserver.TCPServer(('127.0.0.1', 0), functools.partial(Quiet, directory=DECK))
threading.Thread(target=httpd.serve_forever, daemon=True).start()
url = f'http://127.0.0.1:{httpd.server_address[1]}/{a.file}?noanim' + ('&ovf' if a.check else '')

errors = []
with sync_playwright() as p:
    ch = os.environ.get('CHROME_CHANNEL')
    browser = p.chromium.launch(**({'channel': ch} if ch else {}), args=['--hide-scrollbars'])
    page = browser.new_page(viewport={'width': a.width, 'height': 900}, device_scale_factor=a.scale)
    page.on('pageerror', lambda e: errors.append('PAGE ERROR  ' + str(e)))
    page.on('console', lambda m: m.type == 'error' and errors.append('CONSOLE     ' + m.text))
    page.on('response', lambda r: r.status >= 400 and errors.append(f'HTTP {r.status}    ' + re.sub(r'^http://127\.0\.0\.1:\d+/', '', r.url)))
    page.goto(url, wait_until='networkidle', timeout=120000)
    page.add_style_tag(content=('body .note{display:block!important}' if a.notes else '.note{display:none!important}') +
                       ' .div-slide{min-height:720px!important;display:flex!important;align-items:center!important} .div-slide .in{width:100%}')
    page.evaluate("""() => { for (const el of document.querySelectorAll('body *')) {
        if (getComputedStyle(el).position === 'fixed' && !el.closest('section.slide')) el.style.display = 'none'; } }""")
    page.evaluate("""async () => { const imgs = [...document.images]; imgs.forEach(i => { i.loading = 'eager'; });
        await Promise.all(imgs.map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; }))); }""")
    time.sleep(1.5)

    if a.check:
        rep = page.evaluate("""() => { const out = { broken: [], nan: [], todo: [] };
          document.querySelectorAll('section.slide img').forEach(i => { if (i.complete && i.naturalWidth === 0 && i.getAttribute('src')) out.broken.push((i.closest('section')||{}).id + ' ' + i.getAttribute('src').slice(0, 60)); });
          document.querySelectorAll('section.slide').forEach(s => { const t = s.innerText;
            const bad = t.match(/.{0,30}\\b(NaN|undefined|Infinity|null)\\b.{0,30}/g); if (bad) out.nan.push(s.id + ': ' + bad.slice(0, 3).join(' | '));
            const todo = t.match(/⟦[^⟧]{0,60}⟧/g); if (todo) out.todo.push(s.id + ': ' + todo.length); });
          return out; }""")
        ovf = page.evaluate('() => document.body.dataset.ovf || ""')
        print(f'\n── QA {a.file} at {a.width}px ──')
        print('\n'.join(errors) if errors else 'console + network: clean')
        print('BROKEN IMAGES\n  ' + '\n  '.join(rep['broken']) if rep['broken'] else 'images: all load')
        print('NaN / undefined ON SCREEN\n  ' + '\n  '.join(rep['nan']) if rep['nan'] else 'numbers: no NaN / undefined on screen')
        if ovf:
            o = json.loads(ovf)
            print(f"OVERFLOW (page {o['docW']}px wide at {o['W']}px)\n  " + '\n  '.join(o['bad']) if o['bad'] else 'overflow: none')
        print('⟦…⟧ STILL SHOWING  ' + ' · '.join(rep['todo']) if rep['todo'] else 'markers: none left')
        browser.close(); httpd.shutdown()
        sys.exit(1 if (errors or rep['broken'] or rep['nan']) else 0)

    os.makedirs(OUT, exist_ok=True)
    want = a.ids.split(',') if a.ids else None
    slides = page.evaluate("""() => [...document.querySelectorAll('section.slide')].filter(s => s.offsetHeight > 0)
        .map(s => { const r = s.getBoundingClientRect(); return { id: s.id, y: r.top + scrollY, h: r.height }; })""")
    for n, s in enumerate(slides, 1):
        if want and s['id'] not in want:
            continue
        page.evaluate('y => window.scrollTo(0, y)', s['y']); time.sleep(0.45)
        f = os.path.join(OUT, f"{n:02d}_{s['id'] or 'slide'}.jpg")
        page.screenshot(path=f, type='jpeg', quality=84, full_page=True,
                        clip={'x': 0, 'y': s['y'], 'width': a.width, 'height': int(s['h'] + .999)})
        print(os.path.relpath(f), f"{round(s['h'])}px")
    if errors:
        print('\n' + '\n'.join(errors))
    browser.close(); httpd.shutdown()
