# Test 17: full Jarvis 2.0 run on Base44 (prompt for Claude in Chrome)

Before you start:
1. Have your Retell key ready (you paste it yourself; it never goes through the chat).
2. Put these 5 files in your Downloads folder (from course/downloads/jarvis-2 in GitHub): jarvis-skills-module-1-core.zip, jarvis-skills-module-2-offer.zip, jarvis-skills-module-3-funnel.zip, jarvis-skills-module-4-outreach.zip, agency-hq-v3.16.1.zip.
3. Open Base44 in Chrome, signed in. Note your credit balance.
4. Replace the 2 brackets in the prompt: your test inbox and your first name.
5. Paste everything inside the box below into Claude in Chrome.

```text
You are testing Jarvis 2.0, a Base44 Superagent product, the way a non-technical student would use it. Work in my signed-in Chrome tabs on base44.com. Be thorough and honest: I need real results, not a summary that sounds good.

SAFETY RULES
1. Only create and touch two things: a Superagent named "Jarvis Test 17" and an app named "Agency HQ Test 17". Never open, change or delete any other agent or app.
2. Never send an email to anyone except [test inbox]. Never buy anything, add a card, or buy a phone number. Stop and ask me if any page asks for payment.
3. Never paste a key, token or password into a chat, except the HUD key handover in step 9.
4. Uploads, sign-ins and keys: you cannot use my computer's file picker, sign in for me, or handle my Retell key. When a step needs a file attached, a sign-in or a key, PAUSE, tell me exactly which file goes where (it is in my Downloads folder), wait for me to say "done", then continue.
5. If a step fails, take a screenshot, copy the exact error text, try once more, then move on. Do not invent workarounds that change the product.

TEST ANSWERS (use these whenever Jarvis asks)
Name: [first name]. Country: United States. Niche: residential roofers in Dallas. Service: follow up on unsold estimates. Monthly target: $10,000 by 1 March 2027. Sales calls a week: 3. Morning brief: 8am, Monday to Friday. Leads a day: 5. Hours a week: 10. Guarantee: work free until the result. Business size: $100k a month or more. Postal address: 500 Congress Ave, Austin TX 78701.

FOR EVERY STEP RECORD
Status (PASS, PARTIAL or FAIL), time taken, credits used (read the Base44 credit balance before and after if it is visible), exact error text, a screenshot on anything not PASS, and a user-friendliness score from 1 to 5 with one line on where a non-technical student would get stuck or confused.

THE STEPS

1. Create the Superagent. In Base44, create a new Superagent named "Jarvis Test 17". PASS: it exists and its chat opens.

2. Install Jarvis 2.0. PAUSE for me to attach jarvis-skills-module-1-core.zip to the Jarvis Test 17 chat. Then send: "Hey Jarvis, upgrade me to Jarvis 2.0. Everything you need is in the attached file. Follow its install steps in order, keep what you already know about me, and walk me through anything I need to do." Answer its questions with the test answers. PASS: it says "You're on Jarvis 2.0" (or similar) and names a first mission. Record every question it asked and how many messages the install took.

3. The setting. If Jarvis asks, open its settings, Security, and switch on Update data. PASS: Jarvis confirms it.

4. Create the app. Create a new empty Base44 app named "Agency HQ Test 17". PASS: the app exists and its builder chat is open.

5. Install Agency HQ. PAUSE for me to attach agency-hq-v3.16.1.zip to the Agency HQ Test 17 builder chat. Then paste this as the message:
"Install the attached Agency HQ v3.16.1.1 package into this app as the exact source of truth. Unzip it and copy every file under source/ into this project at the same paths, replacing what is there. Copy in this order: everything under base44/ first, then src/api/, src/lib/, src/hooks/, src/utils/, then src/components/, then src/pages/, then src/index.css, and last src/App.jsx, src/main.jsx and index.html. Restart or reload the dev server after copying. Make sure every entity in base44/entities/ exists exactly as defined (19 tables). Deploy every backend function in base44/functions/ exactly as written (20 functions), including connections, sendCheck, retellWebhook, which Retell calls from outside without a login because it checks Retell's signature itself, and jarvisVoice. Register the workflow in base44/workflows/ and confirm it is active. Make sure package.json lists three 0.171.0 and retell-client-js-sdk 3.0.3 exactly, and install them. Never rename or move a file and never change an import path to work around an error. Keep the app's login requirement on. Do not redesign, simplify or recreate any page, component, style, entity, function, shared module or workflow. Run the build and fix only genuine build errors. Report: every table, every deployed function (send each an empty POST and give the status code; none may be 404), the workflow status, and the build result. Do not publish."
PASS: the builder reports 19 tables, 20 functions with none returning 404 (connections included), the workflow active, and the build passing. List any table or function missing.

6. Publish twice. Publish the app, wait for it to finish, publish again. PASS: the published app opens and shows the HUD.

7. The HUD, visual check. On the published HUD home, screenshot it and confirm each: the four role labels around the ring (Scout, Writer, Closer, Ops), the J.A.R.V.I.S. title and status line, a cyan "Talk to Jarvis" button with a microphone, the "Next check-in" pill, the pipeline strip, the "Message Jarvis" box, the live feed. Also check the nav: HUD, Pipeline, Leads, Campaigns, Clients, Results, Settings all open without errors.

8. Jarvis access token. In Jarvis Test 17: settings, Developer, Create access token, choose One app or Superagent, the entry with the Agent badge, Full access. Then in the HUD: Settings, Connections, Jarvis access: paste it and Save. PASS: the line shows "Connected, ends ...". Also open the ? on that line and say whether its help text was enough to do this without help.

9. HUD key. In Connections, press "Copy for Jarvis", paste the copied text into the Jarvis Test 17 chat and send. PASS: Connections shows the HUD key as connected and Jarvis confirms it saved it as a secret.

10. Connect them. In HUD Settings add Jarvis Test 17's agent ID and the name. Leave voice on Browser voice. In Jarvis Test 17: settings, General, give it access to Agency HQ Test 17. Then tell Jarvis: "Done. Check my Agency HQ and tell me it's ready." PASS: Jarvis runs its check and says the HQ is ready, naming the app.

11. Message Jarvis on the HUD. Type "What's next?" in Message Jarvis and press Send. PASS: "Jarvis is on it" appears, then a real reply under the box. Record how many seconds it took.

12. Talk to Jarvis. Press the Talk to Jarvis button, then close it. Then click the triangle core. PASS: both open the live call screen with the orb. You cannot judge audio; just confirm it opens and closes cleanly.

13. Retell voice (the paid add-on). Do NOT ask for the Retell key in chat and never type it yourself. PAUSE and ask me to paste my Retell key into HUD Settings, Connections, Live voice (Retell add-on) and press Save. When I say done: press Test key (PASS: "Retell accepted the key"), then press Set up my voice and wait up to 60 seconds (PASS: "Done. Your Jarvis voice is built and published", copy any warning word for word). Then in Settings, Voice, choose Retell voice, and publish the app again. Press Talk to Jarvis: PASS if the live call screen opens and connects. You cannot hear audio, so PAUSE and ask me whether Jarvis greeted me in the Retell voice and record my answer. Do not buy or bind a phone number; skip Call me.

14. Skill missing on purpose. In the Jarvis chat send: "Use the proposal builder skill to write the proposal for Lone Star Roofing." Module 6 is not installed and there is no deal. PASS: Jarvis explains clearly what is missing and what to do, without inventing a proposal. Quote its answer.

15. Offer. PAUSE for me to attach jarvis-skills-module-2-offer.zip to the Jarvis chat. Send: "Install Module 2, The Irresistible Offer, from the attached file. Add every skill inside, replace any older versions, and don't run anything yet. When you're done, show me what you installed and where we start." Then send: "Use the offer creation skill to write my offer. Ask me only what you need, then show me the six lines so I can approve them." Answer with the test answers, then send "Approved." PASS: it asked about guarantee, hours and business size, showed a six line offer ending with "Approve it, or tell me what to change", and the approved offer is saved. Paste the six lines.

16. Outreach skills and lead hunt. PAUSE for me to attach jarvis-skills-module-4-outreach.zip. Send: "Install Module 4, Outreach, from the attached file. Add every skill inside, replace any older versions, and don't run anything yet. When you're done, show me what you installed and where we start." Then send: "Use the lead hunter skill to find me 5 residential roofers in Dallas." PASS: 5 real businesses appear in the HUD pipeline, each with scores, a reason to contact and a source link. Open 2 of the source links and confirm they are real and match. Record time and credits.

17. Email. Send: "Use the email setup skill to connect my Gmail. Walk me through it, send me a test email, and tell me anything else you need from me." PAUSE for me to approve the Gmail connection. Then let Jarvis send its test email to me, and give it the postal address. Then send: "Use the outreach coordinator skill to write first emails for my best leads. Show me every draft in full so I can approve, edit or skip each one." Approve ONE draft and have it sent only to [test inbox]. PASS: the test email arrived, the approved email arrived at [test inbox] with an opt out line and the postal address, and nothing went to any real business.

18. Check-in. Send: "Show me what my afternoon check-in would say today." PASS: three parts (since last time, one next task, where I stand against today's target), under about 80 words, and it mentions where check-ins will be sent (WhatsApp, Telegram or this chat).

19. Where am I. Send: "Where am I?" PASS: it names the step, the mission, what is done and one next action.

20. HUD after work. Reload the HUD home and screenshot. PASS: the pipeline shows the new leads, the live feed shows Jarvis's work with role labels, and the mission bar moved.

21. Funnel: install and set up. PAUSE for me to attach jarvis-skills-module-3-funnel.zip to the Jarvis chat. Send: "Install Module 3, Funnels, from the attached file. Add every skill inside, replace any older versions, and don't run anything yet. When you're done, show me what you installed and where we start." PASS: Jarvis lists 4 skills with versions and the first step. Then follow Jarvis: it should guide creating an empty Funnel app (with the exact message for the Base44 build box) and adding it to Cross-app data access next to the Agency HQ. Record whether Jarvis explained this clearly on its own.

22. Calendar. Follow Jarvis to connect my Google Calendar (PAUSE for me to approve the sign-in) and create a booking page for a 30 minute call. PASS: a booking link exists. Record every step a student would find hard.

23. Landing page. Send: "Use the landing page skill to build my landing page from my approved offer. Show me the colour palettes first, and use my booking page for calls." Pick the second palette. PASS: a published page with my offer, a short application with the monthly revenue question and the unticked SMS consent box, a privacy page, and the booking step. Screenshot the page on a desktop size and on a phone size (narrow the window to about 390 pixels).

24. Application lands in the HUD. Fill in the application on the published page with test details (name Test Lead, my test inbox) and complete a booking for any free slot. PASS: within a few minutes a new lead appears in my Agency HQ pipeline with where it came from, and Jarvis tells me about it. Then cancel the test booking in my calendar.

THE REPORT (write it at the end)
1. A table: step number, step name, status, time, credits, friendliness score, one line note.
2. Every PARTIAL and FAIL in detail: what you did, what you expected, what happened, the exact error text, the screenshot.
3. Totals: steps passed, partial and failed; total time; total credits used.
4. User friendliness: the 5 moments a non-technical student is most likely to get stuck, in order of how bad they are.
5. The 5 fixes you would make first, most important first.
6. THE ONBOARDING SEQUENCE. A numbered list of every action, in the exact order it happened, written so it can be copied straight into a student onboarding guide. For each action give: where it happens (Jarvis chat, Base44 builder chat, HUD page and section, Jarvis settings page, Retell website), who does it (student or Jarvis), which file is attached if any (exact file name), the exact message sent if any (word for word), the exact buttons clicked in order, what the student sees when it worked, and how long it took. Group the actions under these headings: Set up Jarvis, Set up Agency HQ, Connect them, Retell voice, Offer, Leads, Email, Funnel, Daily use. Mark any action that needed my help (an upload, a sign-in, a key) so it can become a clear instruction for the student.
Do not round PARTIAL up to PASS.
```
