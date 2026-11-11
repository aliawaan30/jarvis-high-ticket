# Adapting the deck to a different business, market or offer

The template's example is a lead-generation agency selling a paid-social campaign to a property developer, aimed at
Australian buyers. Underneath, the deck is a general argument that fits any service sold to a business:

| Chapter | The general question it answers | Template page(s) |
|---|---|---|
| Opening | *Do these people understand my situation, and have they done this before?* | summary · bridge · case · cases |
| One — the opportunity | *Why now? Why would my customers choose me? Where are they? What does the pace cost, and what is it worth to me?* | whynow · gap · catchment · numbers · forecast |
| Two — already built | *What actually happens, step by step? How big is the work? Is it real? Is it thought through? Will I know how it's going?* | how · structure · ads1–4 · stories · paper · reporting |
| Three — the case for yes | *What do I get, what's guaranteed, what does it cost?* | included |

Keep that argument and the page order; change what each page shows. Port page by page — don't restructure.

## Mapping the pages to other services

| Page | Lead-gen / ads (template) | SEO / content | Website / design | Consulting / B2B service | Software / implementation |
|---|---|---|---|---|---|
| `gap` | Three buyer questions the product answers | Three searches their customers make that competitors don't answer | Three things visitors need to see before they enquire | Three problems their market has that they solve best | Three jobs their team is doing by hand |
| `catchment` | Where buyers live, by tier, on a map | Search demand by topic cluster / region | Their visitor sources and devices | Their target accounts by segment / region | Teams / sites / users to roll out to |
| `numbers` dials | Ad spend ↔ enquiries/day ↔ cost per enquiry | Articles/month ↔ ranking pages ↔ visits | Pages ↔ timeline ↔ budget | Hours/month ↔ workstreams ↔ fee | Seats ↔ modules ↔ price |
| `forecast` | Enquiries × (1 ÷ enquiries per sale) × price, less ad spend | Visits × conversion × value | Visitors × enquiry rate × value | Hours saved / revenue added × their rate | Time saved × cost of time, less licence |
| `how` film | Ad → form → codes → alert → call → reservation | Search → article → CTA → enquiry → sales call | Landing → key page → form → booking | Kick-off → diagnosis → plan → delivery → result | Request → system → approval → done |
| `structure` wall | Products × locations × angles × formats = live ads | Pillars × topics × formats = pieces | Sitemap: sections × pages × components | Workstreams × weeks × deliverables | Modules × teams × integrations |
| `ads1–4` | Finished ads per angle | Finished sample articles / page outlines | Finished page mock-ups | Finished sample deliverables (a memo, a dashboard, a workshop agenda) | Configured screens with their data |
| `stories` | Full-screen story ads | Social cut-downs | Mobile screens | One-page summaries | Mobile / notification views |
| `paper` | 90-day marketing plan | 90-day content plan | Project plan & spec | Engagement plan | Implementation plan |
| `reporting` | Weekly ad report email | Monthly traffic report | Launch report | Weekly status note | Adoption dashboard |

The rule that carries everywhere: **build their deliverables before they say yes.** The finished ads are what made the
original work — for another service, the equivalent is a finished sample made with *their* name, photos, prices and
data: a page, an article, a dashboard, a screen.

What changes in code for each:
- Page copy and presenter notes: everywhere (`src/s*.html`, generators in `build/`).
- The dials and the model: `CFG` and `media()` / `calc()` / `earn()` in `src/script.js`, and the slider ranges and labels
  in `src/s10_numbers.html` / `src/s11_forecast.html`. Every derived figure elsewhere is a `data-live` span — keep using them.
- The film: the step list (`Dir`), screens and captions in `build/gen_how.py`; motion in `src/js/journey.js`.
- The wall: the data at the top of `build/gen_builds.py` (products, locations, angles, formats, targeting, photos).
- The creative: the treatment functions and the per-page ad lists in `build/gen_ads.py`; `src/s19_stories.html`.

## A local service business (clinic, trades, studio, gym)

- **The "stock" is capacity** — chairs, appointment slots, a crew's week. There's no sell-out story; the pace dial is
  capped by how many enquiries the team can call and book, and the forecast is enquiries → booked → attended →
  treatment/job accepted × its value.
- **The reach is a radius, not a country.** Draw the real area (council or postcode boundaries) with true-distance rings
  (e.g. 5/10/20 km or a drive-time), populations per area from the statistics office, and the share that's relevant
  (an age band, homeowners) — each with its source.
- **The funnel** usually ends in a booking link or a reception call within the hour; the outcome card is "Booked"
  and "Attended", not "Reserved".
- **The creative** must pass the vertical's advertising rules (see `copy-and-creative.md` → regulated industries).
- **Account size:** a few ad sets (one per service, plus retargeting), not dozens.

## A different market or country

- **The map.** Replace the geography with real boundaries — never a hand-drawn shape. (The template's catchment map is a
  simplified outline labelled "illustrative"; the wall's map uses real Natural Earth state boundaries. For a real client,
  build the real one.) `scripts/osm_map.py` fetches OpenStreetMap boundaries and writes a projected SVG with true-distance
  rings — read its header. Gotchas: search by OpenStreetMap relation ID when a name is ambiguous (a town name can return a
  club or a street); council outlines often include lakes and estuaries, so cut the water polygons out; land outside
  the polygons you fetched reads as sea, so fetch the neighbours or crop the frame; one huge, mostly-empty district
  shrinks everything else — crop to the towns that matter. Country/region outlines:
  Natural Earth (public domain) or OpenStreetMap's Nominatim (`…/search?q=<place>&format=json&polygon_geojson=1&polygon_threshold=0.001`,
  with a descriptive User-Agent, respecting its usage policy). Project lon/lat into the SVG viewBox (x scaled by
  cos(latitude)). The template's Australian state paths live in `assets/cb-aus-paths.json` and inline in the wall data.
- **Tiers.** Rank regions by how likely and how reachable the buyers are (proximity, travel routes, affinity), each
  with a population from the national statistics office, dated.
- **Currency.** `aud()` in `src/script.js` formats money with `en-AU` and `$`; change the locale and symbol. Show both
  currencies where the product is priced in one and bought in another, with the rate and "about".
- **Language and spelling.** `<html lang>` in `tpl/00_head.html`; spelling of the prospect's country throughout.
- **Rules and compliance.** Check the ad platform's special categories for the vertical and country (housing, credit,
  employment, financial products, health) and the local consumer-law rules on guarantees and testimonials.

## A different brand

- **Colours:** `deck.config.json` → `palette` maps the template's canonical colours (navy `#13283A`, deep navy
  `#0C1B28`, ink `#16212B`, sand `#B57A2E`, gold-lite `#E2B872`, gold-dark `#9A6420`, ivory `#F4EFE7`, paper `#FCFAF6`,
  sand-lite `#F3EADB`) to the client's. Keep enough contrast; the deck is light-themed with dark bands.
- **Type:** Playfair Display (display) + Jost (text) are set in `tpl/00_head.html` (`@font-face` and the font stacks).
  Swap both files in `assets/` and the family names if the client's brand demands it. Ad-creative display faces
  (Anton, Bebas Neue, Archivo Black, DM Serif, Caveat, Permanent Marker, Space Mono) are in `assets/fonts/` — all
  open-licence.
- **Logos:** `assets/brand-logo-light.png` (white), `brand-logo-dark.png`, `brand-wordmark-light.png`,
  `brand-avatar.png` (square), `partner-logo-light.png` (a second party, e.g. an operator — delete its uses if none).

## When there's no proof yet

Cut `case` and `cases`, reword `bridge` to describe the system rather than its history ("This is the exact system we
are about to walk you through, built for <client>"), and let Chapter Two carry the weight — the working demo, the
finished deliverables and the plan are proof of competence. Lean on guarantees (the risk moves to you), and consider a
smaller first term. Never fill the gap with an invented example.
