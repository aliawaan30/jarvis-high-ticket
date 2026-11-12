# Agency HQ release notes

## v3.13 (12 Nov 2026)
- Owner messages after a call go out within 3 minutes: the one-time workflow runs right away, or is scheduled 1 to 2 minutes ahead, never with a safety buffer.

## v3.12 (12 Nov 2026)
- The greeting waits for the stage: it plays once the orb has drawn and the transition has settled (about 0.7 s), with bounded waits on slow devices. Retell connects from the tap, behind the transition.

## v3.11
- Instant greeting: prepared in the Jarvis voice when the HUD loads, played from memory on Talk.

## v3.10
- After-call DONE message is required: sent on WhatsApp (Telegram if not connected) through a one-time workflow when no direct tool exists.

## v3.9
- Lead page: the Call button and contact block show the first clean phone number and email; extra numbers and sources move to a small line underneath.

## v3.8
- Faster Retell start (briefing reads in parallel, no wait on the log, Retell library preloaded). Captions and live transcript removed from the voice stage.

## v3.7
- retellWebhook deployed with its shared modules (it had never been deployed, so no call reached the app).

## v3.6
- After-call rules: leads go into the Agency HQ Account table through jarvis-lead-hunter, never the old Lead table; owner messages on WhatsApp first, Telegram second; one DONE message with key numbers. First name sent to Retell. Retell public key setting (no longer used after v3.8).

## v3.5
- Base44 mode: every voice turn carries a live CRM briefing.

## v3.4
- jarvisVoice: Base44 mode speaks in the Jarvis voice through Fish Audio, with the orb following the real audio; browser voice as fallback.

## v3.3
- Shared CRM briefing (crm-context) used by Talk, Call me and get_context: goal, money this month, mission, today's calls, emails and replies, pipeline, hot leads, deals, campaigns, recent activity.

## v3.1 and v3.2
- Retell v3 web calls (/v3/create-web-call, browser SDK 3.0.3); the orb detects Jarvis speaking from audio levels; Retell errors show Retell's own reason (Talk and Call me).

## v3.0
- Cinematic voice mode: the HUD fades, the camera pushes in, the particle orb (JarvisOrb) breathes, follows the mic and swells with Jarvis's voice. Greets by name. Replaces the Talk pop-up.

## v2.4 to v2.11
- Settings rebuilt to the approved design with the AgencySettings table; phone layout; tap to send, instant acknowledgements; Safari-safe speech; Retell error reasons.
