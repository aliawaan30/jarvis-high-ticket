# Booking-reminder handoff

Blake's 5 November schedule: immediate email/SMS; emails at -48h, -24h, -2h, -5m; SMS at -24h and -5m; student notification/call task at -1h only while attendance is not confirmed. There is no -1h prospect SMS. This is the launch default, not a mandatory frequency for unrelated services.

Read the existing student CRM contract. Minimum information needed: booking/event ID and version, created/start time with timezone, current cancellation/reschedule state, prospect contact and channel eligibility, owner, meeting/confirmation/reschedule links, attendance status and how it was established. These are data needs, not a claim that a schema or integration is deployed.

For each action save its scheduled time, owning sender, action key, state and delivery/task result. Skip reminder offsets at or before booking creation; do not send stale reminders in a burst. Immediate confirmation owns the booking boundary. Avoid overlapping native calendar reminders. A new version cancels old tasks before scheduling from the updated start time. Recheck attendance at one hour and immediately before a queued call task is delivered.

The confirmation page explains the same attendance method the email actually implements. A tokenised attendance link must validate server-side for the booking and update the authorised record idempotently. A generic button click, page view or unspecific reply is not sufficient. Human confirmation on the call is logged separately. Calendar invitation/RSVP state is provider-specific and may not be available.

Draft copy must match the saved offer and actual appointment. Instant email: booking details, confirmation action and preparation page. Instant SMS: brief logistics/confirmation link. Earlier reminders can answer one objection with an actual asset. Near-call messages focus on time and joining. No invented testimonials, “everyone else confirmed” claim, extra meeting duration or public offer pricing.

Expected schedule examples for manual review:

- Booking 72h ahead, no confirmation: immediate email/SMS, all four reminder emails, 24h/5m SMS, one internal call task at 1h.
- Booking 3h ahead: immediate email/SMS, 2h/5m email, 5m SMS, call task at 1h if unconfirmed. No 48h/24h backlog.
- Booking 30m ahead: immediate email/SMS and the 5m reminders. No retroactive 1h call task.
- Already confirmed at 1h: no call task. Continue appropriate appointment reminders without asking to confirm again.
- Rescheduled/cancelled/replayed event: no remaining actions on the old booking version; no duplicate messages.

This specification is not a connected automation. The owner must test sender/provider behaviour using owned recipients before activation.

## Calendly option checked 5 November 2026

Prefer an existing provider attendance action over building a new confirmation endpoint when the connected account supports it. Calendly's official reconfirmation guide documents an email attendance button, a text confirmation-link variable and a host notification on attendance confirmation. Availability depends on the account's plan/feature access. Verify event/CRM access separately rather than assuming that every invite acceptance is available through an API.

Sources: https://calendly.com/help/how-to-reconfirm-meetings-with-automations and https://calendly.com/help/calendly-scheduling-notifications . The notification guide distinguishes a connected-calendar invitation from an emailed static event file; don't promise the latter automatically updates on every change. No member account was configured or tested in this research.
