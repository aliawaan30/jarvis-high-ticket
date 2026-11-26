# Jarvis 2.0 onboarding hub

One page per module with the file, the install message and every prompt. Students sign in with their programme email. Ticks, installed pack versions and "I'm stuck" tickets save to Supabase.

## How updates flow

1. Edit a skill in skills/ (bump its Version line) or a page in hub/content/.
2. Change the pack's "note" in hub/content/packs.json if students should hear about it.
3. Commit and push to GitHub.
4. Netlify rebuilds: zips are rebuilt from skills/, changed packs upload to Supabase, the hub shows the new versions, students who installed an older version see "Update available", and Discord gets a one line notice per changed pack.

Students still update their own Jarvis: they send "Update my Jarvis 2.0 skills" (uses their update link) or download the file again.

## Files

| Path | What |
| --- | --- |
| content/packs.json | Which skills go in which zip |
| content/site.md | Welcome page, booking link, Discord link |
| content/modules/*.md | One file per page. `## Step title {time} optional`, prompt blocks, `> see:` and `> fix:` notes, `[[pack:id]]`, `[[link:slug]]` |
| src/ | The site (plain HTML, CSS, JS) |
| functions/pack.mjs | Signed downloads and the update manifest for Jarvis |
| functions/site.mjs | Programme content, members only |
| supabase/schema.sql | Tables, sign up gate, storage bucket |
| ../scripts/build_hub.py | The build |

## One time setup

1. **Supabase:** create a new project. SQL Editor: run supabase/schema.sql. Authentication, Email Templates, Magic Link: add `Your code: {{ .Token }}`. Authentication, URL Configuration: set Site URL to the Netlify URL.
2. **Netlify:** Add new site, Import from GitHub, pick jarvis-high-ticket. Base directory: `hub`. Build settings come from hub/netlify.toml.
3. **Netlify environment variables:** SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY (mark secret), DISCORD_WEBHOOK_URL (optional, from Discord channel settings, Integrations, Webhooks).
4. Deploy. The first production build uploads every pack.

## Adding a student

Supabase, Table Editor, members: add a row with their email in lower case and their first name. They can sign in straight away. Set active to false to remove access (also kills their update link).

## Seeing who is stuck

Supabase, Table Editor: tickets (status new, doing, done) and the team_progress view (steps done, last active, open tickets).

## Local preview

    python3 scripts/build_hub.py --demo
    cd hub/dist && python3 -m http.server 8080

Open http://localhost:8080. With no Supabase settings the hub runs in preview mode.

## Security

1. **Members only.** Only emails in the members table can create a login (a database trigger blocks everyone else). Set active to false to remove someone: their content, downloads and update link stop working straight away.
2. **No passwords.** Sign in is a 6 digit code (or the link) sent to their email.
3. **Content behind login.** The lesson text, prompts and file details are bundled into the /api/site function and only returned to a signed in member. The public site is an empty shell. Zips come from private storage through 5 minute signed links.
4. **Keys.** The service role key lives only in Netlify environment variables. The browser only ever sees the anon key, and every table has row level security.
5. **Recommended Supabase settings:** Authentication, Providers, Email: set the email OTP expiry to 600 seconds (10 minutes). Keep the default rate limits. Add custom SMTP before launch.
