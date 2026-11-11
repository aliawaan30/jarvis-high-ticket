---
name: caller-lead-finder
description: The complete blueprint of the Caller Lead Finder, the part of my Lead CRM app that finds local businesses losing phone calls so I can build them an AI receptionist and sell it. Read this skill before building or changing anything in that finder, and build only when asked, one piece at a time.
---

# Caller Lead Finder, the blueprint

This lives inside the Lead CRM app. One search prints 40 to 50 real businesses nearby, keeps the ones with a phone number, works out when they shut, and saves them into the Leads list through save_lead.

Rules for using this skill:
- Never build the whole thing in one go. The student asks for one piece at a time. Build exactly the piece they name, nothing more.
- If a request conflicts with this blueprint, follow the blueprint and say so.
- The Google key lives in a Secret and is never shown on any page or in any reply.
- Nothing writes into the Leads list except save_lead. Never write to it directly.

## The pieces

### Piece 1: the search (backend function: search_callers)
- Inputs: business_type (like "plumber") and suburb (like "Springvale VIC").
- Calls Google Places API (New) Text Search using the GOOGLE_PLACES_API_KEY secret, server side only.
- Runs FOUR query variations: "[type] in [suburb]", "[type] services in [suburb]", "[type] company in [suburb]", "[type] business in [suburb]".
- Pulls up to 3 pages of results per variation.
- Combines everything and removes duplicates by google_place_id.
- For each business returns: name, phone, address, rating, review count, opening hours, google_place_id.
- THE FILTER THAT IS THIS BUSINESS: keep only results that have a phone number. A business with no phone cannot miss a call, so it is not a lead for this service.
- Typical result: 40 to 50 unique businesses per search before the filter.

### Piece 2: the closing-time read
- For every kept business, read the opening hours and work out the earliest weekday closing time.
- Save that as closes_at, in plain 24 hour text like "17:00". If Google gives no hours at all, save "unknown".
- Set gap from the hours:
  - "closes early" when the earliest weekday close is 17:00 or before
  - "closed weekends" when Saturday and Sunday are both shut
  - "unknown hours" when Google has no hours
  - "open late" when they trade past 17:00 every weekday
- Tag lead_quality "hot" when the business has 10 or more reviews AND a rating of 4.0 or higher AND gap is not "open late". Otherwise "normal".
- Nothing gets dropped for being "open late". A business that trades late still misses calls when everyone is on a job. The tag just says who to call first.

### Piece 3: the smart suburb box (backend function: autocomplete_suburb)
- As the student types a suburb, suggest real suburbs using Google Places Autocomplete.
- Start suggesting after 2 characters. Debounce so it does not fire on every keystroke.

### Piece 4: feeding the CRM
- Every kept business goes into the Leads list by calling save_lead, one at a time.
- service is always "caller". gap is the gap worked out in piece 2. source is "caller finder".
- Also pass closes_at through so it is stored on the lead.
- save_lead handles duplicates. The finder never checks for them itself and never writes to the list directly.
- After a run, report back: how many businesses Google returned, how many had a phone number, how many were new, how many already existed.

### Piece 5: the search screen
- One page inside the Lead CRM app. Two boxes: business type, and suburb (powered by autocomplete_suburb). A Search button.
- While it runs, show what it is doing. When it finishes, show the four numbers from piece 4 and a link through to the Leads screen.
- Plain and easy to read. No dashboard, no charts.

### Piece 6: the secret shop record
- Two extra fields on a lead: secret_shop_result, one of "no answer", "voicemail", "answered", or empty until it is tried, and secret_shop_date.
- On the Leads screen, a one-click control to set secret_shop_result, which stamps secret_shop_date with today.

## The secret
- GOOGLE_PLACES_API_KEY holds the student's own Google key. Backend functions read it. Nothing else ever does. It never appears in a page, a reply, or a log.

## Never do
- Never invent businesses, phone numbers or opening hours. Everything comes from the live Google results.
- Never write into the Leads list except through save_lead.
- Never drop a business for trading late without being asked. Late traders still miss calls.
- Never guess a closing time. If Google has no hours, gap is "unknown hours" and the student finds out by calling.

Once it's saved, play the blueprint back to me in one short paragraph so I know you've got the whole machine. Don't build anything yet.
