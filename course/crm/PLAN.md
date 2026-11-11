# Student CRM: build plan

31 October 2026. Draft. Every step below waits for Blake's go. No app, account, integration or sending has been created or changed.

**First member experience:** an invite opens their pipeline, with the numbers card above it and an Add lead button. An empty pipeline says “Your leads will appear here”. A short walkthrough shows adding a lead, moving a card and opening its history. Team setup happens before the invite. A failed connection says “The team is fixing this” and alerts the technical owner; it never sends the student to a webhook or database screen.

## Build order and owners

| Step | Codex builds after approval | Blake's technical lead owns | Done when |
| --- | --- | --- | --- |
| 1. Prove the route | A two-member integration proof and exact field mapping for the chosen platform. | Test accounts, paid plan access, sender ownership, booking/mailbox choice, support owner and cost ceiling. | Both members have isolated records, credentials and sender identities. |
| 2. Establish records | Fixed stages, lead fields, timeline and event history. On GHL, a maintained snapshot plus the fields needed by the adapter. | Snapshot rollout, permission review and backup/export process. | Lead creation, edits and stage moves retain history; no member can read or change another's data. |
| 3. Connect Jarvis | Small API adapter, member-key validation, signed events, retry queue and duplicate protection. | Store and rotate secrets; provision each Jarvis connection. | Every real stage change reaches the correct Jarvis once in effect, including after an outage. |
| 4. Connect intake | Meta lead-form and existing calendar adapters; preserve source and qualification. | Authorise member accounts and map form/calendar ownership. | A form then a booking produces one lead; duplicates, Call 2, reschedules and cancellations behave correctly. |
| 5. Connect follow-up | Jarvis event handlers and message/call history ingestion. No student workflow builder. | Member-owned Twilio and mailbox connections, two-way replies, approved copy and sending eligibility. | Controlled test covers reminder, reply, opt-out, no-show, proposal and cancellation paths. |
| 6. Add the card | Morning Meta data import through Jarvis, event-based totals and the single card. | Meta read permissions, account timezone/currency, ticket targets and spend limits. | A known test dataset reconciles to spend, appointments and cash receipts; failed sync shows stale data, not zero. |
| 7. Pilot and hand over | Short walkthrough, recovery notes and draft corrections to affected course lessons. | One member pilot, monitoring, restore rehearsal and release decision. | Member can use it without technical help; team can diagnose and recover a broken connection. |

## Platform proof before committing

**Recommended GHL route:** validate subaccount API permissions, stage webhooks, Meta intake, member-owned Twilio, business-mailbox replies and the existing booking tool. Basic API access is listed on the $297 plan, but exact endpoint coverage must be checked before choosing a higher plan. Confirm the daily card can live on the member's landing screen; otherwise use one small hosted card view with authenticated member access. Keep follow-up decisions in Jarvis. Hide unused product areas and give members no setup duties. A snapshot is a template, not proof every existing subaccount will update safely. Track versions and roll updates through a test account first.

**If Blake chooses Base44:** prove the following in one team-owned paid app before building screens. Each remains **[VERIFY ON PAID PLAN]**, even where the underlying capability is documented:

- Two logins cannot list, guess IDs, edit ownership or access each other's leads, activities, daily figures or credentials. Apply member rules to all records. Service-role functions bypass those rules, so they must independently enforce ownership.
- Two external Jarvis keys are stored hashed, scoped and revocable. No master platform credential leaves the backend. Reject missing/revoked keys and cross-member IDs.
- A stage edit produces a signed outbound webhook; timeout, retry and replay do not lose events or duplicate actions. All stage writes use one controlled path. Reconcile saved changes against undelivered events.
- A scheduled job runs without a browser session. Confirm whether this app uses automations or workflows: current docs say apps with workflows enabled cannot deploy legacy function automations. No workflow editor is exposed to students.
- Two members connect separate Meta accounts and forms. Prove lead retrieval, account-to-member mapping, token renewal and daily spend access. A generic Meta connection or Pixel does not establish any of these.
- Confirm paid-plan entitlements, credits, limits and recovery behaviour at expected member volume. Record real operating cost, including support time, before promising savings.

If one Base44 requirement cannot pass, stop that route and propose the managed GHL setup to Blake. Do not make students install or repair a substitute.

## Rules that make the numbers and follow-up reliable

- Deduplicate using provider event IDs and member-scoped phone/email matching. Conflicting matches go to the team. Keep original acquisition source; store campaign/form IDs and website UTMs when available. Unknown attribution stays unknown.
- Count a person once for first Call 1 booking and once as a buyer. Reschedules replace the appointment time, not the lead. Show rate uses elapsed appointments with recorded attendance; missing outcomes are shown as incomplete. Call 2 is excluded from acquisition booking counts.
- Store immutable dated events rather than counting cards currently in a stage. Daily activity uses the member's timezone. Cumulative conversion figures group leads by acquisition period and include their later outcomes, labelled “to date”. Associate spend with that same acquisition period. Do not mix currencies.
- Record cash receipts on lead detail without adding invoicing. Won alone does not prove payment. Count a paying client once and revenue from actual receipts; correct mistakes with traceable adjustments. Ticket is agreed deal value, not a deposit amount.
- Jarvis rechecks booking, reply, pause and opt-out state immediately before sending. Replies stop automation until a person resumes it. Store invite acceptance and “yes” replies separately. Delivery failures go to the team. Resend is optional for permitted transactional email, never cold lists, and still needs a reply route.

## Gaps found in the required reading

The Meta campaign setup skill explicitly says Jarvis has no account access. It guides manual setup. The daily read-only Meta import is new integration work, not an existing verified capability. The ad scripting skill writes copy only; the pre-call skill produces drafts and event rules, not connected sending.

The CRM stub mentions builds and money beyond this brief; the Meta skill asks for per-ad tracking and weekly reviews. Those extra screens are outside v1. Store essential attribution internally and keep this release to the card. The follow-up lesson and handoff describe CRM-owned sending; this brief takes precedence: Jarvis runs follow-up through the member's connected senders, with history and stop state in the CRM. Update teaching copy only after Blake selects and approves the working route.

## Evidence and current checkpoint

Read all five named lesson files, the 30 October sender handoff, all three named Jarvis skills and CLOSER-SALES-PROCESS.md. Public capability and pricing references are linked in SPEC.md, checked 31 October 2026. Documentation supports feasibility, not a paid-plan or student test. Only SPEC.md and PLAN.md were produced. Proposed recommendation: managed GHL. Pending: Blake's decision and the three questions in SPEC.md. Next action: wait for Blake.
