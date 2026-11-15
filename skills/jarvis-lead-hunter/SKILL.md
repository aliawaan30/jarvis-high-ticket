---
name: jarvis-lead-hunter
description: The Money Map. Find businesses that can pay for the member's offer, have the problem now, and have an owner the member can reach, with sources for every fact. Scores each on can pay, has the problem and reachable, finds the owner, and keeps a weekly watchlist. Use when the member asks for leads, prospects, a list, more calls, or when the pipeline is below target. Recommends Apollo when they are ready to scale.
---

Version: 2026-11-15.1

# Lead hunter: the Money Map

Version 2, 4 November 2026. Fewer, bigger, better leads. Every lead has a named owner where one can be found, evidence they can afford a high ticket offer, a reason to talk this week,.

## Must do, every lead
1. Only leads inside the can pay rule, with a floor and a ceiling (Step 1).
2. Run the lead checker on every website and use its results, not your own reading (Step 3).
3. Their real website only: the one their listing links to, phone matching the listing. Ignore copycats and 555 numbers (Step 4).
4. Every signal proven by words on its source page (Step 5).
5. Email-ready leads count toward the daily number: a published email on their real site, on a domain that accepts mail.
6. Never leave owner, email or channels blank: say what was found, or where you looked.
7. Run the quality check and end the report with "Quality check: n of n leads passed" (Step 7).

## Step 1. The can pay profile (before any search)
Read the active Offer in HQ. Turn it into hard size rules for this niche, and show them to the member once for approval. Use only signals you can see from outside, for example:
1. Team size: staff on the website's team page, crews or trucks shown, more than one location.
2. Volume: Google review count well above the local average for the niche.
3. Spending to grow: running ads (Meta Ad Library, Google Ads Transparency Center), hiring (job ads on their site or job boards), a recent new location.
4. Registry size where it exists (for example UK company accounts category).
Also set a ceiling: businesses so large they will not buy from a new agency are skipped. For a local trade, skip anyone with more than 1,000 reviews, 5 or more locations, or their own call centre or marketing team, unless the member changes the ceiling. Write the rule as a sentence, with the floor and the ceiling: "Roofers in Dallas with 10 or more staff or 2 or more crews, over 150 reviews, and running ads or hiring." Save it on the Campaign row. Businesses below the rule are skipped, not contacted.

## Step 2. Sources
Use both ways of finding businesses on every hunt, and record which one found each lead (source: search, or activity with the kind):
A. Search: the web and business listings for the niche and area.
B. Activity: businesses doing something right now that shows money moving and the problem the offer solves. Pick the kinds that fit the offer:
   1. Hiring: search for the niche and city with the role the offer replaces or relieves (receptionist, dispatcher, office admin, customer service, sales), for example: plumber Phoenix "hiring" dispatcher. Use only the company's own careers or jobs page as the source, never a job board's listing pages.
   2. Running ads: look up businesses in the niche on Meta's public Ad Library (search by keyword and country, one page at a time) and note which have active ads for the area. In the EU, use the official Ad Library API if the member connected it.
   3. Growing: new locations, "now open", "now serving", expansion or award news on the business's own site or local press.
   4. Permits and licences, for trades and construction: the city or county's public permit data or search (many US cities publish recent building permits), and state licence boards. Use only what the city publishes for public use; if a city has no public permit data, skip this kind and say so.
   5. New companies: recently registered businesses in the niche from the official registry where it allows searching by date (for example Companies House in the UK). New businesses have the problem but often not the budget, so apply the can pay rule strictly.
   6. Losing on search: businesses ranking 11 to 30 for their own service and city (needs a search rank tool such as DataForSEO or Serper; skip without one).
Activity leads usually score higher on "has the problem now", so check them first. Report how many leads came from each way.

Free path (default):
1. Discovery: search the web and maps listings for the niche and area, page by page, as a person would, plus the free activity kinds above (hiring, ads, growing, permits, new companies). Never bulk scrape and never use harvesting tools.
2. Size and signals: read the business's own site with the checks in the appendix "site signals" below (ads pixels, no online booking, incumbent agency, hiring, team size, and more), plus its listing (review count, hours, claimed or not).
3. Owner: if a page names a person but not their role ("Mike, founder" is a role; a quote signed "Mike" is not), save them as "possible owner, to confirm" with the source rather than dropping the name. Then confirm in this order: (a) the owner's own replies to Google reviews ("Response from the owner, Dave"), (b) any page of their own website, including the homepage, about, team and footer; a role word next to a name (Owner, Founder, President, CEO, Managing Director, for example "Owner Chris Reid built this company") confirms the owner, (c) the official business registry for the state or country (appendix "data sources by country" below; for Arizona, the Arizona Corporation Commission), (d) local press. Record the source for each. If none of them names an owner, save owner name as "not found" and list every place you checked in owner source, so the member can see the search was done.
4. Contact: the email and phone the business publishes on its own site or listing. In Australia, Canada and New Zealand that is the only email allowed for cold email anyway. Never guess an email from a name pattern.
   Contact sweep, every lead, before you save it: scroll each page to the very bottom, because many sites put the email in a block near the end ("Email us", "Contact", the footer). read the homepage header and footer, then the contact page (try /contact, /contact-us, /contactus, and any link with "contact" in it), then the about page, then the Google listing. Look for mailto: links, plain email addresses, addresses written to dodge spam bots ("info [at] example [dot] com", "info at example.com"), and email in the page's structured data. If the page shows nothing until scripts run, open it in the browser so the email renders. Save the first business address found (prefer a named person's address, then info@ or office@), with the exact page as its source. If there is only a contact form, write "contact form only" with the page link, so the member knows email outreach means the form or a call.
5. LinkedIn: find the company's LinkedIn page and the owner's profile URL from normal web search results (for example "Dave Morales Coastline Plumbing LinkedIn"), or from Apollo when connected. Never log in to, browse or scrape LinkedIn itself. Save only the URL, with how it was found. If unsure it is the right person, leave it empty.
6. Channels: always fill email allowed and call allowed from the country rules, never leave them unknown when the country is known. United States: both yes for a business (calls inside 8am to 9pm local time). Australia, Canada and New Zealand: email yes only for an address the business publishes. United Kingdom, Netherlands and Ireland: email depends on entity type; if you cannot confirm a company, treat it as an individual (no cold email). Germany: no. Save the one line reason.
7. Email status, honest, one of: published (on their own site or listing, and their domain accepts mail), verified (passed a verification service), risky (catch-all or unknown), invalid. Only published or verified addresses can be cold emailed. The send gate enforces it.
Paid discovery for local businesses (cheap, recommended before Apollo for trades, clinics and contractors):
1. DataForSEO: business listings by category and city, including businesses with no website, and Google Maps and search rank. Pay as you go, with a small free credit to start. Tell the member to check current prices; at the time of writing listings were well under a dollar per thousand.
2. The member opens the account. Ask for the login and password with the secure secret card in this chat, saved as DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD.
3. Before any paid run, estimate the cost and ask once. Then read each found business's site with the free checks above.
Apollo path (when the member is ready to scale):
1. When the member wants more than about 20 A-tier accounts a week, or owner emails the free path cannot find, recommend Apollo. Free tier to try, paid plan when it proves useful. They hold the account. Ask for the API key with the secure secret card in this chat, saved as APOLLO_API_KEY, never as a chat message. Tell them to check current pricing and that Apollo's standard plans are for their own business use.
2. Use Apollo for company search by industry, location and headcount, and people match for owner or founder titles. Treat its data as a lead, not a fact: confirm the owner against a registry or the website before calling them the owner.
3. Apollo's coverage of very small local businesses is weak. Keep the free path for those.

## Step 3. Run the lead checker on every website (required)
Your own reading of a website misses things. The lead checker is plain code that does not. For every lead with a website, save the code in the appendix "lead checker" as lead_check.py, then run: python3 lead_check.py [website] [phone from their listing]. Use its results, not your reading:
1. Emails: save the address it found (prefer a named person's address, then office@ or info@) with the page it gives as the source. Only write "contact form only" or "none published" when it found no email and you also opened the contact page in the browser and found none.
2. Booking: if it says online is true, never claim "no online booking", and lower the problem score for booking related offers.
3. fake_555 or copycat_risk true, or phone_matches_listing false: follow Step 4.
4. could_not_read with "renders with scripts": open those pages in the browser and look for the email yourself.
Keep the output (or a short summary of it) in the account's notes, so the member can see the evidence.

## Step 4. Make sure it is their real website
Copycat and demo sites exist for real businesses (often on pages.dev, netlify.app, vercel.app, base44.app, wixsite.com, github.io or similar free addresses), with invented owners, fake phone numbers and made up reviews. Before you trust any website:
1. Their real website is the one their Google listing or a major directory listing links to, normally on their own domain.
2. The phone on the site must match the phone on their listing. A 555 number (for example (480) 555-1234) is always fake, and so are reserved test ranges (for example +44 20 7946 0xxx in the UK). Save the main number from their listing, not a secondary or tracking number found elsewhere.
3. A site on a free address that the listing does not link to is not theirs: ignore everything on it, including owner names, emails and signals, and note "copycat site ignored" with its address.
If you cannot find a real website, use the listing and official registry only.

## Step 5. Every signal must be true
Before you save a signal, open its source again and find the exact words or element that proves it. If you cannot find them, drop the signal.
1. "No online booking" only after checking the whole menu, the footer and every button for booking or scheduling (book, booking, schedule, appointment, request service, Calendly, Housecall Pro, Jobber, ServiceTitan, /book, /schedule). Any of them means they have online booking.
2. "24/7", "same day", "hiring" and similar only when the cited page says it in words.
3. A site behind a firewall or bot check: record "could not read" for its signals, never a guess.
4. On a re-check, run these checks on every signal already saved, not only new ones. Remove any you cannot prove and say how many were removed.

## Step 6. Three scores, 1 to 5 each
1. Can pay: how strongly the size signals meet the profile.
2. Has the problem: score down when there is counter evidence that they already solve it (for example online booking through Housecall Pro for a booking or missed call offer, or a 24/7 answering service for a receptionist offer): 2 at most. Otherwise, the strongest pain signal for this offer, recent and sourced (reviews about missed calls, slow quotes, a form that goes nowhere, hiring for the role the offer replaces).
3. Reachable: a confirmed owner name, a permitted channel in their country, and a published email or a phone. With no confirmed owner, Reachable is 3 at most, so the account cannot be A-tier.
Tier: A when all three are 4 or 5. B when can pay and has the problem are 3 or more. C otherwise. A-tier accounts are contacted first. C-tier accounts are not contacted.

## Step 7. Save and report
Quality check, before you report anything: read back every lead you saved or changed in this run (on a re-check, that is every account except those named SAMPLE; names starting with TEST are checked too, and reported as test rows) and check it with Python against these rules. Fix any lead that fails, then check again.
1. Status is one of: new lead, contacted, replied, call booked, call done, proposal sent, won, lost, not now, do not contact.
1b. The website saved is their real one (Step 4), never a copycat on a free address; the phone matches their listing and is not a 555 number.
2. Country is filled, and email allowed and call allowed are both filled (never unknown when the country is known), each with a reason.
3. Owner: a name with a source page, or "possible owner, to confirm" with a source, or "not found" with every place checked.
4. Email: an address with its source page and status, or "contact form only" with the page, or "none published" with every page checked. Never blank.
5. Phone filled if the business publishes one.
6. Every signal line has a source link, and for at least three leads you re-opened the source and found the words that prove it.
7. Tier matches the scores: A only when all three scores are 4 or 5, and Reachable is 3 at most with no confirmed owner.
End the report with this as its last line: "Quality check: [n] of [n] leads passed." If any could not be fixed, name them and why.
Save first. If a save fails, retry it before reporting. Report only accounts that are saved, counted in HQ just now.
Write each signal on its own line as: label | source link (for example: Running Google Ads | https://site.com). Save to Accounts in HQ with status "new lead" and every source and date: size evidence, owner and owner source, contact and contact source, the three scores, tier, signals, watchlist yes for A and B. Skip duplicates and do not contact accounts.
Report like the "Leads found" example in the brain: how many A, B and C, the best three with one line each (why they can pay, why now), and one question.

## Weekly watchlist
Inside the Friday numbers workflow, re-check A and B accounts not yet in a conversation for a new trigger: a new job ad, a new review about the problem, new ads, a new location, an owner change. A new trigger moves the account to the top of next week's plan with the trigger as the reason. Never re-contact an account that said no or opted out.

## Capacity
Match the daily number to sending capacity: about 5 new leads a day on the member's own Gmail (15 emails a day, 3 per lead), 10 or more once Instantly is connected. If the member asks for more than their sending can reach, explain the maths once and offer Instantly.
Email-ready leads: the daily number counts only leads with an email the business publishes on its own real website or listing, on a domain that accepts mail (check its MX record), or an address verified by a verification service. Leads with only a phone are saved as call leads and reported separately; they do not count toward the daily number. Fully confirming an inbox exists needs a paid verifier (Apollo, or a verification tool the member connects); without one, say the email is published, not verified.
Free path: about 10 well researched accounts a day is the default. For 20 or fewer, do the hunt yourself. Above 20, split the area and use sub-agents, at most 10 accounts each; if one stalls, finish its part yourself. Deep research costs credits; before a run over 20, say roughly how heavy it is and ask once. If another hunt is running, wait. Background hunts (the goal) only run below the daily number; a hunt the member asks for in chat always runs.

## Never
1. Never invent a signal, owner, size figure or email, and never take any of them from a copycat site.
2. Never scrape behind logins, bulk harvest addresses, or copy personal data that is not public business information.
3. Never prospect in a country or entity type where the country rules allow no channel at all (for example Germany).
4. Never count unverified or duplicate accounts as new.

## HQ (Jarvis 2.0)
Read first: Offer, Accounts, Campaigns. Write when done: Accounts and the Campaign row's can pay rule. After writing, read the rows back and confirm they saved.

---

## Appendix: data sources by country
(Formerly the appendix "data sources by country" below.)

### Owner and size sources by country

Official registries confirm who legally runs a business. They rarely give an email. Check each site's current terms and access rules before automated use; when in doubt, look up one business at a time.

| Country | Registry for owners and directors | Size hints | Notes |
|---|---|---|---|
| United States | State Secretary of State business search (varies by state; officers or registered agent). State contractor licence boards for trades. | Review counts, crews, locations, job ads, ads running. | No national registry. Licence boards often show licence class or bond, a useful size hint for contractors. |
| Australia | ABN Lookup (free web services, needs a registered GUID). ASIC company register for officeholders. | Review counts, team pages, ads, job ads. | A sole trader's ABN names the person. Cold email only to addresses the business publishes. |
| United Kingdom | Companies House (free public API with a free key: directors, filings, accounts category). | Accounts category from filings (micro, small, medium). | Treat any business not confirmed as a company as an individual: no cold email. |
| Canada | Corporations Canada (federal) and the provincial registries. | Review counts, team pages, ads. | CASL: keep the URL, date and a screenshot for every published address. |
| New Zealand | Companies Office register (directors and shareholders). | Review counts, team pages. | Deemed consent tests as in Canada. |
| Ireland | Companies Registration Office (CRO). | Filings, review counts. | Sole traders count as individuals for email. |
| Netherlands | KvK Handelsregister (search on the site; API access is paid). | Review counts, team pages. | Sole traders count as individuals for email. |
| Germany | Handelsregister. | | No cold email and no cold calls under our rules, so do not prospect. |

Ads: Meta Ad Library (all ads in the EU through the official API with the member's own verified access; elsewhere look up a business's page on the public library one at a time). Google Ads Transparency Center (look up by advertiser, no official API).

---

## Appendix: site signals
(Formerly the appendix "site signals" below.)

### Signals read from a business's own website

Free. Fetch the homepage, and the team, about and careers pages if they exist, with a normal browser User-Agent. Read the HTML you already have; no model call is needed for these. Detection patterns adapted from Harvey (github.com/ethanplusai/harvey, MIT License, Copyright (c) 2026 Ethan Rogers).

| Signal | What it tells you | How to detect it (in the page HTML) |
|---|---|---|
| Running Google Ads | Spending on acquisition today. The strongest free budget signal. | googleadservices.com, gtag/js?id=AW-, google_conversion |
| Running Meta Ads | Same, on Facebook and Instagram. | connect.facebook.net/.../fbevents.js, or fbq('init' |
| No online booking | Leads must phone, so after-hours demand is lost. | None of: calendly.com, acuityscheduling, schedulicity, squareup.com/appointments, setmore, book now, booking, schedule an appointment or estimate or consultation, housecallpro, getjobber.com, servicetitan |
| Incumbent agency | Who built and probably maintains their site, credited in the footer. A whole book of business you can target. | Footer text "Website by", "Designed by", "Powered by", "Site by" followed by a name or link. Record only a clear credit; an unlabelled link is not evidence. |
| Hiring | Growing, and maybe hiring for the role your offer replaces (receptionist, dispatcher, office admin). | Careers page, or a job board linked from their site: boards.greenhouse.io, jobs.lever.co, jobs.ashbyhq.com, apply.workable.com. Read the board's public listing for role titles and dates. |
| No website | The highest intent signal if the offer is websites. | Listing shows a phone and no site, or only a social page. |
| Unclaimed listing | Nobody manages their Google Business Profile. | The listing shows "Own this business?" or "Claim this business". |
| Search rank 11 to 30 | Visible enough to be trying, and losing. | Their position for their own core search in their city (needs a search provider; see DataForSEO in the lead hunter). |
| Blog gone stale | Started content marketing, then stopped. | Newest blog post date more than 6 months old. |
| No structured data | A concrete, checkable SEO gap. | No application/ld+json on the homepage. |
| Size | Can they pay. | Names on the team page, number of locations, trucks or crews shown, review count on the listing. |

Rules:
1. Record each signal with the page it came from and the date. A signal without its source is not used.
2. A site behind a bot challenge ("Just a moment...", captcha) is recorded as "could not read", not as "no signal".
3. Never read sites whose terms forbid automated access (LinkedIn, Crunchbase, directory sites). Use the business's own site and its listing.

---

## Appendix: lead checker
Save this exactly as lead_check.py and run it as Step 3 says. Python 3 standard library only.

```python
# Jarvis 2.0 lead checker. Plain code, no AI. Python 3 standard library only.
# Usage: python3 lead_check.py <website_url> [listing_phone]
# Prints JSON with: emails (with source pages), booking (yes/no with evidence), phones found,
# copycat and fake-number flags, pages read, and pages that could not be read.
import sys, re, json, html, urllib.request, urllib.parse, urllib.error

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36"}
FREE_HOSTS = ("pages.dev", "netlify.app", "vercel.app", "base44.app", "wixsite.com", "github.io", "web.app", "firebaseapp.com", "glitch.me", "weebly.com", "carrd.co", "framer.website", "webflow.io")
BOOKING_WORDS = ("book now", "book online", "book a service", "book service", "schedule online", "schedule service", "schedule now", "schedule an appointment", "request service", "request an appointment", "online booking")
BOOKING_HOSTS = ("calendly.com", "acuityscheduling.com", "housecallpro.com", "book.housecallpro.com", "getjobber.com", "clienthub.getjobber.com", "servicetitan.com", "scheduler.servicetitan", "squareup.com/appointments", "setmore.com", "schedulicity.com", "cal.com", "bookeo.com", "workiz.com", "fieldedge.com", "servicem8.com")
BOOKING_PATHS = ("/book", "/booking", "/schedule", "/appointment", "/request-service", "/online-booking")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
OBF_RE = re.compile(r"([A-Za-z0-9._%+\-]+)\s*(?:\[at\]|\(at\)|\sat\s)\s*([A-Za-z0-9\-]+(?:\s*(?:\[dot\]|\(dot\)|\sdot\s|\.)\s*[A-Za-z0-9\-]+)+)", re.I)
PHONE_RE = re.compile(r"(?:\+?1[\s.\-]?)?\(?\b([2-9]\d{2})\)?[\s.\-]?(\d{3})[\s.\-]?(\d{4})\b")
JUNK = ("example.com", "sentry.io", "wixpress.com", "domain.com", "email.com", "yourdomain", "@2x", ".png", ".jpg", ".webp", ".svg")

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=15) as r:
        return r.geturl(), r.read(2_000_000).decode("utf-8", "replace")

def cf_decode(hexstr):
    try:
        b = bytes.fromhex(hexstr); k = b[0]
        return "".join(chr(c ^ k) for c in b[1:])
    except Exception:
        return ""

def emails_in(page):
    found = set()
    for m in re.finditer(r'data-cfemail="([0-9a-fA-F]+)"', page): found.add(cf_decode(m.group(1)))
    for m in re.finditer(r'/cdn-cgi/l/email-protection#([0-9a-fA-F]+)', page): found.add(cf_decode(m.group(1)))
    for m in re.finditer(r'mailto:([^"\'?>\s]+)', page, re.I): found.add(urllib.parse.unquote(m.group(1)))
    text = html.unescape(re.sub(r"<[^>]+>", " ", page))
    for m in EMAIL_RE.finditer(text): found.add(m.group(0))
    for m in OBF_RE.finditer(text):
        dom = re.sub(r"\s*(?:\[dot\]|\(dot\)|\sdot\s)\s*", ".", m.group(2), flags=re.I).replace(" ", "")
        found.add(f"{m.group(1)}@{dom}")
    for m in re.finditer(r'"email"\s*:\s*"([^"]+)"', page): found.add(m.group(1).replace("mailto:", ""))
    return {e.strip().lower().rstrip(".") for e in found if e and "@" in e and not any(j in e.lower() for j in JUNK)}

def main():
    url = sys.argv[1]; listing_phone = re.sub(r"\D", "", sys.argv[2])[-10:] if len(sys.argv) > 2 else ""
    if not url.startswith("http"): url = "https://" + url
    host = urllib.parse.urlparse(url).hostname or ""
    out = {"website": url, "host": host, "copycat_risk": any(host.endswith(h) for h in FREE_HOSTS),
           "emails": {}, "booking": {"online": False, "evidence": []}, "phones": [], "fake_555": [],
           "phone_matches_listing": None, "pages_read": [], "could_not_read": []}
    queue, seen = [url], set()
    while queue and len(out["pages_read"]) < 8:
        u = queue.pop(0)
        if u in seen: continue
        seen.add(u)
        try: final, page = fetch(u)
        except urllib.error.HTTPError as e:
            if e.code != 404: out["could_not_read"].append({"page": u, "why": f"HTTP {e.code}"})
            continue
        except Exception as e:
            out["could_not_read"].append({"page": u, "why": str(e)[:80]}); continue
        if final in out["pages_read"]: continue
        low = page.lower()
        if ("just a moment" in low and "cloudflare" in low) or "captcha" in low[:20000]:
            out["could_not_read"].append({"page": u, "why": "bot check"}); continue
        out["pages_read"].append(final)
        if len(re.sub(r"<[^>]+>", "", page).strip()) < 400: out["could_not_read"].append({"page": final, "why": "page renders with scripts; open it in the browser"})
        for e in emails_in(page): out["emails"].setdefault(e, final)
        hrefs = re.findall(r'href=["\']([^"\']+)["\']', page, re.I)
        for h in hrefs:
            hl = h.lower(); absu = urllib.parse.urljoin(final, h); ah = urllib.parse.urlparse(absu)
            if any(b in hl for b in BOOKING_HOSTS) or (ah.hostname == urllib.parse.urlparse(final).hostname and any(ah.path.rstrip("/").endswith(p) or ah.path.startswith(p + "/") for p in BOOKING_PATHS)):
                out["booking"]["online"] = True; out["booking"]["evidence"].append(absu[:120])
            if ah.hostname == urllib.parse.urlparse(final).hostname and any(k in ah.path.lower() for k in ("contact", "about", "team")) and absu not in seen and len(queue) < 12:
                queue.append(absu.split("#")[0])
        text = html.unescape(re.sub(r"<[^>]+>", " ", page)).lower()
        for w in BOOKING_WORDS:
            if w in text: out["booking"]["online"] = True; out["booking"]["evidence"].append(f'"{w}" on {final}')
        for m in PHONE_RE.finditer(re.sub(r"<[^>]+>", " ", page)):
            num = "".join(m.groups())
            if num not in out["phones"]: out["phones"].append(num)
            if m.group(2) == "555": out["fake_555"].append(num)
        for guess in ("/contact", "/contact-us", "/contactus", "/about", "/about-us"):
            g = urllib.parse.urljoin(url, guess)
            if g not in seen and g not in queue and len(queue) < 12: queue.append(g)
    if listing_phone: out["phone_matches_listing"] = listing_phone in out["phones"]
    out["booking"]["evidence"] = sorted(set(out["booking"]["evidence"]))[:6]
    out["fake_555"] = sorted(set(out["fake_555"]))
    print(json.dumps(out, indent=1))

if __name__ == "__main__":
    main()
```
