# Higgsfield prompting, setup and errors

How to get the best images and films from Higgsfield, how to connect it the first time, and how to explain its errors in plain words. Read with higgsfield-route.md.

## 0. Write shots from the story, not the topic

Basic results come from topic prompts ("something about websites", "a modern office"). Write every shot from the buyer's journey in the Scroll Score instead: the problem moment, the turning point, the result. Each shot names a real person's situation (shot so no real customer is implied), a place, a time of day, an emotion and one thing that moves. Check each shot against the recipe for the niche in motion-system.md. If a shot would fit any business, rewrite it until it only fits this one.

## 0b. The premium image bar (every still, every site)

Learned 27 November 2026: first images read as generic stock or 3D renders because the skill set a budget but never defined premium. Every still prompt starts from this core, adapted to the niche, then adds the look line and the shot recipe:

1. **The photographic standard:** shot like the best photography in the niche, on a professional camera (for example "top-tier architectural photography on a medium-format camera" for properties and buildings, "editorial food photography" for restaurants, "documentary photography" for trades, "soft editorial beauty photography without faces" for med spas).
2. **Real, local light:** the time of day, the direction of the sun and the place (for example "late-afternoon Texas Hill Country light, low western sun"), deep or shallow focus as the shot needs, fine film grain.
3. **Quiet quality:** never glossy, over-retouched, oversaturated or CGI-looking.

**Generate 2 to 3 options for every key shot** (the hero, the keyframes, the most-seen section images) and pick the best. Never ship the first result.

## 1. The look line (shared by every shot)

Write one look line from the brand guideline and put it at the start of every prompt, word for word, so every image feels like one shoot:

`[light] , [time of day], [lens and depth of field], [colour palette in words], [film or texture look], [mood]. No text, no logos, no watermarks.`

Example (Fernhollow): "Early morning golden light with soft mist, 35mm lens, shallow depth of field, sage, moss green, warm stone and cream tones, fine film grain, calm and natural. No text, no logos, no watermarks."

## 2. The shot recipe (fill every line)

Cinematic films need depth: a foreground, a middle and a background layer (for example grasses close to the lens, the path in the middle, trees behind), so the camera move creates parallax.

1. **Subject:** exactly what is in the frame, with real materials (weathered limestone path, dew on lamb's ear leaves).
2. **Composition:** the shape (from the image role map), where the subject sits, where the text-safe area is (for example "subject in the right third, calm empty sky on the left for text").
3. **Camera:** height and angle (low, eye level, overhead), lens feel (35mm, 85mm close), distance.
4. **Light:** direction and quality (low sun from the left, backlight through leaves, soft overcast).
5. **Textures and details:** two or three tactile details that make it feel real.
6. **Colour:** the palette words from the look line, plus one accent if needed.
7. **For films only, one movement:** a single slow camera move (slow push in, slow lateral glide, slow crane up), 5 to 8 seconds, steady, no cuts. Describe what moves in the scene (grasses swaying, mist drifting, water trickling).
8. **Avoid:** screens, monitors, laptops, tablets and phones (screens are built in code instead), people's faces, hands with visible fingers in close-up unless needed, text, signs, logos, brand names, oversaturated colour, plastic-looking surfaces.

## 3. Choosing models: top quality only for finals

Checked 19 November 2026. The catalogue and names change often, so list the models your API account can use before every job and pick from what is actually available. Never use budget, turbo, lite or fast variants, or default quality settings, for final images and films: they are for drafts only.

**Stills:** the most photoreal image model in the catalogue (for example Higgsfield's Soul or Soul Cinema, Nano Banana Pro or FLUX.2, whichever are available), at the highest resolution. Make 2 to 4 options per shot and pick the best.

**Films, by shot type** (from Higgsfield's own model guidance and independent comparisons):

| Shot | First choice | Also strong |
| --- | --- | --- |
| Landscapes, gardens, outdoor light, weather, architecture exteriors | Veo 3.1 at its highest quality setting (high or ultra, or its best-quality preview variant) | Seedance 2.x |
| Turning an approved still into motion (most website films) | Seedance 2.x, or Kling 3.0 in its Pro mode at 1080p | Veo 3.1 with a start frame |
| Precise camera moves (a slow dolly, crane or orbit) | Higgsfield DOP named camera moves, or Kling with start and end frames | Wan |
| Interiors, products, close details | Kling 3.0 Pro or Seedance 2.x | Veo 3.1 |

**How to make the hero film top quality:**
1. Start from the approved, upscaled still (image to video), never text to video.
2. Use 1080p and 8 to 10 seconds; the highest quality setting the model offers.
3. Make the hero film with two different top models from the table and keep the better one. The extra cost is small next to the value of the hero.
4. Where the model supports it, give a start frame and an end frame so the camera move is controlled.
5. Use one named camera move (from DOP presets or a precise description) and natural motion in the scene: mist drifting, grasses swaying, light shifting, steam rising. Something must move in the scene, not only the camera, or the film looks like a slideshow.

Before generating, show the member the models you chose for each shot, why, and the cost.

**Proven in live builds (27 November 2026), check the catalogue still offers them:** Soul Cinema (or Grok Imagine) for hero and gallery stills; Kling 3.0 Pro with a start and an end frame for drone and transformation films.

## 4. Keyframe pairs for the transformation scroll

The transformation scroll (motion-system.md) needs a film that goes from a start state to an end state with the camera and composition matching exactly, so scrolling feels like time passing in one place.

1. **Start keyframe:** generate the start state (for example the bare yard) with the look line and full shot recipe, 16:9 for desktop.
2. **End keyframe:** create the end state (the finished garden) by **editing the start keyframe**. Keep the composition, lens and light identical; change only what the story needs (the state of the scene, or for a drone move only the camera height or position) with an image editing model, keeping the same camera, horizon, framing and light, rather than generating a new image. Check both frames line up when laid over each other.
3. **The film between them:** use a video model that accepts a start frame and an end frame (for example Kling 3.0 with start and end frames, or a Veo start and end frame lane, whichever the catalogue offers), 8 seconds, highest quality, a locked or very slow camera, with the prompt describing the change happening gradually (soil levelled, path laid, plants growing in, light warming).
4. **Frames for the web:** if the workspace has ffmpeg, extract frames for a canvas sequence:
   `ffmpeg -i film.mp4 -vf "fps=12,scale=1600:-2" -c:v libwebp -quality 70 frames/desktop_%03d.webp`
   and a phone set with `scale=900:-2`. Keep about 90 to 100 frames per sequence. If ffmpeg is not available, encode the film with a keyframe on every frame and scrub the video's current time instead (the v3 engine's method), and say which method was used.
5. Also make a phone keyframe pair in a tall shape (4:5 or 9:16) when the phone version keeps the transformation.

## 4b. Planning to the budget

Before generating, write a short cost table from the current catalogue prices: each shot type (key still, gallery still, keyframe pair, drone or transformation film, phone film version), how many, the price each, and the total. Plan to the member's cap in this order: the hero, then the keyframes and the signature film, then section images, then the gallery. **When the cap is tight, cut the number of gallery images and secondary films, never the quality or the model of the key shots.** Show the table at check-in 1.

## 5. Quality gate (reject and redo only these)

Anything that reads as stock or a 3D render, fake-looking materials, plastic-looking plants or foliage, too much contrast, light that does not match the other shots, films that look like a still photo slowly zooming (no motion in the scene, no depth), soft or low-detail frames, warped or melting shapes, extra or broken fingers, garbled or fake text, plastic or waxy surfaces, impossible physics (water flowing up, floating objects), a subject cut off where text will sit, colours that do not match the look line, jitter or morphing in films, or a weak final second (trim it instead of rerolling when the story still works).

## 6. Niche starter prompts (adapt, never paste blindly)

- **Garden and landscaping:** "Winding natural stone path through a mature water-wise garden of ornamental grasses and native perennials at dawn, soft mist, low golden light from the left."
- **Real estate:** "Bright, airy living room of a modern family home, large windows, straight vertical lines, natural daylight, wide interior view from the corner at chest height."
- **Med spa:** "Calm, minimal treatment room with soft natural light, linen textures, a single orchid, warm neutral tones, clean and serene, no people."
- **Restaurant or cafe:** "Close-up of a freshly plated dish on a handmade ceramic plate, warm side light, shallow depth of field, rustic wooden table."
- **Trades and contractors:** "New roof on a two-storey home at golden hour, clean shingle lines, blue sky, shot from the street at an upward angle."
- **AI receptionist (the problem moment):** "A roofer kneeling on a half-finished roof at dusk, first drops of rain, tool belt and shingles around him, his phone buzzing in his jacket pocket with the screen not visible, he cannot answer, cinematic low angle, cool blue dusk with warm last light on the horizon, wet shingles glinting." Keyframe pair for the evening scroll: the same small contractor's workshop exterior at 6pm daylight, and edited to 11pm night with one light on inside.
- **Websites agency (the buyer's world):** "A busy café owner wiping the counter during the lunch rush, customers blurred in the background, natural window light, warm tones, shallow depth of field, no screens." 

## 7. First-time connection

When no Higgsfield keys are saved:

1. Explain in plain words: "Higgsfield makes your client's images and films. It needs its own API account and a small balance, separate from any Higgsfield subscription."
2. Walk the member through console.higgsfield.ai: sign in, add a balance (about 10 US dollars covers a test site), create an API key.
3. Open the secure secret card for HIGGSFIELD_KEY_ID and HIGGSFIELD_KEY_SECRET. Never ask for keys in chat. If the console gives one combined key instead of two parts, put the whole combined key in HIGGSFIELD_KEY_ID (this worked in the live build on 27 November 2026) and leave the secret field as the card allows.
4. Run one cheap test image. Report the model, the cost and the request ID.
5. Ask once for the media budget per website (suggest 15 US dollars) and save it in memory, so later websites need no cost approval within it.

## 8. Errors in plain words

Read the error message Higgsfield returns (its text and status), then tell the member what happened and what to do. Never show raw error text alone, and never pay twice for the same shot.

| What happened | Tell the member | Then |
| --- | --- | --- |
| Not enough balance or credits | "Your Higgsfield balance has run out. Add credit at console.higgsfield.ai, then say continue. Nothing was charged for this shot." | Wait for continue, then resubmit only the failed shots. Before a job, if the balance is lower than the estimate, warn first instead of failing halfway |
| Key rejected or not allowed | "Higgsfield did not accept the key. Create a new key at console.higgsfield.ai and save it again." | Open the secure secret card |
| Too many requests | Nothing, unless it keeps happening | Wait and retry with growing pauses, up to three times |
| Prompt blocked by content rules | "Higgsfield blocked one shot under its content rules, so I rewrote it." | Rewrite the shot safely and retry once |
| Model unavailable or renamed | "That model is not available right now, so I used the closest one." | Pick the closest model from the current catalogue |
| Higgsfield busy, slow or down | "Higgsfield is busy. I will check again in a few minutes." | Check the request status by its ID before any retry |
| Anything else | "Higgsfield returned an error: [short plain summary]. I have not been charged twice." | Save the request ID and the error, and tell the member the next step |

Record every error with its request ID and time in the job log.
