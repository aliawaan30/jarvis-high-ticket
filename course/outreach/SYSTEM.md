# The Outreach System: design v2

29 October 2026. Claude, merging live tool research (`research-tools.md`), compliance research (`research-compliance.md`, with `research-compliance-intl.md` for UK, Canada, NZ and the EU), and the Codex offer agent's Jarvis architecture (`../handoffs/2026-10-29-from-offer-agent-outreach.md`). Design only. Nothing here has been run. Every rate is a planning assumption until the lab produces our own numbers.

v2 corrects v1 on three points from Blake: Clay has a full public API (v1 was wrong), manual cold calls to the business's listed number are fine even when that number is the owner's mobile, and the system must work in every country members sell into, not just Australia and the US.

## 0. Operating principle

A working system beats a pure Jarvis system. Jarvis does the judgment: defining the account, reading evidence, scoring, writing, reviewing replies. Platforms do the plumbing: finding people, enriching contacts, sending email, logging events. Where a platform already does a step as well or better than Jarvis could, use the platform and have Jarvis drive it. The member should never have to operate eight tools by hand, but they also should not wait for a Jarvis feature that a US$185 account already provides.

## 1. Clay is the data layer

Verified on 29 Oct against Clay's own developer docs (university.clay.com/docs/using-clay-as-an-api, developers.clay.com):

- Clay has a public REST API, a CLI and an agent plugin for Claude Code and Codex. **Available on every plan including Free and trial.** Auth is an API key created in the workspace. Using the API costs the same credits as using the app, nothing extra.
- Through it you can: search Clay's database of people and companies with structured filters (industry, headcount, location, titles); run Clay-managed functions, which is the enrichment and research catalogue (waterfall email and mobile finding across many providers, company lookups, Claygent research); run custom functions and workflows; create signals that fire on changes such as job postings; build Sequencer campaigns and read their analytics.
- Search limits by plan: paid self-serve is 500 results per request and 1,000,000 per rolling 30 days. Free is 50 per request and 100 per 30 days, which is enough to test and nothing more.
- Limits that shape the design: Tables are read-only through the API on self-serve plans (structured table queries need Enterprise). Launching, pausing and resuming a Sequencer campaign stays in the Clay app. So **our CRM is the system of record, not a Clay table**, and the member presses "launch" in Clay.
- Pricing (Clay's page shows two numbers for each, confirm before quoting members): Launch US$167 to 185 a month with 2,500 to 3,000 data credits; Growth US$446 to 495 with 6,000. Sequencer costs 0.03 credits per email on all plans. Launch sends from inboxes you already own; buying pre-warmed inboxes inside Clay needs Growth.
- Credit burn (third-party figures, inconsistent): a work email 2 to 3 credits single provider or 4 to 8 through a waterfall; a mobile 5 to 25 depending on provider. Clay does not charge data credits on a provider miss, so you mostly pay for hits.

Why Clay rather than stitching Places, Apollo, FullEnrich and Instantly ourselves: the waterfall across many providers will find more contacts than any single provider, which is the "same or better" test; signals are built in; sequencing is built in; one account to connect instead of four; and Blake's own agents can drive it through the plugin for the lab. The v1 cost estimate of US$200 to 350 for an API-direct stack still holds as a fallback for a member who refuses the Clay subscription, and the adapters stay swappable.

What Clay still does not give us: local service businesses with no domain and no LinkedIn presence (a plumber with a Google listing and a mobile). For those, Google Places remains the discovery source and Clay enriches from the business name, website and phone. And Australian owner mobile coverage is untested on every provider including Clay's waterfall. **The first thing the lab measures is contact coverage per country.**

## 2. The constraints the research found

1. **Owner mobiles in Australia are not reliably available from any provider.** The business line is the channel, and in a trade or clinic under 20 staff the owner often answers it, or the person who does knows exactly who decides.
2. **Australia has no business-to-business exemption for email.** A cold email is lawful only under conspicuous publication: the address is published by the business, there is no "no unsolicited" statement, and the message is relevant to the recipient's role. The Act also bars harvesting software and harvested lists. Every AU email carries a logged source URL and the system never bulk-harvests.
3. **The risky things are automated, not human.** A person dialling the number a business publishes is fine everywhere we checked, including when that number is the owner's mobile. What attracts the US$500 to 1,500 per message TCPA damages is autodialed or AI or prerecorded voice calls and SMS to mobiles without consent. So: humans call, Jarvis prepares. No cold SMS. No AI voice on cold calls in v1.
4. **LinkedIn bans automation.** HeyReach, Expandi and Waalaxy run against section 8.2 of the user agreement. Jarvis drafts, the member sends.
5. **Meta DMs cannot be cold-sent by API.** Instagram and Facebook DMs are manual, drafted by Jarvis.
6. **Email deliverability rules apply at any volume.** SPF, DKIM, DMARC, a separate sending domain, warmup, spam rate under 0.3 percent. Cold email from the main domain can burn it.
7. **Scraping Google Maps breaches Google's terms.** The Places API is allowed, nearly free at our volume, and returns website, phone, rating count and hours. It does not return an owner or an email.

## 3. Channel rules by country

The campaign carries a country. Jarvis holds the rule set per country and marks each contact eligible or not, per channel, with a reason. A contact with no eligible channel goes to the review queue, never to an invented channel. Rules below are plain-English summaries of `research-compliance.md` and `research-compliance-intl.md`; they are not legal advice, and items those files mark SECONDARY or UNSETTLED get confirmed before they become hard rules in a lesson.

| Channel | Australia | United States | UK, Canada, NZ, EU |
|---|---|---|---|
| Cold email to a published business address | Yes, under conspicuous publication. Log the source URL per address. Identify the sender, working unsubscribe honoured within 5 business days. Never harvest. | Yes, under CAN-SPAM. Accurate headers, postal address, opt-out honoured within 10 business days. | See the per-country table in section 3a once the international research lands. Canada and the EU are stricter than AU; the UK treats sole traders as individuals. |
| Human cold call to the business's listed number, including an owner's mobile | Yes. Business voice numbers cannot be on the Do Not Call Register. Identify yourself, keep to the Telemarketing Standard hours. If calling at scale, wash the list against the Register because a sole trader's mobile can be on it. | Yes. B2B calls are largely exempt from the Telemarketing Sales Rule. 8am to 9pm local. Manual dialling only. | Section 3a. The UK has a corporate TPS to check; Canada's DNCL exempts B2B. |
| Autodialed, AI or prerecorded voice calls | Not in v1. If ever used, disclose "AI assistant" at the start. | Not to mobiles without prior express consent. Not in v1. | Not in v1. |
| SMS | Only after a conversation where the person agreed, or in reply to their message. Register the sender ID (unregistered alphanumeric IDs show "Unverified" from 1 July 2026). | Not taught. | Not taught cold anywhere. |
| LinkedIn | Jarvis drafts, human sends. No bots or scraping tools on the account. | Same. | Same. |
| Instagram and Facebook DM | Manual, Jarvis drafts. | Same. | Same. |

### 3a. Per-country table

Summary of `research-compliance-intl.md`. Two design rules fall out of it before any row: **gate by the recipient's country and entity type, not the member's country** (every lead carries country plus company type: company versus sole trader or partnership), and **keep one cross-country suppression list** so an opt-out in one campaign holds everywhere.

| Country | Cold email to a business | Human cold call to the listed number | SMS | AI or automated voice | Data sourcing | Penalty scale |
|---|---|---|---|---|---|---|
| Australia | Conspicuous publication only. Log source URL per address. Unsubscribe within 5 business days. No harvesting. | Yes. Wash against the Do Not Call Register at scale (sole trader mobiles can be listed). Telemarketing Standard hours. | After a conversation only. Register sender ID. | Not in v1. | Business contact data from public sources is workable; no general business-contact exemption in the Privacy Act. | Six figures per message line in 2026 ACMA actions. |
| United States | Yes under CAN-SPAM: accurate headers, postal address, opt-out within 10 business days. | Yes. B2B largely exempt from the Telemarketing Sales Rule. 8am to 9pm local. | Not taught. | Not to mobiles without prior express consent. | Public business data is fine; CCPA reaches larger businesses and brokers. | Up to US$53k per email; US$500 to 1,500 per TCPA message or call. |
| United Kingdom | Companies and LLPs: yes, opt-out basis. Sole traders and partnerships: consent needed, so any lead not verified as a company is treated as an individual. Add a Companies House check per lead. | Yes for companies, but screen every list against the Telephone Preference Service and the Corporate TPS plus an internal do-not-call list. | After a conversation only. | Treat as an automated call needing prior consent. UNSETTLED for conversational agents. | UK GDPR legitimate interest covers B2B contact data with a documented assessment. | PECR maximum now GBP 17.5m or 4 percent of turnover (Data (Use and Access) Act 2025, from Feb 2026, date SECONDARY). |
| Canada | CASL: conspicuous publication, role relevance, no "no spam" notice, and the sender carries the burden of proof. Store URL, date and screenshot per lead. | Yes. Business numbers sit outside the National Do Not Call List. 9:00 to 21:30 weekdays. Whether B2B-only callers must register with the DNCL operator is UNSETTLED. | After a conversation only. | Prior consent. | PIPEDA business contact information exception applies when used to contact the person in their business role. | Up to CAD 10m per violation. |
| New Zealand | Deemed consent on the same three tests as Canada (published, relevant, no opt-out notice). | Yes. No specific rule on voice calls found. | After a conversation only. | Disclose AI at the start; no NZ rule found. | Privacy Act 2020; IPP 3A indirect-collection notice in force since 1 May 2026. | Up to NZD 500k for organisations. |
| Germany | **No cold email at all.** UWG section 7 needs prior express consent, no B2B exception. | Only with "presumed consent" tied to that business and that offer, and competitors enforce with cease-and-desist letters. Treat as high risk. | No. | No. | GDPR; legitimate interest is a weak basis here. | Up to EUR 300k plus competitor claims. |
| Netherlands and Ireland | B2B email to published business contacts, relevant to the business, with opt-out. Sole traders are natural persons, so opt-in. | Yes for companies, with national opt-out registers to respect. | After a conversation only. | Prior consent. | GDPR legitimate interest with a documented assessment. | GDPR scale (up to 4 percent of turnover). |

EU-wide: the AI Act's Article 50 transparency duty applies from 2 August 2026 (SECONDARY), so any AI-generated interaction with a person discloses that it is AI. Disclose AI at the start of every automated contact everywhere, whether or not the law requires it.

Before any of these rows becomes a hard rule in a lesson, the open items at the end of `research-compliance-intl.md` list the primary texts still to fetch (several regulator sites returned 403 or 404 during research).

## 4. The system, stage by stage

One request from the member, in the Codex agent's words: "Find businesses that fit this offer, show me why they fit, prepare the outreach and keep the campaign organised." Underneath, seven stages. Jarvis runs stages 1 to 6 with a review gate at each. The member runs stage 7 with Jarvis beside them.

### Stage 0. The approved offer brief
Input from Module 2 and the strategy session: buyer type and geography, the problem, the solution, who decides, exclusions, approved claims, the demo. No campaign without an approved, versioned brief. A research hypothesis can run a discovery campaign (booking conversations to learn), not a sales campaign promising an unscoped result.

### Stage 1. Define the account (Jarvis)
Jarvis turns the brief into: a one-line account definition, three to five fit signals visible from outside, disqualifiers, and the discovery questions that would confirm the pain. A signal is a reason to investigate, not proof of pain. Member confirms the buyer is commercially worth it and that they understand the problem in their own words.

### Stage 2. Build the list (Clay, plus Places for local)
- **Businesses with a domain and staff (most US, larger AU, UK, CA, NZ, EU):** Clay company search by industry, headcount and location through the API, written to our CRM.
- **Local service businesses (most AU trades and clinics):** Google Places Text Search by category and suburb, filtered by rating count, hours and whether a website exists. This is the free course's Website Lead Finder, reused, then handed to Clay for enrichment.
Deduplicate on canonical domain plus provider ID, with branch rules so franchisees and multi-site businesses do not collapse into one. Output: 200 to 300 raw accounts with website, phone, listing data and provider IDs.

### Stage 3. Score on pain signals (Jarvis, with Clay signals and Claygent)
This is the bet that makes the system worth more than scrape-and-blast. For each account Jarvis reads the website and the public listing and records evidence against the stage 1 signals. Clay signals (job postings, headcount changes, tech detected) and Claygent research per account feed it. Signals we can actually see from outside:
- Hiring an admin, receptionist or scheduler (Clay job-posting signals; Seek has no read API so AU job ads are Jarvis reading the public page, terms to confirm).
- Reviews that mention nobody answering, slow quotes, missed callbacks.
- No online booking, no quote form, a contact form that goes nowhere.
- Running paid ads (the Meta Ad Library is public and searchable by page; to confirm as a Jarvis-readable source).
- Software with known limits, detectable from the site (the CRM pattern from Module 6).
- Website age, last post on socials, review velocity.
Output: each account tiered A, B or C with the quoted evidence and the source date. A missing field is unknown, not a negative. **The member reviews the first ten by hand before trusting any tier,** then corrects the criteria, and Jarvis rescores. Keep the earlier version so we can see whether fit improved.

### Stage 4. Find the decision maker (Clay people search, plus registries)
- Clay people search by company and title for owner, director, GM or operations roles, in every country.
- **AU top-up:** ABN Lookup web services (free, needs a registered GUID) give the registered entity; the ASIC companies dataset on data.gov.au gives officeholders; a sole trader's ABN is the person.
- **Elsewhere:** state and national business registries where Clay has no record.
Output: a named person per A account, with role evidence, flagged as a hypothesis until confirmed by phone. Business fit, identity accuracy, reachability and permission are four separate fields, never one "qualified" tick.

### Stage 5. Enrich (Clay waterfall)
Clay-managed functions: find work email through the waterfall, then mobile only for A accounts where the country rules allow using it. Every contact carries its provider, source and checked date. **Test coverage per country on 100 to 300 real contacts before promising members anything,** and record credits spent per usable contact.
Output: a contactable A list in the CRM with channel eligibility per contact, each with a reason.

### Stage 6. Write and plan the sequence (Jarvis)
Jarvis writes one problem, one angle, adapted per channel: a call opener, an email with two follow-ups, a LinkedIn message, a DM, and an SMS draft held for use only after a conversation. The same words on every channel reads like a machine, so each channel gets its own version of the same angle. Every personalised factual claim is tied to a piece of stage 3 evidence. The member approves the first batch and the templates.
Sequence v1, as a working shape, three touches a week for three weeks: call the listed number first, email the same day, LinkedIn connect in week one, second call and second email in week two, final email in week three. Any reply, booking or opt-out stops every pending touch on every channel for that contact, and pauses the rest of the account for review.

### Stage 7. Run it (member, Clay Sequencer, Jarvis)
- Calls: the member dials the listed number, Jarvis has the account card open (evidence, opener, the discovery questions). Manual dialling in v1. A power dialler is a later add for members who want it.
- Email: Clay Sequencer on a separate sending domain warmed for two to three weeks, about 20 emails a day per inbox, three inboxes per domain. The member presses launch in Clay. Instantly or Smartlead remain the fallback for a member who already has them.
- LinkedIn and DMs: Jarvis drafts in the queue, the member sends.
- Replies: Jarvis classifies intent, drafts the reply, pauses the sequence, proposes the booking. The member sends anything commercial. Jarvis does not sell autonomously in v1.
- Before any send, the scheduler rechecks approval version, suppression, reply state and limits. A timeout is not a failed send. Never blindly resend.

### The funnel we track, every campaign
Accounts inspected, accounts accepted after review, named buyers, contactable by channel, touches sent, replies (positive and negative), opt-outs, conversations, call ones booked, attended, qualified, call twos, won, cash collected, plus data cost, sending cost and human minutes. Cost per held qualified meeting includes all of it. Opens are not an outcome.

### Volume, as a planning assumption
Two closed deals a month at five figures, on Module 6's two call close, needs roughly seven call ones. Published benchmarks for signal-based outbound (8 to 25 percent reply) are vendor claims and none are for small trades. Plan on low single-digit reply and 0.5 to 2 percent booked-call rate until the lab says otherwise. At 1 percent booked, seven call ones means about 700 contactable A contacts a month, which is more than one person should start with. So the first campaign is 30 accounts, reviewed by hand, and the second is bigger only if the first taught us the signals work.

## 5. Where Jarvis lives, and what it cannot do from a skill file

Student Jarvis stays on Base44. The Codex agent's table in its handoff is the honest split: briefs, research reasoning, copy and review summaries can live in Superagent skills; Clay and Places need the member's own paid accounts connected as tools, which a skill upload does not supply; CRM reads and writes need a tested app connection; schedules and retries need a tested Base44 workflow or an external service; LinkedIn and DMs stay manual; Retell and local scripts are not transferred by a skill. None of those connections have been tested in a member's account. That is what the lab is for. If connecting Clay to a Base44 Superagent proves slow, the fallback is explicit: the member runs the Clay steps in Clay's own interface following the lesson, and Jarvis does the judgment steps. Working beats pure.

Proposed skill set (design names, Codex handoff section 3): coordinator, account definition, account research (list plus scoring), buyer contact research (plus enrichment), outreach writer, campaign planner, reply and booking assistant, campaign review. Build the coordinator plus the references for one lab first. Do not multiply skills before one complete path works.

## 6. The lab: run it on our own offer before teaching it

Codex handoff "Lab plan", agreed, with Clay as the data layer. Blake's own agents can run it through Clay's plugin for Claude Code and Codex. Five phases.

A. Offline rehearsal with ten synthetic fixtures (strong fit, wrong country, duplicate branch, reply before send, opt-out after import, ambiguous timeout). Outbound disabled, providers mocked. Proves the workflow does not invent evidence, duplicate actions or send without permission.
B. Read-only data pilot: 30 real accounts in one market, one offer, on a Clay Launch account. Provider spend authorised first. Label the first ten by hand, revise, score the rest. Measures fit precision, buyer identity accuracy, contact coverage by channel and country, credits per usable contact, review minutes. No messages.
C. Member-environment rehearsal: fresh student Base44 setup, test tools only, ten records through research, copy, review and CRM handoff. Close and reopen the chat and resume. Break a credential, exhaust a quota, replay a webhook.
D. Live pilot, separately authorised by Blake: a saved manifest with exact cohort, sender identities, channels, copy versions, limits, dates and who answers replies. Small cohort, fixed observation window, a named person able to pause everything.
E. Compare signal-ranked against randomly ordered eligible accounts in the same segment, then turn the recordings, failures and revisions into Module 3.

Which offer runs the lab is Blake's call. Selling the course and selling a custom implementation are different funnels and must not share a results cohort.

## 7. What is still unknown

- Contact coverage per country from Clay's waterfall, especially AU mobiles (test, do not assume).
- Clay's current plan prices (the pricing page contradicts itself) and the exact credit cost per managed function.
- Whether a Base44 Superagent can call Clay's API as a connected tool, read and write the member's CRM, and run a durable schedule.
- Seek's terms for reading job ads; the Meta Ad Library as a scoring source.
- The exact Telemarketing Standard hours and the conspicuous publication clause text, from primary sources.
- UK, Canada, NZ and EU rules rest partly on secondary sources; primary texts listed in `research-compliance-intl.md` still to fetch.

## 8. Build order

1. Blake confirms the lab offer, opens a Clay Launch account for the lab, and authorises data spend.
2. Coordinator skill plus references, written against this document and the Codex data contract (Codex agent, with me reviewing).
3. Phase A and B of the lab (me, through Clay's plugin), producing the coverage numbers and cost per accepted account.
4. Rewrite Module 3 from what phase B actually showed, lesson by lesson: account definition, list, scoring, decision maker, enrichment, the sequence, running it. The current one-page lesson becomes the overview.
5. Phase D only after Blake approves the manifest.
