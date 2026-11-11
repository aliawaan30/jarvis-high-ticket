# Proposal builder adaptation — 25 October 2026

Status: reference-inspected draft; structural validation passed. No complete generated client proposal, Base44 run or student test has been performed for this candidate.

## Inspected
- Original ZIP directory and full SKILL.md.
- adapting.md; first 150 lines of components.md; first 180 lines of offer-and-pricing.md; deck.config.json.
- Opened original index.html in local headless Chrome through Playwright. Confirmed 23 section IDs. Captured cover, summary, how and included; visually inspected summary, how and included screenshots. This was a sampled visual inspection, not a complete original-deck audit or animation/runtime test.
- Existing jarvis-offer-creation/SKILL.md for shared-brief and public-pricing requirements.

## Decisions
Keep buyer-specific explanation, restrained premium hierarchy, useful walkthrough and traceable numbers. Replace mandatory 23-section port with approximately six sections. Remove obligatory ad creative, map, cinematic sections and arbitrary value stacks. Keep pricing private and approved. Clearly distinguish prototypes from live integrations. No hidden guarantee limit or automatic legal clauses. Produce scoping proposals where implementation feasibility is unknown.

## Checks actually run
Skill creator quick_validate.py passed. ZIP and Markdown exports created from canonical skill. Single-file upload includes demonstration reference text so it has no missing reference-file dependency.

## Next behavioral test
Use a real approved brief and discovery notes to produce one full proposal. Inspect each rendered section, operate demo and calculator if present, and assess buyer clarity, technical scope and commercial consistency separately. Then test in Base44. A longer custom implementation may need an appendix; do not shorten by hiding material commitments.

## Original preservation
Original Downloads/proposal-deck.zip unchanged. Extracted reference retained at references/proposal-deck-original/proposal-deck. The new package deliberately does not include the villa campaign renderer; it supplies new instructions for a short output rather than claiming the old 23-section template has been rewritten.
