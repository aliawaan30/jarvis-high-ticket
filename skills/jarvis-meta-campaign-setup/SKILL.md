---
name: jarvis-meta-campaign-setup
description: "Walk a member through setting up one Meta campaign for a booked call objective, step by step in plain language, and produce the plan that goes with it: naming, starting budget worked from ticket size, one ad per angle, broad targeting by country, and the 24 hour, 72 hour and 7 day checks with scale, fix or kill rules. Not a media buying service, not for ecom, not for campaigns with no booking page behind them."
---

# Jarvis Meta Campaign Setup

Draft, 29 October 2026. Built for Module 4 of the high ticket course. Since Meta's Andromeda ranking, the creative does the targeting, so the setup is deliberately simple: one campaign, one ad set, broad by country, one ad per angle. This skill tells the member what to click and gives them the plan to click it against.

Meta moves its interface around. Every instruction about the screen below carries this rule: check the current screen, Meta moves things. When what the member sees does not match, ask them to describe the screen and find the current path from there. Never insist the button is where it used to be.

## Inputs, read before producing anything

1. The offer price, and the member's four target numbers from the ads lesson: the most they will spend to win one client, the most a qualified booked call can cost, the most a lead can cost, and the guessed close and booking rates behind them. If they do not have these, work them out with the member first, labelled as guesses.
2. The ads ready to upload: how many videos, how many statics, and the angle each one tests.
3. The booking page link, and confirmation that the member has tested the booking flow themselves, start to finish, on a phone. If not tested, stop and tell them to test it before anything is turned on.
4. The country or countries they sell in.
5. Whether a Meta pixel or dataset is installed on the booking page. If unknown, step 1 below covers it.

## What Jarvis produces

A single campaign plan document, then the walkthrough. The plan contains:

- **Naming convention.** Campaign: `[Offer] · Booked calls · [Month Year]`. Ad set: `[Country] · Broad`. Ads: `[Angle] · [V1 / S1 for video or static] · [date]`. Names are how the member reads results in a month. Insist on them.
- **Starting daily budget**, worked from ticket size, all illustrative until the account has data. A working rule: start at roughly the target cost of one qualified booked call per day, with a floor that lets Meta deliver across every ad in the set (around $10 to $15 per ad per day as a rough minimum). For an $8,000 offer with a $500 target per booked call and five ads, that suggests a start near $75 a day. Say clearly that this is a starting point, not a prediction, and that the member should never run a daily figure they cannot afford for two weeks with nothing to show.
- **The structure.** One campaign, objective leads or booked calls through the website. One ad set, broad targeting, country only, no interests, no job titles, age 25 to 65 unless the offer says otherwise. One ad per angle, video and static as separate ads. Advantage plus or automatic placements left on.
- **The check schedule.** What to look at and what to do at 24 hours, 72 hours and 7 days, written as a checklist the member can paste into their CRM.
- **The decision rules.** Scale, fix or kill, with the member's own target numbers filled in.

## The walkthrough, step by step

Give these to the member one block at a time. Each step says what they click, what they should see, and what to tell Jarvis if it does not match. Check the current screen, Meta moves things.

### Step 1. Ad account, page and pixel check
1. Open Meta Business Suite, then Ads Manager. Confirm they are in the right ad account (the account name is at the top left) and that it has a payment method attached.
2. Confirm the Facebook page and, if they have one, the Instagram account are connected to the business.
3. Open Events Manager. Look for a dataset or pixel. If there is none, create one and install it on the booking page. The member's page builder (from the funnels module) usually has a field for the pixel ID; if not, paste the base code into the page head. Test with the Test Events tab by loading the booking page on a phone.
4. Set up one event that fires when a call is booked (a thank you page view or a lead event). This is the event the campaign optimises for.
Do not continue until the event fires in Test Events.

### Step 2. Create the campaign
1. Ads Manager, Create. Choose the leads objective (the name of this objective changes; it is the one for leads, enquiries or bookings through a website).
2. Name it from the plan. Leave campaign budget off at the start so the budget sits on the ad set, unless the current screen only offers campaign level budget, in which case set the daily figure there.
3. No A/B test, no special ad category unless the member's offer legally requires one.

### Step 3. Create the ad set
1. Conversion location: website. Performance goal: maximise conversions, with the booked call event from step 1 as the event.
2. Name it from the plan. Daily budget from the plan. Start date today, no end date.
3. Audience: country only. Remove every interest and job title. Age 25 to 65. All genders. Leave Advantage plus audience or the broad default on if offered.
4. Placements: automatic.
Explain why in one line: the ad copy does the targeting now, and narrowing the audience only makes the ad more expensive to show.

### Step 4. Create the ads, one per angle
For each video or static:
1. Create a new ad inside the ad set. Name it from the plan.
2. Identity: the Facebook page and Instagram account.
3. Upload the video (vertical, 9:16) or the static (feed and story versions separately if the member has both). Do not stretch one into the other.
4. Primary text: the first two lines of the script, or the static's primary text. Headline: the angle in six words or fewer. No price, no urgency, no invented result.
5. Website URL: the booking page. Add a simple UTM so the member can see which angle booked the call: `?utm_source=meta&utm_campaign=[offer]&utm_content=[angle]`.
6. Call to action button: Learn more or Book now, whichever reads honestly for a booking page.
7. Duplicate the ad for the next angle and change only the creative, the name, the text and the UTM content.
Publish the whole set together. Then leave it alone for 24 hours.

### Step 5. Turn on the tracking in the CRM
Before the first dollar: a line per ad in the member's CRM with the angle, the date it went live, and empty columns for spend, leads, booked calls, cost per booked call, decision and reason.

## The check schedule

**24 hours.** Is it spending? Is every ad delivering at least some impressions? Is the booked call event firing? Fix delivery problems only: a rejected ad, an ad with zero impressions, an event not firing. Judge nothing else. Day one numbers mean nothing.

**72 hours.** Look at CTR and cost per lead by ad. If one ad has a CTR far below the others and no leads, its hook is not landing; note it, do not kill it yet unless it has spent the cost of a booked call with nothing. If leads are arriving but no bookings, the problem is the page or the qualifying questions, not the ads. Fix that first.

**7 days.** Every ad that has spent about the cost of one to two target booked calls gets a decision:

- **Scale.** Cost per qualified booked call at or under target. Raise the ad set budget by around 20 percent, wait two or three days, raise again if it holds. Ask the member to run the ad scripting skill's variation mode on this angle and add the versions as new ads. Do not edit the winning ad.
- **Fix.** One step is broken, the rest is fine. High CTR, expensive leads: the page does not match the ad; rewrite the page's first screen in the ad's words. Cheap leads, no bookings: the qualifying questions or the calendar step; shorten the form, check the calendar works on a phone. Bookings but low show rate: the reminders and the pre call content from the funnels module. Fix one step, wait 72 hours, judge again.
- **Kill.** It has had fair spend and the cost per qualified booked call is well over target, or it is not getting clicks at all. Turn it off. Write one line in the CRM on why. Replace it with the next angle in the queue.

Repeat the 7 day check weekly. After four weeks, produce a short review for the member: which angles won, which died and why, what the real booking and close rates turned out to be, and whether the four target numbers should change.

## Rules

- Never turn on a campaign pointing at an untested booking page.
- Never put a price, a discount or urgency in an ad, headline or description.
- Never claim a result the member has not earned.
- Never recommend a daily budget the member has said they cannot afford to lose over two weeks.
- Never narrow the audience to interests or job titles to "fix" performance. Fix the creative or the page.
- No em dashes anywhere in the output.
- Jarvis does not have access to the member's Meta account and does not publish anything. The member clicks; Jarvis guides and records.
