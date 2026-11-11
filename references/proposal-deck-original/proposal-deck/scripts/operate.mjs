#!/usr/bin/env node
// Drives the deck's interactions headlessly and prints what changed — the "operate" step of QA.
//
//   node operate.mjs <deck-dir> [out-dir]          (screenshots of each state go to out-dir, default <deck-dir>/operate)
//
// It moves every dial and preset and reads the outputs back (and the package's live ad-spend line), presses every reach
// tier, opens the summary cards, the report attachment, a plan page and the call script, flips an ad, steps the wall
// through its products and locations, and plays the film for a few seconds. Any NaN, console error or failed load is
// listed at the end. It is a starting point: when you add or change an interaction, add a step here.
// Needs puppeteer-core (or puppeteer) and Chrome, like shoot.mjs.
import { createRequire } from 'module';
import http from 'http'; import fs from 'fs'; import path from 'path'; import os from 'os';
const require = createRequire(import.meta.url);
let puppeteer; try { puppeteer = require('puppeteer-core'); } catch { puppeteer = require('puppeteer'); }

const DECK = path.resolve(process.argv[2] || '.'), OUT = path.resolve(process.argv[3] || path.join(DECK, 'operate'));
fs.mkdirSync(OUT, { recursive: true });
const MIME = { '.html': 'text/html; charset=utf-8', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.jpg': 'image/jpeg',
  '.png': 'image/png', '.svg': 'image/svg+xml', '.ttf': 'font/ttf', '.woff2': 'font/woff2', '.mp3': 'audio/mpeg' };
const server = http.createServer((q, r) => { if (q.url.startsWith('/favicon')) { r.writeHead(204); return r.end(); }
  const p = path.join(DECK, decodeURIComponent(q.url.split('?')[0])); if (!p.startsWith(DECK) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { r.writeHead(404); return r.end(); }
  r.writeHead(200, { 'Content-Type': MIME[path.extname(p).toLowerCase()] || 'application/octet-stream' }); fs.createReadStream(p).pipe(r); });
await new Promise(r => server.listen(0, '127.0.0.1', r));
const exe = process.env.CHROME_PATH || { darwin: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', linux: '/usr/bin/google-chrome',
  win32: path.join(process.env.PROGRAMFILES || '', 'Google/Chrome/Application/chrome.exe') }[os.platform()];
const browser = await puppeteer.launch({ ...(exe && fs.existsSync(exe) ? { executablePath: exe } : {}), headless: 'new', args: ['--no-sandbox', '--autoplay-policy=no-user-gesture-required'] });
const page = await browser.newPage(); await page.setViewport({ width: 1440, height: 900 });
const problems = [];
page.on('pageerror', e => problems.push('PAGE ERROR ' + e.message));
page.on('console', m => { if (m.type() === 'error') problems.push('CONSOLE ' + m.text()); });
await page.goto(`http://127.0.0.1:${server.address().port}/index.html`, { waitUntil: 'networkidle0', timeout: 120000 });
const wait = ms => new Promise(r => setTimeout(r, ms));
const has = sel => page.$(sel).then(Boolean);
const text = sel => page.$eval(sel, el => el.textContent.trim()).catch(() => '(missing)');
const go = async id => { await page.evaluate(i => document.getElementById(i)?.scrollIntoView(), id); await wait(700); };
const shot = async (name, id) => { const el = await page.$('#' + id); if (el) await el.screenshot({ path: path.join(OUT, name + '.jpg'), type: 'jpeg', quality: 78 }); };
const slide = async (sel, v) => page.$eval(sel, (el, v) => { el.value = v; el.dispatchEvent(new Event('input', { bubbles: true })); el.dispatchEvent(new Event('change', { bubbles: true })); }, v);
const log = (...a) => console.log(...a);

if (await has('#sB')) {
  await go('numbers');
  const read = async () => `per day ${await text('#oDay')} · a month ${await text('#oL')} · the quarter ${await text('#oQ')} · spend ${await text('#oT')}`;
  log('numbers  opening      ', await read());
  await slide('#sB', 8000); log('numbers  budget 8000  ', await read());
  await slide('#sC', 40);   log('numbers  cost 40      ', await read());
  await slide('#sE', 3);    log('numbers  3 a day      ', await read(), '| budget →', await text('#vB'));
  for (const c of await page.$$('#numbers .chip')) { await c.click(); log('numbers  preset       ', await text('#numbers .chip.on'), '→', await read()); }
  await shot('numbers', 'numbers');
  const live = await page.$$eval('#included [data-live]', els => els.map(e => e.dataset.live + '=' + e.textContent.trim()));
  log('package  live values  ', live.join('  '));
}
if (await has('#sS')) {
  await go('forecast');
  await slide('#sS', 60); log('forecast 1 in 60      ', 'sales', await text('#fSale'), '· after ad spend', await text('#fNet'));
  if (await has('#sP')) { const max = await page.$eval('#sP', e => e.max); await slide('#sP', max); log('forecast top price    ', await text('#vP'), '→', await text('#fNet')); }
  await shot('forecast', 'forecast');
}
for (const b of await page.$$('#catchment .rc')) { await b.click(); await wait(250); log('reach    tier', await page.evaluate(e => e.dataset.r, b), '→', await text('#rTot')); }
for (const s of await page.$$('#summary .stage')) { await s.click(); await wait(200); }
log('summary  cards open   ', await page.$$eval('#summary .stage.open', e => e.length));
if (await has('#attachBtn')) { await go('reporting'); await page.click('#attachBtn'); await wait(900); log('report   open         ', await page.$eval('#reportDoc', e => e.classList.contains('open'))); await shot('report', 'reporting'); }
const flip = await page.$('#ads1 .whyb'); if (flip) { await go("ads1"); await page.evaluate(e => e.click(), flip); await wait(900); log('ads      flipped      ', await page.$$eval('#ads1 .adcell.flipped', e => e.length)); await shot('ads1-flip', 'ads1'); }
const card = await page.$('#paper .mkp-card'); if (card) { await go('paper'); await card.click(); await wait(900); log('plan     dialog open  ', await page.$eval('#paper .mkp-dlg', d => d.open || d.classList.contains('on') || getComputedStyle(d).display !== 'none')); await page.keyboard.press('Escape'); }
const tabs = await page.$$('#structure .bx-tab');
if (tabs.length) { await go('structure'); for (const t of tabs.slice(0, 4)) { await t.click().catch(() => {}); await wait(300); } log('wall     product tabs ', tabs.length, '· heading:', (await text('#structure .bx-loc, #structure h3')).slice(0, 60)); await shot('wall', 'structure'); }
const play = await page.$('#how .xj.one .xplay');
if (play) { await go('how'); await play.click().catch(() => {}); await wait(6000); await shot('film-6s', 'how'); log('film     playing      ', 'screenshot at 6s'); }
const cs = await page.$('[data-pop="callscript"]'); if (cs) { await page.evaluate(e => e.click(), cs); await wait(600); log('script   pop-up       ', await has('.csp')); await page.keyboard.press('Escape'); }

const nan = await page.$$eval('section.slide', ss => ss.map(s => [s.id, (s.innerText.match(/\b(NaN|undefined|Infinity)\b/g) || []).length]).filter(x => x[1]));
if (nan.length) problems.push('NaN/undefined on screen: ' + JSON.stringify(nan));
log('\n' + (problems.length ? 'PROBLEMS\n  ' + problems.join('\n  ') : 'no console errors, no NaN') + `\nscreenshots → ${OUT}`);
await browser.close(); server.close(); process.exit(problems.length ? 1 : 0);
