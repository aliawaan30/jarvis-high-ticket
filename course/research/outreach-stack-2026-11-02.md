# Outreach stack for student Jarvis: email, SMS, calls, LinkedIn

Date: 2 November 2026. Researched for the high ticket course. Prices in USD unless marked. Everything below was checked against vendor pages or primary sources on this date unless marked "unverified". Prices change; re-check before a lesson ships.

## The answer in one paragraph

Teach ONE email inbox at 30 to 50 cold emails a day as the default, run by Jarvis through Gmail. That is zero extra cost and beginner-safe. Do NOT teach cold SMS as a first touch in any of the three countries. The famous "98% open rate" is an FCC upper-bound estimate for opted-in texts, and cold B2B SMS is a consent problem in AU and the US (and only half-allowed in the UK). Use SMS as the second touch AFTER a reply, a call, or a published mobile number. Calls: the student dials, Jarvis preps and logs. AI outbound calling (Retell batch) is the advanced module, legal to business landlines but a minefield to mobiles. LinkedIn: HeyReach or Dripify (both have an API and an MCP server) at about $79 a month per LinkedIn account, 20 to 25 connection requests a day. The upgrade path is Instantly (API + MCP) with more inboxes when they hit 100+ emails a day.

---

## 1. EMAIL

### 1a. One mailbox: what is actually safe

| Item | Number | Source |
|---|---|---|
| Google Workspace hard cap | 2,000 messages/day per user; 3,000 external recipients/day; 500/day on trial accounts | [Google Workspace sending limits](https://knowledge.workspace.google.com/admin/gmail/gmail-sending-limits-in-google-workspace) |
| Trial limits lift | Only after the domain has paid at least US$100 cumulative; up to 75 days | Same Google page |
| Microsoft 365 hard cap | 10,000 recipients/day, 30 messages/minute, 500 recipients per message | [Microsoft Q&A](https://learn.microsoft.com/en-us/answers/questions/5844111/maximum-emails-sent); [Woodpecker](https://woodpecker.co/blog/cold-email/email-sending-limits/) |
| Safe COLD volume per warmed inbox (vendor consensus, not Google policy) | 20 to 30/day on Workspace; some say up to 50 | [Maildeck Q3 2026](https://maildeck.co/blog/cold-email-sending-limits/); [ScaledMail](https://www.scaledmail.com/blogs/how-many-cold-emails-per-day); [Puzzle Inbox](https://puzzleinbox.com/blog/google-workspace-cold-email-limits-2026/) |
| Warm-up time for a new inbox | Start at 5 to 10/day, ramp over 2 to 4 weeks; most vendors say 4 to 8 weeks before full volume | [LeadHaste](https://leadhaste.com/blog/google-workspace-cold-email-limits-2026); [Outbound System](https://outboundsystem.com/blog/google-workspace-cold-email-limits) |
| Google bulk-sender rules (apply once you send 5,000+/day to Gmail, but treat as baseline) | SPF + DKIM + DMARC, one-click unsubscribe, spam complaints under 0.3% | [LeadHaste deliverability guide](https://leadhaste.com/blog/gmail-email-deliverability-guide) |
| Workspace price | US$7/user/mo annual, US$8.40 monthly. AU: A$9.90/user/mo on annual commitment (A$7.92 promo to 15 Feb 2027) | [Google AU pricing](https://workspace.google.com/intl/en_au/pricing); [Email Vendor Selection](https://www.emailvendorselection.com/google-workspace-pricing/) |

What gets a beginner blocked, in order of how often it happens:
1. Sending cold from a brand-new domain or a trial Workspace with no warm-up. Google locks sending for 24 hours when you hit a cap, and reputation tanks long before the cap.
2. No SPF/DKIM/DMARC. Mail goes to spam, bounces pile up, Google flags the domain.
3. Bounce rate over about 3 to 5% (unverified list). Verify emails before sending.
4. Same template 50 times in a row with links and images. Plain text, short, one link max, personalised first line.
5. Sending from the main business domain. One bad week burns the domain the student's own clients email them on.

Realistic daily cold volume from ONE inbox for a student: 30 to 50 cold emails a day after a two-week ramp, on a secondary domain. That is 150 to 250 new businesses a week. For a local agency selling one service, that is plenty.

What "reply rate" to promise: Instantly's 2026 benchmark (2025 data, billions of emails) is 3.43% average reply, top 10% at 10.7%+ ([Instantly report](https://instantly.ai/blog/ai-sales-agent-benchmarks-2026-the-complete-performance-report/)). Smartlead's 850M-email benchmark counts per contact and gets a 0.74% median ([Smartlead benchmarks](https://www.smartlead.ai/benchmarks)). Apollo calls 3 to 6% healthy ([Apollo](https://www.apollo.io/insights/what-is-a-good-benchmark-for-reply-rates-in-cold-outreach)). Tell students: 1 to 3 replies per 100 emails is normal, 5+ is good. Positive replies are a fraction of that (roughly 1 in 7 replies per one secondary estimate, unverified).

### 1b. Multi-inbox sequencers (2026)

| Tool | Entry price | Public API | MCP server | Agent can create campaigns + add leads via API | Email accounts | Notes |
|---|---|---|---|---|---|---|
| Instantly | Growth $47/mo ($37.60 annual): 5,000 emails/mo, 1,000 contacts. Hypergrowth $97: 125,000 emails, 25,000 contacts | Yes, API v2 (`api.instantly.ai/api/v2`) | Yes, hosted at `mcp.instantly.ai`, exposes the full v2 API (accounts, campaigns, leads, emails/replies, analytics, webhooks) | Yes: create campaigns, bulk import leads, move leads, read and reply to emails | Unlimited on Growth and Hypergrowth | Webhooks are Hypergrowth and up. Whether API is on Growth is contradicted between help center (yes) and pricing page (Hypergrowth only): unverified. Email verification costs credits. | 
| Smartlead | Base $39/mo ($32 annual): 2,000 contacts, 6,000 emails/mo. Pro $94: 30,000 contacts, 90,000 emails | Yes, REST v1 (`server.smartlead.ai/api/v1`), included on paid plans | Yes: Smartlead's own blog lists `@smartlead/mcp-server` with 116+ tools; a LeadMagic partner server also exists. Which is "official" is unclear: unverified | Yes | Unlimited on all plans | Sells inboxes itself: SmartSenders at $4.50/mailbox/mo + $13/domain/yr (Google or Outlook, fresh) or $9/mailbox/mo pre-warmed |
| lemlist | Email $69/mo ($55 annual): 50,000 emails/mo. Multichannel $109/mo ($87 annual) adds LinkedIn + dialer, 5 senders per user | Yes, all plans since July 2026 | Yes, `app.lemlist.com/mcp`, OAuth, all plans | Yes | Unlimited (Email plan); 5 per user (Multichannel) | The only one that does email + LinkedIn + calls in one sequence with an MCP |
| Apollo | Free; Basic ~$49 to $59/user; Pro ~$79 to $99/user (third-party figures, Apollo does not list prices on the page) | Only on Custom/Enterprise plans per pricing page | Yes, `mcp.apollo.io/mcp`, OAuth; can search people, enrich, add contacts to sequences | Via MCP yes; via REST only on Custom | Free plan: Gmail only, 250 sends/day | Best as a B2B list source + MCP, not as the sending engine for a beginner |

Sources: [Instantly pricing](https://instantly.ai/pricing), [Instantly MCP docs](https://developer.instantly.ai/mcp/introduction.md), [Instantly API](https://developer.instantly.ai/), [Smartlead pricing](https://www.smartlead.ai/pricing), [Smartlead MCP blog](https://www.smartlead.ai/blog/what-is-mcp-server), [lemlist pricing](https://www.lemlist.com/pricing), [lemlist pricing changelog](https://pricingsaas.com/companies/lemlist/diffs/2026W31), [lemlist MCP review](https://reply.io/blog/lemlist-mcp/), [Apollo pricing](https://www.apollo.io/pricing), [Apollo MCP docs](https://docs.apollo.io/docs/apollo-mcp), [Apollo MCP review](https://www.cleanlist.ai/blog/2026-10-01-apollo-mcp-server-review).

How many inboxes for 100 to 300 a day (at 25 to 30 cold emails per inbox per day, 2 to 3 inboxes per domain):

| Target per day | Inboxes | Domains | Inbox cost (Workspace at $8.40) | Inbox cost (Smartlead SmartSenders at $4.50) | Domains per year (~$10 to $13 each) |
|---|---|---|---|---|---|
| 100 | 4 | 2 | $34/mo | $18/mo | $20 to $26/yr |
| 200 | 8 | 3 to 4 | $67/mo | $36/mo | $40 to $52/yr |
| 300 | 12 | 4 to 6 | $101/mo | $54/mo | $50 to $78/yr |

Domain prices: Cloudflare .com about $9 to $10.50/yr at cost, Porkbun about $11/yr ([DEV registrar comparison](https://dev.to/devtoolpicks/namecheap-vs-porkbun-vs-cloudflare-registrar-vs-godaddy-for-indie-hackers-in-2026-35cd); [Porkbun .com calculator](https://porkbun.com/about/domain-cost-calculator/com.txt)). Pre-warmed inboxes from third parties run $2.80 to $4.50/inbox/mo ([Prospeo buyer's guide](https://prospeo.io/s/pre-warmed-email-accounts)).

### 1c. Recommendation for the course

Default (Module 4 "Outreach"): ONE Google Workspace inbox on a secondary domain (e.g. `getjoesplumbingsites.com` not `joesplumbingsites.com`), SPF/DKIM/DMARC set in the first lesson, two-week ramp (5, 10, 15, 20, 30), then 30 to 50 cold emails a day. Jarvis writes, sends via the Gmail connector/API, logs to the Prospects table, and schedules day-3 and day-7 follow-ups. Cost: A$9.90 or US$8.40 a month. No sequencer. The student never touches a deliverability dashboard.

Upgrade (when they have 1 client and want 100+ a day): Instantly Hypergrowth ($97/mo, webhooks included so Jarvis gets replies pushed to it) + 4 to 12 inboxes bought through Smartlead SmartSenders or Workspace, 2 to 3 per domain. Jarvis uses the Instantly MCP to create the campaign, push leads from the Prospects table, and read replies. If the student also wants LinkedIn in the same tool, lemlist Multichannel ($109) replaces Instantly + a LinkedIn tool, but it is per user and LinkedIn is capped at 5 senders.

Why not teach multi-inbox from day one: a beginner managing 8 inboxes, 4 domains and warm-up is the exact "quit at friction" trap. One inbox, one domain, 40 a day, every day, for 30 days beats 300 a day for a week.

---

## 2. SMS

### 2a. The numbers, honestly

| Claim | Where it comes from | What it actually says |
|---|---|---|
| SMS 98% open, 45% response | FCC Consumer Advisory Committee working group report, August 2022 | "Open rates COULD REACH 98% and response rates 45%". An upper-bound estimate, not a measured campaign average. [Broadband Breakfast on the FCC CAC report](https://broadbandbreakfast.com/fcc-committee-approves-broader-adoption-of-best-practices-to-block-unwanted-texts/); [Kixie summary](https://www.kixie.com/sales-blog/sms-vs-email-marketing-a-data-driven-study-for-your-sales-strategy/) |
| Email 20% open, 6% response | Attributed to the same FCC report by marketing blogs | Not found in the FCC primary text: unverified. [PitchPrfct](https://www.pitchprfct.com/blog/sms-marketing-statistics/) |
| Gartner "98% / 45%" | Repeated everywhere, usually linking to an archived 2016 Gartner page | Same "as high as" language. No disclosed methodology. SMS has no open tracking; "open" means the notification was seen. [Clickminded](https://www.clickminded.com/sms-marketing-statistics/); [Sakari](https://sakari.io/blog/sms-marketing-statistics-data-backed-insights-for-2025-2026) |
| Cold B2B SMS reply rate | No published benchmark found in any 2025/2026 source | Every "SMS stat" is opted-in consumer marketing. Do not quote a cold SMS reply rate in the course. |

So the honest line for a lesson: "A text gets read. Almost every text gets read within minutes. That does not mean a cold text to a stranger gets a reply, and in most countries you are not allowed to send it anyway."

### 2b. Twilio prices and rules by country

| | Australia | United States | United Kingdom |
|---|---|---|---|
| Outbound SMS per segment | $0.0515 (about A$0.0695 + GST on invoice per a reseller, unverified) | $0.0083 + carrier fee $0.0035 to $0.005 (AT&T/T-Mobile/Verizon) | $0.056 |
| Inbound SMS | $0.0075 | $0.0083 + carrier fee | $0.0075 |
| Number per month | Mobile number $8.25; alphanumeric sender ID free (one-way, no replies) | Local long code $1.15; toll-free $2.15 | Mobile $2.50; local $1.15; alphanumeric free (one-way) |
| Registration | Alphanumeric sender IDs must be on the ACMA SMS Sender ID Register since 1 July 2026 (ABN + ID of the authorised rep, via Twilio). Unregistered branded texts are labelled "Unverified". Numeric numbers unaffected. Twilio AU numbers need KYC (business name, registry proof, address) | A2P 10DLC is mandatory. Brand registration $4.50 one-off (sole prop or low-volume), standard secondary vetting $41.50, campaign vetting $15 one-off, campaign $1.50 to $10/month | No registration regime for numbers. Alphanumeric sender IDs allowed |
| Two-way replies via API | Yes on a mobile number (not on alphanumeric) | Yes on long code | Yes on mobile or local number |
| Agent sends via API | Yes, Messages API, any HTTP client | Yes | Yes |

Sources: [Twilio AU SMS pricing](https://www.twilio.com/en-us/sms/pricing/au), [Twilio US SMS pricing](https://www.twilio.com/en-us/sms/pricing/us), [Twilio UK SMS pricing](https://www.twilio.com/en-us/sms/pricing/gb), [Twilio 10DLC fees](https://support.twilio.com/hc/en-us/articles/1260803965530), [Twilio campaign vetting FAQ](https://support.twilio.com/hc/en-us/articles/11587910480155-A2P-10DLC-Campaign-Vetting-FAQ), [Twilio brand registration doc](https://static0.twilio.com/docs/trust-hub/registrations/a2p-10dlc-brand.md), [business.gov.au on the sender ID register](https://business.gov.au/news/new-rules-for-businesses-sending-text-messages), [Twilio AU sender ID registration](https://support.twilio.com/hc/en-us/articles/46266521342747-Regulatory-information-Your-Sender-ID-registrations-via-Twilio-Australia), [Twilio AU KYC](https://support.twilio.com/hc/en-us/articles/49291010297883-Know-Your-Customer-KYC-in-Australia).

Alternatives: ClickSend, MessageMedia and Sinch are the usual AU names and all expose an API; Texto claims A$0.03/SMS ([Texto vs Twilio](https://texto.com.au/compare/twilio), vendor claim, unverified). Twilio is the right teaching default because it covers all three countries, the docs are the best, and Blake already runs it for the Retell bridge.

The 10DLC trap for cold texting in the US: campaign registration requires you to describe an opt-in flow and keep consent records per recipient. Campaigns get rejected for pre-ticked boxes, missing consent language, or "terms of service" consent ([Twilio error 30925](https://www.twilio.com/docs/api/errors/30925), [30924](https://www.twilio.com/docs/api/errors/30924), [30913](https://static1.twilio.com/docs/api/errors/30913)). A student cannot honestly register a "cold outreach to strangers" campaign. Unregistered traffic is surcharged and filtered.

### 2c. Is cold B2B SMS legal? Plain English

| Country | Law | Cold text to a business mobile with no prior contact | Practical rule for students |
|---|---|---|---|
| Australia | Spam Act 2003 (ACMA enforces). No B2B carve-out. Consent must be express or inferred. Inferred consent exists where the number is conspicuously published (e.g. on their website or Google listing), the message relates to their role or business, and there is no "no unsolicited messages" note. Sender must be identified and there must be a working unsubscribe. Asking for consent by message is itself a marketing message. | Grey. A mobile number published on a tradie's own website or Google Business Profile arguably gives inferred consent for a message about their business. ACMA has fined on this. Burden of proof is on the sender. | Only text a number the business itself publishes as its contact number, about their business, with your name + business and "reply STOP". Never text a number you scraped from a directory or guessed. Prefer: text AFTER a call or email reply. Sources: [Sinch AU guide](https://sinch.com/engage/resources/sms-compliance/sms-marketing-laws-australia/), [Corrs on ACMA enforcement](https://www.corrs.com.au/insights/acma-spam-act-enforcement-and-the-implications-for-business), [Spam Act text (Sch 2 item 4, ss16-18)](https://www.legislation.gov.au/C2004A01214/latest/text). ACMA's own consent page timed out on fetch; verify at acma.gov.au before publishing. |
| United States | TCPA (federal) + state laws (Florida, Oklahoma, Washington and others). TCPA has no B2B exemption for texts to cell phones: a business-use cell is still a cell. Prior express consent needed for autodialed/texted marketing; $500 to $1,500 per message statutory damages. FCC's one-to-one consent rule was vacated in Jan 2025. Feb 2026 *Sovereign Pest Control* decision may have loosened "written" consent to any express consent: unverified. | No. Texting a stranger's mobile for marketing is the textbook TCPA claim, and 10DLC will not let you register the campaign. | Do not cold text in the US. SMS only after they reply by email or ask on a call ("can I text you the link?"), log the consent in the Prospects table, and always include STOP. Sources: [ActiveProspect](https://activeprospect.com/blog/tcpa-text-messages/), [IDT Express](https://www.idtexpress.com/blog/tcpa-compliance-for-sms-in-2026-the-complete-guide-for-us-businesses/), [MessageIQ state laws](https://messageiq.io/blogs/sms-marketing-laws/), [TCPAWorld on business cells](https://tcpaworld.com/2019/11/14/refresher-on-tcpa-liability-for-calls-to-cell-phones-1-the-dncr-provision-only-prohibits-calls-to-residential-lines-but-2-using-an-atds-without-prior-consent-is-prohibited-to-cell-phones/). |
| United Kingdom | PECR + UK GDPR. ICO: the electronic-mail consent rule "does not apply to corporate subscribers", so you can text a limited company, LLP or Scottish partnership without consent. Sole traders and ordinary partnerships are individuals: consent or soft opt-in required. Every text must identify you and carry an opt-out. Since 5 Feb 2026 (Data (Use and Access) Act commencement) PECR fines go up to £17.5m or 4% of turnover. | Yes for a Ltd company's number. No for a sole trader (which is most tradies). | Text only when Companies House shows a Ltd/LLP, or after the person has replied. Keep a do-not-text list. Sources: [ICO B2B marketing](https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/), [Telerivet on PECR + DUAA](https://www.telerivet.com/blog/uk-sms-compliance-pecr-gdpr-duaa), [ICO DUAA commencement statement](https://www.wired-gov.net/wg/news.nsf/articles/Statement+on+the+commencement+of+the+Data+Use+and+Access+Act+DUAA+06022026102000). |

One rule for the course, all countries: SMS is a follow-up channel, never a first touch. Jarvis sends a text only when one of three things is true: (1) the prospect replied to an email, (2) the prospect was spoken to on a call and said text is fine, (3) AU only: the mobile is the published contact number on their own site or Google listing and the text is about their business. Every text: name, business, one line, "reply STOP to opt out". This is simple, defensible, and it still gets students the "SMS gets read in 3 minutes" advantage where it matters, which is on warm leads.

---

## 3. CALLS

### 3a. AI calling platforms (outbound)

| Platform | Per minute | Fixed costs | Outbound batch | API | Notes |
|---|---|---|---|---|---|
| Retell AI | Voice engine $0.055 + telephony $0.015 + TTS $0.015 (Retell/Cartesia voices) + LLM $0.0032 to $0.128 depending on model. Realistic all-in about $0.09 to $0.15/min | Phone number $2/mo; 20 concurrent calls free; batch +$0.005/dial; $10 free credit | Yes: Create Batch Call API with CSV-style task list, call_time_window (hours/days), schedule or send now | Yes | Blake already uses it; MCP exists. Returns batch_call_id; poll List Calls for transcripts. Scheduled batches can't be edited once "Planned" (community report). |
| Bland | Start $0.14/min, Build $0.12/min + $299/mo. Includes LLM/STT/TTS | Start plan: 10 concurrent, 100 calls/day cap, inbound number included | `/batches` endpoint (third-party listing, unverified) | Yes | Simplest bundle. Daily cap of 100 on free tier is fine for a student. |
| Vapi | $0.05/min platform + pass-through (Deepgram ~$0.01, LLM $0.008 to $0.045, ElevenLabs $0.015 to $0.024, Twilio outbound $0.014). Vapi's own example: $82 to $129 per 1,000 minutes | 4 concurrent on free; $10/line/mo extra; $5 free credit | Yes: Outbound Campaigns with CSV upload and dynamic variables; Vapi free numbers cannot run campaigns (use Twilio) | Yes | Most developer-ish. |

Sources: [Retell pricing](https://www.retellai.com/pricing), [Retell batch call API](https://docs.retellai.com/api-references/create-batch-call), [Retell batch guide](https://docs.retellai.com/deploy/make-batch-call), [Bland pricing](https://www.bland.ai/pricing), [Vapi pricing](https://vapi.ai/pricing), [Vapi outbound campaigns](https://docs.vapi.ai/outbound-campaigns/overview), [Stackbinary comparison](https://stackbinary.io/insights/voice-ai-pricing-per-minute-2026).

Cost reality for a student: 100 outbound dials a day, 30% answered, 2 minute average on answered, 20 seconds on unanswered: roughly 60 + 23 = 83 minutes/day, about $8 to $12/day on Retell, $170 to $250/month. That is more than their whole email + SMS + LinkedIn bill. AI calling is not the cheap channel.

### 3b. Power dialers (student dials, Jarvis preps)

| Tool | Price | API | Notes |
|---|---|---|---|
| GoHighLevel native dialer | Included in $97/$297 plans + LC Phone usage | Native dialer is sequential (one at a time), workflow-driven; no documented API for parallel dialing (unverified) | Blake has GHL. Fine for 50 to 60 dials/day. |
| JustCall | $29 Team / $49 Pro / $89 Pro Plus per user/mo annual, 2-seat minimum; power dialer from Pro | Yes | |
| Kixie | ~$35 to $65/user/mo (Dupple) or $75 to $185 (Prospeo); undisclosed on Kixie's site | Yes | Multi-line up to 10. |
| PhoneBurner | $140 to $199/user/mo | Yes, Professional tier and up | Expensive for a beginner. |

Sources: [Aloware on GHL dialer](https://aloware.com/blog/gohighlevel-power-dialer), [JustCall power dialer cost](https://justcall.io/blog/how-much-does-power-dialer-cost.html), [Dupple Kixie pricing](https://dupple.com/pricing/kixie), [LeadHaste PhoneBurner](https://leadhaste.com/blog/phoneburner-pricing).

### 3c. Legal, plain English (calls)

- Australia: business numbers cannot go on the Do Not Call Register, so a human or AI call to a business number is allowed if the Telemarketing Industry Standard is followed (calling hours: weekdays 9am to 8pm, Saturday 9am to 5pm, none Sunday or public holidays; identify yourself and purpose; end the call if asked). No ACMA rule yet requiring AI disclosure on phone calls (vendor blogs claim otherwise; none point to a rule). Sources: [donotcall.gov.au](https://www.donotcall.gov.au/about), [Brightlaw on the standard](https://www.brightlaw.com.au/do-not-call-register-telemarketing-standards-explained-for-businesses/), [Sprintlaw](https://sprintlaw.com.au/articles/do-not-call-register-australia-businesses-need-to-know/). Hours figures from secondary sources: verify against the Standard.
- United States: FCC's February 2024 declaratory ruling says an AI-generated voice is an "artificial or prerecorded voice" under the TCPA. 47 USC 227(b)(1)(A)(iii) bans artificial-voice calls to ANY cell phone without prior express consent, business-use or not. 227(b)(1)(B) covers residential landlines. Business landlines are not named in either, so an AI call to a business landline appears outside the 227(b) ban (state laws and caller-ID/identification rules still apply). Human cold calls to business numbers are fine. Sources: [Wiley on the FCC ruling](https://wiley.law/alert-FCC-Extends-Regulatory-Reach-Over-AI-Announces-TCPA-Restrictions-Cover-AI-Generated-Voices-in-Outbound-Calls), [Hunton](https://www.hunton.com/privacy-and-cybersecurity-law-blog/fcc-issues-declaratory-ruling-that-tcpa-applies-to-ai-generated-voice-calls), [NatLawReview refresher](https://natlawreview.com/article/refresher-tcpa-liability-calls-to-cell-phones-1-dncr-provision-only-prohibits-calls). Business-landline reading is my statutory reading, not a lawyer's: mark "get counsel" in the lesson.
- United Kingdom: live B2B calls allowed without consent if you screen against the Corporate TPS (Reg 21). Automated calling systems need prior consent (Reg 19); whether an AI voice agent counts as "automated" is unsettled (DMA, June 2026). Fines up to £17.5m since Feb 2026. Sources: [DMA on automated outbound](https://www.dma.org.uk/about/articles/automated-outbound-contact-and-the-collapse-of-the-human-review), [Prospeo PECR cold calling](https://prospeo.io/s/pecr-cold-calling-rules), [Sprintlaw telephone marketing](https://sprintlaw.co.uk/articles/telephone-marketing-rules-staying-pecrcompliant/).

### 3d. Recommendation

Default: the STUDENT calls. Jarvis builds the call list from the Prospects table (people who opened or replied, plus "closes early / no website" gap hits), writes a 5-line brief per prospect (business, gap spotted, opener, likely objection, next step), and logs the outcome from a one-line debrief ("spoke to Dave, send proposal Thursday"). 20 dials a day, 4 days a week. Zero cost beyond their phone. This is what gets a first client.

Advanced (optional lesson, after first client): Retell batch calling to BUSINESS LANDLINES ONLY, AU and US, during the AU/US standard hours, with the agent saying it is an AI assistant for [student's business] in the first sentence, tier "take details and book a callback". Jarvis uploads the batch via the Retell API, reads transcripts back, writes outcomes to Prospects. Skip the UK for AI outbound. Budget line: $0.10 to $0.15/min.

---

## 4. LINKEDIN

LinkedIn's limits are not published. Community consensus for 2026: about 100 connection requests per rolling 7 days (200 to 250 for strong accounts/Sales Navigator), 1,500 pending invites max, and the limit shrinks when acceptance rate is low or people click "I don't know this person" ([Overloop](https://overloop.com/blog/linkedin-limits), [Join Valley](https://www.joinvalley.co/blog/linkedin-invitation-limit-in-2026-weekly-limits-more), [Salesforge](https://www.salesforge.ai/blog/linkedin-connection-request-limit)). Everyone agrees cloud tools with a dedicated IP are safer than Chrome extensions and desktop apps, but the "60% higher ban risk" number has no primary source ([Zeliq](https://www.zeliq.com/blog/linkedin-automation-2026), [SyncGTM](https://syncgtm.com/blog/best-linkedin-outreach-automation-tools)). All automation breaches LinkedIn's User Agreement; the risk is a restriction, not a lawsuit.

| Tool | Type | API | MCP | Price | Vendor's own daily limits | Ban risk (2026 reputation) | Notes |
|---|---|---|---|---|---|---|---|
| HeyReach | Cloud, dedicated proxy | Yes, REST, X-API-KEY, 300 req/min, on Growth | Yes, on Growth | $79/sender/mo ($64 annual). Agency $999/mo for 25 senders | Up to 40 connection requests/day, default 25; weekly cap too. Messages: no published figure | Low to medium; HeyReach's own help centre says it keeps within limits. One "HeyReach ban" article refers to LinkedIn restricting accounts, not the tool | Native Instantly + Smartlead integrations. Best "agent-first" LinkedIn tool. [Pricing](https://www.heyreach.io/pricing), [limits help](https://help.heyreach.io/en/articles/15128619-how-do-connection-request-limits-work-in-heyreach), [API review](https://www.swarmhit.com/blog/heyreach-api) |
| Dripify | Cloud | Yes, Open API on Pro | Yes, MCP server on Pro | Pro $79/user/mo ($59 annual); Advanced $99 ($79 annual) | 75 connection requests/day, 100+ messages/day, 30 InMails (vendor caps; too high, set lower) | Medium | Cheapest tool with both API and MCP. [Pricing](https://dripify.com/pricing/) |
| Unipile | API provider (you build the sending logic) | Yes, full LinkedIn + email + WhatsApp messaging API | Yes, `developer.unipile.com/mcp` (built for coding agents) | €49/$55 per month for up to 10 connected accounts, then $5.50/account. 7-day trial | Documents LinkedIn's ceilings as 80 to 100 invites/day, ~200/week, 100 to 150 messages/day; applies a lower default you can change | Medium; LinkedIn and WhatsApp are reverse-engineered | No campaigns or sequences: Jarvis would run the sequence logic itself. Most powerful, least beginner-friendly. [Pricing](https://www.unipile.com/pricing/), [provider limits](https://developer.unipile.com/docs/provider-limits-and-restrictions) |
| lemlist | Cloud, multichannel | Yes, all plans | Yes, all plans | Multichannel $109/user/mo ($87 annual); LinkedIn needs Multichannel | Recommended defaults: 20 invites, 30 profile visits, 30 messages/day; warns above that; invite ramp-up feature | Low to medium | One tool for email + LinkedIn + calls. [Pricing](https://www.lemlist.com/pricing), [lemlist limits](https://help.lemlist.com/en/articles/7210709-set-account-limits) |
| Expandi | Cloud, dedicated country IP | Partial: per-campaign webhook URL to add leads + event webhooks; a `api.expandi.io/api/lead` Bearer endpoint is reported by one blog (unverified); no public API docs found | No | $99/account/mo ($79 annual) | User-set; markets "300+ connection requests weekly" (ignore that) | Medium | [Pricing](https://www.expandi.io/pricing/), [Cargo integration doc](https://docs.getcargo.io/integration/expandi) |
| La Growth Machine | Cloud, multichannel | Yes, on Pro (Zapier/Make/Clay/API) | No | Basic €60/identity (LinkedIn + email); Pro €120 adds calls | Not published on pricing page | Medium | [Pricing](https://lagrowthmachine.com/pricing/) |
| Waalaxy | Chrome extension | Yes, on Advanced (Make/Zapier/n8n) | No | Pro €19, Advanced €49, Business €69 per user/mo; 300 invites/mo on Pro, 800 on Advanced | 800 invites/month = ~27/day | Higher (extension) | Cheapest with an API. [Pricing](https://www.waalaxy.com/pricing) |
| Linked Helper | Desktop app (local or their cloud) | No public API; incoming/outgoing webhooks on Cloud; Zapier/Make/n8n | No | $15/mo list (from $8.25 local, $16.50 cloud with term discounts); 14-day trial | Standard: 20/day on advanced actions; "smart daily limits" on invites, number not stated | Highest (ranked most detectable in 2026 roundups, anecdotal) | [Pricing](https://www.linkedhelper.com/pricing) |

Daily plan to teach regardless of tool: 15 to 20 connection requests a day (about 100/week), 20 to 30 messages a day to first-degree connections, no InMail unless Sales Navigator, no weekends, ramp from 5/day over two weeks. These are below every vendor's cap and inside the community consensus.

---

## 5. ONE SYSTEM: what Jarvis runs

### The week for one lead (three touches across channels)

| Day | Channel | Who does it | Rule |
|---|---|---|---|
| Mon | Email 1 (gap-based, 4 lines) | Jarvis, via Gmail or Instantly | Always. |
| Tue | LinkedIn connection request, no note or one line | Jarvis via HeyReach/Dripify API; only if the owner has a profile (B2B lane) | Skip for sole tradies with no LinkedIn. |
| Thu | Email 2 (reply-to-thread, one new fact) | Jarvis | Always. |
| Fri | Call | Student dials from Jarvis's brief; AI batch only for landlines in the advanced lesson | Only if phone on Places listing. |
| Day 7 | SMS | Jarvis via Twilio, only if: replied by email, or said yes on the call, or (AU) mobile is their published contact number | "Hi Dave, Blake from X, we spoke Fri, link to the mockup: ... Reply STOP to opt out." |
| Day 10 | LinkedIn message (if connected) or Email 3 break-up | Jarvis | Last touch. Mark cold at day 14. |

Jarvis's Prospects table carries per lead: channels allowed (email / linkedin / phone / sms_consent + why), last touch, next touch date, status. Every skill checks those columns before sending. That is the whole "unison" mechanism: one table, one next-action per lead, one daily run.

### List source

Google Places API (New) Text Search. Phone and website come back only on the Enterprise SKU: $35 per 1,000 requests after a small free monthly allowance (1,000 per a third party, unverified), within the $300 / 90-day trial credit students already set up in SETUP ([Google pricing](https://developers.google.com/maps/billing-and-pricing/pricing), [Open Places API breakdown](https://openplacesapi.com/blog/google-places-api-pricing)). 300 leads a week = about $10/month after the credit. For B2B lanes: Apollo free tier + Apollo MCP for search/enrich (credits).

### Cheapest version (month 1 to 3)

| Piece | Tool | Monthly |
|---|---|---|
| List | Google Places (trial credit) | $0 to $10 |
| Email | 1 Google Workspace inbox on a secondary domain, Jarvis sends via Gmail | $8.40 (A$9.90) + $1/mo domain |
| SMS | Twilio: 1 mobile number (AU $8.25 / US $1.15 + 10DLC $1.50 campaign / UK $2.50) + ~100 texts | $5 to $15 |
| Calls | Student's own phone, Jarvis briefs + logs | $0 |
| LinkedIn | Manual: Jarvis writes the note, student sends 15 requests/day from the brief | $0 |
| Total | | about $15 to $35/month |

Volume: 30 to 50 emails/day, 15 LinkedIn requests/day, 20 calls/day, 5 to 10 warm texts/day. About 150 to 250 new businesses a week touched 3 times. That lands a first client for a local service.

### Scaled version (first client landed, wants 100 to 300 emails a day)

| Piece | Tool | Monthly |
|---|---|---|
| List | Places Enterprise beyond credit + Apollo Basic for B2B | $10 to $60 |
| Email | Instantly Hypergrowth (API + MCP + webhooks) + 8 to 12 inboxes (Smartlead SmartSenders $4.50 each or Workspace $8.40 each) + 4 domains | $97 + $36 to $101 + $4 |
| SMS | Twilio, 2 numbers, ~500 texts | $20 to $45 |
| Calls | Retell batch to business landlines, ~1,500 min/mo, 1 number | $150 to $225 |
| LinkedIn | HeyReach Growth 1 sender (API + MCP) or Dripify Pro | $79 ($59 to $64 annual) |
| Total | | about $400 to $600/month, or $250 to $350 without AI calling |

Alternative single-vendor scaled stack: lemlist Multichannel ($109) covers email + LinkedIn + dialer with one MCP, plus Twilio for SMS and Retell for AI calls. Fewer keys for Jarvis to hold, but per-user pricing and a 5-sender LinkedIn cap.

### What to tell Blake straight

1. Multi-account mass outreach is not a beginner move and it is not where the first client comes from. The first client comes from 40 emails a day, every day, plus 20 calls, for 30 days. Teach that.
2. "SMS has a 98% open rate" is an FCC "could reach" figure for opted-in texts. Keep SMS as the warm-lead channel. It still wins there: a text after a call gets the proposal opened.
3. The agent-ready tools are: Instantly (MCP), Smartlead (MCP), lemlist (MCP), Apollo (MCP), HeyReach (MCP), Dripify (MCP), Unipile (MCP), Twilio (plain API), Retell (API + MCP). Base44 Jarvis can hit all of them over HTTP. Skills = one markdown file per channel + one "next touch" skill that reads the Prospects table.
4. Open question only Blake can answer: does the course sell to AU-first students (Places + Twilio AU + inferred-consent SMS all work) or US-first (SMS is dead as a first touch, AI calls landline-only)? The default lesson should be written for AU and a US/UK box-out added.

## Unverified list (re-check before a lesson ships)

- Instantly API on Growth vs Hypergrowth (help centre says Growth; pricing page ticks Hypergrowth only).
- Which Smartlead MCP package is official (`@smartlead/mcp-server` per Smartlead blog vs partner servers).
- Twilio AU landed AUD rate per SMS (reseller claims A$0.0695 + GST).
- Expandi's `api.expandi.io/api/lead` endpoint (single blog source).
- Bland `/batches` endpoint (aggregator listing, not Bland docs).
- AU telemarketing hours (secondary sources; confirm in the Telemarketing and Research Calls Industry Standard 2017).
- US: AI calls to business landlines falling outside 227(b) (statutory reading, not legal advice). *Sovereign Pest Control* Feb 2026 "written consent" change.
- Email "20% open / 6% response" attributed to the FCC report.
- Google Places Enterprise free monthly allowance (1,000 per third party).
- ACMA consent guidance page could not be fetched (timeouts); Spam Act Sch 2 item 4 is the primary source and should be quoted directly.
