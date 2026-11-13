---
name: jarvis-meta-campaign-setup
description: Plan and set up the student's first Meta ad campaign, then check it at 24 hours, 72 hours and 7 days from Ads Manager screenshots. Use when the student says "set up my Meta ads", "launch my ads", "check my ads" or shares an Ads Manager screenshot. Jarvis guides and records; the student does every click in Meta.
---

# Meta campaign setup (basic version)

Version: 2026-11-13.1

Student prompts:
1. **"Set up my Meta ads."**
2. **"Check my ads"** with an Ads Manager screenshot attached.

Jarvis never logs in to Meta and never publishes anything. The student clicks. Jarvis plans, guides, reads screenshots and records decisions.

## Before you start

1. Agency HQ must exist and its app ID must be saved. If not, stop and say: "I need Agency HQ set up first. Install the Agency HQ skill and say 'set up my CRM'."
2. The landing page must be live and the student must have tested it on their phone, start to finish. If not, stop and say: "Let's finish and test your landing page first. Ads only go on once it works."
3. Save everything as jarvis-hq says. The Campaign row is in the Agency HQ app; spend, budget, targets, ad names and decisions go in CampaignExtra in your Data area, linked by the Campaign's id. Never add fields to the app.

## Step 1: work out the numbers

Read the offer price from the Offer table. Ask for anything missing in **one** message:

1. The most they will spend to win one client. Suggest 25 percent of the price.
2. Their guess at how many booked calls become clients. Suggest 1 in 4.
3. Their guess at how many applications become booked calls. Suggest 1 in 3.
4. The most they can afford to lose in the first 2 weeks with no results.
5. The country they sell in.

Then work out and show:

1. Target cost per booked call = most per client x close rate.
2. Target cost per application = target cost per booked call x booking rate.
3. Daily budget = 2 x target cost per application, but never more than (2 week loss limit / 14).
4. Number of ads from the daily budget: under 50 a day, 2 ads. 50 to 149 a day, 3 or 4 ads. 150 a day or more, up to 6 ads. Fewer ads means each one gets enough spend to be judged.

Use the student's own currency for every number. Label every guessed number as a guess. Never round a budget up past what the student said they can lose.

**Budget too small:** if the daily budget is under 20 a day, say plainly: "At this budget Meta can't learn much, and you'll likely spend it all without a clear answer. I'd start with outreach (Module 4) and come back to ads when you can put in more." Only continue if the student still wants to, with 2 ads.

**Example (USD):** $8,000 offer, $2,000 per client, 1 in 4 close, 1 in 3 book. Target per booked call $500, per application about $167. Suggested budget $333 a day. Student can lose $1,400 in 2 weeks, so the budget is $100 a day with 3 or 4 ads.

## Step 2: write the plan

Show the plan and wait for approval:

1. **Campaign name:** [Niche] Leads [Month Year]. Example: Plumbers Leads Nov 2026.
2. **Ad set name:** [Country] Broad.
3. **Ads:** the number from Step 1, each a genuinely different angle. Use the finished videos from the ad editing skill and the statics. Name each ad [Angle] [Hook number] [Video or Static]. Example: Missed calls Hook1 Video.
4. **Daily budget** from Step 1.
5. **Landing page link** with tracking added to each ad: `?utm_source=meta&utm_campaign=[campaign name]&utm_content=[ad name]`, spaces replaced with hyphens.

Ask: "Ready to set it up? I'll walk you through it one step at a time."

## Step 3: walk through the setup

Give **one block at a time**. After each block ask the student to reply "Done" or describe what they see. Meta moves buttons often: if the screen does not match, ask what they see and find the current path from there. Never insist a button is where it used to be.

**Block 1: account check.**
1. Open Meta Ads Manager. Check the ad account name at the top left is their business.
2. A payment method is added, ideally a card in the business's name.
3. Two factor login is switched on for their Facebook account.
4. Their Facebook page (and Instagram, if they have one) is connected.
5. Set the account spending limit to their 2 week loss limit: Billing and payments, then Account spending limit. This is a hard ceiling inside Meta, so spending stops there even if a check is late. Ask them to confirm the number they set.
6. If Meta shows the account as restricted or disabled at any point: stop the setup. Ask them to open Account Quality and follow Meta's steps (usually identity or business verification). Never create a new ad account to get around a restriction; that makes it worse.

**Block 2: tracking check.**
1. Open Events Manager and find the pixel saved in their Funnel record.
2. Open Test Events, submit a test application on the landing page from their phone, and confirm a **Lead** event appears.
3. Find that test application in Agency HQ and mark it as a test (or delete it once the student confirms), so it never counts as a real lead.
Do not continue until the Lead event shows.

**Block 3: create the campaign.**
1. Click Create. Choose the **Leads** objective.
2. Name it from the plan.
3. Keep Meta's recommended setup (Advantage+) switched on. Set the daily budget at campaign level from the plan.
4. No special ad category unless the offer is credit, jobs, housing, financial products or politics.

**Block 4: the ad set.**
1. Conversion location: **Website**. Conversion event: **Lead**.
2. Name it from the plan.
3. Audience: set only the **country** and **minimum age 25**. Add no interests or job titles. Leave Advantage+ audience on.
4. Placements: leave on Advantage+.
Explain in one line: "Your ad's words do the targeting now. Narrowing the audience only makes ads cost more."

**Block 5: the ads, one per angle.**
1. Create the ad and name it from the plan. Identity: their Facebook page and Instagram.
2. Upload the video (vertical) or static.
3. Primary text: the first two lines of the script or the static's text. Headline: the angle in 6 words or fewer.
4. Website URL: the landing page with that ad's tracking link.
5. Button: Apply now or Learn more.
6. Open the creative enhancements and **switch off text improvements**. Meta must not rewrite their words.
7. Duplicate for the next angle. Change only the video, name, text and tracking link.

**Block 6: publish.**
1. Check every ad has its own name and tracking link.
2. Publish. Ads go into review, usually within a day.
3. Say: "Now leave it alone for 24 hours. Send me a screenshot tomorrow and say 'check my ads'."

Save the campaign: in the app's Campaign table the name, status "live" and approved_date; in CampaignExtra the date live, daily budget, spending limit, each ad's name and angle, and the target numbers.

## Step 4: the checks

Ask for a screenshot of Ads Manager **on a computer, not the phone app**, on the **Ads** tab, with these columns: Amount spent, Results, Cost per result, Link clicks, CTR (link). If columns are missing, tell them how to add them. If the screenshot is unclear, ask for a clearer one. Never guess a number.

Also read Agency HQ for applications and booked calls from each ad (the "came from" field).

**24 hours:** delivery only. Is it spending? Any ad rejected or with no impressions? Is the Lead event recording? Judge nothing else.

**72 hours:** note each ad's CTR and cost per application. If clicks come in but no applications, the landing page or application is the problem, not the ad. Change nothing yet unless something is broken.

**7 days, then weekly:** decide on each ad once it has spent at least 1 x the target cost per application, or at day 14, whichever comes first. An ad below both stays running until next week.

1. **Scale:** cost per application at or under target, and it has produced at least one booked call in Agency HQ. Raise the campaign budget by about 20 percent. Wait 3 days before the next increase. Never make two changes at once.
2. **Fix:** one step is broken. Clicks but no applications on **every** ad: fix the page's first screen to match the ads. If other ads get applications from the same page, the page is fine; leave this ad running until the kill rule. Applications but no bookings: check the application questions and calendar on a phone. Bookings but no shows: check the reminders. Fix one thing, then wait 72 hours.
3. **Kill:** no application after spending 2 x the target cost per application, no application by day 14, or cost per application above 2 x target. Turn it off and write one line on why.
4. **Keep running:** anything else. Check again next week.

**Hard stop (check every time):** add up total spend. If it has reached the student's 2 week loss limit and Agency HQ shows no booked call, tell them to pause the campaign now. Then review the offer, the landing page and the application with them before any more money goes in. Never suggest continuing past the loss limit without a booked call.

Tell the student which ads to scale, fix or kill, in plain words, with the numbers.

## Step 5: log every decision

Save each check to CampaignExtra: date, each ad's spend, applications, booked calls, cost per application, decision and reason. After 4 weeks, give a short review: which angles won, which died and why, and whether the target numbers should change.

## Rules

1. Jarvis never logs in to Meta, never publishes and never changes a budget. The student does.
2. Never suggest a budget the student cannot afford to lose over 2 weeks. Always set the account spending limit and enforce the hard stop. Never tell them to raise the spending limit while there is no booked call.
3. If the account is restricted, never suggest a new ad account.
4. No price, discount, urgency or invented result in any ad.
5. Never narrow the audience to fix results. Fix the ad or the page.
6. Use the student's currency. Plain language. No em or en dashes.
