# Student CRM: decision spec

31 October 2026. Draft for Blake. Spec only; no build authorised.

**Purpose:** run the member's agency pipeline. Blake's team connects and maintains everything. Members never debug integrations.

**Seven things in v1**

1. **Leads:** name, phone, email, business, source (Meta ad, outreach, referral), stage, notes, next action date. Add by hand or Jarvis.
2. **Pipeline:** drag cards through New lead, Contacted, Call 1 booked, Call 1 done, Proposal sent, Call 2 booked, Won, Lost, Not now. One fixed pipeline. Discovery first, proposal between calls, close on call two.
3. **Automatic intake:** Meta forms create leads; the existing booking tool creates or updates a lead and sets Call 1 booked. Match within that member only. Call 2 bookings never reset discovery. Base44 Meta intake: **[VERIFY ON PAID PLAN]**.
4. **Jarvis follow-up:** confirmation, prep, reminders, no-show recovery and proposal follow-up. Member-owned Twilio number and authenticated business mailbox. Replies pause automation; opt-outs stop sends; changed bookings cancel old reminders. No workflow editor.
5. **Daily numbers card:** spend, leads, CPL, qualified Call 1 bookings, cost per booked call, show rate, close rate, cash revenue and CAC against ticket. Show period, source and last sync. Jarvis imports Meta spend each morning; CRM events supply outcomes.
6. **Lead detail:** one timeline of messages in/out, delivery status, calls, stage moves and notes. Supporting fields: booking ID/time/timezone/type/outcome, qualification, attribution IDs, consent/opt-out, reply/pause state, ticket, cash received and payment date. No dialer or invoicing.
7. **Login:** each member sees only their records. Team provisions access and connections. No shared master key in a member's Jarvis.

**API and events:** member-scoped `createLead`, `updateStage`, `addNote`, `readPipeline`, `writeDailyNumbers`; add `recordActivity` for messages, call outcomes and cash receipts. Incoming hooks: lead form, booking created/changed/cancelled, message/reply/delivery/opt-out. Outgoing to Jarvis: every `stage.changed`, plus booking and reply/opt-out events. Include event ID, lead ID, time and changes; sign, retry and deduplicate. Team issues and revokes keys; server derives member identity from the key.

**Card maths:** spend / unique paid leads = CPL; spend / unique qualified paid Call 1 bookings = cost/booked call; attended / elapsed non-cancelled Call 1 appointments = show rate; unique buyers / unique leads who attended Call 1 = close rate; sum cash receipts = revenue; spend / unique paying clients = ad CAC; CAC / average sold ticket × 100 = CAC %. Use matching source and period, never divide paid spend by referral wins. Zero denominators show “No data”. Show daily activity plus cumulative conversion figures for leads acquired in the selected period, so sales delays stay visible. Below 50% CAC/ticket is the lesson's rough ceiling, not a profit guarantee; 25% is illustrative. Delivery costs still matter.

**Decision: GHL wins for v1 support load.** Use team-owned subaccounts, one maintained snapshot, restricted member access and a small Jarvis/card adapter. [GHL pricing](https://www.gohighlevel.com/pricing) is US$97/month for three subaccounts or US$297/month for unlimited with basic API access, plus usage. At ten members the latter is $29.70 each before usage/support. Existing pipeline, conversations and calendars reduce custom maintenance; snapshot drift, sender setup and the exact card still need team work. Lock-in is GHL's data model and configuration.

The alternative is one team-owned Base44 app, never copies per student. [Builder lists US$40/month billed annually](https://base44.com/pricing), plus usage, senders and engineering. It offers a tighter interface but makes us responsible for reliability. [Member data rules](https://docs.base44.com/developers/backend/resources/entities/security), [HTTP functions](https://docs.base44.com/developers/backend/resources/backend-functions/overview), [outbound requests](https://docs.base44.com/developers/references/sdk/getting-started/third-party-apis) and [scheduled jobs](https://docs.base44.com/developers/backend/resources/backend-functions/automations) are documented. Per-member API keys require our own validation layer. End-to-end isolation, keys, webhooks, schedule and separate Meta accounts: **[VERIFY ON PAID PLAN]**. No tested failure is established. If a requirement fails, use managed GHL, the smallest alternative. Base44 exports do not remove migration work for its backend and connectors.

**Excluded:** email/funnel/website builders, calendar engine, workflow editor, dialer, memberships, invoicing and reporting beyond this card.

**Questions for Blake**

1. Approve managed GHL, or prefer the Base44 proof first?
2. Which booking tool and mailbox provider should the first pilot support?
3. How many members at launch, and who is the named technical owner?
