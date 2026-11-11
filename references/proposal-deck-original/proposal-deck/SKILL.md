---
name: proposal-deck
description: Build a high-converting, interactive sales proposal as one scroll-through HTML deck — researched facts sheet, a three-chapter argument, live calculators the prospect drives, an auto-playing customer-journey demo, finished ad creative, a 90-day plan and a value-stacked package that ends on one price — plus presenter notes, a call script and a client PDF. Ships a complete working template with every component and animation. Use this whenever the user wants to create, port, improve, review or export a proposal, pitch deck, sales deck, client presentation, campaign proposal, quote or offer for a prospect — including "make a proposal for X", "pitch this client", "build a deck for my call on Friday", "turn this prospect's website into a proposal", or when they paste a prospect's details and ask how to win them.
---

# Proposal Deck

This skill builds proposals that do the selling structurally, so the presenter doesn't have to. The deck is a single
scrolling web page (it also exports to a PDF) that walks a prospect from *"this person understands my situation"* to
*"everything is already built"* to *"I'd be silly to say no"* — and only then shows the price.

It is not a slideshow of claims. Every page either shows evidence, lets the prospect operate something, or shows finished
work made for *them* before they've agreed to anything: their own photos and prices in finished ads, a calculator set to
their budget, a working demo of what happens when one of their customers enquires. That is what makes it convert.

The method was developed for a performance-marketing agency selling lead-generation campaigns to property developers,
and the template's worked example is exactly that (a fictional agency, **Harbour Lane Media**, pitching a fictional resort
developer, **Kestrel Developments**). The structure, components and rules carry to any business that sells a service to
another business — `references/adapting.md` shows how to map each page to a different offer or market.

## What you produce

| File | What it is |
|---|---|
| `index.html` + `assets/` | The deck. Scroll or use the arrow keys; press **N** for presenter notes. |
| `standalone.html` | The same deck as ONE self-contained file (every photo stored once) — to email, upload or publish. |
| `<Client> Proposal.pdf` | One slide per page, exactly as presented — for sending. |
| `assets/call-script.jpg` | A one-page script for the client's team, opened from inside the deck. |
| `source/facts.md` | The facts sheet every word of the deck is checked against. |

## The template

`assets/template/` is a complete, working deck: 23 slides, every animation and interaction, a build system and the
fictional worked example. **Always start from it** — copy it into a new project folder and port it. Don't write a deck
from scratch, and don't "simplify" components out of it: the structure is the product of many rounds of live client
feedback, and each page earns its place (see `references/slide-playbook.md` for what each one is for).

Things in the template that are NOT finished content, by design:
- `⟦…⟧` markers — anything that must be real and supplied by the user: their results, testimonials, case studies,
  and every third-party statistic or news headline. The build lists every marker still in the deck.
- `assets/ph-*.jpg`, `proof-*.jpg`, `brand-*.png` — labelled placeholder images ("PHOTO PLACEHOLDER · what goes here").
  The build lists every placeholder still referenced.
- Everything about Kestrel Bay Resort and Harbour Lane Media — fictional. Never let it reach a real client.

## The deck, in order

The argument runs in three chapters. Read `references/slide-playbook.md` before writing any slide.

| # | id | Page | Its job |
|---|---|---|---|
| 1 | `cover` | Cover | Their product, their logo, one plain promise. |
| 2 | `summary` | Where we're up to | Their situation → the plan → the work, in three tap-to-open cards. |
| 3 | `bridge` | The exact strategy | "This is what we're about to show you, and what it has done" + three proof numbers. |
| 4 | `case` | One case study | The closest real result: photo, quote, three or four numbers. Nothing else. |
| 5 | `cases` | Past results | Real platform screenshots + a totals band. |
| 6 | `ch1` | **Chapter One** | The opportunity in front of you. |
| 7 | `whynow` | Why now | Converging real-world forces, with dated, linkable sources. |
| 8 | `gap` | Why they say yes to *you* | The three questions a buyer must have answered — and why this client answers all three. |
| 9 | `catchment` | The reach | A real map; tap a tier and it lights up; population × share = the addressable market. |
| 10 | `numbers` | The pace | Three linked dials: budget ↔ enquiries a day ↔ cost per enquiry. The prospect sets the pace. |
| 11 | `forecast` | Your numbers, not ours | Their conversion and their prices → what a quarter could be worth, less ad spend. |
| 12 | `ch2` | **Chapter Two** | The campaign, already built. |
| 13 | `how` | The named funnel | The showpiece: a live demo — the customer's phone, the CRM record and the sales team's phone, wired together, playing. |
| 14 | `structure` | The build | The whole account on one page: products × locations × angles × formats = every live ad, explorable. |
| 15–18 | `ads1`–`ads4` | The creative | Finished ads, one page per angle, no two alike, each with a "why it works" flip. |
| 19 | `stories` | Full screen | Eight full-screen story ads, eight different native treatments. |
| 20 | `paper` | On paper | The 90-day plan as eight A4 pages — tap to read. |
| 21 | `reporting` | The weekly report | The Friday email; click the attachment and the report opens. |
| 22 | `ch3` | **Chapter Three** | The case for saying yes. |
| 23 | `included` | The package | One long card built backwards from the price: what you get → what is guaranteed → one price. **The deck ends here.** |

Optional modules in `assets/template/optional/` (the three-screen enquiry form, soft next steps, a finale) are added
only when a deal needs them — see the README there.

## Workflow

**Tools, once per machine.** Python 3 (with Pillow for the PDF) runs the build. For screenshots and QA, either
Node 18+ with `npm i puppeteer-core` run inside `<skill-dir>/scripts/` (it drives an installed Chrome/Chromium; or
`npm i puppeteer` to download one), or Python with `pip install playwright && playwright install chromium` and use
`scripts/shoot.py` instead of `shoot.mjs`. If neither can be installed, you can still build — but say plainly that
the deck hasn't been looked at in a browser, and ask the user to open `standalone.html` and send screenshots.

### Step 0 — The user's own business (first proposal only)

The template's agency side is fictional. Before the first proposal, collect the user's real details and keep them in
`source/our-business.md` (the template ships a filled-in fictional example — copy its shape; reuse the file for
every later proposal):
- business name, logo or monogram, presenter name, email, phone;
- what they sell and how they deliver it (steps, timelines — the go-live promise, e.g. "live within six days of
  onboarding", and how fast enquiries get called);
- whether their tools can really do what the template shows — e.g. verifying a mobile and an email by code before an
  enquiry counts. If they can't, cut that step from the film, the form and the guarantee that depends on it;
- **their proof**: real result counts, real money figures, platform screenshots, testimonials *with permission*, one
  strong case study. Ask for the screenshots themselves, not a summary;
- their normal pricing, term and payment terms (paid on signing? monthly in advance?) — **their terms win over the
  template's defaults** — and which guarantees they will actually stand behind (`references/offer-and-pricing.md`);
- the tools they use (ad platform, CRM, booking), and what they don't do (where their service stops).

**Never invent proof.** No made-up case study, testimonial, result, client name or "representative" example presented as
real — it is misleading conduct, and it collapses the first time a prospect asks for a reference. If the user has no
proof yet, cut the `case` and `cases` pages and sell the system instead (the demo, the build, the plan), and lean on the
guarantees. If the proof exists but isn't in hand yet, keep the pages with their `⟦…⟧` markers, tell the user exactly what to send
(the screenshots, the numbers, the client's permission), and cut the pages if it hasn't arrived by the time the deck goes
out. If the user asks you to add a result you have reason to think is generated, say so in two lines and offer
the honest alternatives: a real result with the name withheld, or a page clearly labelled as a projection.

### Step 1 — Intake on the prospect

Ask only what research can't answer:
1. Who is it, and what exactly is being sold — one product, one development, or their whole business?
2. **What is their role?** The owner of what's sold (a developer, a manufacturer, a clinic), or a middleman (an agent,
   broker, advisor, reseller)? This changes the whole argument — see `references/slide-playbook.md` → "The client's role".
   Look for the tells yourself: "presented by" vs "developed by", "access to" stock vs "our development".
3. Budget: ad spend per month, and the all-in ceiling for the deal. **Who pays the ad platform** — inside your price, or
   on their own card? (It changes the stack, the price card and the maths.) Term (one quarter is the default). Currency.
4. Their CRM, who will call the enquiries, and how many a day they can actually call (that caps the pace you recommend).
5. Live call or sent as a PDF? When? (A PDF must explain itself — the reasons live on the page, not in the notes.)
6. Anything they said on a call. Their words shape the talk track and the presenter notes — **never** a slide that
   quotes or lists their brief back to them. Show you understood by writing their situation in your own words.
7. Anything to leave out.

### Step 2 — Research → the facts sheet

Read their website, brochure, price list and any document they sent (use web search/fetch if you have it; if you
don't, ask the user to paste the pages or send the PDFs). Write `source/facts.md` in the template's shape
(it ships with a filled-in example): who they are and their role · the product with exact prices, sizes, features ·
**DO NOT USE** (anything unverified, conflicting or risky — dates, yields, tenure, room counts, third-party claims) ·
photos available · your side · the deal · the ad sets · the qualifying questions · the pipeline stages · market data.
Every line carries its source and the date you read it.

**The facts sheet is the only source of truth.** If a sentence in the deck can't be traced to it, it doesn't go in.

- Save their own photography into `assets/` over the matching placeholder. Use their real photos for any claim about
  their product — never stock. Stock is only for lines about the place or the market in general.
- "Why now" facts must be real, recent, dated and linkable; news headlines are quoted exactly as published.
- Mine their own documents for numbers that are already theirs — a marketing budget line in their prospectus, a
  pre-sales threshold, a launch date — and build the argument around those (`references/offer-and-pricing.md`).
- Note which true facts can appear in the deck but **not in the ads** (in Australian health advertising, for example,
  reviews and testimonials are off-limits in ads) — mark them "deck only" in `facts.md`. See
  `references/copy-and-creative.md` → "Numbers and claims" for regulated industries.
- Checking their current ads? In Meta's Ad Library, filter by each country — the EU transparency panel only shows the
  EU part of an ad's audience, so "it doesn't run in Australia" read off that panel is often false.

### Step 3 — Design the offer before writing a slide

Read `references/offer-and-pricing.md`. Decide it on paper, in `source/offer.md` (the template's example shows the shape,
including the sum check): the value stack (lines, prices, groups — they must sum), the
anchor, the one price and the named reason it's lower, the guarantees (each with a name, a promise, a remedy and its
conditions), the payment point and the term. The whole deck builds towards this page, so it has to exist first.

**When the user hasn't given you something** (no guarantees named, no go-live time, no proof yet): facts become `⟦…⟧`
markers; offer elements you design (a guarantee, a stack price, a discount) go in the deck but are listed back to the
user as proposals to confirm — never presented as decided.

### Step 4 — Copy the template and port it, slide by slide

```bash
cp -r <skill-dir>/assets/template ./<client>-proposal && cd ./<client>-proposal
```

1. `deck.config.json`: the title; `palette` (map the template's colours to the client's brand colours); and `residue` —
   the template's own names (Kestrel, Tidewater, Harbour Lane, Garden Suite, Ocean Suite, Alex Morgan, Sarah Mitchell…)
   so the build flags any that survive. When you later port from a *previous client's* deck, put that client's names
   **and concepts** in `residue`.
2. Replace the brand files (`assets/brand-*.png`) with the client's logo (white + dark versions) and avatar.
3. Go page by page with `references/slide-playbook.md` open: rewrite every line from `facts.md`, keep each page's
   structure and length, rewrite every presenter note. Big pages are **generated** — edit the generator in `build/`
   and re-run it; never hand-edit its output (each generated file says so in its first lines).
4. `src/script.js` → `CFG` holds the deal numbers (budget, cost per enquiry, price, stack total). Every number that
   appears on more than one page is driven from there or from the dials (`data-live`) — never retyped.
5. **Sweep the shared facts that are written into many pages** — grep for each and change every instance together:
   the go-live promise (`six days`, `6 days`, `Six-Day`), the call speed (`five minutes`), the price and fee, the pace
   (`$25`, `160`, `480`), the six form questions, the demo customer (name, city, answers, score), the pipeline stages,
   the CRM's name, the clocks/time zone in the film (`Bali time is Perth time`), and the lead-score table
   (`SCORES` in `src/script.js` — keyed on the exact option text of the six questions).

The template's own build report lists its example names as RESIDUE — that's the `residue` list doing its job; clear
them all as you port.

**Sell only what the user actually delivers.** The template's agency sells a specific service list — the campaign, a
call script and training calls, code verification, a "nurture bank", a phase-two film and landing page, a weekly
review, and paying the ad platform on the client's behalf. Check every one against `source/our-business.md` and delete
whatever the user doesn't do — from the package stack, the guarantees, the film, the plan pages, the summary and the
notes. Porting the template faithfully would otherwise sell the prospect things nobody will deliver.

**A find-and-replace is not a port.** Swapping names leaves the previous client's *reasoning* behind: an ad saying
"finished and furnished" for a project still under construction, a "buying overseas safely" angle for a local buyer, a
middleman's commission figure in a developer's deck. After the swap, read every page — ads, captions, form questions,
notes — as the new client would, and grep for the old client's concepts as well as their names.

With subagents available, split the port the way the template is split — one agent per section, one shared brief,
each editing only its own files. `references/build-and-qa.md` has the brief template and the file map.

### Step 5 — Build, look, fix

```bash
python3 build/build.py                         # writes index.html + standalone.html, prints what's unfinished
node <skill-dir>/scripts/shoot.mjs . shots     # one JPG per slide at 1440px — then LOOK at every one
node <skill-dir>/scripts/shoot.mjs . --check   # console errors, broken images, NaN on screen, overflow, markers left
node <skill-dir>/scripts/operate.mjs .         # drives every dial, tier, tab, flip, the film — prints what followed
```

Read every screenshot yourself. Then check what `operate.mjs` printed — the dials, the map tiers, the tabs, the
flips, the film's Play button, the report attachment, the plan pages — and that the numbers follow them. A page that *looks*
sparse is a bug to investigate, not a design choice (elements can be painted underneath others). Repeat until the build
report and the check are clean, apart from markers you are deliberately handing back to the user. Details:
`references/build-and-qa.md`.

### Step 6 — The adversarial pass, before the user sees it

Do the audit yourself so the user doesn't have to catch things. For every page:
1. Does anything sound machine-made, fake-personal, poetic or clever? Would the presenter say every word out loud?
2. Does it serve the prospect, or just us?
3. Is any claim unverified — especially about a third party? Is every number traceable to `facts.md`?
4. Does anything lower the prospect's belief that this can work for them?
5. What is the obvious objection, and is it answered (in one line on the page or in the note)?
6. Is there a reason to act now?

Then the cross-deck checks: every number that appears twice agrees (budget, cost per enquiry, enquiries a quarter, the
price, the stack total, the guarantee figure vs the calculator); two pages never use the same word for different
quantities; the fee never appears on the forecast page; the price appears nowhere before the package's price section;
every ad's ad-set label is right; no two ads on a page share a layout or an angle.

**If a fact check kills a page's main point, recommend cutting the page** — don't rebuild it around weaker leftovers.

Present the deck with a short list of what you checked, what you fixed, every `⟦…⟧` still open and every judgement
call the user should confirm (currency, pricing, a guarantee, a claim you couldn't verify).

### Step 7 — Deliver

- **Live link.** If the environment can publish HTML (an artifact or hosting tool), publish `index.html` with the
  `assets/` folder as supporting files, or `standalone.html` alone when it is under ~16 MB. Otherwise hand over the files.
- **PDF.** `node <skill-dir>/scripts/shoot.mjs . pdf-shots --scale 1.5` then
  `python3 <skill-dir>/scripts/make_pdf.py pdf-shots "<Client> Proposal.pdf"`. One slide per page, exactly as presented,
  under 15 MB. Never the browser's Print → PDF: it reflows to A4, shifts slides and cuts them across pages.
  A **send-only** PDF must stand alone: move the reasons from the presenter notes into the visible copy of the summary
  and the price card, and state the period on every price.
- **Call script.** Rewrite `build/call_script.html` for the client, then
  `node <skill-dir>/scripts/render_page.mjs build/call_script.html assets/call-script.jpg` and rebuild.
- Tell the user how to present: arrow keys step slide to slide, **N** shows the notes, the dials and buttons are live.
  **On a video call, share a window that does NOT have notes on** — open the deck twice (share one, press N in the
  other on a second screen), or keep the notes open on a second device. Notes are part of the page: a shared tab shows them.

## The rules that matter most

These come from real deals won and lost. The reference files explain each one.

1. **Facts only from `facts.md`.** Never invent a statistic, quote, testimonial, review, result or news story. A `⟦…⟧`
   marker is always better than a plausible guess.
2. **Know the client's role** before writing a word. An owner's deck sells the product; a middleman's deck sells the
   middleman.
3. **Keep the proven structure.** Port page for page; add a page where it earns money; never merge core pages into a
   "master slide", never redesign an approved page unasked, never quote the prospect's brief back to them.
4. **Plain words.** Each headline is a plain fact plus its consequence; each point is "X, so Y". No metaphors, no
   slogans, no clever contrasts. If the presenter wouldn't say a word out loud, it comes out.
5. **The slide is for their eyes; the note is for the presenter's mouth.** Anything said once, out loud, lives in the
   note. A value page that works can be ~80 words. When cutting leaves a page sparse, enlarge the visual — don't write
   copy back in.
6. **Show, don't tell.** Every page adds evidence, a working demo, a finished asset or a control the prospect operates.
   A page that restates a claim in new prose gets cut. Interactivity is how one page carries real depth and stays simple.
7. **Creative is finished work.** Ads are designed statics (headline, price, feature strip, logo composed on the photo),
   on the client's real photography, no two alike in layout or angle, labelled with their ad set.
8. **One set of numbers.** Anything on an interactive page drives every other mention of it. Conversion assumptions
   are a published third-party benchmark or the prospect's own figure — never yours — and they live on the forecast
   page as a slider, never as a bare stat tile.
9. **Price last.** The package is built backwards from one price: value stack → guarantees → struck anchors → the price
   with a named reason. The prospect's revenue never appears on the price page; your fee never appears on their
   revenue page.
10. **Guarantees have names and remedies.** Name + hard promise + a bounded make-good + "that is the only remedy" +
    the conditions that keep it alive. A bare promise is more dangerous than one with a remedy.
11. **Verify what renders, not what the code implies.** Screenshot, read, operate. Then audit adversarially.
12. **When a premise dies, cut the page.**
13. **Agreements contain only what was said on the call.** A term the presenter never raised out loud stays out.

## Reference files

| File | Read it when |
|---|---|
| `references/slide-playbook.md` | Writing or reviewing any page — each page's job, contents, copy pattern, note, pitfalls. |
| `references/offer-and-pricing.md` | Designing the package, the price, the guarantees, the next steps, the agreement. |
| `references/copy-and-creative.md` | Writing any line, presenter note or ad; choosing photos; building ad and story treatments. |
| `references/components.md` | Changing how a page works — every interactive/animated component, its code, its data, its hooks. |
| `references/build-and-qa.md` | Building, previewing, parallel agents, QA, PDF export, publishing, file sizes. |
| `references/adapting.md` | The prospect isn't a property developer, the market isn't Australia, or the service isn't ads. |
