# Retell setup for Jarvis voice (Agency HQ)

For Jarvis. The member has a Retell account and wants the real-time Jarvis voice in their Agency HQ app (the HUD). Follow this file exactly. It is the free course's proven Retell build.

Before you start:
1. The member adds these secrets in their Agency HQ app (Dashboard, Secrets), then publishes twice: RETELL_API_KEY (from the Retell dashboard, Settings, API Keys) and HUD_KEY (any long random password they keep; Retell needs it to reach the app from outside). Never ask them to paste either into a chat. If you need the Retell key yourself, ask for it with the secure secret card.
2. "Their own HUD app" below means their Agency HQ app. Its function addresses are its published address plus /functions/<name>.
3. A Retell phone number is only needed for "Call me" (Jarvis phoning them). Live voice in Talk works without a number. If they have no number yet, skip binding the number in step 5 and say so.
4. After you finish, tell them to open Settings in the app, choose Retell under Voice provider (the app finds the agent and number by itself), add their mobile number for Call me, and publish again.

# RETELL BUILD

Only run this if the owner asked for the JARVIS voice and has a Retell account,
a card and a phone number already. You cannot buy the number for them.

If they do not have an account yet, send them to https://dashboard.retellai.com/?ref=blake9a
to sign up. Always use that link, it is the course's own.

The `RETELL_API_KEY` secret must be in the HUD app and the app published since
it was added. Authenticate every call as `Authorization: Bearer <key>` against
`https://api.retellai.com`.

Never print the key. Never ask the owner to paste it into a chat.

## What this agent is

It is not you. It is a small separate voice agent whose only job is to talk on
the phone. It has no memory, no knowledge base and does not do the work. It
takes the instruction, the transcript comes back to you, and you do the work.
Do not try to give it your brain.

## 1. Import the voice

Blake's Jarvis voice is a public Fish Audio community model. Retell hosts Fish
itself, so no Fish account, key or payment is needed.

```
POST /add-community-voice
{"voice_provider":"fish_audio","provider_voice_id":"612b878b113047d9a770c069c8b4fdfe","voice_name":"Jarvis"}
```

It returns the owner's own `voice_id`. Blake's own id is specific to his account
and will not work in theirs.

Before importing, check `list-voices` for one already named `Jarvis` and reuse
it. Dedupe on `voice_name`, not on `provider_voice_id`: `list-voices` no longer
returns that field, and matching on it imports the voice twice.

## 2. Create the LLM

- `model` claude-4.5-haiku
- `model_temperature` 0.3
- No begin message: the user speaks first (`start_speaker` user, or the dashboard's "User speaks first"). The Agency HQ app plays the greeting itself the moment the voice stage opens, so a Retell greeting would say hello twice.
- `default_dynamic_variables` `{"context_summary":"unavailable"}`
- `general_prompt` exactly the text in "The prompt" below.

## 3. The tools

Four tools. The first three are `type: custom`, `method: POST`, pointed at the
owner's own HUD app.

| Tool | Endpoint on their app |
|---|---|
| `add_task` | `/functions/upsertTask` |
| `remember` | `/functions/remember` |
| `get_context` | `/functions/getContext` |
| `end_call` | `type: end_call` |

On all three custom tools:

- **`args_at_root` must be `true`.** Without it Retell wraps the payload and
  every call returns 400. This cost a full day once already.
- `timeout_ms` 8000
- `headers` `{"x-hud-key": <their HUD_KEY>, "Content-Type": "application/json"}`
- `speak_during_execution` true on `add_task` and `remember`, with
  `execution_message_description` `"One sec."`

This is the one place the HUD key is genuinely needed, because Retell calls the
HUD from outside Base44. Read it from the app's secrets; never ask the owner for
it.

## 4. Create the agent

- `voice_id` the id returned in step 1
- `voice_model` s2.1-pro
- `voice_temperature` 0.6
- `voice_speed` 1
- `fallback_voice_ids` `["11labs-Anthony"]`
- `language` their locale, `en-AU` for Australia
- `responsiveness` 1
- `interruption_sensitivity` 0.8
- `enable_backchannel` true
- `max_call_duration_ms` 3600000
- `allow_user_dtmf` true
- `post_call_analysis_model` gpt-5.6-terra
- `webhook_url` their own app's `/functions/retellWebhook`, **no query string**.
  Unlike the optional instant hook, this one carries no key: Retell proves
  itself by signature, or by an authenticated lookup using their API key.

No ambient sound. No boosted keywords.

## 5. Publish, then bind the number

Publish the agent. Then bind their number to the **published** version.

If the number is bound to a draft, calls connect and sound perfect and nothing
ever reaches the dashboard. It is the single hardest failure to diagnose here,
so check it rather than assuming.

## 6. Write it back and report

Save `retell_agent_id` and `retell_from_number` to the Profile through
`upsertProfile`, replacing whatever is there. A student who already built a
receptionist agent for clients will have the wrong one auto-selected; replacing
it is the fix.

Then tell the owner: the agent id, the voice, the webhook you set, that it is
published, and which number you bound.

## Never

- Never create more than one Jarvis agent.
- Never touch any other Retell agent they own, especially a receptionist.
- Never print or repeat the API key or the HUD key.
- Never tell them to pick their own voice. The Jarvis voice is the entire reason
  this option exists.

## What is proven, and what is not

`create-retell-llm`, `create-agent`, `publish-agent`, `delete-agent` and
`delete-retell-llm` were all run against the live Retell API on 30 September
2026 and all returned successfully. `update-agent`, `update-phone-number`,
`create-phone-call`, `get-agent`, `get-retell-llm` and `list-voices` were
already proven before that. So the whole path in this file is real, not assumed.

One honest limit. The create calls were proven with a **minimal body**, not with
the full config in this file in a single request. These fields were sent

## The prompt (use exactly)

```
Live briefing from the owner's Agency HQ CRM (use it for any question about leads, replies, calls due, deals, missions or the goal, and never invent CRM facts that aren't in it): {{context_summary}}

HOW WORK GETS DONE: You are the voice of Jarvis. During the call you talk, answer from the live CRM briefing, and capture requests. The owner's full Jarvis does all real work automatically right after this call ends, from the call transcript, with every skill he has: finding leads, building offers, writing emails, research, call cards, CRM updates, proposals and more.

So for ANY request you can't answer right now from the briefing:
1. Never say you can't do it.
2. Confirm it in one short sentence with the key details (what, how many, where, by when). Ask one quick question only if something essential is missing.
3. Call add_task with a clear title and all the details.
4. Then say: "Got it. I'll start on that as soon as we hang up and message you when it's done."
5. Carry on with the conversation.

Only decline things that are truly unsafe or not allowed, like contacting a lead or client on the owner's behalf during this call. Never claim work is already finished.

HOW YOU SPEAK: You are Jarvis, the owner's AI agency partner. Keep every reply short and natural, one to three spoken sentences. One question at a time. Plain words, no lists or markdown. Use the owner's first name now and then. When the owner says goodbye or that's all, say a short goodbye and end the call with end_call.
```

## Required, learned the hard way (12 Nov 2026)

1. `webhook_url` on the agent must be the owner's app `/functions/retellWebhook`, no query string. Without it no call ever reaches the app and nothing happens after the call. Check that retellWebhook is deployed in the app: an empty POST must return 401 invalid_signature, never 404.
2. The three custom tools must exist (add_task, remember, get_context) with `args_at_root` true and header `x-hud-key` set to the app's HUD_KEY. If the platform will not let you send the key, give the owner the exact paste steps for each tool's Headers.
3. Published versions are locked: to change anything, create a new version, edit it, then publish it (current route: publish-agent-version).
4. Web calls use `POST /v3/create-web-call`; v2 is retired. The app's browser SDK is retell-client-js-sdk 3.0.3.
5. The app's Profile must hold the agent id in `retell_agent_id`, or the webhook ignores the call.
6. After setup, place one test call with a small request and confirm, in order: a CallReceipt row, a new unattended Jarvis conversation, the result in Agency HQ, and the owner's WhatsApp or Telegram DONE message.
