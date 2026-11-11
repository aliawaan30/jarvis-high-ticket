# Student CRM: brief for the build agent

Owner: Blake. Builder: this Codex session (GPT-6 Astra). Date: 31 Oct 2026.

Rule one: students never debug this. If a member would ever need to open code, a database, a webhook page or a settings screen they do not understand, the design is wrong.
Rule two: spec first. Do not build anything until Blake says go. Your first output is a one page spec and a build plan, then you stop and wait.

## Who uses it

Members of Blake's high ticket programme. Each runs a small AI services agency selling five figure systems to business owners. This CRM runs THEIR agency's pipeline: their leads, their calls, their deals. It is not the CRM they sell to clients.

## What it realistically needs. Seven things, nothing else in v1.

1. Leads. Name, phone, email, business, source (Meta ad, outreach, referral), stage, notes, next action date.
2. One pipeline with fixed stages: New lead, Contacted, Call 1 booked, Call 1 done, Proposal sent, Call 2 booked, Won, Lost, Not now. Drag between stages. No custom pipelines.
3. Leads arrive on their own. Meta lead forms land automatically through the Base44 Meta connection [VERIFY ON PAID PLAN]. A calendar booking creates or updates the lead and moves it to Call 1 booked. Outreach leads are added by the member's Jarvis or by hand.
4. Follow up runs through the member's Jarvis, not a workflow builder. The CRM fires a webhook on every stage change and exposes a small API (create lead, update stage, add note, read pipeline, write daily numbers). Jarvis sends the pre call reminders, the no show re-book and the proposal follow up. Sending identity: the member's own Twilio number for two way SMS and the member's own mailbox for email, per the sending recommendation in handoffs/2026-10-30-from-offer-agent-offers.md.
5. A daily numbers card: ad spend, leads, cost per lead, calls booked, cost per booked call, show rate, close rate, revenue, CAC against ticket. Jarvis's Meta skill pulls the ad numbers every morning and writes them in through the API. The CRM computes the rest from pipeline events.
6. One screen per lead with the whole history: messages, calls, stage moves, notes.
7. Member login. Each member sees only their own data.

Not in v1, and say no if asked: email builder, website or funnel builder, a calendar engine (use the booking tool the funnel already uses), workflow editor, dialer, memberships, invoicing, reporting beyond the card.

## Architecture to recommend, and to challenge honestly

Default: ONE hosted multi tenant app that Blake's team owns and maintains. Every member logs into the same app. Each member's Jarvis talks to it through an API key for that member. Not one app per student, because one codebase is the only way nobody debugs their own copy.

The alternative to weigh in the spec: GoHighLevel sub accounts loaded from a snapshot Blake's team maintains, driven by the member's Jarvis through the GHL API. It already has the pipeline, two way SMS, Meta lead form intake and a calendar. Cost is roughly US$97 a month per member or Blake's agency plan with unlimited sub accounts. Say which wins and why, with cost, support load and lock in both ways. Do not flatter the custom build.

Platform default is Base44, because the members' Jarvis lives there and the Meta connection is claimed there. Confirm Base44 can do all of: multi tenant data rules per member, external API access with per member keys, outbound webhooks, a scheduled job. Mark anything you cannot confirm [VERIFY ON PAID PLAN]. If one of those fails, say so and propose the smallest alternative that keeps rule one.

## Read before you write

- /Users/blakestephens/co-founder/projects/high-ticket-course/studio/data/lessons/m5-your-crm.json (stub), m5-the-follow-up-that-runs-without-you.json, m5-get-them-to-show-up-ready.json, m5-build-the-page.json
- /Users/blakestephens/co-founder/projects/high-ticket-course/studio/data/lessons/m4-how-ads-actually-work.json (the numbers the card must show, the CAC floor)
- /Users/blakestephens/co-founder/projects/high-ticket-course/handoffs/2026-10-30-from-offer-agent-offers.md (SMS, email, Twilio, Resend rules)
- /Users/blakestephens/co-founder/projects/high-ticket-program/skills/ (jarvis-meta-campaign-setup, jarvis-ad-scripting, jarvis-precall-followup if present)
- /Users/blakestephens/co-founder/projects/base44-course/CLOSER-SALES-PROCESS.md (the two call close the pipeline stages mirror)

## Deliverables, then stop

- crm/SPEC.md: one page. The seven things as screens and fields, the API and webhook list, the daily numbers formulas, the architecture decision with the GHL comparison.
- crm/PLAN.md: build order in small steps, what you build versus what Blake's technical lead does, what needs a paid Base44 plan to test, and the first thing a member sees.
- At most three questions for Blake, at the end of SPEC.md.

No em dashes anywhere. Plain words. Write for Blake, who will read it in two minutes.
