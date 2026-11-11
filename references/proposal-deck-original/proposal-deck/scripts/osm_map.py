#!/usr/bin/env python3
"""Draw a real map for a deck — true boundaries from OpenStreetMap, true-distance rings, labelled points — as inline SVG.

    python3 osm_map.py map.json out.svg

map.json (paths are relative to it; fetched shapes are cached in a geo/ folder beside it, so re-runs are offline):
{
  "user_agent": "proposal-map/1.0 (you@yourdomain.com)",       # required by OpenStreetMap's Nominatim usage policy
  "areas":  [ {"id": "newcastle", "osm": "R1234567", "class": "tier1"},        # by OSM id: R=relation, W=way, N=node
              {"id": "lakemac",   "q": "Lake Macquarie City Council, NSW", "class": "tier2"} ],   # or by search text
  "context": [ {"id": "centralcoast", "q": "Central Coast Council, NSW"} ],   # neighbours, drawn faint, so land isn't read as sea
  "water":  [ {"id": "lake", "q": "Lake Macquarie, NSW"} ],                    # cut out of the land (drawn in the sea colour)
  "centre": [151.75, -32.92],                                                  # lon, lat of the pin (the client)
  "rings_km": [10, 25, 50],
  "points": [ {"label": "CHARLESTOWN", "lon": 151.69, "lat": -32.96} ],
  "frame":  [151.27, 152.20, -33.16, -32.60],      # lon_min, lon_max, lat_min, lat_max — crop to the towns that matter
  "width": 1000,
  "detail": 0.0008                                  # Nominatim polygon_threshold: bigger = simpler, smaller file
}

Why: a hand-drawn map in a proposal reads as amateur. Look an ambiguous name up on openstreetmap.org and use its id
(search text can return a club or a street with the same name). Fetch the neighbouring areas as "context", or crop the
frame, otherwise land you didn't fetch reads as sea. Projection: equirectangular with x scaled by cos(latitude), so
distances are true in every direction and the rings are real circles. Map data © OpenStreetMap contributors (ODbL) —
keep the credit line the SVG includes.
Each area becomes <path id="<id>" class="area <class>">, each point a <g class="city">, each ring <circle class="ring">,
so the deck's CSS and JS (e.g. the reach tiers) can light them up by id.
"""
import json, math, os, sys, time, urllib.parse, urllib.request

if len(sys.argv) < 3:
    sys.exit(__doc__)
CFGP, OUT = sys.argv[1], sys.argv[2]
C = json.load(open(CFGP))
GEO = os.path.join(os.path.dirname(os.path.abspath(CFGP)), 'geo'); os.makedirs(GEO, exist_ok=True)
UA = C.get('user_agent') or sys.exit('Set "user_agent" in the config (Nominatim requires an identifying User-Agent).')
DETAIL = C.get('detail', 0.0008)

def fetch(item):
    path = os.path.join(GEO, item['id'] + '.json')
    if os.path.exists(path):
        d = json.load(open(path))
        return d[0] if isinstance(d, list) else d
    base = 'https://nominatim.openstreetmap.org/'
    common = {'format': 'json', 'polygon_geojson': 1, 'polygon_threshold': DETAIL}
    if 'osm' in item:
        url = base + 'lookup?' + urllib.parse.urlencode({**common, 'osm_ids': item['osm']})
    else:
        url = base + 'search?' + urllib.parse.urlencode({**common, 'q': item['q'], 'limit': 1})
    time.sleep(1.1)                                   # Nominatim's policy: at most one request a second
    data = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=60))
    if not data:
        sys.exit(f"Nothing found for {item} — check the name on openstreetmap.org and use its id instead.")
    print(f"fetched {item['id']}: {data[0].get('display_name', '')[:90]}")
    json.dump(data[0], open(path, 'w'))
    return data[0]

def polys(d):
    g = d['geojson']
    if g['type'] == 'Polygon': return [g['coordinates']]
    if g['type'] == 'MultiPolygon': return g['coordinates']
    return []                                         # a point or line: nothing to fill

AREAS = [(a, polys(fetch(a))) for a in C.get('areas', [])]
CONTEXT = [(a, polys(fetch(a))) for a in C.get('context', [])]
WATER = [(a, polys(fetch(a))) for a in C.get('water', [])]

if 'frame' in C:
    lo0, lo1, la0, la1 = C['frame']
else:                                                 # the bounding box of the areas, plus 4%
    pts = [pt for _, ps in AREAS for poly in ps for ring in poly for pt in ring]
    lo0, lo1 = min(p[0] for p in pts), max(p[0] for p in pts); la0, la1 = min(p[1] for p in pts), max(p[1] for p in pts)
    pad = .04 * max(lo1 - lo0, la1 - la0); lo0 -= pad; lo1 += pad; la0 -= pad; la1 += pad
kx = math.cos(math.radians((la0 + la1) / 2))
W = C.get('width', 1000); K = W / ((lo1 - lo0) * kx); H = round((la1 - la0) * K); KM = K / 111.32
xy = lambda lon, lat: ((lon - lo0) * kx * K, (la1 - lat) * K)

def d_attr(ps):
    return ' '.join('M' + ' L'.join('%.1f,%.1f' % xy(*c) for c in ring) + ' Z' for poly in ps for ring in poly)

out = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" class="osm-map" role="img" aria-label="Map">',
       f'<rect class="sea" width="{W}" height="{H}"/>']
out += [f'<path id="{a["id"]}" class="area ctx {a.get("class", "")}" d="{d_attr(ps)}" fill-rule="evenodd"/>' for a, ps in CONTEXT]
out += [f'<path id="{a["id"]}" class="area {a.get("class", "")}" d="{d_attr(ps)}" fill-rule="evenodd"/>' for a, ps in AREAS]
out += [f'<path id="{a["id"]}" class="water" d="{d_attr(ps)}" fill-rule="evenodd"/>' for a, ps in WATER]
if 'centre' in C:
    cx, cy = xy(*C['centre'])
    out += [f'<circle class="ring" id="ring{int(km)}" cx="{cx:.1f}" cy="{cy:.1f}" r="{km * KM:.1f}"/>'
            f'<text class="ring-l" x="{cx + km * KM * .707 + 4:.1f}" y="{cy - km * KM * .707:.1f}">{km:g} km</text>' for km in C.get('rings_km', [])]
    out.append(f'<circle class="pin" cx="{cx:.1f}" cy="{cy:.1f}" r="7"/>')
for p in C.get('points', []):
    x, y = xy(p['lon'], p['lat'])
    out.append(f'<g class="city" id="{p.get("id", "")}"><circle cx="{x:.1f}" cy="{y:.1f}" r="4"/>'
               f'<text x="{x + 9:.1f}" y="{y + 4:.1f}">{p["label"]}</text></g>')
out.append(f'<text class="credit" x="{W - 8}" y="{H - 8}" text-anchor="end">Map data © OpenStreetMap contributors</text>')
out.append('<style>.osm-map .sea{fill:#E7ECEC}.osm-map .area{fill:#EFE9DD;stroke:#C9BFAE;stroke-width:1}.osm-map .ctx{opacity:.55}'
           '.osm-map .water{fill:#E7ECEC;stroke:#C9BFAE;stroke-width:.6}.osm-map .ring{fill:none;stroke:#B57A2E;stroke-dasharray:5 5;opacity:.7}'
           '.osm-map .ring-l,.osm-map .credit{font:9px Jost,sans-serif;letter-spacing:.12em;fill:#8C8173}.osm-map .pin{fill:#13283A;stroke:#fff;stroke-width:2}'
           '.osm-map .city circle{fill:#8C8173}.osm-map .city text{font:600 10px Jost,sans-serif;letter-spacing:.14em;fill:#5A5249}</style></svg>')
open(OUT, 'w').write('\n'.join(out))
print(f'{OUT}: {W}×{H}, {len(AREAS)} areas, {len(CONTEXT)} context, {len(WATER)} water, {len(C.get("points", []))} points')
