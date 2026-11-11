# Offers scaling in the Meta Ad Library, 30 Oct 2026

Method: Meta Ad Library search through the Ads MCP, active ads only, US/AU/GB/CA, eight offer keywords, then a per page count for the pages that kept showing up. The Ad Library shows creative count and run dates, not impressions (impressions are only published for political ads), so "scaling" here means many active creatives plus a long run. Blake's rule: 15 or more active creatives on one offer means they are scaling and worth studying. Counts are what the library returned on the day; they move.

## Pages over the 15 creative line

| Page | Active ads | Offer in one line | Niche | Running since | Hook pattern | Two ways to evolve |
|---|---|---|---|---|---|---|
| Cole Gordon | ~511 | Our setters perform or you don't pay (appointment setters placed in your business) | Coaches, agencies, info businesses | Oct 2026 batch, page older | Performance guarantee in the headline, dozens of versions of one line | Same promise, narrower niche (trades, clinics); same promise with AI run outreach instead of human setters |
| Aaron Burnham | ~205 | Sales calls on your calendar in 14 days | B2B companies, SaaS, agencies | Sep 2026 | Outcome plus timeframe, one line repeated across hundreds of versions | Same offer for one industry; same offer for AU/UK where few run it |
| Jimmy The Lead Gen Guy | ~41 | Learn AI email lead generation (course, free course front end) | People wanting an agency or lead gen skill | Oct 2026 | Education offer, "learn" hook | Not a service offer; study the funnel, not the offer |
| Andrew J. Cass | ~32 | AI chatbot and after hours answering, built and live in 10 days; also "1,000 leads in your CRM in 60 days" | Rotated by niche: plumbers, HVAC, pest control, lawyers, CPAs, SaaS | Apr 2026 | Same offer, different niche per ad (the clearest example of Blake's "same offer, different niche") | Pick a niche he is not running; same offer in AU/UK |
| Enhanced AI (UK) | ~23 | We find leads, you build / Your postcode, your customers | Builders and trades, UK | Oct 2026 | Local, plain, "your postcode" | Same offer for another trade; same offer in AU/US |
| CallHero (CA) | ~21 | Turn missed calls into booked (dental) patients | Dental and clinics | Jul 2026 (page since 2025) | Missed calls to booked patients, dental variant split tested | Same offer for physio, vets, med spa; same offer in AU |

## Below the line but worth a look

| Page | Active ads | Offer | Note |
|---|---|---|---|
| Roof Flow AI | 12 | One roofing CRM that replaces 10 apps | The niche CRM play. Same shape as Blake's $22k construction CRM. Evolve: another trade, another country |
| 11x | 6+ | AI SDR that calls every inbound lead in under 2 minutes | SaaS, shows the speed to lead angle |
| Switched On AI (AU) | 5 | AI receptionist plus websites for locals | AU proof the receptionist offer runs here |
| SMGP | 4 | 20 meetings every month with AI | Appointment setting with a number |
| Marketing for Businesses | 2 | 1,000 real leads or you don't pay | Performance guarantee, lead gen |
| Fize AI, Growth Layer AI, Quantum Peak AI | 1 to 5 each | 90 qualified calls in 90 days / revenue every month with this system | Same promise shape, many small players |

## The four offers for the course table

1. **Missed call recovery and AI receptionist for clinics and trades.** CallHero (21), Andrew J. Cass (32, niche rotated), Switched On AI (AU). Evolve: pick a clinic or trade type nobody is running in your country.
2. **Booked sales calls, performance based.** Cole Gordon (511), Aaron Burnham (205), SMGP, "1,000 leads or you don't pay". Evolve: one industry only, or AI run outreach as the mechanism.
3. **Local lead gen for trades, "we find leads, you build".** Enhanced AI UK (23), Tradie Pulse AU, BrokerGrow AU (brokers). Evolve: another trade, another country.
4. **One niche CRM that replaces the stack.** Roof Flow AI (12). Evolve: plumbing, electrical, landscaping; this is the custom implementation path from Module 2.

Searches run: AI receptionist, AI lead generation, AI voice agent, AI appointment setter, AI automation agency, missed call text back, AI SDR, AI employee for your business, AI chatbot for your website. Keep this file current; the programme promises members the list is maintained.

## AU and UK pages, rechecked 30 Oct 2026 afternoon (per page look up, active, country filtered)

| Page | Country | Active ads | Offer from headlines | Note |
|---|---|---|---|---|
| Enhanced AI | UK | 20 | "We Find Leads, You Build" / "Your Postcode, Your Customers" | Local lead gen for builders and trades. Two headlines, ten variations each, all started 28 Oct 2026 |
| Tradie Pulse | AU | 14 | Ads and lead gen for tradies, proof led ("$44K In Roofing. Real Jobs", "$170K In Work", "60 Leads. Zero Follow Ups. Gone") | Marketing agency for tradies, Gold Coast. Oldest active ad from Oct 2026. The "we find leads, you build" shape in AU |
| BrokerGrow | AU | 12 | "Qualified Meetings. More Settlements." | Appointment setting for mortgage brokers. One headline, twelve variations, all started 29 Oct |
| Callacy AI | AU | 11 | (no headline set) AI call answering | Ads since mid Oct 2026 |
| Switched On AI | AU | 5 | "Answers your phone when you can't", "Get a text when you can't pick up", "Websites by two locals in Morayfield" | AI receptionist plus websites, local positioning |
| Sevenfold | AU | 4 | "Never miss a customer again" | AI receptionist |
| Con The Builder | AU | n/a | "$700 spent. $98K won." | Ads for builders, proof led, same shape as Tradie Pulse |
| PulseAu | AU | n/a | "Join 500+ Tradies using PulseAU" | Software for tradies, not a service offer |

Read: no AI service page in AU is over the 15 line today. The 15 plus pages are US (Cole Gordon, Aaron Burnham, Andrew J. Cass) and UK (Enhanced AI). That is the arbitrage the course teaches: proven at scale in the US, barely run in AU.

## How the Ad Library tool behaves (tested, for the course prompt)

- Keyword search returns 25 ads of an estimated total. Generic words are junk: "missed calls" AU = 9,098 results, first page all novel and drama apps. "AI receptionist" AU = 552, first page had seven relevant pages.
- A page's active count only comes from a second look up by page id (estimated_total_count). So the course prompt is two steps: find pages, then count them.
- Fields returned: page name, page id, link headline, creation and start time, snapshot URL, currency. No body text, no impressions. Hook reading needs the snapshot link opened.
- Works in Claude with the Meta Ads connector on an account that has an active ad account. Not available inside a Base44 Jarvis.
