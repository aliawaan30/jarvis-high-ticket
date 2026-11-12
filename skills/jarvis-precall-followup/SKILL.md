---
name: jarvis-precall-followup
description: Create offer-specific pre-call email and SMS sequences and a precise event workflow for booked prospects, including replies, reschedules and cancellation handling.
---

# Jarvis Pre-call Follow-up
Recovery draft. Copy and workflow are not a connected sending system.

## One-line entry and shared context

Student prompt: **“Run the pre-call follow up skill for my offer and my landing page. Calendar: [tool].”**

Read the current member's saved offer, funnel pages/URLs, proof, preparation video, calendar setup and booked-call records. Do not ask the student to paste the offer, landing copy or proof again. Use the existing funnel record; ask which offer only if the active one is ambiguous. Ask only for missing information needed to prepare the sequence, such as an unavailable calendar configuration or intended call host.

The qualified booking page comes before an appointment; the confirmation/thank-you page comes after a booking is created. Start pre-call messages from the real booking-created event. Reuse the post-booking page and preparation video; keep attendance/invite acceptance separate from booking creation. Do not enrol an unbooked applicant into appointment reminders.

Prepare useful drafts even when senders are not connected. Before activation, resolve the sender email/number, account access, event integration and recipient channel permissions that are actually missing. Use connected provider tools only within authorised scope; the skill itself does not establish a working email/SMS sender. Save copy, workflow version, page references and integration status in the member's existing funnel/campaign record.

Use the canonical offer, booking state, timezone, appointment link and genuine preparation/proof assets. The goal is a prepared, suitable prospect who attends, not message volume. Booking confirmation comes first; useful education and reminders follow. Avoid repeated generic 'just checking in'.

Produce a small sequence suited to the actual booking lead time. Each touch has one job: confirm logistics, answer a major objection with a relevant asset, help them prepare, or remind them of the appointment. For a same-day booking compress the sequence rather than firing every queued touch. SMS is concise; email can carry the explanation. Do not invent customer results or send placeholders.

Define the event workflow as well as copy: trigger, recipient, offset/local time, required fields, stop conditions and reply routing. Stop or rebuild scheduled reminders on cancellation/reschedule. Stop prospect nurture after won/lost disposition where appropriate. A human reply pauses robotic follow-ups and creates a handoff. Honour opt-outs across the relevant sender's workflow. Use event IDs to prevent duplicate sends and record delivery errors for review.

Deliver: message drafts, event table, required integration fields and a sandbox test plan covering booking, reply, reschedule, cancellation, opt-out and duplicate webhook. Do not say a Base44/CRM integration is connected unless it has been tested in that environment. A missing sender affects execution status, not our ability to prepare useful copy.

## HQ (Jarvis 2.0)
In Jarvis 2.0, "saved offer", "offer brief", "funnel record", "campaign record", "project record" and "CRM" all mean the HQ tables in the jarvis-hq skill. Do not keep a second copy anywhere else.
Read first: Offer, Funnel, Deals. Do not ask the member for anything HQ already holds.
Write when done: Funnel: pre-call sequence version, sender email, SMS sender, integration status.
After writing, read the rows back and confirm they saved before you tell the member it is done.
