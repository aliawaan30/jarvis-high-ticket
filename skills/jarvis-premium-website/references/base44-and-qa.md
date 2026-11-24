# Base44 implementation and evidence

> **Version 3 evidence.** Kept for its tested methods and results. Where it differs from the version 4 files (Higgsfield instead of Envato or Kie, the phone video loop, one enquiry pipeline owned by the website, the design system and surface rules), the version 4 files win.


## Build and publish are separate states

Record the app ID, app name, exact editor route, exact public route and current public fingerprint. The root can show a diagnostic page while the intended page exists at another route. Do not diagnose a failed build by looking only at `/`.

After sending a builder instruction, retain the response, task ID and claimed files when the tools expose them. If the public bundle is unchanged, possible explanations include unpublished changes, the wrong route/app, a failed build or stale deployment. That evidence alone cannot distinguish them.

Inspect the editor/source/preview when supported. If changes are present there but not public, mark publication pending. If publishing is not available to the Superagent, ask the owner for the single publish action after the code is ready to review. Do not wait indefinitely or resend the same build to fix publication.

Use the supported Base44 native frontend. Do not deploy interactive HTML as a backend function. Do not infer tool schemas or app-creation/publishing authority from another agent's transcript.

## Runtime adaptation

`../assets/runtime.js` is a tested local vanilla reference, not a React component. When adapting:

- Use refs for the film section, sticky element and video.
- Create one controller per mounted film and clean it up from the effect.
- Bind menu and selector state through the framework's normal handlers.
- Keep frame updates out of React state.
- Keep one source of truth for selected panels and ARIA state.
- Do not let shared styles leak into unrelated Base44 pages.
- Load stored assets from stable final URLs. Recheck CORS if fetch crosses origins.

Choose the film/still mode before setting `src`. Phones, reduced motion and data saving should make zero video requests. A failed video load switches to still mode and removes long travel. It necessarily starts with a failed attempt, so report failure bytes honestly.

## Minimum actual-browser checks

Run each on the exact frontend route and record passed, failed or unverified:

1. Native page renders with final stored images and the intended content.
2. Both film sections load on an eligible desktop viewport.
3. Scroll to separated points near 0%, 25%, 60% and the ending, then reverse to 30%. Record actual currentTime and expected duration mapping. Observe decoded frames or screenshots as well as the number.
4. Scroll normally and rapidly. Seeking catches up without freezing or trapping the page. The clip is paused while time is controlled by scroll.
5. The first screen is useful before loading. The main button and skip link reach the promised sections.
6. All navigation and back-to-top links reach real targets.
7. Compact menu opens, closes after navigation and with Escape, and returns focus to its trigger.
8. Keyboard and pointer activate every choice; exactly one corresponding panel appears with correct selected state.
9. A real form/booking/checkout integration produces its actual intended outcome. For a concept using a download, verify the generated file contains the selected information. Do not substitute a success toast for delivery.
10. At about 780px and 375px, inspect whole-page layout, overflow, clipped headings, image crops and contrast. Hiding overflow is not a repair for oversized content.
11. Reduced motion and detectable data saving use still layout with zero video requests.
12. Deliberately abort a video request. The page remains usable without pinned empty space. Restore normal assets after the test.
13. Inspect browser console and page errors. Source grep alone is not console verification.
14. Navigate away and back. The media controller works again.
15. Search authored copy for em dashes, placeholder links, invented facts, fake claims and development instructions.

For full-page screenshots, let lazy images actually load first. A screenshot tool can otherwise capture empty offscreen images even though they load during ordinary scrolling. State when mobile results are emulation rather than a physical phone.

## Evidence and stopping

Save concise raw measurements, screenshots, generation task IDs, original/processed media sizes, final URLs, changed files and public fingerprint. Record Base44 credit use only if visible. Do not guess it from elapsed time.

Fix a demonstrated issue and rerun the affected checks. A repeated unresolved blocker should be reported with the precise failing operation. Do not declare the builder broken from a public fingerprint alone and do not spend repeated calls on that assumption.

The local five-site test establishes technical behaviour of its reference implementation. A fresh Base44 agent must still port and test it. User aesthetic approval, client content and real business integrations are separate release conditions.
