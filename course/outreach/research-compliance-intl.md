# Outreach compliance research: UK, Canada, New Zealand and EU cold outreach by small AI agencies

Prepared 29 Oct 2026. General information for course design only. This is not legal advice. Members should get advice from a lawyer in the recipient's country before running volume. Companion to research-compliance.md (AU and US).

## How to read the confidence tags

- [PRIMARY] I read the regulator, statute or official page in this pass (or a regulator-published decision quoted back to me).
- [SECONDARY] Law-firm, vendor or search-extract summary only. Verify before it becomes a hard number in a lesson.
- [UNSETTLED] Sources conflict, or the law is untested or in flux.
- [KNOWLEDGE] Established law I know well but did not re-fetch today. Verify the cite.

Research limits, stated plainly: the CRTC, DIA (NZ), legislation.govt.nz and Irish DPC pages returned 403 or 404 to my fetcher. Only the ICO (UK), the German UWG English text, and the NZ Marketing Association FAQ were read directly. Canada, NZ, Netherlands and Ireland claims therefore lean on search extracts of the regulator or statute plus law-firm summaries and are tagged accordingly. Many results were vendor blogs; anything resting only on those is SECONDARY.

---

## 0. The rules most likely to change the system design

1. One "country" field on every lead drives the whole send path. The same B2B prospect is opt-out in the UK (companies) and Netherlands/Ireland (business addresses), opt-in-ish (conspicuous publication) in Canada and NZ, and flatly opt-in in Germany. Build the compliance gate per recipient country, not per member country.
2. Entity type decides the rules. UK sole traders and some partnerships are treated as individuals for PECR (need consent), limited companies are not. GDPR treats sole traders as natural persons everywhere in the EU. So the lead record needs "company type" (Ltd/LLP vs sole trader/partnership), not just "business".
3. Germany: no cold email at all without prior express consent (UWG s7). Block German cold email in the sender. Cold calls to businesses need only "presumed consent", but it is narrow and competitors can send cease-and-desist letters.
4. Canada and NZ: cold email depends on conspicuous publication + role relevance + no "no spam" statement, and the sender carries the burden of proof. Store URL, date, screenshot per lead. Canada penalties are up to CAD 10m per violation for a business.
5. Calls: UK needs TPS and CTPS screening before every live B2B call (sole traders are on TPS). Canada has no DNCL duty for business numbers but CRTC hours and an internal DNC list still apply. Germany, UK and the US treat AI/recorded-voice calls as needing prior consent. Do not teach AI cold calling outside AU/NZ-style grey areas without per-country consent.
6. Every message needs a real sender identity, a postal or contact address, and a working unsubscribe, in every jurisdiction. One suppression list across all countries.
7. UK penalties changed: PECR maximum fine rose from GBP 500,000 to GBP 17.5m or 4% of worldwide turnover for conduct from 5 Feb 2026 [SECONDARY, see 1.6].

---

## 1. United Kingdom (PECR + UK GDPR)

### 1.1 Cold email
- PECR regulation 22 covers email and SMS marketing. Regulator guidance: companies, Scottish partnerships, LLPs and government bodies ("corporate subscribers") can be emailed, with good practice being to keep a do-not-email list and screen against it [PRIMARY, ICO email marketing guide].
- Sole traders and some partnerships (English/Welsh/NI ordinary partnerships) are treated as individuals, so you need their specific consent or the soft opt-in [PRIMARY, ICO].
- Soft opt-in covers only existing customers who bought or negotiated to buy a similar product from you, with an opt-out at collection and in every message. It does not cover prospects or bought lists [PRIMARY, ICO].
- Sender identity must not be disguised, and a valid contact address must be given. An opt-out route must work, and you must act promptly [PRIMARY, ICO].
- Practical reading for the course: a cold email to info@acmeplumbing.co.uk (a Ltd company) is lawful without prior consent if it complies with identity and opt-out. The same email to a named sole trader (john@johnsmithplumbing.co.uk, "trading as") needs consent. In practice you cannot reliably tell sole traders from companies, so check Companies House and treat anything unverifiable, or any address containing a personal name at a non-company business, as an individual [KNOWLEDGE for the Companies House workflow].
- UK GDPR still applies to personal data in the address (john.smith@...), see 1.5.

### 1.2 Cold calls (live, to a business number)
- Live calls to businesses follow the same rules as to individuals: you can call a business number not on the TPS or CTPS that has not previously objected, and you are not marketing claims management [PRIMARY, ICO telephone marketing guide].
- CTPS covers companies, LLPs, Scottish partnerships and government bodies. Sole traders and some partnerships register with the TPS. Screen against both registers plus your own do-not-call list [PRIMARY, ICO].
- You must say who is calling, allow your number (or an alternative contact number) to be displayed, and give an address or freephone number on request [PRIMARY, ICO].
- Calling a sole trader's mobile that you took from a directory or enrichment tool needs a TPS check, because it can be an individual's number [PRIMARY on TPS rule; KNOWLEDGE on the mobile inference].

### 1.3 SMS
- SMS is "electronic mail" under PECR regulation 22. Same rules as email: individuals (including sole traders) need consent or soft opt-in. Corporate subscribers are not protected by the consent rule, but a mobile number published for a person is a poor basis to infer "corporate". The regulator-fined 2026 cases involved SMS volume, e.g. KRA Consultancy Ltd, GBP 300,000, 5.5m texts, 60,000+ complaints [SECONDARY, Freevacy summarising an ICO notice].
- Course rule: no cold SMS in the UK. Text only after a conversation.

### 1.4 AI voice and automated calls
- Automated marketing calls (recorded message) need specific consent covering that call type. General marketing consent or consent for live calls is not enough. Each call must include your name and a contact address or freephone number, display a number, and stop if consent is withdrawn [PRIMARY, ICO].
- Whether a conversational AI voice agent counts as "automated" under PECR is not settled in an ICO decision I could find [UNSETTLED]. Treat an AI voice cold call as an automated call: prior specific consent first. Even if a regulator accepted "it is live in effect", misleading the recipient into thinking it is a human is a consumer/business protection risk [KNOWLEDGE].

### 1.5 Data sourcing and enrichment
- UK GDPR Article 6(1)(f) legitimate interests is the usual basis for B2B prospecting data. You need a three-part test (purpose, necessity, balancing) written down, a privacy notice (Article 14 applies when you did not collect the data from the person, with notice within one month or at first contact), and a working right to object to direct marketing (absolute, Article 21) [KNOWLEDGE; ICO direct marketing guidance not re-fetched].
- Sole trader and named-employee details are personal data. Generic role addresses (info@) at a company are generally not.
- The Data (Use and Access) Act 2025 explicitly recognises direct marketing as a possible legitimate interest and creates "recognised legitimate interests" for some other purposes. It does not remove the balancing test for B2B marketing [SECONDARY, law-firm commentary; verify exact section].
- Buying enriched contacts: you remain the controller for what you do. Check the broker's source and lawful basis. PECR consent for the channel is separate and not solved by the broker's warranty [KNOWLEDGE].

### 1.6 2025 and 2026 changes
- Data (Use and Access) Act 2025: PECR fines brought into line with UK GDPR: up to GBP 17.5m or 4% of worldwide annual turnover, whichever is higher, from conduct on or after 5 Feb 2026 (Commencement No. 6 Regulations 2026, SI 2026/82) [SECONDARY: law-firm and consultancy commentary agree; I did not read the SI text. One ICO blog dates "commencement" to 19 June 2026, which is probably a different provision (complaints-handling), UNSETTLED on that point].
- Appeal route for PECR penalties now follows the Data Protection Act 2018 route [SECONDARY].
- PECR enforcement is active: 2026 monetary penalties include TMAC Ltd GBP 100,000 (Feb), Energy Prices Direct GBP 160,000 (May), KRA Consultancy GBP 300,000 (June), Jacksons Marketing GBP 130,000 (TPS calls, July), Elderly Aids Ltd GBP 190,000 (Aug, 758,053 calls) [SECONDARY, Freevacy plus ICO enforcement URLs].
- Other DUAA changes (cookie exemptions, charity soft opt-in) are not relevant to B2B outbound [SECONDARY].

### UK: what the member must do
- Verify entity type per lead. Limited company/LLP: email and live call allowed with compliance. Sole trader/ordinary partnership: treat as consumer, consent only.
- Screen every call list against TPS and CTPS plus your own DNC list before each campaign.
- Identify yourself by name and company, give a contact address, include a working unsubscribe in every email.
- Record the legitimate-interest assessment and send the Article 14 notice (first email can carry it).
- Honour objections immediately and keep a suppression list.

### UK: never do this
- Never email a named sole trader or ordinary partnership cold.
- Never call a TPS/CTPS number.
- Never run an AI voice/recorded call without prior specific consent.
- Never send cold SMS.
- Never conceal your identity, spoof numbers or hide behind a "client's" name.

---

## 2. Canada (CASL + CRTC rules + PIPEDA)

### 2.1 Cold email
- CASL applies to any commercial electronic message (CEM) sent to or from Canada. Business-to-business is not exempt. Implied consent for a cold email is possible only through conspicuous publication: (1) the recipient conspicuously published the address (or caused it to be published), (2) the publication has no statement declining unsolicited CEMs, and (3) the message is relevant to the recipient's business, role, functions or duties [PRIMARY via the Federal Court of Appeal summary of s 10(9)(b) in secondary commentary; statute text not read directly, so SECONDARY on the wording].
- The CRTC held that mere public availability is not enough, and the Federal Court of Appeal upheld the CRTC's rejection of CompuFinder's implied-consent argument [SECONDARY, law-firm summaries of CRTC 2015-109 and the FCA decision].
- Burden of proof sits on the sender [SECONDARY, consistent across sources].
- Other implied-consent routes: an existing business relationship (purchase within the prior 2 years, or inquiry within 6 months) and existing non-business relationships [KNOWLEDGE].
- Every CEM must identify the sender, include contact information, and carry a working unsubscribe honoured within 10 business days. The conspicuous-publication exception does not remove these duties [SECONDARY].
- Sole traders: CASL speaks of "a person", so the sole trader rule is the same as for a company, but PIPEDA applies more strongly to personal info (see 2.5). No separate corporate carve-out [KNOWLEDGE].
- Penalties: administrative monetary penalty of up to CAD 10m per violation for a business and CAD 1m for an individual [PRIMARY, CRTC FAQ as quoted in search extract; page itself returned 403]. Real penalties were smaller: CompuFinder reduced to CAD 200,000 (from 1.1m notice); Blackstone Learning CAD 50,000 (from 640,000 notice) [SECONDARY]. The private right of action in CASL has been suspended indefinitely since 2017 [KNOWLEDGE, verify].

### 2.2 Cold calls
- The National Do Not Call List (DNCL) rules do not apply to calls to businesses, and business numbers are not to be registered. A personal number also used for business counts as a business number [SECONDARY, CRTC-derived summary; CRTC page 403].
- The CRTC Telemarketing Rules still apply to exempt calls: identification, internal DNC list, honouring requests [SECONDARY].
- Hours: weekdays 9:00 to 21:30, weekends 10:00 to 18:00, recipient's local time; stricter provincial hours may apply [PRIMARY via CRTC rules text as quoted in search extract].
- Registration with the DNCL operator even when making only exempt B2B calls: one vendor source says required, CRTC page unclear [UNSETTLED]. Confirm with the CRTC before a Canadian dialling campaign.
- A CRTC review of the Unsolicited Telecommunications Rules was reported for 2026 [SECONDARY, single mention].

### 2.3 SMS
- A text promoting a service is a CEM. The same rules apply, plus the Canadian carrier rules. Mobile numbers are rarely "conspicuously published", so implied consent is hard [KNOWLEDGE].
- Course rule: no cold SMS in Canada.

### 2.4 AI voice and automated calls
- The CRTC ADAD (automatic dialling and announcing device) rules restrict automated solicitation calls and require an identification message and callback number [KNOWLEDGE, rules text not read]. Whether the ADAD rules apply to a conversational AI agent, or to B2B calls, is [UNSETTLED]. Treat AI cold calling in Canada as not to be taught without legal advice.

### 2.5 Data sourcing
- PIPEDA excludes "business contact information" collected, used or disclosed solely to communicate with a person about their employment or profession [PRIMARY wording via OPC guide extract]. This does not decide whether you may send the CEM; CASL does. The Privacy Commissioner applied PIPEDA to CompuFinder because many of the emails were not relevant to the recipients' work [SECONDARY].
- PIPEDA restricts address harvesting; businesses must ensure consent exists for electronic addresses even when bought from a third party [PRIMARY wording via OPC e-marketing page extract].
- Quebec Law 25 and provincial laws add obligations for Quebec contacts (French-language, privacy notices) [KNOWLEDGE].

### 2.6 2025 and 2026 changes
- No amendment to CASL penalties or the conspicuous-publication test found. CRTC enforcement continues. CRTC review of unsolicited telecom rules reported [SECONDARY].

### Canada: what the member must do
- Cold email only where the three conspicuous-publication conditions are met; log URL, date, screenshot.
- Include sender name, address, working unsubscribe honoured in 10 business days.
- Call business lines only within 9:00 to 21:30 weekdays and 10:00 to 18:00 weekends, identify yourself, maintain an internal DNC list.
- Confirm DNCL operator registration with the CRTC before dialling.

### Canada: never do this
- Never email an address because it is "public" without the role-relevance test.
- Never send cold SMS or run AI auto-dialled solicitation calls.
- Never rely on a purchased list's consent claim.
- Never ignore a "no unsolicited messages" statement on a site.

---

## 3. New Zealand (Unsolicited Electronic Messages Act 2007 + Privacy Act 2020)

### 3.1 Cold email
- The Act prohibits sending unsolicited commercial electronic messages with a NZ link. Commercial messages need consent, accurate sender identification and a working unsubscribe [SECONDARY via legislation search extract; statute page 403].
- Consent can be express, inferred from conduct and business relationships, or deemed. Deemed consent applies when: the address is conspicuously published by a person in a business or official capacity, there is no statement against unsolicited messages, and the message is relevant to the recipient's business, role, functions or duties [PRIMARY, NZ Marketing Association FAQ and DIA case study extract; Schedule text not read directly]. Trade directories count as publication; addresses from a colleague's referral do not [PRIMARY, Marketing Association FAQ].
- Sole traders: no special rule found; "business or official capacity" is the test [PRIMARY on the wording, UNSETTLED on edge cases]. The FAQ directs sole traders to DIA for certainty.
- Burden of proof sits on the sender (s 9(3) as cited in secondary commentary) [SECONDARY].
- Penalties: courts can award up to NZD 200,000 for an individual and NZD 500,000 for an organisation; infringement notices are up to NZD 200 (individual) and NZD 500 (organisation) per event [SECONDARY, regulation form extract and consistent commentary]. Affected recipients can seek compensation [PRIMARY, Marketing Association FAQ].
- Address-harvesting software and harvested-address lists are prohibited [KNOWLEDGE].

### 3.2 Cold calls
- The Unsolicited Electronic Messages Act does not cover ordinary voice calls. Cold calling is not banned in NZ [SECONDARY]. The Privacy Act 2020, Fair Trading Act 1986 (misleading conduct) and Telecommunications Information Privacy Code apply [KNOWLEDGE]. The Unsolicited Direct Sales rules in the Fair Trading Act cover consumer sales, not B2B [KNOWLEDGE].
- The Marketing Association "Do Not Call" is a voluntary consumer list [KNOWLEDGE; not confirmed in this pass]. No mandatory NZ DNC register for business numbers found [UNSETTLED, absence of evidence].
- Course rule: live human calls to business lines with honest identification and a stop-calling honoured immediately.

### 3.3 SMS
- A text is an electronic message under the Act. Same consent test. A mobile number is rarely conspicuously published in a business capacity, so deemed consent is close to useless for SMS [SECONDARY].
- Course rule: no cold SMS in NZ.

### 3.4 AI voice and automated calls
- No NZ-specific rule found on AI voice outbound calls [UNSETTLED]. The Act does not cover voice calls; Fair Trading Act misleading conduct applies if the AI pretends to be human [KNOWLEDGE]. Disclose AI at the start.

### 3.5 Data sourcing
- Privacy Act 2020 information privacy principles apply to personal information (including a sole trader's name and mobile). IPP 3A, in force from 1 May 2026, requires notifying individuals when you collect their information indirectly (from a source other than the person). Whether it covers only information collected on or after 1 May 2026 is [UNSETTLED] on a single non-authoritative source.
- Buying lists: you must have a lawful and fair purpose and be able to show the source [KNOWLEDGE]. Generic company contact details are not personal information.

### 3.6 2025 and 2026 changes
- IPP 3A in force 1 May 2026 [SECONDARY]. No change to UEMA penalties found.

### NZ: what the member must do
- Email only where the three deemed-consent conditions are met; log URL, date, screenshot.
- Identify the sender and include a working unsubscribe.
- Give the Privacy Act IPP 3A notice when you hold indirectly sourced personal data (first message can carry it).
- Call business lines honestly; disclose AI use.

### NZ: never do this
- Never use harvested or purchased address lists.
- Never send an unrelated pitch to a published role address.
- Never text cold.
- Never pose as a person you are not.

---

## 4. European Union (GDPR + ePrivacy) with Germany, Netherlands, Ireland

### 4.1 EU baseline
- ePrivacy Directive Article 13: electronic mail (includes SMS), fax and automated calling systems need prior consent, with a soft opt-in for existing customers' similar products. Live calls are left to member states to choose opt-in or opt-out. Protection of legal persons (companies) is left to member states [KNOWLEDGE; directive text not re-fetched]. This is why national law differs.
- GDPR applies to personal data of any person. A sole trader is a natural person. Corporate generic addresses are not personal data, named-employee addresses are [KNOWLEDGE].
- GDPR Article 6(1)(f) legitimate interests can support B2B prospecting data, Article 14 notice within one month of collecting data from a third-party source, absolute right to object to direct marketing (Article 21) [KNOWLEDGE]. Fines up to EUR 20m or 4% of global turnover [KNOWLEDGE].

### 4.2 Germany (UWG + GDPR)
- Email and automated calls: advertising by automated calling machine, fax or email needs the addressee's prior express consent. No general B2B exception. The only exception is s 7(3) for existing customers' similar products, with clear opt-out at collection and each use [PRIMARY, UWG English text from gesetze-im-internet.de].
- Live calls: to a consumer need prior express consent; to another market participant need at least presumed consent [PRIMARY, UWG s 7(2) no. 1]. Case law requires concrete circumstances showing the business has a real interest in this exact offer. "The product might be useful" is not enough [SECONDARY, consistent across several practitioner guides].
- Identity concealment, missing valid contact address for stopping are separately unlawful [PRIMARY, s 7(2) no. 3].
- Fines under the UWG: up to EUR 300,000 for calls/automated calls without consent; up to EUR 50,000 for failing to document consent; up to EUR 100,000 for other cases [PRIMARY, UWG s 20 as returned by the fetch].
- Enforcement is mostly by competitors and associations through cease-and-desist letters with cost claims [SECONDARY].
- One practitioner guide claims B2B email to businesses is allowed on presumed consent. This contradicts the statute text. Do not rely on it [PRIMARY statute beats SECONDARY guide].

### 4.3 Netherlands (Telecommunicatiewet art 11.7 + GDPR)
- General rule: unsolicited commercial email, automated calls and fax need prior consent the sender can prove [SECONDARY, art 11.7 text via PONT/overheid extract].
- Paragraph 2 B2B exception: no prior consent is needed to a legal entity or a natural person acting in the course of their profession or business, if you use contact details they provided or published for that purpose and use them in line with that purpose [SECONDARY, statute extract]. In practice, a pitch relevant to the business address published for business contact is allowed with opt-out; an unrelated pitch is not.
- Live-call register (Bel-me-niet) and the telemarketing paragraphs protect natural persons only [SECONDARY, 2008-era summary; verify current wording].
- ACM has fined unsolicited email (e.g., EUR 100,000 decisions) [SECONDARY].

### 4.4 Ireland (S.I. 336/2011 reg 13 + GDPR)
- Regulation 13 defaults to opt-in for individuals. For subscribers that are not natural persons, email marketing can run on an opt-out basis (prohibited only once they have notified they do not consent) [SECONDARY, statute extract]. Email to an address that reasonably appears to be used mainly for commercial or official activity is allowed where the message relates solely to that activity [SECONDARY, statute extract].
- Identity must not be disguised, and a valid opt-out address must exist [SECONDARY]. Each unsolicited message is a separate offence, and the defendant carries the burden of proving consent [SECONDARY].
- Sole traders are generally natural persons: treat as opt-in [KNOWLEDGE].
- Live calls: business numbers subject to the National Directory Database opt-out and the subscriber's objections [KNOWLEDGE; not confirmed in this pass].
- DPC guidance generally requires clear affirmative consent for direct marketing outside existing-customer cases [PRIMARY on the general rule, DPC extract].

### 4.5 SMS (EU)
- SMS is electronic mail under Article 13. Opt-in in Germany; Netherlands/Ireland B2B exceptions apply in principle but a mobile is rarely "published for business contact". Course rule: no cold SMS in the EU.

### 4.6 AI voice and automated calls (EU)
- Automated calling systems need prior consent under Article 13(1). Germany lists automated calling machines in UWG s 7(2) no. 2 [PRIMARY]. Netherlands art 11.7 names automatic call systems [SECONDARY].
- EU AI Act Article 50 transparency duties, including telling people they are interacting with an AI system, applied from 2 Aug 2026, and the Digital Omnibus delayed high-risk obligations but not Article 50(1) [SECONDARY: several law-firm summaries; official text not read]. A member using an AI voice agent to talk to EU prospects should disclose AI at the start.

### 4.7 Data sourcing (EU)
- Scraped or bought B2B contact data needs a GDPR basis (legitimate interests is the realistic one), an Article 14 notice and an objection route. Germany applies UWG on top for the channel [KNOWLEDGE].
- Buying enriched mobiles does not give you channel consent [KNOWLEDGE].

### 4.8 2025 and 2026 changes (EU)
- EU AI Act Article 50 transparency (Aug 2026) [SECONDARY].
- The European Commission's Digital Omnibus proposed changes to GDPR and ePrivacy; the AI part was adopted, but data-law changes are [UNSETTLED] and should not be taught as law.

### EU: what the member must do
- Germany: no cold email. Calls only with a documented presumed-consent reason specific to the target business and the offer. Keep a record of why.
- Netherlands and Ireland: B2B email only to published business contact details, relevant to the business, with identity, address and unsubscribe, and with sole traders treated as opt-in.
- Send the GDPR Article 14 notice, keep a legitimate-interest assessment, honour objections immediately.
- Disclose AI on any voice agent.

### EU: never do this
- Never cold email a German business.
- Never email a sole trader on an opt-out theory.
- Never auto-dial or run recorded/AI voice calls without prior consent.
- Never reuse a purchased list across countries.

---

## 5. Cross-jurisdiction summary table

AU and US columns are copied from research-compliance.md conclusions.

| Topic | UK | Canada | New Zealand | EU (DE / NL / IE) | Australia | United States |
|---|---|---|---|---|---|---|
| B2B cold email model | Companies/LLPs: opt-out with identity + unsubscribe. Sole traders/some partnerships: consent needed | Implied consent only via conspicuous publication + role relevance + no refusal; sender proves it | Deemed consent: conspicuous business publication + relevance + no refusal; sender proves | DE: prior express consent (no B2B exception). NL: allowed to published business contacts for that purpose. IE: opt-out for non-natural subscribers, relevant business addresses | Same three-part conspicuous publication test; no B2B exemption | Opt-out (CAN-SPAM): ad disclosure, address, opt-out in 10 business days |
| Sole trader treatment | Individual: consent | Same CASL test, plus PIPEDA | Same test, "business capacity" | Natural person: treat as opt-in | Personal info can still be an issue | n/a for CAN-SPAM; TCPA risk on mobiles |
| Max penalty (headline) | GBP 17.5m or 4% turnover from 5 Feb 2026 [SEC] | CAD 10m per violation (business) | NZD 500,000 (organisation) | DE UWG up to EUR 300,000 (calls); GDPR EUR 20m or 4% | ACMA notices e.g. $330,000 (Tabcorp) | USD 53,088 per email (CAN-SPAM) |
| Cold call to business line | Allowed unless TPS/CTPS-listed or objected | Allowed; National DNCL does not apply to businesses; CRTC hours, internal DNC apply | Allowed; no mandatory register found | DE: presumed consent needed. NL: register covers natural persons. IE: directory opt-out [KNOWLEDGE] | Business lines not on DNC register; Industry Standard hours apply | TSR exempts most B2B calls; hours 8am to 9pm |
| Sole trader mobile calls | TPS check | Treated as business number | Privacy Act applies | Natural person rules | Wash against register | Presumed residential: high risk |
| SMS | Electronic mail: consent for individuals; do not teach cold SMS | CEM: avoid | UEMA: avoid | Opt-in in practice: avoid | Spam Act: higher risk, avoid | TCPA: do not teach |
| AI/automated voice | Prior specific consent for automated calls; AI conversational is [UNSETTLED] | ADAD rules; [UNSETTLED]; avoid | No rule found; disclose AI | Prior consent; AI Act Art 50 disclosure from Aug 2026 | No AU rule found; disclose | FCC Feb 2024: AI voices are "artificial"; consent for cell phones |
| Data sourcing | UK GDPR legitimate interest + Art 14 notice | PIPEDA business contact exception (does not authorise sending); no harvesting | Privacy Act 2020; IPP 3A from 1 May 2026 | GDPR Art 6(1)(f) + Art 14 + objection | Privacy Act with small-business exemption; harvesting banned | Mostly TOS risk; TCPA on mobiles |
| 2025/26 change | DUAA fine uplift (Feb 2026) [SEC] | CRTC rules review reported [SEC] | IPP 3A (May 2026) | AI Act Art 50 (Aug 2026) [SEC] | Sender ID register 1 Jul 2026; ACMA fines rising | FCC revocation rule delayed to Jan 2027 |
| Course verdict | Email OK to Ltd with checks; no cold SMS; TPS wash | Email only with proof; no SMS/AI voice | Email only with proof; no SMS | Block DE email; NL/IE B2B with care | Narrow email; avoid SMS | Email OK; avoid SMS/AI voice to mobiles |

---

## Sources

Primary or near-primary (read or quoted back from the regulator/statute)
- ICO, Electronic mail marketing: https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/electronic-mail-marketing/
- ICO, Telephone marketing: https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/guide-to-pecr/electronic-and-telephone-marketing/telephone-marketing/
- ICO enforcement notices (TMAC, KRA Consultancy): https://ico.org.uk/action-weve-taken/enforcement/2026/02/tmac-ltd-en/ and https://ico.org.uk/action-weve-taken/enforcement/2026/05/kra-consultancy-ltd-mpn/
- German UWG English text, ss 7 and 20: https://www.gesetze-im-internet.de/englisch_uwg/englisch_uwg.html
- NZ Marketing Association, FAQ on inferred and deemed consent: https://marketing.org.nz/resource-hub/faq-inferred-and-deemed-consent
- CRTC FAQ on CASL (seen as search extract, fetch 403): https://crtc.gc.ca/eng/com500/faq500.htm
- CRTC Unsolicited Telecommunications Rules (extract): https://www.crtc.gc.ca/eng/trules-reglest.htm and https://crtc.gc.ca/eng/phone/telemarketing/tobligations/rules-regles.htm
- OPC, e-marketing and PIPEDA guidance (extract): https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/r_o_p/canadas-anti-spam-legislation/casl-compliance-help-for-businesses/casl_guide/
- NZ Unsolicited Electronic Messages Act 2007 (fetch 403): https://www.legislation.govt.nz/act/public/2007/7/en/latest/
- DIA spam case studies: https://www.dia.govt.nz/Spam-Case-Studies
- Irish DPC, Rules for direct electronic marketing (fetch 403): https://www.dataprotection.ie/en/organisations/rules-electronic-and-direct-marketing
- Dutch Telecommunicatiewet art 11.7: https://wetten-overheid.nl/wet/BWBR0009950/artikel/11.7
- ACM spam decisions (Companeo): https://www.acm.nl/sites/default/files/old_publication/publicaties/10416_Boetebesluit%20e-mailspam%20Companeo.pdf

Secondary (verify before teaching as fact)
- ICO one-year DUAA blog: https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2026/06/one-year-on-marking-the-12-month-commencement-of-the-data-use-and-access-act/
- Perfmetrix, PECR fines after DUAA: https://perfmetrix.com/blog/pecr-fines-after-duaa-2026
- Bratby Law, DUAA commencement: https://bratby.law/data-use-and-access-act-2025-commencement/
- Freevacy PECR fine summaries: https://www.freevacy.com/news/ico/ico-fines-debt-services-company-ps300000-for-pecr-violations/7488
- Slaw, CRTC on conspicuous publication: https://www.slaw.ca/2016/11/24/crtc-assesses-conspicuous-publication-basis-of-implied-consent-in-casl-enforcement-decision/
- Stikeman, CASL enforcement: https://stikeman.com/siteassets/media-library/files/kh-general/casl-enforcement-crtc.pdf
- Lexology, FCA on CASL B2B exemption: https://www.lexology.com/library/detail.aspx?g=d7c5b6cb-1b30-4a87-b161-35a65cc97f56
- Clendons, NZ anti-spam guide: https://www.clendons.co.nz/resources/background-papers/unsolicited-electronic-messages-act-2007-practical-guide/
- Cooney Lees Morgan, IPP 3A: https://cooneyleesmorgan.co.nz/insights/the-new-privacy-rule-you-cant-ignore/
- German practitioner guides on cold calling and email: https://www.cegtec.net/en/knowledge/b2b-kaltakquise-erlaubt/ and https://dialfox.de/en/b2b-cold-calling-germany-legal/
- Gibson Dunn, EU AI Act omnibus: https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
- Jones Walker, Article 50 still applies: https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html

Open items to fetch before a final lesson
- CASL s 10(9)(b) and s 6 statute text; CRTC ADAD rules text; whether B2B-only telemarketers must register with the DNCL operator.
- NZ UEMA Schedule 1 text and penalty sections; DIA guidance on sole traders.
- Irish SI 336/2011 reg 13 live-call and National Directory Database rules; Irish penalty levels.
- Dutch art 11.7 current paragraph wording; ACM B2B guidance.
- SI 2026/82 text confirming the 5 Feb 2026 PECR fine commencement.
- Any ICO position on conversational AI voice agents under PECR reg 19.
