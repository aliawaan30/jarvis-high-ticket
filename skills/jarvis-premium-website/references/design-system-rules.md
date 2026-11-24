# Design system rules (strict)

These rules are not suggestions. They make every site consistent: one button style, one spacing system, one alignment, on every screen size. Build the system first, then the pages.

Learned from the Fernhollow Gardens test (18 November 2026): on phones the hero image did not load and left a dark gap, the header buttons were mismatched boxes, a photo sat inside a black frame with a black band, and wrapped list lines did not align.

## 1. Build order

1. **Tokens first.** Before any page, ask the builder to create the site's design tokens from the brand guideline: colours (by role, with a Light set and a Dark set for the surface system in section 2), fonts, type scale, spacing scale, corner radius, shadows (if any), breakpoints, and motion timings.
2. **Components second.** Then the shared components, built only from the tokens: Button (three variants), IconButton, Header (with phone menu), Container, Section, ImageFrame, Card, Carousel, Tabs, Accordion, FormField, StickyActionBar, Footer.
3. **Pages last.** Pages are composed only from these components. No one-off button, spacing or image styles inside a page. If a page needs something new, add it to the components first.

## 2. Surfaces: components choose their colours automatically

Learned from the Fernhollow phone test: buttons and icons were set one by one, so a dark Menu button ended up on a dark header and a dark-text button on a dark photo. Fix it once, in the system.

1. **Every section and bar declares its surface:** Light (linen, paper, white), Dark (deep green, ink, any dark colour), or Image (a photo or film behind content, treated as Dark once its gradient is in place).
2. **Components never pick their own colours.** Text, buttons, outlines, icons, focus rings, dividers, form fields and the logo read the surface they sit on and use its matching set:

| Element | On Light | On Dark or Image |
| --- | --- | --- |
| Headings and body | Ink and muted from the palette | Linen or white, and linen at 85 percent for muted |
| Main button | Accent fill, light text | Accent fill, light text (check the accent against the dark surface, otherwise use a linen fill with ink text) |
| Secondary button | Ink outline, ink text | Linen outline, linen text |
| Icon button (Menu, Close) | Ink icon and outline | Linen icon and outline |
| Links | Ink with an accent underline | Linen with a linen underline |
| Logo | Dark version | Light version |
| Focus ring | Accent | Linen |

3. **Every pairing above passes contrast** on its surface (4.5 to 1 for text, 3 to 1 for outlines, icons and large text). Check them once when the tokens are built, and again in QA.
4. **Elements that change surface switch automatically,** for example a header that is transparent over the hero (Image surface) and solid when scrolling (Dark or Light surface), or a sticky bar over changing sections.
5. **Never set a colour on a single component inside a page** to "make it fit". Change the surface instead.

## 3. Overlays on images

1. Put the gradient **only where the text is** (for example the bottom 50 percent, or the left half), not a flat dark wash over the whole image, so the photo keeps its life.
2. The gradient is strong enough that the text passes contrast over the busiest part of the image under it.
3. Text on an image is **anchored** to an edge (usually the bottom on phones) with the section's normal padding, never floating in the middle of empty image.
4. A section that puts text over an image keeps its full context: the section label and heading go over the image too, so visitors know what they are reading.

## 4. Spacing

1. One scale only: 4, 8, 12, 16, 24, 32, 48, 64, 96, 128 px. No other values.
2. Section spacing (top and bottom): 96 to 128 px on desktop, 72 to 96 px on tablet, 64 to 80 px on phones. The same value for every standard section.
3. Side margins: 20 px on phones, 32 px on tablets, 40 px on desktop, and a maximum content width of 1200 to 1320 px.

## 5. Buttons

1. Exactly three variants: **Main** (filled accent), **Secondary** (outline or filled neutral), **Text** (text with an underline). Nothing else.
2. Main and Secondary share the same height (48 px; never under 44 px on phones), padding (0 24 px), corner radius, font, size, weight, letter spacing and text case.
3. Icon buttons are square, 44 by 44 px, with a visible label for screen readers.
4. Buttons side by side are the same height and aligned on one line; on phones they stack full width with 12 px between them, or sit in one row if both fit.
5. Every button has hover, focus (visible outline), pressed and disabled states.
6. One Main button per screen view where possible; the rest Secondary or Text.
6b. **Button labels are 2 to 4 words** that say what happens ("Book a consultation", "Get my quote"), never wrap onto two lines at any width, and never break a word (white-space: nowrap; hyphens: none). Put any detail in the text above the button, not in its label. (Found live: a long quiz button wrapped and split "low-water" at the hyphen.)
7. **Buttons on images and dark backgrounds use the light version:** light text and a light outline (or the Main fill), never the dark Secondary style. Check every button's contrast in every state it appears in.
8. **Header buttons in both header states:** over the hero image (transparent header) the button uses the light version; once the header turns solid on scroll it switches to the normal version. Check both states.

## 6. Header

1. Logo, links and buttons are vertically centred on one line.
2. Phones: logo on the left; on the right one small Main button (for example Book) and a 44 px Menu icon button (three lines), the same height, with 8 px between them. Never two mismatched boxed buttons.
3. Header height: 64 px on phones, 72 to 80 px on desktop. It never covers content: add matching top padding, or hide on scroll down and show on scroll up.
4. **No gap under the header.** Either the header sits over the hero (transparent, Image surface) or the first section starts exactly at the header's bottom edge. Never a strip of background between them.
5. **Sticky bars never cover content:** add bottom padding to the page equal to the bar's height plus the phone's safe area, and hide the sticky action bar while the section it points to (for example the booking form) is on screen.

## 7. Form controls

1. Every field (text, email, phone, select, textarea) shares the same height (48 px; textareas taller), border, corner radius, inner padding (0 16 px), font (16 px) and label style.
2. **Selects use a custom arrow:** remove the browser's default arrow (appearance none) and add a chevron icon placed with the same inner spacing as the text (16 px from the right edge), vertically centred, in the text colour. Leave room for it on the right (padding-right about 44 px) so long options never run under it. Give the builder the exact method, because "centred" alone gets built wrong:
   - As a background image: background-position: right 16px center; background-repeat: no-repeat; background-size: 16px 16px.
   - As an icon element: wrap the select in a container with position: relative; the icon gets position: absolute; right: 16px; top: 50%; transform: translateY(-50%); pointer-events: none.
   - Check: the arrow's vertical centre matches the selected text's vertical centre within 2 px, at phone and desktop sizes.
3. Labels sit above fields with 8 px between; 24 px between fields; fields in a row are the same height and aligned.
4. Focus: a visible outline in the accent colour with the same corner radius, never shifting the layout.
5. Errors: red text below the field with a clear message, and the field border in the error colour; the error colour must pass contrast.

## 8. Alignment

1. Every block lines up to the same left edge inside the container. Headings, text, buttons, lists and images share that edge unless an image is deliberately full bleed.
2. Lists with wrapped lines use a hanging indent, so wrapped lines align with the first line's text, not the bullet.
3. Cards in a row or carousel are equal height, with their buttons aligned at the bottom.
4. Text inside a card or panel has the same inner padding on all sides (24 px on desktop, 20 px on phones).
5. Numbers, labels and headings in a set (steps, services) use the same position and style in every item.

## 9. Images

1. **Images always fill their frame:** object-fit cover with a set focal point. Never shrink an image inside a frame; never leave black bars, bands or gaps.
2. Every image frame has its aspect ratio set before the image loads, so nothing jumps.
3. The first-screen image (the hero) loads immediately (not lazily), as a real image element with a set size, so it shows on phones. Every other image is lazy-loaded.
4. Every hidden film or background image has a phone still (see mobile-design.md).
5. Overlay text on images always sits on a gradient strong enough to pass contrast.

## 10. Breakpoints

| Name | Width | Notes |
| --- | --- | --- |
| Phone | 360 to 767 px | One column, phone header and menu, carousels for repeated cards, sticky action bar |
| Tablet | 768 to 1023 px | Two columns where it helps, desktop header if it fits, otherwise phone header |
| Desktop | 1024 px and up | Full layouts, 12-column grid, max content width 1200 to 1320 px |

Design and check each one. Do not let a desktop layout squeeze down by accident.

## 11. Desktop rules

1. A 12-column grid with 24 to 32 px gutters; every block spans whole columns.
2. Body text lines 60 to 75 characters long.
3. Large images may run full bleed; text never does.
4. Hover states on everything clickable.

## 12. Layout QA checklist (run before the member sees anything)

Check at 360, 390, 430, 768, 1024 and 1440 px wide. Every item must pass.

1. No empty blocks: every section shows its image or content; the hero image is visible on phones.
2. No sideways scrolling except inside carousels.
3. Buttons: one Main style, one Secondary style; every button 48 px tall (at least 44 px on phones); the same padding and radius everywhere; buttons in a row aligned; every button readable on its background, including the header button over the hero and after scrolling.
4. Header: logo and buttons vertically centred, the same height, nothing overlapping.
5. Images fill their frames: no black bars, bands or gaps; nothing stretched.
6. Alignment: one left edge per section; wrapped list lines hang-indented; cards equal height.
7. Spacing: only scale values; section spacing consistent.
8. Text: every label, button and field meets the visibility rules; no text clipped or overlapping.
9. Tap targets at least 44 px with space between them on phones.
10. Form controls: every field the same height, padding and radius; select arrows 16 px from the right edge and vertically centred (arrow centre within 2 px of the text centre); visible focus.

11. **Surface check:** every component on every surface uses that surface's set: no dark buttons, icons, outlines or text on dark or image surfaces, no light ones on light surfaces. Check the header in both states and the sticky bar over every section.

12. **Overlay check:** gradients only behind text, text anchored to an edge, label and heading kept with the text, no muddy full-image darkening.

13. **Overlap and gap check:** no gap under the header, the sticky bar never covers text, and it hides at the section it points to.

14. **Relevance and palette check:** every visual passes the relevance test (it shows the buyer, the problem, the product working or the result); no generated screens or devices; nothing off-palette.

15. **Fit check:** no text, headline or element runs past the page margins at any width, checked at every scroll position from top to bottom (before and after each animation plays, since waiting animations can widen the page); very large headlines scale down with the screen (clamp sizes) and wrap rather than overflow.

16. **Mobile excellence check:** phone-first layout, thumb-friendly actions, nothing hover-only, a mobile PageSpeed performance score recorded (aim for 90 or more).

17. **Motion check:** every signature moment from the Scroll Score plays forward and backward at 1440 and 390 px with no jumps, blank frames or stutter; reduced motion shows complete, readable still states.

18. Full-page screenshots at 390 and 1440 px reviewed as a whole: varied rhythm, no repeated runs, the action always reachable.

Fix every failure and run the checklist again before the client review.
