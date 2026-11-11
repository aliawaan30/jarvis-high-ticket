# ACT whole-project proposal revision

31 October 2026. Replaces the visual proposal's incorrect existing-build framing for this demonstration. Blake wants a proposal after discovery, before any build has begun: what is being built and why, the problems and cost, solution, timeline and commercial terms. Plain section names; use it to present on a call.

## Files

- Current HTML: `/Users/blakestephens/Downloads/ACT-CRM-Proposal/ACT-CRM-Proposal.html`.
- Prior visual HTML/CSS/JS preserved in `Downloads/ACT-CRM-Proposal/archive/visual-v1-2026-10-30/`.
- Source: this folder's `build.py`, generated HTML, CSS and JavaScript.
- Previous plain PDF and editable Markdown are unchanged; they do not represent this revision.

## Structure

1. ACT CRM proposal: propose the full new CRM and connected workflow.
2. Problems: six actual workflow issues, staff actions and practical consequences.
3. Current cost: six distinct task buckets, current and proposed minutes, volume and loaded hourly cost, monthly/annual current handling cost and capacity released.
4. Proposed build out: map each deliverable to the change for ACT.
5. CRM example: six-stage sample job, no live integrations.
6. Project scope: build/integrations/testing/training; agree inventory, migration and ownership before start.
7. Timeline: proposed eight-week planning estimate, subject to technical scope and ACT inputs.
8. Costs: unpriced build/support/tools inputs, proposed 40/40/20 milestones and first-year budget calculation.
9. Next steps.

## Evidence and unconfirmed terms

Read the earlier ACT proposal JSON, proposal brief/source record and call-derived action register. These support the workflow problems; no discovery recording was replayed in this revision. They do not establish ACT job volume, staff handling time/cost, the CRM quote or accepted project dates.

The cost page is explicitly a working example: 60 jobs/month, A$45/hour, 75 current manual minutes/job versus 31 target minutes/job. This gives 75 current hours/month, A$3,375/month, A$40,500/year, 31 target hours and 44 hours released (A$1,980 staff-time value/month). Inputs are assumptions, not ACT findings. Changing the assumptions is necessary before issuing a buyer-specific cost claim. Minutes must not overlap; the model uses jobs completing all included steps, excludes unconverted enquiries, additional revenue, delay costs and net software savings. Capacity is not automatically cash savings.

The eight-week programme and 40/40/20 payment split are proposed draft terms, not an actual agreement. No build/support/software fee invented. Blank fees remain unpriced; zero must be entered explicitly to represent no cost. This is a reviewable draft, not an issue-ready priced quote.

## Checks

- Both JavaScript files passed `node --check`; preview returns HTTP 200.
- Native Safari: current-cost table, item outputs and sample total observed; screenshot inspected for legibility. Scope/headings present in correct sequence. Costs page visually inspected.
- Payment calculation tested with temporary figures (A$10,000 build / A$200 support / A$100 tools): milestones A$4,000/A$4,000/A$2,000; first-year budget A$13,600. Missing inputs initially show dashes rather than zero. Temporary figures were reset by fresh navigation, and are not in the source.
- CRM example selected stage six and observed inspection booking, current action, activity history and 6/6 state. The six-state component is retained from the earlier tested version with the unused old calculator removed.
- No production CRM, sender, client account or external integration changed. Desktop review only; mobile viewport and PDF rendering have not been checked for this revision.
