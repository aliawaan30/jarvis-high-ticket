# Components — how each interactive and animated piece works

Read this before changing how a page *behaves* (copy changes don't need it). Everything is plain HTML, CSS and
JavaScript — no framework, no build step beyond `build/build.py` concatenating the parts.

## Contents
- [Deck-wide behaviour](#deck-wide-behaviour)
- [The deal numbers: CFG, the dials and data-live](#the-deal-numbers-cfg-the-dials-and-data-live)
- [Page by page](#page-by-page)
- [The film (`#how`)](#the-film-how)
- [The build wall (`#structure`)](#the-build-wall-structure)
- [The ads (`#ads1`–`#ads4`) and stories](#the-ads-ads1ads4-and-stories)
- [Design tokens and type](#design-tokens-and-type)
- [Rules for anything you add](#rules-for-anything-you-add)

---

## Deck-wide behaviour

All in `src/script.js` (bottom half) and `tpl/02_body_pre.html`:

| Feature | How it works | Where |
|---|---|---|
| Progress bar | `#bar` width = scroll fraction | `spy()` |
| Nav dots | one dot per `section.slide`, label from `NAMES[id]`, turns white over dark slides (`DARK` set) | `NAMES`, `DARK`, `spy()` |
| Reveal on scroll | elements with `.rv` start hidden only when `body.anim` is set, and get `.in` from an IntersectionObserver. Opt-in, so print, `?noanim` and no-JS show everything | "reveal on scroll" block |
| Keys | ↓ / PageDown / Space → next slide, ↑ / PageUp → previous, **N** → toggles `body.notes` (shows every `.note`) | "keys" block |
| Presenter notes | `<div class="note"><b>Lead-in</b>Text…</div>` inside a slide; hidden unless `body.notes` | CSS `.note` |
| Count-ups | `<b class="cup" data-to="1630000" data-sep="1" data-pre="$" data-suf="+" data-dec="0">` counts up once when 60% visible (skipped with `?noanim` / reduced motion) | "count-ups" block |
| Tap-to-open cards | `#summary .stage` toggles `.open` on click / Enter / Space | "summary" block |
| `asset(path)` | every asset path built in JS goes through it, so `standalone.html` can serve the inlined copy | top of `script.js` |
| QA hooks | `?noanim` `?ovf` `?offs` `?qa` `?shift=` — see `build-and-qa.md` | end of `script.js` |
| Reduced motion | every animation checks `prefers-reduced-motion` and `?noanim`, and falls back to the finished state | each module |

## The deal numbers: CFG, the dials and data-live

```js
const CFG = {
  qual: 0.65,        // share of verified enquiries scored "call first"
  days: 30,          // a month in the model; the quarter is 3 months
  price: 24000,      // the quarter, all in (fee + the ad spend included in the price)
  budgetM: 4000,     // the prospect's monthly ad spend
  paceC: 25,         // the planned cost per verified enquiry
  stackBase: 46300,  // the value stack WITHOUT the ad-spend line (that line follows the dials)
  locale: 'en-AU',   // number formatting       cur: '$'  — money symbol      curShort: 'A$' — where it must be explicit
  avgSale: 240000,   // the forecast's average sale when the page has no #sP slider (one flat price or fee)
};
```
- **The dials** (`#numbers`): `#sB` monthly budget, `#sE` enquiries per day, `#sC` cost per enquiry; presets are
  `#numbers .chip[data-b][data-c]` (scoped to the numbers page, so a `.chip` elsewhere is never wired to the budget). `media()` derives everything from budget and cost; moving `#sE` sets the budget
  (`enquiries × cost × 30`). Ranges, steps and default `value`s live on the `<input type=range>` elements in
  `src/s10_numbers.html` — make the defaults equal `CFG`.
- **Outputs** on the numbers page: `#oDay #oL #oM #oQ #oT`. **The forecast** (`#forecast`): `#sS` enquiries per sale,
  `#sP` average sale in thousands (optional — without it, `CFG.avgSale`) → `#fSale #fPer #fComm #fAd #fAdPer #fNet #fRoas` (and `#vQ #qMo #vS #vP`), via `earn()`.
- **`data-live`** — any element anywhere with `data-live="<key>"` is rewritten by `calc()` whenever a dial moves:

| key | value | key | value |
|---|---|---|---|
| `cpe` | cost per enquiry | `price` | fee + the quarter's ad spend |
| `daily` | ad spend per day | `fee` | `CFG.price − 3 × CFG.budgetM` |
| `month` | enquiries per month | `perAll` | all-in cost per enquiry |
| `quarterN` | enquiries per quarter | `callFirst` | enquiries a month scored "call first" |
| `spendM` | ad spend per month | `incG` / `spendQ` | ad spend for the quarter |
| `stack` | stack total incl. ad spend | `save` | stack − price |
| `wkN` / `wk` / `cpq` | the example weekly report: enquiries in a week at this pace, its ad spend, cost per qualified enquiry | | |

  Use `data-live` for every figure that also exists on an interactive page (the package's ad-spend line, the report,
  the summary chips) — and put the correct opening value inside the span too, so the page reads right before JS runs.
- If you change the model (a different service), keep this shape: one `CFG`, one function that derives everything, one
  `LIVE` map, and spans that subscribe. Never retype a derived number.

## Page by page

| Page | Component | Code |
|---|---|---|
| `summary` | three `.stage` cards joined by arrows; `.open` reveals the detail | `script.js` |
| `bridge`, `case`, `cases` | static; `.rv` reveals; tiles `.mp` (money tile `.mp.gci` is dark); proof screenshots `assets/proof-N.jpg` in `.shot-cs` frames | — |
| chapter dividers | `.div-slide`: full-bleed `.bg` image + `.sc` gradient scrim + `.in` text block | — |
| `whynow` | photo stat cards, news cards, count-up band | `script.js` (count-ups) |
| `gap` | three question cards (✕ typical / ✓ this one / why it matters) + closing band | — |
| `catchment` | inline SVG map; tier buttons `.rc[data-r]`; `BAND` in `script.js` lists, per tier key, the ring ids and city ids to light, the cumulative total and the map tag; `setReach(k)` applies it (it reads every id from `BAND`, so editing `BAND` + the map's ids is enough; the first key opens). A real map for a new market: `scripts/osm_map.py` | `script.js` → `BAND`, `setReach` |
| `numbers`, `forecast` | the dials (above) | `script.js` |
| `how` | the film | `build/gen_how.py`, `build/how.css`, `src/js/journey.js` |
| `structure` | the wall + console | `build/gen_builds.py`, `src/js/wall.js` |
| `ads1`–`ads4` | feed ads with flips | `build/gen_ads.py`, `src/js/ads.js` |
| `stories` | 9:16 stories in container units | `src/s19_stories.html` |
| `paper` | eight A4 pages; tap → dialog with tabs, prev/next, Esc | `build/gen_paper.py`, `src/js/paper.js` |
| `reporting` | email + report; `#attachBtn` toggles `#reportDoc.open` (opened automatically for print) | `script.js` |
| `included` | the package: static markup + `data-live` spans | `src/s23_included.html` |
| call script | `[data-pop="callscript"]` anywhere opens `assets/call-script.jpg` in a modal | `src/js/callscript.js` |

## The film (`#how`)

Generated by `build/gen_how.py` (markup + timing data) with `build/how.css`; played by `src/js/journey.js`.

**Structure:**
1. `.hz` — the six-step strip of mini phones. Each `.hz-s` gets `.on` in turn (`STEP` ms each), a progress line fills
   (`--hzp`), then it loops while visible.
2. `.xj.one` — **stage one**: three panes — the buyer's phone (`.xscr` screens `s1…s11`), the CRM record in the middle,
   the sales team's phone (`.gscr` screens `g1…g11`) — joined by SVG wires (`.xwires`). Below: Play button, chapter
   timeline (`.xsb` storyboard cards you can click), captions.
3. `.xj.two` — **stage two** (phase two): the same frame, only what's different.

**Timing model (in `gen_how.py`):**
- `Dir` ("the director") walks a clock forward and writes the scripted thumb: `wait(ms)`, `sy(key)` scroll-into-view,
  `tap(key)`, `pg(i)` form page, `ty(key, text, base)` typing, `cap(label, text)` a caption, `mark()` a chapter boundary,
  plus helpers `question(i, …)`, `details(…)`, `codes(…)`. The form chapters are timed by the director; the later
  chapters by `AFTER = [ms, …]`.
- Per chapter `k`: `CC1[k]` = captions `[[ms, html], …]`; `ev1[k]` = events `[[ms, type, …]]` where `cm` points the
  camera (`L` buyer · `W` wide · `R` team), `pk` sends a packet along a wire (`L`/`R`/`C`, label, direction), `pl` moves
  the pipeline marker to stage n, `bz` buzzes the team's phone.
- `one_caps` = the chapter titles on the timeline; `one_acts` = the activity log lines that appear in the CRM record;
  `BRIEF` = the answers shown in the record; `SCORE_STEPS` = the running lead score as answers land (ends on the demo
  customer's score); `COLS` = the pipeline stages.
- Durations go out as `data-dur`, events as `data-ev`, on the `.xj` element; `journey.js` runs one clock per stage.

**To change the story:** edit only the **CONFIG block at the top of `gen_how.py`** — the client and brand, the
products, the six questions (`QS`), the demo customer (name, initials, city, masked mobile and email, answers, score
and running score steps), who calls and the time-zone line, the CRM label, the pipeline stages, the meeting and outcome
words, and the story's clock. Everything below the block reads from it. Sentence-level copy lives in the per-chapter
captions (`CC1`/`CC2`), events (`ev1`/`ev2`), chapter titles (`one_caps`), the activity log (`one_acts`) and the strip
(`HZ_STEPS`). The demo customer's sentences use she/her. Run `python3 build/gen_how.py`, build, then **watch it play**
without `?noanim` (Play, scrub, click a chapter, let it finish) — and check the static `?noanim` frame too, because
that is what the PDF shows.

**Sound:** music only, never a voice, and only after the viewer presses Play. `assets/film-music.mp3` (a gentle chord
bed made by `build/gen_music.py`); if the file can't load, a small Web Audio pad plays instead. A mute button sits on the player.

## The build wall (`#structure`)

Generated by `build/gen_builds.py` → `src/s14_structure.html`; behaviour in `src/js/wall.js`.

**Edit only the data block at the top of `gen_builds.py`** (its header comment walks through it), then
`python3 build/gen_builds.py`:
- `SITE` — the page name on every mini creative, the map pin, the story sticker, the boarding-pass destination.
- the products (key, name, status, description, angle names, CTA, colour), `HOOKS` (one per angle), `ANG` (the
  mini-creative content per angle: poll / steps / chat / ask / number / checklist / Q&A), `PANEL` (colours).
- `FORMATS` — `(label, type)` with type one of `ph` photo · `ca` carousel · `vi` short video · `st` story.
- `LOCS` — one row per location (key, short label, full name, `''` or `'Warm'`, the metro areas, the map states it
  lights). A row keyed `'RT'` is retargeting; leave it out if there is none. `ORIG` gives each location's airport code
  for the boarding-pass creative.
- `T` — "who this ad set finds": three audience lines per location × product.
- `SLOTS[product][creative]` — candidate photos per creative (creative = angle × formats + format); a location takes
  candidate `location % len`, so neighbouring ad sets don't repeat a photo. `PEEK` — the carousel's second card.
- `BAND` — the words in the maths band ("the two suites, the Owners' Club, and who is behind it").

**Everything countable is derived:** products × locations = ad sets; angles × formats = ads each; the total, the
maths band, the dot grids, the wall squares, "Location n of L", "Ad set n of S", the count-up, the Auto-tour wrap and the
retargeting styling all follow the data (emitted to the page as `D.n`). The generator checks the data and stops with
a plain message if a list is the wrong length or an entry is missing. Still fixed: the map is Australia's states (Natural
Earth outlines in `assets/cb-aus-paths.json`) with one destination pin, and copy like "tap a product, then a state" —
change those by hand for another country. Each format type has four layouts, so a fifth angle reuses the first.

`wall.js` draws the wall (one square per ad, coloured by product, building in on arrival; Replay), the console (product
tabs, map states + chips, the angle × format grid of creatives drawn in code, hover/tap to enlarge) and Auto-tour
(steps products × locations on a timer with a progress bar; pauses while the pointer is over the ads).

## The ads (`#ads1`–`#ads4`) and stories

`build/gen_ads.py` writes the four pages. Each ad = a function returning the creative's markup (`C_FOUR`, the
magazine-cover treatment, the receipt, etc.), drawn in **container-query units** (`cqw` of the image box) so it scales
like a real 1080 × 1080 file; wrapped in the feed frame (`.fb`: header with avatar and page name, primary text `.fbt`,
the image `.fbi`, the link row `.fbl` with headline and button, reactions, actions), an ad-set chip above and a
"Why it works" back face (`.adback`). `PAGES` maps each page to its ad list and the treatment keys used — **no key may
repeat on a page**. `ads.js` handles the flips (`.adcell.flipped`), the swipeable carousel and number count-ups.

Stories (`src/s19_stories.html`) are hand-written 9:16 cards in container units (`100cqw` = the story's width,
`177.8cqw` its height), each a different treatment, with the safe zones marked in the CSS comment.

## Design tokens and type

`tpl/00_head.html` `:root`:
`--ivory` page background · `--paper` card · `--ink` text · `--soft` body text · `--taupe` labels · `--stone`
rules/neutral · `--teal` the primary (navy in the template) · `--teal-lite` tint · `--sand` accent ·
`--rule`/`--rule2` hairlines · `--sh`/`--sh-lg` shadows. `src/extra.css` adds `--gold-lite`, `--gold-d`.
Type: Playfair Display for display (`h1`, `h2`, figures), Jost for everything else; eyebrows are 10.5 px, .44em
letter-spacing, uppercase. Section rhythm: `.slide` 84 px top / 90 px bottom, `.wrap` max 1120 px.
Re-skin with `deck.config.json → palette` rather than editing hex values by hand (some colours are hard-coded in
generators for the ad creatives).

## Rules for anything you add

- A new slide is a `src/sNN_name.html` file whose number sorts it into place, containing one `<section class="slide" id="…">`.
  Add its id to `NAMES` in `script.js` (and to `DARK` if it's a dark full-bleed slide).
- Page-specific CSS goes in a `<style>` block inside the section, scoped with the section id.
- Page-specific JS goes in `src/js/<name>.js` as an IIFE that returns early if its section isn't present.
- Respect `?noanim` and `prefers-reduced-motion`: show the finished state, start nothing.
- Anything that animates on arrival waits until it's actually visible (IntersectionObserver), pauses when scrolled away,
  and has a static, complete state for print and PDF.
- Asset paths built in JS go through `asset()`.
- Numbers that exist elsewhere subscribe through `data-live`.
- Test it: screenshot, operate, `--check`.
