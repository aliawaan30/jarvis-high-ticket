# ACT Certification Services CRM proposal brief

**Buyer:** ACT Certification Services Pty Ltd  
**Use:** Proposal to read through live with ACT owners after discovery  
**Status:** Buyer-specific discussion draft. Not a priced quote, final scope or go-live sign-off.  
**Discovery source:** ACT CRM walkthrough, 9 October 2026; `client-recovery/act-crm-2026-10-06/call-2026-10-09/deliverables/call-review.html` and `action-register.json`.  
**Current build evidence:** ACT project recovery folder; latest retained CRM candidate is `release-2026-10-28-live`. Proposal/browser findings are in `development-2026-10-27/tests/` and earlier ACT handover notes. These describe separate UI/build checks and do not certify the live integrations.

## What ACT said

- Website quote and inspection requests use Jotform. The request emails admin and staff retype information into BCS.
- The workflow moves through request review, pricing/checklist choice, a Word proposal and related ACT forms, signatures, invoicing, payment, assessment and inspections.
- ACT wants separate Enquiries, Proposals and Projects, with non-converting enquiries retained for reporting.
- The CRM should carry uploaded documents, use staff-selected document types/standard names, allow manual uploads, and distinguish approved material from superseded versions.
- ACT wants to keep its Microsoft inspection calendar initially, with booking communication, day-before reminders and a way to handle Y/N replies and exceptions.
- ACT wants workload visibility, assigned tasks, contacts such as builders/engineers/energy assessors, editable checklists and later reporting based on its spreadsheet.
- ACT discussed AI suggesting a suitable proposal template from job details. Staff choose/override it. No agreement for AI to set fees or make building-compliance decisions.
- Initial invoice workflow direction was 100% upfront, with possible 60/40 or other exceptions to define. This does not mean every ACT customer’s terms have changed.

## Proposal recommendation

Build the ACT CRM as the staff workspace for the request-to-assessment process, keeping external services for the functions they already perform. Each enquiry/job should show the current stage, responsible person, documents, activity and next action. Automate reliable handoffs; keep staff responsible for quoted fees, proposal approval and assessment decisions.

## What exists in the current candidate (not all end-to-end accepted)

- Project workspace, project records, task and inspection areas.
- Proposal draft editor based on supplied ACT Word templates; pricing lines, GST/totals and saved revisions have retained browser/API test evidence.
- Library of ACT-supplied government forms and preparation of the three-page Appointment of Certifier; staff must complete owner/classification/declaration/signature fields.
- Signing package flow with internal test PDFs; DocuSign sandbox signing has been exercised. This is not proof of ACT production-account end-to-end acceptance.
- Inspection and booking screens.
- Local template-suggestion logic evaluated; approved example coverage/rules need ACT confirmation.

## Still to prove before ACT can call it live

- Fresh ACT Jotform submissions, correct field mapping, attachments, one-time record/task creation and visible retries.
- ACT DocuSign account authorization, required signer placement, signed-file return and non-completion/duplicate-event handling.
- Correct ACT Xero organization, fee/GST/invoice-type mapping, safe invoice creation, duplicate prevention and actual payment-state handoff.
- ACT Microsoft mailbox/calendar identity and controlled email, reply, attachments, create/reschedule/cancel booking, timezone and message checks.
- Twilio account/number, permissioned staff access, message delivery/replies and booking exception routing.
- ACT-approved role/finance visibility, document categories, checklist templates, reporting definitions, historical-data/cutover scope and acceptance.

## Commercial and delivery facts

The 9 October call record does not state the CRM implementation fee, ongoing support price, licence budget, agreed contract milestones or an accepted delivery date. Do not invent an anchor or ROI. The visible proposal asks to attach the existing agreed commercial terms (or obtain approval for them) before client approval. Current-process staff hours and volumes also need measuring before stating a dollar saving.

The release order is: confirm ACT rules and inputs → complete representative integrations → run controlled end-to-end ACT tests → resolve defects and confirm ownership/access → train and obtain ACT acceptance → agree any cutover. Dates require current access and acceptance scope.

## Exclusions / guardrails

- No automated building-certification or compliance decision.
- No AI-selected price, unsupervised proposal, or silent client send.
- Government forms in the library are not all auto-populated; signing depends on form-specific fields, parties and approvals.
- No claim of full BCS replacement, complete historical migration, full reporting parity or production readiness until scoped and verified.
- No fabricated savings, timeline, testimonials or security-team claims.
