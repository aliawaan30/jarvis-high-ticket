# Premium websites: research translated into five working tests

> **Version 3 evidence.** Kept for its tested methods and results. Where it differs from the version 4 files (Higgsfield instead of Envato or Kie, the phone video loop, one enquiry pipeline owned by the website, the design system and surface rules), the version 4 files win.


Research and implementation date: 10 September 2026.

## Finding

The reliable starting point is a complete visual and content system, followed by media generation and implementation. A scroll video is one component. It does not solve content hierarchy, image consistency, section composition, navigation or the visitor's next action.

This experiment builds five different business concepts with the same small motion runtime, but different typography, image crops, section arrangements, colours and content. Each has a moving hero, ordinary editorial sections, a second moving chapter and a working direction selector with a text download. This deliberately tests a two-film pattern requested by Blake. It is not a prescription that every client site should have two pinned films.

The evidence supports local technical feasibility. It does not establish a sale price, conversion uplift, fresh-agent repeatability, Base44 deployment success or Blake's aesthetic approval.

## What the references actually contribute

The source selection combines creator-written case studies with real business websites. These are useful exemplars, not an objective ranking of the world's best websites. The live business sites were inspected through their public content; their entire interactive experience was not audited here.

| Source | Observation supported by the source | Decision tested here |
| --- | --- | --- |
| PX PUSH, creator case study [1] | One governing identity connects its effects and components. Its creators discuss shared animation lifecycle and native mobile scrolling. | Give every business a coherent material and type system; share lifecycle mechanics rather than a universal visual template. |
| Troa portfolio, creator case study [2] | The project discusses rendering, media and performance decisions as part of the experience. | Process originals into smaller web files, retain stills and load the second film near its section. |
| NOD bootcamp, creator case study [3] | Pacing and motion were considered in prototypes, with a distinction between triggered and scroll-controlled movement. | Separate the pinned chapters with real reading space. Do not attach scrubbing to every paragraph. |
| Norm Architects [4] | The portfolio organises work into architectural and design categories, with named projects and substantive descriptions. | The architecture test needs a project composition and material context after its hero, rather than another generic benefit grid. |
| Audo Copenhagen [5] | Product discovery is supported by furniture, lighting, accessories and contextual brand content. | A product needs to be seen in use and in detail, not only as a single studio cutout. |
| Noma [6] | The restaurant site provides routes into its dining and wider food world. | The restaurant test connects atmosphere with food and a meaningful planning action. A cinematic kitchen cannot replace menu content. |
| Aesop [7] | The site combines product discovery, explanatory content and shopping actions. | Visual restraint still needs concrete content and a usable destination. Spaciousness is not a substitute for information. |

These are design inferences from the sources, not claims that adopting a font or effect reproduces their commercial results. No source code, photography or brand assets from these reference businesses were copied into the five concepts.

## Attributes that matter below the hero

1. **Image coverage.** Plan a subject, an environment, a detail and an in-context view. Assign each an actual section and crop before paying for generation. We generated portrait food, planting, surfboard, architectural and room images specifically for lower sections.
2. **Continuity.** Lighting, material, lens character and colour should belong to the same world. Prompting separate images with the same vague style did not fully preserve the lamp's shape. A reference-guided correction was needed for the room image. Exact client products should use approved reference photography and comparisons, not imagined specifications.
3. **Hierarchy at section scale.** One dominant headline or photograph per composition, enough body copy to explain its purpose, and a real onward action. A large numeral and excess padding do not supply substance.
4. **Different rhythms.** Surf uses condensed type, an offset board photograph and acid-colour selection section. Restaurant uses centred serif composition, a seal, food photograph and ruled menu. Landscape uses botanical form and material swatches. Architecture separates the masthead from the film and uses differently sized project images. Product uses a studio view, material details and an interior scene.
5. **Editorial variety without random decoration.** Across a page, vary image size, column balance, background and information density. Across businesses, change the visual grammar, not just the accent colour.
6. **A specific visitor task.** The local prototypes allow a visitor to choose and download a relevant brief. They do not pretend to book a table, sell a lamp or send an enquiry to fictional staff. A real client version needs the actual booking, enquiry or checkout integration and approved business information.
7. **Mobile art direction.** A universal 65% crop failed for the surfer and lamp. Both were repaired using an image-led upper region and ordinary headline area below. Other compositions retained full-height photography. The subject and readable type both matter.
8. **Motion pacing.** A 10-second source does not require ten seconds of scrolling. The section's physical travel determines how quickly the visitor samples it. Here the hero starts at 250vh and the second chapter at 185vh; these are tested starting values, not a quality metric.
9. **Restraint between peaks.** The middle sections remain usable without animation. Extra particles, decorative caption beats, cursor replacements and perpetual loops would compete with the film and the content.
10. **Evidence on the actual build.** Time samples, decoded frames, browser interactions and screenshots answer different questions. None can replace the others.

## Generation experiment

Provider: Kie. Stills: Seedream 4.5 basic, including a later reference-guided edit. New videos: Kling 2.5 Turbo image-to-video Pro. Four 10-second heroes and five 5-second detail chapters. The existing surf hero was reused and trimmed to 6.8 seconds before its weak ending.

The nine new video jobs all completed. Each was inspected in six distributed frames. Their deliberately restrained motions preserved the principal environment or object well enough for these concepts. This does not demonstrate reliable complex choreography, exact surfing physics, continuous multi-location fly-throughs or exact product reproduction.

The watched outputs show clear motion in the environment films. The lamp and ember films are subtler. Longer is not automatically more dramatic: motion amplitude and camera path need to be explicit in the shot brief. A future high-energy concept should test a carefully bounded action independently before committing the whole page to it.

The new batch initially used 617.5 credits: 71.5 for eleven text-to-image stills and 546 for nine videos. A single image correction was then added within the disclosed 650-credit cap. The final cost and each provider-reported deduction are recorded in media-state.json and TEST-REPORT.md. Previous completed stills and the existing surf video are reused assets with earlier costs, not included in this batch subtotal. Current published pricing is a snapshot, not a promise for future students. [8][9]

No authenticated API key is shipped in the site. Generation records remain outside the served site directory. A job is persisted before its paid submission and is polled by task ID. An ambiguous response must be investigated rather than resubmitted automatically.

## Implementation experiment

The local pages use explicit CSS and vanilla JavaScript. This avoids a hidden dependency on a chat preview's injected Tailwind stylesheet. The shared film runtime reads actual sticky travel, updates on scroll using requestAnimationFrame, serialises seeks and follows the latest target after seek completion. Repeated seek stalls trigger still mode. It stops scheduling offscreen and when the document is hidden, aborts pending fetches on teardown, revokes Blob URLs, and restores the runtime when returning from browser history.

Desktop media is fetched into a complete local Blob. That enables seeking from the downloaded file without requiring the simple local HTTP server to provide range requests. It is not progressive playback. The poster remains visible while fetching. The second clip waits until its section approaches the viewport. A real Base44 deployment must test CORS, storage URLs and seeking again.

At widths of 700px and below, reduced motion or detectable data saving, the runtime never assigns a video source or fetches a clip. Failure mode necessarily attempts the initial request before discovering failure; it then collapses the pinned travel and retains useful content. It cannot truthfully promise zero downloaded bytes for a failure that occurs after a request begins.

H.264, yuv420p, no audio, short GOP and faststart were used. The processed videos range from roughly 1.4 MB to 7.4 MB. Originals are retained outside the public assets. All ten clips have matching posters. Source and processed sizes are in processing.json.

## What the five tests can and cannot establish

The browser harness tests both videos at separated positions and reverses the scroll. A second pass samples decoded video frames, so a changing currentTime property alone is insufficient. It exercises all three options with the keyboard, downloads the actual selected brief, checks anchors, examines page and console errors, and inspects widths of 780 and 375 pixels. It also aborts video requests and separately tests reduced motion and data saving.

Those checks concern a local Chromium browser, including phone-sized emulation. They do not establish physical iPhone Safari behaviour, actual mobile-network performance, live client transactions or Base44 frontend compatibility. These limits are explicit in the result record.

The old premium-lab-v1 result should not be used as course evidence. Its five variants were not a reliable five-business motion test. This v2 folder is an isolated replacement experiment, with raw evidence and a reproducible harness.

## Course consequence

Keep the standard local-business workflow separate. Make cinematic websites an advanced path where the agent takes responsibility for the whole page and asks for missing client content only where it matters. Do not inflate message count for its own sake. Useful stages are a complete visual/content direction, approved media, working frontend, and evidence-based refinement.

The next Base44 test should port one approved local reference using its actual assets, then verify its native app route. Record editor state and published state separately. An unchanged public bundle proves only that the public deployment did not change; it does not prove the builder wrote no source. The earlier failure loop came from collapsing those states.

A fresh-agent test using the finished skill is still required before describing the course workflow as repeatable. One successful local implementation by its author is not that experiment.

## Sources

[1] [Lewis Webber, The Department Is Open: Building the PX PUSH Website](https://tympanus.net/codrops/2026/08/07/the-department-is-open-building-the-px-push-website/), 7 August 2026. Creator-written technical case study.

[2] [Case Study: Troa 25' Folio](https://tympanus.net/codrops/2025/03/28/case-study-troa-25-folio/), 28 March 2025. Creator case study.

[3] [Case Study: NOD Coding Bootcamp](https://tympanus.net/codrops/2024/11/26/case-study-nod-coding-bootcamp/), 26 November 2024. Creator case study.

[4] [Norm Architects](https://normcph.com/), public portfolio accessed 10 September 2026.

[5] [Audo Copenhagen](https://audocph.com/), public brand site accessed 10 September 2026.

[6] [Noma](https://noma.dk/), public restaurant site accessed 10 September 2026.

[7] [Aesop](https://www.aesop.com/), public brand site accessed 10 September 2026.

[8] [Kie Kling 2.5 pricing and API overview](https://kie.ai/kling-2-5), retrieved 10 September 2026. Saved pricing text reports 42 credits per 5 seconds and 84 per 10 seconds for this route.

[9] [Kie Seedream 4.5](https://kie.ai/seedream-4-5) and [reference editing API](https://docs.kie.ai/market/seedream/4-5-edit), accessed 10 September 2026. Actual job costs are recorded from provider responses rather than inferred from marketing copy.
