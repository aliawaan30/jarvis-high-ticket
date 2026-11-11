#!/usr/bin/env node
// Screenshots and checks a deck exactly as it presents — one JPG per slide, plus a QA report.
//
//   node shoot.mjs <deck-dir> [out-dir] [--ids cover,summary] [--width 1440] [--scale 1] [--file index.html] [--notes] [--check]
//
//   <deck-dir>  the folder that holds index.html and assets/ (it is served on a private local port — no server needed)
//   out-dir     where the JPGs go (default: <deck-dir>/shots). Name pattern: 01_cover.jpg, 02_summary.jpg …
//   --ids       only these slide ids (default: every slide)
//   --width     viewport width: 1440 = the desktop deck, 390 = a phone
//   --scale     device pixel ratio (1.5 for a crisp client PDF)
//   --notes     show the presenter notes (press N in the deck) instead of hiding them
//   --check     QA only, no screenshots: console errors, broken images, NaN/undefined on screen,
//               horizontal overflow, ⟦…⟧ markers and placeholder images still on show
//
// Needs Node 18+ and puppeteer-core (`npm i puppeteer-core` beside this script) plus Chrome/Chromium on the machine,
// or the full `puppeteer` package (which downloads its own Chromium). CHROME_PATH overrides the browser it finds.
import { createRequire } from 'module';
import http from 'http';
import fs from 'fs';
import path from 'path';
import os from 'os';

const require = createRequire(import.meta.url);
let puppeteer;
try { puppeteer = require('puppeteer-core'); } catch { try { puppeteer = require('puppeteer'); } catch {
  console.error('Install a browser driver first:  npm i puppeteer-core   (or: npm i puppeteer)'); process.exit(1); } }

const argv = process.argv.slice(2), opt = {}, pos = [];
const VALUED = ['ids', 'width', 'scale', 'file'];
for (let i = 0; i < argv.length; i++) {
  const a = argv[i];
  if (!a.startsWith('--')) { pos.push(a); continue; }
  const k = a.slice(2);
  opt[k] = VALUED.includes(k) ? argv[++i] : true;
}
const flag = (n, d) => (n in opt ? opt[n] : d);
const DECK = path.resolve(pos[0] || '.');
const OUT = path.resolve(pos[1] || path.join(DECK, 'shots'));
const IDS = flag('ids', null), WIDTH = +flag('width', 1440), SCALE = +flag('scale', 1), FILE = flag('file', 'index.html');
const NOTES = !!flag('notes', false), CHECK = !!flag('check', false);
if (!fs.existsSync(path.join(DECK, FILE))) { console.error(`No ${FILE} in ${DECK} — run build/build.py first.`); process.exit(1); }

function findChrome() {
  if (process.env.CHROME_PATH) return process.env.CHROME_PATH;
  const c = {
    darwin: ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/Applications/Chromium.app/Contents/MacOS/Chromium',
      '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge'],
    linux: ['/usr/bin/google-chrome', '/usr/bin/google-chrome-stable', '/usr/bin/chromium', '/usr/bin/chromium-browser', '/snap/bin/chromium'],
    win32: [path.join(process.env['PROGRAMFILES'] || '', 'Google/Chrome/Application/chrome.exe'),
      path.join(process.env['PROGRAMFILES(X86)'] || '', 'Google/Chrome/Application/chrome.exe'),
      path.join(process.env['LOCALAPPDATA'] || '', 'Google/Chrome/Application/chrome.exe')],
  }[os.platform()] || [];
  return c.find(p => p && fs.existsSync(p));
}

const MIME = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.js': 'text/javascript', '.json': 'application/json',
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml', '.webp': 'image/webp',
  '.ttf': 'font/ttf', '.woff2': 'font/woff2', '.mp3': 'audio/mpeg', '.mp4': 'video/mp4' };
const server = http.createServer((req, res) => {
  if (req.url.startsWith('/favicon')) { res.writeHead(204); return res.end(); }
  const p = path.join(DECK, decodeURIComponent(req.url.split('?')[0]));
  if (!p.startsWith(DECK) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': MIME[path.extname(p).toLowerCase()] || 'application/octet-stream' });
  fs.createReadStream(p).pipe(res);
});
await new Promise(r => server.listen(0, '127.0.0.1', r));
const URL = `http://127.0.0.1:${server.address().port}/${FILE}?noanim${CHECK ? '&ovf' : ''}`;

const exe = findChrome();
const browser = await puppeteer.launch({ ...(exe ? { executablePath: exe } : {}), headless: 'new', args: ['--hide-scrollbars', '--disable-gpu', '--no-sandbox'] });
const page = await browser.newPage();
const errors = [];
page.on('pageerror', e => errors.push('PAGE ERROR  ' + e.message));
page.on('console', m => { if (m.type() === 'error') errors.push('CONSOLE     ' + m.text()); });
page.on('requestfailed', r => errors.push('LOAD FAILED ' + r.url().replace(/^http:\/\/127\.0\.0\.1:\d+\//, '')));
page.on('response', r => { if (r.status() >= 400) errors.push(`HTTP ${r.status()}    ` + r.url().replace(/^http:\/\/127\.0\.0\.1:\d+\//, '')); });
await page.setViewport({ width: WIDTH, height: 900, deviceScaleFactor: SCALE });
await page.goto(URL, { waitUntil: 'networkidle0', timeout: 120000 });

// present it exactly as the client sees it: no presenter notes, no fixed chrome (dots, progress bar, hints)
await page.addStyleTag({ content: (NOTES ? 'body .note{display:block!important}' : '.note{display:none!important}') +
  ' .div-slide{min-height:720px!important;display:flex!important;align-items:center!important} .div-slide .in{width:100%}' });
await page.evaluate(() => { for (const el of document.querySelectorAll('body *')) {
  if (getComputedStyle(el).position === 'fixed' && !el.closest('section.slide')) el.style.display = 'none'; } });
await page.evaluate(async () => { const imgs = [...document.images]; imgs.forEach(i => { i.loading = 'eager'; });
  await Promise.all(imgs.map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; }))); });
await new Promise(r => setTimeout(r, 1500));

if (CHECK) {
  const rep = await page.evaluate(() => {
    const out = { broken: [], nan: [], todo: [], ph: [] };
    document.querySelectorAll('section.slide img').forEach(i => { if (i.complete && i.naturalWidth === 0 && i.getAttribute('src')) out.broken.push((i.closest('section') || {}).id + ' ' + i.getAttribute('src').slice(0, 60)); });
    document.querySelectorAll('section.slide').forEach(s => {
      const t = s.innerText;
      const bad = t.match(/.{0,30}\b(NaN|undefined|Infinity|null)\b.{0,30}/g); if (bad) out.nan.push(s.id + ': ' + bad.slice(0, 3).join(' | '));
      const todo = t.match(/⟦[^⟧]{0,60}⟧/g); if (todo) out.todo.push(`${s.id}: ${todo.length}`);
    });
    return out;
  });
  const ovf = await page.evaluate(() => document.body.dataset.ovf || '');
  console.log('\n── QA ' + FILE + ' at ' + WIDTH + 'px ──');
  console.log(errors.length ? errors.join('\n') : 'console + network: clean');
  console.log(rep.broken.length ? 'BROKEN IMAGES\n  ' + rep.broken.join('\n  ') : 'images: all load');
  console.log(rep.nan.length ? 'NaN / undefined ON SCREEN\n  ' + rep.nan.join('\n  ') : 'numbers: no NaN / undefined on screen');
  if (ovf) { const o = JSON.parse(ovf); console.log(o.bad.length ? `OVERFLOW (page ${o.docW}px wide at ${o.W}px)\n  ` + o.bad.join('\n  ') : 'overflow: none'); }
  console.log(rep.todo.length ? '⟦…⟧ STILL SHOWING  ' + rep.todo.join(' · ') : 'markers: none left');
  await browser.close(); server.close();
  process.exit(errors.length || rep.broken.length || rep.nan.length ? 1 : 0);
}

fs.mkdirSync(OUT, { recursive: true });
const want = IDS ? String(IDS).split(',') : null;
const slides = await page.evaluate(() => [...document.querySelectorAll('section.slide')].filter(s => s.offsetHeight > 0)
  .map(s => { const r = s.getBoundingClientRect(); return { id: s.id, y: r.top + scrollY, h: r.height }; }));
let n = 0;
for (const s of slides) {
  n++; if (want && !want.includes(s.id)) continue;
  await page.evaluate(y => window.scrollTo(0, y), s.y);                 // let visibility-driven content paint
  await new Promise(r => setTimeout(r, 450));
  const f = path.join(OUT, `${String(n).padStart(2, '0')}_${s.id || 'slide'}.jpg`);
  await page.screenshot({ path: f, type: 'jpeg', quality: 84, clip: { x: 0, y: s.y, width: WIDTH, height: Math.ceil(s.h) }, captureBeyondViewport: true });
  console.log(path.relative(process.cwd(), f), Math.round(s.h) + 'px');
}
if (errors.length) console.log('\n' + errors.join('\n'));
await browser.close(); server.close();
