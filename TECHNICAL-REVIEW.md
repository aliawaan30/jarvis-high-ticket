# Technical review guide

This private repository contains the current high-ticket course and the skills behind it. The aim is to help a member choose, explain, demonstrate, sell and deliver an AI service. Review the complete workflow, not just whether individual prompts produce text.

## Read first

1. [Course status and lesson index](docs/COURSE-STATUS.md). The outline is current; a nonempty lesson is a draft, not a release approval.
2. [Skill index](skills/README.md). It separates current entry points, older supporting skills and dependencies.
3. [Latest funnel and outreach decisions](docs/decisions/funnel-and-outreach-2026-11-02.md).
4. [CRM spec](course/crm/SPEC.md) and [proof/status notes](course/crm/PROOF.md).
5. [Outreach lean path](course/outreach/LEAN-PATH.md) and the newer proposal in the decision handoff. The older SYSTEM.md records superseded Clay-first choices.

## Programme and operating model

The learning journey is Jarvis setup, buyer/problem/service selection, a six-line offer, funnel and CRM, acquisition, discovery and proposal, then delivery. The programme targets a credible path toward $20k/month; that is not a verified or guaranteed student result.

Known services, outside ideas and custom research are all valid offer entry points. The catalogue is optional. AI content includes editing; a niche AI automation agency is a business model that can use a free audit as one funnel. Technical support helps check feasibility; it is not a promise of unlimited development. The internal fulfilment split is not part of marketing/research skills.

All members are intended to have weekly group strategy support. A DIY tier exists, so essential instructions cannot depend on attending a call. No final tuition, income guarantee or support-extension commitment is established by this repository.

Jarvis is intended to coordinate specialist work and preserve project state. Claude/Codex/Base44 model routing and an autonomous multi-agent backend are not implemented by this repository. A SKILL.md is instructions; provider access and execution are separate components.

## Shared records needed for execution

Use the member CRM/project store as the record of the business. Each step reads the previous approved version instead of asking the student to paste everything again.

| Record | Minimum purpose |
|---|---|
| Offer brief | Buyer, problem, value model, before/after, evidence, delivery route, approved claims and six-line card. |
| Funnel | Offer version, landing/form/booking/thank-you URLs, fit rules, calendar, video/proof assets and actual connection status. |
| Campaign | Target accounts, country, copy/version, channels, tools, budget, approval scope and shared schedule. |
| Contact and event | Source, role, channel eligibility, conversation, provider IDs, next action and suppression. |
| Sales opportunity | Discovery, agreed problem, feasible scope/cost, demo, proposal version and decision. |
| Delivery project | Accepted scope, access, developer/build owner, milestones, tests, handover and support terms. |

These are an integration contract, not proof a backend schema is already deployed. Enforce member isolation and access in the application. Store secrets in provider/application secret storage, never skills, lessons, exports or prompts.

## The first tests

### Offer discovery to offer

Give a fresh test member a location, background and time/budget. Run one known-service route and one audit-led/custom route. Check whether they can explain the buyer, pain, solution, value, alternatives, delivery and acquisition. Then run offer creation: exactly six lines. Competitor outcomes must not become the student's proof. A service description alone is not a compelling offer.

Market scoring is an optional offer-menu mode: five researched tests, each 1 to 5. The 20+/15-19/<15 bands are screening heuristics. They do not validate demand or justify invented annual-cost inputs.

### Offer to funnel

Run: `Run the landing page skill for my offer. Domain: [x]. Calendar: [link]. Video: [link or none yet].`

Expected: saved-context reuse; landing, progressive application and qualified booking page in one run. Three/four fit questions, then name/email/phone together. No public prices or completion-time estimate. No video defaults to Offer Testing mode. Calendar approval is call eligibility, not a claim of service acceptance.

Run: `Run the confirmation page skill for my landing page. Video: [link or placeholder].`

Expected: a distinct post-booking page with prep video, accurate booking/invite status, invite action and genuine proof when available. Unknown acceptance status must not be called unconfirmed. Booking creation and attendance confirmation are separate states. A page visit is not proof of either event.

Run: `Run the pre-call follow up skill for my offer and my landing page. Calendar: [tool].`

Expected: event-specific copy/workflow from saved context. Test booking, reply, reschedule, cancellation, opt-out and duplicate webhook. An unconnected sender must remain explicitly unconnected.

### Sales to delivery

Use one authorised discovery record. Prepare a plain call-two proposal: executive overview, current problem/impact, proposed build, timeline, costs and next step. Keep any demo in a separate file/link. Pricing belongs in private sales material. Check that it invents no client numbers or acceptance. After acceptance, use scoping to produce the full build plan. Pre-sale feasibility remains necessary before accepting or pricing the project.

The recovered solution-scoping and client-onboarding files are available for comparison. They are not automatically updated to the latest course contract.

### Outreach

Reuse the existing coordinator's list/enrich/score references. Channel sending and reply handling are proposed work. Start with offline fixtures and a read-only account sample. Then test providers with owned/sandbox recipients before any authorised live campaign.

Three touches per lead per week means three total across channels. Recheck state before dispatch. Replies pause cold acquisition; booking hands over to pre-call nurture; opt-outs survive imports. A timed-out send is reconciled rather than blindly repeated. SMS needs its own recorded permission; an email reply is not sufficient by itself. Third-party LinkedIn APIs are not evidence of LinkedIn authorisation.

## What is and is not tested

The current outline still has an older paid-ads blurb implying outreach must close first. Blake's later decision allows ads when the offer, demonstration, delivery route and budget are ready; a prior sale is not a mandatory gate. Treat this as a course-copy reconciliation item, not a new restriction. Historical catalogue ad counts and draft guarantees also need review before teaching them as current facts or approved terms.

- Instruction structure, source files and local prototypes have been checked at different times.
- Existing simulated beginner runs show weak selections, supervisor intervention and rejected economics as well as useful demonstrations. They are not real student outcomes.
- Proposal examples are drafts; fictional numbers and incomplete ACT inputs remain labelled.
- No current complete route is established as end-to-end Base44-tested or student-pilot-tested.
- The authoring server and reading copy have no member access gate. The server binds locally and must not be exposed as a paid member portal.
- Actual video editing, Meta management, email/SMS sending and autonomous voice integrations need separate runtime verification.

## How to report findings

Record the skill/course version, environment, input, tools connected, output paths, exact failure, buyer/learner clarity, expected versus actual behaviour and the smallest proposed fix. Use a named fixture and retain it for regression. Report functional, commercial and visual quality separately. Test one complete benchmark before generating batches.

Mark status as draft, locally checked, Base44-tested or student-pilot-tested, with evidence. No production sends, ad spend, purchases or client writes are authorised by this guide.
