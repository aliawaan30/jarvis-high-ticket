# Outreach compliance research: AU and US cold outreach by small AI agencies

Prepared 29 Oct 2026. General information for course design only. This is not legal advice. Members should get advice from a lawyer in their own jurisdiction before running volume.

## How to read the confidence tags

- [PRIMARY] I read the regulator, statute or platform page in this research pass.
- [SECONDARY] Law-firm or vendor summary only. Verify before it goes into a lesson as a hard number.
- [KNOWLEDGE] From established law I know well but did not re-fetch today. Verify the cite.
- [UNSETTLED] Sources disagree or courts have not decided.

Several sources I found were vendor blogs. Anything resting only on those is tagged SECONDARY and should not be taught as a hard number without a primary check.

---

## 0. The five rules that should shape the system design

1. Australia: email and SMS are the same legal animal (Spam Act). Both need consent, and for cold B2B the only route is "conspicuous publication" with a role-relevance test. It is narrow, and it is not a licence to blast every business with a published address.
2. Australia: the Do Not Call Register does NOT accept business numbers (only private/domestic numbers, government numbers and business fax). Cold calling a genuine business line is not a register breach, but the Telemarketing Industry Standard (hours, identification) still applies. A sole trader's mobile that is also personal-use can be registered, so wash anyway.
3. US: B2B cold email is lawful under CAN-SPAM if it meets the rules. B2B cold SMS and AI-voice calls to a mobile are the high-risk zone, because TCPA does not have a B2B carve-out for cell phones and damages are $500 to $1,500 per message.
4. LinkedIn and Instagram/Facebook: the platform terms ban bots, scraping and unauthorised automation. The risk is account loss (and for an agency, client-account loss), not a regulator fine. Design for human-sent or API-permitted channels only.
5. Data: scraping Google Maps/websites is mostly a platform terms-of-service problem rather than a criminal one. The real legal exposure is what you do with the data (Spam Act address-harvesting rules in AU, TCPA in US). If you buy mobile numbers from Apollo/Lusha, you carry the sending risk, not them.

---

## 1. Cold EMAIL to a business owner

### 1A. Australia (Spam Act 2003)

What the Act does [KNOWLEDGE, headings confirmed PRIMARY on legislation.gov.au]:
- s16: you must not send, or cause to be sent, an unsolicited commercial electronic message that has an Australian link.
- s17: the message must clearly identify the sender (name, and contact details that are accurate and valid for at least 30 days after sending).
- s18: the message must contain a functional unsubscribe facility. The unsubscribe must be honoured within 5 working days, and must not cost the recipient more than a normal message or reply.
- "Commercial electronic message" is any message that offers, advertises or promotes goods, services or business opportunities. B2B pitches count. Being "business to business" is NOT an exemption in AU.
- "Electronic message" covers email, SMS, MMS, iMessage and instant messaging. It excludes ordinary voice calls.

Consent, and the "conspicuous publication" exception (Schedule 2, clause 4) [KNOWLEDGE for exact conditions; headings PRIMARY; ACMA summary SECONDARY]:
Consent can be inferred where ALL of these are true:
1. The address was conspicuously published, for example on the business website, in a directory, or in an ad. Hidden, or obtained by scraping, or from a purchased list is weaker. Conspicuous means a person would notice it; it does not cover addresses published in obscure places.
2. The publication carried no statement that the address holder does not want unsolicited commercial messages (check footers, contact pages and "no spam" notices).
3. The message is relevant to the work-related functions of the person who published or holds the address. The role is read from the address (accounts@, sales@) or the context where it was published.

Plain English: if you sell website redesign, an email to the info@ or the owner's address on a trades website is arguably relevant to the owner. An email to a randomly picked accounts@ mailbox pitching something unrelated to accounts is not. ACMA has said publishing an address is not an open invitation to send anything [SECONDARY, mailing-list quote]. The burden of proof of consent sits with the sender, so record the URL, date and a screenshot for every lead.

Other Spam Act points [KNOWLEDGE, verify]:
- Address-harvesting software and harvested-address lists: the Act prohibits supplying, acquiring or using address-harvesting software or lists produced by it in connection with sending unsolicited commercial messages. Treat scraped email lists as a red flag. This is the clause that bites a "scrape then email" workflow.
- Consent is not transferable. A purchased list is not consent unless the people consented to messages from you or your category.
- Penalties are not set by a single figure; ACMA uses formal warnings, infringement notices, enforceable undertakings and Federal Court civil penalties.

ACMA enforcement examples (use as scale, not as a formula):
- Tabcorp, infringement notice dated 10 April 2026, $330,000 for one line of messages (50 contraventions of s16(1)) [PRIMARY, ACMA notice PDF found in search; read from the search extract only].
- Latitude, infringement notice dated 20 January 2026, ACMA investigation opened 30 October 2025 [PRIMARY existence; the $4m figure is aggregator-only, SECONDARY].
- Lululemon, about $702,000 in March 2026 [SECONDARY, primary notice not found].
- Optus, $504,000 (2022) and Oneflare, $75,600 (about 2021), Kogan and Ticketek notices exist on ACMA's site [SECONDARY via news, ACMA PDFs located].
- Smaller operators receive formal warnings first, but repeat offenders get notices. ACMA's 2025-26 focus is high-volume brands, but nothing in the Act scales down for small senders.

Change flag 2025/2026: ACMA's penalty tally rose through 2026 (wagering-sector fines reported as about $5.4m, SECONDARY). Enforcement is clearly active.

### 1B. United States (CAN-SPAM)

Per the FTC's compliance guide [PRIMARY, read 29 Oct 2026]:
1. Header information (From, To, Reply-To, routing) must be accurate and identify who sent it.
2. Subject line must not mislead.
3. Disclose that the message is an advertisement.
4. Include a valid physical postal address.
5. Give a clear opt-out and honour it within 10 business days.
6. The opt-out mechanism must work for at least 30 days after sending; no fee; no requirement to log in; do not sell or transfer opted-out addresses.
7. You are responsible for anyone sending on your behalf.
Penalty: up to $53,088 per separate email (the figure the FTC page carried; it is inflation-adjusted yearly so may be higher now). The FTC states the law "makes no exception for business-to-business email".

So B2B cold email in the US is permitted without prior consent (opt-out model), as long as the rules above are met. The US also has state laws that can be stricter (for example deceptive-subject-line rules), and the FTC Act on deceptive claims.

### 1C. Deliverability rules that are effectively mandatory in 2026

From Google's sender guidelines [PRIMARY, read 29 Oct 2026]:
- ALL senders to Gmail, regardless of volume: SPF or DKIM authentication, valid forward and reverse DNS, TLS, RFC 5322 formatting, no spoofing Gmail From headers, and spam rate under 0.3% in Postmaster Tools (target under 0.1%).
- Bulk senders (more than 5,000 messages/day to Gmail): SPF AND DKIM AND DMARC (policy may be "none"), From-domain alignment, one-click unsubscribe (List-Unsubscribe-Post) for marketing mail plus a visible unsubscribe link.
- Below 5,000/day, DMARC and one-click unsubscribe are not formally required, but Google recommends them and, in practice, any cold-email sender who skips them gets filtered. Treat SPF + DKIM + DMARC + one-click unsubscribe as non-optional for the course.
- Yahoo applies similar bulk-sender rules (SPF, DKIM, DMARC, one-click, spam rate under 0.3%) [KNOWLEDGE, not re-fetched; Microsoft Outlook.com added comparable bulk rules from May 2025, KNOWLEDGE, verify].
- Practical: use a separate sending domain (not the client's main domain), warm it up, keep volumes low per mailbox. This is deliverability hygiene, not law, but it protects the member's main domain.

### Email: what the member must do
- AU: send only where there is conspicuous publication AND the pitch is relevant to the person's role, with no "no unsolicited" statement. Log URL and screenshot.
- AU: sender name, real business details, and a working unsubscribe honoured within 5 working days.
- US: ad disclosure, physical address, accurate headers, opt-out honoured within 10 business days.
- Keep a suppression list across all campaigns and across both countries.
- SPF, DKIM, DMARC set up on a secondary domain; one-click unsubscribe header; spam rate monitored.

### Email: never do this
- Never email scraped or bought AU lists on the theory that "it is B2B".
- Never send an AU email that has no relevance to the recipient's role.
- Never hide who you are, fake a personal "we met" subject line, or use a deceptive From name.
- Never ignore a reply of "stop" or "remove me", or make unsubscribing require a login.
- Never send from the client's primary domain.

---

## 2. Cold SMS to a business mobile

### 2A. Australia

- Spam Act treats SMS exactly as email: it is an "electronic message" [KNOWLEDGE]. The same consent, identification and unsubscribe duties apply. Unsubscribe by replying STOP is the norm.
- Conspicuous publication: the clause covers any "electronic address" including a mobile number [KNOWLEDGE, clause text is address-neutral]. ACMA has said publishing an email address or mobile number on a website is not an open invitation [SECONDARY]. A number scraped from a Google listing or website still has to meet all three conditions (published, no refusal, relevant to role). Many Google Business Profile numbers are landlines or reception lines, and many mobiles are personal. [UNSETTLED]: I did not find an ACMA ruling on Google-listing mobiles specifically.
- Practical stance for the course: cold SMS in AU is higher-risk than cold email because it is intrusive, a personal mobile is more likely to be personal-use, and ACMA complaints are frictionless (forward to 0429 999 888, reported by ACMA publicly). Recommend email, calls and warm-up channels first. If a member insists, require conspicuous publication evidence and an identification plus STOP line in every message.
- Sender ID Register (change flag 2025/2026): the Telecommunications (SMS Sender ID Register) Industry Standard 2025 applies to telcos handling alphanumeric sender IDs. Per ACMA's telco guidance, from 1 July 2026 unregistered alphanumeric sender IDs are over-stamped "Unverified" [PRIMARY via ACMA telco page, extract from search; earlier target of Dec 2025 was moved]. Registration is done by the business through its SMS provider. Sources disagree on ID length (2-11 vs 3-11 characters); check your provider. Implication: a member sending under a brand name must register; sending from a plain mobile or long number is not an alphanumeric ID, but scam filtering is tightening.

### 2B. United States (TCPA)

Rules [KNOWLEDGE unless tagged]:
- Texts are "calls" under the TCPA. Marketing texts to a cell phone made with an automatic telephone dialing system or with an artificial/prerecorded voice need prior express written consent. After Facebook v. Duguid (2021) the "autodialer" definition is narrow, but plaintiffs still sue under (a) the DNC provisions, (b) state mini-TCPAs (Florida FTSA, Oklahoma, Maryland, Washington etc., which have lower thresholds and quiet hours), and (c) platform-level carrier rules. Do not rely on the autodialer loophole.
- Damages: $500 per violation, up to $1,500 if willful or knowing (47 U.S.C. 227). Every text is a separate violation, so a 1,000-text blast can be a $500,000 to $1.5m claim. Class actions are common.
- Business cell phones: there is no clean B2B exemption for cell phones. The DNC Registry rules protect "residential subscribers", and the FCC presumes wireless numbers are residential. A business owner's mobile is very likely to be treated as a consumer number, especially for a sole proprietor. [UNSETTLED at the margins: courts have gone both ways on mobile numbers used purely for business. Nothing safe to teach.]
- Hours: no telemarketing before 8am or after 9pm in the recipient's local time (47 CFR 64.1200(c)(1)) [KNOWLEDGE]. Some states are narrower (Florida 8am to 8pm, plus caps on attempts per 24 hours).
- 2024-2026 FCC changes:
  - Revocation of consent: opt-outs in any reasonable way, honoured within 10 business days. The part requiring one STOP to revoke ALL messages was delayed from April 2025 to April 2026, then on 6 Jan 2026 to 31 Jan 2027 [SECONDARY, multiple firms].
  - Latham & Watkins reports an FCC order released 1 Oct 2026 that lets callers limit informational revocations to the relevant category, keeps marketing revocation broad, and opens further comment [SECONDARY, single source, not yet effective until 30 days after Federal Register publication]. Treat as in flux.
  - One-to-one consent rule (2023 order) was vacated by the 11th Circuit on 24 Jan 2025 [SECONDARY, multiple firm summaries]. Lead-gen consent rules are therefore back to the previous standard.
  - McLaughlin Chiropractic v. McKesson (US Supreme Court, June 2025): district courts are not bound by FCC TCPA interpretations in private suits [KNOWLEDGE, verify]. Outcome: more inconsistent court rulings, more unpredictability for senders.
- A2P 10DLC: US carriers require a registered brand and campaign (via a provider like Twilio) for application-to-person texting from 10-digit numbers, and CTIA messaging principles require consent and prohibit purchased lists and "snowshoeing" (rotating numbers). Cold B2B texting does not fit an approved campaign type in practice; unregistered traffic is filtered. [KNOWLEDGE]

Recommendation for the course: US cold SMS is a "do not teach" channel. Use SMS only after the prospect has replied, opted in via a form, or booked a call.

### SMS: what the member must do
- AU: only with conspicuous-publication evidence; every message identifies the sender and has STOP; register any alphanumeric Sender ID.
- US: only with documented prior express written consent, registered 10DLC brand and campaign, STOP honoured, send within 8am to 9pm local.
- Keep consent records (what, when, where, wording).

### SMS: never do this
- Never text a number from a bought list, scraped listing or enrichment tool in the US.
- Never rely on "it is a business phone" as a defence.
- Never spoof or rotate numbers to avoid filters.
- Never text after STOP, or outside permitted hours.

---

## 3. Cold CALLS to a business

### 3A. Australia

- Do Not Call Register [PRIMARY, donotcall.gov.au]: general public can register numbers "used for private or domestic purposes"; government bodies can register government numbers; businesses can register fax numbers. Business voice numbers are not listed as registrable. So a genuine business line cannot be on the Register. Caveat: a sole trader's mobile used for both personal and business may be registered, so wash against the Register or avoid mobiles you are unsure about.
- The Telecommunications (Telemarketing and Research Calls) Industry Standard 2017 applies to telemarketing calls whether or not the number is on the Register [SECONDARY, confirmed by several summaries; get the Federal Register of Legislation text for the lesson]:
  - Calling hours: Monday to Friday 9am to 8pm, Saturday 9am to 5pm, no calls on Sundays or public holidays (one source says 8am weekday start; verify).
  - The caller must identify themselves and their organisation, and the purpose of the call, at the start; provide caller ID; end the call when asked; not call again after being told not to.
  - Keep call records.
- AI or recorded voices: I found no AU-specific rule for AI voices on outbound B2B calls. Vendor blogs say the Standard applies equally to AI-initiated calls [SECONDARY]. The Spam Act excludes standard voice calls [KNOWLEDGE]. There is no mandatory AI-disclosure law in AU as of today [see section 7], but a call that pretends to be a human while selling is a misleading-conduct risk under the Australian Consumer Law. [UNSETTLED]: treatment of fully automated outbound calls under the Do Not Call Register Act, because its "telemarketing call" definition is broad; verify with ACMA before teaching AI outbound cold calling in AU.

### 3B. United States

- TCPA, artificial or prerecorded voice [PRIMARY via FCC summary, secondary law-firm coverage]: on 8 Feb 2024 the FCC issued a declaratory ruling that AI-generated voices are "artificial" under the TCPA. So calls with AI voices to cell phones need prior express consent (written consent for telemarketing). Calls to residential landlines with artificial voice need consent too. The ruling is effective immediately.
- B2B and the TCPA: the artificial/prerecorded prohibition for cell phones applies regardless of whether the person is a business owner. The "residential line" limb does not cover pure business landlines, so an AI voice call to a business landline is a grey area federally [UNSETTLED], and states may still restrict it.
- FTC Telemarketing Sales Rule [PRIMARY]: "Most phone calls between a telemarketer and a business are exempt from the TSR." Exceptions: sales of nondurable office or cleaning supplies, and calls that pitch an individual employee for personal use. TSR calling hours are 8am to 9pm local time.
- National DNC Registry: protects residential subscribers; business numbers are not covered, and the FCC treats cell numbers as presumptively residential. A solo owner on a mobile is therefore the awkward case. Still honour company-specific "do not call me" requests (internal DNC list) [KNOWLEDGE].
- Identification: caller must state their identity at the start and give a number [KNOWLEDGE, 47 CFR 64.1200(b)].
- States: many states regulate telemarketing with registration, bonds, hours and their own DNC lists (Florida, Oklahoma, Texas, others). Recorded-call consent: all-party consent states (e.g., California, Florida, Washington, Illinois, Pennsylvania) require telling the person before recording, and AI voice vendors often record by default. [KNOWLEDGE]
- AI-disclosure laws affecting calls: no federal statute. California's bot-disclosure law (BPC 17941) is aimed at online bots used to influence a sale; sources conflict on its reach to voice calls [UNSETTLED]. Utah's 2025 AI Policy Act amendments require disclosing AI use when asked, and in regulated occupations upfront [SECONDARY]. Maine and Washington passed chatbot disclosure laws in 2025-26 [SECONDARY]. Safest rule: disclose AI at the start of every call in every state.
- Change flags: Feb 2024 AI ruling (still the anchor); revocation-rule delays through Jan 2027; October 2026 order in flux; no federal AI disclosure rule found.

### Calls: what the member must do
- AU: call business lines only within permitted hours, wash mobiles against the Register, identify at the start, honour "do not call again" immediately.
- US: calls to business landlines by a live human are the lowest-risk path. Respect 8am to 9pm local time, identify yourself, keep an internal DNC list.
- AI voice: disclose it is an AI at the start, keep the script honest, and for US cell phones obtain consent first.
- Log calls, outcomes and DNC requests.

### Calls: never do this
- Never run an AI voice agent to cold call US mobile numbers without documented consent.
- Never call outside hours, on Sundays/public holidays in AU, or after "stop calling".
- Never pose as a human or invent a relationship.
- Never call a sole trader's mobile pulled from an enrichment tool in the US.

---

## 4. LinkedIn

- User Agreement section 8.2 [PRIMARY, read 29 Oct 2026]: you agree not to "develop, support or use software, devices, scripts, robots or any other means or processes" to scrape or copy the Services (browser add-ons and crawlers named); not to "use bots or other unauthorized automated methods to access the Services" (including downloading contacts and generating engagement); and not to interfere with the Services (spam is an example).
- Connection request limits: LinkedIn does not publish a hard number in the agreement. Vendor sources commonly cite about 100 requests per week for free accounts, fewer personalised notes on free accounts, and roughly 200 for Premium/Sales Navigator [SECONDARY, unverified; treat as folklore and do not teach as fact].
- What gets accounts restricted: unusual speed, many requests ignored or reported as "I don't know this person", copy-paste notes, logins from many IPs, browser extensions that drive the UI, and scraping profile data [SECONDARY]. LinkedIn restricts, then permanently bans. Litigation exists against scrapers (LinkedIn v. Proxycurl/Nubela 2026 reported, SECONDARY); hiQ v. LinkedIn did not authorise breaching the User Agreement [KNOWLEDGE, correct the vendor claim that the Supreme Court sided with hiQ: it vacated and remanded in 2021 on other grounds].
- "Assisted" vs "bot": a tool that drafts a message or lists prospects while you click Send manually is assisted. A tool or extension that logs in or drives LinkedIn to send requests, visit profiles, or scrape is a bot, and is a breach of 8.2 regardless of speed settings. Vendors who say "safe automation" are selling risk reduction, not compliance. For the course: assisted-only, human sends, small daily numbers.
- Also remember the Spam Act and CAN-SPAM-style duties: ACMA treats social messaging as electronic messages [KNOWLEDGE, verify], so an AU LinkedIn commercial DM still needs the three Spam Act elements.

Must do: send manually, personalise, keep volume modest (tens per day at most), include real identification, stop when asked, use LinkedIn's own tools (Sales Navigator, InMail).
Never: use auto-connect/auto-message extensions, scrape profiles into a CRM with a bot, buy "LinkedIn lists" scraped by others, or run a client's account with a shared login from many locations.

---

## 5. Instagram and Facebook DMs

- Meta's messaging APIs only let a business message someone who messaged or interacted first, inside a 24-hour window (up to 7 days in some Click-to-Message cases) [SECONDARY via multiple vendors; confirm in Meta developer docs]. Cold outreach to arbitrary accounts through the API is not supported.
- Meta Terms of Service and Platform Terms ban automated data collection and unauthorised automation (bots driving the app) [KNOWLEDGE; I did not fetch Meta's terms today].
- Limits: vendor figures (about 200 API DMs/hour, a few dozen manual cold DMs per day before flags) conflict and are unverified [SECONDARY, UNSETTLED]. Meta does not publish a fixed number. Mass identical DMs or many new-account DMs trigger action blocks, then restrictions.
- Spam Act exposure for AU recipients applies to commercial DMs, as above [KNOWLEDGE].

Must do: comment/engage first, DM manually, small numbers, honest identification, stop on reply "no". Use official automation only for people who messaged or commented first.
Never: use third-party DM-blasting bots or cookie-session tools, run the same pitch to dozens of strangers per day, or buy follower/engagement lists.

---

## 6. Data sourcing

### 6A. Australia
- Privacy Act 1988: there is no general "business contact" exception. Personal information includes a sole trader's name, mobile and email. The Act binds most businesses with turnover above $3 million, and many small businesses are exempt under s6D, BUT the exemption does not apply to businesses that trade in personal information (buying or selling lists) or are related to larger bodies [KNOWLEDGE; SECONDARY confirms $3m threshold]. Most course members will be exempt as agencies, while their clients may not be.
- 2024-2025 reforms: Privacy and Other Legislation Amendment Act 2024 commenced 10 Dec 2024; the statutory tort for serious invasions of privacy commenced 10 June 2025 [SECONDARY]. Commentators say small businesses can be defendants under the tort. Small business exemption removal is still only proposed [SECONDARY]. Change flag: more exposure than before.
- APP 7 (direct marketing) turns on reasonable expectation plus easy opt-out for organisations covered [SECONDARY, OAIC page]. Spam Act is the stricter regime for electronic messages.
- Scraping: the Spam Act's address-harvesting provisions apply to bulk-harvested email addresses when used for unsolicited commercial messages [KNOWLEDGE]. Google Maps scraping breaches Google's terms; the Places API is the permitted route (the course already notes this). ABN Lookup data is public and has its own use terms and a bulk data file on data.gov.au [KNOWLEDGE, verify the licence]. Company websites: public, but robots.txt/terms may prohibit scraping, and publication does not equal marketing consent.

### 6B. United States
- Public business data is generally lawful to collect; the issues are website terms (breach of contract claims, CFAA after Van Buren/hiQ is narrower but not zero) and what you do with it [KNOWLEDGE].
- CCPA/CPRA: the B2B and employee exemptions expired 1 Jan 2023 [SECONDARY], so California business contacts are "consumers". But CCPA only applies to businesses above revenue/volume thresholds (about $26m revenue, 100,000+ consumers, or 50% revenue from selling data) [KNOWLEDGE], so small agencies are mostly out of scope; data brokers (Apollo, Lusha) are in scope and California's Delete Act deletion platform for brokers started in 2026 [KNOWLEDGE, verify]. Several other states exempt B2B contacts [KNOWLEDGE].
- Buying enriched mobiles (Apollo, Lusha, etc.): the provider's terms put compliance on you. If you text or robocall a purchased number, you are the sender and TCPA liability is yours. You cannot assume the provider got consent for your messages. Same under AU Spam Act (consent is sender's burden). Provider indemnities, if any, do not stop a regulator or a plaintiff suing you.

### Data: must do
- Prefer official APIs (Places API) and publicly published business details.
- Store source URL, date, and screenshot per lead; run a suppression list.
- Hold only what you need, delete on request.

### Data: never do this
- Never scrape Google Maps pages, LinkedIn or Instagram with bots.
- Never buy mobile numbers and cold text or robocall them.
- Never treat "it is on the internet" as consent.
- Never sell or pass the list on.

---

## 7. AI disclosure

- Australia: no current rule found requiring disclosure that an email, SMS or call was AI-written or AI-voiced. Government AI policy is voluntary; mandatory guardrails have not been legislated [KNOWLEDGE, verify]. Misleading-conduct rules (Australian Consumer Law) still stop you pretending a human relationship exists.
- United States: no federal rule requiring AI-written email or SMS disclosure. For calls: the FCC treated AI voices as "artificial" (Feb 2024) and has floated AI-call disclosure rules in a 2024 notice but I found no adopted rule [SECONDARY]. States: California bot law, Utah, Maine, Washington and Colorado have chatbot or bot disclosure laws of varying scope, mostly aimed at online chat; voice-call reach is unsettled [SECONDARY, UNSETTLED].
- FTC Act: deceptive claims are unlawful. A fake "I saw your work" opener from an AI is a deception risk.
- Course design implication: build "AI assistant" disclosure into voice scripts by default. For email, no disclosure needed, but every factual claim must be true and the sender must be the real business.

---

## Sources

Primary or near-primary
- FTC, CAN-SPAM Act: A Compliance Guide for Business: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- FTC, Complying with the Telemarketing Sales Rule: https://www.ftc.gov/business-guidance/resources/complying-telemarketing-sales-rule
- Google, Email sender guidelines: https://support.google.com/a/answer/81126
- Do Not Call Register (ACMA), about the Register: https://www.donotcall.gov.au/about/about-the-do-not-call-register
- Spam Act 2003 (Cth), Federal Register of Legislation: https://www.legislation.gov.au/C2004A01214/latest/text
- LinkedIn User Agreement s8.2: https://www.linkedin.com/legal/user-agreement
- ACMA SMS Sender ID Register rules for telcos: https://www.acma.gov.au/sms-sender-id-register-rules-telcos
- Telecommunications (SMS Sender ID Register) Industry Standard 2025 explanatory statement: https://www.legislation.gov.au/F2025L01235/asmade/2025-10-08/es/original/word
- ACMA Tabcorp infringement notice (April 2026): https://www.acma.gov.au/sites/default/files/2026-07/Tabcorp%20Holdings%20Limited%20-%20Infringement%20Notice%20-%20Spam%20Act%202003_Redacted.pdf
- ACMA Latitude infringement notice (Jan 2026): https://www.acma.gov.au/sites/default/files/2026-04/Latitude%20-%20Spam%20Infringement%20Notice%20-Redacted.pdf
- FCC, AI-generated voices robocalls ruling: https://www.fcc.gov/document/fcc-makes-ai-generated-voices-robocalls-illegal
- OAIC, Direct marketing: https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/organisations/direct-marketing

Secondary (verify before teaching as fact)
- Latham & Watkins, FCC revamps consent rules (1 Oct 2026 order): https://www.lw.com/en/insights/fcc-revamps-rules-on-consent-to-calls-and-texts-under-the-tcpa
- GM Law, FCC revoke-all waiver to 2027: https://www.gmlaw.com/news/fcc-extends-waiver-on-revocation-of-consent-rules-delaying-broad-applicability-until-2027-2/
- Morrison Foerster, 11th Circuit vacates one-to-one consent: https://mofo.com/resources/insights/250130-eleventh-circuit-vacates-fcc-s-tcpa-one-to-one-consent-rule
- Brightlaw, Do Not Call standards: https://www.brightlaw.com.au/do-not-call-register-telemarketing-standards-explained-for-businesses/
- Holding Redlich, Spam Act compliance: https://www.holdingredlich.com/the-importance-of-compliance-with-the-spam-act
- Ashurst, ACMA spam enforcement: https://www.ashurst.com/en/insights/acma-goes-ham-on-spam-is-your-business-in-breach-of-the-spam-act
- Colemangreig on the Privacy and Other Legislation Amendment Act 2024: https://colemangreig.com.au/insights/blogs/concerns-for-business-under-the-privacy-and-other-legislation-amendment-act-2024
- Troutman, CCPA B2B exemption sunset: https://www.troutman.com/insights/californias-looming-privacy-deadline-for-personnel-and-b2b-data/
- Creatorflow, Instagram DM compliance (vendor): https://creatorflow.so/blog/instagram-dm-compliance-meta-rules/
- Orrick AI law center, California: https://ai-law-center.orrick.com/california/
- JustCall, AI voice disclosure laws (vendor): https://justcall.io/blog/ai-voice-agent-disclosure-laws.html

Not fetched but needed for a final lesson (open items)
- Spam Act Schedule 2 clause 4 exact text and ACMA "Avoid sending spam" page (fetch timed out).
- Telemarketing Industry Standard 2017 text (calling hours).
- 47 CFR 64.1200 current text (eCFR blocked).
- Meta Platform Terms and Instagram Messaging API docs.
- LinkedIn Help Center on connection limits.
- Google Places API terms, ABN Lookup terms.
