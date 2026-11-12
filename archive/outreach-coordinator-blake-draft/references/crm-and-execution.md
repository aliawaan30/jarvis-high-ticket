# CRM and execution contract

The custom member CRM is the record of the business; the agent chat is the interface. Funnels and the CRM come before outreach in the updated course order. Keep campaign setup usable without live coaching for the DIY tier.

## Minimum records

| Record | Required content |
|---|---|
| Offer | ID/version, buyer/problem/solution, approved claims, demo reference, delivery assumptions. |
| Campaign | Member/workspace ID, objective, target segment/geography, offer/criteria/copy versions, allowed tools/spend, mode, owner, approval scope. |
| Account | Stable ID, business/domain/location, parent/branch, provider references, fit/reason, evidence references, reviewer. |
| Contact | Account links, person/role evidence, contact fields, provenance/date, published versus verified status, eligibility per channel and reason. |
| Action | Contact/account, campaign, channel, draft reference, owner, due time/timezone, approval version, execution state and external ID where applicable. |
| Event | Stable provider/event ID, source, occurred/received times, conversation link, outcome and processing status. |
| Suppression | Contact/account/channel scope, reason, source/date and reviewer. Survives reimports. |
| Opportunity | Buyer, call notes, booked/attended outcome, pain/baseline, solution scope, proposal version, deal state, value/currency and actual collected payment source. |

Enforce member ownership in the connected service, not merely by a prompt. Keep keys out of chats, exports and skill files. Inspect only records available to the authenticated member.

## Separate workflow states

Research: new → researching → needs review → reviewed fit / excluded.

Actions: draft → approved → queued → attempted → confirmed sent/completed, or failed/unknown/cancelled. In this lab all actions stop at draft. Unknown after a timeout needs reconciliation, not blind retry.

Sales: not contacted → contacted → conversation → call one booked → attended/qualified → scope/proposal → call two → won/lost/nurture. Keep bookings, attendance and qualification as separate events, not a single “lead converted” flag. A won deal hands over to onboarding/delivery; it is not a completed project or cash collected.

Member views: review queue, today's calls/tasks, accounts/contacts, conversations, opportunities, proposals, projects and performance. Call cards show fit evidence, likely buyer, opener, questions and next action. Manual outcomes must be easy to log while talking.

## Sending later

“Google Workspace through the CRM” is a proposed integration, not supplied by these instructions. Confirm actual send/reply access, rate/capacity, opt-out handling, authentication and provider policy. If unsupported, the member sends through their mail client and logs the action manually. A draft must not show as sent.

Any reply pauses further acquisition actions for that contact; a booking hands over to pre-call nurture; an opt-out suppresses the relevant scope. Other contacts at the account pause for review by default. Manual messages/calls need explicit logging. Recheck state before each manual task or provider dispatch.

Where pausing requires a platform UI action, record `pause_requested` until the member or provider confirms it. Local cancellation cannot recall a dispatched message. Deduplicate provider events and action keys, reconcile uncertain sends, and preserve a recovery queue. Draft approval never expands to a new cohort, channel or higher spend by implication.
