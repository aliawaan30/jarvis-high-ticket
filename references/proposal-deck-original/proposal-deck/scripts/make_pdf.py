#!/usr/bin/env python3
"""Assemble the per-slide screenshots into the client PDF — one slide per page, each page exactly the slide's size.

    python3 make_pdf.py <shots-dir> <out.pdf> [--max-mb 15] [--width 1440]

Why screenshots and not the browser's Print → PDF: print reflows the page to A4, shifts it left, splits slides across
pages and drops dark bands and shadows. A screenshot per slide looks exactly like the deck did on the call.
Take the shots first:  node shoot.mjs <deck-dir> <shots-dir> --scale 1.5
Tall slides stay one tall page (a PDF reader scrolls them) — never cut a slide in half.
If the file is over --max-mb (email attachments get refused around 20 MB), it re-encodes smaller until it fits.
Needs Pillow (pip install pillow).
"""
import sys, os, glob, io, argparse
from PIL import Image

ap = argparse.ArgumentParser()
ap.add_argument('shots'); ap.add_argument('out')
ap.add_argument('--max-mb', type=float, default=15.0)
ap.add_argument('--width', type=int, default=1440, help='page width in px the shots are scaled to')
a = ap.parse_args()

files = sorted(glob.glob(os.path.join(a.shots, '*.jpg')) + glob.glob(os.path.join(a.shots, '*.png')))
if not files:
    sys.exit(f'No .jpg/.png slides in {a.shots} — run shoot.mjs first.')

def build(quality, scale):
    pages = []
    for f in files:
        im = Image.open(f).convert('RGB')
        w = int(a.width * scale)
        if im.width != w:
            im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        b = io.BytesIO(); im.save(b, 'JPEG', quality=quality, optimize=True); b.seek(0)
        pages.append(Image.open(b))
    buf = io.BytesIO()
    pages[0].save(buf, 'PDF', save_all=True, append_images=pages[1:], resolution=96 * scale)
    return buf.getvalue()

for q, s in [(88, 1.5), (82, 1.5), (80, 1.25), (76, 1.0), (70, 1.0), (62, 0.9)]:
    data = build(q, s)
    mb = len(data) / 1e6
    if mb <= a.max_mb:
        break
open(a.out, 'wb').write(data)
print(f'{a.out}: {len(files)} pages, {mb:.1f} MB (JPEG q{q}, {int(a.width * s)}px wide)'
      + ('' if mb <= a.max_mb else f'  — still over {a.max_mb} MB: send a link instead of an attachment'))
