# Higgsfield media route

Higgsfield generates the site's images and films. Checked 18 November 2026; the API and its model list change, so read Higgsfield's current documentation and price list before every new job.

## What it is

- An API at api.higgsfield.ai with keys made in the Higgsfield console (console.higgsfield.ai), billed from a prepaid US dollar balance. Source: Higgsfield, "How To Generate AI Videos Straight From the Higgsfield API", https://higgsfield.ai/blog/generate-ai-videos-higgsfield-api
- The API is a separate product from the higgsfield.ai website: website plans and credits do not cover API use. Source: same.
- The catalogue includes video families such as Kling (the family v3 was tested with), Seedance, Wan, MiniMax, LTX and Higgsfield's DoP, and image models including Higgsfield's Soul 2 and Soul Cinema. The API catalogue can differ from the website's model list. Source: same.
- Requests are asynchronous: submit, keep the request ID, poll the status, download the result when complete.
- Authentication uses a key ID and a key secret. One published guide shows the header as Authorization: Key KEY_ID:KEY_SECRET. Source: Layer3 Labs guide, https://www.layer3labs.io/guides/higgsfield-api . Confirm against the official documentation before the first call.

For the shot-writing method, the first-time connection steps and plain-words error messages, see [higgsfield-prompting.md](higgsfield-prompting.md).

## Setting it up with the member (once)

1. The member creates an API account at console.higgsfield.ai, adds a small balance, and creates an API key.
2. They save the key ID and secret as your secrets using the secure secret card (names: HIGGSFIELD_KEY_ID and HIGGSFIELD_KEY_SECRET). Never ask them to paste keys into chat, and never put a key in the website's code or files.
3. Run one small, cheap test (one image) and confirm it works and what it cost.

## Every job

1. **Plan.** List each shot: its section, aspect ratio, still or film, duration, the art direction paragraph from the guideline, the composition, the one camera movement, the ending, and the text-safe area.
2. **Price and time it.** Look up the current price per image and per second of video for the chosen models, and estimate the total and the time (films often take several minutes each). Within the member's saved media budget, carry on without asking; if the total would exceed it, ask first and offer a cheaper option. Never exceed what was agreed. Pause any background goal while generating.

   Speed: submit every shot in one go and then wait for them together, not one after another. Make quick drafts first (lower resolution or a faster model) to approve the look and framing, then generate finals only for the approved shots.
3. **Generate stills first,** in the shape each shot's role needs (tall, wide, square, texture), not all in one ratio. Inspect each for shape, materials, light, crop, unwanted text and continuity with the other shots. Regenerate only real defects.
4. **Animate approved stills** into films: one clear movement per film, stable geometry, 5 to 10 seconds. Inspect at least six points across each film, including the ending. Trim a weak ending rather than paying for a reroll when the story still works.
5. **Record** every request ID, model, prompt, cost and result, and keep originals outside the published site.
6. **Process for the web:** films as H.264, no audio, faststart, around 1600 px wide (the v3 settings that tested well), plus a phone version of the hero film (tall crop, 720p, ideally under 3 MB) for the phone loop; stills as compressed WebP or AVIF with a JPEG fallback.

## Never

- Generate people presented as the client's real staff, customers or patients.
- Generate before and after results.
- Generate logos, certification badges or text meant to look real.
- Retry a paid request whose result is unclear: check the request ID first.
