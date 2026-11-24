# Signature mechanics (tested code)

Tested React components for the signature moments in motion-system.md and the interactive building blocks many niches need. They are mechanics, not niche designs: every site configures them with its own words, colours, images and story. Use them instead of describing effects to the builder: a description gets reinterpreted; tested code does not. Tested 23 and 24 November 2026; confirmed on Base44 on 24 November 2026 (the builder kept every component file exactly as given) in React 18 pages with GSAP 3.15.1 and Lenis 1.3.27: desktop behaviour, forward and backward scrolling, keyboard use, six widths (360, 390, 430, 768, 1024, 1440 px) at every scroll position with no overflow, phones with touch, and reduced motion; then used to build a complete clinic site with no changes to the components. 33 components in total; 25 width and error checks across four test pages, plus behaviour checks for every component (forms, menus, dialogs, keyboard, time zones). Every component's outer box can shrink (min-width 0), so none can widen a grid on small phones.

## Install in the client's website app

Ask the builder to add these exact versions to the app's dependencies (approve the install cards): `gsap@3.15.1` and `lenis@1.3.27`. Then ask it to create a folder `src/components/mechanics/` and add the files below with their content exactly as given.

| File | Use it for |
| --- | --- |
| motion.js | Shared setup: plugins, reduced motion and phone conditions, cleanup (useMotion), and desktop smooth scrolling (useSmoothScroll, call once in the page) |
| KineticHeadline.jsx | Headlines that reveal by line or word (or on load) |
| Reveal.jsx | Overflow-safe entrance animation (vertical only) for blocks or lists |
| LightShiftHero.jsx | Pinned hero where light changes with scroll (night to morning, day to dusk) and a giant word lights up |
| TransformationScroll.jsx | Pinned canvas frame sequence from a Higgsfield film (before to after), with phone frames and stage labels |
| StoryScene.jsx | Pinned slice of time: a giant clock, beats and a code-built simulation filling in |
| CursorPreviewList.jsx | Giant list with an image following the pointer; tap to open on phones |
| Marquee.jsx | Endless row of names or logos, pauses on hover |
| MagneticButton.jsx | Main button drifting toward the pointer on desktop |
| CountUp.jsx | Confirmed figures counting up once |
| DrawDiagram.jsx | SVG diagrams whose lines trace in and nodes fade in, with a text alternative |
| PinnedSteps.jsx | Steps that hold and crossfade while pinned on desktop; a plain stack on phones |
| BeforeAfterSlider.jsx | Before and after of real, consented work or labelled concept work (drag, tap or keyboard) |
| TabImageSwap.jsx | One large image that crossfades with tabs (seasons, treatments, packages, conditions) |
| MenuTabs.jsx | A real menu or price list with category tabs and dietary or type filters |
| ServiceAreaMap.jsx | A stylised, code-built map of areas served, linked to a list (the text alternative). Give it an `outline` (a simple hand-drawn path of the city or region) so it does not look generic; `route` lines only when they mean something. Place every area in its real relative position (north at the top); never move areas to fit a line or a layout, because locals notice wrong geography at once |
| ListingsGrid.jsx | Property listings with filters, cards and a map with linked pins; List or Map toggle on phones |

### Site essentials

| File | Use it for |
| --- | --- |
| SiteHeader.jsx | Header with desktop links and a full-screen phone menu (focus kept inside, Escape closes, page locked), hiding on scroll down and returning on scroll up |
| StickyActionBar.jsx | Phone-only bottom bar (main action and Call), clear of the home bar, adds page padding, hides at its target section |
| ScrollProgress.jsx | Thin reading-progress line for long pages |
| FAQAccordion.jsx | Accessible questions and answers with FAQPage structured data for search. Questions inherit the site's font; set --faq-font, --faq-weight and --faq-size in the tokens (for example the headline font). On desktop, pair it with a left column (heading and a call-us line) so it never leaves half the section empty |
| EnquiryForm.jsx | The form wired to the site's own backend: labels, validation, honeypot, double-submit guard, honest success and failure with the phone as fallback |
| OpenHours.jsx | Opening hours with "Open now" computed in the business's own time zone |
| SiteCheck.jsx | The built-in site check for real phones and computers: add `?qa` to the address, press Run, and it scrolls the page and reports overflow (naming the element), broken images, small tap targets and browser errors, with Copy report. Invisible without `?qa` |

### Trust and selling

| File | Use it for |
| --- | --- |
| Testimonials.jsx | Real reviews with name, source and date (and owner replies), swipeable with buttons |
| Packages.jsx | Packages or pricing with an optional billing toggle and a "Most chosen" card; prices may stay [placeholders] |
| ProfileQuiz.jsx | Three to five questions that recommend a real option, then lead to the action |
| Timeline.jsx | Real milestones on a line that draws with scroll |
| GalleryLightbox.jsx | Real work in mixed shapes with a lightbox (arrows, swipe, Escape, focus returned) |

### Motion and media

| File | Use it for |
| --- | --- |
| HorizontalJourney.jsx | Pinned sideways scroll through cards on desktop; a swipe row on phones |
| LayeredDepth.jsx | Layers moving at different speeds for depth (two layers on phones) |
| ImageReveal.jsx | Images unmasking and settling from a slight zoom as they enter |
| VideoLoopHero.jsx | A quiet muted loop hero with the poster as the fallback (blocked autoplay, data saver, reduced motion, failure) |
| PhoneDemo.jsx | A code-built product demo on a phone screen (for example an AI receptionist call becoming a booking), labelled Demo |

Tabs and toggles take the brand accent from the CSS variables --tab-bg, --tab-border and --tab-on (text on the selected tab); set them in the design tokens.

## Which components fit which niche (starting points)

| Niche | Usually fits | Usually avoid |
| --- | --- | --- |
| Clinics (GP, dental, physio) | OpenHours, FAQAccordion, StoryScene (your first appointment), PinnedSteps (how treatment works), DrawDiagram (care team, referral path), CursorPreviewList or TabImageSwap (services, conditions), ServiceAreaMap | TransformationScroll and BeforeAfterSlider for medical results; dramatic light shows |
| Med spas | LightShiftHero or a calm still hero, StoryScene, CursorPreviewList (treatments), DrawDiagram (who looks after you), TabImageSwap, Packages, FAQAccordion | Generated before and after results |
| Gardens and landscaping | TransformationScroll, VideoLoopHero, TabImageSwap (seasons), BeforeAfterSlider (real work), GalleryLightbox, LayeredDepth, PinnedSteps, ServiceAreaMap | Anything clinical |
| Trades and roofing | StickyActionBar with Call, BeforeAfterSlider (real jobs), TransformationScroll, PinnedSteps, ServiceAreaMap, Testimonials, CountUp | Slow artistic heroes that hide the phone number |
| Restaurants and cafes | MenuTabs, OpenHours, VideoLoopHero, LightShiftHero (golden hour to evening), GalleryLightbox, Marquee, TransformationScroll (the room filling) | Diagrams |
| Real estate | ListingsGrid, ServiceAreaMap (neighbourhoods), LightShiftHero (day to twilight), GalleryLightbox, BeforeAfterSlider (renovations) | Arch frames and moody textures |
| AI receptionist, agencies, software | PhoneDemo (the hero demo), StoryScene (one evening of calls), DrawDiagram, PinnedSteps, Packages, BeforeAfterSlider (built website mockups), FAQAccordion | Nature or abstract cinematic heroes |
| Legal and professional | KineticHeadline, PinnedSteps, DrawDiagram, CursorPreviewList (practice areas), Timeline, FAQAccordion | Playful motion |

Every site uses the site essentials (SiteHeader, StickyActionBar, EnquiryForm, usually FAQAccordion). Every site still decides with the triggers in section-patterns.md and the wow pass: use a component only when its trigger is true.

## Hand-off rules for the builder

0. **Only what the plan needs.** Read this README, pick the components the site plan and Scroll Score actually use (usually 8 to 12, always including motion.js), and give the builder only those files. Never install the whole library. More components is not more premium: a busy page feels cheap.
1. Give the builder the file contents exactly and say: "Create these files with exactly this content. Do not rewrite, simplify or merge them." Then read the files back and confirm they match.
2. Change only the props and the content (words, colours, images, beats, items). Never edit the mechanics' internals to restyle a site: style through props, the design tokens and the surrounding layout.
3. Call useSmoothScroll once in the page root. Every mechanic already handles phones, touch, reduced motion and cleanup.
4. Keep every mechanic inside sections that follow the design system and surface rules; text stays real text.
5. After building, run the motion check and the fit check (design-system-rules.md) at every width and scroll position.
6. Every element with a set width and padding or border sizes itself with box-sizing border-box, and every component's outer box can shrink (min-width 0), so none can widen the page on any site, whatever the site's own styles.
6b. Never hand-write a pointer-following or hover effect outside these components; if one is truly needed, it must reset on scroll and when off screen, like CursorPreviewList and MagneticButton.
7. Add SiteCheck to every site during the build (it renders nothing unless the address has `?qa`), so the member can run real-device checks; it may stay after launch because it is invisible without `?qa`.
7b. EnquiryForm's onSubmit must call the website's own backend function and resolve only after the enquiry is saved (client-delivery.md).
8. These components are mechanics, not designs. Each site still needs its own idea, composition, copy and art direction (wow-pass.md). The screenshots in references/quality-bar show the level to reach, never a layout to copy.
