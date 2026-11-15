---
name: jarvis-rhythm
description: The five Jarvis 2.0 workflows: morning brief, reply watch, after the call, evening log and Friday numbers. Use when setting up or changing scheduled or triggered work.
---

Version: 2026-11-15.1

# Rhythm: what Jarvis does without being asked

Five workflows. Create them once HQ is set up and the student has given their timezone, working days and morning time. Keep it to these five, plus one more only while an outreach campaign is live: Campaign runner. Every run costs credits. Workflows run in the background, so the same fence as the goal applies: they only read HQ and the funnel's Applications table, add new applications to HQ, run the weekly watchlist check on Fridays, report, draft messages for leads and replies, and update Numbers. The only thing they may send is an email from a campaign the member approved, through the Campaign runner, within its limits, after re-checking the account. They apply opt outs straight away. They never start offer, pricing, funnel, ads or script work. Suggest it in the message instead. Reply watch and after the call need a connected inbox: if there is none yet, wait and create them when one is connected.

## 1. Morning brief (scheduled, working days, their chosen time)
Workflow prompt:
"Query HQ now, do not use memory or earlier summaries. Run the operating loop. If the Funnel row has an app, read its Applications table and add new applications to HQ. Leads who replied with interest go first in the brief as calls to make. Read Deals, Accounts, Calls and Numbers. Check the active mission's proof (jarvis-missions) and mark it done if met. Send the morning brief in the style of the example in the brain, opening with the mission line. Draft every message the brief mentions and save the drafts. Do not send anything to prospects."

## 2. Reply watch (triggered: new email in the connected inbox)
Workflow prompt:
"If this email is from someone in Accounts or Deals: run jarvis-reply-desk, then send me one short message like the "A reply lands" example in the brain. If it says stop or unsubscribe, mark do not contact and tell me. If it is from no one in HQ, do nothing."

## 3. After the call (triggered: meeting notes for a sales call arrive by email or in Notes, or the member says the call is done)
Workflow prompt:
"If this is a sales call, run playbook-call-to-close. If it is not a sales call, do nothing."

## 4. Evening log (scheduled, working days, 6pm their time)
Workflow prompt:
"Ask me one short question: 'What did you get done today that I don't know about?' Log my answer to HQ. Compare today with this week's targets in Numbers and give me the one fix for tomorrow."

## 5. Friday numbers (scheduled, Friday 4pm their time)
Workflow prompt:
"Query HQ now, do not use memory or earlier summaries. Fill this week's Numbers row from HQ events. Compare with the goal. Send a short message like the "Friday" example in the brain: numbers, what we built, what's working, the gap, next week's targets. Then set next week's Numbers row. Then run the weekly watchlist check from jarvis-lead-hunter. Then check for a Jarvis 2.0 update as the brain's Updating section says."

## 6. Campaign runner (only while an outreach campaign is live)
Created by jarvis-outreach-coordinator when the member approves a campaign, paused when it ends or the member says stop. Base44 cannot trigger a workflow on another app's table (tested 4 Nov 2026), so run it every hour inside the member's working days and hours. A check can take several minutes, so tell the member that call now alerts arrive within the hour, not instantly.
Workflow prompt:
"Replies to Gmail arrive through the reply watch. On Instantly, read new replies through its API. Send every reply to jarvis-reply-desk. For any opt out found in replies: mark the account do not contact in HQ and cancel its pending touches now. Then work from the planned Touches due now (the outreach plan in jarvis-outreach-coordinator): send the emails due now in the approved campaign, follow ups first (email 3, then email 2, then new email 1s with whatever cap is left), within the daily limit per inbox and the recipient's working hours, re-checking each account first (do not contact, reply, opt out, booking), and sending only emails the send gate (send-check in Agency HQ) returns ok for, and saving each gate receipt. Calls are never made by you: put due calls in my list. If there is nothing new, send me nothing."
