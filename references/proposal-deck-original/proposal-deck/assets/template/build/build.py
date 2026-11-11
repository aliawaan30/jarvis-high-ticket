# Assembles the deck from its parts:
#   tpl/00_head.html  +  tpl/02_body_pre.html  +  src/extra.css  +  src/sNN_*.html (in filename order)
#   +  src/print.css  +  src/script.js  +  src/js/*.js
# and writes two files:
#   index.html       — references assets/ (preview this one while you work)
#   standalone.html  — every asset inlined as a data URI: ONE file you can email, upload or publish as-is
#
# Settings live in deck.config.json (title, palette re-skin, residue words from the template or the last client).
# The build also reports anything that is not finished yet:
#   · ⟦…⟧ markers   — a fact, figure, quote or proof point that still has to be supplied or verified
#   · placeholder images still referenced (the generated ph-*/proof-*/brand-* files carry a PLACEHOLDER-IMAGE stamp)
#   · residue words  — the previous client's names and concepts that must not survive a port
# Usage:  python3 build/build.py            (OUT=index-mine.html python3 build/build.py writes a private preview only)
import os, re, base64, glob, sys, json

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TPL, SRC = os.path.join(ROOT, 'tpl'), os.path.join(ROOT, 'src')
read = lambda p: open(p, encoding='utf8').read()
CFG = json.load(open(os.path.join(ROOT, 'deck.config.json'), encoding='utf8'))

head = read(os.path.join(TPL, '00_head.html'))
head = re.sub(r'<title>.*?</title>', '<title>' + CFG['title'] + '</title>', head, flags=re.S)
pre = read(os.path.join(TPL, '02_body_pre.html'))
extra = read(os.path.join(SRC, 'extra.css'))
slides = sorted(glob.glob(os.path.join(SRC, 's[0-9][0-9]*_*.html')))   # s13_how, s13a_leadform, s14_… (a letter slots a page in)
body = '\n'.join(read(p) for p in slides)
script = read(os.path.join(SRC, 'script.js'))
script += '\n' + '\n'.join(read(p) for p in sorted(glob.glob(os.path.join(SRC, 'js', '*.js'))))
printcss = read(os.path.join(SRC, 'print.css'))
html = (head + '\n</head>\n' + pre + '\n<style>' + extra + '</style>\n' + body + '\n<style>' + printcss + '</style>' +
        '\n<script>\n' + script + '\n</script>\n</body>\n</html>\n')

# re-skin: swap the template's canonical colours for the client's (see deck.config.json → palette)
for a, b in CFG.get('palette', {}).items():
    if a != b:
        html = html.replace(a, b).replace(a.lower(), b)

# ── the "not finished" report ──
SCRIPT_AT = html.rfind('<script>')                 # everything after this is the deck's JavaScript
def slide_of(pos):
    if pos > SCRIPT_AT:
        return '(scripts: src/script.js, src/js/*.js)'
    m = None
    for m in re.finditer(r'<section[^>]*\bid="([^"]+)"', html[:pos]):
        pass
    return m.group(1) if m else '(head / shared CSS)'

todo = {}
for m in re.finditer(r'⟦([^⟧]{0,120})⟧', html):
    todo.setdefault(slide_of(m.start()), []).append(m.group(1))
if todo:
    print(f'TODO  {sum(len(v) for v in todo.values())} ⟦…⟧ marker(s) still to supply or verify:')
    for sid, items in todo.items():
        print(f'   {sid:12s} {len(items):3d}  e.g. ' + ' | '.join(i[:48] for i in items[:3]))

refs = sorted(set(re.findall(r'assets/[A-Za-z0-9_./-]+\.(?:jpg|jpeg|png|svg|webp)', html)))
ph = [r for r in refs if os.path.exists(os.path.join(ROOT, r)) and b'PLACEHOLDER-IMAGE' in open(os.path.join(ROOT, r), 'rb').read()]
if ph:
    print(f'PHOTO {len(ph)} placeholder image(s) still in the deck — replace with the client\'s real photography:')
    print('   ' + ', '.join(p.replace('assets/', '') for p in ph))
missing = [r for r in refs if not os.path.exists(os.path.join(ROOT, r))]
if missing:
    print('MISSING asset file(s):', ', '.join(missing))

for bad in CFG.get('residue', []):
    hits = [m.start() for m in re.finditer(re.escape(bad), html, flags=re.I)]   # case-insensitive: 'suite' also finds 'Suite'
    if hits:
        print(f'RESIDUE {bad!r}: {len(hits)} hit(s) in', ', '.join(sorted({slide_of(h) for h in hits})))

OUT = os.environ.get('OUT', 'index.html')
open(os.path.join(ROOT, OUT), 'w', encoding='utf8').write(html)
print(OUT, f'{len(html):,} bytes,', len(slides), 'slide files')
if OUT != 'index.html':
    sys.exit(0)

# ── standalone: one self-contained file, each asset stored ONCE ──
# Photos repeat across slides (a hero shot can appear 20+ times), so inlining at every use balloons the file.
# Instead: one table of data URIs (window.__ASSETS); CSS url(assets/x) → var(--aN), set from the table at load;
# <img src="assets/x"> → filled from the table just before the deck script runs; JS-built paths use asset() (script.js).
MIME = {'.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.svg': 'image/svg+xml', '.webp': 'image/webp',
        '.ttf': 'font/ttf', '.woff2': 'font/woff2', '.mp3': 'audio/mpeg', '.json': 'application/json'}
def data_uri(path):
    full = os.path.join(ROOT, path)
    ext = os.path.splitext(path)[1].lower()
    if not os.path.exists(full) or ext not in MIME:
        return None
    return f'data:{MIME[ext]};base64,' + base64.b64encode(open(full, 'rb').read()).decode()

art = html
# fonts: used once each, inline in place (var() is not allowed inside @font-face)
art = re.sub(r'''url\((["']?)(assets/[^"')]+\.(?:ttf|woff2))\1\)''', lambda m: f'url("{data_uri(m.group(2)) or m.group(2)}")', art)
paths = sorted(set(re.findall(r'assets/[A-Za-z0-9_./-]+\.(?:jpg|jpeg|png|svg|webp|mp3|json)', art)))
table = {p: data_uri(p) for p in paths}
table = {p: u for p, u in table.items() if u}
var = {p: f'--a{i}' for i, p in enumerate(table)}
art = re.sub(r'''url\((["']?)(assets/[^"')]+)\1\)''', lambda m: f'var({var[m.group(2)]})' if m.group(2) in var else m.group(0), art)
BLANK = 'data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='
art = re.sub(r'''(<img\b[^>]*?\s)src=(["'])(assets/[^"']+)\2''', lambda m: f'{m.group(1)}src="{BLANK}" data-asset="{m.group(3)}"' if m.group(3) in table else m.group(0), art)
boot = ('<script>window.__ASSETS=' + json.dumps(table) + ';(function(){var s=document.documentElement.style,V=' +
        json.dumps([[v, p] for p, v in var.items()]) + ';V.forEach(function(x){s.setProperty(x[0],\'url("\'+window.__ASSETS[x[1]]+\'")\')})})();</script>')
fill = '<script>document.querySelectorAll("img[data-asset]").forEach(function(i){i.src=window.__ASSETS[i.dataset.asset]});</script>'
art = art.replace('<body>', '<body>\n' + boot, 1)
last = art.rfind('<script>\n')                       # the deck script is the last <script> in the file
art = art[:last] + fill + '\n' + art[last:]
open(os.path.join(ROOT, 'standalone.html'), 'w', encoding='utf8').write(art)
mb = len(art.encode()) / 1e6
print(f'standalone.html {mb:.1f} MB, {len(table)} unique assets' +
      ('  ← over 16 MB: shrink the photos (about 1600px wide, JPEG quality 80) before publishing it as one file' if mb > 16 else ''))
