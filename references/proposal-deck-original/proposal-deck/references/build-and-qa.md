# Build, QA and delivery

## Contents
- [The project folder](#the-project-folder)
- [Building](#building)
- [Previewing](#previewing)
- [QA — look, operate, audit](#qa--look-operate-audit)
- [Porting from a previous deck: residue](#porting-from-a-previous-deck-residue)
- [Splitting the work across subagents](#splitting-the-work-across-subagents)
- [The client PDF](#the-client-pdf)
- [Publishing and file sizes](#publishing-and-file-sizes)
- [Editing safely](#editing-safely)

---

## The project folder

```
<client>-proposal/
├── deck.config.json      title · palette re-skin · residue words the build must flag
├── source/              facts.md (the only source of truth) · our-business.md (the presenter's side) · offer.md (the deal)
├── tpl/                  00_head.html (base CSS, fonts, design tokens) · 02_body_pre.html (progress bar, nav dots, notes hint, shared CSS)
├── src/
│   ├── s01_cover.html … s23_included.html   one file per slide, assembled in filename order
│   ├── extra.css         shared skin + ad-mockup styles
│   ├── script.js         CFG (the deal numbers) · the dials · data-live · nav dots · reveal · keys · QA hooks
│   ├── js/*.js           per-page modules: journey.js (the film) · wall.js (the build) · ads.js (flips) · paper.js · callscript.js
│   └── print.css         browser-print fallbacks only (the client PDF is made from screenshots)
├── build/
│   ├── build.py          assembles index.html + standalone.html, reports what's unfinished
│   ├── gen_how.py + how.css   → src/s13_how.html        (the funnel film)
│   ├── gen_builds.py          → src/s14_structure.html  (the 448 wall + ad-set console)
│   ├── gen_ads.py             → src/s15…s18_ads*.html   (the feed ads)
│   ├── gen_paper.py           → src/s20_paper.html      (the 90-day plan)
│   ├── call_script.html       → assets/call-script.jpg  (scripts/render_page.mjs)
│   ├── gen_music.py           → the film's music bed (pure Python; optional)
│   └── placeholders.py        regenerates the placeholder images
├── optional/             extra slides (form · next steps · finale) + README
└── assets/               photos, logos, fonts, music, map data
```

**Generated pages:** edit the generator, then run it (`python3 build/gen_ads.py`), then build. Never hand-edit a
generated file — the next run overwrites it. Each generated file's generator is named in the file's first lines.

## Building

```bash
python3 build/build.py
```
writes `index.html` (references `assets/`) and `standalone.html` (one self-contained file; each asset stored once),
and prints what isn't finished:

| Line | Meaning | Done when |
|---|---|---|
| `TODO n ⟦…⟧ marker(s)` per slide | a fact, figure, quote or proof point still to supply or verify | zero — or every remaining one is listed back to the user |
| `PHOTO n placeholder image(s)` | a `ph-*`/`proof-*`/`brand-*` placeholder is still referenced | zero |
| `MISSING asset file(s)` | a referenced file doesn't exist | zero |
| `RESIDUE 'word': n hit(s) in [slides]` | a word from `deck.config.json → residue` survived (`(scripts…)` = in `src/script.js` or `src/js/`) | zero |

`OUT=index-mine.html python3 build/build.py` writes a private preview only (useful when several agents build at once).

The untouched template reports its own example names as RESIDUE and dozens of TODO markers — expected; a finished
port reports none. Photos: save the client's photo over the placeholder of the same kind, or add your own file and point
the slot at it — any filename works. The placeholder check reads a stamp inside the generated files, so a real photo is
never flagged; to make more placeholders, add rows to `PHOTOS` in `build/placeholders.py` and run it. The example call
script image is stamped too, so the build flags it until you re-render it for the client.

## Previewing

Open `standalone.html` straight in a browser, or serve the folder (`python3 -m http.server 8000`) and open
`http://localhost:8000/index.html` — some browsers block fonts loaded from `file://`.

Keys: ↓ / ↑ / Space / PageDown step slide to slide · **N** toggles presenter notes. URL switches (QA hooks in
`src/script.js`): `?noanim` (no reveal animation — every element shown; the film/wall show a static state), `?ovf`
(writes elements overflowing the viewport into `body[data-ovf]`), `?offs` (slide offsets into `body[data-offs]`),
`?qa` (pins the cover height for tall headless windows), `?shift=<px>` (paints the page offset without scrolling).

## QA — look, operate, audit

1. **Look.** `node <skill>/scripts/shoot.mjs . shots` → one JPG per slide at 1440px. Read every one, at full size,
   as the prospect would. Then `--width 390` for a phone pass on the pages the prospect might open on mobile.
   (Python-only environment: `python3 <skill>/scripts/shoot.py . shots` does the same with Playwright.)
2. **Check.** `node <skill>/scripts/shoot.mjs . --check` → console and network errors, broken images, NaN /
   undefined / Infinity on screen, horizontal overflow, markers still showing. Exit code 1 if anything is broken.
3. **Operate.** `node <skill>/scripts/operate.mjs .` drives every interaction and prints what followed: each dial and
   preset (and the package's live ad-spend and price), the forecast sliders, every reach tier, the summary cards, the
   report attachment, an ad flip, a plan page, the wall's product tabs, the film (screenshot after 6 s of playing) and
   the call-script pop-up — then lists any NaN or console error, with screenshots of each state. Read the numbers: do
   they follow? Then watch the film yourself to the end, and if you add or change an interaction, add a step to the script.
4. **Verify what's painted, not what's present.** An element can exist, be opacity 1 and have the right size while
   sitting underneath something else. Prove visibility with `document.elementsFromPoint(x, y)` — the target must be
   first. A page that looks unusually sparse is a bug hypothesis until paint order is checked. A hidden or backgrounded
   tab delivers no scroll events or IntersectionObserver callbacks — check `document.visibilityState` before believing
   "nothing animates". For media, confirm `currentTime` advances, not just `paused === false`, including after the page
   was loaded in the background and after scrolling away and back.
5. **Audit the numbers across pages.** List every figure that appears more than once (budget, cost per enquiry,
   enquiries per month/quarter, price, fee, stack total, guarantee floor, the demo buyer's answers and score) and
   confirm they agree. Anything that exists on an interactive page must be a `data-live` span elsewhere, never retyped.
   Watch for two pages using the same adjective for different quantities ("qualified ≈ 40" against "100 qualified").
6. **The adversarial pass** (SKILL.md, Step 6) — and show the user what you checked.

## Porting from a previous deck: residue

A clean name-swap still leaves the previous client's *reasoning*. After swapping:
- Put the old client's names **and concepts** in `deck.config.json → residue` (for a resort: rental, yield, occupancy,
  offshore, freehold, finished/furnished, investor, commission…) and clear every hit by reading it in context.
- Read every page as the new client: ad mock-ups and their image captions, form questions, captions in the film,
  presenter notes, the plan pages, alt text.
- Check every claim against the new product's facts (a "keys cut, furnished, operating" ad for a project that completes
  next year contradicts three other pages).
- Check chained substitutions for doubled words and mangled phrases ("your your agent", "What would the north aspect be for?").
- Ask who earns each number in *this* client's world before copying a tile from a deck for a different kind of client.

## Splitting the work across subagents

A full port is ~25 pages and several generators. With subagents, split it the way the files are split, run them in
parallel, and give them all one shared brief. Ownership that works:

| Agent | Files |
|---|---|
| Opening | s01_cover · s02_summary · s03_bridge · s04_case · s05_cases · the three chapter dividers |
| Opportunity | s07_whynow · s08_gap · s09_catchment · s10_numbers · s11_forecast · s21_reporting · **and `src/script.js` (sole owner)** |
| The film | build/gen_how.py · build/how.css · src/js/journey.js |
| The build | build/gen_builds.py · src/js/wall.js |
| The creative | build/gen_ads.py · src/js/ads.js · s19_stories |
| Plan & package | build/gen_paper.py · src/js/paper.js · s23_included · build/call_script.html · src/js/callscript.js |

The shared brief (write it to a file and point every agent at it) contains: what the deck is and who it's for; the path
to `source/facts.md` and the rule that it's the only source of facts; the shared names and numbers every section must
match exactly (product names, prices, the funnel's name, the pace, the price, the form questions, the demo customer,
the pipeline stages, chip colours); the copy rules; the photo and logo files; "edit only your files — never
`src/script.js`, `src/extra.css`, `tpl/*`, `build/build.py` unless named"; "edit generators, not their output"; how to
preview into a private file (`OUT=index-<name>.html`) and screenshot their own slides (`shoot.mjs --file index-<name>.html
--ids …`); the residue grep; "operate your interactions"; "delete your preview file"; and the report format (files
changed, judgement calls, open markers, anything unverified). Then build once, screenshot everything, and do the
cross-page number audit yourself — agents can't see each other's numbers.

## The client PDF

```bash
node <skill>/scripts/shoot.mjs . pdf-shots --scale 1.5          # presented exactly: notes hidden, fixed UI hidden, ?noanim
python3 <skill>/scripts/make_pdf.py pdf-shots "<Client> Proposal.pdf"   # one slide per page, auto-shrinks to ≤ 15 MB
```
Never the browser's Print → PDF for the client file — it reflows to A4, shifts slides left, cuts them across pages,
and rasterises soft shadows into grey blocks. Check the PDF by looking at its pages, not the HTML.
**Send-only PDFs** (no call): move the reasons from the presenter notes into the visible summary and price copy, state
the period on every price, and remove any claim that was cut elsewhere. The film and dials show their static state, so
make sure that state tells the story (the film's static frame is its final, most complete moment).

## Publishing and file sizes

- `standalone.html` is the easiest thing to send or publish: one file, works offline. Keep it under ~16 MB (many
  hosting and artifact tools cap there): photos at about 1600 px wide, JPEG quality ~80, ≤ 300 KB each. The build prints
  the size.
- If the environment can publish a page with supporting files, publish `index.html` with every file under `assets/`
  that the page references.
- Video doesn't fit in a single-file deck at any real length — keep the deck's films as the coded demos, and send real
  video files separately.
- Before publishing, the build report and `--check` must be clean, and nothing fictional from the template may remain.
- A link to a private page someone else must open needs sharing — tell the user how, don't assume.

## Editing safely

- **Before replacing a block of code by slicing between two markers**, print what lies between them — a slice can
  silently delete unrelated features that sat inside the range. After any large edit, list the `/* ═══ … ═══ */` block
  headers in `src/script.js` before and after and compare.
- **Cutting an interactive page:** remove its call sites, update any static fallback numbers in the markup to the
  intended opening state, re-check every `CFG.*` key still referenced, and load the page to confirm no console errors
  and no NaN.
- **A print rule that seems to do nothing** is usually losing on specificity to an id-scoped rule elsewhere — force an
  absurd value with `!important` to tell cascade from media.
- Keep build scripts and backups inside the project folder, not in a temporary directory that may be wiped.
