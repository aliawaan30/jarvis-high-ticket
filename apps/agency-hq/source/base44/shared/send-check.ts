// Jarvis 2.0 send gate. Plain code, no AI: every outreach email must pass before it is sent.
// Logic ported and extended from Harvey's gate.py (github.com/ethanplusai/harvey),
// Copyright (c) 2026 Ethan Rogers, MIT License. See THIRD-PARTY-NOTICES.md.
//
// Input { email, account, settings, recipientLocalHour, sentTodayFromInbox }, output { ok, reasons }.
// Send only when ok is true.
// email: to, subject, body, kind ("cold" or "reply"), step (1, 2, 3 or "email 1"...)
// account: email, emailStatus, emailAllowed, emailAllowedReason, replied, booked, doNotContact, website
// settings: campaignApproved, dailyLimitPerInbox, optOutLine, postalAddress, ourDomains, bookingUrl,
//           doNotContact (list), sendWindowStart, sendWindowEnd

const BANNED_PHRASES = [
  "act now", "buy now", "click here", "click below", "limited time offer", "limited offer",
  "exclusive deal", "special offer", "risk-free", "no obligation", "100% free",
  "make money", "double your", "guaranteed results",
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
const SENDABLE_STATUSES = new Set(["verified", "published"]);

// The app stores yes/no as text. Accept true, "yes", "true", "y", "1".
export function yes(v: unknown): boolean {
  if (v === true || v === 1) return true;
  const s = String(v ?? "").trim().toLowerCase();
  return s === "yes" || s === "true" || s === "y" || s === "1";
}
// Compare text ignoring case, line breaks and repeated spaces.
function norm(s: unknown): string {
  return String(s ?? "").toLowerCase().replace(/[\u2018\u2019]/g, "'").replace(/\s+/g, " ").trim();
}
function hostOf(link: string): string {
  try { return new URL(/^https?:\/\//i.test(link) ? link : "https://" + link).hostname.toLowerCase().replace(/^www\./, ""); }
  catch { return ""; }
}
function isOurs(host: string, allowed: Set<string>): boolean {
  return [...allowed].some((d) => host === d || host.endsWith("." + d));
}
function stepNumber(step: unknown): number | null {
  const m = String(step ?? "").match(/\d+/);
  return m ? Number(m[0]) : null;
}

export function sendCheck(input: any): { ok: boolean; reasons: string[] } {
  const { email, account, settings, recipientLocalHour, sentTodayFromInbox } = input || {};
  const reasons: string[] = [];
  const to = String(email?.to || "").trim().toLowerCase();
  const subject = String(email?.subject || "").trim();
  const body = String(email?.body || "").trim();
  const kind = email?.kind === "reply" ? "reply" : "cold";
  const s = settings || {};
  const a = account || {};
  const bodyN = norm(body);

  // Recipient
  if (!EMAIL_RE.test(to)) reasons.push(`invalid recipient address '${to}'`);
  if (a.email && String(a.email).trim().toLowerCase() !== to) reasons.push("recipient does not match the account in HQ");
  const dncList = Array.isArray(s.doNotContact) ? s.doNotContact : String(s.doNotContact || "").split(/[\n,;]+/);
  const dnc = dncList.map((x: any) => String(x).trim().toLowerCase()).filter(Boolean);
  const toDomain = to.split("@")[1] || "";
  const blocked = dnc.find((x: string) => x === to || (!x.includes("@") && (toDomain === x || toDomain.endsWith("." + x))));
  if (blocked) reasons.push(`'${blocked}' is on the do not contact list`);
  if (yes(a.doNotContact)) reasons.push("account is marked do not contact");

  if (kind === "cold") {
    if (yes(a.replied)) reasons.push("account has replied: sequence must stop");
    if (yes(a.booked)) reasons.push("account has booked: sequence must stop");
    if (!yes(a.emailAllowed)) reasons.push(`cold email not allowed for this account (${a.emailAllowedReason || "country or entity type rule"})`);
    if (!SENDABLE_STATUSES.has(String(a.emailStatus || "").toLowerCase())) reasons.push(`email status '${a.emailStatus || "unknown"}' is not sendable (needs verified or published)`);
    if (!yes(s.campaignApproved)) reasons.push("campaign is not approved by the member");
    const limit = Number(s.dailyLimitPerInbox || 0);
    if (!(limit > 0)) reasons.push("no daily limit set for this inbox");
    else if (Number(sentTodayFromInbox || 0) >= limit) reasons.push(`daily limit reached (${sentTodayFromInbox} of ${limit})`);
    const start = Number(s.sendWindowStart ?? 8), end = Number(s.sendWindowEnd ?? 17);
    const ownAddress = norm(a.emailAllowedReason) === "member's own address";
    const hour = Number(recipientLocalHour);
    if (ownAddress) { /* the member emailing their own test address: working hours do not apply */ }
    else if (recipientLocalHour === undefined || recipientLocalHour === null || recipientLocalHour === "" || Number.isNaN(hour)) reasons.push("recipient local time unknown");
    else if (hour < start || hour >= end) reasons.push(`outside the recipient's working hours (${hour}:00, window ${start} to ${end})`);
    if (!s.postalAddress) reasons.push("no postal address set");
    else if (!bodyN.includes(norm(s.postalAddress))) reasons.push("postal address footer missing");
    if (!s.optOutLine) reasons.push("no opt out line set in settings");
    else if (!bodyN.includes(norm(s.optOutLine))) reasons.push("opt out line missing");
  }

  // Content
  if (!subject && kind === "cold") reasons.push("empty subject");
  if (!body) reasons.push("empty body");
  if (subject.length > MAX_SUBJECT_LEN) reasons.push(`subject too long (${subject.length} > ${MAX_SUBJECT_LEN})`);
  const words = body.split(/\s+/).filter(Boolean).length;
  if (words > MAX_BODY_WORDS) reasons.push(`body too long (${words} words > ${MAX_BODY_WORDS})`);
  const leftover = [...new Set((subject + " " + body).match(MERGE_TAG_RE) || [])];
  if (leftover.length) reasons.push(`unfilled placeholders: ${leftover.slice(0, 3).join(", ")}`);
  const lowered = norm(subject + " " + body);
  const hits = BANNED_PHRASES.filter((p) => lowered.includes(p));
  if (hits.length) reasons.push(`banned phrases: ${hits.slice(0, 3).join(", ")}`);
  if (HTML_RE.test(body)) reasons.push("HTML in body (plain text only)");

  // Links: count them, and only our own domains (and the lead's own website) are allowed
  const links = body.match(URL_RE) || [];
  const maxLinks = kind === "cold" && stepNumber(email?.step) === 1 ? 0 : 1;
  if (links.length > maxLinks) reasons.push(`too many links (${links.length} > ${maxLinks})`);
  const allowed = new Set<string>((s.ourDomains || []).map((d: any) => String(d).toLowerCase().replace(/^https?:\/\//, "").replace(/^www\./, "").replace(/\/.*$/, "")));
  const leadSite = a.website ? hostOf(String(a.website)) : "";
  const booking = String(s.bookingUrl || "").trim().toLowerCase().replace(/^https?:\/\/(www\.)?/, "").replace(/\/+$/, "");
  const isBooking = (link: string) => !!booking && link.toLowerCase().replace(/^https?:\/\/(www\.)?/, "").startsWith(booking);
  const hosts = new Set(links.filter((l) => !isBooking(l)).map(hostOf).filter(Boolean));
  for (const m of body.replace(URL_RE, " ").matchAll(BARE_DOMAIN_RE)) {
    const h = m[1].toLowerCase().replace(/^www\./, "");
    if (!/\.(png|jpg|jpeg|gif|pdf|txt|js|css)$/.test(h)) hosts.add(h);
  }
  hosts.delete(toDomain);
  if (leadSite) hosts.delete(leadSite);
  const foreign = [...hosts].filter((h) => !isOurs(h, allowed));
  if (foreign.length) reasons.push(`link or address on a domain that is not ours: ${foreign.slice(0, 3).join(", ")}`);

  return { ok: reasons.length === 0, reasons };
}
