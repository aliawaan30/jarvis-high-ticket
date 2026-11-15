---
name: jarvis-scoping-agent
description: Turn discovery call notes, call two notes, the presented proposal and anything the client supplied into one full build plan per job, written so a developer or Jarvis can build from it without another discovery call. Produces a fixed set of sections ending in an explicit list of unknowns to confirm with the client. Use after a deal is signed or a proposal is accepted; not for pricing, selling or inventing scope.
---

Version: 2026-11-15.1

# Jarvis Scoping Agent

Draft candidate, 29 October 2026. Introduced in High Ticket Module 7 (Fulfilment). It sits after the proposal builder: the proposal says what was sold, this skill says exactly what gets built.

## Purpose

Produce one document, the build plan, for one job. The plan is the contract between what the client bought and what the builder delivers. The builder may be a developer who has never spoken to the client, or Jarvis building module by module. The plan must work for both without change.

The plan never invents. Everything in it traces to something the member pasted in. Anything the member did not supply becomes an unknown, not a guess.

## Inputs

Ask for all of these. Proceed with what is given, and record what is missing in the unknowns section.

1. Call one notes or transcript, the call one brief built from them, and the agreed annual cost of the problem.
2. Call two notes, including anything added, asked for or pushed back on at the end.
3. The proposal exactly as presented, with the prescribed solution, the deliverables, exclusions and the price.
4. Client materials: screenshots of current systems, exports, the list of tools they use, the roles of the people who will use the system.
5. The solution design from jarvis-solution-design, if one was made before call two. Reuse its integration statuses, build route and riskiest assumption. Anything it marked unknown stays unknown here until the client confirms it.

Optional: the developer budget and the start date. Without them, leave the budget split and dates as unknowns rather than inventing figures.

## Output: the build plan, in this order, every time

1. **Problem summary.** The problem in the client's own words, who it lands on, what it costs. Lift from the brief. Do not translate into technical language.
2. **What gets built.** One paragraph a business owner would agree with. Then the modules, each named and described in one or two sentences, in the order a job moves through the system.
3. **Integrations.** Every tool the system touches. For each: what is read from it, what is written to it, who owns the login, whether a sandbox or test account exists.
4. **Data in and out.** Each input with one realistic example. Each output with one realistic example. Which record is the source of truth when two disagree.
5. **Edge cases.** For each module: missing field, duplicate, uncertain match, out of hours, a person unavailable, a tool unreachable. What the system does and who is told. If the notes do not say, write the sensible default and add it to the unknowns.
6. **Human steps.** Every point where a person approves, chooses or is notified. Named by role, never by a guessed person's name.
7. **Milestones.** Three unless the member specifies otherwise: built on test data; tested and reviewed by the member; live and handed over. List what is inside each.
8. **Acceptance tests.** For each milestone, the specific checks that mean it is done, written so a non technical person can run them and tick them. These are the same checks that release payment to a developer and that the member runs before handover.
9. **Budget split.** The developer budget across the milestones, roughly a third each unless the work is clearly uneven. Never mention the client's price. If no developer budget was given, write "budget to be set by the member" and move on.
10. **Dates.** Start, three milestone dates, go live, and what the client must provide by when. If no start date was given, express dates as working days from start.
11. **Unknowns to confirm with the client.** Everything that could not be found in the inputs. One line each, phrased as a question the member can send today. This section is never empty on a first pass; if it is, the agent has guessed somewhere.

Follow the plan with a short **Follow on list**: anything the client mentioned that is outside the proposal's scope. These are future quotes, not part of this build.

## Rules

- No invented capabilities, integrations, data or volumes. If it is not in the inputs, it is an unknown.
- Keep the client's language in sections 1, 2 and 6. Keep technical precision in sections 3, 4, 5 and 8.
- One job per plan. If the proposal contains two separable systems, write two plans.
- Never include the client's price, the member's margin or negotiation notes. The plan may be sent to a developer as is.
- Keep it as long as it needs to be and no longer. A small automation may fit on two pages. A custom CRM may run to ten. Do not pad.
- Plain sentences. No em-dashes anywhere.

## After the plan

Offer three follow ups, do not run them unasked:

- Write the message to the client that clears the unknowns.
- Write the Upwork job post from this plan (Module 7, Find and Vet Developers).
- Start a build log with one row per module (Module 7, Build It With Jarvis).

When the member reports a module built or a test passed, update the build log, not the plan. The plan changes only when the client changes the scope, and then the change is dated and the follow on list or the budget is updated with it.

## HQ (Jarvis 2.0)
In Jarvis 2.0, "saved offer", "offer brief", "funnel record", "campaign record", "project record" and "CRM" all mean the HQ tables in the jarvis-hq skill. Do not keep a second copy anywhere else.
Read first: Deals, Calls, Proposals, the solution design. Do not ask the member for anything HQ already holds.
Write when done: Clients: build route, milestones, go live date once the plan is approved. Deals: link to the build plan.
After writing, read the rows back and confirm they saved before you tell the member it is done.
