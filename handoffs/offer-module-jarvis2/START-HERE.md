# Offer module handoff for Jarvis 2.0

8 November 2026. Owner: Blake. This handoff packages the current teaching and skills for the technical person building the new Jarvis runtime. That runtime was not inspected here. No dependency on a specific model, framework or database is assumed.

## The experience to build

Students go through the actual course. Jarvis works alongside it: explains confusing sections, uses their business as the example, helps them do the exercises and remembers their work. Do not replace the course with a chatbot that skips the teaching.

The student can start with: “Help me work through Module 2 alongside the course. Find where I am up to and help me understand and complete the next step using my own business.”

From the course, the existing Copy prompt for Jarvis button includes the current lesson and section. It copies text; it is not a live connection to an authenticated Jarvis session. The new system may replace it with a direct handoff that carries the same context.

## What is included

- `course/module-2/`: all five complete source lessons, ordered outline, linked diagrams and a readable Markdown export. This is the offer module to import into the new course system.
- `course/reading-copy/`: the current full course reading view, assets and student skill download. Open through a local static server; see README in that folder. It includes unfinished lessons elsewhere in the course, not a claim that the entire programme is ready.
- `skills/`: the complete current 16-skill set with references and assets, including course guide and all offer-related skills. Keep the folders intact.
- `skills/jarvis-course-guide/references/course-index.json`: the whole course order and snapshot identifiers.
- `skills/jarvis-course-guide/references/lessons/`: all 39 current lesson texts, including explicit empty bodies where unfinished. The guide can retrieve the relevant lesson without the student pasting it.
- `skills/jarvis-course-guide/references/offer-module-flow.json`: exact five-lesson order, section IDs, course links, student tasks, skill routing and saved outputs.
- `implementation/`: this document, a proposed shared-record example and runtime acceptance checks.
- `MANIFEST.json`: content hashes for every packaged file. There are no real student records, provider credentials or private client transcripts in this handoff.

## How the skills connect

| Course lesson | What the student studies | What Jarvis helps do | Main skill |
|---|---|---|---|
| 1. The Irresistible Offer | Service versus offer, financial cost of the problem, buyer awareness | Explain the concepts using the student's context; answer questions | course guide |
| 2. AI services you can sell | Eight service categories and how each changes for the client | Compare options and explain delivery, integrations and human involvement | course guide + offer menu |
| 3. Choose Your Niche | 25 niche ideas with several possible services, service-first or niche-first | Ask about background, interests and location; help choose one combination | offer menu |
| 4. What an Irresistible Offer Looks Like | Finished roofing example, why it is attractive and where offers are used | Explain the example without automatically copying its target into the student's offer | course guide |
| 5. Create Your Offer | Four practical steps: buyer, problem, service/delivery, six lines | Research, save the service brief, write the offer and review it together | offer menu → offer creation |

Use `jarvis-ad-library-offer-research` for an advertising-led research route and `jarvis-custom-opportunity-finder` for deeper custom-workflow research when appropriate. They are alternatives, not compulsory extra assignments. Then use the same saved brief for offer creation. The next module's landing-page skill reads that offer rather than asking the student to explain everything again.

`jarvis-offer-creation` deliberately returns exactly six labelled lines: niche, desired outcome, timeframe, risk reversal, authority/proof and mechanism. The course guide owns teaching and conversation around it. The offer menu owns investigation and service development before it. This division avoids turning the six-line skill into an enormous research/teaching response.

## Runtime connections you must provide

These are capability requirements, not existing APIs:

1. **Course retrieval.** Give Jarvis access to the index, the selected lesson and linked visuals where supported. Read only relevant content per turn. Carry current lesson/section from the course UI, or ask the student when absent. Respect the source IDs if the new platform uses its own IDs by keeping a mapping.
2. **Skill loading.** Make skill discovery and reading available, preserving supporting files. When the guide routes to a specialist, load its current instructions and reuse the student's saved brief. A skill file is instructions, not an installed browser, sender or CRM integration.
3. **Research.** Provide web search and page reading for niche/service evidence and sourced pre-call estimates. If unavailable, disclose the limit and keep the research pending. Do not fabricate sources.
4. **Student storage.** Read/write a persistent record scoped to that student and business project. Use the new system's actual storage, not the distributed course files. Read it before asking previously answered questions. Save changes at useful milestones.
5. **Progress and artifacts.** Save study status separately from task output and student approval. Keep research/service briefs and offer versions as reusable artifacts. Do not silently replace an approved offer after a course update.

The proposed record example is a field contract to adapt, not a database migration or an implemented persistence API. You choose the actual storage and orchestration. These files do not require a rewrite of your Jarvis 2.0 core.

## The student record

Store course snapshot version/hash; lesson/section; what the student reports studying; chosen buyer/location/service; source-backed problem-value brief; delivery/service brief; offer version and approval; unresolved questions; next action. Preserve a distinction between teaching examples, research assumptions, owner-confirmed inputs and actual customer proof.

For low/base/high value estimates, show the arithmetic and sources. Use the owner's figures when available and otherwise label assumptions. The CallRail 82% figure is US consumer stated intent to call a competitor, not a plumber's measured lost-call conversion rate. Do not use it as an extra multiplier in the illustrative 30 calls ×20% ×2500 calculation.

For a known service, fit it to the chosen buyer. For custom automation, learn the workflow before inventing the build; a free AI audit is one way to start that discovery. A receptionist may take notes, transfer, book or trigger CRM actions. Include only agreed capabilities. Recommend experienced developer scoping for full custom CRMs.

The flagship offer leads with the desired business outcome. “5 extra jobs in 30 days” is a proposed teaching example, not a universal promise for every student. Setup timing is separate. Evidence and a feasible delivery path determine whether a member can use a target or guarantee.

## Course updates

Authoring source is `course/studio/data/outline.json` plus its referenced lesson JSON files in the private repository. Run `python3 scripts/build_reading_copy.py` to regenerate the reading view, guide course snapshot and current student ZIP together. Run `python3 scripts/build_offer_module_handoff.py` to rebuild this handoff ZIP. `python3 scripts/review_inventory.py --write` and `--check` refresh and check the wider repository inventory.

Course changes are not automatically fetched by an installed Jarvis. Import a new version, verify the index/hash, preserve student records and apply an ID mapping if necessary. Tell a returning student about a materially changed lesson rather than resetting their work.

## Where to start

Import the five Module 2 lessons and their visuals. Install the guide, offer menu and offer creation skill with references. Connect read/write student state and web research. Use the lesson flow map, then run `ACCEPTANCE-CHECKS.md` with a fresh learner and a returning learner. Keep untested provider actions disabled rather than presenting them as working.

Packaged content, local browser navigation, clipboard handoff and archive integrity were checked. Real Jarvis 2.0 skill routing, persistence, research behavior and learner understanding remain for your runtime test.
