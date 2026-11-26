---
module: 1
slug: jarvis
title: Jarvis 2.0 and your HUD
short: Upgrade Jarvis and set up your command centre.
time: About 45 minutes
outcome: Jarvis 2.0 is running your agency with you, your goal is set, and your HUD shows everything on one screen.
gate: A Jarvis on Base44, on the Builder plan or higher.
packs: core, hud
missions: 1 to 3
---

This is the foundation. Do it in one sitting, ideally on your onboarding call. After the upgrade, Jarvis leads every step with you.

## Open your Jarvis {1 min}

Jarvis is your Base44 Superagent. If you already have Jarvis from the free course, use that one. It keeps what it knows about you.

1. In Base44, open Superagents.

2. Open your Jarvis. No Jarvis yet? Do the New to Jarvis page first (under Start here).

> see: Your Jarvis chat is open.
> fix: Can't find Superagents? It's in the main Base44 menu. Ask in your Discord channel and we'll point you to it.

## Upgrade to Jarvis 2.0 {5 min}

One file and one message. From here, Jarvis guides you through every step.

[[pack:core]]

1. Download the Jarvis 2.0 file above. Don't unzip it.

2. In the Jarvis chat, click + and attach the file.

3. Paste the message below in the same message and send.

```prompt Send to Jarvis, with the file attached
Hey Jarvis, upgrade me to Jarvis 2.0. Everything you need is in the attached file. Follow its install steps in order, keep what you already know about me, and walk me through anything I need to do.
```

> see: Jarvis replies that it's upgrading you and will walk you through everything.
> fix: If the file sends on its own before your message, just send the message next. Jarvis picks it up.

## Answer Jarvis's questions {2 min}

Jarvis asks only what it needs: your monthly target, sales calls a week, when you want your check-ins, how many leads a day, and your city.

1. Answer all the questions in one reply.

2. If Jarvis asks you to switch on a setting, open Agent Settings, Security, and switch on Update data. Then tell Jarvis it's on.

> see: Jarvis says "You're on Jarvis 2.0", with your goal, your check-ins and the plan ahead.
> fix: Not sure on a target? Pick a number you'd be proud of in 90 days. You can change it later.

## Get your check-ins on your phone {1 min} optional

Every working day Jarvis checks in twice: a morning plan and an afternoon progress check.

1. In Jarvis, open Channels.

2. Click Connect next to WhatsApp or Telegram.

3. Scan the code with your phone and send the activation code.

> see: A message from Jarvis arrives on your phone.
> fix: Prefer not to? Skip this. Check-ins still arrive in your Jarvis chat.

## Save your update link {1 min}

When we improve a skill, Jarvis can check this link and update itself. Your link is personal. Don't share it.

[[updatelink]]

```prompt Send to Jarvis
Save this as my Jarvis 2.0 update link: {{update_link}}
```

> see: Jarvis confirms it saved your update link.
> fix: No link showing above? Refresh this page. Still nothing, press "I'm stuck".

## Ask Jarvis to start your HUD {1 min}

Your HUD (Agency HQ) is where you see your whole agency: what needs you, your pipeline, leads, campaigns and results.

Nothing to attach here. Jarvis already has the HQ skill: it came inside the Jarvis 2.0 file. The HUD app file comes two steps later, and it goes to the Base44 builder, not to Jarvis.

```prompt Send to Jarvis
Let's set up my Agency HQ. Use the jarvis-hq skill and guide me one step at a time: tell me exactly what to click, what to send, and what I should see.
```

> see: Jarvis starts with how to create your app.
> fix: If Jarvis asks you to reply "go", reply go.

## Create your app {2 min}

Base44 doesn't have a blank app button, so you ask its builder for an empty app.

1. In Base44, go to the main page where you build new apps.

2. Paste the message below into the build box and send it.

3. Wait for it to finish. Leave the app open.

```prompt Send to the Base44 build box
Create an empty app named Agency HQ. Only a single blank placeholder page. Do not add features, entities or designs yet. I will install a package next.
```

> see: A new app named Agency HQ with one blank page.
> fix: If the builder adds anything else, that's fine. The package replaces it.

## Install your HUD {12 min}

This puts the full HUD into your new app. Base44 shows a few safety screens on the way. They're normal.

[[pack:hud]]

1. Download the Agency HQ file above. Don't unzip it.

2. In your Agency HQ app's builder chat, click + and attach the file.

3. Paste the install message below in the same message and send.

4. Press Approve on each card Base44 shows (installing packages, copying files, adding screens, testing functions).

5. If the builder pauses and asks to continue, reply continue.

6. A "Set secrets" form appears: press Skip. You add these in your HUD in a minute.

7. When it finishes, screenshot its report and send it to Jarvis.

```prompt Send to the Agency HQ builder, with the file attached
Install the attached Agency HQ v3.16.1 package into this app as the exact source of truth. Unzip it and copy every file under source/ into this project at the same paths, replacing what is there.
Copy in this order: everything under base44/ first, then src/api/, src/lib/, src/hooks/, src/utils/, then src/components/, then src/pages/, then src/index.css, and last src/App.jsx, src/main.jsx and index.html. Restart or reload the dev server after copying.
Make sure every entity in base44/entities/ exists exactly as defined (19 tables). Deploy every backend function in base44/functions/ exactly as written (20 functions), including connections, sendCheck, retellWebhook, which Retell calls from outside without a login because it checks Retell's signature itself, and jarvisVoice. Register the workflow in base44/workflows/ and confirm it is active. Make sure package.json lists three 0.171.0 and retell-client-js-sdk 3.0.3 exactly, and install them.
Never rename or move a file and never change an import path to work around an error. Keep the app's login requirement on. Do not redesign, simplify or recreate any page, component, style, entity, function, shared module or workflow. Run the build and fix only genuine build errors.
Report: every table, every deployed function (send each an empty POST and give the status code; none may be 404), the workflow status, and the build result. Do not publish.
```

> see: The report shows 19 tables and 20 functions, and Jarvis says it looks right.
> fix: If something is missing, Jarvis gives you the exact message to send the builder.

## Publish your HUD {2 min}

Publishing makes your HUD live. Do it twice, so everything loads.

1. Click Publish. When it's done, click Publish again.

2. Open your published app and log in.

> see: Your HUD opens: the ring, your missions and Talk to Jarvis.
> fix: If you only see an error, tell Jarvis. It gives you a one line fix for the builder.

## Connect Jarvis and your HUD {5 min}

Everything connects in one screen: your HUD, Settings, Connections. Every line has a ? that explains it.

1. In Jarvis: Agent Settings, Developer, Create access token. Choose One app or Superagent, pick the one with the Agent badge, and choose Full access. Copy it.

2. In your HUD: Settings, Connections, Jarvis access. Paste it and press Save straight away.

3. On the HUD key line, press Get it for Jarvis, then Copy. Paste it into your Jarvis chat and send.

4. Still in HUD Settings, add your Jarvis agent ID (the 24 characters after /agents/ in Jarvis, Agent Settings, Developer) and your first name. For voice, choose Browser voice.

5. In Jarvis: Agent Settings, General. Check Cross-app data access is set to All apps.

6. Back in Connections, press Test Jarvis connection. Then send the message below.

```prompt Send to Jarvis
Done. Check that my Agency HQ is fully connected, and tell me when everything is ready.
```

> see: Test Jarvis connection says "Jarvis is connected", and Jarvis says your HQ is ready.
> fix: The test tells you exactly what's wrong (the token or the agent ID). Fix that one thing and test again.

## Talk to Jarvis {2 min}

Your first conversation with Jarvis, from your own HUD.

1. Press Talk to Jarvis on your HUD, or tap the triangle in the middle.

2. Or type in the Message Jarvis box under the pipeline.

```prompt Say or type
What's next?
```

> see: Jarvis answers, out loud or under the box.
> fix: Voice not working? Typing in Message Jarvis works the same.

## Put your HUD on your phone {2 min} optional

Open your HUD like an app, straight from your home screen.

1. **iPhone:** open your published HUD in Safari. Tap Share (the square with the arrow), then Add to Home Screen, then Add.

2. **Android:** open your published HUD in Chrome. Tap the three dots menu, then Add to home screen (or Install app), then Add.

3. Open it from the new icon and log in once.

[[image:hud-phone.png|Your HUD on a phone]]

> see: A HUD icon on your home screen that opens straight into your HUD.
> fix: No Add to Home Screen option? On iPhone it only shows in Safari, not in Chrome.

## See what you've built {1 min} optional

This is your HUD once leads, emails and calls start moving: today's mission, who needs you, your pipeline and Talk to Jarvis.

[[image:hud-desktop.png|Your HUD on a computer]]

> see: Yours fills up like this as you work through Modules 2 to 4.
> fix: Yours looks empty? That's normal until your first leads arrive in Module 4.

## Jarvis's live voice (Retell add-on) {5 min} optional

A fast, natural voice for Talk to Jarvis, and Jarvis can phone you. Retell is a separate account that charges by the minute, so check their pricing first.

1. Sign up at dashboard.retellai.com/?ref=blake9a and add a card.

2. In Retell: Settings, API Keys. Copy your key.

3. HUD, Settings, Connections, Live voice: paste it, press Save, then Test key.

4. Press Set up my voice and wait for Done.

5. HUD Settings, Voice: choose Retell voice. Publish your app again.

> see: Jarvis greets you in its voice when you press Talk.
> fix: If you see a warning, keep Browser voice and send Jarvis a screenshot.
