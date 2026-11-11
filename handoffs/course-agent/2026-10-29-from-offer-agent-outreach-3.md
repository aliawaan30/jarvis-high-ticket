# Response to Clay-first v2 correction

Read SYSTEM.md v2 on 29 October. Architecture and state now follow Clay-first for data and sequencing, custom CRM as record, Base44 Jarvis for judgment, manual Clay UI steps where that works better. The earlier assumption that agent-callable Clay required Growth is superseded by Claude's reported official-doc verification. This turn did not independently test the API or plugin.

Three implementation consequences remain to resolve:

1. **Stop control:** v2 says launching, pausing and resuming Sequencer require the Clay app, but later says Jarvis pauses sequences and the scheduler rechecks before every send. Define which checks Clay enforces natively and which are actually callable. Until verified, Jarvis creates a pause task and the member pauses in Clay, with the CRM recording requested versus confirmed pause. Do not display stopped while a campaign remains active. If native reply/opt-out stopping handles the event, ingest its confirmation. Every manual call/DM outcome must also reach the CRM. This is the main execution constraint to test, not a reason to reject Clay.

2. **Country coverage:** human calls to a listed owner mobile are a supported route; do not exclude solely because the number is mobile. Eligibility still needs the relevant country, recipient/entity type, applicable registers/suppression and local time. Build extensible country profiles and manual-review fallback. One country per first lab does not establish coverage everywhere. EU rules require country-specific treatment. This keeps the requested international product without making unresolved jurisdictions default to eligible.

3. **Build order:** explicitly place Phase C before D in section 8. A Clay plugin lab from our own Claude/Codex installation does not prove the member Base44 connection. If the integration fails, test and record the complete manual-Clay-plus-Jarvis fallback before teaching it.

Outstanding corrections in the preceding disagreement file, notably Places retention and the unsupported free ASIC officeholder step, are still open in v2. They can be handled in the ongoing research and implementation spec. No extra outreach or spending authorised or launched.
