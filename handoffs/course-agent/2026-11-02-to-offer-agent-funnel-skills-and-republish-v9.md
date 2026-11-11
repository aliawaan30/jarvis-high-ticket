# Funnel skill changes, outreach system, and republish version 9 (2 Nov 2026)

From Claude, after Blake's read on 2 Nov. Three things.

## 1. Landing page skill: one prompt builds the whole front end

Blake: the student should not paste their offer, proof and video into a prompt. Jarvis already has the offer from the offer creation skill. The student's prompt is now one line: "Run the landing page skill for my offer. Domain: [x]. Calendar: [link]. Video: [link or none yet]." The skill must read the saved offer and ask only for what is genuinely missing.

The skill should build three pages in one run, not two prompts:
1. The landing page (compact: audience callout, outcome headline, mechanism line, video, one button).
2. The form: three or four fit questions one per screen, then name, email, phone.
3. The booking page for people who qualify: "Congratulations, your application has been approved. Book your free 30 minute audit." plus one calendar embed. Simple. That is the page the current example site treats as the confirmation step; Blake says it is a book-in page, not the thank you page.

The thank you page (your /confirmation page) stays a separate skill and comes AFTER the booking: "You are booked in, not confirmed yet", a video telling them to accept the calendar invite, then proof. Student prompt: "Run the confirmation page skill for my landing page. Video: [link or placeholder]."

Pre-call follow up skill: same rule. Prompt is "Run the pre-call follow up skill for my offer and my landing page. Calendar: [tool]." It reads the offer and pages itself.

Please update jarvis-landing-page, jarvis-confirmation-page and the follow up skill so these one line prompts work, and reply with what each skill now asks the student for.

## 2. Outreach system

Module 4 (outreach) is seven empty lessons. Blake wants one outreach system the student runs through Jarvis skills: list, enrich, then email, SMS, calls and LinkedIn together on the same lead (three touches a week). I have a research agent writing `research/outreach-stack-2026-11-02.md` (email limits and sequencers with APIs, SMS numbers and rules per country, AI calling options, LinkedIn tools with APIs, one stack with costs). When it lands, please read it and propose the skill set for the outreach system: which existing skills cover list and enrichment, what is missing for sending, and what the student's one line prompts would be. Blake's words: "why don't we just give them skills for mass email outreach, sms and calls together and linkedin and they can do it all together."

## 3. Republish version 9

`hosting/reading-copy/dist/` is updated (byte match with `reading-copy/`). Publish to the SAME URL. Verify live: "11. AI content agency for ecommerce brands", "Run the landing page skill for my offer", "Follow ups due", and that "Build the Demo" no longer appears. Reply in `handoffs/2026-11-02-from-offer-agent-funnel-skills-and-republish-v9.md`.

## Part 1b, added 2 Nov evening: market scoring lives in the skill

The irresistible offer lesson now uses a one-line prompt: `Score [niche, size of business, country or city] against the five tests.` The offer skills must hold the five tests so the student never types them. Add a scoring step (to jarvis-offer-creation or jarvis-offer-menu, your call) that: runs the five tests with real research (1. they already spend on this problem, what they pay today; 2. the pain has a dollar figure, written as a yearly formula; 3. they have the money, staff, premises, revenue signals; 4. the decision maker is reachable, where name and number show up; 5. the one problem they would pay to have solved tomorrow, in their words), scores each 1 to 5 with evidence and one proving line, adds them, and returns: 20 or more go, 15 to 19 narrow the niche and say how, under 15 move on and suggest two markets next door that score higher.

Also note offer 2 (booked sales calls, paid on performance) was rewritten: the engine is installed inside the client's accounts (domain, LinkedIn, number, calendar) and works their ad leads, old database, then cold outbound. Cold outbound alone is capped per account and never the whole engine. Keep the offer menu consistent with that.

## Part 4, added 2 Nov evening: the skills now live in a shared repo

`projects/high-ticket-program/skills` is now a symlink into `projects/high-ticket/skills`, a git repo shared with the technical lead (private, GitHub Blakeyyyyyyy/high-ticket). Same paths work, nothing changes for you, but commit your skill edits there when a piece of work is done: `cd projects/high-ticket && git add skills && git commit`. Seven skill files still contain em-dashes, which is against the no em-dash rule for anything a member pastes: jarvis-custom-opportunity-finder/references/research-method.md, jarvis-offer-discovery/SKILL.md, jarvis-offer-menu/references/us-sector-agencies-2026-11-02.md, jarvis-proposal-builder/assets/call-two/PRESENTER-NOTES.md, jarvis-static-ad-creator/SKILL.md, jarvis-vsl-writer/SKILL.md, jarvis-vsl-writer/references/vsl-source-notes.md. Replace them.
