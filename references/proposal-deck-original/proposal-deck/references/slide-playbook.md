# Slide playbook

Every page of the deck: its job, what goes on it, the copy pattern, the presenter note, and the mistakes that have
cost deals before. Files are in `assets/template/src/` (generated pages name their generator in `build/`).

## Contents
- [Before you start: the client's role](#before-you-start-the-clients-role)
- [How every page is built](#how-every-page-is-built)
- [Opening](#opening) — cover · summary · bridge · case · cases
- [Chapter One — the opportunity](#chapter-one--the-opportunity) — ch1 · whynow · gap · catchment · numbers · forecast
- [Chapter Two — the campaign, already built](#chapter-two--the-campaign-already-built) — ch2 · how · structure · ads1–4 · stories · paper · reporting
- [Chapter Three — the case for saying yes](#chapter-three--the-case-for-saying-yes) — ch3 · included
- [Optional modules](#optional-modules)
- [Adding, cutting, reordering](#adding-cutting-reordering)

---

## Before you start: the client's role

Establish what the prospect actually is in the transaction. Same layout, opposite argument:

| Role | What the deck sells | The money story | Watch for |
|---|---|---|---|
| **Owner** (developer, manufacturer, clinic — owns what's sold) | Their product | Finite stock, sell-out pace, a success fee on the sale price | Urgency from price rises / releases |
| **Seller-side middleman** (selling agent, broker, reseller — sells someone else's stock, paid a commission) | **Them** — their licence, access, representation, service | The buyer register is the asset; listings are this month's hooks; a fee on *their commission*, never on a sale price they don't receive | Never build on one product they could lose next month; never argue one of their products beats another |
| **Buyer-side agent** (buyer's agent, mortgage broker, advisor paid by the buyer — often a flat fee) | **Them** — their licence, track record, process and fee | Each signed client is worth their fee; the forecast is enquiries → strategy calls → signed clients × their fee (one number, no price slider) | Never rank one area or product over another; never promise returns; the "stock" in their ads is proof of what they've bought, not an offer |
| **Advisor** (sells their own time) | Their expertise | The funnel feeds engagements, not sales | Map onto their own published process; show the single step you fill |

Tells: "presented by" vs "developed by"; "access to" stock vs "our development"; whether their site has a portfolio of
their own projects. When you don't know a figure only they know (their commission rate, their conversion), make it a
slider they set on the call instead of guessing it into the deck.

## How every page is built

```html
<section class="slide" id="numbers">
  <div class="wrap">
    <div class="head rv">
      <div class="k">The media approach · all AUD</div>            <!-- eyebrow: small caps, where we are -->
      <h2>You set the pace.<br><em>The budget follows.</em></h2> <!-- plain line + italic turn -->
      <p>Optional one-line standfirst.</p>
    </div>
    … the page's component …
    <div class="note"><b>Do this live — three dials, all linked</b>Start on the top one: …</div>
  </div>
</section>
```

- **Eyebrow** (`.k`): where we are in the argument ("The opportunity · 1 of 2").
- **Headline** (`h2`): a plain statement, then its turn in italics. Two short lines at most. No puns, no poetry.
- **`.rv`**: fades and rises into view on scroll (off when printing or with `?noanim`).
- **Presenter note** (`.note`): hidden until the presenter presses **N**. It is the talk track — the exact words to say,
  what to click, what to do if challenged. Bold lead-in, then the lines in quotes. Everything that only needs saying
  once lives here, not on the page.

---

## Opening

### 1 · `cover` — `s01_cover.html`
**Job:** their product, at its best, with one promise they'll repeat to their partner.
**On it:** a full-bleed photo of *their* product under a dark gradient; your monogram and name small at the top;
their logo (white); a two-line headline (`Australians already know Kestrel Bay. We find the ones who want to own a
suite.` — what's true now + what you'll do); one sentence saying what they get and how it's measured; "Prepared for
<company> · <product> · <month year>"; a small "scroll" hint.
**Note:** open with genuine appreciation and the one thing that shaped the whole plan. Then the line that sets the deck
apart: *"Everything in here is built, not proposed — the ads use your photos and your prices, and they're finished
files ready to upload. We did that before you'd agreed to anything, because we'd rather show you than tell you."*
**Pitfalls:** a stock photo (use theirs); a clever headline; your logo bigger than theirs.

### 2 · `summary` — `s02_summary.html`
**Job:** prove you understand their situation, and give the whole plan in thirty seconds.
**On it:** a headline stating their situation in your words (fact + consequence: "Kestrel Bay is a resort Australians
would love. Now it needs Australian buyers."). Three numbered cards joined by down-arrows — **01 Situation → 02 Plan
→ 03 Work** — each a headline (plain fact, italic consequence) and **two short sentences, maximum**; "See the detail"
opens each card for the specifics (numbers, mechanics, chips).
**Copy:** "X, so Y". No metaphors or fragments ("Seven residences, a finished film" was rejected as poetry). Don't call the
buyer "she" here.
**Note:** read each headline and move on; open a card only if asked. "The price and the guarantee come at the end."
**Pitfalls:** quoting or listing their brief back to them ("You asked for nine things…") — it reads as unprofessional;
a cramped side column instead of the stepped vertical flow. **For a send-only PDF** this page must teach: give each
point its reason and real numbers, because nobody is there to say them.

### 3 · `bridge` — `s03_bridge.html`
**Job:** tell them what they're about to see, and why to believe it, before showing anything.
**On it:** one centred paragraph — *"This is the exact strategy we are about to walk you through, rebuilt specifically
for <product>. Run for <who it has been run for>, it has generated <N> enquiries and <$M> of <stock> sold."* — with the
key phrases in the accent colour; then three stat tiles: volume, value, speed (e.g. "6 days from onboarding to live").
**Pitfalls:** turning it into a diagram (rejected repeatedly — it's a preview statement); putting a conversion rate in a
tile (a bare "1 in 50" reads as a guarantee — keep conversion figures inside a hedged sentence, or out); numbers you
can't back with screenshots.

### 4 · `case` — `s04_case.html`
**Job:** the single most similar real result. The quote argues better than any paragraph about it.
**On it:** photo of the project; name · type · place; the client's words verbatim (with permission) and their
attribution; three or four stat tiles in the money that matters *in this prospect's world* — for an owner: time to first
sale, ad spend, sale value, return on ad spend; for a middleman: commission earned. Nothing else — no framing prose, no
"why this comparison" box, no closing band.
**Note:** read the quote aloud, slowly; stop; then the numbers.
If the testimonial comes without that client's numbers, show the quote larger and use only the tiles you can fill
truthfully (or none) — the tile labels are yours to rewrite, never keep a label that doesn't describe a real number.
**Pitfalls:** copying a tile from a different kind of deal (a middleman's "commission" tile in an owner's deck reads as
"who took a cut?"); a "sold out" claim you can't prove; any invented or "representative" case.

### 5 · `cases` — `s05_cases.html`
**Job:** volume proof, straight from the ad platform.
**On it:** six real results screenshots (Results / Cost per result / Budget rows, cropped from Ads Manager — real
captures, never re-typeset or redrawn) as `assets/proof-1…6.jpg`; a dark band with the totals: enquiries across these,
blended cost per enquiry, the range, the daily budgets. Headline = the total ("<N> enquiries. <N> campaigns.").
**Note:** *"Before you take my word for anything — these are our own numbers, straight out of Ads Manager."*
**Pitfalls:** no screenshots → cut the page, don't fake it. Check the six figures sum to the band.

### 6 · `ch1` — `s06_ch1.html` (chapter divider)
Full-bleed photo, "Chapter One", **"The opportunity in front of you."**, one line listing what the chapter covers.
Dividers are pause points on a call: the presenter says the one sentence in the note and turns the page.

---

## Chapter One — the opportunity

### 7 · `whynow` — `s07_whynow.html`
**Job:** show forces converging *now* that make this the moment — with sources they can check.
**On it:** three photo cards, each one big figure + one line + its source: a **demand** fact (who's already buying, and
rising), a **push** fact (why buyers are looking now), a **rules / timing** fact. Then "In the news": six real clippings
(publication · date · the headline exactly as published · your one-line takeaway · the link), with the rule line
"Headlines as published · the one-liners are ours". Then a band of three numbers that count up on arrival, and a
"general information only — not tax, legal or financial advice" line.
**Pitfalls:** stats that are displayed rather than argued; a statistic with no date or link; anything that sounds like
a forecast of prices or returns.

### 8 · `gap` — `s08_gap.html`
**Job:** the reason a buyer picks *this* product over the alternatives — the core of what the ads will say.
**On it:** "Before an Australian sends six figures overseas, they need three answers. Most projects can give one. <Product>
can give all three." Three cards: a buyer's question over a photo (*Who's behind it? · Who runs it when I'm home? ·
Will I actually use it?*), a ✕ row for "a typical project" and a ✓ row for this one, and "Why it matters". A dark band
closes it: **"That's what we advertise."** — the ads sell these answers; returns stay off the ads and go on the call.
The ✓ rows are written from the *buyer's* side — the answer a stranger needs before they'd trust this product — which is
why this page isn't "stating their advantages back to them": the insight is which three questions decide it.
**Pitfalls:** stating their own advantages back to them as if it were news ("you have a great location") — they already know. A value page
must tell them something they couldn't have worked out, ideally in money. Arguing one of a middleman's products beats another.

### 9 · `catchment` — `s09_catchment.html`
**Job:** where the buyers are, and how many — and let the presenter widen it tier by tier.
**On it:** a real map (true coastlines and borders — never hand-drawn) with the product pinned; tier cards to press
(Tier one · the closest, most frequent buyers → … → National), each with who and why, a population and region chips;
pressing one lights its rings and cities on the map and updates the cumulative reach. Underneath: one multiplication —
population × the share open to buying = the addressable market — with its source.
**Note:** click the tiers in order so they watch the map open up.
**Pitfalls:** a schematic map ("looks like a kid made it") — the template's outline is labelled illustrative; build
the real one for a client (`scripts/osm_map.py`, `references/adapting.md`); a population figure without a source.

### 10 · `numbers` — `s10_numbers.html`
**Job:** hand them the controls. They choose the pace; the budget follows.
**On it:** three linked dials — **ad spend per month**, **enquiries per day**, **cost per enquiry** — move the budget or
the cost and the enquiries follow; move the enquiries and the budget follows. Presets (Steady · Recommended · Go hard).
Outputs: spend per day, enquiries per month, spend per month, enquiries per quarter, spend per quarter. One line saying
why the planned cost per enquiry is set above your real average (a bigger purchase than most of what you advertise).
**Note:** *"Do this live"* — start on the top dial; then hand them the mouse and stay quiet.
**Pitfalls:** replacing a dial when adapting — add the new input alongside the old one; a planned cost that's below what
you can actually deliver; recommending a pace their team can't call (ask how many calls a day they can make, and keep
"Recommended" under it — a volume guarantee depends on it).

### 11 · `forecast` — `s11_forecast.html`
**Job:** what the enquiries could be worth **to them**, in their numbers.
**On it:** enquiries this quarter (from the pace page) → **enquiries per sale** (a slider, opening on a published,
citable third-party benchmark, with the source in a callout — never your own claim) → **average sale** (a slider across
their real prices) → sales, sales value, **less ad spend**, **value after ad spend** (the hero number) and return on
ad spend. A line on what compounds (the database of verified buyers they keep). "Figures follow your sliders — a model,
not a promise."
**Note:** two questions, in order, then stay quiet: "How many enquiries does your team usually need for a sale?" — set
the slider to their answer. Whatever they say becomes the number on the page.
**No citable benchmark for this market?** Open the slider on the prospect's own figure (ask for it on the call) or on a
deliberately cautious value labelled "a starting point — set it to yours", and say so in the note. Never present your
own number, or an invented one, as a benchmark.
**One price, not a range** (a flat fee, a single product)? Remove the average-sale slider and set `CFG.avgSale` in
`src/script.js` — the forecast then multiplies by that one number.
**Pitfalls:** your fee anywhere on this page (it kills the value build before the offer); a forecast that stops at gross
and flatters you (always subtract the ad spend); more than one arithmetic step the presenter can't say in twenty seconds.

### 12 · `ch2` — `s12_ch2.html` (chapter divider)
**"The campaign, already built."** From here everything is finished work.

---

## Chapter Two — the campaign, already built

### 13 · `how` — `s13_how.html` ← `build/gen_how.py`, `build/how.css`, `src/js/journey.js`
**Job:** the showpiece. Show — don't describe — how a stranger scrolling at night becomes a booked call with their team.
**On it:**
1. The funnel's **name** as the headline ("The Verified Buyer Funnel.") and a strip of six live mini-phones on a
   timeline — the ad · the questions · the codes · the alert · the call · the outcome — each with a one-line reason.
2. **The film.** Press Play: the buyer's phone ──wire── the CRM record ──wire── the sales team's phone. A scripted thumb
   taps through the real form; each answer travels down the wire into the record; the alert lands on the team's lock
   screen; the call, the booking, the reminders, the meeting, the outcome — tracked back to the ad. Captions answer the
   question their team would ask at that moment. A chapter timeline you can click, a scrub bar, a music bed.
3. **Phase two** — the next upgrade (e.g. a short film and landing page so buyers watch first and book themselves),
   shown as a second, shorter film of only what's different.
**Note:** start with the strip, one step one reason, left to right. Then let the film play; read two or three captions
aloud and let the rest run.
**Make it true to the client:** the form questions, the demo customer, the CRM's name, the pipeline stages, the
clocks (who is in which time zone — the template says "Bali time is Perth time"), and the verification step only if
the user's tools can really do it.
**Bar:** this is the page prospects remember. Everything must visibly link together, and every media element must
actually play. A static diagram here — however thorough — reads as homework.

### 14 · `structure` — `s14_structure.html` ← `build/gen_builds.py`, `src/js/wall.js`
**Job:** make the scale of the work visible in one glance, and let them explore any corner of it.
**On it:** a maths band — **4 products × 7 locations = 28 ad sets × 16 ads each = 448 live ads · 0 for you to make** —
the wall (every square is one live ad, coloured by product, building in on arrival, with Replay), and a dark console:
tap a product, tap a location on the map (or a chip), and see that ad set's audience ("who this ad set finds") and its
sixteen finished creatives — four angles × four formats (photo, carousel, short video, story) — hover to enlarge, or
press Auto-tour. The headline number is the ad count.
**Note:** numbers first ("four products, seven locations, sixteen ads each — four hundred and forty-eight, and zero for
you to make"), then open one ad set live.
**Size the account to the budget.** Each ad set needs enough daily spend to learn; on a small budget use fewer ad sets
(a handful) with the angles as ads inside them, and let the wall show the honest, smaller multiplication — every count on
the page follows the data in `build/gen_builds.py`. Check whether the platform puts the vertical in a special ad
category (housing, credit, employment, financial products) in that country — it removes targeting options, so write
"who this ad set finds" to what's allowed.
**Pitfalls:** a boxes-and-arrows architecture diagram (rejected as amateur); targeting that doesn't read like real
audience definitions; one product getting weaker creative than the others.

### 15–18 · `ads1`–`ads4` — `s15…s18` ← `build/gen_ads.py`, `src/js/ads.js`
**Job:** prove the creative exists, and that it's good. One page per angle:
1. the core offer ("own a suite at Kestrel Bay") · 2. the doubts that stop a sale · 3. the differentiator (e.g. the
owners' membership) · 4. for people still deciding (retargeting — warm audiences only).
**On it:** five finished feed ads per page (four on the warm page), each in a realistic platform frame (page name +
avatar, primary text with "See more", the creative, the headline row and button, reactions), an ad-set chip above it,
and a **"Why it works"** button that flips the card to the strategy. A legend of the ad-set colours.
**Rules:** every creative is a *designed* static — headline, price, feature strip, logo composed on the photo; **no two
share a layout or an angle**; each uses the client's real photo that matches its line; never promise returns.
**Note:** *"Twenty ads, no two alike — because look-alike ads bid against each other in the auction and push your costs
up."* Then point at one and flip it.

### 19 · `stories` — `s19_stories.html`
**Job:** the same angles, full screen. Eight 9:16 stories, eight different native treatments (giant type stack,
incoming-call screen, news lower-third, split-flap board, poll sticker, wallet passes, number tiles, notes-app list),
each with its caption underneath. Nothing important above the top 14% or below the bottom 20% (the platform's UI sits there).

### 20 · `paper` — `s20_paper.html` ← `build/gen_paper.py`, `src/js/paper.js`
**Job:** "Everything above, written down." Proof it's thought through, and theirs on day one.
**On it:** the 90-day plan as eight A4 pages laid out like a printed document set — 01 Executive summary & objectives ·
02 Audience & positioning · 03 Campaign strategy · 04 Creative plan · 05 Funnel & qualification · 06 CRM, automation &
sales process · 07 Measurement · 08 90-day timeline & responsibilities — tap any page to read it full size (prev/next).
**Note:** twenty seconds: "This is the proof it's thought through. It's yours on day one, updated every month."

### 21 · `reporting` — `s21_reporting.html`
**Job:** what working with you feels like every week.
**On it:** a realistic Friday email (subject, sender, a short plain-English summary that leads with numbers, a warm
sign-off, the attachment) and, on clicking the attachment, the one-page report straightening up beside it: spend,
verified enquiries, cost each, calls booked; per-enquiry and per-qualified costs, booking and show-up rates, best
segment; **what we changed** and **what's next**; the ads running this week. Plus the monthly review call. The numbers
follow the dials.
**Note:** *"Do this live"* — click the attachment and let it straighten up.

---

## Chapter Three — the case for saying yes

### 22 · `ch3` — `s22_ch3.html` (chapter divider)
**"The case for saying yes."** Note: *"Last section, and it's one page. Everything that gets built, then everything
you're guaranteed, and the number is at the very bottom — because it only means something once you've seen the rest."*

### 23 · `included` — `s23_included.html`
**Job:** close. Built **backwards from the price**, read top to bottom as one continuous card, and the deck ends on it.
1. **01 What you get** — the value stack in groups (the campaign · the setup and sales system · sales support · included
   in the price), each line a bold benefit + one explaining line + its price, group subtotals, **Total value**.
2. **02 What is guaranteed** — a hero guarantee (dark card, a seal, its conditions listed) and four named guarantee
   cards, each a name + a promise + a remedy.
3. **03 Your price** — "Everything above, bought separately" (struck) → arrow → "Our standard fee" (struck) → arrow →
   one dark price card with its named reason ("Launch pricing"), the fee + ad spend = all in, the period, when it's paid.
Full rules in `references/offer-and-pricing.md`. **Audit:** list every $ figure in the markup above section 03 — only
stack prices, the total value and ad spend may appear. Your fee must not.

---

## Optional modules

In `assets/template/optional/` (see its README for how to add one):
- **The enquiry form** (`s13a_leadform.html`) — "Six questions. Then a code, before it counts." The real form, three
  paginated phone screens, then the enquiry card the team receives with a live lead score. Add it when the film isn't
  used, or when the prospect has been burned by junk leads (open on that: *"If you have run lead ads before, you already
  know the problem: a name, an email, and a number that never answers."*).
- **Next steps** (`s24_decision.html`) — soft, four stops: your green light → book the onboarding call → live within
  within six days (the deck's onboarding promise) → your first enquiry. No price column, no push. The current default is to end on the price instead.
- **Finale** (`s25_finale.html`) — a closing photo, three numbers and a contact card. Useful when the deck is sent
  rather than presented.

## Adding, cutting, reordering

- **Add** a page where it earns money: a deeper opportunity argument, a second case study (real), a brand or video
  campaign page after the build, an objection page *only* if it can't live as one line on an existing page.
- **Cut** abstract pages ("what we build", "our process" in prose), pages whose premise a fact check killed, and any
  page whose only content is a restatement. Before cutting an interactive page, search `src/script.js` and `src/js/` for
  everything it feeds — other pages may read its numbers (`data-live`, `CFG`), and a thrown error can silently leave
  stale fallback figures on screen.
- **Reorder** rarely. If you move a section, re-read every block for references to things that are now *below* it
  ("On Option One…" before Option One exists).
- Keep the nav labels in sync: `NAMES` in `src/script.js` maps slide ids to the labels on the side dots.
