# Design reference: the CRM Blake pointed at

Source: https://www.youtube.com/watch?v=YtSGWAAf5OU. Frames in `reference/` (01 main table, 02 detail panel, 03 leads table, 04 import modal). Transcript in `reference/video-transcript.txt`.

What it is: a founder built a creator agency CRM in an afternoon with Claude Code, from a free template, as a Next.js app hosted on Vercel with login and team roles. Data synced to Notion. Blake sent it for the look and the simplicity, not the stack.

## The look

Dark theme, dense, Linear or Notion feel. Small type, coloured pill badges for stage, one purple accent. Left sidebar with views and live counts. Nothing decorative.

## The screens (ours map to the seven things)

1. **Main table** (our Leads). Sidebar: All leads, Pipeline, Follow ups, with counts, and the stage list with counts. Top: search (Cmd+K), filters (stage, source, sort). Columns: lead (name plus business), stage pill, source, next step, next follow up date colour coded (red "2 days overdue", amber "Today"), last touch. Buttons: New lead, Export.
2. **Detail slide over** (our lead screen). Opens from the right on row click. Stage, next follow up, next step, last touch, contact fields, notes, and the full timeline underneath: messages in and out, calls, stage moves.
3. **Pipeline board.** One column per fixed stage, drag cards between them. Same data as the table, just a board.
4. **Follow ups.** Grouped Overdue, Today, Next 7 days, Later, with three count cards at the top. This is the daily habit screen.
5. **Numbers card.** Not in the video. Ours sits at the top of the main view: spend, leads, CPL, calls booked, cost per booked call, show rate, close rate, revenue, CAC against ticket, with period and last sync.
6. **Import.** Paste from Sheets or upload CSV, map columns, done. Export to CSV.
7. **Login.** Email login, member sees only their records.

## Interactions to copy

- Click a row, the panel opens, edit in place.
- Drag between stages on the board.
- "Log touch" sets the next follow up three days out.
- Colour coded overdue dates on every row.
- Cmd+K search.

## Leave out

Notion sync, video grid, payouts, workspace switcher, team roles beyond member and team admin, any design tool upsell.

## The presenter's build method, which is also ours

Ship a one page v1 on real data first, then add one feature per prompt. Record a two minute demo, give it to the team, their feedback becomes the next prompts. He says the one thing that stops it looking AI made is design taste: a real style reference, consistent spacing, no stock components. Use the frames in `reference/` as that style reference.
