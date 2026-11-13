# Meta campaign setup skill, scenario test (version 2026-11-11.2)

Method: Claude played Jarvis and followed SKILL.md literally. Mock Ads Manager screenshot (ads7.png) and mock Agency HQ data. Not a Base44 run.

## S1. Happy path, day 7 check (Sam, $8,000 AI CRM, US, can lose $1,400)
Setup: target per application $167, budget $100 a day, 4 ads. Day 7 screenshot: total $700, 4 leads. Agency HQ: 1 booked call from Missed calls Hook1.

Jarvis reply (following the rules):
- Missed calls Hook1: spent $260, 3 applications at $87, 1 booked call. SCALE. Raise campaign budget 20% to $120. Wait 3 days.
- Missed calls Hook2: spent $210, 1 application at $210 (target $167, under 2x). KEEP RUNNING.
- Job admin Hook1: spent $180, 61 clicks, 0 applications. Rules give two answers: FIX ("clicks but no applications: fix the page") or KEEP RUNNING (kill only after $334 or day 14).
- Quote chase Hook1: spent $50, under $167. KEEP RUNNING.
- Hard stop: $700 of $1,400. OK.
Result: PASS with one conflict. Problem A.

## S2. Budget too small (Priya, $5,000 receptionist, can lose $200)
Budget $14 a day. Jarvis gives the "start with outreach" message, continues with 2 ads only if she insists.
Result: PASS.

## S3. Hard stop, day 16 check (Sam again, checked 2 days late)
Screenshot: total $1,610, 6 applications. Agency HQ: 0 booked calls.
Jarvis: loss limit passed, pause now, review offer, page and application.
Result: rule fires, but $210 over the limit already spent, because nothing stops Meta between checks. Problem B.

## S4. Blockers (Leo, landing page not tested; account shows restricted in Block 1)
Jarvis stops at "Before you start" until the page is tested. In Block 1 it stops, sends him to Account Quality, and says never to open a new ad account.
Result: PASS.

## S5. Bad screenshot (Ana, sends a phone app screenshot: spend and results only, cropped)
Jarvis asks for a clearer one with the 5 columns and does not guess. But the skill only explains adding columns on a computer, and the phone app shows a different, shorter view.
Result: PARTIAL. Problem C.

## Problems found
A. Fix and kill overlap. "Clicks but no applications: fix the page" is right when no ad converts. When another ad converts on the same page, the page is fine and the ad's promise does not match it. Changing the page could hurt the winner.
B. Spend can pass the loss limit between checks. Meta has a built in account spending limit; the skill should set it to the 2 week loss limit in Block 1.
C. Screenshots must come from Ads Manager on a computer, not the phone app.

## Proposed fixes
A. Fix the page only when the whole campaign has clicks but no applications. A single ad with clicks but no applications while others convert keeps running until the kill rule.
B. Block 1: set the account spending limit to the 2 week loss limit (Billing and payments, Account spending limit). The hard stop then happens inside Meta even if a check is late.
C. Step 4: "Take the screenshot in Ads Manager on a computer, not the phone app."

---

# Retest after fixes (version 2026-11-11.3)

## S1 again: day 7 check (Sam)
Job admin Hook1: 61 clicks, 0 applications, but other ads convert on the same page. New rule: page is fine, KEEP RUNNING until the kill rule. No conflict.
Result: PASS.

## S3 again: hard stop with a late check (Sam, day 16)
Account spending limit set to $1,400 in Block 1. Ads stop delivering at $1,400 ("Account spending limit reached"). Day 16 check: $1,400 spent, 0 booked calls. Jarvis: pause the campaign, review offer, page and application. No overspend.
Result: PASS.

## S5 again: phone screenshot (Ana)
Jarvis asks for a computer screenshot on the Ads tab with the 5 columns before reading anything.
Result: PASS.

## S6 new: no ad gets applications (Mia, A$4,000 dental offer, AU, can lose A$700)
Budget A$50 a day, 3 ads, target per application about A$83. Day 7 screenshot (ads7b.png): A$350 spent, 243 clicks, 0 results on every ad.
Jarvis: clicks but no applications on every ad, so FIX the page's first screen. No kill yet (no ad has reached 2 x target).
Gap: 243 clicks and zero applications can also mean the pixel stopped recording. The skill reads Agency HQ but never compares it with Meta. If Agency HQ has applications Meta does not show, the page is fine and the tracking is broken; changing the page would be the wrong fix.
Result: PARTIAL. Problem D.

## S7 new: spending limit reached while winning (Sam scales to $120 a day on day 7)
At $120 a day the $1,400 limit is reached around day 13. Agency HQ shows 2 booked calls. Ads stop.
Gap: the skill only covers the limit with no booked call. With booked calls it says nothing, so Jarvis either stalls or raises money questions on its own.
Result: PARTIAL. Problem E.

## New problems
D. Check tracking before fixing the page: compare applications in Agency HQ with Meta's results.
E. Limit reached with booked calls: show the results, then ask the student whether to set a new 2 week limit and how much. The student decides; Jarvis never raises it for them.
