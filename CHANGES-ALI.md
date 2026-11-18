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
