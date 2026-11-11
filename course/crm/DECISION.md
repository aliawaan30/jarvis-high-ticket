# Blake's decision, 31 Oct 2026: build it

Blake read SPEC.md and PLAN.md. Decision: build the custom CRM, not managed GHL. His words: "ideally we want a simple, yet nice looking CRM built. Pretty simple but fairly good." It "definitely needs login" and "needs to track everything across the board and genuinely be useful and simple in nature."

He approved the seven things exactly as written in BRIEF.md. No additions.

## What that means for the plan

- Platform: one team owned Base44 app, every member logs into the same app, their data only. Never one app per student. Start with the Base44 proof steps in PLAN.md (isolation, per member keys, signed webhooks, scheduled job, two Meta accounts). If one fails, stop and report; do not quietly swap platforms.
- Design target: see DESIGN-REFERENCE.md (notes from the video Blake sent, https://www.youtube.com/watch?v=YtSGWAAf5OU). Simple and good looking beats feature rich. One pipeline board, one lead screen, one numbers card, one login. If a screen does not map to one of the seven things, it does not exist.
- Build order: 1 prove the route, 2 records and screens, 3 Jarvis API and webhooks, 4 intake, 5 follow up through Jarvis, 6 the card, 7 pilot. Show Blake something clickable after step 2, before any integration work.
- Questions 2 and 3 from SPEC.md are still open (booking tool and mailbox for the pilot; member count and technical owner). Proceed with sensible defaults and state them: the booking tool the funnel lessons already use, Gmail or Google Workspace for mailbox, pilot of two members, technical owner to be named by Blake.
- Keep [VERIFY ON PAID PLAN] on anything not yet tested on a paid Base44 plan. Never ask a member to paste a key, token or password into a chat.
