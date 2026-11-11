# Generates s14_structure.html — the buyer campaign: the live-ads wall (every square a live ad) and the ad-set viewer
# (product tabs, the Australia map, who each ad set finds, and its mini creatives, drawn by src/js/wall.js).
# For a new client, change the DATA below (PRODUCTS, SITE, SLOTS/PEEK, ANG, HOOKS, CTA, FORMATS, LOCS, T, BAND), then run
#   python3 build/gen_builds.py      → src/s14_structure.html   (never hand-edit the output)
import os, json, re
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'src')

# ══════════════════════════ the buyer campaign · Kestrel Bay Resort ══════════════════════════
# FOR A NEW CLIENT, edit only this data block (down to BAND), then run python3 build/gen_builds.py:
#   PRODUCTS  one entry per product — a tab, a colour, a column of the wall. Every product has the same number of angles,
#             and its key needs an entry in SLOTS, PEEK, ANG, PANEL, HOOKS, CTA and COL (one row per angle in ANG/HOOKS).
#   FORMATS   the ad formats: (name, layout family) — 'ph' photo · 'ca' carousel · 'vi' short video · 'st' story.
#   LOCS      one row per location. The row keyed 'RT' is retargeting (optional, lights every state). The last field names
#             the state outline(s) the location lights on the map — [] for none (its chip still works). T and ORIG need every key.
#   BAND      the descriptive words in the maths band.
# Every count on the slide follows the data — products × locations = ad sets; angles × formats = ads in an ad set;
# ad sets × ads = live ads. The eyebrow, the maths band and its dot grids, the wall, the tabs, the console labels, the
# auto-tour, the count-up, the presenter note and the retargeting styling are all worked out from these lists.
# Every product is always on. Every fact below is from source/facts.md — no yields, no returns, no sold-out claims.
PRODUCTS = [
    dict(key='gar', tag='Always on', name='The Garden Suite',
         sells='The entry suite &mdash; from US$165,000 (about A$240,000): 34&nbsp;m&sup2;, one bedroom, a garden terrace.',
         angles=['A Suite At Kestrel Bay', 'Who Runs It?', 'The Owners&rsquo; Club', 'Still Deciding?']),
    dict(key='oce', tag='Always on', name='The Ocean Suite',
         sells='The larger suite &mdash; US$260,000 (about A$375,000): 52&nbsp;m&sup2;, a balcony with daybed, an ocean outlook, and interconnecting options for families.',
         angles=['The Ocean Outlook', 'Room For Family?', 'Owners&rsquo; Privileges', 'Compare The Suites']),
    dict(key='club', tag='Always on', name='The Owners&rsquo; Club',
         sells='The owners&rsquo; membership &mdash; complimentary resort stays, priority bookings and member rates across Tidewater venues, valued up to US$15,000.',
         angles=['Owner, Not Guest', 'What&rsquo;s Included?', 'Member Rates', 'Come Back An Owner']),
    dict(key='kxt', tag='Always on', name='Kestrel &times; Tidewater',
         sells='Who is behind it &mdash; Kestrel, 18 years and 600+ units delivered, with Tidewater Hospitality running the resort.',
         angles=['Built By Kestrel', 'Who&rsquo;s Behind It?', 'The Owners&rsquo; Club', 'Ask The Developer']),
]
# The words on every mini creative that aren't per-ad: the Facebook / Instagram page name, the map pin on the carousel,
# the location sticker on the story, and the boarding pass's destination (airport code, city).
SITE = dict(page='Kestrel Bay Resort', pin='BALI, INDONESIA', sticker='KESTREL BAY RESORT', dest=['DPS', 'Bali'])
# Photos: the client's own photography only (assets/ph-*.jpg placeholders until it arrives), chosen per creative so the
# picture matches the line. SLOTS[product][creative] = candidates; a location uses candidate[location % len].
# Creative = angle × (number of formats) + format, so one list per angle × format. The carousels of angles 2 and 4
# (the steps and the Q&A — here creatives 5 and 13) carry no photo: leave them []. PEEK = the second card of the angle-one carousel.
SLOTS = {
 'gar':  [['ph-suite-a', 'ph-suite-a2'], ['ph-suite-a2', 'ph-suite-a'], ['ph-hero-pool', 'ph-pool-2'], ['ph-resort-tall', 'ph-night-aerial'],
          ['ph-venue-1', 'ph-venue-2'], [], ['ph-pool-3', 'ph-dining'], ['ph-view', 'ph-bath2'],
          ['ph-venue-3', 'ph-bar'], ['ph-aerial', 'ph-location-wide'], ['ph-plane'], ['ph-member-card', 'ph-event'],
          ['ph-suite-day', 'ph-suite-detail'], [], ['ph-lifestyle', 'ph-wellness'], ['ph-family', 'ph-celebration']],
 'oce':  [['ph-suite-b', 'ph-suite-b2'], ['ph-balcony', 'ph-view'], ['ph-hero-pool', 'ph-pool-2'], ['ph-family', 'ph-pool-3'],
          ['ph-kids', 'ph-kids2'], [], ['ph-suite-day', 'ph-family'], ['ph-lifestyle', 'ph-celebration'],
          ['ph-venue-2', 'ph-venue-1'], ['ph-aerial', 'ph-location-wide'], ['ph-plane'], ['ph-member-card', 'ph-event'],
          ['ph-view', 'ph-balcony'], [], ['ph-suite-a', 'ph-suite-a2'], ['ph-night', 'ph-wellness']],
 'club': [['ph-hero-pool', 'ph-pool-2'], ['ph-pool-3', 'ph-resort-tall'], ['ph-lifestyle', 'ph-celebration'], ['ph-venue-3', 'ph-night-aerial'],
          ['ph-member-card', 'ph-event'], [], ['ph-wellness', 'ph-spa'], ['ph-venue-1', 'ph-venue-2'],
          ['ph-dining', 'ph-bar'], ['ph-aerial', 'ph-location-wide'], ['ph-plane'], ['ph-night', 'ph-venue-3'],
          ['ph-suite-day', 'ph-suite-b2'], [], ['ph-family', 'ph-kids'], ['ph-gym', 'ph-leisure']],
 'kxt':  [['ph-team-signing'], ['ph-resort-tall', 'ph-hero-pool'], ['ph-pool-2', 'ph-pool-3'], ['ph-night-aerial', 'ph-celebration'],
          ['ph-event', 'ph-venue-2'], [], ['ph-site-1', 'ph-site-2'], ['ph-view', 'ph-suite-day'],
          ['ph-facade', 'ph-night'], ['ph-aerial', 'ph-location-wide'], ['ph-plane'], ['ph-member-card', 'ph-venue-3'],
          ['ph-venue-1', 'ph-signing'], [], ['ph-lifestyle', 'ph-dining'], ['ph-bar', 'ph-wellness']]}
PEEK = {'gar': ['ph-suite-detail', 'ph-bath'], 'oce': ['ph-bath2', 'ph-bath'], 'club': ['ph-suite-a', 'ph-suite-b'], 'kxt': ['ph-suite-a', 'ph-suite-b']}
# what each angle says in the layouts that need more than the headline (row = angle; each format family uses its own fields;
# angles 5+ reuse the layouts of angles 1–4 in turn, so they need the same fields as angle 1, 2, 3, 4 …)
#   angle 1 = own a suite at Kestrel Bay · angle 2 = the doubts that stop a sale · angle 3 = the owners' membership · angle 4 = for buyers still deciding
ANG = {
 'gar':  [dict(poll=['Would you own a suite at Kestrel Bay?', 'Tell me more', 'Just looking']),
          dict(steps=['Ask your questions', 'A private call'], chat=['Who looks after it when I&rsquo;m home?', 'Tidewater Hospitality runs the resort day to day.'], ask='What would you ask before buying a suite?'),
          dict(num='12', numL='Tidewater venues &middot; member rates for owners'),
          dict(checks=['From US$165,000 &middot; about A$240k', '34&nbsp;m&sup2; &middot; one bedroom', 'A garden terrace'], qa=['What is it in Australian dollars?', 'About A$240,000 &mdash; from US$165,000.'])],
 'oce':  [dict(poll=['Holiday in Bali as a family?', 'Every year', 'Now and then']),
          dict(steps=['Tell us who travels', 'See it on a private call'], chat=['Is there room for the kids?', '52&nbsp;m&sup2;, with interconnecting options for families.'], ask='Who would you bring to Kestrel Bay?'),
          dict(pre='Close to', num='900K', numL='guests a year at Tidewater venues &middot; owners get member rates'),
          dict(checks=['US$260,000 &middot; about A$375k', '52&nbsp;m&sup2; &middot; balcony with daybed', 'An ocean outlook'], qa=['Garden Suite or Ocean Suite?', '34&nbsp;m&sup2; or 52&nbsp;m&sup2; &mdash; we walk you through both.'])],
 'club': [dict(poll=['Stayed at a Tidewater venue?', 'Many times', 'Not yet']),
          dict(sl='Included', steps=['Complimentary resort stays', 'Priority bookings'], chat=['What do owners actually get?', 'Resort stays, priority bookings and member rates across Tidewater venues.'], ask='Which Tidewater venue is your favourite?'),
          dict(pre='Valued up to', num='US$15,000', numL='The Owners&rsquo; Club &middot; for suite owners'),
          dict(checks=['Complimentary resort stays', 'Priority bookings', 'Invitations to events'], qa=['What is the membership worth?', 'Valued up to US$15,000, for suite owners.'])],
 'kxt':  [dict(poll=['Heard of Kestrel Developments?', 'Yes', 'Tell me more']),
          dict(sl='Who&rsquo;s who', steps=['Kestrel builds it', 'Tidewater runs it'], chat=['Who is actually behind it?', 'Kestrel builds it, and Tidewater Hospitality runs it.'], ask='What would you ask the developer?'),
          dict(num='600+', numL='units delivered &middot; Kestrel Developments'),
          dict(checks=['Built by Kestrel &middot; 18 years', 'Run by Tidewater Hospitality', '9 developments'], qa=['Who builds it?', 'Kestrel Developments &mdash; 18 years and 9 developments.'])]}
PANEL = {'gar': ('#B57A2E', '#FBF7F0'), 'oce': ('#13283A', '#E2B872'), 'club': ('#2F7F9A', '#FBF7F0'), 'kxt': ('#6B7F4E', '#FBF7F0')}
ORIG = {'WA': 'PER', 'NSW': 'SYD', 'VIC': 'MEL', 'QLD': 'BNE', 'SA': 'ADL', 'ATN': 'DRW', 'RT': 'AUS'}
HOOKS = {'gar':  ['Own a suite at Kestrel Bay Resort. From US$165,000.', 'Who runs it while you&rsquo;re home? Tidewater does.',
                  'Suite owners join The Owners&rsquo; Club.', 'Book a private call with our sales team.'],
         'oce':  ['Own the Ocean Suite at Kestrel Bay Resort.', 'Coming with family? Ask about connecting suites.',
                  'Owners get priority bookings and member rates.', 'Compare both suites on a private call.'],
         'club': ['Come to Kestrel Bay as an owner, not a guest.', 'What do owners get? Here&rsquo;s the list.',
                  'The Owners&rsquo; Club. Member rates across Tidewater venues.', 'See the membership on a private call.'],
         'kxt':  ['Built by Kestrel. Run by Tidewater. Own a suite.', 'Who&rsquo;s behind it? Kestrel: 18 years. Tidewater runs it.',
                  'From Kestrel and Tidewater: The Owners&rsquo; Club.', 'Bring your questions to a private call.']}
CTA = {'gar': ('From US$165,000', 'Learn more'), 'oce': ('US$260,000 &middot; 52&nbsp;m&sup2;', 'Learn more'),
       'club': ('The Owners&rsquo; Club', 'Sign up'), 'kxt': ('Kestrel &times; Tidewater &middot; Bali', 'Learn more')}
FORMATS = [('Photo', 'ph'), ('Carousel', 'ca'), ('Short video', 'vi'), ('Story', 'st')]
COL = {'gar': '#B57A2E', 'oce': '#13283A', 'club': '#2F7F9A', 'kxt': '#6B7F4E'}
LOCS = [   # key, short, full name, '' (or 'Warm' for retargeting), the metro areas,
           # the state outline(s) it lights on the map (WA NT SA QLD NSW VIC TAS ACT — each in one location at most; [] = none)
    ('WA', 'WA', 'Western Australia', '', 'Perth metro &middot; Mandurah &middot; Bunbury', ['WA']),
    ('NSW', 'NSW', 'New South Wales', '', 'Sydney metro &middot; Newcastle &middot; Wollongong', ['NSW']),
    ('VIC', 'VIC', 'Victoria', '', 'Melbourne metro &middot; Geelong', ['VIC']),
    ('QLD', 'QLD', 'Queensland', '', 'Brisbane &middot; Gold Coast &middot; Sunshine Coast', ['QLD']),
    ('SA', 'SA', 'South Australia', '', 'Adelaide metro &middot; Adelaide Hills', ['SA']),
    ('ATN', 'ACT &middot; TAS &middot; NT', 'ACT, Tasmania &amp; the Northern Territory', '', 'Canberra &middot; Hobart &middot; Darwin', ['NT', 'TAS', 'ACT']),
    ('RT', 'Retargeting', 'Retargeting &middot; every state', 'Warm', 'People who have already engaged with Kestrel Bay Resort', []),
]
# location → product → who the ad set looks for, written the way the audience is built in Meta Ads Manager:
# flight routes, interests, behaviours, parents' ages, lookalikes and (for retargeting) the engagement event + its window. No statistics.
T = {
 'WA':  {'gar':  ['Perth &#8644; Denpasar flyers &middot; frequent international travellers', 'Interests: Bali &middot; real estate investing &middot; holiday homes', 'Lookalike 1% of your verified enquirers &middot; WA'],
         'oce':  ['Parents with children aged 3&ndash;12 &middot; Perth metro', 'Interests: family holidays &middot; kids&rsquo; clubs &middot; Bali', 'Lookalike 1% of your verified enquirers &middot; WA'],
         'club': ['Behaviours: frequent international travellers', 'Interests: resorts &middot; day spas &middot; beach clubs', 'Lookalike 1% of your verified enquirers &middot; WA'],
         'kxt':  ['Interests: real estate investing &middot; property development', 'Behaviours: small-business owners', 'Lookalike 1% of your customer list &middot; past buyers']},
 'NSW': {'gar':  ['Sydney &#8644; Denpasar flyers &middot; frequent international travellers', 'Interests: overseas property &middot; holiday homes &middot; Bali', 'Lookalike 1% of your verified enquirers &middot; NSW'],
         'oce':  ['Parents with children aged 3&ndash;12 &middot; Sydney &amp; Newcastle', 'Interests: family travel &middot; resort holidays &middot; Bali', 'Lookalike 1% of your verified enquirers &middot; NSW'],
         'club': ['Interests: beach clubs &middot; resorts &middot; luxury travel', 'Behaviours: returned from travel in the last 2 weeks', 'Lookalike 1% of your verified enquirers &middot; NSW'],
         'kxt':  ['Interests: real estate investing &middot; business news', 'Behaviours: frequent international travellers', 'Lookalike 1% of your customer list &middot; past buyers']},
 'VIC': {'gar':  ['Melbourne &#8644; Denpasar flyers &middot; frequent international travellers', 'Interests: Bali &middot; holiday homes &middot; vacation rentals', 'Lookalike 1% of your verified enquirers &middot; VIC'],
         'oce':  ['Parents with children aged 3&ndash;12 &middot; Melbourne &amp; Geelong', 'Interests: school-holiday travel &middot; kids&rsquo; clubs', 'Lookalike 1% of your verified enquirers &middot; VIC'],
         'club': ['Interests: wellness travel &middot; spas &middot; yoga', 'Behaviours: frequent international travellers', 'Lookalike 1% of your verified enquirers &middot; VIC'],
         'kxt':  ['Interests: real estate investing &middot; hotels &amp; resorts', 'Behaviours: small-business owners', 'Lookalike 1% of your customer list &middot; past buyers']},
 'QLD': {'gar':  ['Brisbane &#8644; Denpasar flyers &middot; frequent international travellers', 'Interests: second homes &middot; holiday homes &middot; Bali', 'Lookalike 1% of your verified enquirers &middot; QLD'],
         'oce':  ['Parents with children aged 3&ndash;12 &middot; South East Queensland', 'Interests: family resorts &middot; kids&rsquo; clubs &middot; water parks', 'Lookalike 1% of your verified enquirers &middot; QLD'],
         'club': ['Interests: beach clubs &middot; resorts &middot; Bali', 'Behaviours: returned from travel in the last 2 weeks', 'Lookalike 1% of your verified enquirers &middot; QLD'],
         'kxt':  ['Interests: vacation rentals &middot; short-stay property', 'Interests: real estate investing &middot; property development', 'Lookalike 1% of your customer list &middot; past buyers']},
 'SA':  {'gar':  ['Adelaide &#8644; Denpasar flyers &middot; frequent international travellers', 'Interests: Bali &middot; overseas property', 'Lookalike 1% of your verified enquirers &middot; SA'],
         'oce':  ['Parents with children aged 3&ndash;12 &middot; Adelaide metro', 'Interests: family travel &middot; resort holidays', 'Lookalike 1% of your verified enquirers &middot; SA'],
         'club': ['Interests: resorts &middot; spas &middot; food &amp; wine travel', 'Behaviours: frequent international travellers', 'Lookalike 1% of your verified enquirers &middot; SA'],
         'kxt':  ['Interests: real estate investing &middot; personal finance', 'Behaviours: small-business owners', 'Lookalike 1% of your customer list &middot; past buyers']},
 'ATN': {'gar':  ['Darwin &#8644; Denpasar flyers &middot; frequent international travellers', 'Interests: Bali &middot; holiday homes', 'Lookalike 1% of your verified enquirers &middot; national'],
         'oce':  ['Parents with children aged 3&ndash;12 &middot; Canberra, Hobart, Darwin', 'Interests: family travel &middot; resort holidays', 'Lookalike 1% of your verified enquirers &middot; national'],
         'club': ['Interests: beach clubs &middot; resorts &middot; luxury travel', 'Behaviours: frequent international travellers', 'Lookalike 1% of your verified enquirers &middot; national'],
         'kxt':  ['Interests: real estate investing &middot; business news', 'Behaviours: small-business owners', 'Lookalike 1% of your customer list &middot; past buyers']},
 'RT':  {'gar':  ['Watched 50% of a Garden Suite video &middot; last 30 days', 'Opened the form, didn&rsquo;t submit &middot; last 30 days', 'Engaged with Kestrel Bay Resort on Instagram &middot; last 90 days'],
         'oce':  ['Swiped an Ocean Suite carousel &middot; last 30 days', 'Opened the form, didn&rsquo;t submit &middot; last 30 days', 'Visited the Kestrel Bay Resort website &middot; last 60 days'],
         'club': ['Watched 50% of an Owners&rsquo; Club video &middot; last 30 days', 'Opened the form, didn&rsquo;t submit &middot; last 30 days', 'Engaged with Kestrel Bay Resort on Facebook &middot; last 90 days'],
         'kxt':  ['Watched 50% of a Kestrel &times; Tidewater video &middot; last 30 days', 'Opened the form, didn&rsquo;t submit &middot; last 30 days', 'Saved or shared a Kestrel Bay Resort ad &middot; last 60 days']},
}
# The maths band's own words (its numbers are worked out): what follows "All four always on —", and what one
# non-retargeting location is called, singular and plural ("Six state groups, each targeted on its own").
BAND = dict(products='the two suites, the Owners&rsquo; Club, and who is behind it', places=('state group', 'state groups'))

# ══════════════════════════ worked out from the data — nothing below needs editing for a new client ══════════════════════════
NP, NL, NF = len(PRODUCTS), len(LOCS), len(FORMATS)               # products · locations · formats
NANG = len(PRODUCTS[0]['angles'])                                 # angles per product
ADS, SETS = NANG * NF, NP * NL                                    # ads in one ad set · ad sets
TOTAL = SETS * ADS                                                # live ads
RT = next((r for r, l in enumerate(LOCS) if l[0] == 'RT'), None)  # the retargeting location's index (None: no retargeting)
FAM = [fam for _, fam in FORMATS]                                 # each format's layout family
assert all(len(p['angles']) == NANG for p in PRODUCTS), 'every product needs the same number of angles'
assert all(f in ('ph', 'ca', 'vi', 'st') for f in FAM), 'FORMATS: the layout family is one of ph, ca, vi, st'
for p in PRODUCTS:
    for name, d in (('SLOTS', SLOTS), ('PEEK', PEEK), ('ANG', ANG), ('PANEL', PANEL), ('HOOKS', HOOKS), ('CTA', CTA), ('COL', COL)):
        assert p['key'] in d, f'{name} has no entry for product {p["key"]}'
    assert len(ANG[p['key']]) == len(HOOKS[p['key']]) == NANG, f'ANG and HOOKS need {NANG} rows (one per angle) for {p["key"]}'
for l in LOCS:
    assert len(l) == 6, f'LOCS row {l[0]}: key, short, full name, warm flag, metro areas, map states'
    assert l[0] in ORIG and l[0] in T and all(p['key'] in T[l[0]] for p in PRODUCTS), f'ORIG and T need location {l[0]} (every product)'
# the carousels of angles 2 and 4 (the steps and the Q&A layouts) carry no photo
NOPHOTO = {a * NF + f for a in range(NANG) for f, fam in enumerate(FAM) if fam == 'ca' and a % 4 in (1, 3)}
for p in PRODUCTS:                         # no ad set repeats a photo, in any location; every file exists
    k, slots = p['key'], SLOTS[p['key']]
    assert len(slots) == ADS, f'SLOTS[{k}] needs {ADS} lists (angles × formats)'
    assert all(slots[i] for i in range(ADS) if i not in NOPHOTO), f'SLOTS[{k}]: every creative except {sorted(NOPHOTO)} needs a photo'
    for r in range(NL):
        used = [s[r % len(s)] for i, s in enumerate(slots) if i not in NOPHOTO] + [PEEK[k][r % len(PEEK[k])]]
        assert len(used) == len(set(used)) == ADS - len(NOPHOTO) + 1, (k, r, used)
    for f in sum(slots, []) + PEEK[k]:
        assert os.path.exists(os.path.join(HERE, '..', 'assets', f + '.jpg')), f
IMGS = {k: {'s': [[f + '.jpg' for f in s] for s in v], 'k': [f + '.jpg' for f in PEEK[k]]} for k, v in SLOTS.items()}
# the copy spells small counts ("All four always on", "Sixteen ads in each") and writes the total in figures
_W = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty'.split()
def words(n): return _W[n] if 0 <= n < len(_W) else str(n)
def cap(s): return s[:1].upper() + s[1:]
def pl(n, one, many=None): return one if n == 1 else (many or one + 's')

# ── the map: real state outlines (Natural Earth, public domain), projected equirectangularly at 26°S ──
import math
AUS = json.load(open(os.path.join(HERE, '..', 'assets', 'cb-aus-paths.json'), encoding='utf8'))
_C = math.cos(math.radians(26))
def MP(lon, lat): return ((lon - 112.2) * _C * 20.0, (-7.2 - lat) * 20.0)
BALI = MP(115.22, -8.65)
CITIES = [  # name, lon, lat, the state it is in, label dx, dy, anchor (None = no label)
    ('Perth', 115.86, -31.95, 'WA', 9, 4, 'start'), ('Sydney', 151.21, -33.87, 'NSW', 9, 5, 'start'), ('Melbourne', 144.96, -37.81, 'VIC', 0, 20, 'middle'),
    ('Brisbane', 153.03, -27.47, 'QLD', -9, 4, 'end'), ('Adelaide', 138.60, -34.93, 'SA', -9, 4, 'end'), ('Darwin', 130.84, -12.46, 'NT', 9, 4, 'start'),
    ('Hobart', 147.33, -42.88, 'TAS', 9, 5, 'start'), ('Canberra', 149.13, -35.28, 'ACT', None, None, None)]
STATES = [('WA', 172, 360), ('NT', 382, 236), ('SA', 408, 452), ('QLD', 596, 268), ('NSW', 618, 482),
          ('VIC', 560, 588), ('TAS', 612, 697), ('ACT', 722, 618)]   # state, label x, y
# which location lights each state outline (from the last field of LOCS); states no location names stay unlit and untappable
SR = {}
for r, l in enumerate(LOCS):
    for s in l[5]:
        assert s in AUS and s != 'BALI', f'LOCS {l[0]}: no map outline called {s}'
        assert s not in SR, f'state {s} is in two locations'
        SR[s] = r
MAPPED = sorted(set(SR.values()))          # the locations that have a shape on the map
DR = lambda s: f' data-r="{SR[s]}"' if s in SR else ''
# the map: each mapped location is a tap target, the retargeting pill is another; a flight line runs from each targeted city to Bali
def aus_svg():
    arcs = ''
    for name, lon, lat, s, *_ in CITIES:
        if s not in SR: continue
        r = SR[s]
        x1, y1 = MP(lon, lat); x2, y2 = BALI
        dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy)
        px, py = -dy / L, dx / L
        if -py + px < 0: px, py = -px, -py
        cx, cy = (x1 + x2) / 2 + px * L * .16, (y1 + y2) / 2 + py * L * .16
        arcs += f'<path class="bx-arc" data-r="{r}" d="M{x1:.1f},{y1:.1f} Q{cx:.1f},{cy:.1f} {x2:.1f},{y2:.1f}"/>'
    shapes = ''
    for k, lx, ly in STATES:
        shapes += f'<path class="bx-st"{DR(k)} data-s="{k}" d="{AUS[k]}"/>'
    labels = ''.join(f'<text class="bx-sl{" out" if k == "ACT" else ""}"{DR(k)} x="{lx}" y="{ly}">{k}</text>' for k, lx, ly in STATES)
    cx, cy = MP(149.13, -35.28)
    labels += f'<path class="bx-co"{DR("ACT")} d="M{cx + 4:.1f},{cy + 4:.1f} L704,604"/>'
    pins = ''
    for name, lon, lat, s, ddx, ddy, anc in CITIES:
        if s not in SR: continue
        x, y = MP(lon, lat)
        pins += f'<circle class="bx-pin" data-r="{SR[s]}" cx="{x:.1f}" cy="{y:.1f}" r="4.5"/>'
        if ddx is not None:
            pins += f'<text class="bx-cy" data-r="{SR[s]}" x="{x + ddx:.1f}" y="{y + ddy:.1f}" text-anchor="{anc}">{name}</text>'
    bx, by = BALI
    hits = ''.join(f'<g class="bx-hit" data-r="{r}" role="button" tabindex="0" aria-label="{LOCS[r][2].replace(" &amp; ", " and ")}">'
                   f'<path d="{"".join(AUS[s] for s in LOCS[r][5])}"/></g>' for r in MAPPED)
    rt = '' if RT is None else f'''
      <g class="bx-rt" data-r="{RT}" role="button" tabindex="0" aria-label="Retargeting &mdash; every state" transform="translate(26,604)">
        <rect width="262" height="64" rx="32"/><circle class="bx-rt-o" cx="32" cy="32" r="19"/>
        <path class="bx-rt-i" d="M24 28a9 9 0 0 1 16-3M40 36a9 9 0 0 1-16 3M40 21v5h-5M24 43v-5h5"/>
        <text class="bx-rt-a" x="62" y="29">Retargeting</text><text class="bx-rt-b" x="62" y="48">every state &middot; warm audiences</text></g>'''
    return f'''<svg class="bx-svg" viewBox="0 0 770 740" role="group" aria-label="Australia &mdash; tap a location">
      <defs><radialGradient id="bxGlow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#E2B872" stop-opacity=".55"/><stop offset="1" stop-color="#E2B872" stop-opacity="0"/></radialGradient></defs>
      <g class="bx-grat">{"".join(f'<path d="M0,{MP(0, -lat)[1]:.0f} H770"/>' for lat in (10, 20, 30, 40))}{"".join(f'<path d="M{MP(lon, 0)[0]:.0f},0 V740"/>' for lon in (120, 130, 140, 150))}</g>
      <g class="bx-lands">{shapes}</g>
      <g class="bx-arcs">{arcs}</g>
      <circle class="bx-bglow" cx="{bx:.1f}" cy="{by:.1f}" r="46" fill="url(#bxGlow)"/>
      <path class="bx-bali" d="{AUS["BALI"]}"/>
      <text class="bx-bl" x="{bx + 20:.1f}" y="{by + 4:.1f}">Bali</text>
      {pins}{labels}
      {hits}{rt}
      <text class="bx-hint" x="758" y="30" text-anchor="end">Tap a location</text>
      <text class="bx-cr" x="26" y="728">Boundaries: Natural Earth</text>
    </svg>'''

CSS_B = '<style>' + '''
  #structure .wrap { max-width:1220px; }
  #structure .head p { max-width:720px; }
  /* ── the console: map + location → its ads ── */
  #structure .bx-con { position:relative; background:radial-gradient(110% 80% at 30% 0%, #21405A, #13283A 62%); color:#FBF7F0; border-radius:26px; box-shadow:var(--sh-lg); overflow:hidden; }
  #structure .bx-in { padding:22px 26px 24px; }
  #structure .bx-tabs { display:grid; grid-template-columns:repeat(__P__,minmax(0,1fr)); gap:10px; }
  #structure .bx-tab { font:inherit; cursor:pointer; text-align:left; color:#FBF7F0; background:rgba(251,247,240,.04); border:1px solid rgba(251,247,240,.1); border-radius:14px; padding:10px 14px 9px; display:grid; grid-template-columns:auto minmax(0,1fr) auto; gap:2px 10px; align-items:center; transition:background .2s, border-color .2s, transform .2s; }
  #structure .bx-tab:hover { border-color:rgba(226,184,114,.45); }
  #structure .bx-tab i { grid-row:1 / 3; width:14px; height:14px; border-radius:4px; background:var(--c); box-shadow:inset 0 0 0 1px rgba(251,247,240,.45); }
  #structure .bx-tab b { font-size:14px; font-weight:600; line-height:1.15; }
  #structure .bx-tab small { grid-column:2; font-size:9.5px; letter-spacing:.14em; text-transform:uppercase; font-weight:700; color:rgba(251,247,240,.5); }
  #structure .bx-tab em { grid-row:1 / 3; grid-column:3; font-style:normal; font-family:'Playfair',serif; font-size:22px; color:rgba(251,247,240,.35); }
  #structure .bx-tab.on { background:#FBF7F0; border-color:#FBF7F0; color:#13283A; box-shadow:0 10px 24px rgba(0,0,0,.35); }
  #structure .bx-tab.on small { color:var(--gold-d); } #structure .bx-tab.on em { color:#13283A; }
  #structure .bx-g { display:grid; grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr); gap:26px; margin-top:18px; }
  #structure .bx-map { position:relative; }
  #structure .bx-svg { display:block; width:100%; height:auto; overflow:visible; }
  #structure .bx-grat path { stroke:rgba(251,247,240,.05); stroke-width:1; fill:none; }
  #structure .bx-st { fill:rgba(251,247,240,.07); stroke:rgba(226,184,114,.42); stroke-width:1.2; stroke-linejoin:round; transition:fill .35s, stroke .35s; }
  #structure .bx-bali { fill:#E2B872; stroke:none; }
  #structure .bx-bl { fill:#E2B872; font:italic 500 21px 'Playfair',serif; }
  #structure .bx-bglow { opacity:.8; }
  #structure .bx-arc { fill:none; stroke:rgba(226,184,114,.16); stroke-width:1.3; stroke-dasharray:3 6; transition:stroke .35s; }
  #structure .bx-pin { fill:#13283A; stroke:rgba(226,184,114,.7); stroke-width:2; transition:fill .3s; }
  #structure .bx-cy { fill:rgba(251,247,240,.55); font:500 14px 'Jost',sans-serif; letter-spacing:.02em; pointer-events:none; }
  #structure .bx-sl { fill:rgba(251,247,240,.82); font:600 25px 'Jost',sans-serif; letter-spacing:.1em; text-anchor:middle; pointer-events:none; transition:fill .3s; }
  #structure .bx-co { stroke:rgba(226,184,114,.5); stroke-width:1; fill:none; }
  #structure .bx-hit { cursor:pointer; outline:none; } #structure .bx-hit path { fill:transparent; stroke:none; }
  #structure .bx-hit:hover path { fill:rgba(251,247,240,.07); } #structure .bx-hit:focus-visible path { stroke:#FBF7F0; stroke-width:2; }
  #structure .bx-rt { cursor:pointer; outline:none; }
  #structure .bx-rt rect { fill:rgba(251,247,240,.05); stroke:rgba(226,184,114,.45); stroke-width:1.2; stroke-dasharray:4 4; transition:fill .3s; }
  #structure .bx-rt-o { fill:rgba(226,184,114,.16); }
  #structure .bx-rt-i { fill:none; stroke:#E2B872; stroke-width:2.2; stroke-linecap:round; stroke-linejoin:round; }
  #structure .bx-rt-a { fill:#FBF7F0; font:600 19px 'Jost',sans-serif; }
  #structure .bx-rt-b { fill:rgba(251,247,240,.55); font:400 14px 'Jost',sans-serif; }
  #structure .bx-rt:hover rect, #structure .bx-rt:focus-visible rect { fill:rgba(226,184,114,.12); }
  #structure .bx-hint { fill:#E2B872; font:700 13px 'Jost',sans-serif; letter-spacing:.2em; text-transform:uppercase; }
  #structure .bx-cr { fill:rgba(251,247,240,.3); font:400 11px 'Jost',sans-serif; letter-spacing:.06em; }
  /* the selected location lights up (the attribute is set by wall.js; r0 is the rest state) — written by lit_css() */
  __LIT__
  @keyframes bxFly { to { stroke-dashoffset:-130; } }
  @keyframes bxPulse { 50% { opacity:.35; } }
  @media (prefers-reduced-motion:no-preference) {
    body.anim #structure .bx-arc { animation:bxFly 5s linear infinite; }
    body.anim #structure .bx-bglow { animation:bxPulse 3.2s ease-in-out infinite; }
    __RTANIM__
  }
  #structure .bx-chips { display:flex; flex-wrap:wrap; gap:6px; margin-top:6px; }
  #structure .bx-chip { font:inherit; cursor:pointer; display:flex; align-items:baseline; gap:6px; color:#FBF7F0; background:rgba(251,247,240,.05); border:1px solid rgba(251,247,240,.12); border-radius:16px; padding:6px 11px 5px; font-size:12px; font-weight:600; transition:all .2s; }
  #structure .bx-chip small { font-size:10px; font-weight:500; color:rgba(251,247,240,.45); }
  #structure .bx-chip:hover { border-color:rgba(226,184,114,.5); }
  #structure .bx-chip.on { background:var(--gold-lite); border-color:var(--gold-lite); color:#13283A; } #structure .bx-chip.on small { color:rgba(19,40,58,.65); }
  #structure .bx-who { margin-top:14px; border-top:1px solid rgba(251,247,240,.1); padding-top:12px; }
  #structure .bx-k { font-size:9.5px; letter-spacing:.2em; text-transform:uppercase; font-weight:700; color:var(--gold-lite); }
  #structure .bx-who ul { list-style:none; margin-top:8px; display:grid; gap:6px; }
  #structure .bx-who li { display:grid; grid-template-columns:22px minmax(0,1fr); gap:9px; align-items:center; font-size:13px; line-height:1.35; color:rgba(251,247,240,.86); }
  #structure .bx-who li i { width:22px; height:22px; border-radius:50%; background:rgba(226,184,114,.15); color:var(--gold-lite); font-style:normal; font-size:11px; font-weight:700; display:flex; align-items:center; justify-content:center; }
  #structure .bx-who p { margin-top:9px; font-size:12px; line-height:1.5; color:rgba(251,247,240,.55); font-style:italic; }
  /* the right-hand side: the location's header + one ad set's creatives (angles × formats) */
  #structure .bx-dh { display:flex; justify-content:space-between; align-items:flex-end; gap:12px; padding-bottom:12px; border-bottom:1px solid rgba(251,247,240,.1); }
  #structure .bx-dh h3 { font-family:'Playfair',serif; font-weight:500; font-size:30px; line-height:1.08; margin-top:4px; }
  #structure .bx-dh h3 em { font-style:italic; color:var(--gold-lite); }
  #structure .bx-dh .bx-m { font-size:12px; color:rgba(251,247,240,.55); margin-top:4px; }
  #structure .bx-n { text-align:right; flex:none; }
  #structure .bx-n b { display:block; font-family:'Playfair',serif; font-weight:500; font-size:44px; line-height:.9; color:var(--gold-lite); font-variant-numeric:tabular-nums; }
  #structure .bx-n small { display:block; font-size:9.5px; letter-spacing:.16em; text-transform:uppercase; font-weight:700; color:rgba(251,247,240,.55); margin-top:5px; }
  #structure .bx-ads { display:grid; grid-template-columns:70px repeat(__F__,minmax(0,1fr)); gap:9px 10px; margin-top:12px; }
  #structure .bx-fh { font-size:9px; letter-spacing:.16em; text-transform:uppercase; font-weight:700; color:rgba(251,247,240,.5); text-align:center; }
  #structure .bx-an { display:flex; flex-direction:column; justify-content:center; font-size:11.5px; font-weight:600; line-height:1.25; color:#FBF7F0; }
  #structure .bx-an small { font-size:9px; letter-spacing:.14em; text-transform:uppercase; color:var(--gold-lite); font-weight:700; margin-bottom:3px; }
  #structure .bx-foot { display:flex; justify-content:space-between; gap:10px; flex-wrap:wrap; margin-top:12px; font-size:11.5px; color:rgba(251,247,240,.55); }
  #structure .bx-foot b { color:#FBF7F0; font-weight:600; }

  /* ── a mini creative: sixteen different layouts, sized in cqw so they scale crisply when zoomed ── */
  #structure .bx-cell { position:relative; aspect-ratio:4/5; container-type:inline-size; z-index:1; }
  #structure .bx-ad { position:absolute; inset:0; border-radius:3.5cqw; overflow:hidden; background:#fff; color:#050505; box-shadow:0 6px 16px rgba(0,0,0,.35); cursor:zoom-in; transition:transform .28s cubic-bezier(.2,.8,.2,1), box-shadow .28s; transform-origin:var(--ox) var(--oy); display:flex; flex-direction:column; }
  #structure .bx-cell:hover, #structure .bx-cell.z { z-index:8; }
  #structure .bx-cell:hover .bx-ad, #structure .bx-cell.z .bx-ad { transform:scale(2.15); box-shadow:0 24px 60px rgba(0,0,0,.6); }
  #structure .bx-ad .ph { position:relative; background:#13283A center/cover; }
  #structure .bx-ad .md { position:relative; flex:none; height:100cqw; overflow:hidden; }
  /* the client's logos: the wide white wordmark on photos and colour; the stacked navy logo (about 1.7:1) on white, given room */
  #structure .bx-ad .lk { display:block; width:24cqw; height:6.7cqw; background:url(assets/brand-wordmark-light.png) left center/contain no-repeat; }
  #structure .bx-ad .lk.d { width:15cqw; height:8.8cqw; background-image:url(assets/brand-logo-dark.png); }
  #structure .bx-ad .hd { flex:none; display:flex; align-items:center; gap:2.4cqw; height:13cqw; padding:0 3.4cqw; position:relative; z-index:3; }
  #structure .bx-ad .hd i { flex:none; width:7.6cqw; height:7.6cqw; border-radius:50%; background:#fff url(assets/brand-avatar.png) center/cover no-repeat; box-shadow:inset 0 0 0 .3cqw #E4E6EB; }
  #structure .bx-ad .hd b { display:block; font:700 5cqw/1.1 -apple-system,'Helvetica Neue',Arial,sans-serif; color:inherit; }
  #structure .bx-ad .hd small { display:block; font:400 4cqw/1.1 -apple-system,'Helvetica Neue',Arial,sans-serif; opacity:.65; }
  #structure .bx-ad .ct { flex:none; display:flex; justify-content:space-between; align-items:center; gap:2cqw; background:#F0F2F5; padding:0 3.2cqw; height:12cqw; margin-top:auto; }
  #structure .bx-ad .ct span { font:600 4.3cqw/1.15 -apple-system,'Helvetica Neue',Arial,sans-serif; color:#050505; overflow:hidden; white-space:nowrap; text-overflow:ellipsis; }
  #structure .bx-ad .ct em { flex:none; font:700 4cqw/1 -apple-system,'Helvetica Neue',Arial,sans-serif; font-style:normal; background:#E4E6EB; border-radius:1.6cqw; padding:2cqw 2.6cqw; }
  #structure .bx-ad .fill { position:absolute; inset:0; background:#13283A center/cover; }
  /* PHOTO · p0 editorial */
  #structure .p0 .md::after { content:''; position:absolute; inset:0; background:linear-gradient(180deg,rgba(0,0,0,.35),rgba(0,0,0,0) 30%,rgba(0,0,0,0) 45%,rgba(0,0,0,.78)); }
  #structure .p0 .lk { position:absolute; z-index:2; left:5cqw; top:5cqw; }
  #structure .p0 .t { position:absolute; z-index:2; left:5cqw; right:6cqw; bottom:5cqw; font:italic 500 9cqw/1.05 'Playfair',serif; color:#fff; }
  #structure .p0 .t::before { content:''; display:block; width:10cqw; height:.8cqw; background:var(--gold-lite); margin-bottom:2.4cqw; }
  /* PHOTO · p1 split panel */
  #structure .p1 .md { display:grid; grid-template-columns:52% 48%; }
  #structure .p1 .pn { background:var(--pc); color:var(--pt); padding:5cqw 4cqw; display:flex; flex-direction:column; justify-content:space-between; }
  #structure .p1 .pn b { font:800 7cqw/1.08 'Jost',sans-serif; letter-spacing:-.01em; }
  #structure .p1 .pn small { font:700 3.6cqw/1.2 'Jost',sans-serif; letter-spacing:.14em; text-transform:uppercase; opacity:.75; }
  #structure .p1 .ph { height:100%; }
  /* PHOTO · p2 big number */
  #structure .p2 .md { background:#13283A; display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; padding:0 7cqw; }
  #structure .p2 .fill { opacity:.34; }
  #structure .p2 .n { position:relative; font:500 30cqw/.9 'Playfair',serif; color:var(--gold-lite); letter-spacing:-.02em; }
  #structure .p2 .l { position:relative; font:700 3.8cqw/1.35 'Jost',sans-serif; letter-spacing:.12em; text-transform:uppercase; color:#FBF7F0; margin-top:3cqw; }
  #structure .p2 .lk { position:relative; margin-top:5cqw; }
  #structure .p2 .n.sm { font-size:15cqw; letter-spacing:0; margin:1cqw 0 .5cqw; }
  #structure .p2 .l.pre { margin:0 0 2cqw; color:var(--gold-lite); }
  /* PHOTO · p3 checklist card */
  #structure .p3 .md { background:#F4EFE7; }
  #structure .p3 .ph { height:44cqw; }
  #structure .p3 .cd { position:absolute; left:5cqw; right:5cqw; top:38cqw; bottom:5cqw; background:#fff; border-radius:3cqw; padding:4cqw 5cqw; box-shadow:0 2cqw 6cqw rgba(19,40,58,.18); }
  #structure .p3 .cd b { display:block; font:500 6.4cqw/1.1 'Playfair',serif; color:#13283A; margin-bottom:2.4cqw; }
  #structure .p3 .cd p { display:flex; align-items:center; gap:2.4cqw; font:600 4.6cqw/1.2 'Jost',sans-serif; color:#16212B; margin-top:2.2cqw; }
  #structure .p3 .cd p::before { content:'\\2713'; flex:none; width:5.6cqw; height:5.6cqw; border-radius:50%; background:#2FA05A; color:#fff; font-size:3.6cqw; display:flex; align-items:center; justify-content:center; }
  #structure .p3 .cd .lk { position:absolute; left:auto; right:4cqw; bottom:3.4cqw; width:13cqw; height:7.6cqw; background-position:right bottom; }
  #structure .c3 .cd2 .qs { position:absolute; left:5cqw; right:5cqw; bottom:5cqw; font:700 3.2cqw/1.3 'Jost',sans-serif; letter-spacing:.14em; text-transform:uppercase; opacity:.7; }
  /* CAROUSEL · shared track */
  #structure .bx-ad .tr { flex:none; display:flex; gap:2cqw; padding-left:3.4cqw; height:84cqw; }
  #structure .bx-ad .cd2 { position:relative; flex:none; width:78cqw; border-radius:2.4cqw; overflow:hidden; border:.3cqw solid #E4E6EB; }
  #structure .bx-ad .cd2.pk { width:30cqw; }
  #structure .bx-ad .cdt { flex:none; display:flex; justify-content:center; gap:1.4cqw; height:7cqw; align-items:center; }
  #structure .bx-ad .cdt i { width:1.8cqw; height:1.8cqw; border-radius:50%; background:#CED0D4; } #structure .bx-ad .cdt i:first-child { background:#1877F2; }
  #structure .bx-ad .nn { position:absolute; z-index:2; right:2.6cqw; top:2.6cqw; font:700 3.4cqw/1 'Jost',sans-serif; color:#fff; background:rgba(0,0,0,.55); border-radius:3cqw; padding:1.2cqw 2cqw 1cqw; }
  /* c0 peek: photo card with headline */
  #structure .c0 .cd2 .ph { position:absolute; inset:0; }
  #structure .c0 .cd2 .ph::after { content:''; position:absolute; inset:0; background:linear-gradient(180deg,rgba(0,0,0,0) 45%,rgba(0,0,0,.75)); }
  #structure .c0 .t { position:absolute; z-index:2; left:4cqw; right:4cqw; bottom:4cqw; font:500 7.4cqw/1.08 'Playfair',serif; color:#fff; }
  /* c1 numbered steps */
  #structure .c1 .cd2 { background:var(--pc); color:var(--pt); padding:5cqw; display:flex; flex-direction:column; justify-content:space-between; }
  #structure .c1 .cd2.pk { background:#F4EFE7; color:#13283A; }
  #structure .c1 .cd2 u { text-decoration:none; font:500 17cqw/1 'Playfair',serif; opacity:.9; }
  #structure .c1 .cd2 b { font:800 7.4cqw/1.05 'Jost',sans-serif; }
  #structure .c1 .cd2 small { font:700 3.4cqw/1.2 'Jost',sans-serif; letter-spacing:.14em; text-transform:uppercase; opacity:.7; }
  /* c2 map */
  #structure .c2 .cd2:first-child { background:radial-gradient(90% 80% at 50% 30%, #2E6F7A, #123A44); }
  #structure .c2 svg { position:absolute; left:6cqw; right:6cqw; top:10cqw; width:66cqw; height:auto; }
  #structure .c2 svg path { fill:#E9DFC9; } #structure .c2 svg circle { fill:#F0201D; stroke:#fff; stroke-width:.35; }
  #structure .c2 .pin { position:absolute; left:4cqw; top:4cqw; font:800 3.4cqw/1 'Jost',sans-serif; letter-spacing:.12em; color:#fff; background:rgba(0,0,0,.35); border-radius:3cqw; padding:1.4cqw 2.2cqw 1.1cqw; }
  #structure .c2 .t { position:absolute; left:4cqw; right:4cqw; bottom:4cqw; font:500 6.6cqw/1.1 'Playfair',serif; color:#fff; }
  /* c3 question and answer */
  #structure .c3 .cd2 { background:var(--pc); color:var(--pt); padding:5cqw; }
  #structure .c3 .cd2.pk { background:#fff; color:#13283A; }
  #structure .c3 .cd2 u { display:block; text-decoration:none; font:italic 500 16cqw/1 'Playfair',serif; }
  #structure .c3 .cd2 b { display:block; font:700 7cqw/1.12 'Jost',sans-serif; margin-top:3cqw; }
  #structure .c3 .cd2.pk b { font-size:5cqw; }
  /* VIDEO · shared */
  #structure .bx-ad.vv { background:#000; color:#fff; }
  #structure .vv .hd b, #structure .vv .hd small { color:#fff; }
  #structure .vv .pb { position:absolute; z-index:3; left:4cqw; right:4cqw; bottom:4cqw; height:1cqw; border-radius:1cqw; background:rgba(255,255,255,.35); }
  #structure .vv .pb::after { content:''; display:block; width:36%; height:100%; border-radius:1cqw; background:var(--gold-lite); }
  #structure .vv .tm { position:absolute; z-index:3; right:4cqw; bottom:6.8cqw; font:600 3.6cqw/1 'Jost',sans-serif; color:#fff; }
  #structure .vv .snd { position:absolute; z-index:3; left:4cqw; bottom:6.8cqw; font:700 3.4cqw/1 'Jost',sans-serif; color:#fff; background:rgba(0,0,0,.5); border-radius:3cqw; padding:1.2cqw 2cqw 1cqw; }
  #structure .vv .fill::after { content:''; position:absolute; inset:0; background:linear-gradient(180deg,rgba(0,0,0,.5),rgba(0,0,0,0) 25%,rgba(0,0,0,0) 60%,rgba(0,0,0,.7)); }
  /* v0 kinetic captions */
  #structure .v0 .kw { position:absolute; z-index:3; left:6cqw; right:6cqw; top:50%; transform:translateY(-50%); display:flex; flex-wrap:wrap; justify-content:center; gap:1.2cqw; }
  #structure .v0 .kw span { font:800 6.4cqw/1.1 'Jost',sans-serif; text-transform:uppercase; color:#111; background:#fff; padding:.9cqw 1.8cqw .6cqw; border-radius:1.4cqw; }
  #structure .v0 .kw span.on { background:var(--gold-lite); }
  /* v1 chat */
  #structure .v1 .fill { filter:saturate(.8); }
  #structure .v1 .ch { position:absolute; z-index:3; left:5cqw; right:5cqw; top:26cqw; display:flex; flex-direction:column; gap:2.6cqw; }
  #structure .v1 .ch span { max-width:82%; font:500 4.8cqw/1.3 -apple-system,'Helvetica Neue',Arial,sans-serif; padding:2.6cqw 3.4cqw; border-radius:5cqw; }
  #structure .v1 .ch .cq { align-self:flex-start; background:#E9E9EB; color:#111; border-bottom-left-radius:1.2cqw; }
  #structure .v1 .ch .ca { align-self:flex-end; background:#0A84FF; color:#fff; border-bottom-right-radius:1.2cqw; }
  #structure .v1 .ch em { align-self:flex-end; font-style:normal; font:600 3.2cqw/1 'Jost',sans-serif; color:rgba(255,255,255,.8); }
  /* v2 boarding pass */
  #structure .v2 .bp { position:absolute; z-index:3; left:7cqw; right:7cqw; top:22cqw; background:#FCFAF6; color:#13283A; border-radius:3cqw; overflow:hidden; box-shadow:0 3cqw 8cqw rgba(0,0,0,.45); }
  #structure .v2 .bp .top { display:flex; justify-content:space-between; align-items:center; background:#13283A; padding:2.4cqw 3.4cqw; }
  #structure .v2 .bp .top small { font:700 3cqw/1 'Jost',sans-serif; letter-spacing:.16em; color:var(--gold-lite); }
  #structure .v2 .bp .lk { width:18cqw; height:5cqw; }
  #structure .v2 .bp .rt { display:flex; justify-content:space-between; align-items:center; padding:3cqw 4cqw 1cqw; }
  #structure .v2 .bp .rt b { font:800 11cqw/1 'Jost',sans-serif; letter-spacing:-.01em; }
  #structure .v2 .bp .rt i { font-style:normal; font-size:6cqw; color:var(--sand); }
  #structure .v2 .bp .rw { display:flex; justify-content:space-between; padding:0 4cqw 2.6cqw; font:600 2.9cqw/1.3 'Jost',sans-serif; letter-spacing:.1em; text-transform:uppercase; color:#8C8173; }
  #structure .v2 .bp .rw b { display:block; color:#13283A; font-size:3.6cqw; letter-spacing:.04em; }
  #structure .v2 .bp p { border-top:.5cqw dashed #C9BFAE; padding:2.6cqw 4cqw 3cqw; font:italic 500 5cqw/1.2 'Playfair',serif; }
  /* v3 stacked type */
  #structure .v3 { display:grid !important; grid-template-columns:55% 45%; }
  #structure .v3 .pn { position:relative; z-index:2; background:var(--pc); color:var(--pt); padding:15cqw 4cqw 12cqw; display:flex; flex-direction:column; justify-content:space-between; }
  #structure .v3 .pn b { font:400 13cqw/.9 'Bebas Neue',sans-serif; letter-spacing:.01em; }
  #structure .v3 .pn small { font:600 3.6cqw/1.3 'Jost',sans-serif; opacity:.85; }
  #structure .v3 .ph { position:relative; }
  #structure .v3 .hd { position:absolute; left:0; right:0; top:0; }
  #structure .v3 .pl { position:absolute; z-index:3; right:12cqw; top:50%; width:13cqw; height:13cqw; margin-top:-6.5cqw; border-radius:50%; background:rgba(255,255,255,.3); }
  #structure .v3 .pl::after { content:''; position:absolute; left:5cqw; top:3.5cqw; border-left:4.6cqw solid #fff; border-top:3cqw solid transparent; border-bottom:3cqw solid transparent; }
  /* STORY · shared (9:16, centred in the cell) */
  #structure .bx-ad.sv { left:15cqw; right:15cqw; background:#000; color:#fff; border-radius:4cqw; }
  #structure .sv .sg { position:absolute; z-index:4; left:3cqw; right:3cqw; top:3cqw; display:flex; gap:1cqw; }
  #structure .sv .sg i { flex:1; height:.8cqw; border-radius:1cqw; background:rgba(255,255,255,.4); } #structure .sv .sg i:first-child { background:#fff; }
  #structure .sv .hd { position:absolute; left:0; right:0; top:0; height:auto; padding:6.5cqw 3cqw 0; gap:1.6cqw; z-index:4; }
  #structure .sv .hd i { width:6cqw; height:6cqw; } #structure .sv .hd b { color:#fff; font-size:3.8cqw; } #structure .sv .hd small { display:none; }
  #structure .sv .fill::after { content:''; position:absolute; inset:0; background:linear-gradient(180deg,rgba(0,0,0,.45),rgba(0,0,0,0) 22%,rgba(0,0,0,0) 60%,rgba(0,0,0,.6)); }
  #structure .sv .up { position:absolute; z-index:4; left:50%; bottom:5cqw; transform:translateX(-50%); white-space:nowrap; font:700 3.6cqw/1 'Jost',sans-serif; color:#13283A; background:#fff; border-radius:5cqw; padding:2cqw 3.4cqw 1.8cqw; }
  /* s0 poll sticker */
  #structure .s0 .poll { position:absolute; z-index:4; left:5cqw; right:5cqw; top:34%; background:#fff; color:#111; border-radius:3.4cqw; padding:3cqw; text-align:center; box-shadow:0 2cqw 5cqw rgba(0,0,0,.35); }
  #structure .s0 .poll b { display:block; font:700 4.2cqw/1.2 -apple-system,'Helvetica Neue',Arial,sans-serif; margin-bottom:2cqw; }
  #structure .s0 .poll span { display:flex; justify-content:space-between; font:700 3.6cqw/1 -apple-system,'Helvetica Neue',Arial,sans-serif; border-radius:2cqw; padding:2cqw 2.4cqw; margin-top:1.4cqw; background:linear-gradient(90deg,rgba(226,184,114,.55) var(--v),#F0F0F0 var(--v)); }
  /* s1 question sticker */
  #structure .s1 .ask { position:absolute; z-index:4; left:5cqw; right:5cqw; top:32%; border-radius:3.4cqw; overflow:hidden; background:#fff; text-align:center; box-shadow:0 2cqw 5cqw rgba(0,0,0,.35); }
  #structure .s1 .ask b { display:block; padding:2.6cqw 2.4cqw; background:linear-gradient(90deg,#833AB4,#FD1D1D,#FCB045); color:#fff; font:700 3.8cqw/1.25 -apple-system,'Helvetica Neue',Arial,sans-serif; }
  #structure .s1 .ask span { display:block; margin:2.4cqw; border-radius:2cqw; background:#F0F0F0; color:#8E8E8E; font:500 3.4cqw/1 -apple-system,'Helvetica Neue',Arial,sans-serif; padding:2.4cqw; }
  /* s2 stacked type on colour */
  #structure .s2 { background:var(--pc) !important; color:var(--pt); }
  #structure .s2 .cir { position:absolute; left:50%; top:20cqw; width:40cqw; height:40cqw; margin-left:-20cqw; border-radius:50%; background:#13283A center/cover; border:1.2cqw solid rgba(255,255,255,.7); }
  #structure .s2 .t { position:absolute; left:5cqw; right:5cqw; top:66cqw; text-align:center; font:400 9.4cqw/.95 'Bebas Neue',sans-serif; }
  #structure .s2 .lk { position:absolute; left:50%; bottom:17cqw; margin-left:-12cqw; }
  #structure .s2 .hd b { color:inherit; }
  #structure .s2 .up { background:var(--pt); color:var(--pc); }
  /* s3 location sticker */
  #structure .s3 .loc { position:absolute; z-index:4; left:50%; top:30%; transform:translateX(-50%) rotate(-5deg); white-space:nowrap; font:800 4.6cqw/1 'Jost',sans-serif; letter-spacing:.06em; color:#A34BFF; background:#fff; border-radius:2cqw; padding:2cqw 3cqw 1.6cqw; box-shadow:0 1.5cqw 4cqw rgba(0,0,0,.3); }
  #structure .s3 .t { position:absolute; z-index:4; left:4cqw; right:4cqw; top:48%; text-align:center; }
  #structure .s3 .t span { font:700 4.6cqw/1.5 'Jost',sans-serif; color:#fff; background:rgba(0,0,0,.72); padding:.6cqw 1.6cqw; box-decoration-break:clone; -webkit-box-decoration-break:clone; }
  #structure .s3 .up::before { content:'\\1F517  '; }
  @keyframes bxIn { from { opacity:0; transform:translateY(6px) scale(.92); } }
  body.anim #structure .bx-ads.fresh .bx-cell { animation:bxIn .4s cubic-bezier(.2,.8,.2,1) calc(var(--k) * 28ms) both; }

  /* ── the multiplication: products × locations = ad sets × ads each = live ads, lit in three beats ── */
  #structure .bx-mx { margin-top:18px; background:var(--paper); border:1px solid var(--rule); border-radius:24px; padding:22px 26px 20px; box-shadow:var(--sh); }
  #structure .bx-eq { display:flex; align-items:stretch; justify-content:center; gap:10px; flex-wrap:wrap; }
  #structure .bx-t { display:flex; flex-direction:column; align-items:center; justify-content:flex-end; gap:6px; min-width:96px; padding:10px 12px 9px; border-radius:16px; transition:background .35s, box-shadow .35s; }
  #structure .bx-t .v { height:44px; display:flex; align-items:center; justify-content:center; }
  #structure .bx-t > b { font-family:'Playfair',serif; font-weight:500; font-size:44px; line-height:1; color:var(--ink); font-variant-numeric:tabular-nums; }
  #structure .bx-t small { font-size:9.5px; letter-spacing:.16em; text-transform:uppercase; font-weight:700; color:var(--taupe); text-align:center; line-height:1.3; }
  #structure .bx-t.hi { background:var(--teal); } #structure .bx-t.hi > b { color:var(--gold-lite); font-size:58px; } #structure .bx-t.hi small { color:rgba(251,247,240,.7); }
  #structure .bx-o { align-self:center; font-family:'Playfair',serif; font-size:28px; color:var(--stone); padding-top:40px; }
  #structure .bx-mx[data-s="1"] .bx-t.t1, #structure .bx-mx[data-s="2"] .bx-t.t2, #structure .bx-mx[data-s="2"] .bx-t.t3, #structure .bx-mx[data-s="3"] .bx-t.t4 { background:rgba(226,184,114,.22); box-shadow:inset 0 0 0 1.5px var(--sand); }
  #structure .bx-sw { display:flex; gap:4px; } #structure .bx-sw i { width:13px; height:22px; border-radius:3px; background:var(--c); box-shadow:inset 0 0 0 1px rgba(19,40,58,.18); }
  #structure .bx-sw.loc i { width:9px; height:9px; border-radius:50%; background:var(--sand); }
  #structure .bx-sw.loc { flex-wrap:wrap; width:60px; justify-content:center; }
  #structure .bx-gsets { display:grid; grid-template-columns:repeat(__L__,7px); gap:3px; } #structure .bx-gsets i { height:7px; border-radius:1.5px; background:var(--ink); opacity:.75; }
  #structure .bx-gads { display:grid; grid-template-columns:repeat(__F__,8px); gap:3px; } #structure .bx-gads i { height:8px; border-radius:2px; background:var(--gold-d); }
  #structure .bx-wall { display:grid; grid-template-columns:96px minmax(0,1fr); gap:5px 12px; margin-top:18px; }
  #structure .bx-wl { font-size:11px; font-weight:700; letter-spacing:.06em; color:var(--ink); align-self:center; white-space:nowrap; }
  #structure .bx-wr { display:grid; grid-template-columns:repeat(__P__,minmax(0,1fr)); gap:10px; }
  #structure .bx-blk { display:grid; grid-template-columns:repeat(__ADS__,minmax(0,1fr)); gap:2px; padding:3px; border-radius:6px; box-shadow:inset 0 0 0 1.5px rgba(181,122,46,0); cursor:pointer; transition:box-shadow .35s, background .35s; }
  #structure .bx-blk:hover { background:rgba(226,184,114,.18); }
  #structure .bx-blk i { height:13px; border-radius:2.5px; background:var(--c); box-shadow:inset 0 0 0 1px rgba(19,40,58,.14); transition:opacity .3s, transform .3s; }
  #structure .bx-mx[data-s="1"] .bx-blk.r0, #structure .bx-mx[data-s="2"] .bx-blk { box-shadow:inset 0 0 0 1.5px var(--sand); }
  #structure .bx-mx[data-s="0"] .bx-blk i, #structure .bx-mx[data-s="1"] .bx-blk i, #structure .bx-mx[data-s="2"] .bx-blk i { opacity:.12; transform:scale(.6); }
  #structure .bx-mx[data-s="3"] .bx-blk i { transition-delay:calc(var(--i) * 2.2ms); }
  #structure .bx-wh { display:contents; }
  #structure .bx-wh span { font-size:9.5px; letter-spacing:.14em; text-transform:uppercase; font-weight:700; color:var(--taupe); display:flex; align-items:center; gap:6px; }
  #structure .bx-wh span i { width:10px; height:10px; border-radius:3px; background:var(--c); }
  #structure .bx-wf { display:flex; justify-content:space-between; gap:10px; flex-wrap:wrap; margin-top:12px; padding-top:10px; border-top:1px solid var(--rule); font-size:11.5px; color:var(--taupe); }
  #structure .bx-wf b { color:var(--ink); font-weight:600; }

  /* ── the story strip and the tour control ── */
  #structure .bx-mx { margin-top:0; }
  #structure .bx-con { margin-top:18px; }
  #structure .bx-eq { flex-wrap:nowrap; align-items:stretch; }
  #structure .bx-t { flex:1 1 0; min-width:0; justify-content:flex-start; background:var(--ivory); padding:14px 12px 14px; }
  #structure .bx-t p { font-size:12px; line-height:1.45; color:var(--soft); text-align:center; margin-top:4px; }
  #structure .bx-t p b { color:var(--ink); font-weight:600; }
  #structure .bx-t.hi { justify-content:center; flex:.8 1 0; }
  #structure .bx-t.hi p { color:rgba(251,247,240,.75); font-size:13px; } #structure .bx-t.hi p b { color:var(--gold-lite); font-family:'Playfair',serif; font-size:22px; font-weight:500; }
  #structure .bx-o { padding-top:58px; }
  #structure .bx-replay { font:inherit; font-size:11.5px; font-weight:600; color:var(--gold-d); background:none; border:0; cursor:pointer; padding:0; }
  #structure .bx-bar { display:flex; justify-content:space-between; align-items:center; gap:12px; margin-bottom:12px; }
  #structure .bx-tour { font:inherit; cursor:pointer; display:flex; align-items:center; gap:9px; color:#FBF7F0; background:rgba(251,247,240,.06); border:1px solid rgba(251,247,240,.14); border-radius:18px; padding:6px 12px 6px 8px; font-size:11.5px; font-weight:600; }
  #structure .bx-tour > i { width:20px; height:20px; border-radius:50%; background:var(--gold-lite); position:relative; }
  #structure .bx-tour > i::after { content:''; position:absolute; left:7.5px; top:5.5px; border-left:7px solid #13283A; border-top:4.5px solid transparent; border-bottom:4.5px solid transparent; }
  #structure .bx-tour[aria-pressed="true"] > i::after { left:6px; top:6px; width:2.5px; height:8px; border:0; background:#13283A; box-shadow:5px 0 0 #13283A; }
  #structure .bx-tour u { width:54px; height:3px; border-radius:2px; background:rgba(251,247,240,.15); overflow:hidden; text-decoration:none; }
  #structure .bx-tour u em { display:block; height:100%; width:0; background:var(--gold-lite); }
  #structure .bx-tour.run u em { animation:bxProg var(--t,3.8s) linear forwards; }
  @keyframes bxProg { to { width:100%; } }
  @media screen and (max-width:1080px){
    #structure .bx-g { grid-template-columns:minmax(0,1fr); }
    #structure .bx-map { max-width:600px; margin:0 auto; width:100%; }
    #structure .bx-tabs { grid-template-columns:repeat(2,minmax(0,1fr)); }
    #structure .bx-eq { flex-wrap:wrap; } #structure .bx-t { flex:1 1 40%; } #structure .bx-o { display:none; }
  }
  @media screen and (max-width:640px){
    #structure .bx-in { padding:16px 12px 18px; }
    #structure .bx-mx { padding:16px 12px; }
    #structure .bx-tab { padding:8px 10px; } #structure .bx-tab b { font-size:12.5px; } #structure .bx-tab em { display:none; }
    #structure .bx-dh h3 { font-size:24px; } #structure .bx-n b { font-size:34px; }
    #structure .bx-ads { grid-template-columns:repeat(__F__,minmax(0,1fr)); gap:6px; }
    #structure .bx-ads .bx-fh.x { display:none; } #structure .bx-fh { font-size:7.5px; letter-spacing:.06em; }
    #structure .bx-an { grid-column:1 / -1; flex-direction:row; gap:8px; align-items:baseline; margin-top:4px; }
    #structure .bx-cell:hover .bx-ad { transform:none; } #structure .bx-cell.z .bx-ad { transform:scale(1.9); }
    #structure .bx-eq { gap:4px; } #structure .bx-o { padding-top:30px; font-size:20px; }
    #structure .bx-t { min-width:0; padding:8px 6px; } #structure .bx-t > b { font-size:32px; } #structure .bx-t.hi > b { font-size:40px; } #structure .bx-t small { font-size:8px; letter-spacing:.08em; }
    #structure .bx-wall { grid-template-columns:minmax(0,1fr); gap:3px; } #structure .bx-wl { margin-top:6px; }
    #structure .bx-wr { gap:4px; } #structure .bx-blk { gap:1px; padding:2px; } #structure .bx-blk i { height:9px; border-radius:1.5px; }
    #structure .bx-wh .bx-wl { display:none; } #structure .bx-wh span { font-size:7.5px; letter-spacing:.04em; }
    #structure .bx-t { flex:1 1 100%; } #structure .bx-bar { flex-wrap:wrap; }
  }
  @media print {
    section#structure { height:auto !important; min-height:0 !important; display:block !important; overflow:visible !important; padding:9mm 13mm 4mm !important;
      break-inside:auto !important; page-break-inside:auto !important; }
    section#structure > .wrap { zoom:.8 !important; }
    #structure .head { margin-bottom:14px; }
    #structure .bx-g { grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr) !important; }
    #structure .bx-tabs { grid-template-columns:repeat(__P__,minmax(0,1fr)) !important; }
    #structure .bx-con { break-before:page; page-break-before:always; break-inside:avoid; page-break-inside:avoid; margin-top:0; }
    #structure .bx-eq { flex-wrap:nowrap !important; } #structure .bx-o { display:block !important; }
    #structure .bx-bar { display:none !important; }
    #structure .bx-cell .bx-ad { transform:none !important; }
    #structure .bx-mx .bx-blk i { opacity:1 !important; transform:none !important; }
  }
</style>'''

def lit_css():
    """The rules that light the selected location: one selector per location that has a map shape, plus retargeting
    (which lights every state, every flight line and its own pill). Three selectors to a line."""
    def rule(items, body):
        return (',\n  '.join(', '.join(items[i:i + 3]) for i in range(0, len(items), 3)) + ' { ' + body + ' }') if items else ''
    con = lambda r: f'#structure .bx-con[data-r="{r}"]'
    own = lambda cls: [f'{con(r)} .{cls}[data-r="{r}"]' for r in MAPPED]
    rt = lambda tail: [f'{con(RT)} {tail}'] if RT is not None else []
    out = [f'{con(SR["ACT"])} .bx-sl.out'] if 'ACT' in SR else []      # the ACT label sits outside its state
    rules = [rule(own('bx-st') + rt('.bx-st'), 'fill:rgba(226,184,114,.9); stroke:#FBF7F0;'),
             rule(rt('.bx-st'), 'fill:rgba(226,184,114,.34); stroke:#E2B872; stroke-dasharray:5 4;'),
             rule(own('bx-sl'), 'fill:#13283A;'),
             rule(out, 'fill:#E2B872;'),
             rule(own('bx-arc') + rt('.bx-arc'), 'stroke:#E2B872; stroke-width:2; stroke-dasharray:6 7;'),
             rule(own('bx-pin'), 'fill:#FBF7F0; stroke:#13283A;'),
             rule(rt('.bx-rt rect'), 'fill:#E2B872; stroke:#E2B872; stroke-dasharray:none;'),
             ' '.join(filter(None, (rule(rt('.bx-rt-o'), 'fill:#13283A;'), rule(rt('.bx-rt-a'), 'fill:#13283A;'), rule(rt('.bx-rt-b'), 'fill:rgba(19,40,58,.7);'))))]
    return '\n  '.join(r for r in rules if r)
CSS_B = (CSS_B.replace('__LIT__', lit_css())
              .replace('__RTANIM__', '' if RT is None else f'body.anim #structure .bx-con[data-r="{RT}"] .bx-st {{ animation:bxPulse 2.4s ease-in-out infinite; }}')
              .replace('__ADS__', str(ADS)).replace('__P__', str(NP)).replace('__L__', str(NL)).replace('__F__', str(NF)))

def listing(xs): return xs[0] if len(xs) == 1 else ' and '.join(xs) if len(xs) == 2 else ', '.join(xs[:-1]) + ', and ' + xs[-1]

WCOL = dict(COL)   # the wall and the console use the same product colours (navy gets a light rim on the dark console)
def buyer():
    tabs = ''.join(f'<button type="button" class="bx-tab{" on" if i == 0 else ""}" data-p="{i}" style="--c:{COL[p["key"]]}" aria-pressed="{"true" if i == 0 else "false"}">'
                   f'<i></i><b>{p["name"]}</b><small>Always on</small><em>{ADS}</em></button>'
                   for i, p in enumerate(PRODUCTS))
    chips = ''.join(f'<button type="button" class="bx-chip{" on" if r == 0 else ""}" data-r="{r}">{short}{"<small>warm</small>" if pop == "Warm" else ""}</button>'
                    for r, (k, short, full, pop, metro, states) in enumerate(LOCS))
    fh = '<div class="bx-fh x"></div>' + ''.join(f'<div class="bx-fh">{f}</div>' for f, _ in FORMATS)
    # the multiplication wall — a row per location × a block per product × a square per ad
    wall, n = '', 0
    wall += '<div class="bx-wh"><span class="bx-wl"></span><div class="bx-wr">' + ''.join(f'<span style="--c:{WCOL[p["key"]]}"><i></i>{p["name"]}</span>' for p in PRODUCTS) + '</div></div>'
    for r, (k, short, full, pop, metro, states) in enumerate(LOCS):
        blks = ''
        for g, p in enumerate(PRODUCTS):
            dots = ''.join(f'<i style="--i:{n + t}"></i>' for t in range(ADS)); n += ADS
            blks += f'<div class="bx-blk r{r}" data-r="{r}" data-p="{g}" style="--c:{WCOL[p["key"]]}" title="{short} &middot; {p["name"]} &middot; {ADS} {pl(ADS, "ad")}">{dots}</div>'
        wall += f'<div class="bx-wl">{short}</div><div class="bx-wr">{blks}</div>'
    assert n == TOTAL
    data = {'locs': [[k, full, metro, pop, short] for (k, short, full, pop, metro, states) in LOCS],
            'prods': [[p['key'], p['name'], p['tag'], p['sells'], p['angles'], IMGS[p['key']], HOOKS[p['key']], CTA[p['key']], COL[p['key']]] for p in PRODUCTS],
            'T': T, 'formats': [f for f, _ in FORMATS], 'ang': ANG, 'panel': PANEL, 'orig': ORIG, 'site': SITE, 'bali': AUS['BALI'],
            'fam': FAM, 'n': {'P': NP, 'L': NL, 'ANG': NANG, 'F': NF, 'ADS': ADS, 'SETS': SETS, 'TOTAL': TOTAL, 'rt': RT}}
    swP = ''.join(f'<i style="--c:{WCOL[p["key"]]}"></i>' for p in PRODUCTS)
    swL = '<i></i>' * NL
    gS = '<i></i>' * SETS
    gA = '<i></i>' * ADS
    # the maths band's words, from the counts
    allOn = 'Always on' if NP == 1 else 'Both always on' if NP == 2 else f'All {words(NP)} always on'
    allP = 'the product always on' if NP == 1 else 'both products always on' if NP == 2 else f'all {words(NP)} products always on'
    geo = NL - (RT is not None)                 # locations other than retargeting
    warm = ' &mdash; plus retargeting for people already warm' if RT is not None else ''
    t2 = (f'<b>{cap(words(geo))} {pl(geo, *BAND["places"])}</b>, {"each " if geo > 1 else ""}targeted on its own{warm}.' if geo
          else '<b>Retargeting</b> &mdash; people already warm.')
    names = listing([re.sub(r'^The ', 'the ', p['name']) for p in PRODUCTS])
    return f'''<section class="slide" id="structure">
{CSS_B}
  <div class="wrap">
    <div class="head rv">
      <div class="k">One campaign &middot; {TOTAL} live {pl(TOTAL, "ad")}</div>
      <h2>The buyer <em>campaign.</em></h2>
    </div>

    <div class="bx-mx rv" data-s="4">
      <div class="bx-eq">
        <div class="bx-t t1"><div class="v"><div class="bx-sw">{swP}</div></div><b>{NP}</b><small>{pl(NP, "product")}</small><p><b>{allOn}</b> &mdash; {BAND["products"]}.</p></div><div class="bx-o">&times;</div>
        <div class="bx-t t2"><div class="v"><div class="bx-sw loc">{swL}</div></div><b>{NL}</b><small>{pl(NL, "location")}</small><p>{t2}</p></div><div class="bx-o">=</div>
        <div class="bx-t t3"><div class="v"><div class="bx-gsets">{gS}</div></div><b>{SETS}</b><small>{pl(SETS, "ad set")}</small><p><b>Each its own audience</b> &mdash; so we never bid against ourselves.</p></div><div class="bx-o">&times;</div>
        <div class="bx-t t4"><div class="v"><div class="bx-gads">{gA}</div></div><b>{ADS}</b><small>{pl(ADS, "ad")} each</small><p><b>{NANG} {pl(NANG, "angle")} &times; {NF} {pl(NF, "format")}.</b> Meta tests all {words(ADS)} and backs the winner.</p></div><div class="bx-o">=</div>
        <div class="bx-t hi"><b class="bx-total">{TOTAL}</b><small>live {pl(TOTAL, "ad")}</small><p><b>0</b> for you to make</p></div>
      </div>
      <div class="bx-wall">{wall}</div>
      <div class="bx-wf"><span>Every square is one ad &middot; <b>{allP}</b> &middot; new designs every month</span><span><button type="button" class="bx-replay">&#8635; Replay</button> &middot; Tap a block to open that ad set</span></div>
    </div>

    <div class="bx-con rv" data-r="0" data-p="0">
      <div class="bx-in">
        <div class="bx-bar"><span class="bx-k">Open any ad set &mdash; tap a product, then a state</span><button type="button" class="bx-tour" aria-pressed="true"><i></i><span>Auto-tour</span><u><em></em></u></button></div>
        <div class="bx-tabs" role="group" aria-label="The {words(NP)} {pl(NP, "product")}">{tabs}</div>
        <div class="bx-g">
          <div class="bx-map">
            {aus_svg()}
            <div class="bx-chips" role="group" aria-label="The {words(NL)} {pl(NL, "location")}">{chips}</div>
            <div class="bx-who"><div class="bx-k">Who this ad set finds</div><ul></ul><p></p></div>
          </div>
          <div class="bx-det">
            <div class="bx-dh"><div><div class="bx-k bx-lk"></div><h3></h3><div class="bx-m"></div></div><div class="bx-n"><b>{NP * ADS}</b><small>{pl(NP * ADS, "ad")} in this location</small></div></div>
            <div class="bx-ads">{fh}<div class="bx-body" style="display:contents"></div></div>
            <div class="bx-foot"><span class="bx-as"></span><span class="bx-fx">Hover or tap any ad to see it full size</span></div>
          </div>
        </div>
      </div>
      <script type="application/json" class="bx-data">{json.dumps(data)}</script>
    </div>
    <div class="note"><b>Numbers first, then the console</b><b>&ldquo;{cap(words(NP))} {pl(NP, "product")} &mdash; {names} &mdash; all always on. {cap(words(NL))} {pl(NL, "location")}, and every state gets its own audience, so we never bid against ourselves. {cap(words(ADS))} {pl(ADS, "ad")} in each, so Meta finds the winner. That&rsquo;s {TOTAL} live {pl(TOTAL, "ad")} &mdash; and your team makes none of them.&rdquo;</b> Then the console: it tours itself; tap <b>{LOCS[0][1]}</b> to take over &mdash; <b>&ldquo;who we look for in {LOCS[0][2]}, and the {words(ADS)} {pl(ADS, "ad")} they see.&rdquo;</b> Hover one to show it full size.</div>
  </div>
</section>
'''


# one campaign: write the buyer campaign slide and nothing else
open(os.path.join(SRC, 's14_structure.html'), 'w', encoding='utf8').write(buyer())
print(f'built: s14_structure.html (the buyer campaign: {NP} products × {NL} locations = {SETS} ad sets × {ADS} ads = {TOTAL} live ads)')
