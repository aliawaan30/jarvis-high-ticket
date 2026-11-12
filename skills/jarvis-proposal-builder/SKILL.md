---
name: jarvis-proposal-builder
description: Write a one page client proposal after a sales call, in one fixed premium design. Use when the student says "write the proposal for [business]" or asks for a proposal, quote or pricing document for a prospect. Reads the deal from Agency HQ, suggests a price from the course method, renders the page and saves it back to Agency HQ.
---

# Proposal builder

Version: 2026-11-11.1

Student prompt: **"Write the proposal for [business]."**

## Before you start

1. Agency HQ must exist and you must have its app ID saved. If not, stop and say: "I need Agency HQ set up first. Install the Agency HQ skill and say 'set up my CRM'."
2. Find the deal for this business in Agency HQ. If there is none, ask the student for the business name and create nothing until they confirm.
3. Check the tables' fields before you write anything. Write only to Agency HQ, never to another app.

## Step 1: pick the mode

1. **Quick mode.** The student sells a fixed offer (for example an AI receptionist) and the deal has no solution design. Build from the approved offer in the Offer table. This must be fast enough to use live on call one.
2. **Custom mode.** The deal has a call brief and a solution design. Build from those.

Tell the student which mode you picked in one line.

## Step 2: gather the facts

Read from Agency HQ: the call brief, the solution design (custom mode), the approved offer, the student's brand (logo, main colour) and business details (name, city, email, phone).

You need all of these. Never invent any of them:

1. The client's business name and contact name.
2. One or two problems, each with a number the owner gave on the call.
3. The yearly cost of the problem the owner agreed to out loud, and how it was worked out. If there is no agreed number, leave the cost graphic out.
4. What gets built: two to four parts, each tied to a problem.
5. Timeline stages and what the client must provide.
6. Price, currency, payment terms, monthly running costs, support.

Ask for everything missing in **one** message, as a short numbered list. Then wait.

Use the client's local currency. Keep time freed up separate from cash saved. Never add benefits that overlap.

## Step 3: suggest the price (student approves)

Skip this if the student already gave a price.

1. Suggest a build price of 5 to 10 percent of the agreed yearly problem cost. Show the range and your suggestion.
2. Check it against the build cost in the solution design. If 5 percent does not cover the build cost with margin, say so plainly: the problem is too small or the build is too big.
3. Show the monthly running costs separately.
4. Ask: "Use [price], or tell me the number you want." Do not render until they approve.

## Step 4: write the content

Plain words a business owner uses. No AI jargon, slogans, agency history or hype. No em or en dashes. Stay inside these limits or the page will not fit:

1. Title: up to 8 words, names the system, not the agency.
2. Overview: up to 60 words. The problem in their words, what we will build, the result.
3. Problems: 1 or 2. Each has a number, a short unit and up to 25 words.
4. Calculation: up to 70 words, using only the owner's figures, ending with when they gave them.
5. Build parts: 2 to 4, each up to 25 words. Then what it connects to, what people still decide, and what is not included.
6. Timeline: 2 to 4 stages, each up to 12 words, plus what we need from the client.
7. Next step: up to 35 words. Sign the agreement, pay the deposit, book the kickoff.

No proof section, no guarantee box, no demo link, no accept button. The proposal is one page.

## Step 5: render it

1. Write the content to `proposal.json` in the same shape as `assets/example-proposal.json`.
2. Run `python3 assets/render_proposal.py proposal.json proposal-[business].html`.
3. If it prints "NOT RENDERED", fix each listed problem and run it again. Never edit the HTML by hand and never change the design.
4. Show the student the page and ask: "Anything to change before you send it?"

## Step 6: save and follow up

1. Save to the Proposals table: deal, version, price, currency, date, status "draft", and the file.
2. Put the link on the deal's proposal_link.
3. Only when the student says they have sent it: set the status to "sent", move the deal to "proposal sent", and add a due item in 2 days: "Follow up [business] on the proposal."
4. If they change anything later, save it as a new version. Keep the old one.

## Step 7: presenter notes

Give the student the call two notes from `references/presenter-notes.md`, filled with this client's words and numbers. These are private. They never go in the proposal.

## Rules

1. Every number comes from the owner or the student. If you calculated it, show how.
2. Nothing marked proposed goes to the client until the student approves it.
3. Never send the proposal yourself.
4. If the deal or offer changes, the proposal is out of date. Say so and offer a new version.
