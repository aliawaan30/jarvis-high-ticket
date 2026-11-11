# Generates the placeholder image set the template ships with: every photo slot in the deck points at one of these.
# Replace each file in assets/ with the prospect's REAL photography at the same name (or change the reference) —
# the deck must never ship with a placeholder in it (build.py lists any that are still referenced).
#   python3 build/placeholders.py      → assets/ph-*.jpg, proof-*.jpg, brand-*.png, partner-logo-*.png
import os, math, colorsys
from PIL import Image, ImageDraw, ImageFont, PngImagePlugin
MARK = 'PLACEHOLDER-IMAGE'   # build.py looks for this in every referenced asset and refuses to call the deck finished while one remains
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
A = os.path.join(ROOT, 'assets')
F_SANS = os.path.join(A, 'Jost.ttf'); F_SERIF = os.path.join(A, 'PlayfairDisplay.ttf')

# name, (w, h), what the real photo should show
PHOTOS = [
  ('ph-hero-pool', (1440, 810), 'Hero · the property at its best, landscape'),
  ('ph-pool-2', (1440, 810), 'Second hero angle · landscape'),
  ('ph-pool-3', (1440, 810), 'Amenity · pool or outdoor space'),
  ('ph-resort-tall', (1057, 1518), 'The whole property · portrait'),
  ('ph-facade', (1800, 1013), 'Exterior · architecture detail'),
  ('ph-site-1', (520, 339), 'Site / masterplan view · small'),
  ('ph-site-2', (520, 339), 'Second site view · small'),
  ('ph-suite-a', (1344, 837), 'Product A · main interior'),
  ('ph-suite-a2', (1344, 837), 'Product A · second interior'),
  ('ph-suite-b', (520, 520), 'Product B · main interior · square'),
  ('ph-suite-b2', (520, 520), 'Product B · lounge · square'),
  ('ph-balcony', (1152, 648), 'Balcony / outlook'),
  ('ph-view', (520, 520), 'The view · square'),
  ('ph-bath', (520, 520), 'Bathroom · square'),
  ('ph-bath2', (520, 520), 'Second bathroom · square'),
  ('ph-suite-detail', (520, 520), 'Interior detail · square'),
  ('ph-suite-day', (520, 520), 'Interior in daylight · square'),
  ('ph-event', (1327, 763), 'People · an owners / launch event'),
  ('ph-venue-1', (1327, 763), 'Brand venue or partner · 1'),
  ('ph-venue-2', (1327, 763), 'Brand venue or partner · 2'),
  ('ph-venue-3', (520, 620), 'Brand venue · daytime · portrait'),
  ('ph-aerial', (1800, 1326), 'Aerial / drone · the location'),
  ('ph-night', (1327, 763), 'The property at night'),
  ('ph-night-aerial', (520, 620), 'Night aerial · portrait'),
  ('ph-celebration', (520, 620), 'Lifestyle · celebration · portrait'),
  ('ph-family', (1440, 810), 'Families / kids amenity'),
  ('ph-kids', (1440, 810), 'Kids club or family space'),
  ('ph-kids2', (1440, 810), 'Second family space'),
  ('ph-dining', (1440, 810), 'Dining on site'),
  ('ph-wellness', (1440, 810), 'Wellness · spa / recovery'),
  ('ph-wellness2', (1440, 810), 'Wellness · second'),
  ('ph-spa', (1440, 810), 'Spa / salon'),
  ('ph-gym', (1800, 1013), 'Gym / fitness'),
  ('ph-bar', (1800, 1013), 'Bar / social space'),
  ('ph-leisure', (1800, 1013), 'Leisure amenity'),
  ('ph-member-card', (520, 620), 'Membership card on a phone · portrait'),
  ('ph-team-signing', (1327, 763), 'The people behind it · signing / handshake'),
  ('ph-case-study', (1200, 679), 'YOUR case study · the real project you sold'),
  ('ph-location-wide', (1400, 788), 'The location · wide'),
  ('ph-plane', (760, 428), 'Travel · plane window'),
  ('ph-signing', (760, 608), 'Paperwork · pen on contract'),
  ('ph-lifestyle', (1500, 1000), 'Lifestyle · people enjoying it'),
]
PROOF = [('proof-%d' % i, (1200, h)) for i, h in zip(range(1, 7), (199, 215, 242, 243, 282, 282))]

def font(p, s):
    return ImageFont.truetype(p, s)

def photo(name, size, label, i):
    w, h = size
    hue = (0.58 + 0.083 * (i % 7)) % 1.0           # cycle gently so neighbouring slots read as different photos
    c1 = [int(255 * v) for v in colorsys.hls_to_rgb(hue, 0.30, 0.22)]
    c2 = [int(255 * v) for v in colorsys.hls_to_rgb((hue + 0.08) % 1, 0.62, 0.20)]
    im = Image.new('RGB', size); px = im.load()
    for y in range(h):
        for x in range(0, w):
            t = min(1, max(0, (0.65 * y / h + 0.35 * x / w)))
            px[x, y] = tuple(int(c1[k] + (c2[k] - c1[k]) * t) for k in range(3))
    d = ImageDraw.Draw(im, 'RGBA')
    for k in range(-h, w, max(18, w // 40)):         # faint diagonal hatching = "this is a photo slot"
        d.line([(k, h), (k + h, 0)], fill=(255, 255, 255, 10), width=1)
    # the label sits small and faint in the bottom-right corner, so text the deck lays over the photo stays readable
    s = max(10, min(w, h) // 34)
    f = font(F_SANS, s)
    t = f'PHOTO · {label} · {name}.jpg'
    tw = d.textlength(t, font=f)
    if tw > w * .42:                                 # keep it in the corner — a wide label would sit under centred text
        t = f'PHOTO · {name}.jpg'; tw = d.textlength(t, font=f)
    if tw > w * .92:
        f = font(F_SANS, max(8, int(s * w * .92 / tw))); tw = d.textlength(t, font=f)
    pad = max(6, s // 2)
    x0, y0 = w - tw - pad * 3, h - s - pad * 3
    d.rounded_rectangle([x0, y0, w - pad, h - pad], radius=pad, fill=(0, 0, 0, 60))
    d.text((x0 + pad, y0 + pad * .55), t, font=f, fill=(255, 255, 255, 150))
    im.save(os.path.join(A, name + '.jpg'), quality=82, comment=MARK.encode())

def proof(name, size, i):
    w, h = size
    im = Image.new('RGB', size, (255, 255, 255)); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, w - 1, h - 1], outline=(206, 208, 212))
    f, fb = font(F_SANS, 22), font(F_SANS, 30)
    d.text((24, 18), 'Results', font=f, fill=(28, 30, 33)); d.text((w * .38, 18), 'Cost per result', font=f, fill=(28, 30, 33)); d.text((w * .7, 18), 'Budget', font=f, fill=(28, 30, 33))
    d.line([0, 58, w, 58], fill=(222, 224, 228))
    t = 'PASTE A REAL RESULTS SCREENSHOT HERE  ·  %s.jpg' % name
    d.text(((w - d.textlength(t, font=fb)) / 2, 58 + (h - 58) / 2 - 18), t, font=fb, fill=(24, 119, 242))
    im.save(os.path.join(A, name + '.jpg'), quality=86, comment=MARK.encode())

def _pi():
    i = PngImagePlugin.PngInfo(); i.add_text('Comment', MARK); return i

def logo(name, size, word, sub, col, bg=None, mono=None):
    w, h = size
    im = Image.new('RGBA', size, bg or (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    if mono:                                         # square avatar: monogram in a circle
        d.ellipse([0, 0, w - 1, h - 1], fill=(255, 255, 255, 255), outline=(220, 220, 220, 255))
        f = font(F_SERIF, int(h * .36)); tw = d.textlength(mono, font=f)
        d.text(((w - tw) / 2, h * .28), mono, font=f, fill=col); im.save(os.path.join(A, name + '.png'), pnginfo=_pi()); return
    f1 = font(F_SERIF, int(h * (.36 if sub else .62))); f2 = font(F_SANS, int(h * .13))
    tw = d.textlength(word, font=f1)
    if tw > w * .86:                                 # fit the word to the canvas — never clip a logo
        f1 = font(F_SERIF, int(f1.size * w * .86 / tw)); tw = d.textlength(word, font=f1)
    bb = d.textbbox((0, 0), word, font=f1)
    y = h * .16 if sub else (h - (bb[3] - bb[1])) / 2 - bb[1]
    d.text(((w - tw) / 2, y), word, font=f1, fill=col)
    if sub:
        sw = d.textlength(sub, font=f2); d.text(((w - sw) / 2, h * .66), sub, font=f2, fill=col)
        d.line([w * .2, h * .6, w * .8, h * .6], fill=col, width=max(2, h // 160))
    im.save(os.path.join(A, name + '.png'), pnginfo=_pi())

if __name__ == '__main__':
    for i, (n, sz, lab) in enumerate(PHOTOS): photo(n, sz, lab, i)
    for i, (n, sz) in enumerate(PROOF): proof(n, sz, i)
    NAVY, WHITE = (19, 40, 58, 255), (255, 255, 255, 255)
    logo('brand-logo-dark', (900, 529), 'KESTREL', 'B A Y   R E S O R T', NAVY)
    logo('brand-logo-light', (900, 529), 'KESTREL', 'B A Y   R E S O R T', WHITE)
    logo('brand-wordmark-light', (1000, 219), 'KESTREL BAY', None, WHITE)
    logo('brand-avatar', (400, 400), None, None, NAVY, mono='KB')
    logo('partner-logo-light', (600, 200), 'TIDEWATER', None, WHITE)
    print('placeholders written to', A)
