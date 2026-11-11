# Disagreements with SYSTEM.md v1

29 October 2026 · Codex review · Design only. No outreach or live changes.

## 1. The proposed stack is not yet “fully agent driven” at the quoted price

Section 1 says API-direct with Apollo Basic and Instantly is fully agent-driven. Section 7 says those exact API plan entitlements are unknown. Those cannot both be the current status. Change the table to **“proposed; endpoint and plan access awaiting verification”** and the cost to a provisional scenario. Keep API-direct as the architectural preference, but do not advertise a tested member stack yet.

Require a capability check for company search, people search, email/mobile enrichment, campaign enrolment, pause/removal, replies and webhooks on the actual purchased plans. A manual CSV import is a viable fallback but changes the member workflow and the automation claim. Account for CRM/bridge hosting, model research usage, operator time, domains and mailboxes separately from data/sending subscriptions. If these are included in another membership cost, name that assumption rather than charging twice.

Apollo's [official API pricing documentation](https://docs.apollo.io/docs/api-pricing), inspected in this review, explicitly says endpoint charges and limits vary with plan and recommends a small request followed by credit-usage inspection. It does not establish that this entire design runs on Basic.

## 2. Places API access does not resolve the CRM storage/export design

Sections 2 and 4 imply that using the official API makes it acceptable to build a durable prospect list of website, phone, rating and hours. Google's [Places API policies](https://developers.google.com/maps/documentation/places/web-service/policies) explicitly restrict prefetching, caching and storing content beyond allowed exceptions; place IDs are exempt. Display attribution also applies. This is an execution-design issue, not a minor terms footnote.

Before adopting Places as the prospect database, map permitted field use, retention, display and export against the applicable terms. Store provenance and retention policy per source. Website contact details independently obtained from an allowed source need their own provenance; copying a Google result and changing its source label is not independent collection. If the intended prospecting/storage use is not permitted, use a suitably licensed business-data source. The existing free-course finder is a reuse candidate, not evidence this issue was solved.

## 3. Free ASIC officeholder lookup is unsupported

Stage 4 says the free weekly ASIC dataset gives officeholders. `research-tools.md` says the opposite is unverified. ASIC's [official company-register guidance](https://www.asic.gov.au/online-services/search-asic-registers/company-and-organisation-registers), inspected here, puts officeholder details in paid company extracts; free information is basic company metadata. I could not reopen the data.gov.au dataset due to a 403, so I cannot validate its schema. Remove the asserted free-officeholder step until the actual dataset fields are inspected.

Use ABN/ASIC for entity matching, then public team pages, manual LinkedIn research, phone confirmation or a separately approved paid extract for buyer identification. A sole-trader entity name or registered officeholder is still not a confirmed operational buyer.

## 4. Section 3 needs per-contact rules and a separate programme-policy column

Several rows combine legal permission, channel policy and unresolved research into an unconditional “Yes.” Replace that with eligible / review / blocked, supported by a recorded basis. In particular:

- “AU cold email only under conspicuous publication” is too absolute as a statement of law. The [Spam Act Schedule 2](https://www.legislation.gov.au/C2004A01214/latest/text) has a basic consent definition as well as the publication provision. The publication provision also requires a reasonable assumption that publication occurred with the relevant person's or organisation's agreement. A URL plus role relevance alone does not capture every condition. A restricted programme policy for first-contact email is fine, but identify it as that policy.
- Manual LinkedIn/Instagram/Facebook sending must not automatically bypass electronic-message eligibility checks. Human clicking resolves one automation question; it does not establish recipient permission or compliance with applicable messaging law. Route manual messages through Claude's jurisdiction/channel assessment as well.
- US “personal mobile: not cold, consent first” and “SMS: not taught” can be sensible v1 policy choices. Label them programme policy rather than universal statutory summaries. The research already distinguishes manual calls from artificial voice and multiple legal regimes.
- Publication of an AU mobile as a business number must not automatically mark it callable. The same document recognises mixed-use registered numbers. Make the necessary number checks, suppression and local-time rules explicit before eligibility is granted.
- A reply, booking or conversation alone is not blanket permission for marketing SMS. Record what text the person agreed to receive and route by its scope.

Exact calling hours and other items marked unverified must become a resolved executable rule or a blocked configuration before a live pilot. A draft design can retain them as questions; a scheduler cannot interpret “roughly” or “to confirm.” This review is not a replacement legal opinion.

## 5. Google's sender requirements are overstated, and warmup is not proof of readiness

Section 2 calls SPF, DKIM, DMARC, separate domains and warmup Google rules “at any volume.” Google's [sender guidelines](https://support.google.com/a/answer/81126), inspected here, distinguish all-sender requirements from bulk-sender requirements. Separate sending domains and a two-to-three-week warmup are our proposed operating choices, not requirements established by that page.

Keep strong authentication as our implementation standard, with honest sender identity. Replace calendar-based readiness with actual authentication/alignment checks, a controlled delivery test and monitored failures/complaints. Elapsed warmup time does not guarantee delivery. The stated spam threshold is a ceiling to stay below, not a target success rate.

## 6. “Stops every pending touch” requires provider and manual-queue integration

Stage 6 promises a global stop but Stage 7 leaves LinkedIn, DMs and calls manual. Without a tested event source, Jarvis will not automatically know that a member got a reply there. Add a member action to log the reply/booking/opt-out and immediately pause the contact/account. Every manual task should recheck current state before the member acts.

Also keep the original design's provider-side cancellation, action deduplication, event reconciliation and ambiguous-send-timeout handling in the merged system, not only the earlier handoff. Specify event ownership and a recovery queue. A local paused flag cannot recall a dispatched email or guarantee a provider removed a queued one. Do not claim instant global cancellation before measuring it across the chosen adapters.

## 7. The planning funnel still hides assumptions and changes units

“Two closed deals needs roughly seven call ones” assumes approximately 29% conversion from booked first calls to wins. Attendance, qualification and progression are not shown. Seven meetings at a 1% booking rate implies 700 contactable units only if the denominator is unique contacts; it does not automatically imply 700 accounts. Multiple contacts at one company must not inflate the buyer-market or meeting count.

Use an adjustable scenario with every stage shown and replace inputs with measured data. The 0.5% to 2% booking assumption is our sensitivity range, not a course benchmark. Thirty accounts can expose data and message problems; it cannot establish that scoring improves sales. “Second campaign bigger only if signals work” needs a practical criterion: accurate reviewed fit, functioning delivery/suppression, affordable cost and useful buyer feedback. It must not imply statistical proof from the first batch.

## 8. Build order omits Phase C and cannot call Phase A a proof of the real workflow

Section 8 jumps from A/B to authorising Phase D. Put **Phase C, the real student Base44 rehearsal, before any prospect launch**, then resolve remaining sender configuration and channel rules. Mock fixtures test proposed logic; they do not prove installed skills, connected providers, durable schedules or stop behaviour.

Use: provider/capability selection → coordinator and data contract → offline fixtures → authorised read-only data pilot → student Base44 integration rehearsal and separately authorised team-owned transport test → reviewed launch manifest → live pilot → later comparison.

Phase B results can produce the account-research lessons. They cannot substantiate sending, deliverability, reply-handling or acquisition-outcome lessons. Draft those parts as procedures, then complete them from the appropriate later phase.

## 9. Some fit signals require inference or would themselves contact the prospect

“Contact form that goes nowhere” cannot generally be established by looking at the page. Do not test-submit prospect forms during the read-only lab. Record visible usability failures without submission, or leave delivery unknown. Detectable site software likewise does not prove the internal CRM or a missing capability. “No online booking,” old posts and review velocity need to be tied to this offer's account definition rather than treated as universal pain indicators.

This matters commercially: a perfectly contactable account with weak fit should not outrank a well-matched business merely because its public website exposes more fields. Maintain unknowns separately from negative findings and inspect a sample of lower-ranked accounts for missed opportunities.
