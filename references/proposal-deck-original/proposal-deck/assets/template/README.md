# Proposal deck template

A complete, working proposal deck with a fictional worked example: **Harbour Lane Media** (an ad agency) pitching
**Kestrel Developments** a launch campaign for **Kestrel Bay Resort**. Every name, fact and logo in it is invented.
Photos are labelled placeholders; anything that must be real (results, testimonials, news, market statistics) is
marked `⟦…⟧`.

**See it:** double-click `standalone.html` (it ships prebuilt; `python3 build/build.py` rebuilds it). Arrow keys move slide to slide;
press **N** for the presenter notes; drag the dials, press the map tiers, press Play on the funnel film.

**Use it:** never edit this copy — copy the whole folder for each new proposal and follow the skill (`../../SKILL.md`):
facts sheet first (`source/facts.md` shows the shape), then the offer, then port slide by slide, then build, look, fix.

| Path | What |
|---|---|
| `deck.config.json` | title · colour re-skin · words the build must flag as leftovers |
| `source/facts.md` | the facts sheet — the only source of truth for the deck's copy |
| `src/` | one file per slide (in order) + shared CSS + `script.js` (the deal numbers and the dials) + `js/` modules |
| `build/` | `build.py` (assemble + report) and the generators for the big slides — edit a generator, then re-run it |
| `optional/` | extra slides to add when a deal needs them (see its README) |
| `assets/` | photos, logos, fonts, music, map data |
