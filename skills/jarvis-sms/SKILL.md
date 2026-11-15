---
name: jarvis-sms
description: Text messages to people who opted in or already replied, the easy way: Jarvis writes the text and the member sends it from their own phone with one tap. Telnyx automation is the upgrade. Use when the member wants to text a lead or client, send a booking reminder, or asks about SMS. Never for cold outreach.
---

Version: 2026-11-15.1

# SMS

Version 2, 4 November 2026. Cold texting is not allowed under our rules in any of the 7 countries. In the US, texting without consent can cost $500 to $1,500 per message. So texts only go to people who said yes.

## Who can be texted
1. Someone who ticked the SMS box on the funnel's application form.
1b. Someone who booked a call and ticked "OK to text me reminders" on the booking form. Ask the member to add that yes or no question to their Cal.com event, and record the answer from the booking confirmation as the consent source.
2. Someone who replied and asked to be texted, or gave their mobile for that purpose, or who the member already spoke to and agreed.
3. Nobody else. Not Money Map leads, not numbers from a website, not anyone who said stop.

## Version 1: one tap from their own phone (default, no setup)
1. Write the text: under 160 characters, the member's first name and business, one clear point. The first text to someone ends with "Reply STOP to opt out."
2. Give the member a one tap link that opens their phone's messages with the number and text filled in: sms:[number]?&body=[text, URL encoded]. Show the text above the link so they can read it first.
3. Ask them to reply "sent" after sending, then log it as a Touch with the full text (channel text, direction out).
4. If they get a reply, they can paste it to Jarvis, which handles it like any reply (jarvis-reply-desk). If the reply says stop, mark do not contact for texts straight away.
5. Only suggest texts inside 8am to 9pm in the recipient's local time.

## Upgrade: Telnyx automation
For members texting more than a handful of people a week. Tell them plainly that US business texting needs registration (10DLC or toll free verification) before sending, which takes time, and other countries have their own sender rules. Check Telnyx's current pricing and country rules before starting.
1. They open a Telnyx account, buy a number and complete the registration for their country.
2. Ask for the API key with the secure secret card in this chat, saved as TELNYX_API_KEY, and the number as TELNYX_FROM.
3. Jarvis sends through Telnyx's messaging API from Python, reading the key from secrets, after the same consent and hours checks.
4. STOP replies mark do not contact for texts at once.

## Never
1. Never text anyone without consent or an existing conversation where they agreed.
2. Never use texts for cold outreach, in any country.
3. Never text outside the recipient's local hours.

## HQ (Jarvis 2.0)
Read first: Accounts (SMS consent), Deals. Write when done: a Touch for each text, Accounts: SMS consent source, do not contact for texts when they opt out.
