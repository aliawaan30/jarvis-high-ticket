const S = { campaignApproved: "yes", dailyLimitPerInbox: 10, optOutLine: "Not for you? Reply stop and I won't email again.",
  postalAddress: "Ridgeline AI, 500 Congress Ave, Austin TX 78701", ourDomains: ["ridgeline.ai"],
  bookingUrl: "https://ridgeline.ai/book", doNotContact: ["spam@blocked.com", "nope.com"], sendWindowStart: 8, sendWindowEnd: 17 };
const A = (o = {}) => ({ email: "dave@coastlineplumbing.com", emailStatus: "verified", emailAllowed: "yes", replied: "no", booked: "no", doNotContact: "no", website: "https://coastlineplumbing.com", ...o });
const foot = "\n\nNot for you? Reply stop and I won't email again.\nRidgeline AI, 500 Congress Ave, Austin TX 78701";
const E = (body, o = {}) => ({ to: "dave@coastlineplumbing.com", subject: "Your after hours calls", body: body + foot, kind: "cold", step: 1, ...o });
const base = (email, acc = {}, extra = {}) => ({ email, account: A(acc), settings: S, recipientLocalHour: 10, sentTodayFromInbox: 3, ...extra });

export const good = [
  ["email 1, two insights", base(E("Hi Dave,\n\nSaw Coastline is hiring a second dispatcher, and your Google profile says calls after 5pm go to voicemail.\n\nWe set up an AI receptionist that answers those calls and books jobs into Jobber. Worth a 15 minute look?\n\nSam"))],
  ["mentions their own website", base(E("Hi Dave,\n\nYour site coastlineplumbing.com still says the online booking page is coming soon. Most plumbers we talk to lose late calls the same way.\n\nWorth a chat?\n\nSam"))],
  ["congratulations opener", base(E("Hi Dave,\n\nCongratulations on the new Round Rock location. More vans usually means more missed calls after hours.\n\nOpen to a quick chat about it?\n\nSam"))],
  ["footer on one line", base({ ...E("Hi Dave, saw you are hiring. Open to a chat?\n\nSam"), body: "Hi Dave, saw you are hiring. Open to a chat?\n\nSam\nNot for you? Reply stop and I won't email again. Ridgeline AI, 500 Congress Ave, Austin TX 78701" })],
  ["footer different case and spacing", base({ ...E("x"), body: "Hi Dave,\n\nNoticed your reviews mention slow callbacks. Want to see how we fix that?\n\nSam\n\nnot for you?  reply stop and i won't email again.\nRidgeline AI,\n500 Congress Ave, Austin TX 78701" })],
  ["curly apostrophe in footer", base({ ...E("x"), body: "Hi Dave,\n\nYour ads run all weekend but the office is closed. Worth a chat?\n\nSam\n\nNot for you? Reply stop and I won\u2019t email again.\nRidgeline AI, 500 Congress Ave, Austin TX 78701" })],
  ["email 2 with booking link", base(E("Hi Dave,\n\nFollowing up on my note about after hours calls. If useful, grab a time here: https://ridgeline.ai/book/15min\n\nSam", { step: 2 }))],
  ["step written as text 'email 2'", base(E("Hi Dave,\n\nOne more thought: here is how it works for a Dallas plumber. https://ridgeline.ai/book\n\nSam", { step: "email 2" }))],
  ["email 3 with our own site link", base(E("Hi Dave,\n\nLast note from me. Short example here: https://ridgeline.ai/plumbers\n\nSam", { step: 3 }))],
  ["published email status", base(E("Hi Dave,\n\nSaw you are hiring an office manager. Worth a chat?\n\nSam"), { emailStatus: "published" })],
  ["email_allowed stored as true", base(E("Hi Dave,\n\nSaw you are hiring. Worth a chat?\n\nSam"), { emailAllowed: true })],
  ["window edge 8am", base(E("Hi Dave,\n\nSaw you are hiring. Worth a chat?\n\nSam")), {}],
  ["4pm local", base(E("Hi Dave,\n\nSaw your new van wraps around Austin. Busy season ahead?\n\nSam")), {}],
  ["9 of 10 sent today", base(E("Hi Dave,\n\nQuick one about missed calls. Worth a chat?\n\nSam"))],
  ["reply, no footer needed", { email: { to: "dave@coastlineplumbing.com", subject: "Re: after hours calls", body: "Thanks Dave. Tuesday at 10 works. Here is the link to lock it in: https://ridgeline.ai/book", kind: "reply" }, account: A({ replied: "yes" }), settings: S }],
  ["reply with empty subject", { email: { to: "dave@coastlineplumbing.com", subject: "", body: "Sounds good, talk Thursday.", kind: "reply" }, account: A({ replied: "yes" }), settings: S }],
  ["test email to own address", base({ ...E("Test from Jarvis, please confirm the From address."), to: "sam@ridgeline.ai" }, { email: "sam@ridgeline.ai", emailAllowedReason: "member's own address", website: "" }, { recipientLocalHour: 22 })],
  ["mentions Jobber and Google Ads, no domains", base(E("Hi Dave,\n\nYou run Google Ads and Jobber, but calls after 5pm still go to voicemail.\n\nWorth a chat?\n\nSam"))],
  ["sentence with e.g. and numbers", base(E("Hi Dave,\n\nMost plumbers miss 20 to 30 calls a month, e.g. after 5pm and weekends. Worth a look?\n\nSam"))],
  ["doNotContact list as text", base(E("Hi Dave,\n\nSaw you are hiring. Worth a chat?\n\nSam"), {}, { settings: { ...S, doNotContact: "spam@blocked.com, nope.com" } })],
];
good[11][1].recipientLocalHour = 8; good[12][1].recipientLocalHour = 16; good[13][1].sentTodayFromInbox = 9;

export const bad = [
  ["guessed address", base(E("Hi Dave, worth a chat?\n\nSam"), { emailStatus: "guess" }), "not sendable"],
  ["risky address", base(E("Hi Dave, worth a chat?\n\nSam"), { emailStatus: "risky" }), "not sendable"],
  ["do not contact account", base(E("Hi Dave, worth a chat?\n\nSam"), { doNotContact: "yes" }), "do not contact"],
  ["domain on do not contact list", base({ ...E("Hi, worth a chat?\n\nSam"), to: "bob@nope.com" }, { email: "bob@nope.com", website: "" }), "do not contact list"],
  ["already replied (cold step)", base(E("Hi Dave, following up.\n\nSam", { step: 2 }), { replied: "yes" }), "replied"],
  ["campaign not approved", base(E("Hi Dave, worth a chat?\n\nSam"), {}, { settings: { ...S, campaignApproved: "no" } }), "not approved"],
  ["daily cap reached", base(E("Hi Dave, worth a chat?\n\nSam"), {}, { sentTodayFromInbox: 10 }), "daily limit"],
  ["outside hours", base(E("Hi Dave, worth a chat?\n\nSam"), {}, { recipientLocalHour: 19 }), "working hours"],
  ["missing opt out", base({ ...E("x"), body: "Hi Dave, worth a chat?\n\nSam\nRidgeline AI, 500 Congress Ave, Austin TX 78701" }), "opt out"],
  ["unfilled placeholder", base(E("Hi {{first_name}}, worth a chat?\n\nSam")), "placeholders"],
  ["spam phrase", base(E("Hi Dave, I hope this email finds you well. Limited offer this week.\n\nSam")), "banned"],
  ["link in email 1", base(E("Hi Dave, see https://ridgeline.ai/book\n\nSam", { step: "email 1" })), "too many links"],
  ["foreign domain link", base(E("Hi Dave, see this case study https://bit.ly/abc\n\nSam", { step: 2 })), "not ours"],
  ["HTML body", base(E("<p>Hi Dave</p> worth a chat?\n\nSam")), "HTML"],
  ["cold email not allowed", base(E("Hi Dave, worth a chat?\n\nSam"), { emailAllowed: "no", emailAllowedReason: "sole trader in Germany" }), "not allowed"],
];
