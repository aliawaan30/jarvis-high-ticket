# Offer skills and funnel sending recommendation

30 October 2026. Three entry points built; six-line offer creation implemented. No campaigns, phone purchases or sending connections activated.

## Names for the course

| Way | Course skill name | Existing material |
|---|---|---|
| 1. Study advertised offers | `jarvis-ad-library-offer-research` | New dedicated entry point. Inspects actual ads and destination pages; proposes one adaptation. |
| 2. Choose a service and niche | `jarvis-offer-menu` | New entry point replacing the broad opportunity finder as the menu route. Uses a maintained, reviewed offer catalogue. |
| 3. Find a custom opportunity | `jarvis-custom-opportunity-finder` | Short student entry point over the retained `jarvis-offer-discovery` research method, copied into its references. |

Canonical folders: `/Users/blakestephens/co-founder/projects/high-ticket-program/skills/`. The old `jarvis-opportunity-finder` and `jarvis-offer-discovery` remain for compatibility, not extra student choices. The first is broader research, not an existing proven-offer catalogue. No approved current scaling-offer catalogue was found, so Way 2 needs that maintained data before it can reliably serve the intended menu. Its entry point explicitly reports a missing library rather than inventing winners.

Update after Claude's next handoff: the catalogue now exists at `high-ticket-course/research/offers-scaling-2026-10-30.md` and is copied into `jarvis-offer-menu/references/`. The menu skill reads it by default. Earlier missing-catalogue status is superseded. Treat its page counts as agent-reported advertising activity; direct ad URLs/raw evidence ledger still need adding before stronger performance claims.

Ad Library activity is useful selection evidence. Keep Blake's 15+ creative heuristic, but separate distinct concepts from duplicate IDs and record available impressions/reach by period/geography. It is a research signal, not proof of profitable scale. Meta's [Ad Library API page](https://www.facebook.com/ads/library/api/) was blocked on direct fetch; indexed official results describe estimated UK/EU impressions, not universal commercial-ad performance. Actual ad inspection remains part of each future run.

`jarvis-offer-creation` now returns exactly: **Niche; Outcome; Timeframe; Risk reversal; Authority / proof; Unique mechanism**, with no appendix or expanded brief. DFY money-back / DWY work-free is the proposed remedy direction, not an automatic approved guarantee. The longer old skill is archived at `archive/offer-creation-before-six-line-2026-10-30/`. Scope and economics remain available in separate workflows.

`jarvis-confirmation-page` remains, updated with Blake's proof/testimonials, rapport video, calendar acceptance and reply-yes instructions. Actual booking state and reply-capable channels still matter.

## SMS and funnel email: CRM owns the workflow

**Recommend a member-owned Twilio number for two-way SMS, connected to the CRM. Email comes from the member's authenticated business mailbox through a tested CRM connection.** Jarvis prepares content, proposes responses and operates approved actions through that connection. It is not the sender identity or the storage system.

Use a number that supports the required country, two-way replies and registered use case. A branded alphanumeric sender is not a substitute for a reply-capable number. Preserve consent, sender identity, thread history, delivery status and opt-outs. Twilio documents both [incoming-message webhooks and outbound status callbacks](https://www.twilio.com/docs/usage/webhooks/messaging-webhooks). That is the connection pattern, not evidence our integration is already built.

Do not make a Base44-assigned “Jarvis number” the default prospect sender until third-party outbound rights, country reach, reply routing, registration and CRM event access are confirmed. The [official Superagent setup page](https://docs.base44.com/superagents/creating-a-superagent) inspected here did not establish those campaign capabilities. Member-to-agent messaging is not automatically a prospect-messaging service.

Booking creation/reschedule/cancellation updates the CRM; it schedules the relevant email/SMS, cancels stale reminders and routes replies to a person or draft queue. Recheck state before dispatch. Accepting a calendar invite and replying yes are distinct events. Test timezone changes, duplicate webhooks, STOP and replies before rollout.

For larger opted-in transactional/reminder email volume, an API sender such as Resend is an optional adapter using the member's verified domain and the required recipient permission. [Resend domain docs](https://resend.com/docs/dashboard/domains/introduction) cover identity; its [acceptable-use policy](https://resend.com/legal/acceptable-use) explicitly prohibits cold outreach. Do not use this adapter for cold lists. For email replies, connect the member's mailbox or a tested inbound route; an outbound API alone is not a conversation inbox.

## Cold email: simplest honest route

For a small researched list, one established business inbox can support low-volume personal correspondence within provider rules. The point where it stops being enough is scale, not the first message. For sustained multi-inbox outbound, retain a dedicated sequencer such as Instantly, linked to CRM outcomes. Do not rebuild mailbox rotation and event handling just to remove a familiar tool.

There is no verified instant warmup shortcut. [Instantly recommends at least two weeks](https://help.instantly.ai/en/articles/5975326-instantly-cold-email-strategy); that is vendor guidance, not a guarantee. Authentication, list quality, provider limits and actual delivery results still govern readiness. Buying a “pre-warmed” inbox does not establish its reputation for this member or offer. Keep cold acquisition separate from booking/client email infrastructure.

| Country / recipient | Recommended starting route |
|---|---|
| US businesses | Researched manual calls and small relevant email test, then sequencer if volume justifies it. Meet [CAN-SPAM](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business), including identification and opt-out. |
| AU | Listed-business-number human calls first for local services. Email only with a recorded lawful basis, relevant role and sender/unsubscribe compliance; no generic purchased-list blast. See [ACMA](https://www.acma.gov.au/avoid-sending-spam). |
| UK | Corporate recipients can be emailed under the applicable B2B rules; sole traders and some partnerships need different treatment. Use calls or permission first where required, with TPS/CTPS checks for calls. See [ICO guidance](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/). |
| Canada | Calls with applicable calling checks, or permission-led email. A documented CASL basis is required; relevant conspicuous publication may support implied consent, not every enriched address. See [CRTC](https://crtc.gc.ca/eng/com500/guide.htm). |
| NZ | Calls first where suitable. Email only with the applicable consent basis; published business addresses require the stated conditions. See [DIA consent guidance](https://www.dia.govt.nz/Spam-Frequently-Asked-Questions). |
| EU | Select the actual country and recipient type before a cold-email playbook. Consent-led acquisition is the default when no country-specific route is established; calling also needs local checks. [European Commission guidance](https://commission.europa.eu/law/law-topic/data-protection/information-business-and-organisations/legal-grounds-processing-data/can-data-received-third-party-be-used-marketing_en) requires ePrivacy compliance as well as data-protection compliance. |

These are implementation recommendations, not a complete legal matrix. No vendor bypasses country rules. Use the reviewed international research to implement exact contact-level eligibility.

All five changed/new entry files pass structural validation after the YAML correction. This does not establish behaviour or Base44 execution. The next tests are one task per offer route and one controlled booking-to-email/SMS-to-reply flow, before prospect sending.
