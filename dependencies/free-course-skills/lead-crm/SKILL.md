---
name: lead-crm
description: The complete blueprint of the Lead CRM app, the one place every business I might contact lives, whichever service I sell. Read this skill before building or changing anything in that app, and build only when asked, one piece at a time.
---

# Lead CRM, the blueprint

This is the one list. Every business found by any finder ends up here, gets worked, and never gets lost or rung twice.

Rules for using this skill:
- Never build the whole app in one go. The student asks for one piece at a time. Build exactly the piece they name, nothing more.
- If a request conflicts with this blueprint, follow the blueprint and say so.
- The student's own notes and status are sacred. Nothing automatic ever overwrites them.

## The pieces

### Piece 1: the Leads list
Each row is one business. Fields:
- business_name, phone, email, website, address, suburb
- category, the kind of business it is
- google_place_id, Google's own ID for that business, unique
- rating, review_count
- service, which of my three services this lead is for: "website", "caller" or "walkthrough"
- gap, one short line on what they are missing
- status, one of: new, calling, called, interested, not interested, sold
- last_contacted, a date
- notes, a long text box
- source, where the lead came from
New rows always start at status "new".

### Piece 2: save_lead, the one door in
A backend function. Everything that adds a lead goes through this and nothing else.
It takes: business_name, phone, email, website, address, suburb, category, google_place_id, rating, review_count, service, gap, source.
How it behaves:
1. No row with that google_place_id yet, add a new one with status "new".
2. A row already exists, update it, but only the fields actually passed in. If a field is not passed, leave what is already there. Never wipe a field by passing nothing.
3. Never touch status, notes or last_contacted. Those belong to the student.
4. Report back whether it added a new one or updated an existing one.

### Piece 3: the screen
A table of every lead showing business name, phone, suburb, service, status and when they were last contacted.
At the top, a search box for the business name and buttons to filter by status and by service.
Status can be changed straight from the table without opening anything. Clicking a row opens it so notes can be read and written.
Sort so leads that have not been contacted come first.
It has to work on a phone, because the student reads it while they are on calls.

### Piece 4: the nightly job
An automation that runs every night, brings in new businesses through save_lead, and reports in the morning: how many new leads, and which suburb.

### Piece 5: enrichment
For leads that have not been enriched yet, look at what is public about them and add short notes: whether they have a website and whether it looks old, whether they are on social media and when they last posted, what their reviews say, and one specific thing worth mentioning on a call.
Six lines maximum per lead. Never invent anything. "Not found" is a fine answer.

## Never do
- Never invent a business, a phone number or a review. Everything comes from real results.
- Never add a lead by any route other than save_lead.
- Never overwrite the student's status or notes.
- Never let the same business appear twice.

Once it's saved, play the blueprint back to me in one short paragraph so I know you've got the whole machine. Don't build anything yet.
