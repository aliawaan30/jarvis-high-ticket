---
name: jarvis-ad-library-offer-research
description: Find offer ideas by inspecting Meta Ad Library ads and their destination pages, then recommend a specific niche and offer adaptation.
---

# Find an offer through the Ad Library

Use the target country, service interests and available delivery support. The team's 30 October 2026 test used Claude with the Meta Ads connector and an account with an active ad account. This tested search is not available inside a Base44 Jarvis. Have the member run it in that connected environment and bring the results back to Jarvis, or use another available, permitted source without pretending it has the same fields or coverage.

## Two-step search: find pages, then count per page ID

1. **Find the pages.** Search specific service phrases in the target country, then collect and deduplicate relevant advertiser page names and page IDs. In the tested connector, a keyword search returns 25 ads from an estimated total, not the total ads run by each page. Generic phrases can produce irrelevant results: the team's AU `missed calls` search returned an estimated 9,098 results, with novel/drama apps on the first page. Narrow by the actual service and inspect relevance; do not rank pages from their appearances in a single search batch.
2. **Count and rank them.** Look up each relevant page separately by its page ID, with active status and the target country filter. Record the per-page `estimated_total_count`, retrieval date and filters. Keep estimated totals distinct from records actually returned or paginated through. Rank candidates for inspection using these page counts and run dates; do not sum keyword-result batches as a page's active count.

The tested result fields include page name, page ID, link headline, creation/start time, snapshot URL and currency. They do not include ad body text or impressions. Use the link headline only as a **hook proxy**; a missing headline means the hook is unknown. Open the snapshot URL to inspect the full ad text and creative, and tell the member to open it if this agent cannot. Then inspect the destination page. Never describe a headline-only record as a full ad inspection. An absent impressions field in this connector does not establish that Meta never makes reach/impression information available elsewhere.

The team's 30 October afternoon per-page check reported Enhanced AI (UK) 20, Tradie Pulse (AU) 14, BrokerGrow (AU) 12, Callacy AI (AU) 11 and Switched On AI (AU) 5. These are dated, country-filtered observations, not permanently current rankings or profit evidence. Refresh them when researching a new offer.

Look for sustained activity and distinct creative angles. Blake's 15+ heuristic flags advertisers to investigate, not proven winners. A per-page count may cover multiple offers, duplicated ads and variants: it is not a count of unique concepts or proof one offer has 15 creatives. Inspect and group ads before making that narrower claim. Record dates and advertiser/page IDs. Where another inspected source supplies impressions or reach, record the metric, country, period and whether estimated; otherwise mark unavailable. Counts, longevity and reach do not independently prove spend growth or profit.

Extract the buyer, outcome, mechanism, timeframe, risk reversal, proof and qualification. Read the landing page before recommending an adaptation. Competitor results remain competitor claims, never the member's authority.

Recommend a meaningful adaptation for the same niche or a similar mechanism for a different niche with the relevant problem and delivery route. Changing a niche label is not enough. Do not copy branding or unsupported claims.

Return one short decision card: observed offer and links; activity evidence and limits; proposed niche; plain-English problem/solution; adaptation; one next validation action. Save detailed source records separately. If access is blocked, request an export or manual inspection rather than claiming to have viewed it. Hand the chosen idea to `jarvis-offer-creation`. No campaigns launched.
