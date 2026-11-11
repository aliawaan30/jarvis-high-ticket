# From an AI setter to a roofing lead-conversion system

Draft teaching map, 2 November 2026. Based on the inspected Crown Roofing/Hatch case. The functional design below is our proposed teaching adaptation, not a claim to have inspected Crown's private configuration. No integration or campaign was built.

## Answer in plain words

Yes, an AI appointment setter is part of it. The full service also brings enquiries into one place, answers outside office hours, follows up across the sales cycle, gets the right person involved and records what actually becomes sold and paid work.

The buyer is buying better use of enquiries and estimates, not an AI personality. We would not promise that AI closes roofing contracts or decides prices.

## What problem each part fixes

| Business incident | What the owner loses | Proposed system response |
|---|---|---|
| A paid enquiry arrives while staff are busy | A chance to speak to the homeowner before they choose another roofer | Create one lead record and start the approved response promptly |
| A homeowner calls after hours | The enquiry may wait until tomorrow or disappear | Capture the enquiry, answer approved routine questions and arrange an appropriate next step |
| The business contacts someone outside its area or for work it does not provide | Rep time and wasted appointment capacity | Ask a few relevant fit questions and route correctly |
| The homeowner books but does not attend or reschedules | An empty slot and delayed sale | Confirm, remind, offer appropriate rescheduling and inform the rep |
| The rep gives an estimate and nobody hears back | Uncertainty about objections, timing and whether the job is still available | Follow up against that estimate and surface the homeowner's actual question |
| Someone replies with a pricing, insurance or technical question | Generic automation gets stuck or gives the wrong answer | Preserve context and assign a human response, rather than improvise |
| Follow-up activity looks busy but the owner cannot see sales | No reliable basis for deciding whether the service pays | Connect cohort, conversation, appointment, sale and payment status |

## One homeowner moving through it

1. **Enquiry:** a homeowner requests a roof-replacement estimate through an existing ad or website. Create/deduplicate the CRM record, keep the source and contact preferences. A proposed implementation must use the client's actual permission and suppression rules.
2. **Initial response:** acknowledge the request, identify the business and ask the first useful question. The exact channel, timing, retries and hours are agreed, not universal settings copied from a case.
3. **Qualification:** service area, requested work, property contact and urgency. Ask only what is needed for the next step. Emergencies, complex scope and other exceptions go to the agreed person.
4. **Appointment:** use real availability and service/rep rules. Prevent duplicate bookings. Send the rep the enquiry and answers; give the homeowner a clear confirmation.
5. **Attendance:** remind and handle approved rescheduling. Distinguish booked, attended, no-show and cancelled. A booked appointment is not a sale.
6. **Estimate:** after the roofer prepares the actual estimate, trigger an appropriate follow-up. Refer to the correct job and version. Do not invent prices or offer unauthorized discounts.
7. **Reply/handoff:** if the homeowner asks about a routine approved matter, answer. If they need a revised quote, technical explanation, negotiation or financing decision, give the rep the context and a task/callback. Stop competing follow-ups while a person owns the conversation.
8. **Outcome:** record won/lost/paused and reason. Reconcile the agreement, completed work, invoice and collected payment using the systems actually available. Stop inappropriate campaigns when the opportunity changes state.

## The three related offers

| Offer | Starting list | Main job | Measure |
|---|---|---|---|
| New-lead conversion | New enquiries | Reach, qualify and book promptly | Contact, qualified/attended appointments, sales, contribution |
| Unsold-opportunity recovery | Eligible aged leads/unsold estimates | Reopen interest and resolve the next obstacle | Incremental or clearly attributed sold/paid work from that cohort |
| Past-customer reactivation | Completed past buyers due or suited for another purchase | Start another useful buying conversation | Repeat purchases, booked/completed service, contribution and retention |

Pella belongs mainly to the third example when asking a previous window customer about a new project. Bone Dry rehash belongs to the second. Crown describes several lanes together. Similar technology does not mean identical buyer motivation or targeting.

## What we would deliver first

Start with one location, one CRM and one lane. For a recovery pilot: one agreed eligible estimate cohort, data cleanup/suppression, approved messages and knowledge, reply handling, rep ownership, appropriate booking, outcome tracking, sample-case tests, team training and review cadence.

Expand into new-lead intake and customer recontact only when the first lane works and further scope is agreed. Crown's broader implementation is a useful destination, not a mandatory day-one bundle.

Observed in the source: Salesforce connected to Hatch, after-hours intake, cross-channel response, estimate follow-up, nurture and human escalation. Not verified here: vendor prices, permission tiers, API limits, client data quality, achievable deployment dates, detailed booking configuration or suitability of another CRM. Other systems need their own access/feasibility check.

## What the student actually sells

Generic category: AI appointment setting.

Specific service: roofing enquiry conversion and estimate recovery.

Concrete recovery message: “We work your unsold roof estimates, handle the follow-up and bring interested homeowners back to your team, so more of the quotes you've already paid to create become sold work.”

Broader conversion message: “We install and manage the response and follow-up process that takes your roofing enquiries from first contact through estimate review, keeping your reps focused on the homeowners ready to move forward.”

These are draft positioning directions. The outcome remains sold work and collected cash; follow-up is the mechanism. A defined result/timeframe/remedy belongs in the final offer after pipeline and delivery feasibility are known. No public prices added.

## Why the problem can be worth paying for

Illustration only: two genuinely additional completed and paid jobs at $15,000 each produce $30,000 revenue. At an assumed 30% contribution after incremental delivery costs, that is $9,000 before the recovery service and tools. Two jobs, $15,000 and 30% are assumptions, not Crown data or forecasts. Do not promise a number because this arithmetic makes it attractive.

Before pricing, confirm eligible quote volume, typical contribution, reasons for losses, time since estimate, existing native follow-up, sales/installation capacity and what can reasonably be attributed to the service. Keep actual paid cash distinct from signed jobs and gross margin.

## What the Crown case establishes

Hatch reports $365,000 of sales attributed to the platform over 60 days and describes the broader workflow. It is a customer/provider account, not proof of independent incrementality, collected cash, agency fees or what a first student can achieve. No private records or campaign economics inspected. The strong teaching point is the specific business process and accountable ownership, not copying its reported result into our guarantee.

Source: https://www.usehatchapp.com/case-studies/crown-roofing-and-waterproofing (relevant case text inspected in the expanded research run).
