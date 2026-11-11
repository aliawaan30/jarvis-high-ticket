# Outreach system: joint build, 29 Oct 2026 (Claude to the offer agent)

Blake, this morning: "I wanna massively build on top of the skill for outreach, that's a huge priority. If we can create a sick process that goes through and finds qualified leads and outreaches. Should these guys be connecting to a platform like clay.com, or how should we truly build this fully out for a dialled outreach system?" He is perfecting other modules while we do this.

## Division of labour
- Claude (me): the external research. Tool landscape with live pricing and APIs (Clay, Apollo, Instantly/Smartlead, Prospeo/FullEnrich/Hunter/Lusha, Google Places, Sales Navigator, AU and US phone data), what each is actually good for at SMB owner level, and compliance (AU Spam Act and DNCR, US TCPA/CAN-SPAM, LinkedIn automation terms, AI voice disclosure). Then one system design document and the Module 3 lessons.
- You: the Jarvis side. Read studio/data/lessons/m3-the-whole-system-on-one-page.json (my six stage draft, already softened per your notes) and your own jarvis-opportunity-finder and jarvis-offer-discovery drafts. Draft the skill architecture for a member's Jarvis to run the system: proposed skills (for example account definition, list build, pain-signal scorer, decision-maker finder, enrichment, multi-channel sequencer, pipeline logger), each with inputs, outputs, the external tool or API it needs, what the member must review by hand, and what cannot be done inside student Jarvis on Base44 (memory: student Jarvis stays Base44; Retell is opt-in advanced). Also a plan for the lab: running the whole thing on our own offer first, what we would measure, and what authorisation is needed before any message is sent.

## Constraints we both hold
No outreach is launched by either of us. Draft and design only. No invented reply rates or results. Where a claim is a hypothesis, say so. No em-dashes in anything member facing.

## Output
Write yours to handoffs/2026-10-29-from-offer-agent-outreach.md. I will merge both into projects/high-ticket-course/outreach/SYSTEM.md and tell you when it exists so you can review it.
