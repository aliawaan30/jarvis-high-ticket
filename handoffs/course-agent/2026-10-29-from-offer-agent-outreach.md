# Jarvis outreach architecture and first lab

29 October 2026 · Codex to Claude · Design only, for merge into `outreach/SYSTEM.md`

## Recommended product

Give the member one request: “Find businesses that fit this offer, show me why they fit, prepare the outreach and keep the campaign organised.” Jarvis returns an account list with evidence, named buyers, contact coverage, channel-specific drafts and a review queue. Once the member authorises a defined campaign, connected services execute it and return events to the CRM.

The interface should feel like one sales assistant. Underneath, separate research judgments, contact data and execution state. Do not require the member to operate eight agent chats. Specialist research tasks may run concurrently when supported, but one campaign coordinator owns the result and handoffs. Eight responsibilities do not require eight permanently running agents.

**Clay decision:** design provider adapters so Clay can be used where its data workflows earn their cost. It should not be a mandatory extra brain or a requirement for every student. Jarvis owns the brief, judgment and review; providers supply search, enrichment or delivery. Claude's live tool research should decide the first stack based on actual contact coverage, API access and total cost in the chosen market.

## Inputs from the existing opportunity skills

I read `jarvis-opportunity-finder/SKILL.md`, `jarvis-offer-discovery/SKILL.md` and the revised Module 3 six-stage lesson. Keep both research routes. They hand a shared, versioned offer brief to outreach rather than repeating niche discovery for each campaign.

Required brief: buyer type and geography, workflow/problem, proposed solution, eligibility and exclusions, buyer roles, observed evidence, working demo/proof, approved claims, current delivery route and unresolved questions. A research hypothesis can generate a discovery campaign. It cannot silently become an implementation offer promising an unscoped result. Campaign objective must say discovery interviews or sales meetings.

## Proposed skills and their contracts

These are design names, not installed skills. Keep the main instructions short; put field definitions, channel patterns and provider mappings in references.

| Skill / responsibility | Inputs | Persisted output | Tool dependency | Member review |
|---|---|---|---|---|
| `jarvis-outreach-coordinator` | Offer version, objective, geography, budget, available tools and campaign permissions | Campaign plan, task references, review queue, run summary and resume point | CRM read/write adapter; task runner or Base44 workflow | Approve objective, list rules, claims and permitted actions. Review exceptions and change requests. |
| `jarvis-account-definition` | Approved offer, exclusions, buyer roles and delivery constraints | Account criteria, visible fit signals, disqualifiers and discovery questions | Offer/CRM records; optional web research | Confirm the buyer is commercially worthwhile and the student understands the problem. |
| `jarvis-account-research` | Account definition, source selection and list limit | Deduplicated accounts plus evidence-backed fit, source dates, uncertainties and A/B/C review tiers | Candidate business directory/search API, company websites, permitted public sources | Check first ten accounts, bad matches and low-evidence records. A tier is priority, not proven pain. |
| `jarvis-buyer-contact-research` | Approved accounts, role hypotheses and field requirements | Candidate decision makers, role evidence, enrichment/verification status and contact provenance | Candidate people-data/enrichment APIs, licensed directories; manual LinkedIn research where needed | Check first ten identities and ambiguous owners/branches. Verified email does not verify buying authority or sending permission. |
| `jarvis-outreach-writer` | Account facts, offer, demo, buyer role, channel policy and tone | Call opener, email, DM/LinkedIn message, eligible SMS draft and follow-up variants | Model and source records; no sending tool needed | Approve first batch and message templates; check each personalised factual claim. |
| `jarvis-campaign-planner` | Approved copy, contact availability, channel eligibility and sender capacity | Versioned sequence with schedule, owner, stop conditions and per-contact eligibility | Provider capability lookup and calendar; proposed delivery adapter | Approve the exact cohort, channels, cadence, limits and start/end dates before execution. |
| `jarvis-reply-and-booking-assistant` | Incoming event, thread context, offer, booking rules and suppression state | Intent classification, stopped/paused sequence, draft reply, call task or proposed booking | Provider webhooks, thread reader, calendar and CRM | Handle uncertain intent, substantive questions, objections, complaints and commercial commitments. Begin lab with drafted replies, not autonomous selling. |
| `jarvis-campaign-review` | Account/cohort data, delivery events, conversations, meetings, deal/payment records and actual costs | Funnel with denominators, failure analysis and one proposed next experiment | CRM reporting and provider event/cost exports | Confirm outcomes and approve any list, copy or volume change. |

List construction and pain-signal scoring are stages within account research initially. Split them into separate skills only if testing shows reusable standalone work. Enrichment is similarly a distinct execution step inside buyer/contact research. The **pipeline logger is a shared service**, called by every stage, rather than an agent asked to reconstruct events after the fact.

## Minimal shared records

Use stable IDs and typed records in the custom CRM. If that app is not ready for the lab, use the same fields in a structured table plus an event export. Chat memory is not the campaign database.

- **Offer:** ID/version, approved claims, demo status and delivery assumptions.
- **Campaign:** member/workspace, objective, offer version, target definition, sequence version, mode (`draft`, `dry_run`, `authorised`, `active`, `paused`, `completed`), limits, approver and permission scope.
- **Account:** provider IDs, name, canonical domain, branch/parent relationship, geography, fit, exclusion reason, evidence references and reviewer.
- **Evidence:** source URL/provider, inspected date, factual observation, related field, interpretation and freshness. A missing field is unknown, not a negative finding.
- **Contact:** account, person/role, source and checked date, email/phone/LinkedIn, verification status and channel eligibility with reason. Keep business fit, identity accuracy, reachability and permission as separate fields.
- **Enrollment/action:** campaign/contact/sequence version, channel, scheduled time and timezone, state, approved content reference, provider action ID and deduplication key.
- **Event:** provider/event IDs, received/occurred timestamps, contact/thread mapping, event type and processing status. Save only necessary message data with appropriate access and retention.
- **Suppression/review:** scope, reason, timestamp, source, owner and next task. An opt-out stays suppressed when lists are reimported.

Account deduplication should use canonical domains plus provider identifiers and branch rules. Domain alone must not merge unrelated buying locations or collapse all franchisees. A contact may belong to multiple accounts; account-level reply handling prevents two students' contacts at the same company receiving conflicting approaches within one member's campaign.

## Proposed execution behaviour

1. Coordinator verifies brief and connection capabilities, then issues bounded research jobs.
2. Research stages return structured records, costs and evidence. Coordinator merges and presents the first review batch.
3. Member corrections update the campaign criteria. Preserve the earlier version so we can assess whether fit improved.
4. Writer and planner prepare channel variants and eligible enrollments. Missing data leads to another available channel or a review item, not invented contact details.
5. An authorised scheduler sends through the selected provider. Immediately before dispatch, recheck approval version, current suppression, reply/booking state, schedule and limits.
6. Provider events update the ledger. A reply pauses all pending automated touches to that contact; a booking suppresses acquisition touches and hands over to pre-call nurture. Account-level replies pause other contacts for review by default. An explicit opt-out updates the appropriate suppression scope.
7. Resume from saved job/action state. Retry reads safely; retry a send only after reconciling with the provider. A timeout may mean the message was already accepted. Never blindly resend.

The stop logic must operate in the sending provider too where supported. Cancelling our local task cannot recall an email already dispatched or guarantee cancellation of a provider queue. Measure cancellation delay and document the residual race. Repeated webhook events must not create duplicate replies, bookings or tasks. Unmatched events go to review rather than being attached to the wrong prospect.

Keep research tools unable to send. Reply content and scraped pages are untrusted inputs, not instructions authorising new tools, campaigns or data exports. Separate member workspaces and enforce campaign ownership in the execution service; do not rely on a model remembering which member owns a record. Keep provider credentials out of prompts and exported skill files.

## Base44 boundary

Student Jarvis stays on Base44. Retell remains an optional advanced calling route. Manual human calls are the initial lab default.

I inspected the local SDK skill and in-app agent reference, plus Base44's [Creating a Superagent documentation](https://docs.base44.com/superagents/creating-a-superagent). The official page describes reusable skills, connected tools/custom MCP, goals with subagents, and workflows. That establishes available platform concepts, not a tested outreach installation in our members' accounts. In-app SDK agents and Superagents are different surfaces; SDK methods alone do not establish that a student Superagent can access the custom CRM.

| Work | Proposed home / limitation |
|---|---|
| Briefs, research reasoning, copy, review summaries | Superagent skills using accessible notes, files and connected tools. Confirm actual research/source-opening behaviour in the member environment. |
| Parallel account research | Goal subagents where available; same records and limited research permissions. Sequential processing is an acceptable functional fallback. |
| Prospect discovery, enrichment and address checks | External data providers, with their supported API/connector and paid access. A skill upload supplies none of this data access by itself. |
| CRM reads/writes | Base44 app with permissions and a tested app connection or a narrow authenticated tool bridge. A proposed route, not yet tested here. |
| Schedules, retries and event reconciliation | Tested Base44 workflows/backend where suitable, or an external execution service. Verify triggers, runtime limits, webhook handling and restart behaviour before choosing. A chat response is not a durable queue. |
| Sending email/SMS and retrieving replies | Connected providers with the required sending identity, campaign controls and event feeds. Do not assume a generic email connector has campaign deliverability or suppression features. |
| LinkedIn/DM research and sending | Manual member tasks until Claude confirms a permitted supported connection. Do not require browser-bot actions for the core product. |
| Local Mac scripts, phone dialling and Retell | Not transferred by uploading a skill. Require separately connected execution tools. Retell is not needed for the baseline. |

For each connector, record: actual read/write operations, plan requirement, credentials owner, field coverage, limits/cost, event support, cancellation support and test result. Claude owns current vendor specifics and jurisdiction rules. I have not checked their pricing or selected the final stack.

## Lab plan: one real offer through the whole process

**Phase A, design and offline rehearsal:** choose one real agency implementation offer with a credible delivery route, geography and demo. Do not mix sales of our course with sales of an implementation service in one results cohort. If the team chooses the course as the lab offer, label it accordingly and do not claim it validates selling custom implementations.

Prepare ten synthetic fixtures: strong fit, weak fit, wrong country, stale job ad, uncertain buyer, duplicate branch, bounced email, reply before send, opt-out after import and ambiguous send timeout. These test workflow behaviour, not market performance. Expected outcomes: no invented evidence, unresolved fields visible, no duplicate actions, correct suppression, no send without permission, recoverable state after interruption. Run with outbound disabled and provider calls mocked.

**Phase B, read-only data pilot:** proposed 30 real accounts, one market. This is an experiment size, not a conversion benchmark. Before paid lookup, authorise provider accounts, data spend and allowed sources. Manually label first ten, revise the criteria, then assess the remaining twenty. Log all inspected sources. Produce drafts and the complete dry-run schedule. No outreach yet.

Measure accounts inspected, actual-fit precision on the manually labelled sample, unknown/excluded counts, buyer identity accuracy, usable contact coverage by channel, duplicate rate, time and credits/cash per account, and human review minutes. Cost per accepted account = total lookup/research cost divided by accepted accounts; also report unsuccessful lookup costs. Do not count one contact found via three providers as three leads.

**Phase C, member-environment rehearsal:** install the candidate instructions in a fresh student Base44 test setup; connect only test tools. Run the ten reviewed records through research → copy → review → CRM handoff. Close/reopen the chat and resume. Test a missing credential, exhausted quota, provider failure and out-of-order/duplicate events. Confirm the actual skill load, outputs and persisted records, not only the agent's completion statement. Use controlled team-owned destinations for any transport tests, separately authorised; no prospect messages.

**Phase D, separately authorised live pilot:** Blake or the designated campaign owner approves a saved manifest containing exact offer/cohort, sender identities, channels, message/sequence versions, geography/timezones, exclusions, spend/volume limits, start/end dates and who handles replies. Claude's compliance findings become channel eligibility rules. Define stop conditions and an operator able to pause all providers. New claims, extra channels, larger cohorts or higher limits need an updated scope. This design request does not supply that launch authority.

Begin with a small reviewed cohort, not an automatic volume ramp. Set the observation window and review date before launch; never let “no replies” trigger indefinite extra sends. Obtain a named owner for inbound responses and booking capacity first.

Measure provider acceptance/delivery/failures, positive and negative replies, opt-outs, conversations, booked/attended/qualified calls, proposals, won deals, collected cash, delivery scope/cost and elapsed time. Email opens are not a primary outcome. Report denominators and incomplete observation windows, not invented target reply rates. Cost per held qualified meeting includes data, model, sending and human work. Discovery, nurture and sales campaigns have different success measures.

**Phase E, compare and teach:** first establish that the basic system works. Later compare signal-ranked versus otherwise eligible randomly ordered accounts within the same segment, with similar copy, timing and contact coverage. Do not exclude disqualified accounts from one arm only. Small cohorts produce exploratory results; no causal performance claim from a handful of replies. Turn the actual screen recordings, failures and revisions into Module 3 lessons.

## Course and delivery output

Teach the member to interpret the account evidence and operate the review queue, then run a campaign. Each lesson produces a real record or action. The DIY course needs setup walkthroughs, connection checks, sample data, troubleshooting and a manual fallback, so it remains usable without a live call.

Before release, one member should explain why an account fits, correct a mistaken buyer, approve suitable copy, stop a sequence, handle a reply and trace a booked call back to its account. These are proposed acceptance criteria, not completed tests.

**Next joint build:** Claude selects the first provider stack and channel rules; use this architecture as its data and execution contract. Then write one coordinator skill plus the references needed for one lab. Test that complete path before multiplying specialised skills or provider adapters. No outreach launched and no live settings changed for this handoff.
