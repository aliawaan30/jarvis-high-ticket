# Generates "The strategy on paper" slide (#paper): the 90-day marketing plan as eight A4 pages,
# laid out like a printed document set. Tap any page to read it full size (prev / next in the dialog).
# JS lives in src/js/paper.js. All classes are prefixed mkp- and scoped under #paper.
import os
HERE = os.path.dirname(os.path.abspath(__file__))

N = 8
PAGES = []   # (short tab label, title, body)

def add(tab, title, body):
    PAGES.append((tab, title, body))

def doc_in(n, title, body):
    return f'''<div class="mkp-in">
          <div class="mkp-top"><div><small>Prepared for Kestrel&nbsp;Developments&nbsp;&middot; Kestrel&nbsp;Bay&nbsp;Resort&nbsp;&middot; the&nbsp;90&#8209;day&nbsp;plan</small><b>{title}</b></div><img src="assets/brand-logo-dark.png" alt="Kestrel Bay Resort"></div>
          <i class="mkp-rule"></i>
          {body.replace('<h6>', '<i class="mkp-sp"></i><h6>')}
          <div class="mkp-foot"><span>Kestrel Bay Resort &middot; 90-day marketing plan</span><span>{n} / {N}</span></div>
        </div>'''

# Every number on these pages is from source/facts.md or the deal (A$4,000 a month, A$25, 160 / 480, A$24,000).
# No yields, no returns, no sold-out claims, no completion dates, no tenure, no payment plans.
# Anything the presenter must supply or verify is a ⟦…⟧ marker.

# ── 1 · Executive summary & objectives ──────────────────────────────────────────
add('Executive summary', 'Executive Summary &amp; Objectives', '''
          <p class="mkp-lede">Kestrel Bay Resort has a developer with 18 years behind it and an operator that already runs 12 venues. This plan covers one quarter: <b>one buyer campaign</b> that finds and verifies Australian buyers, a system that gets each one to your sales team the same minute, and a weekly rhythm that turns verified enquiries into private calls and reserved suites.</p>
          <h6>What Kestrel Bay Resort starts with</h6>
          <div class="mkp-quotes mkp-have">
            <span><b>An operator with guests already.</b>Tidewater venues see close to 900,000 guests a year, so the ads can name who runs the resort.</span>
            <span><b>A developer with a record.</b>Kestrel Developments: 18 years, 600+ units delivered and 9 developments.</span>
            <span><b>A resort that runs itself.</b>Tidewater Hospitality runs the resort day to day, so owners don&rsquo;t manage it themselves.</span>
            <span><b>Two clear prices.</b>The Garden Suite from US$165,000 and the Ocean Suite at US$260,000 &mdash; plus the Owners&rsquo; Club.</span>
          </div>
          <h6>Objectives for the quarter</h6>
          <table class="mkp-t2">
            <tr><td>Verified enquiries</td><td>About five a day, planned at A$25 each &mdash; 160 a month, 480 a quarter. Every one answers six questions and confirms mobile and email by code.</td></tr>
            <tr><td>Private calls</td><td>Every call-first buyer rung within five minutes and booked onto a private video call with your sales team.</td></tr>
            <tr><td>Reservations</td><td>Suites reserved with Kestrel &mdash; each one tracked in your CRM back to the ad that found the buyer.</td></tr>
            <tr><td>Speed</td><td>The buyer campaign live by day six. Once the winning message is proven, phase two: a short film and landing page.</td></tr>
          </table>
          <h6>The numbers we report every week</h6>
          <div class="mkp-kpis mkp-k6"><span><b>Cost</b>per verified enquiry</span><span><b>Booked</b>calls booked</span><span><b>Showed</b>show rate</span><span><b>Private</b>private calls held</span><span><b>Reserved</b>suites reserved</span><span><b>Value</b>sales per ad dollar</span></div>
          <h6>Your investment at a glance</h6>
          <div class="mkp-sum"><span><b>A$24,000</b>the quarter, all in &middot; paid on signing</span><span><b>A$12,000</b>our fee &middot; everything built and run</span><span><b>A$12,000</b>ad spend &middot; A$4,000 a month</span></div>''')

# ── 2 · Audience & positioning ─────────────────────────────────────────────────
WHO = [('The Tidewater regular', 'Holidays at Kestrel Bay, as an owner', 'Garden Suite &middot; around A$250k', 'Doesn&rsquo;t know who builds or runs the resort.'),
       ('The family', 'Room for everyone, every trip', 'Ocean Suite &middot; A$250k&ndash;A$400k', 'Not sure a one-bedroom suite fits a family.'),
       ('The income buyer', 'Rental income from a resort that is run for them', 'Either suite', 'Wants the numbers before anyone asks for a commitment.'),
       ('The owner-user', 'To use it, not just own it', 'Either suite', 'Not sure what owners actually get.'),
       ('The researcher', 'Time to decide', 'Not sure yet', 'Not ready for a call yet.')]
who = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in WHO)
add('Audience &amp; positioning', 'Audience &amp; Positioning', f'''
          <div class="mkp-pos"><small>Positioning</small><b>A suite at Kestrel Bay &mdash; built by Kestrel, run by Tidewater.</b><span>Two suites, two clear prices, and an owners&rsquo; membership.</span></div>
          <p>One development, so every ad, question and call is about Kestrel Bay Resort: the two suites, the Owners&rsquo; Club, and who is behind it. The ads give buyers the detail, and a reason to call.</p>
          <h6>Who we are talking to</h6>
          <p>Australians who holiday in Bali, with <b>around A$250k to A$400k+</b> to place &mdash; for rental income, holidays at the resort, or a bit of both. Five types lead:</p>
          <table class="mkp-t4"><tr><th>Buyer</th><th>What they want</th><th>Likely suite &middot; budget</th><th>What stops them</th></tr>{who}</table>
          <h6>Why Kestrel Bay, in four numbers</h6>
          <div class="mkp-facts"><span><b>Close to 900,000</b>guests a year across Tidewater&rsquo;s 12 venues</span><span><b>18</b>years &mdash; Kestrel, the developer</span><span><b>600+</b>units Kestrel has delivered</span><span><b>Up to US$15,000</b>what the Owners&rsquo; Club is valued at</span></div>
          <p class="mkp-src">Figures from Kestrel Developments&rsquo; own Kestrel Bay Resort and company pages, checked ⟦month and year you read them⟧.</p>
          <h6>Guardrails, on every ad</h6>
          <ul class="mkp-ul"><li>No promise of returns, yields or capital growth &mdash; your sales team explains projected returns on the call, on request.</li><li>No sold-out claims, and no area of Bali ranked against another.</li><li>Prices in US$, with A$ shown as &ldquo;about&rdquo;, so Australians can read them at a glance.</li><li>Every word approved by you before it runs.</li></ul>''')

# ── 3 · Meta campaign strategy ─────────────────────────────────────────────────
add('Meta campaign strategy', 'Meta Campaign Strategy', '''
          <h6>One campaign, four products, all always on</h6>
          <table class="mkp-t4"><tr><th>Product</th><th>What it sells</th><th>Price</th></tr>
            <tr><td>The Garden Suite</td><td>34 m&sup2;, one bedroom, garden terrace</td><td>From US$165,000 &middot; about A$240k</td></tr>
            <tr><td>The Ocean Suite</td><td>52 m&sup2;, balcony with daybed, ocean outlook</td><td>US$260,000 &middot; about A$375k</td></tr>
            <tr><td>The Owners&rsquo; Club</td><td>Resort stays, priority bookings, Tidewater member rates</td><td>Valued up to US$15,000</td></tr>
            <tr><td>Kestrel &times; Tidewater</td><td>Kestrel builds it (18 years); Tidewater runs it</td><td>&mdash;</td></tr></table>
          <h6>The buyer campaign &middot; 448 live ads</h6>
          <div class="mkp-eq"><span><b>4</b>products</span><i>&times;</i><span><b>7</b>locations</span><i>=</i><span><b>28</b>ad sets</span><i>&times;</i><span><b>16</b>ads each</span><i>=</i><span class="mkp-hl"><b>448</b>live ads</span></div>
          <p>Each ad set is its own audience, so we never bid against ourselves. Sixteen ads in each &mdash; four angles &times; four formats &mdash; and Meta backs the ones that bring verified enquiries.</p>
          <h6>Seven locations</h6>
          <table class="mkp-t2">
            <tr><td>WA</td><td>Perth &#8644; Denpasar flyers, Bali holiday-makers, families who travel to Bali.</td></tr>
            <tr><td>NSW &middot; VIC</td><td>Sydney and Melbourne Bali travellers, property and finance readers, people researching buying overseas.</td></tr>
            <tr><td>QLD</td><td>Brisbane Bali travellers, holiday-home owners, families who travel to Bali.</td></tr>
            <tr><td>SA</td><td>Adelaide Bali travellers and investment-property owners.</td></tr>
            <tr><td>ACT &middot; TAS &middot; NT</td><td>Darwin, Canberra and Hobart Bali travellers and early researchers.</td></tr>
            <tr><td>Retargeting</td><td>Watched a video, opened the form, engaged with Kestrel Bay Resort &mdash; shown the ads for buyers still deciding.</td></tr></table>
          <p>Every state also targets interest in Tidewater venues, and lookalikes of your own verified enquirers as they come in.</p>
          <h6>Budget &amp; pace</h6>
          <div class="mkp-eq"><span><b>A$4,000</b>ad spend a month</span><i>&divide;</i><span><b>A$25</b>planned per verified enquiry</span><i>=</i><span><b>160</b>a month</span><i>&times;</i><span><b>3</b>months</span><i>=</i><span class="mkp-hl"><b>480</b>a quarter</span></div>
          <p><b>About A$133 a day, A$12,000 for the quarter</b> &mdash; included in the A$24,000. Meta tests every ad and budget follows the winners; each week we move it to what is producing. As calls and reservations are logged in your CRM, they feed back to Meta, so it looks for more people like your real buyers.</p>''')

# ── 4 · Creative plan ──────────────────────────────────────────────────────────
add('Creative plan', 'Creative Plan', '''
          <h6>Four angles, in every ad set</h6>
          <table class="mkp-t4"><tr><th>Angle</th><th>What it says</th><th>Example line</th></tr>
            <tr><td>1 &middot; Own a suite at Kestrel Bay</td><td>The suite, the price, the resort.</td><td>&ldquo;Own a suite at Kestrel Bay Resort. From US$165,000.&rdquo;</td></tr>
            <tr><td>2 &middot; The doubts that stop a sale</td><td>Who builds it, who runs it, what it costs in A$.</td><td>&ldquo;Who runs it while you&rsquo;re home? Tidewater does.&rdquo;</td></tr>
            <tr><td>3 &middot; The owners&rsquo; membership</td><td>Resort stays, priority bookings, member rates across Tidewater venues.</td><td>&ldquo;Suite owners join the Owners&rsquo; Club.&rdquo;</td></tr>
            <tr><td>4 &middot; For buyers still deciding</td><td>Compare the suites, ask a question, book a private call.</td><td>&ldquo;Compare both suites on a private call.&rdquo;</td></tr></table>
          <h6>Four formats, in every ad set</h6>
          <table class="mkp-t2">
            <tr><td>Photo</td><td>Designed statics &mdash; headline, price, feature strip and logo composed on the image.</td></tr>
            <tr><td>Carousel</td><td>Swipe-through cards: the suites, the steps, a question and its answer.</td></tr>
            <tr><td>Short video</td><td>Motion ads cut from Kestrel Bay renders and photos &mdash; captioned, so they work with the sound off.</td></tr>
            <tr><td>Story</td><td>Full-screen vertical, with a poll, a question or a location sticker.</td></tr></table>
          <p>Four angles &times; four formats = sixteen ads per ad set, no two alike: <b>64 designs across the four products, 448 live ads</b> across the seven locations.</p>
          <h6>New designs every month</h6>
          <p>Meta shows which ads bring verified enquiries. Every month the weakest designs are replaced with new ones built on what is working. If new suites are released, their ads are live within five business days.</p>
          <h6>Photos and words</h6>
          <ul class="mkp-ul"><li>Only Kestrel Bay Resort&rsquo;s own renders and photos &mdash; never generic stock for a claim about the resort.</li><li>Every number from your own materials; prices in US$, with A$ shown as &ldquo;about&rdquo;.</li><li>Every ad, question and message approved by you before it runs.</li></ul>
          <h6>Compliance</h6>
          <ul class="mkp-ul"><li>No promise of returns, yields or capital growth in any ad &mdash; Meta&rsquo;s financial-claims rules, and your own site lists projected returns as &ldquo;on request&rdquo;.</li><li>No sold-out claims, and no area-against-area comparisons.</li><li>Returns are explained by your sales team, on the private call.</li></ul>''')

# ── 5 · Funnel & lead qualification ────────────────────────────────────────────
Q = [('Which suite?', 'Garden Suite &middot; from US$165k / Ocean Suite &middot; US$260k / Not sure yet'),
     ('What&rsquo;s it for?', 'Rental income / Holidays / A bit of both'),
     ('Budget (AUD)?', 'Around A$250k / A$250k&ndash;A$400k / A$400k+'),
     ('When are you looking to buy?', 'In the next 3 months / 3&ndash;6 months / Just researching'),
     ('How would you fund it?', 'Savings or equity, ready / Arranging finance / Selling something first'),
     ('Have you stayed at a Tidewater venue?', 'Many times / Once or twice / Not yet')]
qs = ''.join(f'<tr><td>{i}</td><td>{a}</td><td>{b}</td></tr>' for i, (a, b) in enumerate(Q, 1))
add('Funnel &amp; qualification', 'Funnel &amp; Lead Qualification', f'''
          <h6>The Verified Buyer Funnel &middot; live by day six</h6>
          <div class="mkp-flow"><span>Meta ad</span><i></i><span>Instant form &middot; six questions</span><i></i><span>Mobile + email codes</span><i></i><span>Verified enquiry</span><i></i><span>Alert to your sales team</span><i></i><span>Private call booked</span></div>
          <h6>The six questions</h6>
          <table class="mkp-t5 mkp-q"><tr><th>#</th><th>Question</th><th>Answers</th></tr>{qs}</table>
          <p>Name, mobile and email are prefilled by Meta and confirmed by the buyer, with consent. Then a code to the mobile <i>and</i> a code to the email &mdash; <b>no code, no enquiry.</b> It gives fewer enquiries than an open form, and every one is a real, reachable buyer.</p>
          <h6>The lead score</h6>
          <table class="mkp-t3"><tr><th>Score out of 100</th><th>Call first</th><th>Nurture bank</th></tr>
            <tr><td>Built from the six answers &mdash; timing, funding and budget weigh most.</td><td>Ready to move &mdash; rung within five minutes and booked onto a private call.</td><td>Just researching &mdash; kept in the nurture bank and followed up until they&rsquo;re ready.</td></tr></table>
          <p>Example from the demo: Sarah Mitchell, Perth &mdash; Garden Suite, a bit of both, around A$250k, the next 3 months, savings ready, stayed at a Tidewater venue many times. <b>Score 88 &mdash; rung first.</b></p>
          <h6>Phase two &middot; the film-first funnel</h6>
          <div class="mkp-flow"><span>Meta ad</span><i></i><span>Landing page</span><i></i><span>Short film</span><i></i><span>Six questions + codes</span><i></i><span>They book themselves</span></div>
          <p>Once the winning message is proven, we script, film and edit a short film and build the landing page, so buyers watch first and book a private call themselves. The Verified Buyer Funnel keeps running alongside it.</p>''')

# ── 6 · CRM, automation & sales process ────────────────────────────────────────
AUTO = [('Verified enquiry', 'A confirmation to the buyer straight away, from your accounts.'),
        ('Same minute', 'A phone alert to your sales team &mdash; the six answers, the score, one tap to call.'),
        ('0&ndash;5 min', 'Every call-first buyer rung within five minutes.'),
        ('No answer', 'Follow-up texts, emails and calls, sent from your accounts in your words.'),
        ('Booked', 'The private video call lands in your sales team&rsquo;s calendar, with a confirmation to the buyer.'),
        ('Before the call', 'Reminders, so they show.'),
        ('Just looking', 'Kept in the nurture bank and followed up until they&rsquo;re ready.')]
auto = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in AUTO)
STG = ['Verified', 'Called', 'Booked', 'Private call', 'Suite chosen', 'Reserved']
stg = '<i></i>'.join(f'<span><b>{i}</b>{s}</span>' for i, s in enumerate(STG, 1))
add('CRM &amp; sales process', 'CRM, Automation &amp; Sales Process', f'''
          <p>Your CRM, the one your team already uses. We connect the campaign to it, so every enquiry arrives as a lead with all six answers, the score and the ad it came from. Every message goes <b>from your accounts, in your words</b> &mdash; never from ours.</p>
          <h6>The pipeline &middot; six stages, enquiry to reservation</h6>
          <div class="mkp-stg">{stg}</div>
          <h6>Routing &amp; follow-up</h6>
          <table class="mkp-t2">{auto}</table>
          <h6>The sales process</h6>
          <table class="mkp-t4"><tr><th>Step</th><th>What happens</th></tr>
            <tr><td>Speed to lead</td><td>Call-first buyers rung within five minutes, while they&rsquo;re still keen.</td></tr>
            <tr><td>Our call script</td><td>Confirm the six answers, send the Kestrel Bay pack, book the private call. On screen for every call.</td></tr>
            <tr><td>Private video call</td><td>Your sales team walks them through the suite, the Owners&rsquo; Club and the numbers &mdash; projected returns are explained here, on request.</td></tr>
            <tr><td>Reservation</td><td>The buyer chooses a suite and reserves it with Kestrel. Every stage is logged in your CRM.</td></tr></table>
          <h6>Training</h6>
          <p>Our call script, plus training calls with your sales team &mdash; we listen, coach and role-play until everyone books the same way. Bali is on Perth time, so your team calls Australians during their day.</p>''')

# ── 7 · Measurement & optimisation ─────────────────────────────────────────────
add('Measurement', 'Measurement &amp; Optimisation', '''
          <h6>The KPIs, top to bottom</h6>
          <div class="mkp-casc"><span><b>Spend</b>A$133 a day</span><i></i><span><b>Verified</b>A$25 planned</span><i></i><span><b>Booked</b>calls booked</span><i></i><span><b>Showed</b>show rate</span><i></i><span><b>Private</b>calls held</span><i></i><span><b>Reserved</b>suites</span><i></i><span><b>Value</b>sales per ad dollar</span></div>
          <p>Every dollar is traced through each step. If one step falls short, we fix that step &mdash; not the ones around it.</p>
          <h6>The weekly rhythm</h6>
          <table class="mkp-t3"><tr><th>Every week &middot; the report</th><th>Every week &middot; 20-minute review</th><th>Every month &middot; 30-minute Zoom</th></tr>
            <tr><td>A one-page report in your inbox, in plain English &mdash; the numbers below, what we changed and what&rsquo;s next.</td><td>We go through the numbers with your sales team: what moved, which calls became private calls, what to fix.</td><td>What worked, what we cut, what we scale &mdash; and the new designs going in.</td></tr></table>
          <h6>The weekly report</h6>
          <div class="mkp-pills"><span>Ad spend</span><span>Verified enquiries</span><span>Cost per verified enquiry</span><span>Calls booked</span><span>Show rate</span><span>Private calls</span><span>Reservations</span><span>Sales value per ad dollar</span><span>Best state &amp; angle</span><span>What we changed</span><span>What&rsquo;s next</span></div>
          <h6>The reviews</h6>
          <table class="mkp-t2">
            <tr><td>Day 30</td><td>The first full read: cost per verified enquiry, calls booked and show rate.</td></tr>
            <tr><td>Day 60</td><td>Budget concentrated on the winning states and angles; calls and reservations feeding back to Meta.</td></tr>
            <tr><td>Day 90</td><td>The numbers that show what the next quarter should cost, and where to push.</td></tr></table>
          <h6>The 90-day ramp</h6>
          <table class="mkp-t4"><tr><th></th><th>Weeks 1&ndash;4 &middot; learn</th><th>Weeks 5&ndash;8 &middot; scale</th><th>Weeks 9&ndash;13 &middot; compound</th></tr>
            <tr><td>Media</td><td>Broad tests, every state, all four products.</td><td>Budget on the winning states and angles.</td><td>Winners run; new designs every month.</td></tr>
            <tr><td>Sales loop</td><td>Lead quality fed back from your calls.</td><td>Calls and private calls fed back to Meta.</td><td>Reservations reported against the ad.</td></tr></table>''')

# ── 8 · 90-day timeline & responsibilities ─────────────────────────────────────
TL = [('Today', 'Agreement signed and paid; onboarding call booked.'),
      ('Onboarding', 'Access to your page, Instagram and ad account; your CRM connected and the pipeline stages set; the six questions signed off; the Kestrel Bay pack set up for Australians.'),
      ('Days 1&ndash;6', 'Every ad, question and message approved by you &mdash; the buyer campaign <b>live by day six.</b>'),
      ('Weeks 1&ndash;4', 'Training calls with your sales team on the script; the weekly report and 20-minute review begin.'),
      ('Day 30', 'The first full read, the first monthly Zoom and the first new designs.'),
      ('Weeks 5&ndash;8', 'Scale what works. Once the winning message is proven: <b>phase two</b> &mdash; the short film and landing page, scripted, filmed and edited by us.'),
      ('Weeks 9&ndash;13', 'Winners run, new designs monthly. <b>The day-90 review</b> and the plan for the next quarter.')]
tl = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in TL)
add('Timeline &amp; responsibilities', '90-Day Timeline &amp; Responsibilities', f'''
          <h6>Week by week</h6>
          <table class="mkp-t2 mkp-tl">{tl}</table>
          <h6>Who does what</h6>
          <div class="mkp-who">
            <div><small>We build and run</small><ul class="mkp-ul"><li>The buyer campaign: 448 ads, new designs monthly, retargeting</li><li>The six-question form, two-code verification and routing</li><li>The connection to your CRM and the pipeline, phone alerts, follow-ups, booking and reminders</li><li>The Kestrel Bay pack for Australians, in A$ and US$</li><li>Our call script, training calls, the weekly report and reviews</li><li>Phase two: the short film and landing page</li></ul></div>
            <div><small>Your sales team</small><ul class="mkp-ul"><li>Approve every ad and message before it runs</li><li>Call every call-first buyer within five minutes</li><li>Run the private video calls</li><li>Log every call and outcome in your CRM</li><li>Take reservations with Kestrel</li><li>Join the 20-minute weekly review</li></ul></div>
          </div>
          <div class="mkp-g"><small>Where we stop</small><b>We deliver the verified enquiry, the system and the training. Your sales team makes the calls and the sales.</b>
            <span>One quarter &middot; A$24,000 all in &mdash; A$12,000 our fee + A$12,000 ad spend &middot; paid on signing.</span></div>''')

assert len(PAGES) == N

thumbs = ''.join(f'''
      <div class="mkp-card" style="--i:{i}">
        <span class="mkp-tab"><b>{i+1:02d}</b>{tab}</span>
        <div class="mkp-doc" data-doc="{i}" role="button" tabindex="0" aria-label="Open page {i+1} of {N}: {tab}">
          {doc_in(i+1, title, body)}
        </div>
      </div>''' for i, (tab, title, body) in enumerate(PAGES))

dtabs = ''.join(f'<button type="button" data-go="{i}"><b>{i+1}</b><span>{tab}</span></button>' for i, (tab, _, _) in enumerate(PAGES))

# print copies: two legible pages per A4 landscape sheet
spreads = ''.join('<div class="mkp-spread">' + ''.join(f'<div class="mkp-pg">{doc_in(j+1, PAGES[j][1], PAGES[j][2])}</div>' for j in (i, i+1)) + '</div>' for i in range(0, N, 2))

CSS = '''<style>
  #paper .wrap { max-width:1240px; }
  #paper .mkp-desk { position:relative; padding:40px 34px 30px; background:radial-gradient(120% 90% at 50% 0%,#EFE8DC,#E1D7C7 70%,#D9CDBA); border-radius:24px; box-shadow:inset 0 1px 0 rgba(255,255,255,.55); }
  #paper .mkp-grid { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:40px 26px; }
  #paper .mkp-card { position:relative; min-width:0; }
  #paper .mkp-tab { position:absolute; left:10px; top:-21px; height:24px; max-width:calc(100% - 20px); display:flex; align-items:center; gap:7px; padding:0 11px 3px 9px; border-radius:8px 8px 0 0; background:#13283A; color:#F4EFE7; font:600 10.5px/1 'Jost',sans-serif; letter-spacing:.06em; text-transform:uppercase; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; z-index:0; }
  #paper .mkp-tab b { font-family:'Playfair',serif; font-weight:500; font-size:13px; letter-spacing:0; color:#E2B872; }
  #paper .mkp-card:nth-child(even) .mkp-tab { background:#9A6420; }
  #paper .mkp-card:nth-child(even) .mkp-tab b { color:#FCFAF6; }
  #paper .mkp-doc { position:relative; z-index:1; aspect-ratio:1/1.4133; background:#FFFDFA; border-radius:3px; box-shadow:0 1px 2px rgba(19,40,58,.12), 0 16px 34px rgba(19,40,58,.18); cursor:pointer; overflow:hidden; transition:transform .25s ease, box-shadow .25s ease; outline-offset:3px; }
  #paper .mkp-doc:hover, #paper .mkp-doc:focus-visible { transform:translateY(-5px) rotate(-.4deg); box-shadow:0 2px 4px rgba(19,40,58,.12), 0 26px 50px rgba(19,40,58,.26); }
  #paper .mkp-doc::after { content:'Tap to read'; position:absolute; right:10px; bottom:10px; z-index:2; padding:5px 10px 4px; border-radius:20px; background:#13283A; color:#E2B872; font:600 10px/1 'Jost',sans-serif; letter-spacing:.12em; text-transform:uppercase; opacity:0; transform:translateY(4px); transition:.2s; }
  #paper .mkp-doc:hover::after, #paper .mkp-doc:focus-visible::after { opacity:1; transform:none; }
  #paper .mkp-doc > .mkp-in { position:absolute; left:0; top:0; transform-origin:0 0; transform:scale(var(--mkp-s,.45)); }
  /* the page itself — fixed 600 × 848 artboard */
  #paper .mkp-in { width:600px; height:848px; padding:36px 40px 26px; font-family:'Jost',sans-serif; color:#2A2521; display:flex; flex-direction:column; background:#FFFDFA; text-align:left; }
  #paper .mkp-top { display:flex; justify-content:space-between; align-items:flex-start; gap:20px; }
  #paper .mkp-top small { display:block; font-size:8.5px; letter-spacing:.2em; text-transform:uppercase; font-weight:700; color:#9A6420; text-wrap:balance; }
  #paper .mkp-top b { display:block; font-family:'Playfair',serif; font-weight:500; font-size:26px; line-height:1.15; color:#13283A; margin-top:6px; }
  #paper .mkp-top img { width:80px; height:auto; flex:none; margin-top:-2px; }
  #paper .mkp-sp { display:block; flex:1 1 0; max-height:16px; }
  #paper .mkp-rule { display:block; height:2px; width:60px; background:#B57A2E; margin:12px 0 4px; }
  #paper .mkp-in h6 { font-family:'Playfair',serif; font-weight:500; font-size:14.5px; color:#13283A; margin:13px 0 0; }
  #paper .mkp-in p { font-size:10.5px; line-height:1.5; color:#4A443E; margin:4px 0 0; }
  #paper .mkp-in p b { color:#13283A; }
  #paper .mkp-in .mkp-lede { font-size:12px; line-height:1.5; margin-top:8px; }
  #paper .mkp-in table { width:100%; border-collapse:collapse; margin-top:6px; font-size:9.5px; line-height:1.38; }
  #paper .mkp-in th { background:#13283A; color:#E2B872; font-size:8.5px; letter-spacing:.08em; text-transform:uppercase; font-weight:700; text-align:left; padding:5px 6px; }
  #paper .mkp-in td { border-bottom:1px solid #E6E0D7; padding:4.5px 6px; vertical-align:top; color:#4A443E; }
  #paper .mkp-in .mkp-t2 td:first-child, #paper .mkp-in .mkp-t4 td:first-child { font-weight:700; color:#13283A; white-space:nowrap; }
  #paper .mkp-in .mkp-t2 td:first-child { width:1%; padding-right:14px; }
  #paper .mkp-in .mkp-t5 td { padding:3.5px 6px; }
  #paper .mkp-in .mkp-q td:first-child { font-weight:700; color:#9A6420; width:1%; }
  #paper .mkp-in .mkp-q td:nth-child(2) { font-weight:600; color:#13283A; white-space:nowrap; }
  #paper .mkp-in .mkp-t3 th, #paper .mkp-in .mkp-t3 td { width:33.3%; }
  #paper .mkp-in .mkp-tl td:first-child { color:#9A6420; }
  #paper .mkp-quotes { display:grid; grid-template-columns:1fr 1fr; gap:6px; margin-top:6px; }
  #paper .mkp-quotes span { border-left:2px solid #B57A2E; background:#FBF8F3; padding:7px 10px; font-family:'Playfair',serif; font-size:11.5px; line-height:1.4; color:#13283A; font-style:italic; }
  /* four facts about the client (not quotes) — plain type, bold lead-in */
  #paper .mkp-quotes.mkp-have span { font-family:'Jost',sans-serif; font-style:normal; font-size:10px; line-height:1.45; color:#4A443E; }
  #paper .mkp-quotes.mkp-have b { display:block; font-family:'Playfair',serif; font-weight:500; font-size:12.5px; color:#13283A; margin-bottom:2px; }
  #paper .mkp-in .mkp-src { font-size:8.5px; line-height:1.4; color:#8C8173; margin-top:5px; }
  #paper .mkp-kpis, #paper .mkp-sum, #paper .mkp-facts { display:grid; grid-template-columns:repeat(5,1fr); gap:5px; margin-top:6px; }
  #paper .mkp-sum { grid-template-columns:1.1fr 1fr 1fr; }
  #paper .mkp-kpis.mkp-k6 { grid-template-columns:repeat(6,1fr); }
  #paper .mkp-facts { grid-template-columns:1fr 1fr; }
  #paper .mkp-kpis span, #paper .mkp-casc span, #paper .mkp-sum span, #paper .mkp-facts span, #paper .mkp-eq span, #paper .mkp-stg span { border:1px solid #E6E0D7; border-radius:4px; padding:6px 5px; text-align:center; font-size:8.5px; line-height:1.3; color:#6B645C; background:#FBF8F3; }
  #paper .mkp-kpis b, #paper .mkp-casc b, #paper .mkp-sum b, #paper .mkp-facts b, #paper .mkp-eq b { display:block; font-family:'Playfair',serif; font-weight:500; font-size:14px; color:#13283A; }
  #paper .mkp-sum span:first-child { background:#13283A; border-color:#13283A; color:#E2B872; }
  #paper .mkp-sum span:first-child b { color:#FCFAF6; font-size:17px; }
  #paper .mkp-facts span { text-align:left; padding:7px 9px; display:flex; gap:9px; align-items:center; }
  #paper .mkp-facts b { font-size:19px; color:#9A6420; flex:none; }
  #paper .mkp-pos { margin-top:8px; padding:12px 16px; border-radius:6px; background:#13283A; color:#F4EFE7; }
  #paper .mkp-pos small { display:block; font-size:8px; letter-spacing:.2em; text-transform:uppercase; font-weight:700; color:#E2B872; }
  #paper .mkp-pos b { display:block; font-family:'Playfair',serif; font-weight:500; font-size:18px; line-height:1.25; margin-top:4px; }
  #paper .mkp-pos span { display:block; font-size:10.5px; margin-top:3px; color:#E2B872; font-style:italic; }
  #paper .mkp-ul { margin:5px 0 0; padding:0 0 0 14px; font-size:10px; line-height:1.5; color:#4A443E; }
  #paper .mkp-ul li { margin:1px 0; }
  #paper .mkp-ul li::marker { color:#B57A2E; }
  #paper .mkp-pills { display:flex; flex-wrap:wrap; gap:4px; margin-top:6px; }
  #paper .mkp-pills span { font-size:8.5px; letter-spacing:.08em; text-transform:uppercase; font-weight:700; color:#13283A; background:#F4EFE7; border:1px solid #E6E0D7; border-radius:10px; padding:4px 8px 3px; }
  #paper .mkp-eq { display:flex; align-items:center; gap:5px; margin-top:6px; }
  #paper .mkp-eq span { flex:1; padding:5px 3px; }
  #paper .mkp-eq i { font-style:normal; color:#B57A2E; font-weight:700; font-size:13px; }
  #paper .mkp-eq .mkp-hl { background:#13283A; border-color:#13283A; color:#E2B872; }
  #paper .mkp-eq .mkp-hl b { color:#FCFAF6; }
  #paper .mkp-casc, #paper .mkp-flow, #paper .mkp-stg { display:flex; align-items:center; gap:3px; margin-top:6px; }
  #paper .mkp-casc span { flex:1; padding:6px 2px; }
  #paper .mkp-casc > i, #paper .mkp-flow > i, #paper .mkp-stg > i { flex:none; width:0; height:0; border-left:5px solid #B57A2E; border-top:4px solid transparent; border-bottom:4px solid transparent; }
  #paper .mkp-flow span { flex:1; align-self:stretch; display:flex; align-items:center; justify-content:center; text-align:center; padding:6px 4px; border-radius:4px; background:#F4EFE7; border:1px solid #E6E0D7; font-size:8.8px; line-height:1.25; font-weight:600; color:#13283A; }
  #paper .mkp-flow span:last-child { background:#13283A; color:#E2B872; border-color:#13283A; }
  #paper .mkp-stg span { flex:1; padding:5px 2px; font-size:8px; font-weight:600; color:#13283A; }
  #paper .mkp-stg b { display:block; font-family:'Playfair',serif; font-weight:500; font-size:12px; color:#9A6420; }
  #paper .mkp-stg span:last-child { background:#13283A; color:#E2B872; border-color:#13283A; }
  #paper .mkp-stg span:last-child b { color:#FCFAF6; }
  #paper .mkp-who { display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-top:6px; }
  #paper .mkp-who > div { border:1px solid #E6E0D7; border-radius:5px; padding:8px 10px; background:#FBF8F3; }
  #paper .mkp-who small, #paper .mkp-g small { display:block; font-size:8px; letter-spacing:.18em; text-transform:uppercase; font-weight:700; color:#9A6420; }
  #paper .mkp-g { margin-top:12px; padding:12px 16px; border-radius:6px; background:#13283A; color:#F4EFE7; }
  #paper .mkp-g small { color:#E2B872; }
  #paper .mkp-g b { display:block; font-family:'Playfair',serif; font-weight:500; font-size:15px; line-height:1.3; margin-top:4px; }
  #paper .mkp-g span { display:block; font-size:10px; margin-top:3px; color:#E2B872; }
  #paper .mkp-g .mkp-ul { color:#E9E1D4; columns:2; column-gap:18px; }
  #paper .mkp-g em { display:block; font-size:8.5px; color:#A89A88; margin-top:4px; }
  #paper .mkp-foot { margin-top:auto; padding-top:9px; border-top:1px solid #E6E0D7; display:flex; justify-content:space-between; font-size:7.5px; letter-spacing:.16em; text-transform:uppercase; color:#8C8173; }
  #paper .mkp-foot span:last-child { font-weight:700; color:#13283A; letter-spacing:.1em; }
  #paper .mkp-legend { display:flex; justify-content:center; gap:10px 22px; flex-wrap:wrap; margin-top:18px; font-size:12.5px; color:var(--soft); }
  #paper .mkp-legend b { color:var(--ink); }
  /* deal-in: pages start stacked, then fan out to the grid */
  #paper .mkp-card { transition:transform .8s cubic-bezier(.2,.8,.2,1), opacity .5s ease; transition-delay:calc(var(--i) * 70ms); }
  /* dialog */
  #paper .mkp-dlg { position:fixed; inset:0; z-index:1000; display:none; flex-direction:column; align-items:center; background:rgba(20,16,13,.82); -webkit-backdrop-filter:blur(3px); backdrop-filter:blur(3px); }
  #paper .mkp-dlg.on { display:flex; }
  #paper .mkp-bar { flex:none; width:100%; display:flex; align-items:center; gap:10px; padding:10px 14px; color:#F4EFE7; }
  #paper .mkp-dtabs { flex:1; min-width:0; display:flex; gap:4px; overflow-x:auto; scrollbar-width:none; }
  #paper .mkp-dtabs::-webkit-scrollbar { display:none; }
  #paper .mkp-dtabs button { flex:none; display:flex; align-items:center; gap:6px; border:1px solid rgba(226,184,114,.3); background:transparent; color:#D8CFC2; border-radius:16px; padding:5px 11px 4px; font:600 11px/1 'Jost',sans-serif; letter-spacing:.05em; text-transform:uppercase; cursor:pointer; }
  #paper .mkp-dtabs button b { font-family:'Playfair',serif; font-size:13px; color:#E2B872; }
  #paper .mkp-dtabs button.on { background:#E2B872; color:#13283A; border-color:#E2B872; }
  #paper .mkp-dtabs button.on b { color:#13283A; }
  #paper .mkp-x { flex:none; width:36px; height:36px; border-radius:50%; border:0; background:#E2B872; color:#13283A; font-size:20px; line-height:1; cursor:pointer; }
  #paper .mkp-stage { flex:1; min-height:0; width:100%; display:flex; align-items:flex-start; justify-content:center; gap:14px; padding:4px 14px 18px; overflow:auto; }
  #paper .mkp-view { flex:none; position:relative; background:#FFFDFA; border-radius:3px; box-shadow:0 30px 80px rgba(0,0,0,.5); overflow:hidden; }
  #paper .mkp-view > .mkp-in { transform-origin:0 0; }
  #paper .mkp-nav { flex:none; align-self:center; width:46px; height:46px; border-radius:50%; border:1px solid rgba(226,184,114,.5); background:rgba(19,40,58,.6); color:#E2B872; font-size:22px; cursor:pointer; }
  #paper .mkp-nav:disabled { opacity:.25; cursor:default; }
  #paper .mkp-print { display:none; }
  @media screen and (max-width:1100px){ #paper .mkp-grid { gap:38px 18px; } #paper .mkp-tab { font-size:9.5px; } }
  @media screen and (max-width:900px){ #paper .mkp-grid { grid-template-columns:repeat(2,minmax(0,1fr)); max-width:560px; margin:0 auto; gap:36px 16px; } #paper .mkp-desk { padding:34px 16px 22px; } }
  @media screen and (max-width:520px){
    #paper .mkp-desk { padding:30px 10px 18px; border-radius:16px; } #paper .mkp-grid { gap:32px 10px; }
    #paper .mkp-tab { left:4px; max-width:calc(100% - 8px); font-size:8.5px; padding:0 7px 3px 6px; gap:4px; letter-spacing:.03em; }
    #paper .mkp-tab b { font-size:11px; }
    #paper .mkp-legend { display:none; }
    /* phone reading mode: the page reflows instead of shrinking */
    #paper .mkp-stage { padding:0 8px 16px; display:block; }
    #paper .mkp-nav { display:none; }
    #paper .mkp-view { width:100% !important; height:auto !important; }
    #paper .mkp-view > .mkp-in { transform:none !important; width:100%; height:auto; padding:22px 16px 16px; }
    #paper .mkp-view .mkp-top b { font-size:21px; } #paper .mkp-view .mkp-top img { width:62px; }
    #paper .mkp-view .mkp-in p, #paper .mkp-view .mkp-ul { font-size:12.5px; }
    #paper .mkp-view table { font-size:11px; } #paper .mkp-view .mkp-q td:nth-child(2) { white-space:normal; }
    #paper .mkp-view .mkp-t2 td:first-child, #paper .mkp-view .mkp-t4 td:first-child { white-space:normal; }
    #paper .mkp-view .mkp-quotes, #paper .mkp-view .mkp-who, #paper .mkp-view .mkp-facts { grid-template-columns:1fr; }
    #paper .mkp-view .mkp-kpis { grid-template-columns:repeat(3,1fr); }
    #paper .mkp-view .mkp-casc, #paper .mkp-view .mkp-flow, #paper .mkp-view .mkp-stg, #paper .mkp-view .mkp-eq { flex-wrap:wrap; }
    #paper .mkp-view .mkp-casc span, #paper .mkp-view .mkp-flow span, #paper .mkp-view .mkp-stg span, #paper .mkp-view .mkp-eq span { flex:1 1 28%; }
    #paper .mkp-view .mkp-casc > i, #paper .mkp-view .mkp-flow > i, #paper .mkp-view .mkp-stg > i, #paper .mkp-view .mkp-eq i { display:none; }
    #paper .mkp-view .mkp-g .mkp-ul { columns:1; }
    #paper .mkp-view .mkp-foot { margin-top:18px; }
  }
  @media (prefers-reduced-motion:reduce){ #paper .mkp-card, #paper .mkp-doc { transition:none !important; } }
  @media print {
    #paper { height:auto !important; min-height:0 !important; display:block !important; overflow:visible !important; padding:0 !important; }
    #paper > .wrap { zoom:.8; padding-top:10mm !important; }
    #paper .head { margin-bottom:22px; }
    #paper .mkp-grid { grid-template-columns:repeat(4,minmax(0,1fr)) !important; max-width:none !important; gap:36px 22px !important; }
    #paper .mkp-card { opacity:1 !important; transform:none !important; }
    #paper .mkp-dlg, #paper .mkp-doc::after { display:none !important; }
    #paper .mkp-print { display:block !important; }
    #paper .mkp-spread { break-before:page; page-break-before:always; height:auto; padding-top:8mm; display:flex !important; justify-content:center; align-items:flex-start; gap:12mm; }
    #paper .mkp-pg { zoom:1.15; border:1px solid #E6E0D7; }
  }
</style>'''

html = f'''<section class="slide" id="paper">
{CSS}
  <div class="wrap">
    <div class="head rv">
      <div class="k">The strategy on paper &middot; the 90-day marketing plan &middot; {N} pages</div>
      <h2>Everything above, <em>written down.</em></h2>
      <p>The whole plan for Kestrel Bay Resort in eight pages &mdash; objectives, audience, the campaign, creative, funnel, CRM, measurement and the timeline. <b>Yours on day one, updated every month.</b> Tap any page to read it.</p>
    </div>
    <div class="mkp-desk rv">
      <div class="mkp-grid">{thumbs}
      </div>
    </div>
    <div class="mkp-legend rv"><span><b>1&ndash;2</b> &middot; the why and the who</span><span><b>3&ndash;5</b> &middot; the campaign, creative, funnel</span><span><b>6&ndash;7</b> &middot; the system and the numbers</span><span><b>8</b> &middot; the 90 days, and who does what</span></div>
    <div class="mkp-print" aria-hidden="true">{spreads}</div>
    <div class="mkp-dlg" role="dialog" aria-modal="true" aria-label="Marketing plan page" aria-hidden="true">
      <div class="mkp-bar"><div class="mkp-dtabs">{dtabs}</div><button type="button" class="mkp-x" aria-label="Close">&times;</button></div>
      <div class="mkp-stage"><button type="button" class="mkp-nav mkp-prev" aria-label="Previous page">&lsaquo;</button><div class="mkp-view"></div><button type="button" class="mkp-nav mkp-next" aria-label="Next page">&rsaquo;</button></div>
    </div>
    <div class="note"><b>Twenty seconds &mdash; this is the proof it&rsquo;s thought through</b><b>&ldquo;And this is all of it on paper &mdash; eight pages, the full 90-day plan for Kestrel Bay Resort. You get it on day one, and we update it every month.&rdquo;</b> Tap page one: <b>&ldquo;what Kestrel Bay starts with, and the objectives for the quarter.&rdquo;</b> Then arrow to page eight if they want the timeline: <b>&ldquo;live by day six, a review every week, and exactly who does what &mdash; we stop at the verified enquiry, and your sales team makes the sales.&rdquo;</b></div>
  </div>
</section>
'''
open(os.path.join(HERE, '..', 'src', 's20_paper.html'), 'w', encoding='utf8').write(html)
print('paper written', len(html))
