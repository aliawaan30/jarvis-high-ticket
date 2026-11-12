---
name: jarvis-hq
description: HQ, the business record, kept in the member's Agency HQ app (their CRM). Use whenever reading or writing offer, accounts, touches, deals, calls, proposals, clients, missions or weekly numbers, and when setting up or moving HQ.
---

# HQ: the business record

HQ is the member's whole business in one place. Every skill reads from it and writes back to it. Chat memory holds who the member is. HQ holds the business.

## Where HQ lives
1. Home: the member's Agency HQ app, their CRM, which you build for them from the build spec in the appendix below, inside an empty app they create (you cannot create apps yourself). You read and write it through cross-app access, with "Update data" on. The member sees everything you write: the pipeline, each lead's call card and timeline, the dashboard and results.
2. Until Agency HQ is connected: keep the same tables in your own Data area, so nothing waits.
3. Moving in (mission 4): when the member has copied Agency HQ and given you access, copy every row from your Data area into the matching Agency HQ table, check the counts match table by table, then tell the member in one line. If any count does not match, stop, keep both copies, and say which table differs. If the member has more than one Agency HQ copy, ask which one is theirs before writing anything. Keep your Data area copy for 7 days, then ask before clearing it.
4. Never read into, change or delete records whose name or note starts with SAMPLE. They are the CRM's example data. Create your own rows instead.
5. Names: Agency HQ uses one word entity names and snake_case fields. Map by meaning: Accounts is Account, Touches is Touch, Deals is Deal, Campaigns is Campaign, Clients is Client, Numbers is WeekNumbers, Missions is Mission; Offer, Funnel, Calls and Proposals keep their names. "Owner name" is owner_name, and so on.
5b. If the member already has an Agency HQ app (an app you have access to with an Account table, often named "Agency HQ" or "Jarvis HUD"), that app is HQ. Use it exactly as it is: never build, rebuild, redesign or edit it, and never ask for an empty app. Any HQ table that app does not have (for example Offer, Funnel, Calls, Proposals), keep in your own Data area.
6. Building it (only when the member has no Agency HQ app yet): ask the member once, in one message: "Create a new empty app in Base44 called Agency HQ (don't type anything into it), then in my Agent Settings give me access to it. Tell me when it's done." Then build it from the build spec in two passes (pass 1, then pass 2), check every table and page in the spec exists, add the send-check backend function (jarvis-email-setup), fix anything missing, and only then say it is ready. Never add sample data.

## Setup

When the brain is first installed, use Agency HQ if it is already connected. Otherwise create these tables in your own Data area. Then ask only for what is missing to fill Offer and Numbers. Confirm with: "HQ ready: 11 tables." and list them.

## Tables

### Offer
The single offer brief every skill reads. One active row at a time. Old versions stay with active set to no.
Fields: version, active (yes or no), approved by member (yes or no, date), niche, buyer, problem, buyer awareness, desired outcome, solution, mechanism, deliverables, timeframe, risk reversal, proof (only real, with source), approved claims, alternatives the buyer uses now, price and terms, value model, six line offer, delivery route (self build, developer, hybrid), research links, created date.

### Funnel
Everything the funnel skills build. One row per offer version.
Fields: offer version, landing page URL, application form URL, booking page URL, confirmation page URL, VSL status (none, script, filmed, live), fit rules, calendar link, pre-call sequence version, sender email, SMS sender, integration status (each item: tested, drafted, missing), notes.

### Campaigns
Every outreach or ad campaign, so another chat can pick it up.
Fields: name, can pay rule, opt out line, postal address, our domains, booking page, send window, type (outreach, cold call, email, Meta ads, other), sending method (level 1 or 2), sending inboxes, daily limit per inbox, warm up start date, DNS status, offer version, status (draft, approved, live, paused, done), audience, angle, daily limit, approved by member (yes or no, date), spend, leads, booked calls, cost per booked call, decision, reason, start date.

### Accounts
Businesses being targeted.
In an Agency HQ v2 app, save leads in the Account table with exactly these field names: business_name, niche, city, state, country, time_zone, entity_type, phone, website, owner_name, owner_source_url, owner_linkedin_url, company_linkedin_url, email, email_status (published, verified, risky, invalid, contact form only, none published), email_allowed, call_allowed, channel_reason, tier (A, B, C), can_pay_score, problem_score, reachable_score (1 to 5), signals (one per line as "what you saw | source link"), status, source (search, or activity: ads, hiring, growing, permits, new company), campaign, value_estimate (rough yearly value in dollars), call_card, call_card_date, next_action, next_action_date, last_touch_date, notes. Save each lead as soon as it passes the checks, one at a time, so it appears in the member's pipeline while you work, and read it back to confirm. One value per field: phone holds exactly one number (the best one, as written, for example (214) 725-2291) and email holds exactly one address, with nothing else in either field; put other numbers, other emails, sources and explanations in notes. The app's Call button dials the phone field as it is.
Settings: an Agency HQ v2 app has an AgencySettings table (postal_address, opt_out_line, booking_page, daily_cap, send_window_start, send_window_end, brief_time, working_hours, inbox_email, do_not_contact). Read campaign settings from it before asking the member, and write inbox_email when an inbox is connected.
Fields: business name, niche, city, state, country, time zone (IANA), entity type (company, sole trader or partnership, unknown), channels allowed (email, call, each yes or no with reason), tier (A, B, C), phone, website, owner name, owner email, source, reason to contact now, reason source link, signal date, first message draft, size evidence, can pay score, problem score, reachable score, owner name, owner source, owner LinkedIn URL, company LinkedIn URL, contact source, email status (published, verified, risky, invalid), signals with source, referrer, watchlist (yes or no), last checked, score (1 to 5), status (new lead, contacted, replied, call booked, call done, proposal sent, won, lost, not now, do not contact). Use only these exact values, the same as the Agency HQ pipeline columns. A drafted first message does not change the status; it is a Touch with status draft, consent email (yes, no, unknown), consent SMS (yes, no, unknown), last touch date, last touch outcome, touches this week, last reply, reply class, last text, SMS consent source, call card, call card date, notes.

### Touches
Every outreach touch and reply, so the lead's timeline is complete.
Fields: account, date, created time, channel (email, call, text, linkedin, note), direction (out, in), status (planned, draft, sent, received, logged, cancelled), step (email 1, email 2, call 1, email 3, last call, call now, or blank), due date, summary, full text, outcome, gate result, cancelled reason.

### Deals
Every sales opportunity.
Fields: business (links to Accounts), contact name, stage (call one booked, call one done, proposal sent, won, lost), booked via channel, booked via signal, call one date, call two date, problem cost per year, problem cost confirmed (yes or no), proposed price, next action, next action date, lost reason, links (brief, solution design, proposal, demo).

### Calls
Every sales call.
Fields: deal, type (call one, call two, other), date, recorded (yes or no), everyone told it was recorded (yes or no), summary, number agreed, objections, review score, one change for next time.

### Proposals
Fields: deal, version, status (draft, presented, accepted, declined), build price, monthly running cost, timeline, link.

### Clients
Won work being delivered.
Fields: business, deal, build route, developer, milestones, current milestone, go live date, support end date, retainer (yes or no), case study (yes or no).

### Missions
One row per mission from jarvis-missions.
Fields: number, name, status (locked, active, done), started date, done date, proof link.

### Numbers
One row per week.
Fields: week start, daily lead quota, new accounts added, target calls, calls booked, calls held, proposals sent, deals won, cash collected, ad spend, notes.

## Rules

1. Write first, then reply. If something changes in chat, update HQ before answering.
2. Never delete rows in bulk. Mark them instead. Ask before deleting anything. When the member asks to delete a lead, delete its Touches with it, and keep its email and domain on the do not contact list if it was marked do not contact.
3. A contact marked do not contact stays that way through every import and every campaign.
4. Numbers come from actual events in HQ, never from estimates.
5. Every date is plain text, YYYY-MM-DD, in the student's timezone.
6. Every reason to contact has a source link. No source, no reason.
7. Never change the active Offer row with your own suggestions. Proposed changes go into a new Offer version with active set to no, every proposed field marked "proposed". It only becomes active when the member says yes. Guarantees, risk reversals, prices and delivery times always need the member's explicit yes.

---

## Appendix: agency hq build
(Formerly the appendix "agency hq build" below.)

### Build spec: Agency HQ (student CRM)

Paste this whole file into the Base44 app builder of an empty app named "Agency HQ". Build it in two passes (see the end). Design values are taken from the Agency Builder CRM so the look matches exactly. No sample data anywhere.

---

## 1. Design system

### Colours (light)
| Token | Value | Use |
|---|---|---|
| bg | #FAFAF9 | page background |
| side | #F3F3F1 | sidebar, board column background |
| surface | #FFFFFF | cards, tables, drawer, inputs |
| surface-2 | #F7F7F5 | table header, group rows |
| hover | #F0F0ED | hover background, segmented control track |
| ink | #1B1B1A | main text, primary button background |
| ink-2 | #46463F | nav text |
| muted | #74746D | secondary text, labels |
| faint | #A6A69F | counts, placeholders, empty column text |
| line | #E5E5E1 | borders |
| line-2 | #EEEEEA | row dividers inside tables and stat strips |
| accent | #2D4FC4 | focus, active filters, links, the one action colour |
| accent-soft | #ECF0FC | focus ring, active filter background, drop target |
| won | #1F7A4E / soft #E6F3EC | won, success, connected |
| lost | #B4433A / soft #F9EAE8 | lost, danger, overdue |
| warn | #9C620E / soft #FAF1E0 | due soon, warnings |
| pop shadow | 0 1px 2px rgba(0,0,0,.05), 0 10px 30px rgba(0,0,0,.12) | drawer, modal |

### Colours (dark, follow the system setting, with a manual toggle)
bg #151514, side #101010, surface #1B1B1A, surface-2 #20201E, hover #262624, ink #EDEDEA, ink-2 #CACAC4, muted #98988F, faint #6E6E68, line #2B2B28, line-2 #232321, accent #90A8FF, accent-ink #0E1430, accent-soft #1F2744, won #62C898 / #15291F, lost #F08C82 / #2E1816, warn #E2B064 / #2A2212, pop shadow 0 1px 2px rgba(0,0,0,.4), 0 12px 34px rgba(0,0,0,.5).

### Type
1. Font: Geist (weights 400, 500, 600), fallback system-ui.
2. Body 13.5px, line height 1.45, tabular numbers everywhere.
3. Page title 18px, weight 600, letter spacing -0.011em.
4. Secondary text 12.5px muted. Small labels and counts 12px.
5. Stat numbers 22px, weight 600, letter spacing -0.02em.

### Shape and spacing
Radius: buttons and inputs 7px, cards 7px, lists and tables 9px, modal 12px, tags 4px, avatars round. Borders always 1px. Content padding 22px 28px, max width 1340px. Gaps are small: 6 to 10px between related items, 16px between blocks.

---

## 2. Components

1. Button: height 32px, padding 0 12px, radius 7px, 1px line border, surface background, weight 500. Primary: ink background, bg-coloured text. Ghost: no border, transparent. Small: 28px high, 13px text. Danger: lost-coloured text.
2. Input, select, textarea: surface background, 1px line border, radius 7px, padding 7px 10px. Focus: accent border plus 3px accent-soft ring.
3. Segmented control: track in hover colour, radius 7px, padding 2px; buttons 13px weight 500 muted; selected one on surface with a 1px line ring.
4. Tag: height 19px, padding 0 6px, radius 4px, 11.5px weight 500, background is the tag colour at 12 percent, text the tag colour.
5. Avatar: 24px circle (40px large), initials 10.5px weight 600, tinted background.
6. Dot: 7px circle, faint by default, won colour when good.
7. Pipeline column: 250px wide, header with name (weight 500), count (faint) and value sum (muted, right). Column body: side background, radius 9px, padding 4px, gap 6px, min height 140px; accent-soft while dragging over.
8. Pipeline card: surface, 1px line border, radius 7px, padding 9px 10px. Top row: business name (weight 500) and avatar. Second line: owner name muted 12.5px. Tags row. Footer: value on the left, next action date on the right (lost colour if overdue, warn if today).
9. Table: header 34px, surface-2 background, 12.5px muted weight 500, sortable; cells padding 9px 12px, line-2 dividers, inside a list container with 1px border and 9px radius.
10. Stat strip: one bordered row of 4 stats, each with a 12.5px muted label and a 22px number, divided by line-2.
11. Drawer: fixed on the right, width 470px (full width on phones), surface, left border, pop shadow, slides in. Closes on Escape and on the background.
12. Modal: surface, radius 12px, width up to 520px, pop shadow.
13. Toast: bottom centre, ink background, bg-coloured text, radius 8px, optional Undo.
14. Empty state: centred, 36px padding, a one line title in ink and one line in muted, with one action.

---

## 3. Layout

1. Two columns: sidebar 224px, main area fills the rest. When Ask Jarvis is open, a third column of 380px on the right.
2. Sidebar (side background, right border, padding 10px 8px):
   a. App mark and name "Agency HQ" at the top.
   b. Navigation: Dashboard, Results, Pipeline, Leads, Campaigns, Clients, with counts on the right. Links 6px 8px padding, radius 6px, ink-2; the current page sits on surface with a 1px line ring.
   c. "Saved views" heading (12px faint), then coloured dot links: Call now, Hot, Going cold, Overdue, No next step.
   d. At the bottom: the owner's name, a theme toggle (auto, light, dark).
3. Top bar: sticky, slightly blurred bg, bottom border, padding 10px 28px. Search (max 380px, shows "/" shortcut), then on the right "Ask Jarvis" (button) and "New lead" (primary).
4. Page header: title 18px, a muted meta line beside it, actions on the right.
5. Phones: the sidebar becomes a horizontal scrolling bar at the top, tables scroll sideways inside their box, the drawer is full width, the stat strip becomes 2 by 2.

---

## 4. Data (entities)

All dates are plain text in YYYY-MM-DD, entered from a short list of days, never a date picker. Status lists are fixed.

1. Account: business_name, niche, city, state, country, entity_type (company, sole trader, unknown), phone, website, owner_name, owner_source_url, owner_linkedin_url, company_linkedin_url, email, email_status (published, verified, risky, invalid), email_allowed (yes, no), call_allowed (yes, no), channel_reason, tier (A, B, C), can_pay_score, problem_score, reachable_score (1 to 5), signals (text, one per line, written as: label | source link, for example: Running Google Ads | https://example.com; charts and tags use only the label), status (new lead, contacted, replied, call booked, call done, proposal sent, won, lost, not now, do not contact), source (Money Map, Funnel application, Inbound, Referral), value_estimate (number), call_card (text), call_card_date, next_action, next_action_date, last_touch_date, notes.
2. Touch: account, date, channel (email, call, text, linkedin, note), direction (out, in), status (planned, draft, sent, received, logged, cancelled), step (email 1, email 2, call 1, email 3, last call, call now), due_date, summary, full_text, outcome, gate_result, cancelled_reason.
3. Deal: account, stage (call booked, call done, proposal sent, won, lost), problem_cost_per_year, problem_cost_confirmed (yes, no), proposed_price, booked_via_channel (email, call, linkedin, funnel, referral), booked_via_signal (the label of the signal that led to the booking), next_action, next_action_date, call_brief, call_review, solution_design, proposal_link.
4. Campaign: name, status (draft, approved, live, paused, done), can_pay_rule, daily_limit, opt_out_line, postal_address, our_domains, booking_page, send_window, sent, replies, booked.
5. Client: business, deal, stage (Kickoff, Build, Test, Handover, Live), go_live_date, retainer (yes, no), notes.
6. WeekNumbers: week_start, target_calls, calls_booked, proposals_sent, deals_won, cash_collected.
8. Mission: number, name, status (locked, active, done), started_date, done_date, proof_link. The 19 names, in order: Jarvis 2.0 is live; Goal set; First 10 leads; Your CRM is ready; Niche and problem picked; Offer approved; Funnel live; The Money Map; Sending ready; First 6 of 6 email; First campaign live; First 10 calls; First reply handled; First call booked; First sales call held; First proposal sent; First client signed; Build kicked off; Client live.
7. Offer, Funnel, Calls, Proposals: as in the Jarvis 2.0 HQ, stored here so Jarvis has one home. No pages needed for these in the first version beyond read only views inside the lead drawer and Clients.

---

## 5. Pages

1. Dashboard: "what do I do today?". One screen, no scrolling on a laptop, nothing else on it:
   a. Mission bar: "Mission [n] of 19: [name]" with a progress bar (Mission table).
   b. Today, three lists side by side on desktop, stacked on phones: Call now (replied with interest, or a planned call due today, inside calling hours; each row opens straight to the call card), Replies waiting, Due today (built from planned Touches due today or overdue, each row naming the step, for example "Send email 2 to Lawson" or "Call Coastline"). Each list shows at most 5 rows and a "See all" link.
   c. This week: three numbers against target: calls booked, proposals sent, cash collected.
   d. One chart: calls booked per week, last 8 weeks, bars with the weekly target as a faint line drawn only for weeks that have a WeekNumbers row (no line, not zero, for weeks without one), one line takeaway under it ("On track" or how many short).
1b. Results: "what's working?", its own page in the sidebar under Dashboard:
   a. The funnel: leads, contacted, replied, call booked, proposal sent, won, as horizontal bars with the conversion percentage between steps.
   b. What's working: booked calls by signal and by channel, from the Deal's booked_via_signal and booked_via_channel.
   c. Pipeline value by stage.
   d. Cash collected by month, last 6 months.
   Each chart has a one line takeaway. When values tie, say so ("Oct and Nov tied at $4.5k"). Accent colour for the main series, green for won, faint grey for targets, no pie charts, no 3D, numbers labelled, a calm empty state when there is no data.
   All counts and charts leave out accounts marked do not contact.
2. Pipeline: board of Accounts by status, columns new lead, contacted, replied, call booked, call done, proposal sent, won, lost. Drag a card to change status, which also writes a Touch with channel "note" and the change. Filters above the board: Tier, Source, Signal (contains), Going cold. Board and List toggle.
3. Leads: table of Accounts with search, the same filters and sort (name, business, tier, status, next action date). Clicking a row opens the drawer.
4. Lead drawer, top to bottom: business name and status; owner with a link to where they were found; tier and the three scores as small bars; contact (phone as a tap to call link, email with its status tag, the owner's and company's LinkedIn links if found, channels allowed and the reason); signals as a list, each with its source link; the call card (latest, with its date, in a box with a Copy button); the outreach plan (the lead's planned steps in order, each with its due date and a status tag: done, due today, upcoming, overdue or cancelled with its reason); next action and date (editable); timeline of Touches, newest first, each expandable to its full text, drafts marked as drafts; and, when there is a deal, links to its call brief, call review, solution design and proposal. Buttons: Add note, Log call (outcome list: no answer, voicemail, gatekeeper, call back, booked, not interested, do not call), Do not contact (asks to confirm, cannot be undone from here). Under a "More" menu, kept out of the way: Delete lead (asks to confirm, names the business, deletes the lead and all its Touches; if the lead was marked do not contact, keep its email and domain on the do not contact list).
5. Saved views: Call now, Hot (tier A, not contacted or replied), Going cold (no touch in 7 days and still open), Overdue (next action date before today), No next step.
6. Campaigns: table with name, status, daily limit, sent, replies, booked, and results by signal in the row's detail.
7. Clients: board by Kickoff, Build, Test, Handover, Live, cards with business, go live date and retainer.
8. Ask Jarvis: opens the right column with a short note and a button that opens the owner's Jarvis chat.
9. Settings (from the name at the bottom of the sidebar): opt out line, postal address, our domains, booking page, send window, do not contact list (help text: "Leads marked do not contact are never contacted again. This can't be undone in the app."), theme.

---

## 6. Rules
1. Private app: only the signed in owner can see anything.
2. No sample data, no fake numbers. Empty states explain what will appear and that Jarvis fills it.
3. Do not contact can only be set, never cleared, from the app.
4. Every list and board loads fast with a few thousand accounts.
5. Text never touches the screen edge on phones; tap targets at least 40px.

---

## 7. How to build (two passes)
Pass 1: sections 1, 2, 3, the entities in section 4, and the Pipeline, Leads and the lead drawer from section 5.
Pass 2: Dashboard, Results, saved views, Campaigns, Clients, Ask Jarvis and Settings.
After each pass: check light and dark mode, a phone width, an empty state, and dragging a card.
