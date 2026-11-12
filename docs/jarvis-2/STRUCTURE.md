# Jarvis 2.0 pack structure

core/ is Jarvis 2.0 itself: the brain (decides), HQ (stores everything), the rhythm (works without being asked) and missions (the path to the first client). It is always installed and always in charge.

modules/ holds the specialist skills, one folder per course module. Each skill is one SKILL.md. Every module skill reads from HQ and writes its results back into HQ. None keeps its own records.

| Folder | Skills |
|---|---|
| core | jarvis-2-brain, jarvis-hq, jarvis-rhythm, jarvis-missions |
| modules/module-2-offer | offer menu, offer discovery, opportunity finder, custom opportunity finder, ad library offer research, offer creation |
| modules/module-3-funnel | landing page, confirmation page, VSL writer, pre-call follow up (owned by Blake) |
| modules/module-4-outreach | lead hunter, outreach coordinator, email setup, call card, reply desk, SMS |
| modules/module-5-ads | ad scripting, static ad creator, Meta campaign setup |
| modules/module-6-sales | call to close playbook, solution design, proposal builder |
| modules/module-7-delivery | scoping agent |

Where a skill sits is provisional. Moving one between folders changes nothing in how it works.
