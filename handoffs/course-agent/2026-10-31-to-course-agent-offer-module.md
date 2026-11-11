# Offer module: from a blank page to a service they understand and an offer they can sell

For Claude course session `3dff04c3-a79d-46ee-9e66-3daf91fdb31b`, on Blake's explicit instruction. Prepared after inspecting the structure, prompts and relevant teaching passages in the four current Module 2 lesson JSON files on 31 October. Proposed teaching revision; not a published course change.

## What Blake wants

Students must understand who buys, the problem, why it matters, how it gets solved, and what they actually deliver. Then package that into the six-line marketing offer. They should finish this module with an offer they can explain with conviction, rather than a polished sentence they cannot defend.

Keep the useful education. Remove repetition and claims that substitute certainty for understanding. The DIY course must work without a coach supplying the missing reasoning.

## The missing bridge

The current progression is market theory → ten examples → six lines → demo. It does not explicitly take the learner through working out their own service. “Jarvis already has the market research and the problem you found” assumes work the lessons have not reliably led them through.

Use this progression throughout:

**Find a buyer and problem → understand the business impact → work out the service → write the marketing offer → show the solution.**

Two different outputs belong together:

- **Service brief:** plain explanation of buyer, pain, current process, value, solution and delivery. This gives the student understanding and gives Jarvis shared context.
- **Marketing offer:** exactly the six agreed lines. This gives the student the message for outreach, ads and funnels.

Do not expand `jarvis-offer-creation` into another giant report. Keep the service brief upstream and pass it to that skill.

## Four lessons, four useful outputs

### 1. Understand why the business would buy

Keep the strongest explanation of pain, value, awareness and market fit. Teach problem vs service vs offer using one understandable business example throughout.

- Problem: homeowners receive roof estimates, then go quiet; the rep does not know who still needs help deciding.
- Service: a follow-up system works eligible open estimates, handles approved questions and hands interested homeowners back to the rep.
- Desired result: more of the estimates already paid for become sold jobs and collected cash.
- Marketing offer: the specific promise, timeframe, risk reversal, proof and mechanism we can support.

Explain why the system contributes to sales without pretending the system controls the homeowner's decision or the roofer's closing ability. A result-led offer still needs a credible link between the work and the result.

Keep the five market questions as prompts for judgment, not a scoring machine that declares demand proven. Public signals suggest fit; they do not reveal an individual owner's budget or intent.

**Student output:** explain one business problem, who feels it and what improves when it is fixed. No technical jargon required.

### 2. Find your buyer and problem

Make the ten examples an inspiration library. The student can choose one, adapt it, bring an outside idea or find a different one. They do not need to study all ten before acting.

Three useful entry points:

1. Ad Library research: `jarvis-ad-library-offer-research`.
2. Examples or an existing idea: `jarvis-offer-menu` (optional catalogue, not a restricted menu).
3. Deeper custom opportunity research: `jarvis-custom-opportunity-finder`.

One route is enough. Explain which route fits which learner. Do not force advanced research on a beginner who already has a clear, suitable service; do not force a technical student into receptionist/websites.

Jarvis returns candidate buyer/problem/service combinations in simple language. The student chooses one based on need, access, understandable value and feasible delivery. Put deeper evidence behind the explanation.

**Student output:** one buyer segment, one recurring problem, one service idea, relevant evidence, the strongest existing alternative and what still needs confirming.

### 3. Work out the service and write the offer

This is the bridge to add to the current offer-writing lesson. First complete a short service brief, then use the six-line offer skill.

Use these questions, with short answers:

1. **Who buys?** A recognisable type and size of business, with a person responsible for the problem.
2. **What happens today?** Walk through one real or clearly labelled illustrative example. What tools and people are involved?
3. **Where does it hurt?** What gets missed, delayed or repeated? What does the owner/staff/customer experience?
4. **Why pay to fix it?** Time, capacity, missed margin, delays or other business impact. Show the calculation and label research assumptions. Do not equate all wages with savings or all possible revenue with recoverable cash.
5. **What changes?** Input → system action → exception/human decision → useful result. Show before and after in ordinary language.
6. **What do we provide?** The bounded first build, setup and ongoing work; what the client still does; how the student fulfils it or gets technical help.
7. **Why believe it?** What sources establish the problem, what the demo demonstrates, and what still needs buyer/technical confirmation.

Keep it to a readable page, not seven separate assignments. This is the shared brief for downstream assets.

Then run `jarvis-offer-creation`, which returns exactly:

- Niche
- Outcome
- Timeframe
- Risk reversal
- Authority/proof
- Unique mechanism

Public offer has no price. Private delivery costs still matter before agreeing a commercial deal. A name for the mechanism must describe a real process; naming it alone does not make it unique. A demo demonstrates operation, not client revenue results. Do not invent authority, an achievable timeframe or a guarantee because a template has a blank.

**Student output:** their one-page service brief plus their own six-line offer, using the same buyer, problem and mechanism.

### 4. Show the solution and practise explaining it

Keep this practical and short. Build the smallest demonstration that helps the owner understand the service. A receptionist can be test-called; a custom workflow may need only one realistic input, one exception and the resulting screen/output. A mock-up is labelled as a mock-up. It is not a finished client installation.

Research conversations do not require a complete build first. Custom production software should not be built speculatively before discovery and scope. Before a sales demonstration, test the specific sequence you will show.

The student records a two-minute explanation:

“These are the businesses I help. This is what happens today and what it costs them. Here is the change we make. Let me show you. This is what we handle and what your team still does. This is the result the offer is built around.”

If they can repeat the six lines but cannot explain that, Jarvis helps clarify the brief before more marketing assets are generated.

**Student output:** brief + six-line offer + smallest useful demo/walkthrough. Those become the shared context for funnels, acquisition and sales.

## Specific corrections in the current source

- `m2-three-ways-to-find-an-offer-that-scales.json`: remove “Nobody keeps paying for 90 versions of an offer that loses money.” Ad activity is a useful research signal, not profitability proof. Label six-line service adaptations as teaching examples, not advertisers' verified promises.
- Same lesson: replace closing “Pick one” with choosing/adapting an example OR bringing/researching another idea. Do not claim US offers are generally barely present elsewhere without evidence.
- `m2-write-the-offer.json`: replace “[which one from the list]” with the student's selected service/idea from any route; supply the service brief to the prompt. “They do nothing, they risk nothing” is inaccurate for an implementation with access, decisions and adoption required. Explain reduced effort and defined risk reversal instead.
- Same lesson: the coaching example can show the formula, but use the AI-service worked example to teach the learner's actual task. A borrowed provider's proof is not their proof.
- `m2-build-the-demo.json`: replace universal “build it before you talk to anyone” and “Jarvis builds it in a day” with a smallest-demo instruction matching scope, tools and access. Keep the energetic practical tone; avoid universal delivery promises.
- `m2-the-irresistible-offer.json`: the $13k CRM plus $65k admin example does not establish $78k recoverable savings. Identify replaceable software and the share of admin time actually affected. Missed-call value needs qualified demand, conversion and margin assumptions. “Less aware” is not automatically easier to sell; aim at a buyer who recognises the problem and can understand the fix.
- A 20/25 score, staff count or public phone number is a screening aid, not a proven purchase decision. Avoid hard exclusions that are not justified by the actual deal economics.

## Where validation belongs

Module 2 happens before acquisition. It must not demand buyer-confirmed volume and financial numbers from a call the learner has not yet learned how to book. They leave with researched hypotheses and the questions to confirm them.

Call one later confirms the individual buyer's problem, current cost and requirements. Technical feasibility and delivery cost inform the proposal for call two. The current `jarvis-scoping-agent` creates the detailed build plan after the accepted proposal; do not mislabel it as the pre-sale pricing step.

## Suggested recording format

Show one complete worked example across these four lessons: Blake explains the decision → gives Jarvis the task → reviews its output → corrects weak reasoning → saves the approved brief. Then the member repeats it for their own idea. Every lesson ends with the next concrete output, not another page of theory.

## Coordination

I have not overwritten your lesson files or published this revision. Please implement in the course authoring source, preserving useful explanations and keeping the four-lesson structure unless you see a concrete reason to change it. Reply with disagreements or the changed lesson paths in `handoffs/2026-10-31-from-course-agent-offer-module.md`.

Terminal delivery is currently blocked by the computer-control tool: `Computer Use is not allowed to use the app 'com.apple.Terminal' for safety reasons.` This file is saved for handoff; receipt by your active session is not yet verified.
