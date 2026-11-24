# Mobile design

Most visitors arrive on a phone. Design the phone version on purpose, not as the desktop squeezed into a column.

Learned from the Fernhollow Gardens test (18 November 2026): on phones the films and background images were hidden with nothing in their place, leaving five large empty dark blocks (hero, quote break, seasons, service areas, closing); there was no menu; and services and steps became eight identical picture-then-text blocks in a row.

## 0. Mobile excellence (the standard, not just the absence of bugs)

Most of the client's customers will see the site on a phone, so the phone version must be outstanding, not merely working.

1. **Phone first.** Plan and build each section for a 390 px screen first, then expand it for tablet and desktop.
2. **Thumb friendly.** The main action sits in easy reach of the thumb (the sticky action bar at the bottom), everything works one-handed, and tap targets are at least 44 px with space between them.
3. **Fast.** The first screen is useful within about 2.5 seconds on a phone connection. Aim for a Google PageSpeed (Lighthouse) mobile performance score of 90 or more, and record the score in the test step.
4. **Nothing depends on hover.** Anything shown on hover on desktop (previews, image swaps, tooltips) has a tap or swipe version on phones.
5. **A phone wow moment** (see the phone versions in motion-system.md). The phone version gets its own moments of craft: the hero loop, swipe carousels with the next card peeking in, smooth reveals as sections arrive, a tidy full-screen menu. It should feel like an app, not a squeezed web page.
6. **Phone review before anyone sees it.** Take full-page screenshots at 390 px and look at every screen in turn. If any screen looks empty, cramped, repetitive, off-brand or hard to read, fix it before the member's review.

## 1. Every image has a phone version

1. **Never hide an image without a replacement.** If a film or background image is turned off on phones, show a still image in its place.
2. **Films on phones play as a quiet loop, not a scroll film.** Scroll-controlled films feel jumpy with phone scrolling, so on phones the hero film plays on its own as a short muted loop:
   - A separate phone version of the film: portrait or tall crop, 720p, about 5 to 8 seconds, no audio, H.264 with fast start, ideally under 3 MB.
   - Video settings: muted, autoplay, loop, playsinline, preload metadata, with the film's best frame as the poster image, object-fit cover.
   - The poster still always shows first and stays if the phone blocks autoplay (iPhone Low Power Mode, data saver), if the visitor prefers reduced motion, or if the video fails.
   - Other films (mid-page chapters) stay as stills on phones unless the member asks, to keep the page light.
3. **Crop for the phone:** tall sections need a portrait crop (4:5 or 9:16) with the subject kept in frame. Set the focal point (object-position) per image, or use a separate phone image with the picture element.
4. **Plan it before generating:** the image role map lists each image's phone shape. For key images (the hero, chapter breaks), generate or choose a tall version as well as the wide one.
5. **Text over images on phones:** stronger gradients only where the text sits, because phone crops put text over busier parts of the image. Anchor the text to the bottom with the section label and heading included, never floating mid-image. Recheck contrast at phone width.

## 2. Phone header and navigation

1. A compact header: logo on the left; on the right a Menu button and the main action (Call or Book) as a small button or icon.
2. Menu: full screen, large tap targets, the main action at the bottom, closes with a close button and the Escape key, focus moves into it and back.
3. The header may hide when scrolling down and return when scrolling up, so it never covers content.

## 3. Phone rhythm (no repetition)

1. **Never more than two picture-then-text blocks in a row.** Change the pattern.
2. **Repeated cards become a swipe carousel:** one card wide with the next one peeking in, smooth scroll snapping, dots or a count, and visible on keyboard. Use it for services, steps, galleries and journal posts.
3. **Long lists become accordions** (FAQ, detailed services).
4. **Vary the phone sections too:** a full-bleed image, a carousel, a text-only section with a big quote, a list, a form.

## 4. Phone versions of the image patterns

| Desktop pattern | Phone version |
| --- | --- |
| Scroll film hero | Full-screen muted loop of the phone film version (poster still as fallback), headline and button at the bottom over a gradient |
| Full-bleed chapter break | Tall image (about 70 percent of the screen) with the line of text over a gradient |
| Edge-to-edge split | Full-width image above the text, no side margins |
| Sticky image, scrolling steps | Swipe carousel: one step per card, image on top |
| Hover or focus preview list | Swipe carousel, or a tap list where the image above changes |
| Tab image swap | Image on top, tabs as a single row of scrollable pills below it, text under the tabs |
| Overlapping pair | Keep the overlap smaller, or show only the main image |
| Panorama band | Portrait crop with the names over it, or the image above with the names below |
| Image as section background | Image as a band on top, text on a solid colour below, unless the text is short |

## 5. Phone basics

1. Hero fills the screen (use 100svh, not 100vh, so phone address bars do not cut it off), with the headline and the main button visible without scrolling.
2. Sticky action bar (Call, Book or Quote) from the second screen onward, clear of the phone's home bar (safe area).
3. Tap targets at least 44 by 44 pixels, with space between them.
4. Section spacing about 64 to 80 px top and bottom; side margins 20 to 24 px.
5. Type: hero 40 to 52 px, section headings 30 to 36 px, body 16 to 17 px, labels at least 12 px.
6. Form fields 16 px text (so phones do not zoom), one column, the keyboard type matched to the field (email, phone).
7. Images lazy-loaded, sized for the phone, about 200 KB or less each.
8. No horizontal scrolling anywhere, except inside carousels. Grid and flex children can shrink; long words and numbers wrap or scale down; huge headlines never break a word mid-line.
9. Pinned scenes fit one phone screen with headroom for the header and the action bar; a story scene keeps its timeline and simulation on phones.
10. Collapse content on phones (accordions, condensed rows, tap to expand) instead of hiding it; side-by-side layouts stack with the explanation first and the visual second; demos and mockups switch to a taller shape.

## 6. Test on phones before review

1. Check at 360, 390 and 430 px wide, and once in landscape.
2. Take a full-page screenshot at 390 px and look at it as a whole: no empty blocks, no long repeated runs, every image visible and well cropped, the action always reachable.
3. Open the menu, swipe each carousel, use the tabs, the quiz and the form with touch.
4. If possible, check on a real phone through the review link.
