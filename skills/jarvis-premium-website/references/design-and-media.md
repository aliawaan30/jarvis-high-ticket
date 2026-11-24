# Whole-page design and media decisions

> **Version 3 evidence.** Kept for its tested methods and results. Where it differs from the version 4 files (Higgsfield instead of Envato or Kie, the phone video loop, one enquiry pipeline owned by the website, the design system and surface rules), the version 4 files win.


Read this when creating the direction and shot list. The five examples are tested references, not a rule to reuse the same content on unrelated businesses.

| Business | Governing idea | Lower-page composition | Primary and second motion |
| --- | --- | --- | --- |
| Surf | Athletic, salty, direct | Oversized condensed statement; offset portrait surfboards; contrasting session chooser | Existing surfer ride; separate empty-barrel water shot |
| Restaurant | Unhurried, warm, tactile | Centred serif editorial opening; small seal; portrait food beside ruled menu | Slow kitchen dolly; close fire and grill detail |
| Landscape | Organic form with structural clarity | Open introduction; two-column prose; tall botanical crop and material swatches | Travel along curved path; water bowl and grasses |
| Architecture | Space, margin and material | Separate masthead; wide project study; narrower staircase photograph and text | Exterior parallax; interior move toward courtyard |
| Product | Quiet object, close attention | Precise typography and material rows; full product-in-room image | Stable lamp with camera parallax; metal reflection study |

The source-only HTML/CSS examples in `../assets/source-layouts/` show exact compositions that were rendered locally. Their images and fonts live in the separate complete reference-site archive; these source copies are not standalone runnable pages. View the approved full-page compositions in `screenshots/surf.jpg`, `screenshots/restaurant.jpg`, `screenshots/landscape.jpg`, `screenshots/architecture.jpg` and `screenshots/product.jpg`. They are starting references. Keep their relationship between media, content and spacing rather than copying a section name or enforcing a hard-coded height on every business.

## The section brief

For every section write: visitor question, content answering it, composition, asset, action and phone arrangement. Example:

- Visitor question: what kind of food is this?
- Content: three approved dishes, their components and a route to the full menu or reservation.
- Composition: a portrait food image beside a narrow ruled menu, with a large serif introduction.
- Asset: one sharp overhead plated dish, burgundy linen, warm ceramics, matching the hero's palette.
- Action: the real booking or menu destination. In the local lab, save an evening direction instead of a fake booking.
- Phone: image first, menu below, readable rules and generous tap areas.

If the business has no real menu, project images, service information or actual booking destination, do not fill the gaps with invented commercial claims. Ask for the missing high-value content. The agent should be proactive about requesting useful assets, not passive about accepting an empty page.

## Shot briefing

Keep a shared art-direction paragraph: material, light direction, palette, contrast, lens character and realism. Add a separate composition instruction for each intended crop. Keep text as HTML.

For stills, specify the complete subject, its position, the scene around it and exclusions that matter. For an actual client product, use a reference image. Generated identity must be visually compared across views. The local lamp's first room view changed its stem; a reference edit corrected it.

For motion, specify one shot, camera path, subject movement, invariant geometry and a clear ending. "Cinematic, premium, smooth" alone leaves too much unspecified. A request to orbit a product, fly through a window, follow a person and change scenes in one clip has multiple independent failure points.

The local Kie pilot used Seedream 4.5 basic and Kling 2.5 Turbo image-to-video Pro. These names and prices are observations, not permanent defaults. Verify current model support and account cost before a new job. The tested Kling route accepted `image_url`, `prompt`, `duration`, `negative_prompt` and `cfg_scale`. Do not add unsupported resolution or quality fields and then claim they were applied.

Use the provided source prompts in `../assets/media-prompts.json` only when their composition is relevant. They record the real jobs used by the lab. Do not regenerate reference media already attached to an import task.

## Quality gate

Inspect at least six points across a clip, including its ending. Check geometry, continuity, composition and usable detail. Inspect the actual phone crop. Reject legible nonsense branding and inconsistent client products. Trim a weak tail if the retained action still works. The surf source was trimmed before its weak ending; the shorter result is preferable to a flawed longer clip.

A ten-second clip can make a longer progression possible, but duration alone does not improve seeking. Encode and test it. The reference processing used H.264/yuv420p, no audio, faststart, GOP 8 and CRF 23 at 1600px width, preserving aspect ratio. Those settings produced roughly 1.4 to 7.4 MB clips in this batch. Tune and inspect rather than promising a fixed file size or load time.

Avoid placeholder intensity. Large numerals, extra empty padding and giant slogans do not replace supporting imagery or content. Judge the whole page at once, then inspect the important sections at readable scale.
