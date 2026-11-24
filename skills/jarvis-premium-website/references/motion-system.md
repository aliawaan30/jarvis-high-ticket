# Motion system

What makes a site feel premium instead of basic is planned, named motion: a few big moments that tell the business's story, and quiet, consistent motion everywhere else. "Make it animated" gets fade-ups; a Scroll Score with named effects and named tools gets an experience.

Researched 23 November 2026: award-level sites built with Claude Opus use GSAP with ScrollTrigger and SplitText for scroll and text motion, Lenis for smooth scrolling, Three.js for 3D, and Apple-style scroll sequences made from AI video; the difference between basic and award-level output comes from a detailed brief that names the tools and describes every section's motion.

## 1. Tools (install in the client's website app)

- **GSAP** with **ScrollTrigger** (scroll-linked animation, pinning, scrubbing) and **SplitText** (headline reveals by line, word or letter). Free for all use, plugins included.
- **Lenis** for smooth scrolling on desktop, kept in step with ScrollTrigger:
  `lenis.on('scroll', ScrollTrigger.update); gsap.ticker.add((t) => lenis.raf(t * 1000)); gsap.ticker.lagSmoothing(0);`
- **Three.js** only when a 3D object is the product or the story (for example a product that rotates or opens). Most service businesses do not need it.
- Pin exact versions in package.json, and approve the builder's install cards.

## 1b. Tested components

Every signature moment below has a tested React component in assets/signature-mechanics (LightShiftHero, TransformationScroll, StoryScene, PinnedSteps, CursorPreviewList, Marquee, KineticHeadline, Reveal, MagneticButton, CountUp, DrawDiagram), plus interactive building blocks (BeforeAfterSlider, TabImageSwap, MenuTabs, ServiceAreaMap, ListingsGrid), site essentials (SiteHeader, StickyActionBar, ScrollProgress, FAQAccordion, EnquiryForm, OpenHours), trust and selling pieces (Testimonials, Packages, ProfileQuiz, Timeline, GalleryLightbox) and media (HorizontalJourney, LayeredDepth, ImageReveal, VideoLoopHero, PhoneDemo). Its README maps which components usually fit each niche. Use them, passing the exact code to the builder, instead of describing the effect. Name the component in the Scroll Score.

## 2. The Scroll Score (written at check-in 1)

For every section: its motion, named from the library below, what triggers it (page load, entering view, scroll scrubbed, pinned), how long or how far, and its phone version. Then choose **three to five signature moments** for the site: the moments people remember. Everything else uses the quiet defaults. Never animate everything; contrast is what makes the big moments land.

## 3. Signature moments (pick 3 to 5)

1. **Transformation scroll** (TransformationScroll crossfades smoothly when it only has a few stills, for example four existing shots; a Higgsfield film between two keyframes gives true continuous growth). The site's story told by scroll: a pinned full-screen scene that turns from the start state into the end state as the visitor scrolls, and back again when they scroll up. Built from two Higgsfield keyframes and a film between them (see higgsfield-prompting.md), drawn frame by frame on a canvas. Make it the client's real result: a bare yard growing into a finished garden, a storm-damaged roof becoming a new roof, an empty dining room filling for dinner service, a missed call turning into a booked job. The strongest single effect for most businesses.
1b. **Story scene** (only when the value happens over time). A slice of time in the customer's life told by scroll: timestamps advance, a timeline fills, and a code-built simulation (inbox, booking list, dashboard, messages) updates step by step. Needs no generated media; can crossfade a background between two times of day at higher media levels.
2. **Pinned storytelling.** A section pins while three to five steps play through: text changes on one side, the visual changes on the other, then the page releases.
3. **Kinetic headline.** Headlines reveal by line or word with SplitText as they enter, slightly staggered, with the brand's type device (for example the italic words arriving last).
4. **Layered depth.** Foreground, middle and background layers moving at different speeds (for example grasses, a path and trees cut from one generated image), so the page feels three dimensional.
5. **Horizontal journey.** A pinned section that scrolls sideways through a gallery, timeline or set of services. Phone version: a swipe carousel.
6. **Image reveal.** Images unmask as they arrive (a clip-path wipe or a scale from 1.15 to 1 inside the frame), once.
7. **Page-load sequence.** The first second: the logo, then the headline lines, then the button and the hero media, choreographed in under 1.5 seconds. Never blocks reading or the button.
8. **Live product demo.** For tech and outcome services: an interface animated in code that plays the product working (see image-direction.md).
9. **Number moment.** Confirmed figures that count up once, large, in the brand's display type.
10. **3D object.** A Three.js model that rotates, opens or assembles on scroll, only when the product is physical and a model exists.

## 4. Recipes by niche (start here, then adapt)

Each recipe combines up to three layers: code-built animation for the product, scroll as the storyteller, and, only at media level 2 or 3, Higgsfield for the emotion (the buyer's real world). At media level 1, replace each Higgsfield shot in a recipe with code-built visuals (code-visuals.md) or the client's real photos; for example the AI receptionist evening scroll uses an illustrated or colour-shifting dusk to night background instead of a film. Pick the recipe for the niche, then adapt it to the client's real offer.

**AI receptionist (and any call or booking service)**
1. Hero: a code-built live phone demo beside the headline, optionally over a still or short cinematic Higgsfield film of the problem moment when it earns its place (a tradesperson on a roof at dusk as rain starts and his phone buzzes unanswered in his pocket, screen never visible), with a code-built phone beside the headline where a call comes in, the AI answers, the transcript types out and a booking card lands.
2. Transformation scroll, "One evening at your business": pinned; as the visitor scrolls, a clock runs from 6pm to 11pm; the Higgsfield background moves from dusk to night (two keyframes, same camera); code-built call cards arrive one by one, each answered and booked; a counter ends at the evening's totals (calls answered, jobs booked, revenue kept), labelled as an example.
3. Demo call: a real recording from the member's own receptionist with a live waveform and a transcript that highlights each line as it plays, labelled Demo.
4. Kinetic headline for the cost of missed calls, with a number moment (only figures the member can support or clearly marked examples).
5. Pinned "How it works" in three steps with the code-built interface changing per step.

**Websites agency**
1. Hero: a transformation scroll where a client's old, tired homepage turns into the new premium one (code-built mock browser, real screenshots where available), with the headline above.
2. Horizontal journey through demo sites in code-built device frames, labelled Concept work.
3. Number moment for speed (for example days to launch), only if true.
4. Higgsfield only for the buyer's world (a busy café owner, a contractor between jobs), never screens.

**Garden and landscaping**: transformation scroll from bare yard to finished garden; seasons as a horizontal journey; layered depth of grasses, path and trees.

**Roofing and trades**: a still proof hero (a real job photo or a strong still) with the phone always one tap away, no hero video; the motion budget goes to the transformation scroll from storm-damaged roof to new roof (same camera); pinned process with real job photos.

**Med spa**: a calm transformation of the treatment room from morning light to evening glow (never people's faces or results); treatments as tab image swaps; soft kinetic headlines.

**Restaurant and cafe**: a transformation of the empty dining room filling for dinner service (no faces in focus); the menu as a horizontal journey; close food films on the chapter breaks.

**Real estate**: a transformation of a property from day to twilight with lights coming on; listings as a clean grid with image reveals; neighbourhood panorama bands.

## 5. Quiet defaults (everything else)

- Sections and cards rise 24 px and fade in once, 0.6 to 0.8 seconds, ease out, small stagger.
- Buttons: a short hover lift and colour change; on desktop the main button may be slightly magnetic toward the pointer (within 8 px).
- Links: an underline that draws on hover.
- A thin scroll progress bar at the top in the accent colour; rules (thin lines) draw left to right as they arrive.
- Menu: opens with a quick fade and staggered links.
- One easing family across the site (for example power2 or power3 out); durations from a small set (0.3, 0.6, 0.9, 1.2 seconds).

## 6. Phone versions

- Transformation scroll: keep it (it works with touch scrolling) but shorter, with fewer frames sized for the phone, or as an autoplaying loop if it stutters on the test phone.
- Pinned sections: shorter pins, or unpinned stacks with the visual above each step.
- Horizontal journeys become swipe carousels. Layered depth uses two layers at most.
- No smooth-scroll library on touch devices: use native scrolling.
- Nothing depends on hover or a pointer.

## 7. Performance and accessibility

- Animate only transform and opacity. No layout-changing animation.
- Pointer effects (images following the cursor, magnetic buttons, hover reveals) must reset when the page scrolls under a still pointer and when their section leaves the screen: browsers do not fire mouseleave on scroll, so a hover image can otherwise stay stuck over other sections (found live on 24 November 2026).
- Entrance animations never start outside the screen: slide in vertically, or keep horizontal offsets inside a section that clips its overflow (overflow-x: clip). An element waiting off to the side widens the page on phones until it animates, and makes phone browsers zoom out.
- Frame sequences: WebP, about 12 frames per second of film, sized to the screen (around 1600 px wide on desktop, 900 px on phones), loaded progressively with the first frame as a poster; aim for about 5 MB or less per sequence.
- Pause and clean up animations that are off screen; kill ScrollTriggers when a page unmounts.
- Prefers-reduced-motion: no scrubbing, pinning or parallax; show the end state of each moment as a still and keep every word readable.
- Text is always real text in the page, never baked into video or frames.

## 8. Verify before review

- Every signature moment plays forward and backward at 1440 px and 390 px, with no jumps, blank frames or stutter.
- No layout shift while scrolling; the action stays reachable.
- With reduced motion turned on, every section is complete and readable.
- Record the mobile PageSpeed score after the motion is in.
