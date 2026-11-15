# Jarvis skill index

Updated 8 November 2026. The current folders below supersede the October ZIPs and the old descriptions that preceded the latest funnel changes. Instructions, references and proposal assets are all included. No current complete student journey is established as Base44-tested or student-pilot-tested. See [the technical guide](../TECHNICAL-REVIEW.md) for integration tests and [the manifest](../docs/REPOSITORY-MANIFEST.json) for exact files/hashes.

| Skill | Module | Inputs and output | Required capability or review gap |
|---|---|---|---|
| [jarvis-course-guide](jarvis-course-guide/SKILL.md) | All | Current course snapshot and student question → explanation, next task and saved progress. | Course files must be accessible; persistence depends on runtime. Instructions tested structurally, not yet student/Base44-tested. |
| [jarvis-ad-library-offer-research](jarvis-ad-library-offer-research/SKILL.md) | 2 | Existing ads and destination pages → one supported buyer/service adaptation. | Ad Library/page access; inspection and source capture, not a profitability feed. |
| [jarvis-offer-menu](jarvis-offer-menu/SKILL.md) | 2 | Known examples, outside idea or niche/service fit → understandable opportunity and delivery route. | Current source access. Includes content/editing and niche automation agency; sourced pre-call value estimates and client-specific service scope. |
| [jarvis-custom-opportunity-finder](jarvis-custom-opportunity-finder/SKILL.md) | 2 | Buyer market/workflow → evidence-backed custom opportunity. | Research access and technical feasibility; advanced route, not a required beginner report. |
| [jarvis-offer-creation](jarvis-offer-creation/SKILL.md) | 2 | Selected buyer/problem/solution → exactly six labelled offer lines. | Saved brief, real proof, feasible timeframe and approved or explicitly proposed remedy. |
| [jarvis-landing-page](jarvis-landing-page/SKILL.md) | 3 | Saved offer → compact landing, progressive application and qualified booking page. | Page builder/hosting and calendar. One-line entry; no-video Offer Testing mode supported. |
| [jarvis-confirmation-page](jarvis-confirmation-page/SKILL.md) | 3 | Saved funnel and prep video → separate post-booking page. | Actual booking event, calendar/invite status where exposed, proof assets. |
| [jarvis-precall-followup](jarvis-precall-followup/SKILL.md) | 3 | Offer/funnel and booking → messages plus event workflow. | Connected mailbox/SMS and calendar/CRM events for execution; copy alone is not sending. |
| [jarvis-vsl-writer](jarvis-vsl-writer/SKILL.md) | 3 | Offer and buyer objections → VSL/prep script and filming direction. | Research/proof/demos; reference inspection depth varies. Review actual script quality. |
| [jarvis-ad-scripting](jarvis-ad-scripting/SKILL.md) | 5 | Offer and awareness → spoken video ad scripts/variations. | Real offer/claims. Does not film, edit or publish ads. |
| [jarvis-static-ad-creator](jarvis-static-ad-creator/SKILL.md) | 5 | Offer and inspected creative references → static concepts and exports. | Image/design/render tools and visual QA. Readability checks do not prove strong creative. |
| [jarvis-meta-campaign-setup](jarvis-meta-campaign-setup/SKILL.md) | 5 | Offer/funnel and budget → campaign setup guidance and review plan. | Meta access if execution is requested; not a verified autonomous media buyer. |
| [jarvis-proposal-builder](jarvis-proposal-builder/SKILL.md) | 6 | Call-one discovery and scoped terms → plain private call-two proposal. | Short document template included; buyer impact before solution, demo separate. Rendering is not closing proof. |
| [jarvis-scoping-agent](jarvis-scoping-agent/SKILL.md) | 7 | Accepted proposal and discovery → complete delivery/build plan. | Accepted scope and actual integration details; not the pre-sale pricing/feasibility step. |

## One-line funnel entries

- `Run the landing page skill for my offer. Domain: [x]. Calendar: [link]. Video: [link or none yet].`
- `Run the confirmation page skill for my landing page. Video: [link or placeholder].`
- `Run the pre-call follow up skill for my offer and my landing page. Calendar: [tool].`

Each reads saved project context and asks only for genuine missing inputs. The three/four fit questions precede the combined name/email/phone screen. Booking page and post-booking thank-you page are different stages. Read each full skill for exact states and outputs.

## Supporting material included elsewhere

- [Existing outreach coordinator](../course/outreach/skills/jarvis-outreach-coordinator/SKILL.md): list/enrich/score/draft/CRM instructions, with references and a proposed lab. Currently draft/read-only; not a live sequencer.
- [Outreach execution proposal](../docs/decisions/funnel-and-outreach-2026-11-02.md): planned channel adapters, reply handling and student prompts. Proposed skills are not installed merely because their names appear here.
- [Recovered earlier skills](../archive/recovered-skills/README.md): call review, onboarding, marketing research and pre-sale solution scoping, pending reconciliation.
- [Free-course dependencies](../dependencies/free-course-skills/README.md): four discovery/CRM blueprints, pending port/runtime review.
- [Proposal examples and checks](../tests/proposal-template-2026-10-31/REVIEW.md).
- [Simulated beginner test findings](../tests/beginner-offer-runs-2026-11-02/SUMMARY.md).

## Latest changes and limits

Offer menu now includes provider research, the optional examples route, niche AI agencies, content engines with video editing, a simple teaching process and researched US sector agencies. The market-scoring prompt is an additional mode of offer-menu, not extra output from six-line offer creation. The 30 October ad-count catalogue is historical advertising evidence, not a ranking of proven profit.

Funnel skills now read saved offer/page records rather than making students repaste information. The landing skill produces three pages; confirmation is post-booking. Pre-call messages trigger on booking, not application submission. These instruction changes passed structural checks but need a fresh Base44 integration test.

Jarvis 2.0 installation/loader, paid member access, a live member CRM, channel senders, real reply handling, actual video editing and Meta execution need implementation or runtime evidence. The course and these instructions do not automatically supply those connections.

Never paste secrets into chat. Pass approved records between skills and record actual tool results. The technical lead should establish the smallest working route before multiplying niches or creative variations.

5 November page/proposal repair: compact student landing default retained; congratulations is pre-booking, thank-you is post-booking. Roofline assets now include an honest review fallback instead of approving every form. The short proposal and separate-demo rule also govern the course lessons and master template. These are locally checked drafts, not a release of the full programme. Outreach remains with Blake’s technical lead.

Compass update, 5 November: post-booking is one confirmation page using the Compass Leads action/video/email/calendar/proof sequence. No reviews means no review block. Booking page includes a calendar section. Internal booking-state tests are not separate customer pages. Proposal development is now owned by Blake’s technical lead.
