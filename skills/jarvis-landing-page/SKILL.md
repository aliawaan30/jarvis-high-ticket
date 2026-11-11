---
name: jarvis-landing-page
description: Build a compact offer-led landing page, progressive application and qualified booking page from the saved offer. Use for a student B2B service funnel, with a VSL or a no-video offer-testing mode.
---

# Jarvis Landing Page

Reference-inspected instruction draft. Revised 5 November 2026 from Blake's page corrections and 4 November call. This is the student service funnel, not the longer high-ticket programme demonstration from J-374.

## Working rules
1. Where you may write: only the member's Agency HQ app (their CRM) and their Funnel app (the public pages). Use the saved app IDs. If none are saved, find and confirm them as jarvis-hq describes. Never write to any other app.
2. Ask first before creating test bookings, deleting any record, changing the brand or colours, or publishing. Label every test submission TEST and remove it after testing, with the member's yes.
3. Talk like a builder, not an engineer. No test counts, route names, file paths, colour codes or code in your messages. While a build runs, give one useful line instead of status updates. Technical detail only if asked or if the member must do something.
4. Read, don't recall. When asked about records, read them and quote the actual rows. Use saved dates for "when". Only list open items that exist in the saved record.

## Start from the saved offer

Student prompt: **“Run the landing page skill for my offer. Domain: [x]. Calendar: [link]. Video: [link or none yet].”**

Read the member's saved buyer/problem/solution brief, six-line offer, approved claims, identity and current funnel. Do not ask them to paste these again. Resolve only missing inputs that affect this build: intended offer if ambiguous, identity/domain, calendar, video mode and meaningful fit criteria. Draft without a missing calendar; ask for it and report the connection gap outside the prospect page.

The service must be understood before its headline is written: who buys, what currently happens, the consequence, what changes, delivery and what can genuinely be promised. Do not invent a guarantee or numerical outcome to complete a page. A new promise returns to offer approval rather than silently changing the service. Setup timing and result timing are different.

Build only from the approved offer in Agency HQ's Offer table (approved by member: yes). If the risk reversal or any target is still marked proposed, leave it off the page and ask: "Your guarantee isn't approved yet. Approve it to add it to the page, or build without it?"

Read [the reference analysis](references/funnel-visual-analysis.md). Use `assets/roofline/` for the approved visual/interaction pattern, after reading [its benchmark](assets/roofline/benchmark.json). Replace the example's identity, claims, questions and submission handler. Its worked roofing promise is illustrative, not verified proof or a universal student guarantee.

## Brand and colour palette (before you design)
The layout is the same for every student. The brand is theirs. Never reuse the example's colours or fonts.
1. Use the saved brand if the Funnel row has one (brand primary colour, secondary colour, font, logo link).
2. If not, ask once: "Do you have brand colours or a logo? Send them, or answer two quick questions and I'll design options for you."
3. If they have colours or a logo, build from them: take the main colour from the logo or their colour, then make 3 variations (light, dark, and one bold).
4. If they have nothing, ask two quick questions with tap options:
   a. "How should your business feel?" Bold, Calm and trustworthy, Premium, Friendly, Modern.
   b. "Light or dark page?" Light, Dark, Show me both.
5. Pick 3 different options from the palette library ([palettes](references/palettes.md)) that match their niche and answers. Each option is a different colour family and a different font. Then shift each main colour slightly using the business name, as the library describes, so no two students get exactly the same shade.
6. Show them, don't describe them. Render the top of their own page (callout, headline, button) in each option as one preview image, labelled 1, 2 and 3. If you cannot render the page, draw the preview with Pillow. Ask: "Which one? Want 3 more, or a mix?" No colour codes in the message.
7. Contrast check before showing anything: body text and button text both at least 4.5 to 1 against their background. Drop or adjust any option that fails.
8. Save the choice to the Funnel row (brand primary colour, secondary colour, font, logo link). The video ad and static ad skills reuse it. Never change it later without asking.

## The landing page, in order

0. **Header:** the logo centred at the top, no tagline.
1. **Audience callout:** the most specific line on the page: the buyer, the city, and the size the guarantee applies to when there is one, for example "For Dallas plumbing companies doing $100k+ a month".
2. **Headline:** the result they actually want, with approved timeframe and risk reversal when available. Sold jobs or cash collected can be the desire; replies and appointments are often intermediate steps. Never promise a sale when the service only supplies an appointment without an agreed basis for the downstream result.
3. **Subheadline:** one short sentence, about 30 words at most, saying what is done and the problem it stops, in everyday words. The full service description stays in the brief and VSL. Do not paste the six-line card as the headline.
4. **VSL:** a dominant 16:9 player when a video is supplied. An explicitly requested VSL draft without footage says only **“Insert VSL here”**.
5. **One application CTA:** **“See if you qualify”** or the member's approved **“Apply”**. Continue into the progressive application.

Default to the compact reference. The VSL explains deeper pain, workflow and objections. No duplicated written pain essay, numbered process, detailed guarantee block, generic FAQ, feature wall or invented testimonials underneath. Add longer sections only for an explicit different brief; do not make that exception the student default.

If there is no video and no explicit VSL-draft request, build **Offer Testing Landing Page**: callout, headline, brief mechanism and application CTA. Remove the video area entirely. Do not substitute a storyboard, fake player or hero illustration. Keep the same offer and fit rules when comparing page formats.

Keep public prices out. No countdowns, fabricated proof or scarcity. No em dashes, completion-time estimate, preparation burden, production commentary or course-example footer on the prospect page. Keep material guarantee conditions accessible without a long sales block. A work-free remedy must say internally which fee stops, the target, measurement and responsibilities; it is not automatically a refund or free software. Under the button add one small line with the guarantee's condition, for example "For plumbing companies doing $100k+ a month. Covers our fee, not your ad or tool costs."

Use the brand chosen in the palette step with a narrow centred reading column, strong headline, balanced whitespace and one next action. Compare proportions and order with the actual reference, not just its colours. The Meta non-affiliation line is optional branding copy, not a verified universal advertising requirement or a substitute for privacy information.

## Application

Use three or four useful fit questions, one per screen, then **name, email and phone together** on the final screen. Add company there only if needed; do not create a separate contact step for each field. Ask about the buyer's business and the conditions needed for this service, not irrelevant generic qualification questions. When the offer has a size qualifier, one question asks for it (for example monthly revenue ranges). Below the qualifier goes to the review page, not booking.

Preserve answers on Back. Validate each step and the final contact fields. Phone: digits, spaces, brackets, dashes and a leading plus only, at least 10 digits. Otherwise show "Enter a valid phone number." Under the phone field add one unticked checkbox: "Text me reminders about my call. Msg and data rates may apply. Reply STOP to opt out." It is optional and never blocks the application. Save yes or no with the date as texts OK.

Keep where the visitor came from. Read utm_source, utm_campaign and utm_content from the page address when they land, carry them through the application, and save them with it as one "came from" line, for example "Meta ad, hook: Missed call = lost job" (utm_content is the hook). No UTM means "Direct". Final copy: **“Where can we reach you?”** and **“Add your details below to complete your application.”** Do not mention choosing a call before they have applied. Required contact/privacy wording must match the actual sender and intended use.

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

## Meta pixel and conversion events
1. Ask once: "Do you have a Meta pixel ID yet? If not, we can skip it and add it in Module 5." Save it in the Funnel row.
2. When there is a pixel ID, install the pixel on every funnel page (landing, application, booking, confirmation) and fire:
   a. PageView on every page.
   b. Lead once, only after an application is saved successfully, never on a button click.
   c. Schedule once, only when the calendar confirms a real booking. Never on page load alone.
3. Never send names, emails or phone numbers to Meta from the page.
4. Test each event with Meta's Test Events and record it as tested, drafted or missing in the Funnel row's integration status.

## Privacy page
Before publishing, make a simple /privacy page from the student's business name, contact email and location. Cover what the form collects (name, email, phone, answers), why (to check fit and contact them about the call), who sees it (the business and its booking and messaging tools), how to opt out or ask for deletion, and the contact email. Link it under the contact step and in the footer. Tell the student once: "This is a basic template, not legal advice. Check it suits your business." Save the URL in the Funnel row.

## Review and deliver

Deliver the page files/preview, saved funnel record and a short list of missing connections. Test desktop and phone widths, every form step, Back, invalid input, retry, successful storage, each qualification route and the calendar-to-thank-you handoff where connected. In a draft, identify which checks are local simulations and which real integrations remain untested. Separately review buyer clarity, promise congruence, reference fidelity and mobile readability. Do not call the course, funnel or Base44 integration ready because HTML renders.
