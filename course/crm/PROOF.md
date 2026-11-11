# Base44 route proof

**Recommendation:** keep one team-owned Base44 app as the first choice, conditional on passing the hosted tests below. It keeps hosting, login, data and Jarvis integration in fewer places, while still allowing the compact dark interface in the reference. Next.js on Vercel would give us more control over the application and backend choices, but the team would also own the database, authentication and integration setup. The reference's appearance does not require Next.js. Its free-hosting claim is not a budget for this commercial CRM: [Vercel Hobby is restricted to personal, non-commercial use](https://vercel.com/docs/plans/hobby). Today's authentication blocker is not evidence against Base44's capabilities. Blake must confirm Base44 or Next.js/Vercel before screens begin; no platform switch has been made.

31 October 2026. **Step 1 is blocked, not completed. No live proof passed.**

## What actually happened

- Read DECISION.md, DESIGN-REFERENCE.md and PLAN.md, plus the supplied transcript. Visually inspected all four reference JPGs.
- No Base44 config exists at the project root or in `crm/`. No provisioned Base44 app ID or Base44 credential was present in the process environment. No Base44 connector tool was available in this session.
- Attempted the CLI account check with `npm exec --yes --package=base44 -- base44 whoami`. The sandboxed attempt failed with `ENOTFOUND registry.npmjs.org`.
- Retried with approved network access. The CLI reached its login flow and returned: `You need to login first to continue.` It generated a device authorisation request and waited for authentication. Secure login was requested from Blake; no password or token was requested in chat.
- The required authentication check has not succeeded. Workspace ownership, subscription, available connectors and app entitlement could not be inspected. No app was created, no records were deployed, and no Meta accounts were connected.

The [Base44 CLI skill](https://docs.base44.com/developers/skills/base44-cli/index.md) requires: “If the user is NOT logged in ... STOP immediately” before further CLI operations. This is the reason the hosted proof stopped at the access prerequisite.

## Results

The requested status choices are passed, failed or needs a paid plan. **Failed below means the proof attempt failed its access prerequisite, not that Base44 failed the behavioural test.** The actual behavioural tests remain unrun. There is no observed billing rejection, so labelling these “needs a paid plan” would misstate the evidence. All five retain **[VERIFY ON PAID PLAN]**.

| Proof | Status | Observed result | Evidence required for a pass |
| --- | --- | --- | --- |
| Member isolation | **Failed: access prerequisite** | No app or two member sessions available. No cross-member request executed. | In one team-owned app, A and B can access their own leads, activities and numbers. Each is denied the other's records through list, guessed ID, update and delete. Ownership and role changes are denied. Anonymous requests are denied. Test both direct entity access and backend functions. |
| Per-member API keys | **Failed: access prerequisite** | No member keys issued or authenticated API calls executed. | Two random, hashed, scoped keys map to separate members. Own-record calls work; cross-member IDs, forged member IDs, missing/invalid keys and revoked keys fail. Members cannot read key storage. No platform master credential is supplied to Jarvis. |
| Signed stage webhooks | **Failed: access prerequisite** | No deployed sender or receiver; no delivery, retry or signature test executed. | A real saved stage change reaches a controlled receiver with event ID, timestamp and HMAC signature. Tampered and expired messages fail. Timeout and non-2xx responses retry; replays have one effect. A saved change survives a delivery failure and is recovered without losing the event. |
| Scheduled job | **Failed: access prerequisite** | No job deployed or unattended execution observed. | A short proof schedule writes timestamped run records with no browser session. Observe at least two scheduled executions, not manual invokes. Confirm app-specific automation/workflow mode and timezone. Disable the proof schedule after collecting evidence. |
| Meta intake for two accounts | **Failed: access prerequisite** | Connector availability and permissions unknown; neither member account authorised. No lead retrieved. | Two separate member Meta accounts/forms deliver test leads only to their owners. Duplicate events create no duplicate lead. Unknown form/account mappings fail closed. Test token expiry/reconnection without cross-account routing. Separately verify read-only daily spend retrieval for each account. |

## What the public documentation establishes

- [Data security](https://docs.base44.com/developers/backend/resources/entities/security) supports row and field rules, including comparisons to the authenticated user. Service-role calls bypass those rules, so backend ownership checks must be tested separately.
- [Backend functions](https://docs.base44.com/developers/backend/resources/backend-functions/overview) provide external HTTP endpoints. That makes a custom per-member API feasible in principle; it does not prove our key validation or webhook reliability.
- [Third-party API connections](https://docs.base44.com/developers/references/sdk/getting-started/third-party-apis) distinguish shared app credentials from individual user connections and support backend requests. This does not establish that Meta lead forms support the needed per-member connection mode.
- [Scheduled automations](https://docs.base44.com/developers/backend/resources/backend-functions/automations) are documented. Apps with workflows enabled cannot deploy legacy function automations; the applicable mechanism must be checked in the actual proof app.

These are feasibility findings, not runtime passes. No local mock was substituted for a hosted test. No paid-plan capability, credit consumption or operating cost has been verified.

## Resume conditions and boundaries

1. Blake or the technical lead completes Base44's secure device login. If the request expires, run `npx base44 login` locally. Never paste credentials into chat.
2. Confirm the team workspace and its entitlements. Create exactly one backend-only proof app there, using synthetic records and two controlled test users. Do not default silently to a personal workspace or create student copies.
3. Run the five tests above and replace each result with observed status, app ID, timestamp and redacted request/log evidence. If a billing restriction appears, report **needs a paid plan** with the exact blocked operation. Stop on a genuine capability/security failure and report it; do not swap to GHL or Vercel.
4. Meta testing additionally needs two authorised accounts/forms. Paid Base44 access alone does not supply those permissions. Use the providers' secure authorisation screens.

Pilot assumptions remain two members, Gmail/Google Workspace, the funnel's existing booking tool, and a technical owner to be named by Blake. No specific booking provider was established by the supplied lessons. Sender setup, production follow-up and CRM screens are outside this proof.

**Decision pending from Blake:** Base44 or Next.js on Vercel? Screens stay on hold. Only this report was added to the CRM project during this attempt. Step 1 still requires authenticated execution.
