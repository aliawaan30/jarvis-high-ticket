# Disagreements and required CRM fields

29 October 2026. Coordinator candidate built at `outreach/skills/jarvis-outreach-coordinator/SKILL.md`, with list, contact research, scoring, CRM/execution, lab and optional Clay references. No pilot or outreach launched.

## Disagreements

1. **“Phase B can start without any account or authorisation” is not operationally correct for Places.** It requires an authorised connection, appropriate access and confirmed usage limits. “No paid data subscription” is the accurate goal; an exhausted free allowance can incur charges. Existing authorised tools or a supplied/manual list can avoid new procurement. The skill proceeds with routine research once that scope exists, rather than asking for permission for each lookup.

2. **Free discovery is not unrestricted storage or contact harvesting.** The Places data-use restrictions raised in the preceding review still apply. Automated collection of published emails also needs the source/method assessment in Claude's jurisdiction research. Keeping the lab read-only and unsent does not answer those questions. Source-specific retention and collection rules belong in the adapter. The coordinator does not treat a website email as automatic sending permission.

3. **Owner discovery and coverage claims remain overstated.** ABN Lookup does not reliably return a company's owner. Registry access, fields and fees vary internationally, and an officer may not own the workflow budget. Website staff size and after-hours answering are often not observable. “Email on most sites” versus “roughly half” contradict each other and neither has a measured basis for this cohort. The candidate returns unknowns and a business-line buyer-identification task instead of filling names or symptoms by inference.

4. **“Just as effective” and “costs nothing beyond time” are untested.** The lean path is a good first design, but coverage and eventual meetings must be measured. Existing platform/model/mailbox/phone costs still exist. No paid data is a constraint, not a performance result. The proposed 30-account lab establishes findings only for that offer/category/country.

5. **Manual sending needs a real stop mechanism.** Logging a reply must cancel CRM tasks and, if relevant, trigger a member/provider stop action. A Google Workspace connection does not by itself supply campaign scheduling, suppression, reconciliation or global stopping. The course should explicitly teach the manual fallback until those connections pass.

## CRM requirement requested in the handoff

The full field/stage contract is in `references/crm-and-execution.md`. The essentials are accounts, contacts, evidence, versioned offers/campaigns, draft/action queue, conversation/events, persistent suppression and opportunities linked to proposals and projects. Preserve fit, identity, reachability and channel eligibility as separate fields.

Research states: new, researching, needs review, reviewed fit, excluded. Sales stages: not contacted, contacted, conversation, call one booked, attended/qualified, scope/proposal, call two, won/lost/nurture. Store booking, attendance and qualification as separate events even if combined in a visible stage. Action states must distinguish draft, approved, queued, attempted, confirmed, unknown and cancelled. `pause_requested` is not `paused`.

Without these records, putting the CRM earlier in the course only creates an empty dashboard. The member needs an account card and next action they can use while making the call, plus a simple way to log a result and stop follow-ups immediately.
