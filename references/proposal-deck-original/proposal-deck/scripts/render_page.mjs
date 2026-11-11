#!/usr/bin/env node
// Renders a one-page HTML document (the call script, a one-pager, an invoice) to a crisp A4 JPG.
//
//   node render_page.mjs <page.html> <out.jpg> [--width-px 1653]
//
// The page is served from the project root (the folder above build/) so its ../assets/ links resolve.
// Default output: 1653 px wide = A4 at 200 dpi — sharp inside the deck's pop-up and in a PDF.
// Needs puppeteer-core (or puppeteer) and Chrome, exactly like shoot.mjs.
import { createRequire } from 'module';
import http from 'http';
import fs from 'fs';
import path from 'path';
import os from 'os';

const require = createRequire(import.meta.url);
let puppeteer;
try { puppeteer = require('puppeteer-core'); } catch { try { puppeteer = require('puppeteer'); } catch {
  console.error('Install a browser driver first:  npm i puppeteer-core   (or: npm i puppeteer)'); process.exit(1); } }

const [src, out] = process.argv.slice(2).filter(a => !a.startsWith('--'));
const wi = process.argv.indexOf('--width-px'); const W = wi > 0 ? +process.argv[wi + 1] : 1653;
if (!src || !out) { console.error('usage: node render_page.mjs <page.html> <out.jpg>'); process.exit(1); }
const file = path.resolve(src), root = path.dirname(path.dirname(file));   // build/x.html → the project root

const exe = process.env.CHROME_PATH || {
  darwin: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  linux: ['/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser'].find(p => fs.existsSync(p)),
  win32: path.join(process.env['PROGRAMFILES'] || '', 'Google/Chrome/Application/chrome.exe'),
}[os.platform()];
const MIME = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.jpg': 'image/jpeg', '.png': 'image/png',
  '.svg': 'image/svg+xml', '.ttf': 'font/ttf', '.woff2': 'font/woff2' };
const server = http.createServer((req, res) => {
  const p = path.join(root, decodeURIComponent(req.url.split('?')[0]));
  if (!p.startsWith(root) || !fs.existsSync(p) || fs.statSync(p).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': MIME[path.extname(p).toLowerCase()] || 'application/octet-stream' }); fs.createReadStream(p).pipe(res);
});
await new Promise(r => server.listen(0, '127.0.0.1', r));
const browser = await puppeteer.launch({ ...(exe && fs.existsSync(exe) ? { executablePath: exe } : {}), headless: 'new', args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.setViewport({ width: 794, height: 1123, deviceScaleFactor: W / 794 });   // A4 at 96 dpi, scaled up
await page.goto(`http://127.0.0.1:${server.address().port}/${path.relative(root, file).split(path.sep).join('/')}`, { waitUntil: 'networkidle0' });
await page.evaluate(() => document.fonts.ready);
await page.screenshot({ path: path.resolve(out), type: 'jpeg', quality: 85, fullPage: true });
console.log(out, 'rendered');
await browser.close(); server.close();
