---
name: jarvis-solution-design
description: Turn a call one transcript or brief into the real technical build that solves the client's problem, before call two. Produces a plain prescribed solution for the proposal, a technical design, a build route (Jarvis or a developer), effort and running cost estimates, a price check against the agreed problem cost, the riskiest assumption to test, and a quote request for a developer. Use this whenever the member has finished a discovery or audit call and asks what to build, how to solve it, whether it can be built, what it will cost to build, or for a scoping request for their technical partner, even if they do not name this skill. Not for the post-sale build plan (use jarvis-scoping-agent after the client accepts).
---

Version: 2026-11-15.1

# Jarvis Solution Design

Draft 1, 2 November 2026, written from the technical lead's delivery experience. Module 6 (Sales), between Call One and the proposal. It replaces the long "prescribe the solution" prompt in that lesson.

## Why this skill exists

After call one the member knows the client's pain and the number. Most members cannot tell what should be built, whether it can be built with the client's tools, or what it really costs. If they guess, they either sell something that cannot be delivered or price a job that loses money. This skill does the technical thinking a solutions architect would do, and says plainly where it is unsure.

It sits in a chain:

1. Call one brief (the Call One lesson prompt).
2. **This skill: solution design.** What to build, how, by whom, at what cost.
3. jarvis-proposal-builder reads sections 2, 3, 6 and 7 of this design.
4. After the client accepts, jarvis-scoping-agent turns this design plus call two notes into the full build plan.

## Student entry

`Run the solution design skill on my call one brief.`

Or with a transcript: `Run the solution design skill on this call one transcript: [paste].`

Read saved context first: the call one brief, the offer record, the client's tools, the agreed annual cost and the member's delivery preference. Ask only for what is missing and changes the design. If only a raw transcript exists, pull the facts out of it yourself. Do not make the member write the brief first.

## Inputs

Needed:
1. What the client does, who does the work now, step by step.
2. The problems, in the client's words, with any real examples.
3. The agreed annual cost of the problem and how it was worked out.
4. The tools they use now (CRM, email, calendar, accounting, phone, job system, spreadsheets).

Helpful: volumes (enquiries, jobs, invoices per week), number of users and roles, budget hints, deadlines, the member's developer day rate, whether the member wants to build it with Jarvis.

Missing items do not stop the work. Each one becomes a question in section 9 and any figure that depends on it is marked as an estimate.

## Method

Work through these steps in order. Read the references when the step says so.

1. **Readiness check.** Is there an agreed number, a clear owner of the problem and a list of tools? If the number is missing or was never agreed by the client, say so first. The design can still be drafted, but the price check is marked "not ready".
2. **Map the job.** Write how one job moves today: trigger, steps, who does each step, which tool, where it stalls. Then the same job after the build. This is the spine of everything else.
3. **Match each pain to a pattern.** Read [the appendix "build patterns" below](appendix "build patterns" below). Most pains fit a known pattern. Name the pattern, then adapt it to this client. Only design something new when nothing fits, and say so.
4. **Start small.** Choose the smallest system that removes the biggest pain. Put the part with the largest confirmed dollar figure live first. If the biggest figure rests on a guess (an uncounted volume, an assumed conversion), lead with a part whose number is solid and measure the guess before pricing that part. Anything that does not map to a pain is cut or moved to the follow on list.
5. **Check what already connects.** Before designing a build between two of the client's tools, check whether those tools already have a built in connection that is simply not switched on. Configuring it is the cheapest route and often the right answer.
6. **Check every integration.** Read [the appendix "platform facts" below](appendix "platform facts" below). For each tool, record what the build reads and writes, and give it one status: verified, plausible but untested, unknown, or not supported. A tool having an API does not mean this client's plan or account exposes what is needed.
7. **Choose the build route for each part.** Ladder, cheapest first: configure a tool they already pay for; connect existing tools with a workflow; build on Base44 with Jarvis; custom developer build. Base44 is the default build platform when it fits, because members already pay for it and it keeps hosting, login and data in one place. Say why when it does not fit.
8. **Estimate.** Read [the appendix "estimating" below](appendix "estimating" below). Give effort bands per part and list running costs as separate monthly lines. Every figure is labelled estimate, quote or confirmed.
9. **Price check.** Show 10 percent and 5 percent of the agreed annual problem cost next to the estimated build cost. Give one verdict: go, shrink the scope, or the problem is too small for a custom build. Never set the final price. That is the member's and Blake's call.
10. **Find the riskiest assumption.** The one unknown that would most change the design or the cost. Give the smallest test that settles it before call two, for example "log in to their Jobber sandbox and confirm a webhook fires on new quote".
11. **Write the outputs** in the shape in [the appendix "solution design template" below](appendix "solution design template" below).

## Output

One document, eleven sections, always in this order. Full shape in the template.

0. Readiness. Ready, or what is missing.
1. The problem and the number. Client's words, the figure, its source. Split the figure into cash (money lost or spent), staff time already paid for, and parts that rest on a guess. The proposal presents time as time back, not cash saved.
2. Prescribed solution. Plain language for the client: what gets installed, in what order, which pain and dollar figure each part fixes.
3. One job, before and after. Feeds the proposal demo.
4. Technical design. Components, key records, integrations table with status, triggers and automations, where AI is used and where a person approves, data and security notes.
5. Build route. Per part: configure, connect, Base44 with Jarvis, or developer. A verdict on whether the member can self build with Jarvis.
6. Effort and running costs. Bands and monthly lines, all labelled.
7. Price check. 10 and 5 percent, build cost, verdict.
8. Risks. Riskiest assumption and the test, then other risks.
9. Questions before or on call two. One line each, ready to send.
10. Developer quote request. Copy ready. No client price, no margin, no negotiation notes. Client name optional.

In chat, lead with a short summary under 200 words: what to build, the verdict, the riskiest assumption and the next action. Save the full design to the client's opportunity record when available, otherwise return it as one copyable document.

## Rules

- Never invent tools, volumes, numbers, integrations or client quotes. If it was not said, it is an unknown and goes in section 9.
- Never promise a connector or capability marked not supported or unknown. Write "to be confirmed" instead.
- Keep the client's language in sections 1, 2 and 3. Be technically exact in sections 4, 5 and 6.
- Plain names for systems. "A job board with automatic invoice reminders", not "an AI powered operations layer".
- AI only where it earns its place: reading messy input, drafting, summarising, answering from known information. Rules based steps stay rules based. Every AI step that touches money, customers or legal decisions has a human approval.
- Customer messaging must respect consent: opt out on email, recorded permission for SMS, no AI voice calls to people who did not agree to them. If the design depends on it, say so in risks.
- Keys and passwords go in secret storage, never in chat, the design or the quote request.
- Estimates are ranges with assumptions. Never a fake quote, a firm date or a guaranteed result.
- One system per design. If the client needs two separable systems, write two designs and say which to sell first.
- Plain sentences. No em dashes.

## After the design

Offer these, do not run them unasked:
1. Build the proposal from this design (jarvis-proposal-builder).
2. Write the message to the client that clears the open questions.
3. Send the quote request to a developer (Module 7, Find and Vet Developers).

When a real developer quote comes back, update section 6 and 7 with the quote and rerun the price check. Mark the design with a new version and date.

## HQ (Jarvis 2.0)
In Jarvis 2.0, "saved offer", "offer brief", "funnel record", "campaign record", "project record" and "CRM" all mean the HQ tables in the jarvis-hq skill. Do not keep a second copy anywhere else.
Read first: Deals, Calls, Offer. Do not ask the member for anything HQ already holds.
Write when done: Deals: solution design link, problem cost and whether the client confirmed it.
After writing, read the rows back and confirm they saved before you tell the member it is done.

---

## Appendix: solution design template
(Formerly the appendix "solution design template" below.)

### Solution design: [client], [project]
Version [n], [date]. Status: draft for call two. Not a quote, not a signed scope.

## 0. Readiness
Ready or not ready. If not ready, the missing items and why they matter.

## 1. The problem and the number
The problems in the client's words, who they land on, real examples.
Agreed annual cost: [figure], how it was worked out, confirmed by the client yes or no.

## 2. Prescribed solution
One paragraph a business owner would agree with.
Then each part, in go live order:
Part [n], [plain name]. What it does. Fixes: [pain], worth [figure from the brief].
Not included: [items]. Follow on ideas: [items].

## 3. One job, before and after
Before: trigger, steps, who, tool, where it stalls.
After: trigger, what the system does, where a person approves, the useful output.
One realistic exception and what happens.

## 4. Technical design
Components: [list].
Key records: [record, main fields, source of truth].
Integrations, one line per tool: reads, writes, login owner, status (verified, plausible, unknown, not supported), date checked.
Triggers and automations: [event, action, retry, duplicate rule].
AI use: [where, what it does, who approves].
Data and security: [sensitive data, access by role, where secrets live].

## 5. Build route
Per part: configure, connect, Base44 with Jarvis, or developer, and why.
Self build verdict: yes, partly (which parts need a developer), or no.

## 6. Effort and running costs
Per part: band, hours range, label (estimate, quote or confirmed).
Build cost range: hours times rate, or hours only.
Monthly running costs: one line each, labelled.

## 7. Price check
Problem cost [x]. 10 percent [x]. 5 percent [x]. Build cost [range].
Verdict: go, shrink, too small or not ready, with one sentence on why.

## 8. Risks
Riskiest assumption: [one line]. Test before call two: [smallest test].
Other risks: [one line each].

## 9. Questions before or on call two
One line each, phrased so the member can send it today.

## 10. Developer quote request
Project in one paragraph. Parts, with what each must do. Tools and access needed. Sample inputs and expected outputs. Acceptance checks per part. Constraints (data, hosting, deadlines). Ask for hours or a fixed price per part, exclusions, timeline and support terms.
No client price, no margin, no negotiation notes.

---

## Appendix: build patterns
(Formerly the appendix "build patterns" below.)

### Build patterns

Most small and medium business pains fit one of these. Pick the pattern, then adapt it to the client's tools and volumes. Sizes refer to the bands in estimating.md. Running cost lines are categories to price, not prices.

Contents: 1 Enquiry catcher. 2 Missed call recovery and AI receptionist. 3 Quote follow up. 4 Invoice and payment chasing. 5 Booking, reminders and no shows. 6 One job record (custom CRM). 7 Document intake. 8 Weekly numbers. 9 Reviews. 10 Knowledge assistant. 11 Client onboarding. 12 Reactivation.

## 1. Enquiry catcher (lead response)
Fits when: enquiries arrive by email, web form or social and sit unanswered for hours.
Components: intake from inbox or form, a lead record, AI drafted reply, owner alert, follow up if no reply.
Integrations: Gmail or Outlook, website form, CRM or a Base44 table.
Human step: owner approves replies until trusted, then only for quotes and prices.
Size: small. Medium if it must write into an existing CRM with a weak API.
Running costs: AI usage per message, Base44 plan.
Watch outs: duplicate leads from the same person, spam, enquiries that need a site visit before any price.

## 2. Missed call recovery and AI receptionist
Fits when: calls go unanswered during jobs or after hours.
Components: voice agent on a number the business controls, call summary, booking or callback task, owner alert.
Integrations: Retell or a similar voice provider, Twilio or the provider's numbers, calendar, CRM.
Human step: owner reviews summaries and handles anything the agent flags.
Size: medium. Large with live booking into a job system that has no clean API.
Running costs: voice minutes, phone number rental, AI usage, SMS if used.
Watch outs: call forwarding or porting from the existing line, voicemail traps when a transfer goes to a mobile, a disclosure that it is an AI, SMS registration and consent. Base44's own agent phone cannot answer a public business line.

## 3. Quote follow up
Fits when: quotes go out and nobody chases them.
Components: read sent quotes, a follow up schedule, drafted nudges, stop on reply or acceptance, a weekly list of open quotes.
Integrations: job or quoting system (ServiceM8, Jobber, Tradify, QuickBooks estimates), email.
Human step: owner approves the first nudge per quote type.
Size: small if the quoting tool exposes quote status. Medium if status must be read from email.
Running costs: AI usage, any paid API tier on the quoting tool.
Watch outs: quotes accepted by phone never update the system, so nudges must stop on any reply.

## 4. Invoice and payment chasing
Fits when: invoices go out late or overdue money is not chased.
Components: same day invoice trigger at job completion, overdue reminders, a weekly aged debt list.
Integrations: accounting tool, job system.
Human step: owner approves wording and any final notice.
Size: small to medium.
Running costs: AI usage, accounting tool API tier if needed.
Watch outs: Xero has no Base44 connector as of 1 Nov 2026, so it needs a custom integration or a developer. Never send legal or collections threats automatically.

## 5. Booking, reminders and no shows
Fits when: no shows, double bookings or lots of back and forth to book.
Components: booking page or calendar rules, confirmation and reminders, reschedule link, no show follow up.
Integrations: Google or Microsoft calendar, booking tool, SMS provider, CRM.
Human step: staff handle exceptions and same day changes.
Size: small with an existing booking tool. Medium if availability depends on staff, rooms or travel.
Running costs: booking tool, SMS, AI usage.
Watch outs: time zones, travel time between jobs, SMS consent.

## 6. One job record (custom CRM or operations app)
Fits when: the job lives across spreadsheets, inboxes and a rigid platform, with paid staff copying data between them.
Components: job and customer records, pipeline stages, roles and permissions, tasks, documents, automations at stage changes, a simple numbers view.
Integrations: email, calendar, accounting, e-signature, payments.
Human step: staff own the stage changes that mean money or a legal commitment.
Size: large. Phase it: first workflow live, then the rest.
Running costs: Base44 plan or hosting, AI usage, e-signature and payment fees, support retainer.
Watch outs: data migration from the old system, per user access rules, the old platform's notice period, who owns the data after handover.

## 7. Document intake
Fits when: staff retype details from PDFs, forms, photos or emails.
Components: upload or inbox intake, AI extraction to fields, a check screen for uncertain fields, save to the record.
Integrations: email, storage, the target system.
Human step: a person confirms any field the model is unsure of, and always money, IDs and legal details.
Size: medium.
Running costs: AI usage per document, storage.
Watch outs: handwriting and poor scans, health or identity data (see the data rules in platform-facts.md).

## 8. Weekly numbers
Fits when: the owner cannot see enquiries, quotes, jobs and cash in one place.
Components: pull counts from connected tools, a weekly summary message, a small dashboard if wanted.
Size: small once the data sources are connected.
Running costs: AI usage, Base44 plan.
Watch outs: numbers are only as good as the source. Never show sample metrics as real.

## 9. Reviews
Fits when: happy customers never get asked for a review.
Components: trigger after job completion, review request, reply drafts for new reviews.
Size: small.
Watch outs: Google Business Profile has no Base44 connector as of 1 Nov 2026, so reply drafts are pasted by hand or need a developer. Never filter who gets asked by sentiment and never write fake reviews.

## 10. Knowledge assistant
Fits when: staff keep asking the owner the same questions, or customers ask the same things.
Components: approved source documents, an assistant that answers from them and shows the source, handoff to a person when unsure.
Size: small to medium.
Watch outs: out of date documents, access limits on internal information, no medical, legal or financial advice to customers.

## 11. Client onboarding
Fits when: new clients get a messy start with forms, documents and chasing.
Components: intake form, document checklist, welcome sequence, a task list for staff.
Size: small to medium.

## 12. Reactivation
Fits when: there is a list of past customers or old leads nobody contacts.
Components: list clean up, segments, one relevant offer, replies routed to the owner.
Size: small.
Watch outs: consent and opt outs for email and SMS. Old lists bounce and harm the sending domain.

---

## Appendix: estimating
(Formerly the appendix "estimating" below.)

### Estimating

Estimates help the member decide whether the deal makes sense before call two. They are not quotes. Replace them with a real developer quote as soon as one exists.

## Effort bands (developer hours)
These are starting bands from the technical lead. Calibrate them after the first real quotes.
Small: one trigger, one or two connected tools, no new screens. About 4 to 15 hours.
Medium: a workflow of three to five steps, two to four integrations, one or two simple screens. About 20 to 60 hours.
Large: an app or CRM with roles, several screens, migration, or five or more integrations. About 80 to 250 hours. Always phase it.

Move a part up a band when an integration is unknown or not supported, the client's data is messy, there is a migration, more than one role needs different access, or customer facing messaging needs consent and compliance work.

## Build cost
Build cost is hours times the developer rate. Use the member's rate or a real quote. If neither exists, give the hours only and write "rate to be set". Do not invent a market rate.
Self build with Jarvis: there is no developer cost, but there is the member's time and Base44 credits. Say how many build sessions it is likely to take, and whether any part needs a developer anyway.

## Running costs
List each as a separate monthly line. Write "check current price" unless the price was confirmed with a date:
Base44 plan and credits, AI model usage, voice minutes, phone numbers, SMS and registration, email sending and domains, third party subscriptions or API tiers, hosting outside Base44, support retainer.
Next to it, show what the client stops paying, if anything. That is often part of the sale.

## Price check
Show:
1. The agreed annual problem cost and its source.
2. 10 percent and 5 percent of it, the course's working range.
3. The estimated build cost range.
4. A verdict:
   Go: 5 percent is at least twice the high end of the build cost. This is the default floor. The member or Blake can change it.
   Shrink: the gap is too small. Name the part to cut or phase.
   Too small: the problem is too small for a custom build. Suggest configuring an existing tool or a lower priced offer.
If no developer rate exists, show the break even instead: the highest hourly rate at which the low and high hour estimates still pass the floor. It tells the member quickly whether the deal can work.
If the client never agreed the problem cost, write "not ready" instead of a verdict.

---

## Appendix: platform facts
(Formerly the appendix "platform facts" below.)

### Platform facts and feasibility checks

The technical team verified the facts below on the dates shown. Platforms change. Treat anything older than 30 days as plausible, recheck it, and record the date you checked.

## How to check an integration
For each tool the design touches, answer five questions:
1. What exactly do we read, and what do we write?
2. Is there an official connector or API for that action, on the plan this client is on?
3. How does it sign in: one shared login, or does each user connect their own? Who owns that login?
4. Is there a webhook or trigger for the event we need, or must we poll for changes?
5. Is there a test or sandbox account, or would we test on live data?

Then give one status: verified (we ran it), plausible (documented, not run), unknown (not checked or not documented), not supported (checked, it cannot).

## Base44 (checked 31 Oct to 1 Nov 2026)
Supported connectors seen: Gmail, Google Calendar, Outlook, QuickBooks. Gmail may connect with full access even when the card says read only, so check the actual access.
Not supported: Xero, Google Business Profile.
Custom integrations from an OpenAPI spec exist in workspace settings, so a tool with a documented API can often be added. Mark it plausible until tested.
The agent can browse public websites and research a business.
The agent can edit existing apps but cannot create a new app from chat. The member creates the empty app first.
Agent phone: outbound calls for the owner, Builder plan and above, a US number, about 5 calls an hour and 20 a day. Inbound only from trusted contacts. It cannot answer or text from a public business line, so it is not an AI receptionist.
Backend functions give external endpoints, and scheduled automations are documented. Row level security exists, but backend calls with service access bypass it, so ownership checks must be built and tested.
Credits: messages and workflows use message credits. Scheduled or heavy jobs cost the member credits on every run. Put this in running costs.

## Voice, SMS and email
Voice receptionist: the course uses Retell with Twilio. Plan for call forwarding or a new number, voicemail handling and a disclosure line.
SMS: needs the recipient's recorded permission. US business texting from local numbers needs A2P 10DLC registration, which takes time. Australia has its own spam and sender rules. Plan the lead time.
Email: an opt out on marketing email. Cold email goes from a separate warmed domain, never the client's main domain.

## Data and security
Health data (US HIPAA, AU health privacy), payment cards, identity documents and children's data raise the bar. If present, name them in the design, keep them out of AI prompts where possible, and flag the hosting and agreement questions for the developer.
Payments go through a hosted provider such as Stripe. Never store card numbers.
Larger clients may ask for data residency or a privately hosted model. That is a developer route and a bigger quote. Flag it rather than designing around it alone.
Secrets live in secret storage. Never in chat, documents or code shared with the client.
