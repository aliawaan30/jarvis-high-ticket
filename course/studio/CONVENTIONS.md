# Lesson writing conventions (High Ticket Studio)

Audience: a paying member (US$2,500 DIY tier up to private tier). The course must stand on its own without a call. Premium, calm, specific. Warm co-founder tone, tough on outcomes. Never abrasive. NO EM-DASHES anywhere. Use "Jarvis" for their agent.

Blake's raw dumps are principles to expand, not polished copy. Keep his voice and his claims; expand with structure, scripts, worked examples and diagrams. Do not invent client results. Where a number is his, keep it. Where a number is illustrative, say so in the sentence.

## Lesson JSON (data/lessons/<id>.json)
{"id","title","lede","deliverable","body","shapes":[]}
- lede: one short sentence in normal, non-italic text explaining the lesson.
- deliverable: "They leave with ..." one sentence, concrete.
- body: HTML using ONLY this vocabulary, all top-level blocks:
  <h2>Section</h2>, <h3>LABEL</h3>, <p>, <ul>/<ol>, <blockquote>spoken line</blockquote>, <hr>
  <div class="b-script"><p>...</p></div>   SAY THIS: a script block the member reads on a call
  <div class="b-prompt"><p>...</p></div>   PASTE INTO JARVIS
  <div class="b-note"><p>...</p></div>     NOTE (brass)
  <div class="b-ex"><p>...</p></div>       WORKED EXAMPLE
  <table class="tbl"><tr><th>..</th></tr><tr><td>..</td></tr></table>
  <figure class="fig"><img src="/data/img/<id>-<slug>.svg" alt="..."><figcaption>...</figcaption></figure>
- Use <strong> and <em> sparingly. No inline styles. No <h1>.

## Diagrams (data/img/*.svg)
Hand-written SVG, viewBox 1200 x N, white background, fonts: "Instrument Sans", Arial for body, "Fraunces", Georgia for headings, "IBM Plex Mono", Menlo for labels.
Palette: ink #0e1016, ink-2 #5a5d6b, ink-3 #8b8e9c, line #e6e7ec, accent #4b2fc4, accent-soft #efecfb, brass #8a6210, brass-soft #f8f1df, paper #fbfbfc.
Keep them simple: boxes, arrows, a ladder, a timeline. 3 to 7 elements. Every diagram must be readable at 700px wide. Round corners 10. Stroke 1.5. Text 20 to 26px.

## Outline (data/outline.json)
modules[].lessons[] = {"id","title","written":true}. ids: ^[a-z0-9][a-z0-9-]{0,63}$, prefixed m<num>-. Insert new lessons in reading order. Back up before editing (server does this on API saves; if editing the file directly, copy to outline.json.bak first).

## Shape of a premium lesson
1. One paragraph that says what this lesson changes for them.
2. The idea, taught properly (the "why").
3. The method, as numbered steps or a script.
4. A worked example with real texture.
5. What Jarvis does for them here (a b-prompt where it genuinely helps).
6. "Do this now" close: one task, one output, one check.
Target 900 to 1,800 words per lesson. A diagram or table wherever a picture beats a paragraph.
