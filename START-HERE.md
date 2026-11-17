# Jarvis 2.0 and the High Ticket programme: system pack

Prepared by Ali Nawaz (TPM), 15 November 2026. Source of truth: github.com/aliawaan30/jarvis-high-ticket (main), which is Blake's high-ticket repo plus Ali's batches 1 to 3b. This pack is that repo with heavy and outdated folders removed so an agent can read all of it.

## For any agent reviewing this pack

This is a pre-launch build, not a finished product. The known gaps are listed in section 5 on purpose. Review it for launch readiness: confirm or challenge the open items, find anything missing from that list, and give the fastest path to launch.

## 1. What this is, in one paragraph

Students of The AI Agency Builder upgrade the free Jarvis (a Base44 Superagent) to Jarvis 2.0. Jarvis 2.0 is four always-on core skills plus one skill per job, organised by course module, and a Base44 app called Agency HQ (the Jarvis HUD) that shows the student's whole agency on one screen. The course walks students from offer to first client in 7 modules and 19 missions. Jarvis reads and writes every step in Agency HQ, so students never paste their offer, leads or calls between steps.

## 2. How the pieces fit

| Layer | What it is | Where |
| --- | --- | --- |
| Core skills | jarvis-2-brain (how Jarvis thinks, the 8 step programme, solve-it rules), jarvis-hq (where every table and field lives), jarvis-rhythm (a morning brief and an afternoon check-in every working day, sent to the student's WhatsApp, Telegram or other connected channel, plus reply watch, after the call, Friday numbers and the campaign runner), jarvis-missions (19 missions to the first client live) | skills/ |
| Agency HQ app | Base44 app v3.15.1: 19 tables, 20 backend functions (including sendCheck, the email send gate, and connections, which keeps every key in one Settings screen), 1 workflow, HUD, pipeline, lead pages, campaigns, clients, results, Talk to Jarvis (voice stage with a particle orb, Base44 voice or Retell) | apps/agency-hq/ |
| Module skills | Module 2 offer (offer menu, offer creation, ad library research, custom opportunity finder), Module 3 funnel (landing page, confirmation page, VSL writer, pre-call follow up), Module 4 outreach (lead hunter, email setup, outreach coordinator, call card, reply desk, SMS), Module 5 ads (ad scripting, static ad creator, Meta campaign setup; ad editing still to add), Module 6 sales (call to close playbook, solution design, proposal builder), Module 7 fulfilment (scoping agent) | skills/ |
| Data rule | Tables the app has live in Agency HQ. Offer, Funnel, Calls and Proposals live in Jarvis's own Data area. Extra fields go in "Extra" tables (for example CampaignExtra). Jarvis never edits the app | skills/jarvis-hq/SKILL.md |
| Course | Blake's 39 lesson course text, plus a 42 lesson redesign preview with the prompt for every skill lesson | course/studio/export/COURSE.md, previews/ |

## 3. Decisions already made

1. Existing students upgrade the same Jarvis. The upgrade removes old skills and keeps a short profile.
2. One skill per job, in Blake's folder format. The four core skills stay separate (not merged).
3. Order: core, Agency HQ, offer, funnel, outreach, ads (optional), sales, fulfilment. Each module checks the step before it is done.
4. Jarvis solves problems in three levels: fix it myself, fix it together, hand it over ready. It always returns to the original task.
5. Every lesson prompt names its skill: "Use the [skill] skill to [task]." Students never paste what Jarvis already has.
6. Lesson design: Blake's full layout (lede, sections with purpose, worked example with the Dallas roofer, prompt box, checkpoint), every lesson labelled Training, Skill or Prompt.
7. Proposal: one page, premium design (version 5), rendered by a script so it never drifts; price suggested at 5 to 10 percent of the agreed yearly problem cost, approved by the student.
8. Meta ads: basic version for launch. Jarvis plans and guides, the student clicks, checks run from Ads Manager screenshots, optimise for the completed application, account spending limit set to the 2 week loss limit.
9. Calendar: Google or Microsoft instead of Calendly.
10. sendCheck is function 19 of the app package. Tested: 20 good emails pass, 15 bad ones blocked.
11. Agency builders only for now. Business owners get a separate path later.

Full lists: docs/decisions/2026-11-11.md and docs/decisions/2026-11-13.md. Every file Ali added, replaced or archived: CHANGES-ALI.md.

## 4. Status, honestly

Built and tested locally (not yet on Base44): proposal builder and its render script, Meta campaign setup (7 scenario tests), sendCheck (35 test emails), jarvis-hq rewrite against the app's real tables.

Built and tested on Base44 earlier: Jarvis 2.0 core install, Agency HQ (v3.13), Module 4 skills, landing page and offer skills (before the latest fixes).

Not yet run end to end: a fresh Base44 test of the whole flow with Agency HQ v3.15.1 and the current skills. This is the next step.

## 5. Open items before launch

1. Fresh Base44 run: upgrade a free Jarvis, install HQ v3.15.1 (including Settings, Connections and Set up my voice), run offer, landing page, proposal. Confirm Jarvis can remove old skills, and that every "Use the [skill] skill" prompt triggers the right skill.
2. Install format: decided, one zip per module (course/downloads/jarvis-2 in GitHub). Confirm each installs cleanly in the fresh Base44 run.
3. Ad editing skill: ships a day or two after launch.
4. Calendar switch: 5 skills still mention Calendly or Cal.com (call card, lead hunter, reply desk, confirmation page, SMS). They need rewording for Google or Microsoft calendar.
5. Missions order: mission 3 "First 10 leads" comes before the lead hunter is installed (Module 4). Reorder to match the course.
6. Course text: Module 1, the old CRM lesson, the guarantee objection and the install steps are done. Still to do: the Module 6 pricing example maths, and the Module 4 lesson structure.
7. Prerequisite checks: 16 module skills still need the opening check that refuses to run out of order (ad library research, ad scripting, call card, confirmation page, custom opportunity finder, email setup, landing page, lead hunter, offer creation, pre-call follow up, reply desk, scoping agent, SMS, static ad creator, VSL writer, call to close playbook). The core gates in jarvis-2-brain already stop most out-of-order runs; these are the second lock.
8. Retell voice uses a clone of the film JARVIS voice: IP and publicity risk, decide before any public use.
9. Support systems the course promises (weekly session, developer list, call reviews) have no owner yet.

## 6. Folder map

| Folder | What's in it |
| --- | --- |
| skills/ | All 26 current skills, one folder each. skills/README.md is the index: student prompt, version and test notes for every skill |
| apps/agency-hq/ | The HUD app source, install prompt, release notes, Retell setup, talk mode notes, 3 screenshots |
| docs/ | Decisions, course status, test results (Meta scenarios, sendCheck), Jarvis 2.0 install steps |
| course/ | Blake's full course text (studio/export/COURSE.md), his writing rules (studio/VOICE.md), CRM and outreach specs |
| previews/ | The redesigned course (HUD style and light style, open in a browser), the proposal design |
| research/, context/ | Blake's research and agent context |
| CHANGES-ALI.md | Every change Ali made, batch by batch |

Left out on purpose (still in GitHub): reference videos, test runs, old skill packs, the archive of replaced skills (including the retired offer discovery and opportunity finder skills), the legacy course site, review dumps, and Blake's earlier status documents (COURSE-STATUS.md, HANDOFF-CHECKS.md, REPOSITORY-MANIFEST.json, TECHNICAL-REVIEW.md). Those describe the setup before Jarvis 2.0 and are superseded by this file.

## 7. Also worth seeing

1. Promo film (25 seconds, real HUD screens and the live orb): ask Ali for the link or the MP4.
2. High Ticket Onboarding Map and High Ticket Student Prompts: Claude Docs, ask Ali to share or export.

## 8. Suggested prompts for an agent reviewing this pack

1. "Read START-HERE.md, then skills/jarvis-2-brain and skills/jarvis-hq. Explain how a student goes from upgrade to first client, and list every place the skills and the course disagree."
2. "Check every module skill against skills/jarvis-hq: does each one read and write the right tables and fields?"
3. "Review the open items in section 5 and propose the fastest order to clear them before launch."
