# Generates the journey slide (#how) — "The Verified Buyer Funnel" — into src/s13_how.html:
#   1. the six-moment strip  (.hz)  — six live mini phones on a flowing timeline
#   2. stage one, live (.xj.one) — the buyer's phone ──wire──▶ her CRM record ──wire──▶ your sales team's phone.
#      The instant form is played tap by tap by a scripted thumb (Dir below → data-fx → journey.js puppet),
#      one plain-English reason caption per step. Then the call (pack + private call booked), reminders,
#      the private video call, her choice, the outcome — tracked back to the ad.
#   3. the next-stage note, then stage two, live (.xj.two) — the client's landing page (a stills film stands in
#      for the film we shoot), the same six questions, she books her own private call
# Motion + state: src/js/journey.js.  Styles: build/how.css.
#
# To adapt the film for a new client, edit only the CONFIG block below (brand, products, demo customer, sales side,
# pipeline, the six questions, the story's clock) — no client name, place or product is written anywhere else. Then:
#   1. python3 build/gen_how.py (it prints each chapter's length in ms), then python3 build/build.py.
#   2. Reread the copy that is written as sentences (it uses the CONFIG names, but its argument is the worked example's):
#        the strip's six lines ...... HZ_STEPS          form-step reasons ...... R_OPEN … R_SEND, and QS's reasons
#        captions, per chapter ...... CC1[k] / CC2[k]   ([ms into chapter k, html]; the form chapters' come from Dir)
#        events, per chapter ........ ev1[k] / ev2[k]   (cm camera · pk wire packet + label · pl pipeline · bz buzz)
#        chapter titles ............. one_caps / two_caps, and the timeline's step names ST1 / ST2
#        activity log ............... one_acts / two_acts (her CRM record); team-phone alerts ... g_one / g_two
#        presenter note ............. the "note" paragraph at the very end
#   3. Timing: the form chapters are timed by the director (Dir: wait/tap/ty — typing length moves everything after it);
#      the later chapters by AFTER (ms each). Keep every caption/event time inside its chapter's length.
#   4. Watch it play (Play, scrub, click a chapter, let it finish) and check the static ?noanim frame (the PDF).
import os, json, random
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')

def up1(s): return s[:1].upper() + s[1:]                       # 'private call' → 'Private call'
def lo1(s): return s[:1].lower() + s[1:]                       # 'Around A$250k' → 'around A$250k'
def hm(t): return t[:-2] if t[-2:] in ('am', 'pm') else t      # '7:42pm' → '7:42' (status bars, lock screens)


# ═══════════════════════════════════════════════════════════════════════════
# CONFIG — everything client-specific, defined once. Edit only this block.
#   Values are HTML: write apostrophes as &rsquo; (captions travel in single-quoted attributes), keep &middot; etc.
#   BUYER, MOB, EMAIL and the two codes are typed letter by letter by the thumb: plain text only.
#   Worked example: Kestrel Bay Resort (suites in Bali, by Kestrel Developments, run by Tidewater); buyer Sarah Mitchell.
# ═══════════════════════════════════════════════════════════════════════════

# ── 1 · the client and the brand ──
BRAND       = 'Kestrel Bay Resort'          # the project as buyers know it: on her texts, calls, mail, the form, the page
BRAND_SHORT = 'Kestrel Bay'                 # short form in headlines and copy ("Your Kestrel Bay pack")
PAGE        = BRAND                         # the Facebook/Instagram page the ad runs from (the ad, the instant form)
DEV         = 'Kestrel Developments'        # the developer in full (consent line, reservation email, page footer)
DEV_SHORT   = 'Kestrel'                     # the developer, short ("Reserved with Kestrel")
DEV_YEARS   = '18 years'                    # their track record (landing page trust strip)
PARTNER     = 'Tidewater'                   # the operator / brand partner (question six, the film, the trust strip)
PLACE       = 'Bali'                        # where the project is
SITE        = 'resort'                      # what the project is, as a common noun ("the resort film", "The resort, Bali")
BUYERS      = 'Australians'                 # who the ads reach ("… in front of Australians buying in Bali")
DOMAIN      = 'kestrelbay.example'          # the landing page's address (stage two); also her lead source in the CRM
AV          = 'assets/brand-avatar.png'     # round avatar: the ad page, texts, calls, mail
LOGO_LIGHT  = 'assets/brand-logo-light.png' # the logo laid on photos (the ad)
LOGO_DARK   = 'assets/brand-logo-dark.png'  # the landing page footer
WORDMARK    = 'assets/brand-wordmark-light.png'   # the landing page nav bar
IMG_HERO    = 'assets/ph-hero-pool.jpg'     # hero photo: the ad, the instant form, the pack
IMG_P1      = 'assets/ph-suite-a.jpg'       # product one, inside (the pack, the private call, the card she's sent)
IMG_P1B     = 'assets/ph-suite-a2.jpg'      # product one, a second photo (the reservation email)
IMG_SITE    = 'assets/ph-resort-tall.jpg'   # the whole property (the private call)
IMG_CLUB    = 'assets/ph-member-card.jpg'   # the club / perk (the private call)
IMG_EVENT   = 'assets/ph-event.jpg'         # people at an event (the pack)
FILM_STILLS = ['assets/ph-pool-2.jpg', IMG_HERO, IMG_P1, IMG_EVENT, 'assets/ph-venue-2.jpg']   # the stand-in film's five stills, in order

# ── 2 · the products ──
UNIT, UNITS, A_UNIT = 'suite', 'suites', 'a suite'   # what is for sale, as a common noun (A_UNIT carries the article: "an apartment")
P1           = 'Garden Suite'               # product one — the one she chooses
P1_SHORT     = 'Garden'                     # its one-word name (the team's call checklist)
P1_FROM      = 'US$165k'                    # its price as the ad shows it …
P1_FROM_AUD  = 'A$240k'                     # … and converted
P1_PRICE     = 'US$165,000'                 # the same, written in full (the ad's text, the card she's sent)
P1_PRICE_AUD = 'A$240,000'
P1_SPEC      = ('34 m&sup2;', '1 bedroom')  # size, bedrooms
P2           = 'Ocean Suite'                # product two (the form's first question)
P2_FROM      = 'US$260k'
CUR_PAIR     = 'US$ and A$'                 # "prices in US$ and A$"
CLUB         = 'Owners&rsquo; Club'         # the perk that comes with buying (the pack, the call, the film)
CLUB_SHORT   = 'club'
AD_HEAD      = (f'Own {A_UNIT}', f'at {BRAND_SHORT}.')                  # the ad's headline, two lines
AD_NAME      = f'Own {A_UNIT} at {BRAND_SHORT}'                         # the ad by name, when a sale is tracked back to it
AD_TEXT      = f'Own {A_UNIT} at {BRAND}, {PLACE}. From {P1_PRICE} (about {P1_PRICE_AUD}).'   # the ad's primary text
AD_FEATURES  = [PLACE, 'Lagoon pool', CLUB.capitalize()]               # the feature strip on the ad's photo

# ── 3 · the words for the steps ──
MEETING      = 'private call'               # the meeting she books
MEETING_LONG = 'private video call'
MEETING_LEN  = '20-minute video call'
OUTCOME      = 'Reserved'                   # the last pipeline stage and the film's last word
OUTCOME_VERB = 'reserve'                    # "she reserves", "How do I reserve it?"
OUTCOME_NOUN = 'reservation'

# ── 4 · the six questions (keep identical to source/facts.md), and why each is asked ──
#     (question, options, her pick, caption label, the reason for the client's sales team, label on the landing page)
QS = [(f'Which {UNIT}?', [f'{P1} &middot; from {P1_FROM}', f'{P2} &middot; {P2_FROM}', 'Not sure yet'], 0,
       up1(UNIT), f'So you know which {UNIT} to open with.', f'Which {UNIT}?'),
      ('What&rsquo;s it for?', ['Rental income', 'Holidays', 'A bit of both'], 2,
       'What it&rsquo;s for', 'So you know whether to talk income or holidays.', 'What&rsquo;s it for?'),
      ('Budget (AUD)?', ['Around A$250k', 'A$250k &ndash; A$400k', 'A$400k+'], 0,
       'Budget', 'So you know which price to lead with.', 'Budget (AUD)?'),
      ('When are you looking to buy?', ['In the next 3 months', '3&ndash;6 months', 'Just researching'], 0,
       'Timing', 'So the ready-now buyers get your first call.', 'When are you looking to buy?'),
      ('How would you fund it?', ['Savings or equity, ready', 'Arranging finance', 'Selling something first'], 0,
       'Funding', 'So you know if the money is ready.', 'How would you fund it?'),
      (f'Have you stayed at a {PARTNER} venue?', ['Many times', 'Once or twice', 'Not yet'], 0,
       f'Stayed at {PARTNER}', f'So you know how much of {PARTNER} to explain.', f'Have you stayed at a {PARTNER} venue?')]
CONSENT = f'I agree to {DEV} contacting me by phone, text and email about {BRAND}.'

# ── 5 · the demo customer (fictional) ──
BUYER, BUYER_FIRST, BUYER_INIT = 'Sarah Mitchell', 'Sarah', 'SM'
BUYER_SHORT  = f'{BUYER_FIRST} {BUYER_INIT[-1]}.'                       # "Sarah M." (the strip's alert)
BUYER_CITY, BUYER_REGION = 'Perth', 'WA'
MOB, MOB_M   = '0491 570 156', '0491 &bull;&bull;&bull; 156'      # ACMA's reserved fictional mobile range; masked
EMAIL, EMAIL_M = 'sarah.mitchell@example.com', 's&bull;&bull;&bull;&bull;&bull;&bull;@example.com'
CODE_MOB, CODE_EMAIL = '482917', '305628'                           # her two verification codes
# her answers = her picks in QS; the ones the story repeats:
ANS_USE, ANS_BUDGET, ANS_WHEN, ANS_KNOWS = (QS[i][1][QS[i][2]] for i in (1, 2, 3, 5))
ANS_WHEN_SHORT = 'Next 3 months'
HZ_Q  = [(f'Which {UNIT}?', P1), ('For', ANS_USE), ('Budget', ANS_BUDGET), ('When', ANS_WHEN_SHORT), ('Funding', 'Ready'),
         (f'Stayed at {PARTNER}?', ANS_KNOWS)]                                     # as the strip shows them
BRIEF = [(up1(UNIT), P1), ('For', ANS_USE), ('Budget', ANS_BUDGET),
         ('Timeframe', ANS_WHEN), ('Funding', 'Savings or equity &middot; ready'), (f'Stayed at {PARTNER}', ANS_KNOWS)]   # as her CRM record shows them
SCORE        = 88                                                               # her lead score
SCORE_STEPS  = [7, 15, 21, 53, 78, SCORE]   # the running total as each answer lands (ends on her score)

# ── 6 · the sales side ──
TEAM       = 'sales team'                   # who calls her ("your sales team", "our sales team")
CRM        = 'CRM'                          # the app the team works in (her record, the alerts, the booking sheet)
TEAM_PLACE = PLACE                          # where the team's phone is
TZ         = f'{TEAM_PLACE} time'           # the clock every booking is made in
TZ_SAME    = f'{TZ}, same as {BUYER_CITY}'  # her texts and the booking page ("Bali time, same as Perth")
TZ_NOTE    = f'{TZ} is {BUYER_CITY} time.'  # the team phone's tooltip

# ── 7 · the pipeline — the CRM's stages, left to right (her card walks along them) ──
STAGE_CHOSEN = f'{up1(UNIT)} chosen'
COLS = ['Verified', 'Called', 'Booked', up1(MEETING), STAGE_CHOSEN, OUTCOME]

# ── 8 · the story's clock — one demo week; both phones show the same clock (TZ) ──
DAY  = ['Tuesday', 'Wednesday', 'Thursday', 'Friday']   # she enquires · the private call · she chooses · the outcome
DY   = ['Tue', 'Wed', 'Thu', 'Fri']
DATE = [17, 18, 19, 20]
MONTH, MON, YEAR = 'November', 'Nov', 2026
CAL_FROM, CAL_TO = 9, 29                    # the booking calendar's first and last dates (CAL_FROM is a Monday)
TUE, WED, THU, FRI = (f'{DAY[i]} {DATE[i]} {MONTH}' for i in range(4))
CALL_TIME  = '10:30am'                      # the private call, on day two
SLOTS      = ['9:00am', CALL_TIME, '1:00pm', '3:30pm', '5:00pm', '6:30pm']   # the times her calendar offers
CALL_SLOT  = SLOTS.index(CALL_TIME)         # (not first or last: the booking sheets show it between its neighbours)
CALL_SHORT = f'{DY[1]} {DATE[1]} {MON}, {CALL_TIME}'
REBOOK_SLOTS = [f'{DY[1]} 3:00pm', f'{DY[2]} {CALL_TIME}', f'{DY[3]} 9:00am']   # if she misses it (she picks the middle one)
# the clock in each chapter: both phones' status bars, the team's lock screens, the chapter titles
CLOCK1 = ['7:42pm', '7:42pm', '7:43pm', '7:44pm', '7:45pm', '7:45pm', '7:47pm', '9:30am', CALL_TIME, '9:12am', '11:05am']
CDAY1  = [0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 3]  # which day each stage-one chapter falls on
CLOCK2 = ['7:42pm', '7:43pm', '7:45pm', '7:47pm', '7:47pm']   # stage two, all on day one
T_PACK, T_CONFIRM, T_REMIND, T_SENT2 = '7:48pm', '7:53pm', '8:00am', '7:46pm'   # pack sent · booking text · morning reminder · stage-two enquiry
STRIP_CLOCK = ['7:42', '7:42', '7:43', '7:45', '7:48', DY[3]]   # the strip's six mini phones
# ═══════════════════════════════ END OF CONFIG ═════════════════════════════

AVI = f'<span class="fd-av"><img src="{AV}" alt=""></span>'
PHONE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1L6.6 10.8z"/></svg>'
LOCK_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>'
MUTE_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9.5h3.5L12 5.5v13l-4.5-4H4z"/><path d="M16 9.5l5 5M21 9.5l-5 5"/></svg>'
CAM_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="6.5" width="12.5" height="11" rx="2.5"/><path d="M15.5 10.5l5-3v9l-5-3z"/></svg>'
MIC_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0 0 13 0M12 17.5V21"/></svg>'
CHK = '&#10003;'


def tap(d, at=None):
    """a fingertip tap — a ripple centred on its parent element, at delay d"""
    return f'<i class="tp"{f" data-at=\"{at}\"" if at else ""} style="--d:{d}"></i>'


# ═══════════════════════════════════════════════════════════════════════════
# 1 · THE STRIP — six moments, six live mini phones
# ═══════════════════════════════════════════════════════════════════════════
def sb(t, light=False):
    return f'<div class="hz-sb{" lt" if light else ""}"><b>{t}</b><span><i></i><i></i></span></div>'

HZ_AD = f'''<div class="hz-scr hz-ad">{sb(STRIP_CLOCK[0])}
            <div class="ha-feed">
              <div class="ha-sk"><i></i><i></i></div>
              <div class="ha-post">
                <div class="ha-h"><span class="ha-av"><img src="{AV}" alt=""></span><b>{PAGE}</b><em>Sponsored</em></div>
                <div class="ha-img"><img src="{IMG_HERO}" alt=""><img class="ha-lg" src="{LOGO_LIGHT}" alt=""><span>{AD_HEAD[0]}<br><em>{AD_HEAD[1]}</em></span><i class="ha-pr">From {P1_FROM}</i></div>
                <div class="ha-cta"><span>See the {UNITS}</span><b>Sign up</b></div>
                <div class="ha-ic"><i></i><i></i><i></i></div>
              </div>
            </div>
            <i class="hz-tp" style="left:78%;top:218px;--d:1.55s"></i>
          </div>'''
HZ_FORM = f'''<div class="hz-scr hz-fm">{sb(STRIP_CLOCK[1])}
            <div class="hf-h"><span class="ha-av"><img src="{AV}" alt=""></span><b>{BRAND_SHORT} enquiry</b></div>
            <div class="hf-bar"><i></i></div>
            {''.join(f'<div class="hf-q"><small>{q}</small><b style="--d:{.25 + i * .34:.2f}s">{a}</b></div>' for i, (q, a) in enumerate(HZ_Q))}
            <div class="hf-go" style="--d:2.4s">Next</div>
          </div>'''
HZ_CODE = f'''<div class="hz-scr hz-cd">{sb(STRIP_CLOCK[2])}
            <div class="hc-ban" style="--d:.2s"><i></i><div><b>Messages</b><span>{CODE_MOB} is your code</span></div></div>
            <div class="hc-t">Confirm it&rsquo;s you</div>
            <div class="hc-l">Mobile</div>
            <div class="hc-c">{''.join(f'<i style="--d:{.55 + k * .08:.2f}s">{c}</i>' for k, c in enumerate(CODE_MOB))}</div>
            <div class="hc-ok" style="--d:1.1s">{CHK} Mobile</div>
            <div class="hc-l">Email</div>
            <div class="hc-c">{''.join(f'<i style="--d:{1.35 + k * .08:.2f}s">{c}</i>' for k, c in enumerate(CODE_EMAIL))}</div>
            <div class="hc-ok" style="--d:1.9s">{CHK} Email</div>
            <div class="hc-seal" style="--d:2.25s"><b>Verified</b><span>score {SCORE}</span></div>
          </div>'''
HZ_ALERT = f'''<div class="hz-scr hz-al">{sb(STRIP_CLOCK[3], True)}
            <div class="hl-d">{TUE}</div><div class="hl-t">{STRIP_CLOCK[3]}</div>
            <div class="hl-nf" style="--d:.45s"><div class="hl-nh"><i></i>{CRM}<span>now</span></div>
              <b>New verified enquiry</b><p>{BUYER_SHORT} &middot; {P1} &middot; {lo1(ANS_BUDGET)}</p><em>Score {SCORE} &middot; Call first</em></div>
            <div class="hl-home"></div>
          </div>'''
HZ_CALL = f'''<div class="hz-scr hz-cl">{sb(STRIP_CLOCK[4], True)}
            <div class="hk-av">{BUYER_INIT}</div><div class="hk-n">{BUYER}</div><div class="hk-s">03:41</div>
            <div class="hk-k"><i></i><i></i><i></i></div>
            <div class="hk-sh" style="--d:.5s"><small>{CRM} &middot; {MEETING}</small>
              <div class="hk-g"><span class="pk" style="--d:1.1s">{DY[1]}</span><span>{DY[2]}</span><span>{DY[3]}</span></div>
              <div class="hk-g"><span>{hm(SLOTS[CALL_SLOT - 1])}</span><span class="pk" style="--d:1.5s">{hm(CALL_TIME)}</span><span>{hm(SLOTS[CALL_SLOT + 1])}</span></div>
              <div class="hk-ok" style="--d:1.95s">{CHK} Booked &middot; {DY[1]} {CALL_TIME}</div>
            </div>
          </div>'''
HZ_RES = f'''<div class="hz-scr hz-wn">{sb(STRIP_CLOCK[5])}
            <div class="hw-h"><small>{CRM} &middot; pipeline</small><b>{BUYER}</b></div>
            <ol class="hw-pl">
              <li style="--d:.2s"><i></i>Verified enquiry<span>{DY[0]}</span></li>
              <li style="--d:.5s"><i></i>{up1(MEETING)} booked<span>{DY[0]}</span></li>
              <li style="--d:.8s"><i></i>{up1(MEETING)}<span>{DY[1]}</span></li>
              <li class="g" style="--d:1.2s"><i></i>{STAGE_CHOSEN}<span>{DY[2]}</span></li>
            </ol>
            <div class="hw-card" style="--d:1.7s"><img src="{AV}" alt=""><div><b>{OUTCOME}</b><span>Tracked to the ad.</span></div></div>
          </div>'''

HZ_STEPS = [('The ad', f'{BRAND} in front of {BUYERS} buying in {PLACE}.', HZ_AD),
            ('The questions', f'Her {UNIT}, budget and timing before you call.', HZ_FORM),
            ('The codes', 'Every number answers. You never pay for a fake.', HZ_CODE),
            ('The alert', f'Your {TEAM} hears about her the minute she enquires.', HZ_ALERT),
            ('The call', f'You call within five minutes and book the {MEETING}.', HZ_CALL),
            (OUTCOME, f'She {OUTCOME_VERB}s, and it&rsquo;s tracked back to the ad.', HZ_RES)]
simple = '''  <div class="hz rv">
    <div class="hz-grid">
      <div class="hz-track" aria-hidden="true"><i class="hz-fill"><b></b></i></div>
''' + '\n'.join(f'''      <div class="hz-s{' yz' if i >= 4 else ''}" data-i="{i}">
        <i class="hz-n"></i>
        <div class="hz-ph"><div class="hz-in"><i class="hz-isl"></i>
          {scr}
        </div></div>
        <h4>{h}</h4><p>{p}</p>
      </div>''' for i, (h, p, scr) in enumerate(HZ_STEPS)) + '''
    </div>
  </div>'''

LIVE = '''    <div class="jlive rv"><i></i><div><b>The Verified Buyer Funnel, live.</b><span>Two stages. Press play, or tap any step.</span></div><i></i></div>'''


# ═══════════════════════════════════════════════════════════════════════════
# 2 · THE FORM — the six questions are QS in the CONFIG block; here, the reason caption for each other step
# ═══════════════════════════════════════════════════════════════════════════
R_OPEN = ('The form', 'It opens inside Instagram, so nothing slows her down.')
R_NAME = ('Name', 'So your team can greet her by name.')
R_MOB = ('Mobile', 'The number your team will call. It gets checked next.')
R_EMAIL = ('Email', 'Where her pack and reminders go.')
R_OK = ('Consent', f'So she has said yes to hearing from {DEV_SHORT}.')
R_CM = ('Mobile code', 'So every number answers. You never pay for a fake.')
R_CE = ('Email code', 'And a second code, so the email is real too.')
R_SEND = ('Sent', 'No code, no enquiry. Only verified buyers reach your team.')


class Dir:
    """the director: walks a clock forward and writes the thumb's script (global film ms)"""
    def __init__(s, t0):
        s.t, s.A, s.C, s.marks, s.kb0, s.rnd = t0, [], [], [t0], None, random.Random(11)
    def wait(s, ms): s.t += ms
    def mark(s): s.marks.append(s.t)                       # a chapter boundary
    def cap(s, label, text): s.C.append([s.t, (f'<em>{label}</em>' if label else '') + text])
    def sy(s, key, dur=850, frac=.06): s.A.append(['sy', s.t, key, dur, frac])
    def tap(s, key): s.A.append(['tap', s.t, key])
    def pg(s, i): s.A.append(['pg', s.t, i])
    def on(s, key): s.A.append(['on', s.t, key])
    def nf(s, key, dur): s.A.append(['nf', s.t, key, dur])
    def kb(s, mode=None):                                  # keyboard up in a mode, or down (None)
        if mode:
            s.A.append(['km', s.t, mode])
            if s.kb0 is None: s.kb0 = s.t
        elif s.kb0 is not None:
            s.A.append(['kb', s.kb0, s.t]); s.kb0 = None
    def ty(s, key, text, base, digits=False):
        offs, o = [], 0
        for i, ch in enumerate(text):
            if i and not (digits and ch == ' '): o += int(base * (.65 + .7 * s.rnd.random()))
            offs.append(o)
        s.A.append(['ty', s.t, key, text, offs]); s.t += offs[-1] + base

    # ── the steps, at a reading pace ──
    def question(s, qi, key_q, key_o):
        q = QS[qi]
        s.sy(key_q, 750, .04); s.wait(200); s.cap(q[3], q[4]); s.wait(1350); s.tap(key_o); s.wait(1000)
    def field(s, kw, k, r, text, mode, base, first=False):
        s.sy(kw, 700, .05); s.wait(200); s.cap(*r); s.wait(1000); s.tap(k); s.wait(250)
        s.kb(mode); s.wait(400 if first else 200); s.ty(k, text, base, mode == 'n'); s.wait(450)
    def details(s, p):                                     # p = key prefix
        s.field(p + 'fnw', p + 'fn', R_NAME, BUYER, 'a', 95, True)
        s.field(p + 'fmw', p + 'fm', R_MOB, MOB, 'n', 125)
        s.field(p + 'few', p + 'fe', R_EMAIL, EMAIL, 'a', 72)
        s.kb(); s.wait(350)
        s.sy(p + 'ck', 700, .3); s.wait(200); s.cap(*R_OK); s.wait(1200); s.tap(p + 'ck'); s.wait(800)
    def codes(s, p, last):
        s.cap(*R_CM); s.wait(400); s.nf(p + 'nsms', 2600); s.wait(1150); s.tap(p + 'cm'); s.wait(200)
        s.kb('n'); s.wait(400); s.ty(p + 'cm', CODE_MOB, 150); s.wait(200); s.on(p + 'okm'); s.wait(700)
        s.cap(*R_CE); s.wait(300); s.nf(p + 'nmail', 2600); s.wait(1150); s.tap(p + 'ce'); s.wait(400)
        s.ty(p + 'ce', CODE_EMAIL, 150); s.wait(200); s.on(p + 'oke'); s.wait(350); s.kb(); s.wait(350)
        s.sy(last, 600, .35); s.cap(*R_SEND); s.wait(1200); s.tap(last); s.wait(600)


# ── the buyer's screens ──
# the ad: angle one (AD_NAME) — a designed static (logo, headline, price, feature strip on the hero photo)
def feed(cta, btn):
    return f'''<div class="xscr {{S}} t-feed">
              <div class="fd-app"><b>Home</b><span><i></i><i></i></span></div>
              <div class="fd-feed">
                <div class="fd-skel"><i></i><i style="width:78%"></i></div>
                <div class="fd-post">
                  <div class="fd-h">{AVI}<div><b>{PAGE}</b><i>Sponsored</i></div></div>
                  <div class="fd-tx">{AD_TEXT}</div>
                  <div class="fd-img"><img src="{IMG_HERO}" alt="" style="object-position:50% 62%;">
                    <img class="fd-lg" src="{LOGO_LIGHT}" alt="{BRAND}">
                    <span class="fd-pr"><small>From</small>{P1_FROM}<small>&asymp; {P1_FROM_AUD}</small></span>
                    <div class="fd-ov">{AD_HEAD[0]}<br><em>{AD_HEAD[1]}</em></div>
                    <div class="fd-ft">{''.join(f'<span>{x}</span>' for x in AD_FEATURES)}</div></div>
                  <div class="fd-cta"><div><small>{PAGE}</small><b>{cta}</b></div><span class="fd-btn">{btn}{tap('3.3s')}</span></div>
                  <div class="fd-rx"><i></i><i></i><i></i><span>Like &middot; Comment &middot; Share</span></div>
                </div>
              </div>
            </div>'''
FEED1 = feed(f'See the {UNITS} and prices', 'Sign up').replace('{S}', 's1')
FEED2 = feed(f'Watch the {SITE} film first', 'Learn more').replace('{S}', 's1')


def keyboard():
    k = lambda row: ''.join(f'<i data-c="{c}">{c}</i>' for c in row)
    abc = (f'<div class="kr">{k("qwertyuiop")}</div><div class="kr k2">{k("asdfghjkl")}</div>'
           f'<div class="kr"><u class="kw">&#8679;</u>{k("zxcvbnm")}<u class="kw">&#9003;</u></div>'
           f'<div class="kr"><u class="kw">123</u><i data-c="@">@</i><i class="ksp" data-c=" ">space</i><i data-c=".">.</i><u class="kw kg">go</u></div>')
    pad = [('1', ''), ('2', 'ABC'), ('3', 'DEF'), ('4', 'GHI'), ('5', 'JKL'), ('6', 'MNO'), ('7', 'PQRS'), ('8', 'TUV'), ('9', 'WXYZ')]
    num = ('<div class="kn">' + ''.join(f'<i data-c="{d}">{d}<small>{l}</small></i>' for d, l in pad)
           + '<u></u><i data-c="0">0<small>+</small></i><u>&#9003;</u></div>')
    return f'<div class="fx-kb" data-m="a" aria-hidden="true"><div class="kb-a">{abc}</div><div class="kb-n">{num}</div><div class="kb-h"><i></i></div></div>'

def banners(p):
    return (f'<div class="ib fx-nf" data-k="{p}nsms"><i class="ib-i msg"></i><div><b>Messages<span>now</span></b><p>{CODE_MOB} is your {BRAND} code.</p></div></div>'
            f'<div class="ib fx-nf" data-k="{p}nmail"><i class="ib-i mail"></i><div><b>Mail<span>now</span></b><p>{BRAND} &middot; your code is {CODE_EMAIL}</p></div></div>')

FINGER = '<i class="fx-rp" aria-hidden="true"></i><i class="fx-fg" aria-hidden="true"></i>'

def fin(cls, k, ph):
    return f'<div class="{cls}" data-k="{k}"><span class="fx-ph">{ph}</span><span class="fx-tx"></span><i class="fx-car"></i></div>'

# stage one: Meta's instant form — three screens
def lf_q(qi):
    q = QS[qi]
    return (f'<div class="lf-q" data-k="q{qi}"><div class="lf-ql">{qi + 1}. {q[0]}</div>'
            + ''.join(f'<div class="lf-o" data-k="q{qi}o{k}" data-g="q{qi}" data-px=".2"><i></i><span>{o}</span></div>' for k, o in enumerate(q[1])) + '</div>')
def lf_sb(n, lab, w):
    return f'<div class="lf-sb"><div><span>Step {n} of 3 &middot; {lab}</span><span>{n}/3</span></div><i><b style="width:{w}%"></b></i></div>'
def lf_f(k, label, ph):
    return f'<div class="lf-f" data-k="{k}w"><small>{label}</small>{fin("lf-fi", k, ph)}</div>'
def lf_vr(k, label, to):
    return (f'<div class="lf-vr"><div class="lf-vk"><span>{label} &middot; {to}</span><b data-k="ok{k[-1]}">{CHK} Confirmed</b></div>'
            f'<div class="fx-code" data-k="{k}">{"<i></i>" * 6}</div></div>')
FORM = f'''<div class="xscr s2 s3 s4 s5 t-lf fx-root">
              <div class="lf-hd"><span>&#10005;</span><b>{PAGE}</b></div>
              <div class="lf-vp">
                <div class="fx-pg"><div class="fx-doc">
                  <div class="lf-img"><img src="{IMG_HERO}" alt=""></div>
                  {lf_sb(1, f'your {UNIT}', 33)}
                  <div class="lf-in"><h4>Own {A_UNIT} at {BRAND}</h4><p>Six quick questions, so our {TEAM} calls you with the right prices and photos.</p></div>
                  {''.join(lf_q(i) for i in range(3))}
                  <div class="lf-go fx-btn" data-k="go1">Continue</div>
                </div></div>
                <div class="fx-pg"><div class="fx-doc">
                  {lf_sb(2, 'timing &amp; details', 66)}
                  {''.join(lf_q(i) for i in range(3, 6))}
                  {lf_f('fn', 'Full name', 'Your full name')}
                  {lf_f('fm', 'Mobile number', 'Your mobile')}
                  {lf_f('fe', 'Email', 'Your email')}
                  <div class="lf-ck fx-ck" data-k="ck" data-px=".09"><i></i><span>{CONSENT}</span></div>
                  <div class="lf-go fx-btn" data-k="go2">Continue</div>
                </div></div>
                <div class="fx-pg"><div class="fx-doc">
                  {lf_sb(3, 'verify', 100)}
                  <div class="lf-in"><h4>Confirm it&rsquo;s really you</h4><p>We&rsquo;ve sent a six-digit code to your mobile and to your email.</p></div>
                  {lf_vr('cm', 'Mobile', MOB_M)}
                  {lf_vr('ce', 'Email', EMAIL_M)}
                  <div class="lf-go pri fx-btn" data-k="go3">Verify &amp; send my enquiry</div>
                  <div class="lf-rs">Didn&rsquo;t get one? <b>Resend code</b></div>
                </div></div>
              </div>
              {banners('')}
              {keyboard()}
              {FINGER}
            </div>'''

THANKS = f'''<div class="xscr s6 t-thanks">
              <div class="fm-h">{AVI}<div><b>{BRAND}</b><small>Your enquiry &middot; sent</small></div></div>
              <div class="fm-bar"><i style="width:100%"></i></div>
              <div class="th-ok" style="--d:.2s">{CHK}</div>
              <div class="th-t" style="--d:.45s">Thanks, {BUYER_FIRST} &mdash; your enquiry is in.</div>
              <div class="th-s" style="--d:.7s">Our {TEAM} will call you shortly on <b>{MOB_M}</b>.</div>
              <div class="th-n" style="--d:1s"><small>What happens next</small><div><i>1</i>A call from our {TEAM}</div><div><i>2</i>Your pack: prices, photos, {CLUB.lower()}</div><div><i>3</i>A {MEETING_LONG}, at a time that suits you</div></div>
            </div>'''

def incall(cls, when, sub, quote, toast, tm, td='4.2s', extra=''):
    return f'''<div class="xscr {cls} t-call">
              <div class="ic-ring">
                <div class="ic-t">{when}</div>
                <div class="cl-av"><img src="{AV}" alt=""><i></i><i></i></div>
                <div class="ic-n">{BRAND}</div><div class="ic-s">{up1(TEAM)} &middot; mobile</div>
                <div class="cl-btns"><span class="cl-no">{PHONE_SVG}Decline</span><span class="cl-yes">{PHONE_SVG}Accept{tap('.95s')}</span></div>
              </div>
              <div class="ic-live">
                {f'<div class="ib dk" style="--d:{td}"><i class="ib-i br"></i><div><b>{BRAND}<span>now</span></b><p>{toast}</p></div></div>' if toast else ''}
                <div class="ic-t">{when}</div>
                <div class="cl-av sm"><img src="{AV}" alt=""></div>
                <div class="ic-n">{BRAND}</div>
                <div class="ic-s">{sub} &middot; <span class="tmr" data-tm="{tm[0]}" data-tm-at="{tm[1]}" data-tm-len="{tm[2]}">{tm[0] // 60:02d}:{tm[0] % 60:02d}</span></div>
                {f'<div class="ic-q"><small>Your {TEAM}</small>{quote}</div>' if quote else ''}
                <div class="ic-ctl"><span></span><span></span><span></span></div>
                <div class="ic-end">{PHONE_SVG}</div>
                {extra}
              </div>
            </div>'''

def messages(cls, time0, bubbles, typed, extra=''):
    rows = []
    for b in bubbles:
        if b[0] == 't':
            rows.append(f'<div class="ms-time" style="--d:{b[2]}">{b[1]}</div>')
        else:
            rows.append(f'<div class="ms-b {"me" if b[0] == "me" else "in"}" style="--d:{b[2]}">{b[1]}</div>')
    return f'''<div class="xscr {cls} t-msg">
              <div class="ms-h"><span class="ms-back">&lsaquo;</span>{AVI}<b>{BRAND}</b><small>Text message &middot; SMS</small></div>
              <div class="ms-body">
                <div class="ms-time">{time0}</div>
                {''.join(rows)}
              </div>
              <div class="ms-cmp"><span class="ms-plus">+</span><div class="ms-in"><span class="ph">Text message</span>{''.join(f'<span class="ty" style="--d:{d};--n:{len(t)}">{t}</span>' for t, d in typed)}</div><span class="ms-send"></span></div>
              {extra}
            </div>'''

def mail(cls, inner):
    return f'''<div class="xscr {cls} t-mail">
              <div class="ml-h"><span class="ms-back">&lsaquo;</span><b>Inbox</b></div>
              {inner}
            </div>'''

# 7 · the call: she answers, the pack lands while they talk, the private call is booked
PACK = f'''<div class="pk-card" style="--d:3.4s"><small>Mail &middot; {BRAND}</small><b>Your {BRAND_SHORT} pack</b>
                  <div class="pk-ph"><img src="{IMG_P1}" alt=""><img src="{IMG_HERO}" alt=""><img src="{IMG_EVENT}" alt=""></div>
                  <span>Prices in {CUR_PAIR} &middot; photos &middot; {CLUB}</span></div>'''
CALL1 = incall('s7', f'{DAY[0]} &middot; {CLOCK1[6]}', up1(TEAM), '', f'Your {MEETING} is booked: {DAY[1]}, {CALL_TIME}. Speak then.', (372, 1300, 7000), '7.0s', PACK)

# 8 · reminders, and what happens if she misses it
REBOOK = f'''<div class="wi" style="--d:3.6s"><em>If she misses it</em><p>Sorry we missed you, {BUYER_FIRST}. Pick a new time:</p>
                <div><span>{REBOOK_SLOTS[0]}</span><span class="pk" style="--d:5s">{REBOOK_SLOTS[1]}</span><span>{REBOOK_SLOTS[2]}</span></div><b style="--d:5.4s">{CHK} Rebooked</b></div>'''
REMIND = messages('s8', f'Today {T_CONFIRM}', [
    ('in', f'You&rsquo;re booked: a {MEETING_LONG} with {BRAND}, <b>{WED}, {CALL_TIME}</b> ({TZ_SAME}).', '.2s'),
    ('t', f'{DAY[1]} {T_REMIND}', '.8s'),
    ('in', f'Morning {BUYER_FIRST}. Your {MEETING} is today at {CALL_TIME}.', '1s'),
    ('t', f'{DAY[1]} {CLOCK1[7]}', '1.6s'),
    ('in', 'Your call starts in an hour. <u>Join the video call</u>', '1.8s'),
    ('me', 'See you then!', '2.8s')], [('See you then!', '2.3s')], REBOOK)

# 9 · the private call: a video walk-through — the product, the site, the club
SHOTS = [(IMG_P1, '0s', f'The {P1} &middot; {P1_SPEC[0]}', '40% 50%'),
         (IMG_SITE, '2s', f'The {SITE} &middot; {PLACE}', '50% 55%'),
         (IMG_CLUB, '4s', f'The {CLUB}', '26% 22%')]
def shots(label=True):
    return ''.join(f'<div class="vc-sh" style="--d:{d}"><img src="{src}" alt="" style="object-position:{pos}">'
                   + (f'<span>{lab}</span>' if label else '') + '</div>' for src, d, lab, pos in SHOTS)
PRIV = f'''<div class="xscr s9 t-call t-vc">
              <div class="vc-st">{shots()}</div>
              <div class="vc-top"><img src="{AV}" alt=""><div><b>{BRAND}</b><span>{up1(MEETING)} &middot; <span class="tmr" data-tm="1236" data-tm-at="600" data-tm-len="6200">20:36</span></span></div><em><i></i>Live</em></div>
              <div class="vc-me">{BUYER_INIT}</div>
              <div class="vc-ctl"><i>{MIC_SVG}</i><i>{CAM_SVG}</i><i class="end">{PHONE_SVG}</i></div>
            </div>'''

# 10 · her choice: the team sends the product she liked, she chooses it
SUITE_CARD = f'''<div class="pc"><div class="pc-i"><img src="{IMG_P1}" alt=""></div><b>The {P1}</b>
                  <span>{P1_SPEC[0]} &middot; {P1_SPEC[1]}</span><span>From {P1_PRICE}</span><span>&asymp; {P1_PRICE_AUD}</span></div>'''
SUITE = messages('s10', f'{DAY[2]} {CLOCK1[9]}', [
    ('in', f'Hi {BUYER_FIRST}, thanks for your time yesterday. Here&rsquo;s the {UNIT} you liked on the call.', '.3s'),
    ('in', SUITE_CARD, '.9s'),
    ('me', f'That&rsquo;s the one. How do I {OUTCOME_VERB} it?', '3.5s')], [(f'That&rsquo;s the one. How do I {OUTCOME_VERB} it?', '2.3s')])

# 11 · the outcome: with the developer, confirmed by email
RESERVED = mail('s11', f'''<div class="ml-m" style="--d:.3s">
                <div class="ml-f">{AVI}<div><b>{BRAND}</b><small>{DEV} &middot; now</small></div></div>
                <h6>Your {UNIT} is {OUTCOME.lower()}, {BUYER_FIRST}.</h6>
                <div class="ml-img"><img src="{IMG_P1B}" alt=""></div>
                <ul><li>{CHK} The {P1} &middot; {P1_SPEC[0]}</li><li>{CHK} {OUTCOME} with {DEV_SHORT}</li><li>{CHK} Your {TEAM} will call with the next steps</li></ul>
              </div>
              <div class="ml-c gold" style="--d:1.7s"><i>{CHK}</i><small>{BRAND}</small><b>{OUTCOME}</b></div>''')


# ── stage two: the client's landing page, one long page her thumb works through ──
def lq(i):
    q = QS[i]
    return (f'<div class="lpq" data-k="lq{i}"><small>{q[5]}</small><div>'
            + ''.join(f'<span data-k="lq{i}o{k}" data-g="lq{i}">{o}</span>' for k, o in enumerate(q[1])) + '</div></div>')
def lpf(k, label, ph):
    return f'<div class="lpf" data-k="{k}w"><small>{label}</small>{fin("lp-fi", k, ph)}</div>'
def cal_days():
    """three weeks of the month (Monday-first), CAL_FROM to CAL_TO; today (DATE[0]) and earlier are greyed"""
    out = ''
    for d in range(CAL_FROM, CAL_TO + 1):
        wd = (d - CAL_FROM) % 7
        if d <= DATE[0]: out += f'<span class="mu">{d}</span>'
        elif wd in (5, 6): out += f'<span class="we">{d}</span>'
        else: out += f'<span class="av" data-k="cd{d}" data-g="cday">{d}</span>'
    return out
# the film: until the client's film is shot, five of their stills play as a slow Ken Burns film (journey.js plays it like a video)
FILM = [(FILM_STILLS[0], 0, 3, '50% 50%'), (FILM_STILLS[1], 3, 12, '50% 60%'), (FILM_STILLS[2], 12, 24, '40% 50%'),
        (FILM_STILLS[3], 24, 36, '50% 45%'), (FILM_STILLS[4], 36, 48, '50% 50%')]
FILM_SUBS = [f'{BRAND}, {PLACE}', f'Two {UNITS}, two clear prices', f'The {CLUB}', f'Built by {DEV_SHORT}, run by {PARTNER}']   # one per quarter of the film
FILM_CH = [f'The {SITE}, {PLACE}', f'The two {UNITS}', f'The {CLUB}', f'Built by {DEV_SHORT}, run by {PARTNER}']           # its chapter list
TRUST = [f'{DEV_SHORT} &middot; {DEV_YEARS}', f'Run by {PARTNER}', f'From {P1_FROM}']                                     # the strip under the button
LANDING = f'''<div class="xscr s2 s3 s4 s5 lpg fx-root">
              <div class="lp-url">{LOCK_SVG}{DOMAIN}</div>
              <div class="lp-vp">
                <div class="lp-nav"><img src="{WORDMARK}" alt="{BRAND}"><span>{up1(MEETING)}</span><i class="lp-burger"></i></div>
                <div class="lp-doc fx-doc" data-top="46">
                  <div class="lv mb"><div class="lv-page">
                    <div class="lv-eye">A short film &middot; {BRAND}</div>
                    <h5 class="lv-h">Thinking about {A_UNIT} at {BRAND_SHORT}? <em>Watch this first.</em></h5>
                    <div class="lp-vid lv-vid" role="button" aria-label="Play or pause the film" data-len="48" data-subs="{'|'.join(FILM_SUBS)}" data-tip="Your film &mdash; the {SITE}&rsquo;s stills stand in until we shoot it. It plays before she&rsquo;s asked for anything.">
                      {''.join(f'<div class="lv-fr" data-s="{a}" data-e="{b}"><img src="{src}" alt="" style="object-position:{pos}"></div>' for src, a, b, pos in FILM)}
                      <span class="lp-tag lv-tag">Your film &mdash; {SITE} stills stand in</span>
                      <span class="lp-mute">{MUTE_SVG}</span>
                      <span class="lp-big lv-play"></span>
                      <span class="lv-cc">{FILM_SUBS[0]}</span>
                      <div class="lp-ctl"><div class="lp-bar"><i class="lp-fill"></i><b style="left:25%"></b><b style="left:50%"></b><b style="left:75%"></b></div><span class="lp-tm">0:00 / 0:48</span></div>
                    </div>
                    <ol class="lp-ch"><li class="on"><i>0:00</i>{FILM_CH[0]}</li><li><i>0:12</i>{FILM_CH[1]}</li><li><i>0:24</i>{FILM_CH[2]}</li><li><i>0:36</i>{FILM_CH[3]}</li></ol>
                    <div class="lv-cta fx-btn" data-k="lcta">Book a {MEETING} &rarr;</div>
                    <div class="lv-tr">{''.join(f'<span>{x}</span>' for x in TRUST)}</div>
                  </div></div>
                  <div class="lp-sec" data-k="sbrief"><small>Step 1 of 3 &middot; six quick questions</small><b>Tell us what you&rsquo;re after</b></div>
                  <div class="lpqs">{''.join(lq(i) for i in range(6))}</div>
                  <div class="lp-sec" data-k="sdet"><small>Step 2 of 3 &middot; your details</small><b>Your contact details</b></div>
                  {lpf('lfn', 'Full name', 'Your full name')}
                  {lpf('lfm', 'Mobile', 'Your mobile')}
                  {lpf('lfe', 'Email', 'Your email')}
                  <div class="lp-ck fx-ck" data-k="lck" data-px=".09"><i></i><span>{CONSENT}</span></div>
                  <div class="lpv"><small>Mobile &middot; code sent to {MOB_M}</small>
                    <div class="lpv-r"><div class="lpv-c fx-code" data-k="lcm">{"<i></i>" * 6}</div><em data-k="lokm">{CHK}</em></div></div>
                  <div class="lpv"><small>Email &middot; code sent to {EMAIL_M}</small>
                    <div class="lpv-r"><div class="lpv-c fx-code" data-k="lce">{"<i></i>" * 6}</div><em data-k="loke">{CHK}</em></div></div>
                  <div class="lp-next fx-btn" data-k="lgo">Verify &amp; pick a time</div>
                  <div class="lp-sec" data-k="scal"><small>Step 3 of 3 &middot; your {MEETING}</small><b>Pick a time with our {TEAM}</b><span>A {MEETING_LEN} &middot; {TZ_SAME}</span></div>
                  <div class="lpc" data-tip="Your team&rsquo;s calendar on your page &mdash; she books herself, straight into your {CRM}.">
                    <div class="lpc-hd"><b>{MONTH} {YEAR}</b><span>&lsaquo;&nbsp;&nbsp;&rsaquo;</span></div>
                    <div class="lpc-wk"><span>M</span><span>T</span><span>W</span><span>T</span><span>F</span><span>S</span><span>S</span></div>
                    <div class="lpc-g">{cal_days()}</div>
                    <div class="lpc-sl"><small>{WED} &middot; {TZ}</small><div>{''.join(f'<span data-k="ct{i}" data-g="ctime">{s}</span>' for i, s in enumerate(SLOTS))}</div></div>
                    <div class="lpc-go fx-btn" data-k="cgo">Confirm &middot; {CALL_SHORT}</div>
                  </div>
                  <div class="lpk" data-k="lok"><i>{CHK}</i><b>You&rsquo;re booked, {BUYER_FIRST}</b><span>{WED} &middot; {CALL_TIME} {TZ}<br>{up1(MEETING_LONG)} &middot; {BRAND}</span><div><em>Add to calendar</em><em>Reschedule</em></div></div>
                  <div class="lp-foot"><img src="{LOGO_DARK}" alt="{BRAND}"><span>{BRAND} &middot; by {DEV}</span></div>
                </div>
              </div>
              {banners('l')}
              {keyboard()}
              {FINGER}
            </div>'''


# ═══════════════════════════════════════════════════════════════════════════
# 3 · YOUR SALES TEAM'S SCREENS
# ═══════════════════════════════════════════════════════════════════════════
def lock(cls, time, date, notes='', idle=''):
    return f'''<div class="gscr {cls} g-lock">
              <div class="g-date">{date}</div><div class="g-time">{time}</div>
              {f'<div class="g-idle">{idle}</div>' if idle else ''}<div class="g-nfs">{notes}</div>
              <div class="g-btm"><i></i><i></i></div><div class="g-home"></div>
            </div>'''
def nf(title, body, when='now', d=None, tag=None, acts=None, app=CRM):
    st = f' style="--d:{d}"' if d is not None else ''
    a = ''.join(f'<span>{x}</span>' for x in acts) if acts else ''
    return (f'<div class="g-nf{" drop" if d is not None else ""}"{st}><div class="g-nf-h"><i></i>{app}<span>{when}</span></div>'
            f'<b>{title}</b><p>{body}</p>{f"<em>{tag}</em>" if tag else ""}{f"<div class=\"g-act\">{a}</div>" if a else ""}</div>')
def keys():
    return '<div class="g-keys">' + ''.join(f'<span><i></i>{k}</span>' for k in ['mute', 'keypad', 'speaker', 'add call', 'FaceTime', 'contacts']) + '</div>'
def gcall(cls, when, sub2, tm, body='', ring=False, c1dur=None):
    st = f' style="animation-duration:{c1dur}"' if c1dur else ''
    tmr = f'<span class="tmr" data-tm="{tm[0]}" data-tm-at="{tm[1]}" data-tm-len="{tm[2]}">{tm[0] // 60:02d}:{tm[0] % 60:02d}</span>' if tm else ''
    return f'''<div class="gscr {cls} g-call">
              <div class="g-ct">{when}</div>
              <div class="g-av{" rg" if ring else ""}">{BUYER_INIT}</div>
              <div class="g-who">{BUYER}</div>
              <div class="g-sub"><span class="c1"{st}>calling mobile&hellip;</span><span class="c2"{st}>{sub2}{tmr}</span></div>
              {keys()}
              <div class="g-end">{PHONE_SVG}</div>
              {body}
            </div>'''
G_BOOK = gcall('g7 gbk', f'{DAY[0]} &middot; {CLOCK1[6]}', f'mobile &middot; {BUYER_CITY} &middot; ', (372, 1300, 7000), f'''<div class="g-sheet">
                <div class="g-sh-h"><i></i>{CRM} &middot; book the {MEETING}</div>
                <b>{MEETING_LEN} &middot; {BUYER}</b>
                <div class="g-days"><span class="pk" style="--d:6.1s">{DY[1]}{tap('6.05s')}</span><span>{DY[2]}</span><span>{DY[3]}</span></div>
                <div class="g-times"><span>{SLOTS[CALL_SLOT - 1]}</span><span class="pk" style="--d:6.5s">{CALL_TIME}{tap('6.45s')}</span><span>{SLOTS[CALL_SLOT + 1]}</span></div>
                <div class="g-ok" style="--d:6.9s">{CHK} Booked &middot; confirmation sent to {BUYER_FIRST}</div>
              </div>''')
# 9 · the private call, from your team's side: her on video, the walk-through shared, the checklist ticking off
G_PRIV = f'''<div class="gscr g9 g-call g-vc">
              <div class="g-ct">{DAY[1]} &middot; {CALL_TIME}</div>
              <div class="gv-hd"><div class="g-av">{BUYER_INIT}</div><div><b>{BUYER}</b><span>{up1(MEETING_LONG)} &middot; {BUYER_CITY} &middot; <span class="tmr" data-tm="1236" data-tm-at="600" data-tm-len="6200">20:36</span></span></div></div>
              <div class="gv-sh"><small><i></i>Sharing &middot; the walk-through</small><div class="gv-st">{shots(False)}</div></div>
              <div class="g-chk"><small>On the call</small>
                <div style="--d:.6s"><i>{CHK}</i>The {UNIT}<b>{P1_SHORT}</b></div><div style="--d:2.4s"><i>{CHK}</i>The {SITE}<b>{PLACE}</b></div>
                <div style="--d:4.2s"><i>{CHK}</i>The {CLUB}<b>Benefits</b></div><div style="--d:5.2s"><i>{CHK}</i>Returns<b>Explained</b></div>
                <em style="--d:5.9s">Ready to choose {A_UNIT}</em></div>
            </div>'''

# ═══════════════════════════════════════════════════════════════════════════
# 4 · THE SHOW — phones, record, wires, player
# ═══════════════════════════════════════════════════════════════════════════
def phone(scr, status, big=False):
    sts = ''.join(f'<em class="st" data-at="{i+1}">{s}</em>' for i, s in enumerate(status))
    body = '\n            '.join(scr)
    return f'''<div class="xph{' big' if big else ''}"><div class="xph-in">
          <div class="xph-isl"></div>
          <div class="xstatus"><span>{sts}</span><b><i class="xsig"></i><i class="bat"></i></b></div>
          <div class="xscrs">
            {body}
          </div>
        </div></div>'''
def gphone(scrs, status):
    sts = ''.join(f'<em class="st" data-at="{i+1}">{s}</em>' for i, s in enumerate(status))
    return f'''<div class="xph gr"><div class="xph-in">
          <div class="xph-isl"></div>
          <div class="xstatus"><span>{sts}</span><b><i class="xsig"></i><i class="bat"></i></b></div>
          <div class="xscrs">
            {"".join(scrs)}
          </div>
        </div></div><div class="hap" aria-hidden="true"><i></i><i></i></div>'''

def record(fields, badges, acts, src, wait):
    fl = ''.join(f'<div class="f"><small>{k}</small><p><i class="ph"></i><span class="v" data-from="{f}" style="--d:{d}">{v}</span></p></div>' for k, v, f, d in fields)
    bd = ''.join(f'<span class="bd{" gold" if g else ""}" data-from="{f}" style="--d:{d}">{t}</span>' for t, f, d, g in badges)
    ac = ''.join(f'<div data-from="{f}" style="--d:{d}"><b>{w}</b><span>{t}</span></div>' for w, t, f, d in acts)
    cols = ''.join(f'<div class="kc"><small>{c}</small><i></i></div>' for c in COLS)
    return f'''<div class="xrec">
          <div class="xr-bar"><span class="xr-dots"><i></i><i></i><i></i></span><i class="xr-lg"></i>{CRM}<span class="xr-cr">Leads &rsaquo; <b>{BUYER}</b></span><em class="xr-live"><i></i>Live</em></div>
          <div class="xr-body">
            <div class="xr-side"><i class="on"></i><i></i><i></i><i></i><i></i></div>
            <div class="xr-main">
              <div class="xr-hd">
                <div class="xr-av">{BUYER_INIT}</div>
                <div class="xr-nm"><b>{BUYER}</b><span>{BUYER_CITY}, {BUYER_REGION} &middot; {src}</span></div>
                <div class="xr-sc" style="--p:0" data-tip="Her lead score &mdash; every answer adds to it. {SCORE} means call first."><svg viewBox="0 0 44 44" aria-hidden="true"><circle class="bg" cx="22" cy="22" r="19"/><circle class="fg" cx="22" cy="22" r="19" pathLength="100"/></svg><b>&ndash;</b><small>score</small></div>
              </div>
              <div class="xr-bdg" data-tip="Mobile and email, each confirmed by a code. No code, no enquiry.">{bd}</div>
              <div class="xr-k">Her answers</div>
              <div class="xr-br" data-tip="Her six answers, straight into your {CRM}.">{fl}</div>
              <div class="xr-k">Buyer pipeline</div>
              <div class="xr-kb" data-col="-1" style="--col:0" data-tip="Your pipeline &mdash; her card moves itself, from verified to {OUTCOME.lower()}.">{cols}<div class="xr-card"><i>{BUYER_INIT}</i><b>{BUYER_FIRST}</b></div></div>
              <div class="xr-k">Activity</div>
              <div class="xr-act" data-tip="Every step logged with the time &mdash; nothing to type up.">{ac}</div>
            </div>
          </div>
          <div class="xr-wait"><i></i><b>{wait[0]}</b><span>{wait[1]}</span></div>
        </div>'''
WAIT = ('Waiting for her enquiry', 'Her record appears the moment she sends it.')

def land_events(LAND, t0=150):
    """her answers arrive in the CRM all at once, on send: answers, score, both ticks"""
    ev = [[t0, 'pk', 'L', 'Her answers &middot; 6 of 6', 0], [t0 + 1650, 'pl', 0]]
    for i in range(6): ev.append([t0 + 450 + i * 190, 'sc', SCORE_STEPS[i]])
    fields = [(k, v, LAND, f'{(t0 + 350 + i * 190) / 1000:.2f}s') for i, (k, v) in enumerate(BRIEF)]
    return ev, fields

def caps(items):
    ck = ''.join(f'<span data-at="{i+1}">{c}</span>' for i, (c, _) in enumerate(items))
    tx = ''.join(f'<div class="xct" data-at="{i+1}"><h3>{h}</h3></div>' for i, (_, h) in enumerate(items))
    return f'<div class="xcap"><div class="xck"><i></i>{ck}</div>{tx}</div>'

def player(steps, dur, minor):
    tot = sum(dur); acc = 0; ticks = ''
    for d in dur[:-1]:
        acc += d; ticks += f'<b style="left:{acc / tot * 100:.2f}%"></b>'
    ticks += ''.join(f'<b class="mi" style="left:{m / tot * 100:.2f}%"></b>' for m in minor)
    b = ''.join(f'<button type="button" class="xstep{" on" if i == 0 else ""}" data-s="{i+1}"><i class="pt"><i class="pf"></i></i><b>{i+1:02d} &middot; {n}</b><span>{h}</span></button>' for i, (n, h) in enumerate(steps))
    t = f'{tot // 60000}:{(tot // 1000) % 60:02d}'
    return f'''<div class="xbar">
        <div class="xctl"><button type="button" class="xplay" aria-label="Play the film"><i></i><span>Play</span></button><button type="button" class="xrp" aria-label="Replay from the start"><i></i></button></div>
        <div class="xtl">
          <div class="xscrub" role="slider" aria-label="Scrub the film" tabindex="0"><i class="xsf"></i>{ticks}<em class="xsh"></em></div>
          <div class="xsteps">{b}</div>
        </div>
        <div class="xopt"><span class="xtm">0:00 / {t}</span><button type="button" class="xccb on" aria-pressed="true" aria-label="Captions">CC</button><button type="button" class="xsnd" aria-pressed="false"><i></i><span>Music on</span></button></div>
      </div>'''

def storyboard(caps_, steps, cc):
    """at rest and in print: every chapter, and every form step with its reason"""
    out = []
    for i in range(len(steps)):
        lines = ''.join(f'<li>{x[1]}</li>' for x in cc.get(i + 1, []))
        out.append(f'<div><small>{i+1:02d} &middot; {steps[i][1]}</small><b>{caps_[i][1]}</b><ul>{lines}</ul></div>')
    return '<div class="xsb">' + ''.join(out) + '</div>'

WIRES = '<svg class="xwires" aria-hidden="true"><path class="w wL"/><path class="w wR"/><path class="w wC"/></svg>'

TIP_BUY = f'{BUYER_FIRST}&rsquo;s phone &mdash; exactly what she sees, tap for tap.'
TIP_GR = f'Your {TEAM}&rsquo;s phone in {TEAM_PLACE} &mdash; the alert, the call and the booking. {TZ_NOTE}'
def show(cls, attrs, stagetxt, buy, mid, gr, bar, sb='', cc=None, fx=None, over=''):
    fxa = json.dumps(fx, separators=(',', ':'))
    assert "'" not in fxa and "'" not in json.dumps(cc)
    return f'''  <div class="xj {cls}" {attrs} data-cc='{json.dumps(cc)}' data-fx='{fxa}'>
    <div class="xshow rv" data-step="1">
      <div class="xview" data-focus="W">
        <div class="xrig">
          <div class="xglow" aria-hidden="true"></div>
          {WIRES}
          <div class="xbuy"><div class="xlab">{BUYER_FIRST}&rsquo;s phone &middot; {BUYER_CITY}</div>
            <div class="xhit" data-tip="{TIP_BUY}">{buy}</div>
          </div>
          <div class="xmid">
            {mid}
          </div>
          <div class="xgr"><div class="xlab">Your {TEAM}&rsquo;s phone &middot; {TEAM_PLACE}</div>
            <div class="xhit" data-tip="{TIP_GR}">{gr}</div>
          </div>
        </div>
        {over}<div class="xcc on"><span></span></div>
        <div class="xhint">Hover anything to see what it does</div>
      </div>
      {bar}
      {sb}
      <div class="xtip" role="tooltip"></div>
    </div>
  </div>'''

def chapters(marks, fixed_before, fixed_after):
    """durations of every chapter: fixed ones around the director's"""
    return fixed_before + [b - a for a, b in zip(marks, marks[1:])] + fixed_after

def split(F, starts):
    """the director's captions → per-chapter, chapter-relative CC lists; minor ticks for the scrubber"""
    cc, minor = {}, []
    for t, html in F.C:
        n = max(i for i, s in enumerate(starts) if s <= t) + 1
        cc.setdefault(n, []).append([t - starts[n - 1], html]); minor.append(t)
    return cc, minor


# ═══ stage one ═══
F1 = Dir(6000)
F1.pg(0); F1.wait(300); F1.cap(*R_OPEN); F1.wait(1800)
for i in range(3): F1.question(i, f'q{i}', f'q{i}o{QS[i][2]}')
F1.sy('go1', 650, .5); F1.wait(750); F1.tap('go1'); F1.wait(220); F1.pg(1); F1.wait(650)
F1.mark()
for i in range(3, 6): F1.question(i, f'q{i}', f'q{i}o{QS[i][2]}')
F1.mark()
F1.details('')
F1.sy('go2', 650, .5); F1.wait(700); F1.tap('go2'); F1.wait(220); F1.pg(2); F1.wait(700)
F1.mark()
F1.codes('', 'go3')
F1.mark()
AFTER = [5600, 8800, 6600, 7200, 6200, 7600]      # alert · call · reminders · private call · her choice · the outcome (ends on the card)
DUR1 = chapters(F1.marks, [6000], AFTER)
START1 = [sum(DUR1[:i]) for i in range(len(DUR1))]
CC1, MINOR1 = split(F1, START1)
def cc(label, text): return f'<em>{label}</em>{text}'
L1 = 6                                                    # her answers land
CC1[1] = [[400, cc('The ad', 'The price is on the ad, so she enquires knowing it.')]]
CC1[6] = [[300, cc('Verified enquiry', f'Her answers land in your {CRM} and on your {TEAM}&rsquo;s phones the same minute.')]]
CC1[7] = [[300, cc('Within five minutes', 'Called within five minutes, she still remembers why she enquired.')],
          [3300, cc('On the call', f'The pack lands while you talk: prices in {CUR_PAIR}, photos, the {CLUB}.')],
          [5900, cc('Booked', f'A {MEETING_LONG} for tomorrow, in your calendar before you hang up.')]]
CC1[8] = [[300, cc('Reminders', 'In the morning and an hour before, so she turns up.')], [3500, cc('Missed it?', 'She rebooks herself from a text. Your team never chases.')]]
CC1[9] = [[300, cc(f'The {MEETING}', f'Your team walks her through the {UNIT}, the {SITE} and the {CLUB}.')],
          [4600, cc('Returns', 'Your team explains returns here, on the call. Never in an ad.')]]
CC1[10] = [[300, cc(f'Her {UNIT}', f'She chooses the {P1}, so your team can prepare the {OUTCOME_NOUN}.')]]
CC1[11] = [[300, cc(OUTCOME, f'She {OUTCOME_VERB}s with {DEV_SHORT}, and the sale is tracked back to the ad that found her.')]]
for k in range(6, 12): MINOR1 += [START1[k - 1] + c[0] for c in CC1[k][1:]]
MINOR1.sort()

ev1 = {k: [] for k in range(1, 12)}
lev, one_fields = land_events(L1)
ev1[6] += lev + [[2200, 'pk', 'R', f'Alert &middot; score {SCORE}', 0], [2800, 'bz']]
ev1[7] += [[300, 'pk', 'C', '&#9742; Your team calling', 0], [1500, 'pl', 1], [3400, 'pk', 'L', 'The pack &middot; prices + photos', 1], [6900, 'pl', 2], [7000, 'pk', 'L', f'Booked &middot; {DY[1]} {CALL_TIME}', 1]]
ev1[8] += [[200, 'pk', 'L', 'Confirmation', 1], [1000, 'pk', 'L', 'Reminder &middot; morning', 1], [1800, 'pk', 'L', 'Reminder &middot; 1 hour', 1], [2850, 'pk', 'R', 'She confirmed', 0]]
ev1[9] += [[300, 'pk', 'C', f'&#9654; {up1(MEETING_LONG)}', 0], [1200, 'pl', 3], [5900, 'pk', 'R', 'Logged &middot; ready to choose', 1]]
ev1[10] += [[600, 'pk', 'L', f'The {P1} &middot; prices', 1], [3500, 'pk', 'L', f'Her choice &middot; {P1}', 0], [3800, 'pl', 4], [4300, 'pk', 'R', STAGE_CHOSEN, 0]]
ev1[11] += [[300, 'pk', 'L', f'{up1(OUTCOME_NOUN)} confirmed', 1], [1400, 'pl', 5], [1600, 'pk', 'R', f'{OUTCOME} &middot; tracked to the ad', 0], [2300, 'bz']]
for k, cues in {1: [[0, 'cm', 'L']], 2: [[0, 'cm', 'L']], 3: [[0, 'cm', 'L']], 4: [[0, 'cm', 'L']], 5: [[0, 'cm', 'L']],
                6: [[0, 'cm', 'W'], [2200, 'cm', 'R']], 7: [[0, 'cm', 'W']], 8: [[0, 'cm', 'L']], 9: [[0, 'cm', 'L'], [3800, 'cm', 'R']],
                10: [[0, 'cm', 'L']], 11: [[0, 'cm', 'W']]}.items():
    ev1[k] = cues + ev1[k]
one_badges = [('&#10003; Mobile', L1, '1.6s', False), ('&#10003; Email', L1, '1.8s', False), ('Call first', L1, '2.0s', True)]
one_acts = [(CLOCK1[5], 'Enquiry received &middot; 6 answers', L1, '.4s'), (CLOCK1[5], 'Mobile + email verified by code', L1, '1.7s'), (CLOCK1[5], f'Alert sent to your {TEAM}', L1, '2.3s'),
            (CLOCK1[6], 'Call &middot; 6m 12s', 7, '1.5s'), (T_PACK, f'Pack sent &middot; prices, photos, {CLUB}', 7, '3.4s'), (T_CONFIRM, f'{up1(MEETING)} booked &middot; {DY[1]} {CALL_TIME}', 7, '6.9s'),
            (DY[1], 'Reminder &middot; the morning of', 8, '1s'), (DY[1], 'Reminder &middot; an hour before', 8, '1.8s'), (DY[1], f'{BUYER_FIRST} confirmed', 8, '2.85s'),
            (DY[1], f'{up1(MEETING)} &middot; {UNIT}, {SITE}, {CLUB}', 9, '5.9s'),
            (DY[2], f'{STAGE_CHOSEN} &middot; the {P1}', 10, '3.8s'),
            (DY[3], f'{OUTCOME} &middot; from the &ldquo;{lo1(AD_NAME)}&rdquo; ad', 11, '1.6s')]
def when1(i): return f'{DAY[CDAY1[i]]} &middot; {CLOCK1[i]}'   # stage one, chapter i+1: "Tuesday · 7:42pm"
def em_last(s):                                                  # 'private call' → 'private <em>call.</em>'
    a, _, b = s.rpartition(' ')
    return f'{a} <em>{b}.</em>' if a else f'<em>{b}.</em>'
one_caps = [(when1(0), 'She stops <em>scrolling.</em>'),
            (when1(1), 'Her answers, <em>one tap at a time.</em>'),
            (when1(2), f'Timing, funding, <em>and if she knows {PARTNER}.</em>'),
            (when1(3), 'Who she is, <em>and how to reach her.</em>'),
            (when1(4), 'Two codes. <em>She&rsquo;s real.</em>'),
            (when1(5), 'Your team&rsquo;s phones <em>light up.</em>'),
            (when1(6), 'You call. <em>You book.</em>'),
            (f'{DAY[0]} &rarr; {DAY[1]}', 'Reminded. <em>She turns up.</em>'),
            (when1(8), f'The {em_last(MEETING)}'),
            (when1(9), f'Her {UNIT}, <em>chosen.</em>'),
            (when1(10), f'{OUTCOME}, <em>and tracked to the ad.</em>')]
IDLE = 'Nothing for your team to do yet.'
STAT1 = [hm(t) for t in CLOCK1]
DAYS = [TUE, WED, THU, FRI]
g_one = [lock('g1', STAT1[0], TUE, idle=IDLE), lock('g2', STAT1[1], TUE, idle=IDLE), lock('g3', STAT1[2], TUE, idle=IDLE), lock('g4', STAT1[3], TUE, idle=IDLE), lock('g5', STAT1[4], TUE, idle=IDLE),
         lock('g6', STAT1[5], TUE, nf(f'New verified enquiry &middot; score {SCORE}', f'{BUYER} &middot; {BUYER_CITY} &middot; {P1} &middot; {lo1(ANS_BUDGET)} &middot; {lo1(ANS_WHEN_SHORT)}', 'now', '2.8s', 'Call first', [f'Call {BUYER_FIRST}', 'Open record'])),
         G_BOOK,
         lock('g8', STAT1[7], DAYS[CDAY1[7]], nf('Reminder sent &middot; the morning of', f'{BUYER} &middot; from your number, in your words', hm(T_REMIND), '1s')
              + nf('Reminder sent &middot; an hour before', f'Your {MEETING} with {BUYER_FIRST} at {CALL_TIME}', 'now', '1.8s') + nf(f'{BUYER_FIRST} confirmed', '&ldquo;See you then!&rdquo;', 'now', '3s')),
         G_PRIV,
         lock('g10', STAT1[9], DAYS[CDAY1[9]], nf(f'Sent to {BUYER_FIRST} &middot; the {P1}', f'Prices in {CUR_PAIR}, as promised on the call', 'now', '.9s')
              + nf(f'{BUYER_FIRST} chose her {UNIT}', f'The {P1} &middot; &ldquo;How do I {OUTCOME_VERB} it?&rdquo;', 'now', '3.9s', STAGE_CHOSEN, ['Reply', 'Open record'])),
         lock('g11', STAT1[10], DAYS[CDAY1[10]], nf(f'{OUTCOME} &middot; {BUYER}', f'The {P1} &middot; {OUTCOME.lower()} with {DEV_SHORT}', 'now', '1.7s', OUTCOME)
              + nf('Tracked to the ad that found her', f'Instagram &middot; &ldquo;{AD_NAME}&rdquo; &middot; {P1} ad set &middot; {BUYER_REGION}', 'now', '2.5s'))]
ENDONE = f'<div class="xend one" aria-hidden="true"><b>{OUTCOME} with {DEV_SHORT}, <em>and tracked back to the ad that found her.</em></b></div>'
CSBTN = '<button type="button" class="snk-pdf" data-pop="callscript">Open the call script &rarr;</button>'
ST1 = [('The ad', f'{DY[0]} {CLOCK1[0]}'), ('Q1&ndash;3', f'{up1(UNIT)} &middot; use &middot; budget'), ('Q4&ndash;6', f'When &middot; funding &middot; {PARTNER}'), ('Details', 'Name &middot; mobile &middot; email'),
       ('Codes', 'Mobile + email'), ('Alert', 'The same minute'), ('The call', f'Pack + {MEETING}'),
       ('Reminders', 'So she turns up'), (up1(MEETING), f'{up1(UNIT)} &middot; {SITE} &middot; {CLUB_SHORT}'), (f'Her {UNIT}', f'The {P1}'), (OUTCOME, 'Tracked to the ad')]
one = show('one', 'data-stage="1" data-rest="11" data-dur="' + json.dumps(DUR1) + '" data-ev=\'' + json.dumps(ev1) + '\' style="--n:' + str(len(DUR1)) + ';--c:6"',
           None,
           phone([FEED1, FORM, THANKS, CALL1, REMIND, PRIV, SUITE, RESERVED], STAT1),
           caps(one_caps) + '\n        ' + record(one_fields, one_badges, one_acts, 'Instagram &middot; buyer campaign', WAIT) + '\n        ' + CSBTN,
           gphone(g_one, STAT1),
           player(ST1, DUR1, MINOR1),
           storyboard(one_caps, ST1, CC1), CC1, F1.A, ENDONE)

# ═══ the next stage ═══
nxt = f'''  <div class="xnext rv">
    <h3 class="xn-h">Phase two &middot; <em>the film-first funnel.</em></h3>
    <p class="xn-p">Once we know which message wins, we script, film and edit a short {BRAND_SHORT} film. It plays before the questions, so buyers arrive warm and book their own {MEETING}.</p>
  </div>'''

# ═══ stage two: only what changes — the client's film, the same six questions on the page, she books herself ═══
F2 = Dir(4500)
F2.wait(300); F2.cap(None, 'Your film plays first, before she&rsquo;s asked for anything.'); F2.wait(4600)
F2.sy('lcta', 600, .52); F2.wait(700); F2.tap('lcta'); F2.wait(450)
F2.mark()
F2.cap('Same questions, same codes', 'The six questions and two codes, right under your film.')
F2.sy('sbrief', 600, .02); F2.wait(650)
for i in range(6):
    F2.sy(f'lq{i}', 380, .1); F2.wait(480); F2.tap(f'lq{i}o{QS[i][2]}'); F2.wait(240)
F2.sy('lfnw', 500, .05); F2.wait(550); F2.tap('lfn'); F2.wait(150); F2.kb('a'); F2.wait(250); F2.ty('lfn', BUYER, 38); F2.wait(150)
F2.sy('lfmw', 350, .05); F2.wait(450); F2.tap('lfm'); F2.kb('n'); F2.wait(200); F2.ty('lfm', MOB, 45, True); F2.wait(150)
F2.sy('lfew', 350, .05); F2.wait(450); F2.tap('lfe'); F2.kb('a'); F2.wait(200); F2.ty('lfe', EMAIL, 28); F2.wait(150); F2.kb(); F2.wait(200)
F2.sy('lck', 450, .25); F2.wait(550); F2.tap('lck'); F2.wait(300)
F2.sy('lcm', 450, .3); F2.nf('lnsms', 1500); F2.wait(700); F2.tap('lcm'); F2.kb('n'); F2.wait(250); F2.ty('lcm', CODE_MOB, 70); F2.on('lokm'); F2.wait(200)
F2.nf('lnmail', 1500); F2.wait(650); F2.tap('lce'); F2.wait(150); F2.ty('lce', CODE_EMAIL, 70); F2.on('loke'); F2.wait(200); F2.kb(); F2.wait(250)
F2.sy('lgo', 450, .35); F2.wait(600); F2.tap('lgo'); F2.wait(450)
F2.mark()
B0 = F2.t
F2.wait(300); F2.cap('She books herself', 'Your calendar shows only the times your team is free.'); F2.wait(-300)
F2.sy('scal', 800, .02); F2.wait(1500); F2.tap(f'cd{DATE[1]}'); F2.wait(800); F2.tap(f'ct{CALL_SLOT}'); F2.wait(600)
F2.sy('cgo', 500, .55); F2.wait(700); F2.cap('Booked', 'Straight into your calendar and onto your team&rsquo;s phones.'); F2.tap('cgo')
BOOK = F2.t - B0
F2.wait(350); F2.on('lok'); F2.sy('lok', 800, .2); F2.wait(2700)
F2.mark()
L2 = 4
DUR2 = chapters(F2.marks, [4500], [3800])
START2 = [sum(DUR2[:i]) for i in range(len(DUR2))]
CC2, MINOR2 = split(F2, START2)
CC2[1] = [[400, 'She taps Learn more, and your own page opens.']]
CC2[5] = []

ev2 = {k: [] for k in range(1, 6)}
ev2[2] += [[500, 'vd', 1]]
lev2, two_fields = land_events(L2)
ev2[4] += lev2 + [[BOOK + 300, 'pk', 'L', f'Booked &middot; {DY[1]} {CALL_TIME}', 0], [BOOK + 500, 'pl', 2], [BOOK + 1100, 'pk', 'R', 'New booking', 0], [BOOK + 1600, 'bz']]
for k, cues in {1: [[0, 'cm', 'L']], 2: [[0, 'cm', 'L']], 3: [[0, 'cm', 'L']], 4: [[0, 'cm', 'W'], [BOOK + 800, 'cm', 'R']], 5: [[0, 'cm', 'W']]}.items():
    ev2[k] = cues + ev2[k]
bk = f'{(BOOK + 300) / 1000:.2f}s'
two_badges = [('&#9654; Watched your film', L2, '.3s', True), ('&#10003; Mobile', L2, '1.6s', False), ('&#10003; Email', L2, '1.8s', False)]
two_acts = [(CLOCK2[1], 'Watched your film', L2, '.3s'), (T_SENT2, 'Enquiry received &middot; 6 answers', L2, '.4s'), (T_SENT2, 'Mobile + email verified', L2, '1.7s'),
            (CLOCK2[3], f'Booked herself &middot; {CALL_SHORT}', L2, bk)]
two_caps = [(f'{DAY[0]} &middot; {CLOCK2[0]}', 'Same ad. <em>A new next step.</em>'),
            (f'{DAY[0]} &middot; {CLOCK2[1]}', 'She watches <em>the film first.</em>'),
            (f'{DAY[0]} &middot; {CLOCK2[2]}', 'The same six questions, <em>on your page.</em>'),
            (f'{DAY[0]} &middot; {CLOCK2[3]}', 'She books <em>herself.</em>'),
            ('Then', 'From here, <em>the same as phase one.</em>')]
NEWB = (f'New booking &middot; {BUYER}', f'{CALL_SHORT} &middot; {P1} &middot; {lo1(ANS_BUDGET)} &middot; watched your film')
STAT2 = [hm(t) for t in CLOCK2]
g_two = [lock('g1', STAT2[0], TUE, idle=IDLE), lock('g2', STAT2[1], TUE, idle=IDLE), lock('g3', STAT2[2], TUE, idle=IDLE),
         lock('g4', STAT2[3], TUE, nf(*NEWB, 'now', f'{(BOOK + 1600) / 1000:.2f}s', f'Score {SCORE}', ['Open record'])),
         lock('g5', STAT2[4], TUE, nf(*NEWB, 'now', None, f'Score {SCORE}', ['Open record']))]
ENDCARD = '<div class="xend" aria-hidden="true"><b>From here, <em>the same as phase one.</em></b></div>'
ST2 = [('The ad', f'{DY[0]} {CLOCK2[0]}'), ('Your film', 'Plays first'), ('Questions', 'Plus codes, on your page'), ('She books', 'Your calendar'), ('Then', 'As phase one')]
two = show('two', 'data-stage="2" data-rest="4" data-dur="' + json.dumps(DUR2) + '" data-ev=\'' + json.dumps(ev2) + '\' style="--n:' + str(len(DUR2)) + ';--c:5"',
           None,
           phone([FEED2, LANDING], STAT2, big=True),
           caps(two_caps) + '\n        ' + record(two_fields, two_badges, two_acts, DOMAIN, WAIT),
           gphone(g_two, STAT2),
           player(ST2, DUR2, MINOR2),
           storyboard(two_caps, ST2, CC2), CC2, F2.A, ENDCARD)

CSS = open(os.path.join(HERE, 'how.css'), encoding='utf8').read()
html = f'''<section class="slide" id="how">
<style>
{CSS}
</style>
  <div class="wrap">
    <div class="head rv">
      <div class="k">Chapter two &middot; the strategy</div>
      <h2>The Verified Buyer <em>Funnel.</em></h2>
    </div>

{simple}

{one}

{nxt}

{two}

    <div class="note"><b>The Verified Buyer Funnel, start to finish</b>Start with the strip: one step, one reason, left to right. Then let stage one play, about {sum(DUR1) // 1000} seconds. It slows down through the form, then moves quickly from the enquiry to the {OUTCOME_NOUN}. Each caption answers a question {DEV_SHORT}&rsquo;s {TEAM} would ask at that moment, so read two or three aloud and let the rest play. When the first call starts, pause and open the call script: <b>&ldquo;your team calls within five minutes, sends the {BRAND_SHORT} pack while they talk, and books the {MEETING} for tomorrow.&rdquo;</b> On the codes: <b>&ldquo;no code, no enquiry. You never pay for a fake number.&rdquo;</b> On the {MEETING}: <b>&ldquo;your team explains returns here, on the call, never in an ad.&rdquo;</b> On the last step: <b>&ldquo;every {OUTCOME_NOUN} is tracked back to the ad that found the buyer, so we know which ads to fund.&rdquo;</b> Phase two shows only what changes: a short {BRAND_SHORT} film plays first, the same six questions sit under it, and the buyer books the {MEETING} themselves. <b>&ldquo;From there, it&rsquo;s the same as phase one.&rdquo;</b></div>
  </div>
</section>
'''
open(os.path.join(ROOT, 'src', 's13_how.html'), 'w', encoding='utf8').write(html)
print('journey written', len(html), 'stage one', DUR1, sum(DUR1), 'stage two', DUR2, sum(DUR2))
