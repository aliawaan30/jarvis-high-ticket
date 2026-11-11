---
name: website-lead-finder
description: The complete blueprint of the Website Lead Finder, the part of my Lead CRM app that finds local businesses with no website so I can build them one and sell it. Read this skill before building or changing anything in that finder, and build only when asked, one piece at a time.
---

# Website Lead Finder, the blueprint

This lives inside the Lead CRM app. One search prints 40 to 50 real businesses nearby, throws away everyone who already has a website, and saves the rest into the Leads list through save_lead.

Rules for using this skill:
- Never build the whole thing in one go. The student asks for one piece at a time. Build exactly the piece they name, nothing more.
- If a request conflicts with this blueprint, follow the blueprint and say so.
- The Google key lives in a Secret and is never shown on any page or in any reply.
- Nothing writes into the Leads list except save_lead. Never write to it directly.

## The pieces

### Piece 1: the search (backend function: search_websites)
- Inputs: business_type (like "plumber") and suburb (like "Springvale VIC").
- Calls Google Places API (New) Text Search using the GOOGLE_PLACES_API_KEY secret, server side only.
- Runs FOUR query variations: "[type] in [suburb]", "[type] services in [suburb]", "[type] company in [suburb]", "[type] business in [suburb]".
- Pulls up to 3 pages of results per variation.
- Combines everything and removes duplicates by google_place_id.
- For each business returns: name, phone, address, rating, review count, opening hours, websiteUri, google_place_id.
- Typical result: 40 to 50 unique businesses per search before the filter.

### Piece 2: the filter that is this business
- Keep only results where websiteUri is missing or empty. Everyone with a website gets dropped.
- For each kept business set gap to "no website".
- Tag lead_quality "hot" when the business has 10 or more reviews AND a rating of 4.0 or higher. Otherwise "normal".

### Piece 3: the smart suburb box (backend function: autocomplete_suburb)
- As the student types a suburb, suggest real suburbs using Google Places Autocomplete.
- Start suggesting after 2 characters. Debounce so it does not fire on every keystroke.

### Piece 4: feeding the CRM
- Every kept business goes into the Leads list by calling save_lead, one at a time.
- service is always "website". gap is "no website". source is "website finder".
- save_lead handles duplicates. The finder never checks for them itself and never writes to the list directly.
- After a run, report back: how many businesses Google returned, how many had no website, how many were new, how many already existed.

### Piece 5: the search screen
- One page inside the Lead CRM app. Two boxes: business type, and suburb (powered by autocomplete_suburb). A Search button.
- While it runs, show what it is doing. When it finishes, show the four numbers from piece 4 and a link through to the Leads screen.
- Plain and easy to read. No dashboard, no charts.

## The secret
- GOOGLE_PLACES_API_KEY holds the student's own Google key. Backend functions read it. Nothing else ever does. It never appears in a page, a reply, or a log.

## Never do
- Never invent businesses or details. Everything comes from the live Google results.
- Never write into the Leads list except through save_lead.
- Never loosen the no-website filter without being asked. A business with a website is not a lead for this service.

Once it's saved, play the blueprint back to me in one short paragraph so I know you've got the whole machine. Don't build anything yet.
