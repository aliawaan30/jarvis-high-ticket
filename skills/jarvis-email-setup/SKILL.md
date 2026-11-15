---
name: jarvis-email-setup
description: Set up and run cold email the easy way: the member's own Gmail connected to Jarvis, a strict daily cap, the send gate on every email, and an upgrade to Instantly when they want bulk campaigns. Use before any cold email is sent, when the member asks about sending, inboxes, limits or deliverability, or wants to send more emails.
---

Version: 2026-11-15.1

# Email setup

Version 2, 4 November 2026. Easiest start: the member's own Gmail, connected to Jarvis in a minute. Volume stays low and quality stays high, which protects their inbox. Instantly is the upgrade for bulk.

## Level 1: their own Gmail (default)
1. Ask the member to say "connect my Gmail" and approve the card. Straight after it connects, always send one test email to the member's own address and ask them to confirm it arrived and which From address it shows. No cold email until they confirm. Connect it to this agent. If a Gmail is already connected at workspace level, check which address sends: send one test email to the member and confirm the From address is the one they want.
2. Daily cap: 10 cold emails a day to start, never more than 15 from this inbox. Replies and follow ups to people who replied do not count toward the cap.
3. Check their sending domain once: if it is their own business domain, look up its public DNS for SPF, DKIM and DMARC and tell them in one line if anything is missing, with the exact record to add. If it is a plain gmail.com address, nothing to set up.
4. Signature: their name, business name and postal address (required for US email), set once on the Campaign row. The postal address is the only thing to ask for; everything else has a default.
5. Only email addresses the business publishes on its own website or listing (email status published), or addresses verified by a verification service (verified). Never a guessed address.
6. Plain text, no images, no attachments, no link in the first email, at most one link later, send in the recipient's working hours.
7. Auto pause: one bounce over 2 percent of the week's sends, or any spam complaint, pauses cold email from this inbox until the cause is found. Tell the member in one line.
8. Replies land in this same inbox, where the reply watch reads them. No other setup.

## The send gate (every email, no exceptions)
Plain code, no AI: the backend function sendCheck that ships inside the member's Agency HQ app (function 19 of the package). Call it at the app's published address plus /functions/sendCheck, as a POST, with the x-hud-key header set to the app's HUD_KEY. Before any outreach email or reply goes out, call send-check with the email, the account and the campaign settings. Send only if it returns ok true. If it returns reasons, do not send: fix the email or tell the member why. If it cannot be reached, do not send. No check, no send.
It blocks (working hours do not apply to the member's own test address): guessed, risky or invalid addresses for cold email, accounts whose country or entity type forbids email, do not contact, replied or booked accounts, unapproved campaigns, the daily cap, outside the recipient's working hours, a missing opt out line or postal address, unfilled placeholders, banned spam and AI phrases, HTML, any link in email 1, more than one link later, and any link or address on a domain that is not the member's own (only their exact booking page is allowed).
Fields to send: email (to, subject, body, kind cold or reply, step), account (email, emailStatus, emailAllowed, emailAllowedReason, replied, booked, doNotContact, website), passing the Account's yes or no values as they are stored, settings (campaignApproved, dailyLimitPerInbox, optOutLine, postalAddress, ourDomains, bookingUrl, doNotContact, sendWindowStart, sendWindowEnd), recipientLocalHour, sentTodayFromInbox.
Work out the recipient's local hour from the exact IANA time zone of the account's city (Phoenix is America/Phoenix, which never changes for summer; Sydney is Australia/Sydney; London is Europe/London). Save the zone on the account. If the city is unknown, use the country's main zone and say so; never guess across zones in countries that have several.
Gate receipt: save the result on the email's Touch as gate result ("ok", the date and the pack version). An email marked sent without a gate result is a broken rule: tell the member and stop the campaign until it is explained.

## Make sure the send gate works (at install, and again at mission 9)
1. sendCheck is part of the Agency HQ package. Never write or edit it yourself.
2. If a call to sendCheck returns 404, the function was not deployed: give the member this exact message for the Agency HQ builder chat, "Deploy the sendCheck backend function exactly as written in base44/functions/sendCheck, then send it an empty POST and give me the status code", and check again. If it returns 401, the HUD_KEY you sent does not match the app's secret: check it with the member.
3. Backend functions need the member's Base44 Builder plan or higher. If their plan does not include them, tell them in one line which plan does, and hold all sending until it is sorted.
4. Test it: one good test email must return ok true, one with "{{first_name}}" in it and a guessed address must return ok false with reasons. Mission 9 is only done when both behave.

## Level 2: Instantly (upgrade for bulk)
Offer it when the member wants more than 15 cold emails a day, or several inboxes. Instantly can sell ready made sending inboxes and handles warm up, so there is no DNS work. Tell them to check current prices; its API needs the Growth plan or above.
1. They create the Instantly account and buy inboxes inside it.
2. Ask for the API key with the secure secret card in this chat, saved as INSTANTLY_API_KEY.
3. Jarvis creates the campaign, runs the send gate on every template and every merged lead, and adds only the leads that pass, with custom variables (first name and the two insights).
4. The Campaign runner reads new replies through Instantly's API each hour and sends them to jarvis-reply-desk.
Cold email moves off their Gmail once Instantly is live.

## Health check (inside Friday numbers)
Sent, bounced, replies, opt outs and complaints per inbox, in one line. Pause and explain if a limit is crossed.

## Never
1. Never go above 15 cold emails a day from the member's own Gmail.
2. Never buy or use a purchased email list.
3. Never send to a country or entity type the country rules block.
4. Never hide who is sending: real name, real business, real postal address, a working way to opt out.

## HQ (Jarvis 2.0)
Read first: Offer, Campaigns, Accounts. Write when done: Campaigns: sending method (Gmail or Instantly), inbox, daily limit, DNS status if checked. After writing, read the rows back and confirm they saved.

---

## Appendix: send-check code
The code lives in the Agency HQ package: base44/shared/send-check.ts (the rules) and base44/functions/sendCheck/entry.ts (the function). It is tested with 20 good emails that must pass and 15 bad ones that must be blocked. Logic adapted from Harvey (github.com/ethanplusai/harvey), MIT License, Copyright (c) 2026 Ethan Rogers.
