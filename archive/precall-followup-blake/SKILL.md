---
name: jarvis-precall-followup
description: Prepare the booking-confirmation email/SMS and reminder flow from the saved funnel, with a one-hour call task for unconfirmed prospects. Connect only through authorised calendar, sender and CRM tools.
---

# Jarvis booking reminders

Revised 5 November 2026 from Blake's reminder schedule. These instructions prepare the flow; actual senders and booking/attendance events still need connection and tests.

Student prompt: **“Run the pre-call follow up skill for my saved offer and funnel using this reminder schedule. Calendar: [tool or link].”** Older “for my offer and my landing page” prompts remain valid.

Read the saved offer, booking/confirmation pages, video/proof, calendar, sender settings and CRM records. Do not ask the student to paste them again. Resolve only missing settings needed for the flow. The student CRM is being developed by Ali; use its agreed event contract rather than inventing a competing CRM or schema.

## The flow

Start on an actual booking-created event, never application submission or a page view. Calendly is the intended booking tool; check its actual event notification settings. Calendar invitations and email confirmations are provider settings, not interchangeable evidence of invite acceptance. The attendance email must contain the real secure action used by the confirmation page.

| When | Recipient and action |
|---|---|
| Immediately on booking | Prospect: confirmation email and SMS with time/timezone, confirmation-page link and the real attendance action. Calendar provider sends the configured invitation. |
| 48 hours before | Prospect: email reminder and relevant useful offer/preparation content. |
| 24 hours before | Prospect: email and SMS reminder. |
| 2 hours before | Prospect: email with meeting details. |
| 1 hour before, only if attendance is still unconfirmed | Student: notification/call task with prospect, time, contact details and the script below. No automated prospect SMS at one hour. |
| 5 minutes before | Prospect: brief email and SMS with the meeting link. |

The five-minute email follows Blake's final email list; SMS at 24 hours and five minutes follows his accompanying spoken schedule. Keep this default configurable if he changes the cadence. No past-due reminders on short-notice bookings; immediate confirmation still sends. Don't replay missed offsets or duplicate a just-sent message when a booking falls exactly on a reminder boundary. Check any existing Calendly notifications to prevent a second sender repeating the same reminder.

## One-hour call script

“Hey [name], it’s [your name]. I was just going through my calendar and noticed your appointment hasn’t been confirmed yet. Are you still all good to show up for [time]?”

On yes, verify the time and meeting link, then record the manual attendance confirmation. On no, help reschedule and rebuild reminders. The original “everyone else confirmed” comparison may only be used if the actual records establish it; it is not required or invented social proof.

## Connection and event rules

- Keep booking state, attendance confirmation and calendar-invite acceptance distinct. A secure email-confirmation action or an explicitly logged human confirmation may update attendance. A normal reply must be interpreted by a person rather than treated as an automatic yes. Calendar acceptance can count only under the configured policy and actual provider event.
- Recheck the current booking and attendance before creating the one-hour task. Confirmed means no call task; unknown status creates a check-and-call task rather than asserting refusal. Deduplicate by booking ID, version and action. If attendance is confirmed after task creation, close the obsolete task where supported.
- Cancellation stops future reminders and tasks. Rescheduling invalidates the old schedule and uses the new time/version. Replies pause automated nurture for human review; don't silently discard essential meeting logistics or reschedule/cancel updates. Record permission and routing before activation.
- Honour channel opt-outs. Missing SMS permission suppresses SMS, not a fake delivered status. Handle invalid contact details and delivery failures without blind retries. Use the CRM's booking timezone and real meeting links, not manually guessed dates or placeholders.
- Store attendance tokens in the authorised provider/backend, not exported scripts or public examples. Do not enrol a cold prospect in appointment messages. This skill is booked-call follow-up, not outreach, long-term nurture or no-show campaigns.

## Deliver and test

Deliver the message drafts, offset/event table, one-hour task/script and actual connection status. Use [the handoff specification](references/booking-reminders.md) when wiring the calendar/senders/CRM. Test a long-lead and short-notice booking, confirmed and unconfirmed attendance, a duplicate event, reply, opt-out, cancellation and reschedule using owned test recipients before activation. No real sends or calls without authorisation. Record local schedule checks separately from tested provider execution.
