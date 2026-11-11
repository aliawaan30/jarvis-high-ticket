---
name: jarvis-landing-page
description: Build a compact offer-led landing page, progressive application and qualified booking page from the saved offer. Use for a student B2B service funnel, with a VSL or a no-video offer-testing mode.
---

# Jarvis Landing Page

Reference-inspected instruction draft. Revised 5 November 2026 from Blake's page corrections and 4 November call. This is the student service funnel, not the longer high-ticket programme demonstration from J-374.

## Start from the saved offer

Student prompt: **“Run the landing page skill for my offer. Domain: [x]. Calendar: [link]. Video: [link or none yet].”**

Read the member's saved buyer/problem/solution brief, six-line offer, approved claims, identity and current funnel. Do not ask them to paste these again. Resolve only missing inputs that affect this build: intended offer if ambiguous, identity/domain, calendar, video mode and meaningful fit criteria. Draft without a missing calendar; ask for it and report the connection gap outside the prospect page.

The service must be understood before its headline is written: who buys, what currently happens, the consequence, what changes, delivery and what can genuinely be promised. Do not invent a guarantee or numerical outcome to complete a page. A new promise returns to offer approval rather than silently changing the service. Setup timing and result timing are different.

Read [the reference analysis](references/funnel-visual-analysis.md). Use `assets/roofline/` for the approved visual/interaction pattern, after reading [its benchmark](assets/roofline/benchmark.json). Replace the example's identity, claims, questions and submission handler. Its worked roofing promise is illustrative, not verified proof or a universal student guarantee.

## The landing page, in order

1. **Audience callout:** the specific buyer.
2. **Headline:** the result they actually want, with approved timeframe and risk reversal when available. Sold jobs or cash collected can be the desire; replies and appointments are often intermediate steps. Never promise a sale when the service only supplies an appointment without an agreed basis for the downstream result.
3. **Subheadline:** one sentence explaining what is done, how and the relevant avoided burden. The full service description stays in the brief and VSL. Do not paste the six-line card as the headline.
4. **VSL:** a dominant 16:9 player when a video is supplied. An explicitly requested VSL draft without footage says only **“Insert VSL here”**.
5. **One application CTA:** **“See if you qualify”** or the member's approved **“Apply”**. Continue into the progressive application.

Default to the compact reference. The VSL explains deeper pain, workflow and objections. No duplicated written pain essay, numbered process, detailed guarantee block, generic FAQ, feature wall or invented testimonials underneath. Add longer sections only for an explicit different brief; do not make that exception the student default.

If there is no video and no explicit VSL-draft request, build **Offer Testing Landing Page**: callout, headline, brief mechanism and application CTA. Remove the video area entirely. Do not substitute a storyboard, fake player or hero illustration. Keep the same offer and fit rules when comparing page formats.

Keep public prices out. No countdowns, fabricated proof or scarcity. No em dashes, completion-time estimate, preparation burden, production commentary or course-example footer on the prospect page. Keep material guarantee conditions accessible without a long sales block. A work-free remedy must say internally which fee stops, the target, measurement and responsibilities; it is not automatically a refund or free software.

Use the approved brand with a narrow centred reading column, strong headline, balanced whitespace and one next action. Compare proportions and order with the actual reference, not just its colours. The Meta non-affiliation line is optional branding copy, not a verified universal advertising requirement or a substitute for privacy information.

## Application

Use three or four useful fit questions, one per screen, then **name, email and phone together** on the final screen. Add company there only if needed; do not create a separate contact step for each field. Ask about the buyer's business and the conditions needed for this service, not irrelevant generic qualification questions.

Preserve answers on Back. Validate each step and the final contact fields. Final copy: **“Where can we reach you?”** and **“Add your details below to complete your application.”** Do not mention choosing a call before they have applied. Required contact/privacy wording must match the actual sender and intended use.

Production submission must save the application successfully before advancing. Apply approved fit rules server-side or in the trusted CRM/backend; a client-side choice cannot grant eligibility. Define three possible outcomes: qualified for a call, needs review, and outside scope. Missing criteria or unknown answers go to review, not automatic approval. Failed submission retains answers and allows retry without duplicate records. Keep personal details out of URLs, public logs and generated assets.

The bundled example has no submission/qualification integration and routes to a review preview. Replace that handler when building the member's real funnel. A local redirect is not a saved or qualified application.

## Congratulations and booking page

This page is **after a successful qualified application and before a booking**. Use `booking.html` as its canonical name.

**Congratulations, you qualify.**

**Book a time to see how we can [the offer's desired result].**

One short mechanism line may reinforce the benefit without adding an essay, checklist or extra work. Qualification means suitable for this call, not accepted into a paid service. Do not invent a free audit, meeting duration, result or funding approval.

Include a booking calendar section on this page. Use the supplied real embed with a fallback booking link. Ask for the calendar if missing. In a local structure review, reserve a clearly labelled calendar integration area; do not invent available times or imply scheduling works. Replace that review slot with the actual calendar before publication. Do not announce a booking just because the visitor reaches this page. Needs-review and outside-scope applicants receive accurate separate outcomes instead.

`confirmation.html` in the old Roofline asset folder is a compatibility copy of this pre-booking design. It is not the post-booking thank-you page. Never wire it as the calendar-completed destination.

## Post-booking handoff and shared record

Use `jarvis-confirmation-page` for the distinct **thank-you page after a real booking is created**. Reuse the same offer and funnel record. Record the exact URL and connect the calendar's real completed-booking event/redirect. Application, qualified, booking created and attendance confirmed remain separate states. A page view or generic lead event is not a booked call. Pre-call reminders start on the booking event, never the application.

Save the offer version, all page URLs, qualification rules, calendar/video references and connection statuses together in the existing member store. No new parallel memory system or secrets in the record.

## Review and deliver

Deliver the page files/preview, saved funnel record and a short list of missing connections. Test desktop and phone widths, every form step, Back, invalid input, retry, successful storage, each qualification route and the calendar-to-thank-you handoff where connected. In a draft, identify which checks are local simulations and which real integrations remain untested. Separately review buyer clarity, promise congruence, reference fidelity and mobile readability. Do not call the course, funnel or Base44 integration ready because HTML renders.
