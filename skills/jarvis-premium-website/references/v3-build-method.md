# Build method from v3.0.0 (tested locally on five sites)

Kept word for word from version 3.0.0, which Blake approved on 10 September 2026. Version 4 adds research, the brand guide, the section library, Higgsfield and client delivery around it. Where v4 and this file differ, v4 wins: Higgsfield is the media route (not Envato or Kie), the hero film plays as a muted loop on phones, every form uses the website's own enquiry pipeline, and pages are built from the design system with the surface rules.


# Complete premium website builder

Build the entire website. The hero, reading sections, imagery, interactions and closing must belong to one business and one design direction. Do not stop at an impressive scroll video above generic sections.

## Evidence boundary

Version 3.0.0. Blake approved the five local website designs on 10 September 2026 and selected this as the premium website skill.

This method comes from five local Chromium-tested concepts: surf, restaurant, landscape, architecture and product. Both scroll films on all five were tested forward and backward, including decoded-frame checks. Mobile-width, keyboard, download, reduced-motion, data-saving and failed-media checks also ran locally. This skill has not yet passed a fresh Base44 Superagent run. Do not represent that unperformed test as complete.

The reference runtime and visual examples are in this package. The detailed research and test record are in `references/research-and-findings.md` and `references/local-test-results.md`; consult them for evidence and limitations. Read [references/design-and-media.md](references/design-and-media.md) when choosing the direction, and [references/base44-and-qa.md](references/base44-and-qa.md) when building and testing. Use [assets/runtime.js](assets/runtime.js) for the tested vanilla runtime mechanics. Adapt lifecycle and element ownership to the actual app framework rather than running a global DOM script blindly inside React.

## Start from a small brief

Use the business type, desired visitor action and any supplied assets. Infer a creative direction if the user delegated it. Ask one short question at a time only for material missing information, such as which real booking destination to use or whether imagery shows the client's actual products. Do not interview them about every font and section.

For a real business, separate supplied facts from missing facts. Use verified service information and client assets. Do not fabricate reviews, addresses, staff, prices, product specifications or commercial capabilities. For a concept, build meaningful discovery or a saved brief without pretending a booking, payment or enquiry was delivered. Follow the user's requested disclosure treatment; do not automatically append a large fictional-demo warning to every page.

Write in plain language, with no em dashes in authored copy. No decorative captions naming the effect, such as "The pour", "The pause", "The reveal" or "The scroll". Ordinary business copy may remain over footage when useful and readable.

## Plan the whole page before media

Save a concise, visible direction with these items:

- The business, visitor and real primary action.
- A specific visual idea, material palette, two type roles and image treatment.
- A section map from first screen to footer. Each section has a job, composition, copy requirement and media asset.
- A shot list: camera starting position, one achievable movement, ending composition, text-safe area and phone treatment.
- Known facts, required client content and proposed assets. Ask for missing content that materially affects the site instead of filling gaps with generic prose.

Research a few relevant real websites or creator case studies when needed. Inspect more than the hero. Extract concrete composition and content decisions. Do not copy another business's photography, claims or identity.

Use one or two film chapters when their stories justify them. For a two-film site, put a substantial editorial or product/service section between them. A longer video is not automatically a better or smoother experience. Match the motion to the business and the scroll travel to the actual clip.

## Generate a coherent asset set

Use the provider the user selected. For Envato, prepare copyable prompts and let the user perform the manual generation handoff. For an authorised Kie route, use its current documented schema and a saved secret on the agent. Never expose that secret in frontend code, chat, uploaded files or a reference package.

State the known cost or allowance before spending. Respect existing approval and the agreed bound. Persist the request and task ID; poll an existing task after an interruption. An ambiguous paid submission is not permission to generate again.

An initial media set often needs a hero, one meaningful detail image, one environment or use-context image, and an optional second film. Assign aspect ratios to the sections, not to a universal "landscape" rule. Portrait lower-section images were useful in the five-site test.

Inspect the starting images yourself before animating. Check shape, typography contamination, material, lighting, background and crop. For multiple views of one exact product, use the approved hero/client photograph as a reference. A common text prompt alone did not preserve the lamp design in the local test.

Prompt each film as one manageable action with stable geometry. An architectural glide, reflected light, fire or water movement is easier to evaluate than a long chain of unrelated actions. Do not promise that any generator will reliably execute an arbitrary fly-through.

Inspect distributed frames including the ending. Trim a weak tail when that preserves the intended story. Ask for a reroll only when the actual defect warrants its cost. Keep originals outside published assets, process web versions and record source/processed sizes and actual costs.

## Build the native frontend

Discover the current app tools and framework. Preserve the intended app identity and existing unrelated pages. Use Base44 app pages and its normal frontend pipeline, with scoped styles and actual handlers. Do not serve interactive HTML through backend functions or rely on CSS injected by the chat preview.

Use the selected reference's proportions as a starting point, not a universal template. Make the lower half strong: meaningful images, varied compositions, readable type and specific content. A bigger section number or more padding is not a design pass.

For scroll media:

- Keep the poster, headline and primary action useful before media loads.
- On eligible screens, use native page scroll with sticky media. Never intercept the wheel.
- Calculate progress from section height minus sticky-element height. Clamp target time to duration minus a small end tolerance.
- Schedule updates through requestAnimationFrame; serialise seeks and apply the newest target after completion. Bound repeated stalled seeks and fall back cleanly.
- Load the second clip near its section, not at initial page load. Stop unnecessary work offscreen or when the tab is hidden.
- A complete Blob fetch enables local seeking after download. It requires successful fetch/CORS, not HTTP Range. Do not claim progressive playback while building that Blob.
- If using direct loading instead, test actual-host seeking rather than assuming it works.
- Clean up observers, listeners, timers, requests and Blob URLs on unmount. Restore behaviour on history navigation.

At phone widths, reduced motion and detectable data saving, choose the still mode before fetching video. Remove pinned travel. A failed request switches to usable still mode and stops further retries, but it cannot undo bytes already downloaded. Compose the phone subject and type intentionally; do not copy a universal 65% crop.

Use actual section links and keyboard-accessible controls. Menus open, close after navigation, close with Escape and return focus. Selected choices expose state and exactly one panel. Connect client actions to their actual destination and test the result. Never simulate a successful transaction.

## Verify and deliver

Follow the browser checks in [references/base44-and-qa.md](references/base44-and-qa.md). Review full-page screenshots after ensuring lazy images have loaded. Inspect the post-hero sections individually. Test at desktop, around 780px and 375px. Fix observed defects, then rerun the affected checks.

Distinguish editor build state from public deployment. An unchanged public fingerprint does not establish that no code was written. Verify the exact route and target app, inspect the builder response or source when available, then determine whether publication is pending. If only the owner can publish, ask once after the work is concrete. Do not send repeated build requests to solve an unverified publish gap.

Return actual URLs, a concise visual comparison if there are variants, checks passed, checks unverified, exact changed files and visible generation/Base44 costs. A green status, HTTP 200, source-code string or screenshot alone is not proof of functioning motion.

Do not call the result client-ready or repeatedly reproducible solely because one fictional local build passes. The user judges aesthetic quality; real integrations, physical mobile behaviour and a fresh-agent Base44 test have their own evidence requirements.
