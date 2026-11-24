---
name: jarvis-premium-website
description: "Build a complete premium website for a client in Base44 from one prompt: a short intake, research, three brand guidelines to choose from, then the plan and cost, Higgsfield images and films, the build, testing, review and launch: a researched section plan, art-directed Higgsfield images and scroll films, a native Base44 frontend, real enquiry handling, SEO, launch checks and handover. Use when a member asks to build, design or rebuild a website for a client."
---

Version: 2026-11-24.7 (premium website v4; builds on v3.0.0, approved 10 September 2026)

# Premium website

Build the whole site for one business, from one research brief and one brand guideline. Every section has a reason from the research. Every image and film belongs to one art direction. Every button leads somewhere real.

## The model for website builds

Website builds need the strongest model: research, design, copy and the build all benefit. Use Claude Opus 5.5 for this skill. At the start, if you are not running on Claude Opus 5.5 (or you cannot tell), tell the member in one line before the intake: "For the best website, switch me to Claude Opus 5.5 in my Agent Settings (it uses more credits). Say ready when done, or continue to use my current model." If they continue, carry on.

## How it starts: one prompt

The member sends: "Use the premium website skill to build a website for my client. Ask me what you need first." From there you run the whole flow yourself; the member never needs another skill prompt.

1. **Intake, one message.** Ask only what is not already known (check the client record in Agency HQ and memory first), numbered, with a blank line between questions. For niche extras, use the intake question bank in the jarvis-website-research skill.

   1. The client: business name, niche, city and area.

   2. The style they want: sleek and modern, classic and elegant, warm and natural, bold and energetic, or "you decide".

   3. Contact details for the site: phone, email, address, opening hours, booking link, and the email address where new enquiries should be sent.

   4. Services, and prices or "from" prices; licences and certifications.

   5. What they already have: logo, colours, fonts, photos, real reviews.

   6. The one action the site must drive, sites they like, and anything they must have or must never have.

   7. The site's language, and for languages with a formal and an informal "you" (Dutch je or u, German du or Sie, French tu or vous), which one.

2. **Research, then the visual approach.** Run the six research layers from jarvis-website-research yourself (skip its intake; you just asked). Save the brief. In one message, show a short summary (the five most useful findings and the niche design profile in two lines) and **recommend a visual approach** with a one-line reason, listing the others:

   - **Cinematic:** Higgsfield films and photos, a transformation scroll (media level 3). For businesses whose work or place is what people buy.
   - **Photo-led:** the client's real photos or a few Higgsfield stills, calm motion (media level 2).
   - **Diagram-led editorial:** animated diagrams, a code-built story scene and live demos, no generated media (media level 1).
   - **Typography-led minimal:** large expressive type, colour and space, very few visuals (media level 1).

   Ask: "Reply go, or pick another approach." Use [references/image-direction.md](references/image-direction.md) to recommend, and the niche design profile's recommended approach as the starting point.

3. **Brand.** Run jarvis-brand-guide yourself, steered by the chosen style, the chosen visual approach and the niche design profile. Show the three brand guidelines (each with its starter logo) and ask the member to pick one or mix them. If a confirmed brand guideline already exists for this client, show it in a few short lines and ask "Build with this brand, or change anything first?" instead. Never build on a brand the member has not confirmed in this conversation.

4. **Higgsfield, only when needed.** Most sites need no generated media (media level 1, code-built visuals). Connect Higgsfield only when the chosen media level is 2 or 3, at check-in 1, never before. Higgsfield is then the only source for generated images and films. If the keys are not saved yet, run the first-time connection in [references/higgsfield-prompting.md](references/higgsfield-prompting.md) and the one-image test. If no **media budget** is saved, ask once: "How much can I spend on images and videos per website without asking? I suggest 15 US dollars." Save the answer in memory and reuse it for every website.

## Four kinds of website

Ask which one this is if it is not clear from the request.

1. **A client's website** (the default): everything in this skill as written.

2. **The member's own agency website.** The member is the client. Differences:
   - Research targets the member's buyers (for example Dallas roofers who miss calls), not "AI agencies". Use the AI agencies and tech services design profile: lead with the product working (code-built live demos, a demo call player, before and after websites), not cinematic scenery.
   - No invented results, clients, case studies, reviews or numbers. A new agency shows its offer, its process, its guarantee from the approved offer, and its demo sites clearly labelled as concept work.
   - No earnings or income claims of any kind. Results claims only when real and provable.
   - Enquiries go into the member's own Agency HQ as new leads (server to server with the HUD key, through the HQ app's upsertLead function) and email the member. The rest of the enquiry rules in client-delivery.md still apply.
   - Reuse the member's approved offer and brand if they exist; confirm them instead of making new ones.
   - Keep the funnel separate: the Module 3 landing page is still the member's sales funnel; this site adds credibility and a portfolio.

3. **Upgrading an existing site.** The member already has a website (often built earlier with this skill or another tool) and wants it brought up to this standard. Differences:
   - Read the existing app first: its pages, sections, content, forms, brand and media. Keep the content, the brand, the forms and the enquiry pipeline unless the member asks to change them.
   - Audit it against this skill: the relevance test and media plan, the Scroll Score and motion system (including the recipe for its niche), mobile excellence, the design system and surface rules, and the layout QA checklist. Show the member a short list of what fails and the upgrade plan, with a Scroll Score, any new Higgsfield shots and their cost and time, as check-in 1.
   - Upgrade in place in the same app, section by section, testing after each, and never deleting content the member did not ask to remove.
   - Before reporting the upgrade as ready for review, finish every check: the layout QA at all six widths, reduced motion, the motion check, every new section by eye, and the wow pass. Report the component read-back (the builder's files match the tested components exactly) and list anything still unchecked.

4. **A demo site for a prospect** (to help close a deal). Differences:
   - Use only public facts about the prospect (their real services, area and contact details from their own site or Google profile), and mark anything else in [brackets].
   - Label it clearly as a concept: a small "Concept by [agency name]" note in the footer, and keep it out of search engines (noindex).
   - Never use the prospect's logo or photos without permission; make a starter logo and generated images instead, and say so.
   - Do not connect a domain or real enquiry destination; the form shows "This is a concept site" instead of submitting.
   - Keep it light: Premium tier, one hero film at most, so it costs little. Tell the member the cost first as usual.

## The work, with three check-ins

**Check-in 1: the plan and the cost (one message, one approval).**

- The site plan as a numbered list of sections, using [references/section-patterns.md](references/section-patterns.md): ordered by the buyer's questions (see Section order there), each with its pattern, headline and action. Include a story scene, diagrams, a before and after or an estimator only where their trigger is true, and say which trigger, and its phone version from [references/mobile-design.md](references/mobile-design.md). Follow the niche design profile: patterns that fit, none it says to avoid.
- The **media level** (1 Opus only, 2 a few photos, 3 cinematic) from [references/image-direction.md](references/image-direction.md), with a one-line reason; level 1 uses the code-built visuals in [references/code-visuals.md](references/code-visuals.md). Then the **media plan**: first the media type from what the site sells (the relevance test: every visual shows the buyer, the problem, the product working or the result), then each image's role, desktop shape, phone shape and shot, and any code-built demos. The **variety check** passes.
- The **wow plan** from [references/wow-pass.md](references/wow-pass.md): the one brand idea, the immersive signature moment that expresses it, the two bold compositions, and how the palette and type differ from the local competitors.
- The **component list:** the 8 to 12 tested components this site will use, each tied to a section and its trigger.
- The **Scroll Score** from [references/motion-system.md](references/motion-system.md): every section's motion by name, and the three to five signature moments (usually including a transformation scroll of the client's real result).
- The tier: Premium (art-directed stills, light motion) or Cinematic (films where they earn their place). Decide the hero with the video test in image-direction.md ("Does the hero need a video?") and say why in one line; a hero video is never the default.
- The shot list, written with the look line and shot recipe in [references/higgsfield-prompting.md](references/higgsfield-prompting.md), with one line for the estimated cost and time (for information when it is within the media budget).
- Ask: "Shall I build it?" This is the plan approval; there is no separate cost approval when the estimate is within the media budget. If it is over budget, say so in the same message and offer a cheaper option (fewer films, or the Premium tier) or a higher budget for this site.

**Then do the work without stopping:**

1. **Copy.** Write all page copy in the guideline's voice from the research and the client's confirmed facts. **Language:** write natively in the site's language as a local copywriter would, never translated from English: short sentences, local phrasing and examples, one formality used consistently. Reread every line for literal translation before the review, and for any language other than English, recommend a native speaker reads it before launch. Banned claims from the brief never appear, including in image text and alt text. Unconfirmed facts stay in [brackets].

2. **Media.** Use the client's real photos first, then the code-built visuals in code-visuals.md. Only at media level 2 or 3, generate the rest with Higgsfield, always: never Base44's built-in image generation, other generators, stock photos or placeholders, unless the member explicitly asks for something else. Before generating, check the keys HIGGSFIELD_KEY_ID and HIGGSFIELD_KEY_SECRET exist; if they are missing or rejected, stop and say so, open the secure secret card, and never fall back silently to another source. Generate following [references/higgsfield-route.md](references/higgsfield-route.md) and [references/higgsfield-prompting.md](references/higgsfield-prompting.md): generate within the media budget without asking again (stop and ask only if a job would go over it or the Higgsfield balance runs low), pause any background goal, submit all shots together, drafts first, then finals for the best ones, images before films (films are made from the approved stills), and the quality gate in [references/design-and-media.md](references/design-and-media.md) plus higgsfield-prompting.md. Explain any Higgsfield error in plain words, as that file says, and wait only when the member must act (for example adding credit).

3. **Build.** Install the motion tools (gsap@3.15.1 and lenis@1.3.27; Three.js only if a 3D object is the story) and add only the tested components the plan uses (usually 8 to 12, plus motion.js) from [assets/signature-mechanics](assets/signature-mechanics/README.md), exactly as given, following its hand-off rules: the builder gets the exact code, never a description to reinterpret. First the design system, following [references/design-system-rules.md](references/design-system-rules.md): the tokens from the brand guideline, then the shared components (buttons, header, sections, image frames, cards, carousels, tabs, form fields). Then build the hero first, then one section at a time, phone and desktop together, checking each before the next. Build the pages in the client's website app using only those components, following [references/v3-build-method.md](references/v3-build-method.md) for structure, scroll films and phone, reduced-motion and failed-media behaviour, and [assets/runtime.js](assets/runtime.js) for the tested film mechanics. Apply the logo (header, footer, browser tab icon, social preview image), palette, type scale, motion, and the composition rules in image-direction.md. Build the phone version on purpose with mobile-design.md. Build every motion exactly as the Scroll Score names it, with its phone and reduced-motion versions. Hide sections with no real content yet (portfolio, reviews, team). The five sites in [references/screenshots](references/screenshots) and the previews in [references/quality-bar](references/quality-bar) show the level to reach (composition, the lower half of the page, signature moments); they are never templates to copy.

4. **Connect.** Build one enquiry pipeline in the client's own website app and wire every form to it, following [references/client-delivery.md](references/client-delivery.md): saved in the site's own Enquiry table, the client emailed, the visitor confirmed, and only then a copy forwarded server to server to the member's Jarvis if wanted. Never post from the browser to another app, and never show a success message for something that was not saved.

5. **Test.** You cannot run a real browser inside Base44, so the checks that need one run on the member's devices through SiteCheck and [references/member-checklist.md](references/member-checklist.md). Do everything you can yourself (read-backs, code review against the rules, the wow pass on your screenshots), then ask the member for the site check reports from their phone and computer, and fix until they pass. Run the layout QA checklist in design-system-rules.md at 360, 390, 430, 768, 1024 and 1440 px; every item must pass. Then the browser checks in [references/base44-and-qa.md](references/base44-and-qa.md), the **legibility check** (every text style on every background it sits on, including buttons in every header state and text over images), the **phone test** in mobile-design.md, the **motion check** in motion-system.md (every signature moment plays forward and backward on phone and desktop, no stutter, complete with reduced motion), and the launch checks in client-delivery.md. Fix what fails and rerun.

**Then the wow pass:** run [references/wow-pass.md](references/wow-pass.md): the five-second test, then the critique loop twice (screenshot, critique like an award jury, fix the top three), then the layout QA again.

**Check-in 2: the review.** Give the member the real-device checklist first; the review is ready when the site check passes on their phone and computer, the wow pass is done twice, and the component read-back matches. Show the phone version first, then desktop, with a review link, a short list of what to check, and what Higgsfield cost for this site. Text changes, image swaps and section changes happen here. Make them, retest the affected parts, and confirm.

**Check-in 3: launch.** Get every sign-off the brief requires (for example a Texas med spa's medical director approving the content). Then publish, connect the client's domain, and hand over, following client-delivery.md. Move the client's stage in Agency HQ as each step completes.

## Learning from every build

1. **Before planning,** read the saved "Website lessons" in memory for this niche and for this member, and let them shape the plan (for example "Trades: the member replaced the hero video with a still; lead with the phone number").
2. **After each review and after launch,** save short lessons in memory under "Website lessons": the niche, what the member changed, what they kept or praised, and what they asked to remove. One line each, no client personal details.
3. **When the member asks to export lessons** ("Export my website lessons"), give them as a plain list grouped by niche, so they can be shared and folded into this skill.

## Creating the client's website app

If the client has no website app yet, give the member this message for the Base44 build box, word for word, then check the app exists before continuing:

```text
Create an empty app named [Client business name] Website. Only a single blank placeholder page. Do not add features, entities or designs yet. I will build the pages next.
```

Save its app ID in memory as the client's website app ID. Work only in that app and the member's Agency HQ, by their saved IDs.

## Quality bar (what makes it premium)

0. **Fully responsive, first.** The site must be excellent at every width from 360 to 1440 px and on a real phone. Any overflow, cramped header, broken word, hidden content or unusable control at any width blocks the review; nothing goes to the member until every width passes.

1. One governing idea per site, from the guideline. Every section belongs to it.

2. The lower half is as strong as the hero: real content, varied compositions, a proper image for each section that needs one, readable type.

3. Every section has one job and one action. No filler sections, no decorative numbers standing in for content.

3b. Memorable, not just correct: one brand idea, an immersive signature moment, bold compositions and a look distinct from local competitors, proven by the wow pass.

4. Consistent by system: every button, spacing value, header item and image frame comes from the shared components and follows the strict rules; nothing one-off. Components take their colours from the surface they sit on (light, dark or image), so nothing is ever dark on dark or light on light.

5. The phone version is excellent, not just working: designed phone first, thumb friendly, fast (mobile PageSpeed score recorded, aim 90 or more), nothing hover-only, its own wow moments, and no empty blocks, a phone menu, swipe carousels for repeated cards, and every image cropped for the phone.

6. Every section is different: no repeated layout and image treatment, the image on alternating sides, the signature frame at most twice, and every image fits its section's meaning.

7. Images are composed, not placed: at least two full-width image moments after the hero, at most one even grid of cards, at least three image shapes, and images that interact with the design in at least two sections.

8. Motion is planned, not sprinkled: a Scroll Score with three to five signature moments that tell the client's story, quiet consistent motion elsewhere, built with named tools (motion-system.md). Films are scroll-controlled with native scrolling on desktop, never a hijacked wheel. On phones the hero film plays as a short muted loop with its still as the fallback; reduced motion and data saving get the still.

9. Fast: compressed media, the second film loads near its section, nothing heavy before the first screen is useful.

10. Accessible: real links, readable text everywhere (see the legibility check), and buttons, keyboard and screen reader friendly, contrast from the guideline.

## Rules

1. Never invent facts, reviews, credentials, prices, awards, team members or results. [Brackets] until confirmed, and none left at launch.

2. **Every site is unique.** Reuse the method, never the output: a new story scene (when one is used), new diagram metaphors (when used), a new hero composition and new headlines for every client. Never reuse a previous site's copy, mock businesses, demo scripts or layout order, even for the same niche. Website lessons in memory carry methods and preferences only, never another client's content.

3. Never present generated people as the client's real staff, customers or patients. Never use generated "before and after" images.

4. Never copy a reference or competitor site's photos, copy, logo or identity.

5. **The website owns its media.** Every image, film and frame the site uses is stored in the client's own website app (uploaded to its storage), never loaded from another app or from your own workspace, so the site keeps working if anything else changes.

5b. **Media is generated by you, never by the website.** Call Higgsfield yourself with the keys in your own secrets, then upload the finished files into the website app. Never add a Higgsfield function, key or any paid AI generation to the client's website app, and if the builder asks for Higgsfield secrets, tell the member to press Skip. A public site holding a key that spends money is a security risk.

6. Spend only within the member's media budget (or an amount they approved for this site). Save every generation request ID and its cost, and report the total at the review. Generated media comes only from Higgsfield; if Higgsfield cannot be used, stop and tell the member instead of switching source.

7. Build and publish are separate. Verify the exact app, route and published state; do not resend builds to fix an unverified publish.

8. Do not call the site client-ready until the layout QA checklist and the launch checks pass at every width and the required sign-offs are in.

9. Plain words in chat, short lines, a blank line between separate lines, one next step at the end of each message.
