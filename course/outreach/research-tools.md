# Outreach tool landscape, 29 Oct 2026 (research for high-ticket course)

Method note: official pages fetched where possible (Clay, Apollo, Instantly, Smartlead, Google Maps pricing, ABN Lookup, Retell, FullEnrich, LinkedIn help). Everything else is third-party blogs, many vendor-written, and they disagree. Items marked UNVERIFIED were not confirmed on a primary source. Pricing pages often render inconsistently; re-check before quoting to members. Numbers are USD.

## Bottom line first
- For 300-600 accounts/month, an API-direct stack costs roughly US$200-330/mo; a Clay-centred stack roughly US$330-600/mo (estimates, working shown in section 11). Clay is not 10x dearer at this volume; it is dearer AND adds a plan gate (HTTP API/webhooks need Growth, ~US$446-495/mo headline) if the agent must drive it programmatically.
- The agent-callable path is the API-direct stack: Places, Apollo, one waterfall (FullEnrich/Prospeo/LeadMagic), Instantly. Clay's public REST API is new and limited (cannot write to tables per one source).
- AU owner mobiles are the weak point of every database. No source confirms AU mobile coverage for any tool. Plan to test on 100-300 real AU contacts before committing. Places gives the business's main phone and website, which for tradies is often the owner's mobile.
- Cold SMS/AI voice calling to AU/US small businesses carries real legal risk (TCPA in US; Spam Act/DNC in AU, AU DNC rules not verified here). Email + Places phone + manual/human calling is the safe core.

## 1. Clay.com
- Does: table-based enrichment; waterfall across many providers; Claygent (AI web research); signals; email campaigns; CRM sync.
- Pricing (official page, which contradicts itself): Free $0 (500 actions, 100 data credits/mo, 200 rows/table, no phone enrichment). Launch headline $167/mo (FAQ says $185): 15K actions ($60) + 2.5K data credits ($125) monthly; phone enrichment, signals, scheduled runs, no HTTP API or CRM. Growth headline $446 (FAQ $495): 40K actions + 6K data credits; adds CRM sync, HTTP API integrations, webhooks, web intent signals. Enterprise custom. Extra data credit tiers: 6K $290, 10K $460, 20K $880 monthly; top-ups carry a 30% premium. Actions reset monthly; data credits roll over (rollover terms inconsistent). [S1]
- Credit model: two currencies, actions (platform use) and data credits (marketplace data). Bring-your-own-API-key runs use actions only. Failed lookups still bill per one review [S2]. Estimates of 5-15 credits per fully enriched lead with email+phone; phone steps 2-25 credits (third-party, unverified) [S2].
- API: Public REST API (api.clay.com/public/v0, clay-api-key header) reported GA 15 Sep 2026; can run functions/searches, read tables, check balance, cannot write to tables; webhooks write in. Another review says no versioned REST catalogue or public rate limits. Plan gating reported inconsistently (webhooks/HTTP API Growth+). [S3, S4]
- SMB coverage: depends on underlying providers; no Clay-specific AU SMB data claim found.
- Gotcha: pricing complexity and credit burn; automation needs Growth; credits spent on misses.

## 2. Apollo.io
- Pricing: official page lists no prices. 2026 third-party: Free; Basic ~$49/user/mo annual ($59 monthly); Professional $79 ($99); Organization $119 ($149; a tracker says cut from $149 to $119 in Mar 2026, min 3 users). Email credits reported 30K/yr Basic, 48K Pro, 72K Org. Mobile credits reported ~100/user/yr Basic, ~1,500 Pro (UNVERIFIED, blogs only) [S5, S6].
- Official Apollo page: export up to 10,000 leads per click without selection limit; credits pooled, expire unused; API access on Custom plans only per the pricing page, while a tracker says Organization [S5, S7]. API rate limits (official docs): free enrichment 50/min, 200/hr, 600/day; other endpoints (incl. search) 1-50/min, 20-200/hr on free; paid up to 1,000/min enrichment and 200/min other [S8]. Which paid tier unlocks which API endpoints: conflicting, verify.
- Database size claim: ~275M contacts typical marketing figure (not verified here).
- SMB/mobile: head-to-head tests show Apollo mobile weaker than ZoomInfo (41% vs 67% mobile return in one 1,000-lead test; another test contradicts) [S9]. No AU-specific data found.
- Gotcha: credit pools and the API/plan gate; mobile credits scarce on cheap tiers; SMB owner data thin outside US.

## 3. Instantly.ai and Smartlead (sending)
- Instantly (official page, internally inconsistent): outreach plans Growth $47/mo (5K emails, 1K contacts), Hypergrowth $97 (125K emails, 25K contacts), Light Speed $358; unlimited email accounts and warmup on those. Separate "credits" plans for its 450M+ lead database (Growth Credits $47 for 1.5-2K credits). Bundles Starter $94, Scale $194. API listed in comparison table but per-plan availability not confirmed [S10].
- Smartlead (official): Base $39 (2K contacts, 6K sends), Pro $94 (30K contacts, 90K sends), Unlimited Smart $174, Prime $379; unlimited email accounts claimed on all; SmartServers $39/server/mo; whitelabel $29/client workspace; API plan gating unclear on page [S11].
- Both: warmup and inbox rotation built in. You still pay separately for sending domains/mailboxes (Google/Microsoft ~US$6-7 per mailbox, not verified here).
- Gotcha: deliverability is on the operator (secondary domains, SPF/DKIM/DMARC, volume per inbox); plan limits on contacts are lower than sends.

## 4. Enrichment/waterfall providers
Official FullEnrich page [S12]: Pro 1K credits/mo at $0.055/credit (~$55); 15K credits $720; mobile = 10 credits, work email = 1, personal email = 3; charged only on success; API on Pro, MCP server, Clay integration; claims ~80% average find rate, 25+ sources. Credits roll 3 months monthly / 12 yearly.
Third-party (UNVERIFIED, conflicting) [S13, S14]: LeadMagic 1 credit/email, 5/mobile (cheapest mobile; $0.01 email, ~$0.05 phone claimed); Findymail 10 credits/mobile, from ~$49-99/mo; Prospeo ~ $39-49/mo for 1-2K credits, ~10 credits/mobile, no rollover, per-user; Hunter email-focused from ~$34/mo (2K credits), no real mobile; Lusha free 40 credits then ~$37-52/user/mo, phone 5-10 credits; Kaspr from ~$49/user/mo (100 phone credits); ContactOut $49-99/mo, US/UK data strength.
AU coverage: no source confirms Australian mobile coverage for any of these. Treat as unknown; vendor-quoted hit rates are global averages.
Gotcha: mobile is where the money goes (10x an email); "find rate" is not "connect rate."

## 5. Google Places API (New)
- Official pricing [S15]: Text Search Pro $32/1K (5K free/mo); Text Search Enterprise $35/1K (1,000 free/mo); Enterprise+Atmosphere $40/1K; Place Details Essentials $5/1K (10K free), Pro $17/1K, Enterprise $20/1K (1,000 free).
- Fields (official fields doc, as summarised by the fetch tool) [S16]: websiteUri, nationalPhoneNumber, rating, userRatingCount, regularOpeningHours all sit in the Enterprise SKU. So a lead pull with phone+website bills at ~$35/1K requests after 1,000 free per month. Text Search returns up to 20 results per request, so ~600 businesses can be pulled with ~30-60 requests (cost trivial) -- inference.
- Terms: Google Maps Platform terms restrict caching, bulk export and building derivative datasets; place_id may be stored. Scraping Maps is a contract breach (third-party summaries, not legal advice) [S17]. Course note: already locked "scraping is dead."
- Gotcha: no owner name or email; the phone is the business line. Storing results beyond place_id is a terms grey area.

## 6. LinkedIn
- Sales Navigator: Core $119.99/mo ($1,079.88/yr), Advanced $159.99/mo ($1,799.88/yr), Advanced Plus quote; 50 InMail/mo (third-party, Aug-Sep 2026) [S18].
- LinkedIn's stance (official): bans crawlers, bots, browser plugins/extensions that scrape or automate activity; accounts may be limited or terminated; tools may stop working [S19].
- Tools (third-party prices): HeyReach $79/sender/mo ($63 annual), Agency $999/25 senders; Expandi $99/account; Waalaxy EUR19-69/user; La Growth Machine pricing not found [S20]. All violate the user agreement in LinkedIn's terms regardless of "cloud/safe limits" marketing. A source references a March 2026 LinkedIn action against HeyReach; details not retrieved.
- Gotcha: ban risk is real and falls on the member's personal profile. Recommend: manual/semi-manual LinkedIn only, not automated.

## 7. Australian data
- ABN Lookup web services: free, requires registration, GUID emailed, accept web services agreement; SOAP with limited JSON; schema downloadable [S21]. Returns ABN, entity name, status, state/postcode, GST registration, business names (field list from general knowledge; the page itself did not list fields). No phone/email.
- ABN Bulk Extract: free on data.gov.au, CC-BY 3.0 AU, ~6GB uncompressed, weekly; reported to have incomplete records in at least one case [S22].
- ASIC company dataset: weekly extract on data.gov.au, CC-BY; no free live API found [S22]. Company officers/directors are not in the open dataset (UNVERIFIED).
- Seek: no official read API for job ads (API is employer-side); many Apify scrapers exist; their own pages hedge on ToS compliance; SEEK terms not read (UNVERIFIED) [S23]. Safer hiring signals: Adzuna/Indeed-type APIs not verified; company careers pages.
- AU mobiles: no B2B database source confirms AU owner-mobile coverage. Best realistic sources: Places phone (business line), business's own website/Facebook page, Apollo/FullEnrich tests.
- Compliance: Spam Act - consent can be inferred from conspicuously published address only when the message relates to the person's role; no general B2B exemption per commentary; secondary sources only, confirm on acma.gov.au [S24]. Do Not Call Register treatment of business numbers: NOT verified here.

## 8. Phone/SMS and voice
- Twilio 10DLC (US): sole proprietor brand $4.50 one-time; standard brand ~$46; low-volume campaign ~$1.50/mo, standard ~$10/mo; plus carrier per-segment fees (Twilio help article, Aug 2025 changes; 2026 changes unconfirmed) [S25]. Registration requires a legitimate use case and opt-in consent; cold SMS to purchased lists is non-compliant with campaign rules in practice (general knowledge).
- AU: ACMA SMS Sender ID Register in force 1 July 2026; unregistered alphanumeric IDs show "Unverified"; Twilio registers on behalf via Console form; IDs 2-11 characters [S26]. Cold SMS in AU also falls under the Spam Act (consent).
- Retell (official) [S27]: voice $0.07-0.31/min; $10 free credit; 20 concurrent calls included, +$8/concurrent/mo; Retell number $2/mo; telephony $0.015/min (listed countries); batch calls +$0.005/dial; branded caller ID $0.10/call; failed calls not billed. Blake's course already uses SIP bridge for AU.
- Outbound restrictions: Retell leaves consent/DNC/TCPA to the caller; FCC (Feb 2024) treats AI voices as "artificial" under TCPA, needing prior express written consent for marketing calls [S28]. Bland refuses cold-calling use. AU status of Retell-managed numbers unconfirmed. Conclusion: AI cold calls to strangers is high-risk in US; AU DNC/ACMA rules need checking before teaching it.

## 9. Signals
- Common Room: Essential ~$2,100-2,500/mo annual (third-party), no free plan; overkill for a solo operator [S29].
- Trigify: pricing not public (book a call); Ocean.io $47.25/mo claimed on one tracker (UNVERIFIED) [S29].
- Clay signals on Launch+ (job changes, web intent on Growth) [S1].
- Review scrapers: Maps scraping breaches Google terms (see section 5). Using Places API review counts/ratings is permitted within terms.
- Job-posting monitors: Seek scrapers exist but ToS-risky; no official API.
- Cheap signals an agent can compute free: Places (no website, low review count, hours), ABN registration date (new business), own Meta Ad Library check, Google Business Profile gaps. These match the course's "gap filter" approach.

## 10. AI SDR products
- 11x: unpublished; estimated $5-10K/mo or $40-60K/yr, annual, enterprise-positioned. Artisan (Ava): unpublished; est. $2.4-7.2K/mo annual. AiSDR: public Solo $250/mo (200 contacts), Explore $900 (800), Scale $2,500 (2,500). Jason AI (Reply.io): $49 vs $500/mo conflicting. [S30]
- Assessment: no independent small-business results found. At $250+/mo per 200 contacts, AiSDR costs more per contact than the DIY stack and gives less control; 11x/Artisan are priced for enterprise. For a member selling $5-30k systems, over-priced and generic copy is the risk. Treat as hype until independent data appears (our judgement).

## 11. Cost comparison, 300-600 accounts/month
Assumptions (ours): ~450 accounts, ~1.3 contacts each = ~600 contacts, 600 emails, 150 mobile attempts, 3-step email sequence, 2-3 sending domains/6 mailboxes (~$40-60/mo).
API-direct: Places ~$0-20 (1,000 free Enterprise requests) + Apollo Basic $49-59 + FullEnrich Pro ~$55-110 (600 email credits + 150 mobile x10 = 2,100 credits; may need ~2K tier, ~$110) + Instantly $47-97 + mailboxes/domains $40-60 = about $200-350/mo.
Clay-centred: Clay Launch $167-185 + extra data credits (600 contacts at 5-10 credits = 3-6K; Launch 2.5K included, so 6K tier ~$290) = $185-300; if the agent needs HTTP API/webhooks, Growth $446-495 + credits; + Instantly $47-97 + mailboxes $40-60 = about $330-500 (Launch) or $550-700 (Growth). Clay can also be used with Apollo/FullEnrich keys via BYOK to cut data credits but still pays actions.
Where Clay earns its price: multi-provider waterfall without writing code, Claygent research per account (personalised first lines), non-technical members editing columns, signals on Launch. Where overkill: a solo operator whose agent can already call Places/Apollo/FullEnrich APIs; at 450 accounts/mo the orchestration is a script, and Clay's table UI is a second control surface the agent cannot fully drive on lower plans.
Recommendation: API-direct default; Clay as optional for members who want a visual UI and will pay.

## 12. What operators publish for signal-based outbound (their claims, not ours)
Evidence is mostly vendor/agency blogs citing each other (circular), and no Clay-specific case study was found.
- Instantly's 2026 benchmark, quoted second-hand: average cold reply ~3.43% [S31].
- Twelfth Agency claims 15-25% reply on signal-triggered vs ~3% cold; one client 63 meetings from 175 accounts in 90 days [S32].
- Rept: 20.93% positive reply rate across 420K emails / 75 campaigns (own data) [S33].
- GTME agency, more conservative: signal-based 8-14% reply, top quartile 16-22%, 2-4x list-based [S34].
- Growleads (via aggregator): 4-10% meeting conversion with 3-5 intent signals [S35].
Planning assumption for SMB local trades: do not assume more than low-single-digit reply and 0.5-2% booked-call rate until a member's own data says otherwise (our judgement; none of the above are SMB trades benchmarks). Named individual practitioners (e.g. Clay-community GTM engineers) were not verified in this pass.

## Gaps to close
Kaspr/ContactOut/Hunter/Prospeo/LeadMagic official pricing; AU coverage test; AU Do Not Call Register rules for business numbers; Seek ToS; La Growth Machine; Instantly/Smartlead API plan gating; Apollo API plan gating; 2026 Twilio fee confirmation.

## Sources
S1 https://www.clay.com/pricing
S2 https://crustdata.com/reviews/clay ; https://prospeo.io/s/clay-pricing ; https://leadmagic.io/guides/clay-pricing-credits-actions
S3 https://www.cleanlist.ai/blog/2026-10-16-clay-api-guide
S4 https://pipeline.zoominfo.com/sales/clay-api ; https://frontal.so/gtm-apis/enrichment-apis/clay-api-review
S5 https://www.apollo.io/pricing
S6 https://www.zeliq.com/blog/apolloio-pricing ; https://costbench.com/changelog/apollo-io-price-decrease-2026-03/ ; https://bitscale.ai/blogs/apollo-pricing-a-full-breakdown-of-plans-credits-hidden-costs-2026
S7 https://costbench.com/software/ai-sales-tools/apollo/
S8 https://docs.apollo.io/docs/rate-limits
S9 https://www.cleanlist.ai/blog/2026-03-07-apollo-vs-zoominfo ; https://pipeline.zoominfo.com/sales/apollo-vs-lusha
S10 https://instantly.ai/pricing
S11 https://www.smartlead.ai/pricing
S12 https://fullenrich.com/pricing
S13 https://leadmagic.io/comparisons/leadmagic-vs-findymail ; https://satellyte.ai/blog/findymail-review-2026 ; https://satellyte.ai/blog/leadmagic-review-2026
S14 https://overloop.com/blog/contactout-pricing ; https://leadhaste.com/blog/lusha-vs-kaspr ; https://growthhacksuite.com/hunter-io-pricing-model
S15 https://developers.google.com/maps/billing-and-pricing/pricing
S16 https://developers.google.com/maps/documentation/places/web-service/data-fields
S17 https://openplacesapi.com/blog/can-you-store-places-api-results ; https://thunderbit.com/da/blog/is-scraping-google-maps-legal ; https://cloud.google.com/maps-platform/terms/maps-service-terms/index-20181015
S18 https://www.cleanlist.ai/blog/2026-05-08-linkedin-sales-navigator-pricing-guide ; https://www.supered.io/blog/linkedin-sales-navigator-pricing/
S19 https://www.linkedin.com/help/linkedin/answer/a1341387
S20 https://www.joinvalley.co/blog/heyreach-pricing-explained-2026 ; https://blog.gojiberry.ai/blog/heyreach-review ; https://marketbetter.ai/blog/waalaxy-pricing-breakdown-2026/
S21 https://abr.business.gov.au/Tools/WebServices
S22 https://data.gov.au/data/dataset/abn-bulk-extract ; https://www.data.gov.au/data/dataset/asic-companies
S23 https://jobspipe.dev/blog/seek-api.md ; https://apify.com/tortuga/seek-scraper.md
S24 https://legalvision.com.au/spam-act-exemptions ; https://emaillistvalidation.com/blog/conspicuously-published-address-rule-australian-spam-act/
S25 https://support.twilio.com/hc/en-us/articles/1260803965530
S26 https://support.twilio.com/hc/en-us/articles/46266521342747 ; https://www.acma.gov.au/sites/default/files/2026-01/SMS%20Sender%20ID%20Register%20user%20guide%20for%20businesses%20and%20organisations_Dec%202025.pdf
S27 https://www.retellai.com/pricing
S28 https://www.retellai.com/blog/tcpa-compliance-playbook-voice-ai-outbound ; https://wiley.law/alert-FCC-Extends-Regulatory-Reach-Over-AI-Announces-TCPA-Restrictions-Cover-AI-Generated-Voices-in-Outbound-Calls
S29 https://www.11x.ai/guides/common-room-pricing ; https://trigifyio.featurebase.app/help/articles/2331195-trigify-pricing-plans ; https://pricingsaas.com/companies/ocean
S30 https://marketbetter.ai/blog/best-ai-sdr-tools/ ; https://prospectai.co/resources/blog/ai-sdr-pricing-comparison-2026
S31 https://gtmeagency.com/blog/outbound-benchmarks-2026
S32 https://twelfth.agency/2026/04/01/signal-based-outbound/
S33 https://rept.co/blog/outbound-benchmarks-420k-emails-analysis
S34 https://gtmeagency.com/blog/outbound-benchmarks-2026
S35 https://salesmotion.io/blog/b2b-prospecting-guide
