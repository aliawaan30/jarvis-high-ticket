# Five-site premium website test

> **Version 3 evidence.** Kept for its tested methods and results. Where it differs from the version 4 files (Higgsfield instead of Envato or Kie, the phone video loop, one enquiry pipeline owned by the website, the design system and surface rules), the version 4 files win.


10 September 2026. Blake reviewed the local collection and approved its appearance, then explicitly requested this method become the premium website skill.

## Actual builds

Open http://localhost:8766/index.html while the local server is running. The websites are served from `site/` and remain separate from existing Base44 apps.

| Page | Visual system | Film sections passing | 780 / 375 layout | Keyboard / menu / download | Reduced motion / data saving / failure |
| --- | --- | --- | --- | --- | --- |
| surf | Athletic / condensed / offset photography | 2/2 | Pass | Pass | Pass |
| restaurant | Warm editorial / serif / food and menu | 2/2 | Pass | Pass | Pass |
| landscape | Organic / botanical / material palette | 2/2 | Pass | Pass | Pass |
| architecture | Spatial / project gallery / restrained typography | 2/2 | Pass | Pass | Pass |
| product | Studio / material detail / room context | 2/2 | Pass | Pass | Pass |

## What ran

- Chromium through Python Playwright, real localhost pages.
- Ten film sections: currentTime sampled near 0%, 25%, 60%, 95%, then reversed to 30%, with tolerance 0.25 seconds.
- Independent decoded-frame pass at 0%, 50%, 100%, then 25%. Every film produced different decoded frames. Videos remain paused while scrolling controls time.
- Menu Escape, focus restoration and close-after-navigation at 375px.
- All three selector options activated by keyboard; exactly one selected state and panel. Actual text downloads saved to evidence/.
- Real anchor targets, source asset loading and console/pageerror collection. Zero normal-run console or runtime errors recorded.
- Width and text-overflow measurements at 780px and 375px. No measured overflow or clipped text in the checked headings, paragraphs and options.
- Phone, reduced-motion and data-saving sessions: zero MP4 requests. Forced video failures: usable still sections with pinned travel removed.
- Browser navigation away and back restores scroll mode.
- Full-page desktop and phone screenshots plus per-film timeline screenshots inspected.

## Repairs and rejected material

The old generated watch was rejected for invented lettering. The new product concept uses an unbranded lamp. Its room view initially had a different stem, so one reference edit corrected that still. The existing surfer footage was trimmed to 6.8 seconds before its weak tail. The surf and lamp phone crops were repaired with separate image and headline regions. Header contrast was strengthened. Browser-history restoration was added to the media lifecycle. Offscreen lazy images were explicitly loaded before full-page evidence screenshots, avoiding misleading empty image regions in the capture.

## Cost and assets

Final new batch: **624 Kie credits**. Starting balance 702.3, ending balance 78.3. Provider-reported per-job deductions reconcile with that difference. Twelve image jobs including the reference edit cost 78 credits; nine video jobs cost 546 credits. The budget bound was 650 credits. No duplicate jobs or video rerolls were purchased. Earlier stills and the existing surf clip are reused assets with separate previous costs.

Originals are outside the served `site/` directory. Kie key access is outside the frontend. Final web clips use local assets, not temporary provider URLs. All fonts are served locally. The following sizes are from actual processed files:

| Film | Used duration | Web bytes |
| --- | --- | --- |
| landscape-second | 5.06s | 2,933,692 |
| landscape | 10.05s | 7,431,736 |
| surf-second | 5.06s | 3,830,652 |
| restaurant | 10.05s | 4,075,997 |
| product | 10.05s | 2,073,554 |
| architecture-second | 5.06s | 1,901,272 |
| product-second | 5.06s | 1,395,708 |
| architecture | 10.05s | 4,995,021 |
| restaurant-second | 5.06s | 2,676,285 |
| surf | 6.80s | 5,148,655 |

## Limits

These are local business concepts with real navigation, selection and downloadable briefs. They do not process real bookings, payments or enquiries. Those integrations need actual client destinations and testing. The architecture/project imagery and product studies are generated concepts, not claims of built client work or saleable product specifications.

Mobile results are Chromium viewport emulation, not a physical iPhone or Android device. Live network performance, Safari and real Base44 app execution remain unverified. No Base44 credits were spent or measured in this local run. Active build time was not instrumented precisely and is unknown; provider generation durations remain in the raw job records. Do not infer them from chat gaps.

User aesthetic approval is recorded, but no price/value guarantee follows. A fresh-agent Base44 import and later small-brief generation test remain separate course validations.

## Reproduce

From the course project root:

```
python3 -m http.server 8766 --bind 127.0.0.1 --directory research/premium-lab-v2/site
python3 research/premium-lab-v2/check.py
python3 research/premium-lab-v2/visual-check.py
python3 research/premium-lab-v2/package.py
```

Playwright and its Chromium browser must be available for the two test commands. Rebuilding packages or rerunning the browser checks does not generate media or spend Kie credits. Do not run media submission commands to reproduce UI tests.

Raw records: `evidence/qa.json`, `evidence/decoded-frames.json`, `processing.json`, `media-state.json`. Screenshots are under `evidence/`. This record supersedes the overstated premium-lab-v1 report.
