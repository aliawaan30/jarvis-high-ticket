# Agency HQ v3.14 (Jarvis HUD + CRM + cinematic voice): install

Agency HQ is the student's command centre: the Jarvis HUD home, the CRM (Pipeline, Leads, lead page, Campaigns, Clients, Results, Settings) and the cinematic voice mode (Talk to Jarvis). Jarvis 2.0 writes into it; the voice mode reads from it.

## What is in source/

- 18 data tables (base44/entities): Account, AgencySettings, ActivityLog, CallControl, CallReceipt, Campaign, Client, Deal, Lead, Memory, Mission, Profile, SessionLog, TalkTurn, Task, Touch, User, WeekNumbers.
- 19 backend functions (base44/functions): sendCheck (the email send gate), afterCall, callMe, callMeRetell, callStatus, getContext, jarvisVoice, logActivity, logSession, nativeCallHook, remember, retellDiscover, retellWebhook, talkReply, talkSend, talkStart, upsertLead, upsertProfile, upsertTask, plus the shared modules in base44/shared (send-check, after-call-bridge, auto-continue, call-context, crm-context, hud).
- 1 workflow (base44/workflows): "Jarvis after-call execution bridge", calls afterCall every five minutes as a safety net behind the Retell webhook.
- The app (src): HUD, CRM pages, voice stage (VoiceStage.jsx, JarvisOrb.jsx), Settings.
- Packages the app needs: three 0.171.0, retell-client-js-sdk 3.0.3 (exact).

## Install (new app, or an existing Jarvis HUD app)

1. In the Base44 builder chat, attach this zip and send the prompt below in the same message.
2. Check the builder's report: 18 tables, 19 functions deployed (including sendCheck, retellWebhook and jarvisVoice), the workflow registered and active, build passing. Builders sometimes skip a function or a table: do not move on until each is confirmed.
3. Add the secrets (Dashboard, Secrets), then Publish, then Publish again. Secrets do nothing until published.
4. Open the published app, Settings: your Jarvis agent ID, your name, Voice provider.
5. Give your Jarvis agent cross-app access to this app (Agent settings, General).

### The prompt to paste with the zip

```text
Install the attached Agency HQ v3.14 package into this app as the exact source of truth. Unzip it and copy every file under source/ into this project at the same paths, replacing what is there.

Copy in this order: everything under base44/ first, then src/api/, src/lib/, src/hooks/, src/utils/, then src/components/, then src/pages/, then src/index.css, and last src/App.jsx, src/main.jsx and index.html. Restart or reload the dev server after copying.

Make sure every entity in base44/entities/ exists exactly as defined (18 tables). Deploy every backend function in base44/functions/ exactly as written (19 functions), including sendCheck, retellWebhook, which Retell calls from outside without a login because it checks Retell's signature itself, and jarvisVoice. Register the workflow in base44/workflows/ and confirm it is active. Make sure package.json lists three 0.171.0 and retell-client-js-sdk 3.0.3 exactly, and install them.

Never rename or move a file and never change an import path to work around an error. Keep the app's login requirement on. Do not redesign, simplify or recreate any page, component, style, entity, function, shared module or workflow. Run the build and fix only genuine build errors.

Report: every table, every deployed function (send each an empty POST and give the status code; none may be 404), the workflow status, and the build result. Do not publish.
```

## Secrets

| Secret | Needed for | How to get it |
|---|---|---|
| JARVIS_NATIVE_TOKEN | Talk (Base44 mode), after-call handover to Jarvis | Jarvis agent: Agent settings, Developer, Create access token, One app or Superagent, the entry with the Agent badge, Full access |
| HUD_KEY | Retell tools mid-call (add_task, remember, get_context) | Jarvis generates it (32 random hex characters) and hands it over, as in the course install. The same value goes in the Retell tools' x-hud-key header |
| RETELL_API_KEY | Retell voice, Call me, the after-call webhook check | Retell dashboard, API Keys |
| FISH_API_KEY | The Jarvis voice in Base44 mode and the instant greeting | fish.audio, API Keys (separate account from Retell) |

## Voice modes

- Base44 mode (Settings, Voice provider, Base44): the real Jarvis agent answers, with a live CRM briefing on every turn, spoken in the Jarvis voice through Fish Audio (browser voice as fallback). Slower replies, but real actions live.
- Retell mode: a live, fast call in the Jarvis voice. The Retell agent gets the CRM briefing at the start ({{context_summary}}) and can add tasks mid-call; the real work runs after the call through the webhook and the after-call bridge, and the owner gets a WhatsApp (or Telegram) DONE message. Set up the Retell agent with retell-setup.md.
- Both modes: the greeting ("Hey <name>, how can I help you today?") is prepared when the HUD loads and plays as soon as the stage is ready. In Retell, set the agent to let the user speak first, so Jarvis does not greet twice.

## Check it works

1. Talk to Jarvis: the greeting plays within about a second, the orb pulses with it.
2. "Who replied today?" is answered from the CRM.
3. A request such as "find one construction lead in Dallas and WhatsApp me when it's done", then hang up: within about ten minutes the lead is on Pipeline (New lead) and the WhatsApp arrives. If not, check in order: CallReceipt row for the call, a new "This is an unattended run" conversation in the Jarvis chat, the task on the board.

The old screen stays at /classic. Pages show empty states until data arrives; there is no sample data.
