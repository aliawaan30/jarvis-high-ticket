---
name: jarvis-confirmation-page
description: Build the post-booking thank-you page and preparation video brief from the saved funnel and real booking status. Not the congratulations page that invites a qualified applicant to book.
---

# Jarvis Thank-you / Confirmation Page

Reference-inspected instruction draft. Revised 5 November 2026. Use our original [course demonstration](assets/course-demo/index.html) as the student-facing example. It has original Roofline branding, copy and instructional visuals; it does not send emails or verify a real booking. [The historical reference analysis](references/compass-confirmation.md) supports the sequence but the external page must not be used as the course demo. Use this sequence; it supersedes the earlier generic receipt layout. [Earlier reference analysis](references/funnel-visual-analysis.md) remains supporting context. `assets/roofline/thank-you.html` is the compact example; its booking record is demonstration data, not an integration.

Student prompt: **“Run the confirmation page skill for my landing page. Video: [link or placeholder].”**

Read the saved offer, identity, landing/application/qualified-booking pages, calendar, call purpose, confirmation-video, actual attendance-email configuration and approved proof. Reuse context. Ask only for genuinely missing settings or assets, not the offer again.

## Keep these stages distinct

| Stage | Correct page and message |
|---|---|
| Application qualifies, no booking | Landing skill's booking page: “Congratulations, you qualify.” Invite them to book. |
| Booking created, attendance awaiting action | This thank-you page: “You’re booked in.” Then “Please accept your calendar invitation to confirm you’ll attend.” |
| Attendance already confirmed | “You’re booked in. See you then.” Do not ask them to confirm again. |
| Invite acceptance cannot be read | Booking is created; invite status is unknown. Ask them to check/accept the invite without asserting that they have not. |
| No verified booking | Do not display booked status or invented logistics. Offer the saved booking link or a way to resolve it. |
| Booking cancelled or rescheduled | Reflect the authoritative current record, not stale query parameters or cached copy. |

Blake's “booked in, not confirmed yet” distinction means **booking exists, attendance is not yet confirmed**. Use that explicit supporting line only when the provider actually exposes that state. A page visit is neither a booking nor invite acceptance. Do not threaten cancellation or claim they will lose the slot without a real policy.

## Compass-style confirmation page

Build one post-booking confirmation page, also called the thank-you page in older prompts. Do not create a second receipt page. It confirms attendance after an appointment was booked.

1. **Final step / action required:** large clear attendance-status headline. When attendance really awaits a configured confirmation action: **“Your call is booked. Please confirm you’ll attend.”** A red/gold action treatment can follow the reference. Already confirmed attendance gets a completed message instead.
2. **Watch this first:** dominant preparation video. For an explicit placeholder draft use **“Insert confirmation video here”**. Essential instructions remain readable without watching.
3. **Confirm attendance in the email:** when this flow exists, say which email to open and the real button label, such as **“Yes, I’m attending”**. Use a simple original instructional email visual. No pretend on-page button or click-to-confirm claim without a secure real endpoint. Save a clear private integration task if email confirmation is not connected. If only an invite is available, use its actual acceptance action rather than invent another.
4. **Accept the calendar invitation:** brief instruction and, when helpful, an original instructional calendar visual. Real meeting details and reschedule link may appear here, not as a distracting block above the video. No repeated booking calendar or application.
5. **Proof only when it exists:** relevant authorised case studies and/or genuine reviews after the actions. Zero reviews means omit reviews. Zero case studies means omit results. No proof placeholders, fake stars or a substitute wall of features.

The 60-90 second video brief: thank them for booking, explain the real confirmation-email action and calendar invite, say what the call helps decide, and close on the desired result. No unnecessary homework, invented duration, cancellation threats, public prices or em dashes. A reply-YES or email-button step now follows Blake's explicit Compass reference, but only the real configured method should be described in production.

Unknown, cancelled, rescheduled and missing-booking records are internal handling cases on this same route, not four additional prospect-facing pages. Do not list them in the normal review navigation. Provider notices should remain accurate; no need to manufacture a cancellation or reschedule landing page.

## Connect and check

Save the thank-you URL, preparation asset and actual integration status in the same funnel record. Configure the calendar's completed-booking destination where supported. Read a booking from the authorised backend/provider, with appropriate access control; don't trust a public `booked=true`, name/email query string or browser storage as proof. Keep private invite/meeting tokens protected. Use a verified booking event for reminders via `jarvis-precall-followup`.

Deliver the page, preparation script and concise connection report. Test awaiting attendance, already confirmed, unknown invite state, missing booking, cancellation/reschedule and mobile layout when the provider exposes them. A fixture can check display behaviour but does not prove event integration. Do not call a landing/application redirect a successful booking.
