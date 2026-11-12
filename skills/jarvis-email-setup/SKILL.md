---
name: jarvis-email-setup
description: Set up and run cold email the easy way: the member's own Gmail connected to Jarvis, a strict daily cap, the send gate on every email, and an upgrade to Instantly when they want bulk campaigns. Use before any cold email is sent, when the member asks about sending, inboxes, limits or deliverability, or wants to send more emails.
---

# Email setup

Version 2, 4 November 2026. Easiest start: the member's own Gmail, connected to Jarvis in a minute. Volume stays low and quality stays high, which protects their inbox. Instantly is the upgrade for bulk.

## Level 1: their own Gmail (default)
1. Ask the member to say "connect my Gmail" and approve the card. Straight after it connects, always send one test email to the member's own address and ask them to confirm it arrived and which From address it shows. No cold email until they confirm. Connect it to this agent. If a Gmail is already connected at workspace level, check which address sends: send one test email to the member and confirm the From address is the one they want.
2. Daily cap: 10 cold emails a day to start, never more than 15 from this inbox. Replies and follow ups to people who replied do not count toward the cap.
3. Check their sending domain once: if it is their own business domain, look up its public DNS for SPF, DKIM and DMARC and tell them in one line if anything is missing, with the exact record to add. If it is a plain gmail.com address, nothing to set up.
4. Signature: their name, business name and postal address (required for US email), set once on the Campaign row. The postal address is the only thing to ask for; everything else has a default.
5. Only email addresses the business publishes on its own website or listing (email status published), or addresses verified by a verification service (verified). Never a guessed address.
6. Plain text, no images, no attachments, no link in the first email, at most one link later, send in the recipient's working hours.
7. Auto pause: one bounce over 2 percent of the week's sends, or any spam complaint, pauses cold email from this inbox until the cause is found. Tell the member in one line.
8. Replies land in this same inbox, where the reply watch reads them. No other setup.

## The send gate (every email, no exceptions)
Plain code, no AI: a Base44 backend function named send-check inside the member's Agency HQ app. Before any outreach email or reply goes out, call send-check with the email, the account and the campaign settings. Send only if it returns ok true. If it returns reasons, do not send: fix the email or tell the member why. If it cannot be reached, do not send. No check, no send.
It blocks (working hours do not apply to the member's own test address): guessed, risky or invalid addresses for cold email, accounts whose country or entity type forbids email, do not contact, replied or booked accounts, unapproved campaigns, the daily cap, outside the recipient's working hours, a missing opt out line or postal address, unfilled placeholders, banned spam and AI phrases, HTML, any link in email 1, more than one link later, and any link or address on a domain that is not the member's own (only their exact booking page is allowed).
Fields to send: email (to, subject, body, kind cold or reply, step), account (email, emailStatus, emailAllowed, emailAllowedReason, replied, booked, doNotContact), settings (campaignApproved, dailyLimitPerInbox, optOutLine, postalAddress, ourDomains, bookingUrl, doNotContact, sendWindowStart, sendWindowEnd), recipientLocalHour, sentTodayFromInbox.
Work out the recipient's local hour from the exact IANA time zone of the account's city (Phoenix is America/Phoenix, which never changes for summer; Sydney is Australia/Sydney; London is Europe/London). Save the zone on the account. If the city is unknown, use the country's main zone and say so; never guess across zones in countries that have several.
Gate receipt: save the result on the email's Touch as gate result ("ok", the date and the pack version). An email marked sent without a gate result is a broken rule: tell the member and stop the campaign until it is explained.

## Make sure the send gate works (when you build the CRM, and again at mission 9)
1. Backend functions need the member's Base44 Builder plan or higher. If their plan does not include them, tell them in one line which plan does, and hold all sending until it is sorted.
2. If backend functions are off for Agency HQ, ask in one message: "Open Agency HQ, then its Settings, and turn on Backend functions. Tell me when it's on." (Tip for them: Base44's account setting "Default Backend Functions" turns them on for every new app.) If they cannot find it, ask for a screenshot.
3. Add send-check yourself: edit the Agency HQ app and create a backend function named send-check with the code in the appendix "send-check code", exactly as written. The member never copies or pastes code.
4. Test it: one good test email must return ok true, one with "{{first_name}}" in it and a guessed address must return ok false with reasons. Mission 9 is only done when both behave.

## Level 2: Instantly (upgrade for bulk)
Offer it when the member wants more than 15 cold emails a day, or several inboxes. Instantly can sell ready made sending inboxes and handles warm up, so there is no DNS work. Tell them to check current prices; its API needs the Growth plan or above.
1. They create the Instantly account and buy inboxes inside it.
2. Ask for the API key with the secure secret card in this chat, saved as INSTANTLY_API_KEY.
3. Jarvis creates the campaign, runs the send gate on every template and every merged lead, and adds only the leads that pass, with custom variables (first name and the two insights).
4. The Campaign runner reads new replies through Instantly's API each hour and sends them to jarvis-reply-desk.
Cold email moves off their Gmail once Instantly is live.

## Health check (inside Friday numbers)
Sent, bounced, replies, opt outs and complaints per inbox, in one line. Pause and explain if a limit is crossed.

## Never
1. Never go above 15 cold emails a day from the member's own Gmail.
2. Never buy or use a purchased email list.
3. Never send to a country or entity type the country rules block.
4. Never hide who is sending: real name, real business, real postal address, a working way to opt out.

## HQ (Jarvis 2.0)
Read first: Offer, Campaigns, Accounts. Write when done: Campaigns: sending method (Gmail or Instantly), inbox, daily limit, DNS status if checked. After writing, read the rows back and confirm they saved.

---

## Appendix: send-check code
The Agency HQ backend function named send-check. Add it exactly as written. Logic adapted from Harvey (github.com/ethanplusai/harvey), MIT License, Copyright (c) 2026 Ethan Rogers.

```javascript
// Jarvis 2.0 send gate. Plain code, no AI: every outreach email must pass before it is sent.
// Logic ported and extended from Harvey's gate.py (github.com/ethanplusai/harvey),
// Copyright (c) 2026 Ethan Rogers, MIT License. See THIRD-PARTY-NOTICES.md.
//
// Use: put this in the member's funnel app as a backend function at /api/send-check.
// The caller sends JSON { email, account, settings, recipientLocalHour, sentTodayFromInbox }.
// settings: campaignApproved, dailyLimitPerInbox, optOutLine, postalAddress, ourDomains (sending domain,
// agency site, funnel domain), bookingUrl (the member's exact Cal.com page), doNotContact, sendWindowStart/End.
// and gets back { ok, reasons }. Send only when ok is true.

const BANNED_PHRASES = [
  "act now", "buy now", "click here", "click below", "limited time", "limited offer",
  "exclusive deal", "special offer", "risk-free", "no obligation", "100% free",
  "make money", "double your", "guaranteed results", "winner", "congratulations",
  "i hope this finds you well", "hope this email finds you well", "i hope this email finds you",
  "picture this", "what if i told you", "in today's fast-paced world", "game-changer",
  "game changer", "cutting-edge solution", "revolutionize your", "unlock your",
  "supercharge your", "as a language model", "i wanted to reach out", "just circling back",
  "touching base", "i came across your", "quick question for you",
];

const MAX_SUBJECT_LEN = 90;
const MAX_BODY_WORDS = 220;
const EMAIL_RE = /^[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$/;
const MERGE_TAG_RE = /\{\{\s*\w+\s*\}\}|\{\s*\w+\s*\}(?!\})|\[[A-Z][A-Z _]{2,}\]/g;
const URL_RE = /https?:\/\/[^\s<>"')]+/gi;
const BARE_DOMAIN_RE = /(?<![\w@.\/])((?:[a-z0-9-]+\.)+[a-z]{2,24})(?=[\/\s.,;:!?)]|$)/gi;
const HTML_RE = /<\s*(html|body|div|table|img|a|span|p)\b/i;
const SENDABLE_STATUSES = new Set(["verified", "published"]); // never "guess", "risky" or "invalid"

function hostOf(link) {
  try { return new URL(link).hostname.toLowerCase().replace(/^www\./, ""); }
  catch { return ""; }
}
function isOurs(host, allowed) {
  return [...allowed].some((d) => host === d || host.endsWith("." + d));
}

function sendCheck({ email, account, settings, recipientLocalHour, sentTodayFromInbox }) {
  const reasons = [];
  const to = String(email?.to || "").trim().toLowerCase();
  const subject = String(email?.subject || "").trim();
  const body = String(email?.body || "").trim();
  const kind = email?.kind === "reply" ? "reply" : "cold";
  const s = settings || {};
  const a = account || {};

  // Recipient
  if (!EMAIL_RE.test(to)) reasons.push(`invalid recipient address '${to}'`);
  if (a.email && String(a.email).trim().toLowerCase() !== to) reasons.push("recipient does not match the account in HQ");
  const dnc = (s.doNotContact || []).map((x) => String(x).trim().toLowerCase()).filter(Boolean);
  const toDomain = to.split("@")[1] || "";
  const blocked = dnc.find((x) => x === to || (!x.includes("@") && (toDomain === x || toDomain.endsWith("." + x))));
  if (blocked) reasons.push(`'${blocked}' is on the do not contact list`);
  if (a.doNotContact) reasons.push("account is marked do not contact");

  if (kind === "cold") {
    if (a.replied) reasons.push("account has replied: sequence must stop");
    if (a.booked) reasons.push("account has booked: sequence must stop");
    if (a.emailAllowed !== true) reasons.push(`cold email not allowed for this account (${a.emailAllowedReason || "country or entity type rule"})`);
    if (!SENDABLE_STATUSES.has(a.emailStatus)) reasons.push(`email status '${a.emailStatus || "unknown"}' is not sendable (needs verified or published)`);
    if (!s.campaignApproved) reasons.push("campaign is not approved by the member");
    const limit = Number(s.dailyLimitPerInbox || 0);
    if (!(limit > 0)) reasons.push("no daily limit set for this inbox");
    else if (Number(sentTodayFromInbox || 0) >= limit) reasons.push(`daily limit reached (${sentTodayFromInbox} of ${limit})`);
    const start = s.sendWindowStart ?? 8, end = s.sendWindowEnd ?? 17;
    const ownAddress = String(a.emailAllowedReason || "").toLowerCase() === "member's own address";
    if (ownAddress) { /* the member emailing their own test address: working hours do not apply */ }
    else if (typeof recipientLocalHour !== "number") reasons.push("recipient local time unknown");
    else if (recipientLocalHour < start || recipientLocalHour >= end) reasons.push(`outside the recipient's working hours (${recipientLocalHour}:00, window ${start} to ${end})`);
    if (s.postalAddress && !body.includes(String(s.postalAddress).trim())) reasons.push("postal address footer missing");
    if (!s.postalAddress) reasons.push("no postal address set");
    if (!s.optOutLine) reasons.push("no opt out line set in settings");
    else if (!body.includes(String(s.optOutLine).trim())) reasons.push("opt out line missing");
  }

  // Content
  if (!subject && kind === "cold") reasons.push("empty subject");
  if (!body) reasons.push("empty body");
  if (subject.length > MAX_SUBJECT_LEN) reasons.push(`subject too long (${subject.length} > ${MAX_SUBJECT_LEN})`);
  const words = body.split(/\s+/).filter(Boolean).length;
  if (words > MAX_BODY_WORDS) reasons.push(`body too long (${words} words > ${MAX_BODY_WORDS})`);
  const leftover = [...new Set((subject + " " + body).match(MERGE_TAG_RE) || [])];
  if (leftover.length) reasons.push(`unfilled placeholders: ${leftover.slice(0, 3).join(", ")}`);
  const lowered = (subject + " " + body).toLowerCase().replace(/[\u2018\u2019]/g, "'");
  const hits = BANNED_PHRASES.filter((p) => lowered.includes(p));
  if (hits.length) reasons.push(`banned phrases: ${hits.slice(0, 3).join(", ")}`);
  if (HTML_RE.test(body)) reasons.push("HTML in body (plain text only)");

  // Links: count them, and only our own domains are allowed
  const links = body.match(URL_RE) || [];
  const maxLinks = kind === "cold" && email?.step === 1 ? 0 : 1;
  if (links.length > maxLinks) reasons.push(`too many links (${links.length} > ${maxLinks})`);
  const allowed = new Set((s.ourDomains || []).map((d) => String(d).toLowerCase().replace(/^www\./, "")));
  const booking = String(s.bookingUrl || "").trim().toLowerCase().replace(/^https?:\/\/(www\.)?/, "").replace(/\/+$/, "");
  const isBooking = (link) => booking && link.toLowerCase().replace(/^https?:\/\/(www\.)?/, "").startsWith(booking);
  const hosts = new Set(links.filter((l) => !isBooking(l)).map(hostOf).filter(Boolean));
  for (const m of body.replace(URL_RE, " ").matchAll(BARE_DOMAIN_RE)) {
    const h = m[1].toLowerCase().replace(/^www\./, "");
    if (!/\.(png|jpg|jpeg|gif|pdf|txt|js|css)$/.test(h)) hosts.add(h);
  }
  hosts.delete(toDomain);
  const foreign = [...hosts].filter((h) => !isOurs(h, allowed));
  if (foreign.length) reasons.push(`link or address on a domain that is not ours: ${foreign.slice(0, 3).join(", ")}`);

  return { ok: reasons.length === 0, reasons };
}

// Base44 backend function: send-check
// Call with POST JSON { email, account, settings, recipientLocalHour, sentTodayFromInbox }.
// If the app has a secret GATE_TOKEN, callers must send it in the x-gate-token header.
Deno.serve(async (req) => {
  const json = (body, status = 200) => new Response(JSON.stringify(body), { status, headers: { "content-type": "application/json" } });
  const expected = Deno.env.get("GATE_TOKEN");
  if (expected && req.headers.get("x-gate-token") !== expected) return json({ ok: false, reasons: ["unauthorised"] }, 401);
  let input;
  try { input = await req.json(); } catch { return json({ ok: false, reasons: ["bad JSON"] }, 400); }
  try { return json(sendCheck(input)); }
  catch (e) { return json({ ok: false, reasons: ["gate error: " + String(e && e.message || e)] }, 500); }
});
```
