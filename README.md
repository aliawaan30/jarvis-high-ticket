# Jarvis high ticket course and skills

The complete available course source and Jarvis skill collection for Blake's high-ticket AI agency programme. This private repository is the technical review workspace for Blake and the technical lead.

Start with [TECHNICAL-REVIEW.md](TECHNICAL-REVIEW.md), then [the skill index](skills/README.md) and [the current course status](docs/COURSE-STATUS.md). It contains drafts and incomplete lessons. Source availability is not student readiness or proof of commercial results.

## What is included

| Location | Contents |
|---|---|
| [course/studio](course/studio) | Current Claude-authored lesson JSON, ordered modules, images, sketches, editor and local Python server. This is the course authoring source. |
| [course/reading-copy/index.html](course/reading-copy/index.html) | Complete current reading page for local team review, including visibly unfinished lessons. |
| [course/studio/export/COURSE.md](course/studio/export/COURSE.md) | Current text export for reading in GitHub. |
| [skills](skills) | Fifteen canonical skills, with their references and reusable proposal assets. |
| [course/outreach](course/outreach) | Existing coordinator skill, data contract, research and proposed lab. |
| [course/crm](course/crm) | Member CRM brief, spec, plan, references and proof/status notes. |
| [course/research](course/research) | Offer catalogue and provider/channel research. |
| [dependencies/free-course-skills](dependencies/free-course-skills) | Four existing lead-finder/CRM blueprints referenced by the course. Porting dependencies, not validated replacements for the custom member CRM. |
| [archive/recovered-skills](archive/recovered-skills) | Earlier call review, client onboarding, marketing research and pre-sale solution-scoping skills. Review before reuse; not the default current pack. |
| [tests](tests) | Existing simulated beginner runs and proposal-template examples, with their limitations and rejected branches retained. |
| [docs](docs) | Technical decisions, status, handoff and inventory. |

## Open the course

Python 3.9 or later is sufficient; there are no pip or npm requirements for the local course tools.

```bash
git clone https://github.com/Blakeyyyyyyy/high-ticket.git
cd high-ticket
python3 -m http.server 4331 --bind 127.0.0.1 --directory course/reading-copy
```

Open http://127.0.0.1:4331. GitHub shows HTML source rather than running it. This review copy has no login or member gate.

To edit the lessons instead:

```bash
python3 course/studio/server.py
```

Open http://127.0.0.1:4330. The editor saves directly to `course/studio/data/`. Keep it local; it is an authoring tool, not a production member portal.

## Rebuild and check

```bash
python3 scripts/build_reading_copy.py
python3 scripts/review_inventory.py --write
python3 scripts/review_inventory.py --check
```

The first command builds a complete HTML document from this checkout, without publishing. The second regenerates the course status, text export and manifest; the third checks source completeness, skill reference assets and the manifest. These checks do not run the skills in Base44.

The previously published version 9 reading copy is at https://jarvis-review-b8f2a64c9e7d4301a5c6.blakeyyyyyy.chatgpt.site . This repo can advance independently; changing GitHub does not republish that site.

## Working rules

- Use the JSON outline for current lesson order. Old module IDs need not match their displayed module numbers.
- Read [VOICE.md](course/studio/VOICE.md) and [CONVENTIONS.md](course/studio/CONVENTIONS.md) before editing lessons.
- Student prompts stay short. Skills read saved context; do not request the same offer and proof repeatedly.
- No em dashes in canonical student skills. No invented proof, economics or guarantees.
- Public marketing does not disclose offer pricing. Private proposals and internal planning can include commercial figures.
- Keys and passwords belong in secret storage, never chats, lessons, Git or skill files.
- Distinguish drafted instructions, local checks, tested integrations and actual student results.
- Commit only this repo's intended files. Preserve the private visibility and existing collaborator access.

The technical guide contains the workflow, expected inputs/outputs, current gaps and first tests. It does not authorise outreach, ad spend or deployment of client systems.

## Added 10 Nov 2026: the full workspace

Everything from both working folders now lives here, so the technical lead has the same context Blake's agents have.

| Location | Contents |
|---|---|
| [handoffs/course-agent](handoffs/course-agent) | Every note passed between the course agent and the skills agent since 28 Oct: offer research, outreach system, funnel decisions, republish requests and replies. Read these for the reasoning behind each change. |
| [handoffs/2026-10-23](handoffs/2026-10-23) | The original skills package manifest. |
| [archive](archive) | Earlier versions of skills (offer creation before the six-line version, proposal builder before the close template, pre-recovery skills), the previous program AGENTS.md and the 30 Oct skill index. |
| [research](research) | US service demand and offer recovery research behind offer 5. |
| [reviews](reviews), [references](references) | Review recordings and the reference material skills were built from (one 69 MB video is left out, it is on Blake's Mac). |
| [tests](tests) | Every skill run and proposal build so far, including the CRM proposals. |
| [context](context), [training](training), [course-shell](course-shell) | Skills agent state files, setter technical training, and the early course shell. |
| [course/skill-packs](course/skill-packs) | Dated student skill pack builds. |
| [course/legacy-site](course/legacy-site) | The first static site generator, superseded by the studio. Kept for the lesson scaffolding it holds. |
| `course/hosting` | Not tracked. Three deploy repos with their own history (reading copy, funnel examples, GitHub reading copy). |

Blake's agents still work through their old paths; those are symlinks into this repo, so an edit anywhere lands here. Commit after each finished piece of work.
