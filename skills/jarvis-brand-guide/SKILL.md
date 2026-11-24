---
name: jarvis-brand-guide
description: "Turn a client's website research brief into three distinct brand directions (palette, typography, voice, photography and film, motion), let the member pick or mix one, and save it as the client's brand guideline. Use after jarvis-website-research, or when a member asks for branding, colours, fonts or a style for a client. Hands over to jarvis-premium-website."
---

Version: 2026-11-23.1

# Brand guide

Three directions, each one a complete and different idea, built on the research. The member picks one or mixes them. The result is the brand guideline the website is built from.

## Before you start

Read the client's website research brief from Jarvis's Data area. If there is none, say so and offer to run it first: "I need the research first, so the brand fits the market. Send: Use the website research skill to research my client's website." If the client already has a brand (logo, colours, fonts), the three directions must respect it: refine, do not replace, unless the member says to start fresh.

## Inside the website builder

When jarvis-premium-website runs this skill as part of its one-prompt flow: use the style the member chose (sleek and modern, classic and elegant, warm and natural, bold and energetic, or you decide) and the niche design profile to steer all three directions, so they are three takes on that style rather than three unrelated styles (with "you decide", make them clearly different). After the member picks, save the guideline and let the website flow continue. Do not show the hand-over line.

## Make three directions

Each direction is a clear, different answer to "who is this business for, and how should it feel?" Not three colourways of one idea. Name each in two or three words ("Heritage Craft", "Modern Precision", "Bold Local").

For each direction, decide all of these:

1. **Who it is for and why:** one line tied to a research finding (a customer type, a neighbourhood, a competitor gap).

2. **Palette:** distinct from the top local competitors in the research (say how), six colours with roles (background, surface, text, muted text, accent, deep), built and checked with [references/palette-rules.md](references/palette-rules.md). Every text pairing passes contrast; write the ratio and any "never use as" rule.

3. **Typography:** one pairing from [references/type-library.md](references/type-library.md), with sizes for headline, section heading, body and label. Never use a pairing from its "avoid as default" list.

4. **Voice:** three tone words, three sample headlines for this client, and one "never say" line that includes the niche's banned claims from the brief. Write them in the site's language and formality (see Language in jarvis-premium-website), natively, never translated.

5. **Photography and film:** one art direction paragraph (light, lens, colour, materials, people rules) and a three-shot list (hero film, detail still, mid-page film), written for Higgsfield. Real client photos always come first; generated people are never presented as real staff or patients.

6. **Motion:** one line on the personality (calm, precise, bold) and what never moves.

7. **A sample hero:** headline, one supporting line and the main button, in that direction's voice.

8. **A starter logo** made from the business name, following [references/logo-rules.md](references/logo-rules.md): a wordmark in the headline font plus one small mark, drawn in code as SVG.

## Show them

1. **In chat:** a short card per direction (name, who it is for, palette names, type pairing, one headline), a blank line between lines, then: "Which one, or a mix? For example: 2, with 1's colours."

2. **As a page the member and client can see:** ask the builder to add a private, unlinked page named Brand options to the client's website app, showing the three boards side by side in the format of [references/board-format.md](references/board-format.md). If the website app does not exist yet, create it first the way jarvis-premium-website describes, then add the page. Give the member the page link.

## Save the guideline

When the member picks or mixes, write the final brand guideline: the logo files, the chosen palette with roles and ratios, type pairing and scale, voice, photography and film direction with the shot list, motion, and the sample hero. Save it in Jarvis's Data area as the client's brand guideline, with the date and which direction it came from. Show a one-screen summary.

Then end with exactly one next step: "Brand locked. Next, I'll plan and build the site. Send: Use the premium website skill to build a website for my client."

## Rules

1. Every colour pairing used for text passes contrast: 4.5 to 1 for body text and small labels, 3 to 1 for large headings and button shapes. This includes labels, buttons, form fields, placeholders and text over images. Write the ratio; never guess it. See the visibility rules in [references/palette-rules.md](references/palette-rules.md).

2. Fonts come only from the type library, which lists fonts licensed for commercial web use. Never suggest a font whose licence you have not checked.

3. The three directions must differ in idea, type and palette, not only colour.

4. Voice never contains the niche's banned claims from the research brief.

5. Never copy a competitor's or a reference site's logo, name, photos or exact palette.

6. Plain words, short lines, a blank line between separate lines.
