---
name: walkthrough-lead-finder
description: The complete blueprint of the Walkthrough Lead Finder, the part of my Lead CRM app that finds real estate agents with properties listed and no video, so I can sell them walkthrough videos. Read this skill before building or changing anything in that finder, and build only when asked, one piece at a time.
---

# Walkthrough Lead Finder, the blueprint

This lives inside the Lead CRM app. It is deliberately half automatic and half done by hand, and that is not a shortcut.

Why: property listing sites block apps from reading their listings, and their terms do not allow it. Anything that claims to scrape them stops working. So the app finds the agencies, and the student looks at the listings themselves.

Rules for using this skill:
- Never build the whole thing in one go. The student asks for one piece at a time. Build exactly the piece they name, nothing more.
- If a request conflicts with this blueprint, follow the blueprint and say so.
- Never suggest scraping a property site, and never build anything that reads one. If the student asks, explain why and offer this instead.
- Nothing writes into the Leads list except save_lead.

## The pieces

### Piece 1: the agency search (backend function: search_agencies)
- Input: suburb.
- Calls Google Places API (New) Text Search using the GOOGLE_PLACES_API_KEY secret, server side only, with the query "real estate agency in [suburb]".
- Pulls up to 3 pages. Returns name, phone, address, website, rating, review count and google_place_id.

### Piece 2: feeding the CRM
- Every agency found goes into the Leads list by calling save_lead. service is "walkthrough", source is "agency finder", gap is "not checked yet".
- Report how many were new and how many already existed.

### Piece 3: the listing fields
- Three extra fields on a lead: agent_name, listing_address, listing_url.
- save_lead accepts all three, following its usual rules: only update what is passed in, never wipe anything, never touch status or notes.
- Show all three on the lead panel.

### Piece 4: adding a listing from a paste
- The student pastes a property address, an agent name and an agency. It goes in through save_lead with service "walkthrough" and gap "no video on listing".
- If that agency is already a lead, add the agent name and listing to the existing lead rather than creating a second one.
- Confirm back what was added or updated.

### Piece 5: finding the agent
- For a walkthrough lead with an agent_name, look up that agent's own public profile on their agency site and find their direct phone or email.
- Save what is found through save_lead. If nothing is public, write "not found". Never guess a number.

### Piece 6: the weekly reminder
- Every Sunday evening, remind the student to spend 20 minutes checking new listings for missing video.
- Include how many walkthrough leads they have and how many they have contacted.

## Never do
- Never read, scrape or crawl a property listing site, whatever the student asks.
- Never invent an agent, a phone number or a property address.
- Never write into the Leads list except through save_lead.

Once it's saved, play the blueprint back to me in one short paragraph so I know you've got the whole machine. Don't build anything yet.
