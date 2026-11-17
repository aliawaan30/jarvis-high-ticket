# Case study brief: building Jarvis 2.0

For the agent writing the case study. Everything below comes from the project record (October to November 2026). Images are in the images folder, described in IMAGES.md. Use only these facts. If you need a number or a quote that isn't here, leave a placeholder like [ASK ALI] instead of inventing one.

## 1. Writing rules

1. Subject: Ali Nawaz, Technical Project Manager, working with Blake Stephens (CEO, The AI Agency Builder) during a trial period.
2. Tone: confident, plain, specific. Short sentences. No hype words.
3. Never use em dashes or en dashes. Use commas and full stops.
4. Keep business results and Ali's work separate. The company's revenue figures happened before and alongside Ali's work. Do not credit them to him.
5. Be honest about status. Several pieces are built and tested in code but not yet proven end to end on Base44. Say so where it matters. Honesty about testing is part of the story.
6. Check with Ali before naming Blake, the company or Base44 publicly, and before using any screenshot.

## 2. Context

1. **The business:** The AI Agency Builder teaches people to start AI agencies selling AI websites, AI receptionists and AI property walkthrough videos to businesses in the US, Australia and similar markets.
2. **The free offer:** a free Skool course plus Jarvis, a personal AI agent built on Base44.
3. **The model:** Blake is a Base44 partner, so student usage on Base44 earns the company revenue. Every product decision weighed that.
4. **Company traction** (not Ali's result): about $92k to $95k in the first 30 days, with 8 sales reps.
5. **The goal:** sign 20 to 25 high ticket clients a month, with a premium programme built around Jarvis.
6. **Ali's brief, three workstreams:** take the current Jarvis from good to great, build Jarvis 2.0, and help design and deliver the high ticket offers.

## 3. The problem Ali found

From his audit of the free course (11 courses, about 100 lessons, 15 skill files) in October:

1. **Students did too much by hand.** About 65 copy and paste prompts sat in two modules alone.
2. **Skills and lessons disagreed.** Lesson text and skill files had drifted apart, so students got different instructions in different places.
3. **No single source of truth.** Work lived across chats, zips and two people's machines.
4. **Claims weren't tested.** Some features were described as working without proof on Base44.
5. **No student CRM.** Leads, calls and deals had nowhere to live, so Jarvis couldn't track a student's business.
6. **The high ticket offer needed a delivery system,** not just more lessons.

## 4. How Ali worked: principles worth highlighting

1. **Three honest levels for every feature:** written (a rule in a file), tested in code (the logic runs), proven on Base44 (Jarvis actually did it). Only the last counts as working.
2. **Critical steps go in code, not instructions.** Anything that must be exact (sending email, rendering a proposal, checking a lead) became a script or a function, because AI instructions can drift.
3. **Students never paste what Jarvis already knows.** Every skill reads from and writes to the student's own CRM.
4. **Scenario testing before shipping.** Each skill was tested against realistic student situations, issues were logged, fixed and retested.
5. **One source of truth.** Everything moved into one GitHub repository, pushed in documented batches with a change log.
6. **Solve, don't report.** Jarvis fixes what it can itself, walks the student through what only they can do, and only then hands over a ready support message.

## 5. What Ali built, in order

### Late October: fixing the current Jarvis

1. **Onboarding v2:** two paths (business owners and agency builders), tested on real Base44 agents, handed to Blake with a document, a Loom walkthrough and a GitHub repo.
2. **Skool course review and business audit** for Blake: every lesson and skill file reviewed, issues ranked.
3. **Website skills v3:** 7 skills for the AI website service. An automated run passed 23 of 24 checks.
4. **Course flow redesign** ("results first"), so students reach a real outcome sooner.

### 2 to 9 November: Jarvis 2.0 and client acquisition

1. **The Jarvis 2.0 core:** four always-on skills. The brain (how Jarvis decides what's next), HQ (where every piece of data lives), rhythm (automatic jobs like a morning brief and Friday numbers) and missions (19 steps from setup to the first client live, each counted only when proof exists).
2. **Module 4, client acquisition:** 6 skills (lead hunter, email setup, outreach coordinator, call card, reply desk, SMS) and 8 lessons. The lead hunter runs a code-based checker on every website, and every reason to contact a business needs a source link.
3. **A send gate:** plain code that checks every email before it goes out (no guessed addresses, no one who asked to stop, daily limits, no spam phrases).
4. **Testing at scale:** 16 full test runs on Base44. Automated checks reached 97 of 97 verified fixes and 23 of 23 send gate tests. Credits were measured: about 0.1 credits per lead hunt, 4.7 to 6.2 credits per full test run.
5. **Learning from failure:** one full run scored 2 of 13. Ali traced the root causes (skills not updating on reinstall, invented signals, shallow contact searches) and fixed each one. A fresh-agent run on 9 November showed Jarvis can't reliably build apps through Base44's builder, so the approach changed: the student installs the CRM from a package and Jarvis checks it.

### 9 to 11 November: offer, funnel and ads

1. **Offer skills,** improved over 4 rounds plus Blake's feedback and tested with student personas. Average score went from 6.25 of 8, and the 3 weakest rose from 5.7 to 6.8 on retest. The offer now comes as an approval card ("Approve it, or tell me what to change") and never invents proof.
2. **Landing page, confirmation page, pre-call follow up and Meta setup** fixed in two rounds, including colour palettes, SMS consent and a revenue qualifier on the application.
3. **An ad editing skill** with its own editing engine: raw phone footage in, three finished ads with different hooks out.

### 11 to 15 November: making it one system

1. **One repository:** Blake's work and Ali's work consolidated into one GitHub repo, pushed in 7 documented batches.
2. **Proposal builder, rebuilt:** a one page premium proposal. The design lives in a render script, so it never drifts and refuses to render with a missing price or leftover placeholders. It suggests a price at 5 to 10 percent of the client's agreed yearly problem cost, and the student approves it. The price only appears in the costs section, so the sales call's anchor still works.
3. **Meta ads, rebuilt from research:** at a $500 cost per booked call, Meta's learning phase would need about $25,000 a week to optimise for bookings. Ali switched the optimisation to completed applications and kept bookings as the real score in the CRM. 7 scenario tests found 5 issues, all fixed, including a hard spending limit so a student can never lose more than they planned.
4. **The send gate bug:** testing showed the old gate would have blocked every single good email, because the CRM stores yes and no as text. The rebuilt gate passes 20 of 20 good emails and blocks 15 of 15 bad ones, and ships inside the CRM package.
5. **Agency HQ v3.14:** the student's CRM and command centre (18 tables, 19 functions, a live voice call with a particle orb). The HQ skill was rewritten to match it field for field.
6. **The full programme map:** 8 steps from upgrade to first client, with gates so students can't skip ahead, and 18 problem situations each with Jarvis's fix.
7. **The course, redesigned:** all 42 lessons in the HUD's style, each labelled Training, Skill or Prompt, every prompt naming its skill, every skill lesson showing a worked example and a checkpoint.
8. **A 25 second promo film** built from the real CRM screens, with the voice orb ported from the app's own code.
9. **A system pack for Blake:** a START-HERE guide, an index of all 26 skills with prompts and versions, and 14 automated checks all passing.

### 17 November: the agentic HUD

Following Blake's feedback, Ali redesigned the CRM's home screen to feel like a team at work: Jarvis's roles (Scout, Writer, Closer, Ops) light up as they work, a live feed shows what Jarvis finished, and students can message or talk to Jarvis directly. Planned alongside it: Jarvis checking in three times a day with what happened, the one next task, and progress toward the goal.

## 6. Numbers you can use

| Number | What it means |
| --- | --- |
| About 100 lessons, 15 skill files | Audited in the first week |
| About 65 | Copy and paste prompts found in two modules |
| 26 | Skills in Jarvis 2.0 today |
| 19 | Missions from setup to first client live |
| 42 | Lessons in the redesigned course |
| 8 steps, 18 situations | The onboarding map and its problem playbook |
| 16 | Full Base44 test runs during Module 4 |
| 97 of 97 | Verified fixes in Module 4's automated checks |
| 0 of 20 to 20 of 20 | Good emails passing the send gate, before and after the fix |
| 15 of 15 | Bad emails blocked by the new send gate |
| 6.25 of 8, weakest 5.7 to 6.8 | Offer skill persona scores, before and after fixes |
| 7 scenarios, 5 issues fixed | Meta ads skill testing |
| 18 tables, 19 functions | Agency HQ v3.14 |
| 14 of 14 | Automated checks passing on the final system pack |
| About 0.1 credits | Cost of one lead hunt on Base44 |

## 7. Four stories that show the thinking

1. **The bug nobody would have seen.** The send gate looked fine in review. Testing it against data the way the CRM really stores it showed it would block every email. A student would have connected Gmail, launched a campaign, and nothing would ever have gone out.
2. **Doing the maths before the ads.** Instead of copying the usual "optimise for bookings" advice, Ali checked what Meta's algorithm needs and found it was impossible at this price point. One setting change protected every student's ad budget.
3. **Testing that changed the plan.** When a fresh Jarvis couldn't reliably build the CRM, Ali didn't patch around it. He changed the approach so students install a tested package and Jarvis verifies it.
4. **Honest by design.** Every skill carries a version. The system pack lists its own open items before any reviewer finds them. Features are only called working once proven on Base44.

## 8. Still in progress (be honest about this)

1. A full fresh run of the whole flow on Base44 with the current version.
2. Switching booking from Calendly to Google and Microsoft calendars.
3. The ad editing skill's move into the main repository.
4. Course text updates to match the skills.
5. The agentic HUD and three-a-day check-ins: designed, not yet built.

## 9. Visuals

The images folder has 11 images, and IMAGES.md says what each one shows and where it fits in the story. Images 10 and 11 are previews of the next version, so label them as coming next, not live. The 25 second promo film is available from Ali as an MP4. Ask Ali before publishing any image.

## 10. Suggested structure

1. Headline and one-line summary.
2. The situation: a fast-growing course with a good AI agent, and growing pains.
3. The challenge: too much manual work, drift between lessons and skills, no system behind the student.
4. The approach: the six principles in section 4.
5. What was built: Jarvis 2.0, the CRM, the skills, the course.
6. How it was tested: the numbers and the four stories.
7. Where it's going: the agentic HUD and the launch.
8. [ASK ALI] for a quote from Blake, if he's willing.
