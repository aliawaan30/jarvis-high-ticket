# Compact VSL and Offer Testing Landing Page

Blake removed the repeated written pain narrative, numbered process, long guarantee/responsibility section and generic FAQs. The VSL carries the deeper explanation. A separate no-VSL page permits offer testing before filming.

Reference check: read the retained funnel-visual-analysis notes and visually re-inspected `references/2026-10-22/scaleinfo-desktop.png`. Compact Scale Info is callout/headline/mechanism/video/CTA. FAQ videos were documented on Goh's confirmation page; Roofline's generic landing FAQs were our addition. Removed them rather than claiming reference fidelity.

## Changes

- `dist/index.html`: hero, marked VSL storyboard preview, CTA, progressive form, footer. No repeated pain, process, guarantee block, generic FAQ or redundant closing section. Removed the short guarantee/asterisk line too, so deleting its conditions does not leave an unconditional promise behind.
- `dist/offer-testing.html`: same outcome/mechanism and form, no VSL area, storyboard, player, oversized substitute image or empty video placeholder. Title/review label names **Offer Testing Landing Page**.
- `app.js`: optional VSL handlers are guarded; the common form still runs when video elements are absent. No data transmission or persistence added.
- Updated `jarvis-landing-page` with both modes and `jarvis-vsl-writer` with the page/script division. No new skill entry point added. Both structural validators pass.
- Preserved earlier source in `archive/before-compact-2026-10-31/`. Original owner-private hosted benchmark is historical; updated public course copy is the active shared example.

## Verification

Static checks confirm removed sections and details/FAQ accordions are absent, correct VSL presence per mode, shared form present, noindex retained. `node --check` passes.

Native Safari: no-VSL page rendered and visually inspected. Required-answer validation blocked blank submission; selected answer advanced to question two; Back restored question-one selection. VSL version rendered and visually inspected; storyboard opened at step 1/6. Existing contact/redirect logic is unchanged and was not re-run through all six questions in this revision. Narrow viewport was not visually tested in this run. Calendar remains a placeholder, no actual leads/bookings sent or saved.

No conversion or winning-offer claim. The no-VSL page is an experiment surface; distinguish form submissions, qualified bookings, attendance and purchases in a connected test.
