# The High Ticket Course

The members course for the high ticket offer. Same machinery as the free Base44
course: one standalone HTML page per lesson, gated steps, progress saved in the
browser, a jump menu on every page. Built from a content spec so you never edit
HTML by hand.

Right now it is a skeleton. 7 modules, 44 lessons, every title and promise
written, every step body waiting to be filled.

## Build it

```bash
python3 build.py
```

Reads `content/`, writes `site/`. It prints how many blocks are still to fill
and how many videos are recorded.

## Fill in a lesson

Open the module file in `content/`, find the lesson, and replace the hint list
with real blocks.

Blank:

```python
("Run the market research skill", [
    "The exact prompt and the inputs it needs.",
    "What a good run looks like versus a lazy one.",
]),
```

Written:

```python
from build import p, prompt, see, callout, ul

("Run the market research skill", [
    p("Open Jarvis and give it this. One market at a time."),
    prompt("Run the underserved market research skill. My country is ..."),
    see("five markets, each with the evidence it found and a reason against it."),
    callout("<b>If it comes back with huge markets</b>, it did not understand the brief. Run it again and name a revenue range."),
]),
```

Available blocks, all from `build.py`: `p`, `ul`, `prompt`, `script`, `see`,
`callout`, `todo`.

- `prompt(text)` is a copy box for something they paste into Jarvis.
- `prompt(text, label="SOMETHING")` is the tall scrolling version with a Copy button.
- `script(text)` is the same thing labelled for words they say on the phone.
- `see(text)` is the "You should see" confirmation. Put one at the end of any step that builds something.

Then run `python3 build.py` again.

## Add a video

Record it, grab the Loom share link, put it in the lesson:

```python
L(
    "The Offer Strategy Session",
    "...",
    "...",
    loom="https://www.loom.com/share/abc123...",
    ...
)
```

Rebuild. The hub stops saying "to record" against that lesson. `vidcap=` sets
the caption under the player, which is where you name the member you recorded
with.

## Add or move a lesson

Lesson letters, next links, the hub and the jump menu are all generated from
`content/`. Add a lesson to the list and everything renumbers itself. Note that
moving a lesson changes its filename, so anyone deep linked to the old one will
404. Moving things is free before launch and expensive after it.

## Deploy

`site/` is the whole website. Nothing is built at view time.

1. Netlify, Add new site, Deploy manually, drag the `site` folder in. Or point
   Netlify at this repo with publish directory `site` and no build command.
2. Domain management, add the subdomain you want.

`site/netlify.toml` already sends `noindex` headers.

## Before a paying member sees it

**There is no access gate on this site yet.** Anyone with the link reads the
whole course. That is fine while it is empty and not fine the day you fill it.
Two ways to close it:

- Copy `gate.js` from the free course portal (`portal/public/gate.js` in
  base44-course), point it at whatever table says someone has paid, and add
  `<script src="/gate.js"></script>` back into `shell/head.html`. The extractor
  strips it out, so put it back there, not in the generated pages.
- Or Netlify password protection on the site, and hand the password out with
  the welcome email. Cruder, works today.

Pick one before the first real lesson goes up.

## House rules

- No em-dashes anywhere a member reads. The build does not enforce it, so do
  not introduce them.
- One change per prompt, same as the free course.
- Anything you have not personally watched work gets marked `[VERIFY]` in the
  copy until you have.
- Never tell a member to paste an API key into a chat window, including Jarvis.

## Files

```
build.py              the renderer. Look here for the available blocks.
content/              the course. One file per module, plus _common.py
shell/head.html       page head and CSS, lifted from the free course
shell/tail.html       the step gating, copy buttons, sounds, confetti
shell/nav.template.js the jump menu, module list injected at build time
shell/netlify.toml    copied into site/ on every build
tools/extract_shell.py re-sync the shell from the free course if it changes
site/                 generated. Do not edit anything in here.
```
