# Changes by Ali (against Blake's main, zip of 9 to 10 Nov 2026)

Use this list when merging into Blake's repo.

## Batch 1, 11 Nov 2026
Replaced with Ali's fixed versions (offer rounds 1 to 4, landing page rounds 1 and 2, Blake's feedback of 11 Nov):
- skills/jarvis-offer-creation/SKILL.md
- skills/jarvis-offer-menu/SKILL.md
- skills/jarvis-landing-page/SKILL.md

Added:
- skills/jarvis-landing-page/references/palettes.md
- docs/decisions/2026-11-11.md
- CHANGES-ALI.md

Archived: none yet.

## Batch 2a, 11 Nov 2026
Archived (moved, not deleted):
- skills/jarvis-proposal-builder (Blake's 5 Nov version) to archive/proposal-builder-blake-2026-11-05/

Added (replaces the archived version):
- skills/jarvis-proposal-builder/SKILL.md (version 2026-11-11.1, draft, tested locally, not yet on Base44)
- skills/jarvis-proposal-builder/assets/render_proposal.py
- skills/jarvis-proposal-builder/assets/example-proposal.json
- skills/jarvis-proposal-builder/references/presenter-notes.md
- skills/jarvis-proposal-builder/references/discovery-checklist.md

Updated:
- docs/decisions/2026-11-11.md (proposal decisions)
- CHANGES-ALI.md

## Batch 3, 12 Nov 2026: Jarvis 2.0 (pack 2026-11-12.1709, Agency HQ v3.13)
Added, core: skills/jarvis-2-brain, jarvis-hq, jarvis-missions, jarvis-rhythm
Added, Module 4: skills/jarvis-lead-hunter, jarvis-email-setup, jarvis-outreach-coordinator, jarvis-call-card, jarvis-reply-desk, jarvis-sms
Added, Module 6: skills/jarvis-solution-design, playbook-call-to-close
Added: apps/agency-hq/ (v3.13 source, install, release notes, talk mode notes, Retell setup, previews)
Added: docs/jarvis-2/ (INSTALL, STRUCTURE, CHANGELOG, THIRD-PARTY-NOTICES from the pack)
Archived: archive/jarvis-2.0-pack-2026-11-12.1709.json (single pack format retired; its module copies of offer, landing page, proposal and Meta are older than the repo)
Archived (moved): course/outreach/skills/jarvis-outreach-coordinator to archive/outreach-coordinator-blake-draft/
Archived (moved): skills/jarvis-confirmation-page and skills/jarvis-precall-followup (Blake's folders with old references) to archive/, replaced by Ali's single file versions from the pack

Replaced SKILL.md with the pack version (Blake's text plus the HQ (Jarvis 2.0) section, references inlined):
jarvis-ad-library-offer-research, jarvis-custom-opportunity-finder, jarvis-offer-discovery, jarvis-opportunity-finder, jarvis-vsl-writer, jarvis-ad-scripting, jarvis-static-ad-creator, jarvis-scoping-agent

Merged: Ali's 11 Nov versions of jarvis-offer-creation, jarvis-offer-menu, jarvis-landing-page plus the pack's HQ (Jarvis 2.0) section appended.

Not taken from the pack (repo is newer): jarvis-proposal-builder (batch 2a), jarvis-meta-campaign-setup (batch 2b, still to push).
Missing from the pack: jarvis-ad-editing.

## Batch 3b, 13 Nov 2026 (includes batch 2b)
Archived (moved): skills/jarvis-meta-campaign-setup (Blake's 29 Oct version) to archive/meta-campaign-setup-blake-2026-10-29/
Agency HQ app v3.14: added base44/shared/send-check.ts and base44/functions/sendCheck/entry.ts (function 19); updated INSTALL.md and RELEASE-NOTES.md.
Rewritten: skills/jarvis-hq (matches app v3.14, install guide, exact tables, Data area and Extra tables, app check).
Updated: skills/jarvis-2-brain (8 step programme, solve it rules, deal stage names), jarvis-missions (mission 4 and 9), jarvis-email-setup (calls the app's sendCheck), jarvis-call-card, jarvis-reply-desk, playbook-call-to-close (deal stage names), jarvis-proposal-builder 2026-11-13.1 and jarvis-meta-campaign-setup 2026-11-13.1 (save as jarvis-hq says), docs/jarvis-2/INSTALL.md (guided app install, app check).
Added: docs/tests/ (Meta scenario test and mock screenshots, send-check tests and results), docs/decisions/2026-11-11.md (updated), docs/decisions/2026-11-13.md, docs/onboarding-map-2026-11-11.md (exported by Ali).

## Batch 3c, 15 Nov 2026
Archived (moved): skills/jarvis-offer-discovery and skills/jarvis-opportunity-finder to archive/ (retired; custom opportunity finder carries its own copy of the research method). skills/README.md index updated.
Removed em and en dashes: jarvis-offer-menu (references/common-services-2026-11-02.md), jarvis-static-ad-creator (SKILL.md, references/static-visual-analysis.md), jarvis-vsl-writer (SKILL.md, references/vsl-source-notes.md).
Added: START-HERE.md (system overview for Blake and reviewing agents).

## Batch 3d, 15 Nov 2026
Version stamps: every skill now carries a Version line (baseline 2026-11-15.1 where none existed), so "Update these skills" and "Am I up to date?" work.
Rewritten: skills/README.md, the index of all 26 skills with module, student prompt, version and test notes.
Updated: docs/jarvis-2/INSTALL.md (upgrade also removes jarvis-offer-discovery and jarvis-opportunity-finder); jarvis-custom-opportunity-finder (removed the retired skill's embedded header from its appendix and reference file); START-HERE.md (points to the index).

## Batch 3e, 17 Nov 2026
Twice-daily check-ins (Blake's feedback): jarvis-rhythm 2026-11-17.1 replaces the evening log with an afternoon check-in 6 hours after the morning brief. Check-ins go to the student's connected channel (WhatsApp, Telegram, iMessage, Slack or LINE, else Base44 chat), always in three parts (since last time, one next task, momentum), adapt to wins and silence, and are never skipped to save credits.
Updated: jarvis-2-brain 2026-11-17.1 (afternoon check-in example), docs/jarvis-2/INSTALL.md, skills/README.md, START-HERE.md.

## Batch 3f, 17 Nov 2026: course text and skill downloads
Course (course/studio): Module 1 rewritten: Install Jarvis 2.0, How Jarvis 2.0 Works (was Load the High Ticket Skill Pack), Your Jarvis HUD (was Connect Your Pipeline, now the new CRM). Removed from the outline: Prove It on Something Real, and Module 3 Your CRM (old CRM). Module 6 Objections: removed "Can you guarantee it'll work?", nine objections now. An install section opens the first lesson of Modules 2 to 7. Small fixes in Create Your Offer and The Ad Skills (no more single skill pack). export/COURSE.md regenerated with the studio's own export code.
Downloads (course/downloads/jarvis-2): jarvis-skills-module-1-core.zip to module-7-delivery.zip (all 26 skills, each in one module; core includes the install steps) and agency-hq-v3.14.zip.
Added: docs/decisions/2026-11-17.md.

## Batch 3g, 17 Nov 2026: Agency HQ v3.15
App (apps/agency-hq, v3.15): Settings, Connections (every key in one place with a ? help, saved in a new backend-only Vault table, last 4 characters only; HUD key created automatically with Copy for Jarvis; Set up my voice builds the Retell agent in one press). New table Vault, new function connections, shared module keys; every function reads keys through it (Base44 Secrets still win). HUD home agentic layer: Scout, Writer, Closer and Ops around the core from real tasks, who is working on what, next check-in, Needs you, Message Jarvis with the real reply, roles on the live feed. Full production build passes; connections logic tested (9 checks) and Set up my voice tested against a stand-in Retell (4 scenarios).
Skills: jarvis-hq 2026-11-17.1 (guides the Connections screen).
Course: Your Jarvis HUD lesson uses Connections and the v3.15 package. Downloads: agency-hq-v3.15.zip replaces v3.14, core skill zip rebuilt.

## Batch 3h, 17 Nov 2026: Agency HQ v3.15.1
Voice simplified: Browser voice (free) or Retell voice (add-on). Fish Audio hidden from students (existing keys still work). Agents built by Set up my voice greet in their own voice (new Profile field retell_greets). HUD: diag lines hidden from the live feed, feed entries clamp to 3 lines with click to expand, Closer counts replies to call. Downloads: agency-hq-v3.15.1.zip replaces v3.15.

## Batch 3i, 17 Nov 2026: Agency HQ v3.15.2
Talk to Jarvis is the main HUD button (filled cyan, microphone icon, under the status line); tapping the core also opens Talk. Only Hud.jsx and hq.css changed. Downloads: agency-hq-v3.15.2.zip replaces v3.15.1.

## 18 Nov 2026: fixes from Test 17 (Agency HQ v3.16, skills 2026-11-18.1)
App: publish crash fixed (src/lib/utils.js guarded), no app rename, Retell on its current API (v2/list-agents, publish-agent-version, v2/list-phone-numbers), Retell call prepared on hover for a faster greeting, HUD key in two steps, Test Jarvis connection, Message Jarvis explains failures, Campaigns Drafts with Approve, Edit and Skip (new Touch status approved), today's calls target, no Australian phone default.
Skills: jarvis-2-brain (only what was asked or approved, guide every step, message formatting), jarvis-hq (plain-words install guide, reliable HUD key, connection test), jarvis-rhythm (check-ins under 80 words with today's target and one action, campaign runner sends HUD approvals, plain words), jarvis-missions (reordered to match the course, celebrations and module moments, one next action), jarvis-outreach-coordinator (drafts always shown for approval), jarvis-offer-creation (blank lines between the six lines). Install steps: own-app lane, warm welcome, city for timezone, goal scope limited, live message with the plan, no lead hunt from the install, core zip wording.
Docs: Test 17 report, decisions 2026-11-18, run sheet and Chrome test prompt updated. All module zips rebuilt; agency-hq-v3.16.zip replaces v3.15.2.

## 18 Nov 2026: Agency HQ v3.16.1, phones and tablets
HUD on phones: roles in a 2 by 2 grid under the ring (they made the page wider than the screen), Call now right under Talk to Jarvis, thumb-sized tap areas on every link on phones and touch screens, "1 campaign". Checked every page at 360, 390 and 768 wide. Downloads: agency-hq-v3.16.1.zip replaces v3.16.

## 18 Nov 2026: no code needed to upgrade
The upgrade no longer uses a code: the install message is "Upgrade me to Jarvis 2.0. Follow the install steps in the attached file." Jarvis never asks for a code, and still saves one if a student sends it. Updated: docs/jarvis-2/INSTALL.md, the core skill zip, the Install Jarvis 2.0 lesson and course export, the run sheet and the Test 17 prompt.

## 18 Nov 2026: one short message per module
Installing a module is now attach the module file and send "Install Module N." (jarvis-2-brain 2026-11-18.2, new section Installing a module: gate check, install every skill folder, run nothing, reply with each skill and version and the first step). Updated the six module lessons, the course export, the core zip, the Test prompt, and the run sheet, which now has a Files panel and per-step download buttons with every file built in.

## 18 Nov 2026: premium prompts
Every student prompt is one or two warm sentences that name the skill and say what the student wants back: the upgrade, the HUD setup, the module installs ("Install Module 2, The Irresistible Offer, from the attached file..."), offer, leads, email, first emails and the wrap-up. Updated the 8 lessons, the course export, the run sheet and the Test prompt.

## 18 Nov 2026: Funnel app allowed
The stay-in-your-own-app rule now allows the member's Funnel app from Module 3 (it blocked the landing page). jarvis-2-brain 2026-11-18.3, install steps, and jarvis-landing-page 2026-11-18.1, which now guides creating the Funnel app and adding it to Cross-app data access before the first build. Core and Module 3 zips rebuilt. Test prompt: steps 21 to 24 test the funnel end to end (install, calendar, landing page on desktop and phone, an application landing in the HUD).

## 18 Nov 2026: students keep All apps
Students keep Cross-app data access on All apps (the default); Jarvis never asks them to restrict it. Safety stays in behaviour: Jarvis works only in the member's own Agency HQ and Funnel app by the app IDs saved in memory, and never reads, changes or deletes any other app it can see. Updated: install steps, jarvis-2-brain 2026-11-18.4, jarvis-hq 2026-11-18.2, jarvis-landing-page 2026-11-18.2, core and Module 3 zips, the student setup guide (new, docs/previews/jarvis-2-setup-guide.html), the run sheet and the Test 18 prompt.

## 18 Nov 2026: premium website skills
New in Module 7: jarvis-website-research (intake, five research layers, research brief, rule packs with the Texas med spa pack), jarvis-brand-guide (three directions, palette rules with contrast checks, licensed type library, brand board format), jarvis-premium-website v4 (Blake's v3.0.0 engine and five tested designs kept, plus section pattern library, Higgsfield route, client delivery: enquiries, SEO, legal pages, launch checks, domain, handover). Module 7 zip rebuilt with 4 skills. 29 skills in total. Previews: brand directions and a landing page for a sample Dallas roofer.

## 18 Nov 2026: website skills can start after the HUD
jarvis-2-brain 2026-11-18.5: the website research, brand guide and premium website skills can start any time after Your HUD is set up (demo sites for prospects are part of selling); the scoping agent still waits for a won deal. Installing a module is always allowed once Jarvis 2.0 and the HUD are set up: gates decide what Jarvis pushes next, not what the member may install. Core zip, setup guide and run sheet rebuilt.

## 18 Nov 2026: website delivery, final for 18 Nov (after the Fernhollow test)
jarvis-premium-website 2026-11-18.12, jarvis-website-research 2026-11-18.4, jarvis-brand-guide 2026-11-18.4. One starting prompt with a seven-question intake and three check-ins; Higgsfield prompting, first-time connection and plain-words errors (Higgsfield worked live from Jarvis); strict design system with surfaces, buttons, form controls, overlays, header and sticky bar rules, and layout QA at six widths; mobile design with phone images, menu, carousels and the hero video loop; image direction with roles, the variety check and meaning; niche design profiles and reference sites in research; starter logos and visibility rules in the brand guide; 38 section patterns including the Delta set; the website owns its enquiries with two emails; native language and formality. Version 3 files kept as evidence, marked that version 4 wins. Module 7 zip rebuilt. Checks: 29 of 29 website rule checks, 13 of 13 pack checks.

## 23 Nov 2026: motion system, relevance, mobile excellence
jarvis-premium-website 2026-11-23.2: media must prove the offer (relevance test; code-built demos for tech services; never generated screens; nothing off-palette), an AI agencies design profile, mobile excellence standard (phone first, thumb friendly, PageSpeed 90 aim), a motion system (GSAP with ScrollTrigger and SplitText, Lenis, Three.js when needed; a Scroll Score with three to five signature moments; the transformation scroll from two Higgsfield keyframes), top-quality model choice per shot, the Opus 5.5 check, Higgsfield only with no silent fallback. Demo: docs/previews/motion-demo-fernhollow.html.

## 23 Nov 2026: visual approach, chapters, story scene, uniqueness
jarvis-premium-website 2026-11-23.8: after research Jarvis recommends one of four visual approaches (cinematic, photo-led, diagram-led editorial, typography-led minimal) mapped to media levels; chapters answer the buyer's questions; a code-built story scene; strict diagram style with the logo as the central node, phone versions and text alternatives; built before and after, estimator and progress bar patterns; uniqueness rules (reuse the method, never the output); build hero first then chapter by chapter, phone and desktop together; tighter phone rules. Niche profiles carry a recommended approach; type library adds five style archetypes including editorial monograph. Scenario test: 8 of 8 niches got the expected approach, 11 of 11 flow checks. Preview: docs/previews/medspa-preview-solenne.html.

## 23 Nov 2026: the wow pass
jarvis-premium-website 2026-11-23.11: a wow plan at check-in 1 (one brand idea, an immersive signature moment, two bold compositions, a palette and type distinct from local competitors), then before review the five-second test and a critique loop run twice (screenshot, critique like an award jury, fix the top three); entrance animations never start off screen; the fit check runs at every scroll position. Brand guide 2026-11-23.1: palette must differ from local competitors. Chapters are planning logic only; special patterns only when their trigger is true; full responsiveness is rule 0. Preview: docs/previews/medspa-preview-v2.html.

## 23 Nov 2026: signature mechanics library
jarvis-premium-website 2026-11-23.12: assets/signature-mechanics holds 12 tested React components (shared motion setup with reduced motion and cleanup, KineticHeadline, Reveal, LightShiftHero, TransformationScroll, StoryScene, CursorPreviewList, Marquee, MagneticButton, CountUp, DrawDiagram, PinnedSteps) with hand-off rules: the builder gets the exact code, never a description. Tested in a React 18 page with gsap 3.15.1 and lenis 1.3.27: 22 checks (desktop, forward and backward scrolling, six widths at every scroll position, phone touch, reduced motion). references/quality-bar holds the v2 med spa and motion demo screenshots as the level to reach, never templates.

## 23 Nov 2026: 17 components and a niche guide
jarvis-premium-website 2026-11-23.13: five more tested components (BeforeAfterSlider, TabImageSwap, MenuTabs, ServiceAreaMap, ListingsGrid), every component shrink-safe on small phones, tabs take the brand accent from tokens, and a niche-to-component guide in the mechanics README. Proven by building a complete physio clinic site from the library with no component changes: 14 of 14 checks. Quality bar adds the clinic screenshots.

## 24 Nov 2026: 33 tested components and a gallery
jarvis-premium-website 2026-11-24.1: 16 more tested components (SiteHeader, StickyActionBar, ScrollProgress, FAQAccordion, EnquiryForm, OpenHours, Testimonials, Packages, ProfileQuiz, Timeline, GalleryLightbox, HorizontalJourney, LayeredDepth, ImageReveal, VideoLoopHero, PhoneDemo), 33 in total; every component sizes itself with border-box and can shrink; the niche guide covers them all; new hand-off rules (sizing, EnquiryForm wired to the site's own backend). Tests: 25 of 25 width and error checks across four pages, behaviour checks for every component. docs/previews/component-gallery.html shows all 33 live.

## 24 Nov 2026: first live upgrade on Base44, site check
Live result: the Base44 builder kept all 12 component files exactly as given (read-back matched line for line); media moved into the site's own app. Jarvis cannot run a real browser inside Base44, so jarvis-premium-website 2026-11-24.4 adds SiteCheck (34th component: add ?qa to the address, it scrolls the page and reports overflow with the element, broken images, small tap targets and browser errors, measured against the real screen width even when a phone zooms out) and a 5-minute real-device checklist for the member at check-in 2. Also: TransformationScroll crossfades between a few stills; ServiceAreaMap has no decorative route by default and accepts an area outline; the Base44 custom email domain steps; wow-pass weak spots from the live build; media must live in the site's own app; no review before every check.

## 24 Nov 2026: stuck hover image fixed
jarvis-premium-website 2026-11-24.5: CursorPreviewList's image stayed on screen over the hero when the page scrolled under a still mouse (browsers do not fire mouseleave on scroll). It now checks what is under the pointer on every scroll and hides when the list is off screen; MagneticButton springs back the same way. Tested: 6 of 6 for the scroll case, 16 of 16 regression checks across all test pages, the clinic preview and the gallery. New rule: pointer effects must reset on scroll and off screen.

## 24 Nov 2026: FAQ font and map geography
jarvis-premium-website 2026-11-24.6: FAQ questions inherit the site's font (tokens --faq-font, --faq-weight, --faq-size) instead of forcing the body font; FAQ pairs with a left column on desktop; service-area maps keep real relative positions (found live: areas were rearranged to sit on a line); the member checklist stays at five minutes.
