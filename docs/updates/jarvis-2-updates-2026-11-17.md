# Jarvis 2.0 updates, 17 November 2026

Everything that changed today after Blake's feedback, what was tested, and what still needs proving before the first onboarding call.

## 1. Decisions made today

1. **Check-ins:** twice every working day, sent to the student's connected channel.
2. **Agentic HUD v3.15:** approved. Same functions as before, with the agentic look and only the information students need.
3. **Team names:** Scout (leads), Writer (outreach), Closer (calls and proposals), Ops (rhythm and missions).
4. **Voice:** one choice. Browser voice (free) or Retell voice (an add-on). Retell pricing for students to agree with Blake.
5. **Keys:** one Connections screen in HUD Settings.
6. **To build next:** an existing agency audit skill.
7. **Parked:** the onboarding call agent, the pre-call intake skill, and Retell actions during the call.
8. **Ad editing skill:** ships a day or two after launch.
9. **Install format:** one zip per module.

## 2. What changed

### The rhythm (check-ins)

1. **Two check-ins every working day:** the morning brief, then an afternoon check-in 6 hours later. The evening log is folded into the afternoon check-in.
2. **Sent where the student already is:** WhatsApp, Telegram, iMessage, Slack or LINE, whichever is connected, otherwise Base44 chat. If nothing is connected, Jarvis offers once to set up WhatsApp or Telegram.
3. **Always three parts, under 80 words:** since last time, your one next task, and where you stand against today's target.
4. **It adapts:** a win goes first, two ignored check-ins make the next task smaller, and if nothing changed it says so in one line.
5. **Never skipped to save credits.** Each one stays short instead.
6. **Files:** jarvis-rhythm and jarvis-2-brain (version 2026-11-17.1), the install steps, the skill index.

### Agency HQ v3.15 and v3.15.1 (the HUD)

1. **Agentic home screen:** Scout, Writer, Closer and Ops around the core, lit from real running tasks. Shows who is working on what, the next check-in, a Needs you list (drafts to approve, your next task), a Message Jarvis box with Jarvis's real reply, and roles on the live feed.
2. **Settings, Connections:** every key in one place, each with a ? explaining what it is and where to get it. Keys are saved in a locked Vault table that only the app's backend reads, and are never shown again (last 4 characters only). Keys already in Base44 Secrets keep working.
3. **HUD key created automatically,** handed to Jarvis with Copy for Jarvis.
4. **Set up my voice:** one button builds the whole Retell voice agent. The new agent greets in its own voice.
5. **Voice simplified:** Browser voice or Retell voice. Fish Audio is hidden from students.
6. **Feed fixes:** debug lines hidden, long entries cut to 3 lines and expand on click, Closer counts replies waiting for a call.
7. **What it adds to the app:** a Vault table (19 tables), a connections function (20 functions), and a retell_greets field on the Profile.

### The course

1. **Module 1 rewritten:** Install Jarvis 2.0, How Jarvis 2.0 Works, and Your Jarvis HUD (the new CRM, with the Connections screen).
2. **Removed from the course outline:** the old Your CRM lesson, and Prove It on Something Real.
3. **Module 6:** the objection "Can you guarantee it'll work?" is removed, because students now offer a guarantee.
4. **Every module from 2 to 7 opens with its install step,** naming its zip and its skills.
5. **Course export regenerated** with Blake's own studio code.

### Downloads

The 7 module skill zips (all 26 skills, each in one module) and agency-hq-v3.15.1.zip, in course/downloads/jarvis-2 on GitHub.

### Skills

jarvis-hq (2026-11-17.1) now guides students through the Connections screen.

### Other deliverables

1. **Case study pack:** a brief, 11 images and captions, ready for another agent.
2. **System pack for Blake:** updated, and all 13 checks pass.

## 3. How it was tested

1. **Full production build of the whole app:** 1,867 modules, no errors.
2. **Connections logic:** 9 of 9 pass. HUD key created automatically, keys never returned in full, no duplicates, bad keys rejected, Secrets take priority, non-owners and logged-out users blocked.
3. **Set up my voice against a stand-in Retell:** 4 of 4 pass. Full build, reuse instead of duplicating, a clear warning on partial failure, a clear message for a bad key.
4. **On Ali's Base44 app:** v3.15 installed, the agentic HUD renders, and Connections reads the existing keys correctly.

## 4. GitHub batches from today

| Batch | What |
| --- | --- |
| 3e | Twice-daily check-ins |
| 3f | Course text, module installs, skill downloads |
| 3g | Agency HQ v3.15 |
| 3h | Agency HQ v3.15.1 |

Push them in order. 3h's first command only works once 3g is in.

## 5. Ready for tomorrow's onboarding?

**Ready for a guided call, once tonight's checks pass.** Each check below is about 10 minutes.

### Must check tonight

1. **Upgrade your app to v3.15.1,** and confirm the builder reports 19 tables and 20 functions.
2. **Message Jarvis on the HUD:** type "What's next?" and get a real reply. Still unconfirmed.
3. **Set up my voice:** one press, then a Talk call that opens with Jarvis greeting you in the Retell voice. If it fails, use the browser voice tomorrow. That works without Retell.
4. **Reinstall the core skills on your Jarvis** (jarvis-skills-module-1-core.zip), so your own Jarvis runs the new twice-daily rhythm.
5. **A fresh run on a test Jarvis:** install the core zip, install HQ, one lead hunt, one approved email to a test inbox. It proves the student path end to end.

### Blake's side

1. The course published at a real link, so it can go in the client channel.
2. The onboarding call calendar.

### The run sheet for the call

1. Before the call, the client installs Jarvis 2.0 and Agency HQ, or you do it together in the first 20 minutes.
2. Connect Gmail and the calendar.
3. Pick the offer together: "Use the offer creation skill to write my offer." Approve it live.
4. Lead hunt live: 10 real businesses appear in their HUD.
5. First emails drafted and approved.
6. Talk to Jarvis from the HUD: "What should I do before tomorrow?"

### Keep out of tomorrow's call

Anything not yet proven live: Retell actions during the call, the existing agency audit, and the ad editing skill. Mention them as coming soon, not as live features.

## 6. Still open after tomorrow

1. Calendar switch from Calendly in 5 skills.
2. Prerequisite checks in 16 skills.
3. Missions reorder.
4. Module 6 pricing example maths, and the Module 4 lesson structure.
5. Test every "Use the ... skill" prompt on Base44.
6. Existing agency audit skill.
7. Ad editing skill into the repo.
8. Retell add-on pricing, the voice decision, and an owner for support.
