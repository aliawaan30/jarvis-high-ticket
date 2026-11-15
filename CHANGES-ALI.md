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
Rewritten: skills/README.md, the index of all 26 skills with module, student prompt, version and honest test status.
Updated: docs/jarvis-2/INSTALL.md (upgrade also removes jarvis-offer-discovery and jarvis-opportunity-finder); jarvis-custom-opportunity-finder (removed the retired skill's embedded header from its appendix and reference file); START-HERE.md (points to the index).
