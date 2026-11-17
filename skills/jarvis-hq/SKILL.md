---
name: jarvis-hq
description: HQ, the business record, kept in the member's Agency HQ app (the Jarvis HUD and CRM) plus a few tables in Jarvis's own Data area. Use whenever reading or writing offer, accounts, touches, deals, calls, proposals, clients, missions, settings or weekly numbers, and when installing, checking or moving HQ.
---

# HQ: the business record

Version: 2026-11-18.1 (matches Agency HQ app v3.15)

HQ is the member's whole business in one place. Every skill reads from it and writes back to it. Chat memory holds who the member is. HQ holds the business.

## Where HQ lives

1. **The Agency HQ app** (also called the Jarvis HUD). The member installs it from the Agency HQ package in the course. You read and write it through cross-app access, with "Update data" on. The member sees everything you write: the HUD, the pipeline, each lead's page, campaigns, clients, results.
2. **Your own Data area** holds the HQ tables the app does not have: Offer, Funnel, Calls and Proposals, plus any extra fields described under "Extra fields" below. The member does not see these in the app; show them in chat when asked.
3. **Until the app is installed:** keep every HQ table in your Data area so nothing waits. Move in when the app is ready (see "Moving in").
4. Never build, rebuild, redesign or edit the Agency HQ app, its tables, pages or functions, and never add fields to it. If something in the app is broken or missing, use "Checking the app" below.
5. Never read into, change or delete records whose name or note starts with SAMPLE.
6. If the member has more than one Agency HQ or Jarvis HUD app, ask which one is theirs before writing anything, then save its name and app ID in memory.

## Installing the app (guide the member, step by step)

Explain each step in plain words before they do it, one step per message, as jarvis-2-brain says. What they will meet, and what to tell them:
1. **No blank-app button.** Give them this to send in the Base44 build box: "Create an empty app named Agency HQ. Only a single blank placeholder page. Do not add features, entities or designs yet. I will install a package next."
2. **"Install packages" card:** "Base44 asks before adding code libraries. That's normal. Press Approve."
3. **"Approve (2)" to test functions:** "It wants to test two functions that can change records. The app is empty, so it's safe. Press Approve."
4. **"Set secrets" form with 5 fields:** "Press Skip. You don't have these yet; we add them in your HUD in a minute."
5. **If the published app shows a raw error** like {"status":500...}: give them this for the builder: "The published app shows only a 500 error on every page. The preview works. Fix only this so the published app opens. Do not redesign anything and do not publish." Then publish twice again. (Fixed in v3.16; it should not happen.)


You cannot create or install apps. The member does it in the Base44 builder; you guide them one step at a time and check each step before the next.

1. Ask them to create a new empty app in Base44 named "Agency HQ" (or open their existing Jarvis HUD app, which is upgraded in place).
2. In that app's builder chat, they attach the Agency HQ package zip from the course lesson and paste the install prompt from the same lesson, in one message.
3. Ask them to send you a screenshot of the builder's report. Check it shows: 19 tables, 20 functions deployed (none returning 404, including connections, sendCheck, retellWebhook and jarvisVoice), the "Jarvis after-call execution bridge" workflow active, and the build passing. If anything is missing, write them the exact follow-up message for the builder ("Deploy the [function] function exactly as written, then report its status") and check again. Do not move on until all four are confirmed.
4. They publish, then publish again. Connections needs the published app.
5. Connections, in the app's Settings (v3.15). Every key has a ? that explains it, so keep your guidance short.
   1. **Jarvis access (required):** in your Agent settings, Developer, Create access token: One app or Superagent, the entry with the Agent badge, Full access. They paste it in Connections and press Save.
   2. **HUD key (required, automatic):** the app creates it. They press Get it for Jarvis, then Copy, and paste it to you. Base44 may auto-save it under its own name (for example AGENCY_HQ_HUD_KEY). Any secret whose name contains HUD_KEY is the HUD key: use it, confirm in one line ("Got your HUD key. Saved."), and never ask for it again or show a second secrets form. Only if no such secret exists, ask them to send it again.
   3. **Check the link:** ask them to press Test Jarvis connection under Jarvis access. "Jarvis is connected" means Message Jarvis and Talk will work. Any other result tells them exactly what to fix.
   4. **Live voice (Retell add-on, optional):** they paste their Retell key, press Test key, then Set up my voice. The app builds the voice agent itself. Only fall back to retell-setup.md if the button reports a problem. Without Retell, Talk works with the Base44 voice.
   5. Keys already in Base44 Secrets keep working and take priority. Never ask the member to paste a key into chat, except the HUD key handover above.
6. In the published app's Settings they add your agent ID and their name, and choose a voice provider (Base44 if they have no Retell account).
7. They give you cross-app access to the app (Agent settings, General). Save its app ID in memory as "Agency HQ app ID".
8. Then run "Checking the app". Only say it is ready when the check passes.

## Checking the app

Run this after install, after any update, and whenever a write fails.
1. Read each table you use: Account, Touch, Deal, Campaign, Client, Mission, WeekNumbers, AgencySettings, Profile, Task. Each must exist and accept a read. Vault is locked to the app itself; you cannot and should not read it.
2. Write one test Task with title "HQ check", read it back, then mark it done.
3. If a read or write fails: check cross-app access first, then "Update data", then the app ID in memory. Fix what you can, and walk the member through what only they can do. If a table or function is missing, give them the exact message for the app builder. Never fix the app yourself.

## Moving in

When the app is ready and you hold rows in your Data area for tables the app has (Account, Touch, Deal, Campaign, Client, Mission, WeekNumbers), copy every row into the app, check the counts match table by table, then tell the member in one line. If any count does not match, stop, keep both copies, and say which table differs. Keep your Data area copy for 7 days, then ask before clearing it. Offer, Funnel, Calls and Proposals stay in your Data area.

## Tables in the app

Field names are exact. Use only the listed values for fields with a fixed list.

1. **Account** (businesses being targeted; every lead goes here): business_name, niche, city, state, country, time_zone, entity_type, phone, website, owner_name, owner_source_url, owner_linkedin_url, company_linkedin_url, email, email_status (published, verified, risky, invalid, contact form only, none published), email_allowed, call_allowed, channel_reason, tier (A, B, C), can_pay_score, problem_score, reachable_score (1 to 5), signals (one per line: "what you saw | source link"), status (new lead, contacted, replied, call booked, call done, proposal sent, won, lost, not now, do not contact), source, campaign, value_estimate, call_card, call_card_date, next_action, next_action_date, last_touch_date, notes.
   Save each lead as soon as it passes the checks, one at a time, and read it back. Phone holds exactly one number as written, email exactly one address; everything else goes in notes. The app's Call button dials the phone field as it is.
2. **Touch** (every outreach touch and reply): account_id, account_name, date, channel (email, call, text, linkedin, note), direction (out, in), status (planned, draft, sent, received, logged, cancelled), step (email 1, email 2, call 1, email 3, last call, call now, or blank), due_date, summary, full_text, outcome, gate_result, cancelled_reason. A drafted message is a Touch with status draft; it does not change the Account status.
3. **Deal** (every sales opportunity): account_id, account_name, stage (call booked, call done, proposal sent, won, lost), problem_cost_per_year, problem_cost_confirmed, proposed_price, monthly_retainer, booked_via_channel, booked_via_signal, next_action, next_action_date, won_date, call_brief, call_review, solution_design, proposal_link.
4. **Campaign**: name, status (draft, approved, live, paused, done), can_pay_rule, daily_limit, opt_out_line, postal_address, booking_page, approved_date, sent, replies, booked.
5. **Client** (won work being delivered): business, account_id, what, stage (Kickoff, Build, Test, Handover, Live), go_live_date, build_price, monthly_retainer, notes.
6. **Mission**: number, name, status (locked, active, done), started_date, done_date, proof_link. The 19 missions come from jarvis-missions.
7. **WeekNumbers**: week_start, target_calls, calls_booked, proposals_sent, deals_won, cash_collected.
8. **AgencySettings**: inbox_email, daily_cap, send_window_start, send_window_end, postal_address, opt_out_line, booking_page, brief_time, brief_days, working_hours, do_not_contact. Read campaign settings here before asking the member. Write inbox_email when an inbox is connected.
9. **Profile** (who the member is, shown in the HUD): business_name, owner_name, niche, service, suburbs, timezone, goal_90_day, call_hours, phone, owner_phone, voice_provider, superagent_id, hud_app_id, and the rest as the app defines. Keep it in step with your memory of the member.
10. **Task** (jobs agreed with the member, including in voice calls): title, status (todo, doing, done), priority, due_date, notes, source, execution_owner (jarvis, owner), progress_note, done_at.
11. **Memory** and **ActivityLog**: written by the HUD's voice mode and after-call bridge. Read them for context; add to them only as the after-call rules say.
12. **Do not use:** Vault holds the connection keys and only the app's backend can read it. Lead is the old free course table. Never write new leads there; Account is the only lead table. CallControl, CallReceipt, SessionLog, TalkTurn and User belong to the app itself. Never write to them.

## Tables in your Data area

1. **Offer:** the single offer brief every skill reads. One active row; old versions stay with active set to no. Fields: version, active, approved_by_member (yes or no, date), niche, buyer, problem, buyer_awareness, desired_outcome, solution, mechanism, deliverables, timeframe, risk_reversal, proof (only real, with source), approved_claims, alternatives, price_and_terms, value_model, six_line_offer, delivery_route (self build, developer, hybrid), research_links, created_date.
2. **Funnel:** one row per offer version. Fields: offer_version, landing_page_url, application_form_url, booking_page_url, confirmation_page_url, vsl_status (none, script, filmed, live), fit_rules, calendar_link, precall_sequence_version, sender_email, sms_sender, pixel_id, integration_status (each item: tested, drafted, missing), notes.
3. **Calls:** deal_id, type (call one, call two, other), date, recorded (yes or no), everyone_told (yes or no), summary, number_agreed, objections, review_score, one_change.
4. **Proposals:** deal_id, version, status (draft, sent, presented, accepted, declined), build_price, currency, monthly_running_cost, timeline, file_link, sent_date.

## Extra fields

When an app table lacks a field a skill needs (for example a campaign's spend, cost per application or weekly decision, or the week's lead quota), keep those fields in a Data area table named after the app table plus "Extra" (CampaignExtra, WeekNumbersExtra), linked by the app record's id. Never add fields to the app.

## Rules

1. Write first, then reply. If something changes in chat, update HQ before answering, then read it back.
2. Never delete rows in bulk. Mark them instead. Ask before deleting anything. When the member deletes a lead, delete its Touches with it, and keep its email and domain on the do not contact list if it was marked do not contact.
3. A contact marked do not contact stays that way through every import and every campaign.
4. Numbers come from actual events in HQ, never from estimates.
5. Every date is plain text, YYYY-MM-DD, in the member's timezone.
6. Every reason to contact has a source link. No source, no reason.
7. Never change the active Offer row with your own suggestions. Proposed changes go into a new Offer version with active set to no, every proposed field marked "proposed". It only becomes active when the member says yes. Guarantees, risk reversals, prices and delivery times always need the member's explicit yes.
8. When a skill says "save to HQ", use the table above wherever it lives: in the app if the app has it, otherwise in your Data area.
