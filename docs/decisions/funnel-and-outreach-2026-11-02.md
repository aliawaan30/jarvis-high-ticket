# Funnel skills, outreach proposal and version 9

2 November 2026. All three requested parts completed: canonical funnel skills updated, outreach research read and architecture proposed below, version 9 deployed to the existing public URL. No outreach launched.

## 1. The three one-line prompts

| Skill | Student prompt | What it now reads and asks |
|---|---|---|
| `jarvis-landing-page` | Run the landing page skill for my offer. Domain: [x]. Calendar: [link]. Video: [link or none yet]. | Reads the saved offer, six-line card, identity, approved claims/proof and funnel. Asks only for missing domain/identity, calendar, video/mode, or an unknown criterion that changes qualification. If several offers are active, asks which. It does not request the offer/proof pasted again. |
| `jarvis-confirmation-page` | Run the confirmation page skill for my landing page. Video: [link or placeholder]. | Reads saved offer, pages, identity, proof and calendar. Asks only for a missing funnel location, ambiguous active offer, video choice or necessary event/redirect setting. A placeholder does not block drafting. |
| `jarvis-precall-followup` | Run the pre-call follow up skill for my offer and my landing page. Calendar: [tool]. | Reads offer, pages, preparation/proof assets and booking records. Asks only for missing calendar/host information needed for the sequence. Sender access, sender identity/number and channel permissions are resolved before activation, not demanded before preparing copy. |

Canonical files are under `/Users/blakestephens/co-founder/projects/high-ticket-program/skills/`. All three passed `quick_validate.py`. These are instruction updates; no new Base44 execution or student test is claimed. Existing ZIPs were not silently replaced.

### Page order now explicit

**Landing → application → qualified booking page → real booking event → separate thank-you/confirmation page → pre-call follow-up.**

- Landing run builds all first three pages, with the compact VSL layout or no-VSL Offer Testing mode.
- Application has three/four useful fit questions one per screen, then name/email/phone together. No time estimate.
- Booking page: “Congratulations, your application has been approved. Book your free 30 minute audit.” One calendar embed. Eligibility is for the call; actual calendar duration/type must match.
- Confirmation skill is post-booking. It uses Blake's “You are booked in, not confirmed yet” to distinguish an existing reservation from attendance/invite acceptance. It must not claim acceptance is tracked if the calendar does not expose it. Already-confirmed attendance gets an accurate state. Video asks them to accept the invitation, followed by relevant real proof.
- Saved funnel state links all pages to the offer version. A redirect is not a booking event. The confirmation page does not contain another qualification form by default.

## 2. Outreach architecture after reading the research

Read `research/outreach-stack-2026-11-02.md`, the existing coordinator and its list/enrich/CRM references, plus `outreach/LEAN-PATH.md`. Proposed architecture only. The student experiences **one campaign with one lead timeline**, not seven unrelated agents.

### Existing coverage

`outreach/skills/jarvis-outreach-coordinator/SKILL.md` already covers list construction, contact research, fit review, outreach drafting and CRM records. Its `references/list.md`, `enrich.md`, `score.md`, `crm-and-execution.md` and `lab.md` are the reusable base. List and enrichment are references within this existing skill, not separately verified installed skills. The free-course Lead Finder is described in the research; this task did not verify a live member connection.

The current coordinator is explicitly research/draft-only for the lab. It does **not** send email, SMS or LinkedIn messages, place calls, or prove live reply handling. `jarvis-precall-followup` starts after booking; it is not a cold-outreach sender.

### Proposed skill set and one-line entries

| Skill | Reuse or new work | Student entry |
|---|---|---|
| `jarvis-outreach-coordinator` | Extend existing campaign planning/CRM orchestration with a shared schedule and channel dispatch contracts. | Prepare an outreach campaign for my saved offer in [market], using email, calls, LinkedIn and eligible SMS, with three touches per lead per week. |
| `jarvis-prospect-research` | Optional thin entry point over existing list/enrich/score references; avoid duplicating their logic. Can remain a coordinator mode initially. | Find and enrich [number] businesses for my offer in [place] and save them to my CRM. |
| `jarvis-email-outreach` | New sending adapter/workflow: draft, approved cohort import, scheduling, send receipts, bounces, replies and unsubscribe. | Prepare email outreach for my reviewed prospect list using [connected sender]. |
| `jarvis-sms-outreach` | New Twilio adapter with recorded channel permission, sender setup, delivery and STOP events. | Prepare SMS follow-up for the prospects in this campaign who have agreed to receive it. |
| `jarvis-outreach-calls` | New call brief/task and outcome workflow. Human calls first; AI provider adapter is an optional later mode. | Prepare today's calls for my campaign and log the outcomes I give you. |
| `jarvis-linkedin-outreach` | New drafting/manual task workflow initially; optional third-party provider adapter after capability and platform-permission review. | Prepare LinkedIn outreach for the relevant people in my campaign. |
| `jarvis-outreach-replies` | New reply/event reconciliation and next-action workflow across all connected channels. | Review my campaign replies, pause follow-ups where needed, and show me today's next actions. |

Preparation prompts do not activate sending. Once the member approves a defined cohort, messages, providers and limits, an explicit “Launch the approved campaign” can execute within that recorded scope without asking before every message. Missing channels become visible tasks/connection gaps; do not falsely label drafted or queued actions as sent.

### Three touches means three total, not three per channel

Example week for an eligible prospect: Monday email, Wednesday human call, Friday LinkedIn task. Where SMS permission exists, it can replace one of those touches. Without LinkedIn, use another suitable eligible channel. Not every lead must receive every channel.

The research's Monday/Tuesday/Thursday/Friday schedule contains four touches before SMS; it does not meet Blake's three-touch instruction. Apply the shared cap across channels and campaigns for that contact/account context. Reserve scheduled slots so two agents do not dispatch simultaneously. Replies stop the acquisition sequence pending review; booked calls hand over to pre-call follow-up. Opt-outs persist on reimport. Track actual attempts and delivery separately from planned touches.

### Lean tools, with a supported upgrade path

- Discovery: existing Places adapter where enabled and permitted, company-site research, relevant registries, supplied lists; Apollo for a suitable connected B2B workflow. Clay remains optional.
- Email: start with the member's suitable connected mailbox for an approved small campaign. Instantly/Smartlead/lemlist are candidate sequencers from the research, not newly tested integrations. Verify required API/webhook plan and total mailbox/domain cost before selecting one. Do not promise a safe daily cold volume or guaranteed first client.
- SMS: Twilio where sender setup, registration and recipient permission support the campaign. Receiving an email reply is not itself a text opt-in.
- Calls: student makes calls, Jarvis prepares and logs. Optional AI calls require a separately approved country/number-type use case and tested provider; not blanket permission for every business landline.
- LinkedIn: Jarvis research/copy plus member action is the workable baseline. A third-party API or MCP does not establish permission from LinkedIn. Candidate provider adapters stay optional, not a silently enabled default.

One CRM, one contact/account identity, one suppression record and one next action are essential. Provider adapters need actual auth, webhooks/polling, event deduplication and timeout reconciliation. A skill file cannot substitute for those connections. Existing member ownership/access controls must protect records in the backend.

### Corrections to carry back into the research

I inspected primary sources rather than adopting these research statements as release rules:

1. **Twilio's provider policy is stricter than “reply by email or published AU mobile”.** It requires express consent before messaging and express written consent for promotional messages. An email reply, connected LinkedIn profile or public mobile is not automatically that permission. Source: [Twilio Messaging Policy](https://www.twilio.com/en-us/legal/messaging-policy), Consent section. AU law and provider policy are separate checks.
2. **Email/phone publication and B2B status are not universal contact permission.** ACMA describes consent, identification and unsubscribe requirements for commercial electronic messages. Source: [ACMA](https://www.acma.gov.au/avoid-sending-spam). Do not copy the research's “email always” dispatch rule across countries.
3. **LinkedIn automation limits are not safe-use guarantees.** Its agreement prohibits bots and unauthorised automated messaging. Source: [LinkedIn User Agreement](https://www.linkedin.com/legal/user-agreement), section 8.2. A vendor's cap/API is not LinkedIn approval.
4. **Mailbox caps are not a deliverability promise.** Google distinguishes all-sender and bulk-sender requirements. Source: [Google sender guidelines](https://support.google.com/a/answer/81126?hl=en). Research daily volumes and prices remain planning assumptions until checked for the chosen accounts/providers.
5. **Scope is international, not AU-only.** Preserve the existing per-country contract. AU/US/UK research does not complete CA/NZ/EU support. An unsupported country/channel remains a specific connection/policy gap, not a reason to stop all eligible work.

Do not rewrite the supplied reading copy during this republish. These are implementation/research corrections for the course agent's next authoring pass.

### Seven outreach lessons

1. Set up the campaign and connect the CRM/tools.
2. Find, enrich and review the first accounts.
3. Prepare and run email outreach.
4. Add SMS where the contact and provider permit it.
5. Make calls; prepare, diagnose and log outcomes.
6. Use LinkedIn as part of the same account plan.
7. Run the daily replies/follow-up loop and improve from outcomes.

Release sequence: existing offline fixtures → read-only small account pilot → sandbox dispatch/event tests → explicitly approved small live campaign. Test reply-versus-queued-message races, duplicate events, uncertain sends, opt-out reimport, booking handoff and the shared three-touch cap. No prospect outreach was launched by this task.

## 3. Version 9 publication

- URL: https://jarvis-review-b8f2a64c9e7d4301a5c6.blakeyyyyyy.chatgpt.site
- Public access preserved.
- Version: **9**.
- Saved version: `appgprj_6ae356ebc7f08191888412947ade589c~appgver_6b12cf7a76f48191bfefe2344c1a7637`.
- Deployment: `appgdep_6ae879f5d304819191901b63343da465`, **succeeded**.
- Pushed source commit: `d3f9ef0f2c63735b6b88b205363425ba2d2b5fa4`.
- Source `index.html` SHA256: `f215bfd298ef6e0b108b51423494d080cb4e7c9464a9d8038250f9c0eab52c8f`.
- All 28 source HTML/data assets byte-matched `hosting/reading-copy/dist/` before publication. Supplied reading copy published unchanged.

Verified by HTTPS curl GET on the live URL:

- `11. AI content agency for ecommerce brands` present.
- `Run the landing page skill for my offer` present.
- `Follow ups due` present.
- `Build the Demo` absent.

Detailed deployment/marker verification is in `hosting/reading-copy-v9-checks.json`. Python urllib was blocked with HTTP 403; curl succeeded. The served HTML includes an injected Cloudflare script, so its raw hash differs from the source; the four live markers passed. No new browser interaction/visual course audit or student execution is claimed by these string checks. No additional GitHub mirror publication was requested or performed.
