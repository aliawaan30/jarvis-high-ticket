# Palette rules

## Six roles, always

| Role | Use |
| --- | --- |
| Background | The page |
| Surface | Cards, bands, panels |
| Text | Body and headings |
| Muted | Secondary text, labels |
| Accent | Buttons, key numbers, highlights. One accent only |
| Deep | Dark sections, footer, sticky call bar |

## How to build one

1. Start from the research and the photography direction: the palette must belong to the same world as the images (golden hour gives warm neutrals; blue hour gives cool greys).

2. Pick the accent first, from the niche and the competitor gap (if every Dallas med spa is blush pink, a deep green or warm stone stands apart).

3. Build background and text for contrast, then the surface one step from the background, the muted text one step from the text, and the deep colour for dark sections.

4. Check every pairing that will hold text, and write the ratio next to it.

## Contrast (WCAG)

- Body text: at least 4.5 to 1. Aim for 7 to 1 or more for long reading.
- Large headings (24 px and up, or 19 px bold) and buttons: at least 3 to 1.
- Check text on background, muted on background, text on surface, button text on accent, light text on deep.
- If a pairing fails, do not use it, and write the rule: "Copper is never text on Pine (2.0 to 1)."

How to calculate: relative luminance L = 0.2126 R + 0.7152 G + 0.0722 B, where each channel c (0 to 1) is c / 12.92 if c is 0.03928 or less, otherwise ((c + 0.055) / 1.055) to the power 2.4. Ratio = (lighter L + 0.05) / (darker L + 0.05). Calculate it; never estimate it.

## Visibility (every piece of text)

1. **Small text needs more, not less.** Labels, captions, form placeholders and footer text are small, so they need at least 4.5 to 1. Do not use the muted colour for tiny uppercase labels on a light background unless it passes; use the text colour at a smaller size instead.
2. **Minimum sizes:** body 16 px, labels and captions 12 px, buttons 15 px, form text 16 px (so phones do not zoom).
3. **No thin weights for small text:** below 18 px, use regular weight or heavier.
4. **Text over images:** check contrast against the busiest part of the image under the text, not the average. If it fails, add a gradient or tint overlay in a brand colour until it passes, or move the text to a calm part of the image.
5. **Buttons and form fields on dark sections:** borders and text must pass too; outline buttons on dark backgrounds often fail, so check them.

## Taste

- Prefer warm or cool tinted neutrals over pure white (#FFFFFF) and pure black (#000000) for large areas.
- One accent. Two accents is a brand problem, not a design choice.
- Avoid the generic defaults: bright startup purple, blue to purple gradients, neon on black, unless the brand truly calls for it.
- Respect the client's existing colours when they have a real brand. Refine them, do not discard them.
