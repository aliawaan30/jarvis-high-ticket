#!/usr/bin/env python3
"""Build the high ticket course site from the content spec.

    python3 build.py

Reads content/ (one file per module), writes site/. Every page is standalone
HTML, no build step at view time, no framework. Deploy site/ to Netlify.

Nothing here decides what the course says. Content lives in content/*.py.
"""
import html, pathlib, re, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))  # so python3 -I build.py works too
SHELL = ROOT / "shell"
OUT = ROOT / "site"

# --------------------------------------------------------------- look
# Same structure as the free course, different identity: indigo primary with a
# brass alt, so a member can tell at a glance which product they are inside.
EXTRA_CSS = """
/* ---- high ticket identity ---- */
:root{
  --accent:#7c5cf0; --accent-deep:#5733c9; --accent-ink:#ffffff;
  --accent-tint:#f3efff; --accent-tint-2:#e3daff; --accent-line:#c3b1f7;
  --accent2:#c08a2e; --accent2-deep:#8f6410; --accent2-tint:#fdf5e6; --accent2-tint-2:#f7e7c4; --accent2-line:#e5c88c;
  --shadow-lg:0 1px 2px rgba(21,23,29,0.05),0 12px 28px -14px rgba(21,23,29,0.18),0 40px 64px -48px rgba(124,92,240,0.40);
  --ground-2:#f7f6fb; --surface-sunk:#f8f7fc; --line:#e8e6ef; --line-2:#d6d2e2;
}
body{background-image:radial-gradient(900px 460px at 12% -180px,rgba(124,92,240,0.11),transparent 68%),radial-gradient(760px 420px at 92% -60px,rgba(192,138,46,0.09),transparent 66%);}
.steps>li.spine-on+li::before{box-shadow:0 0 8px rgba(124,92,240,0.35);}
/* ---- video slot ---- */
.vid{margin:26px 0 6px;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;background:var(--surface);box-shadow:var(--shadow-sm);}
.vid-frame{position:relative;padding-top:56.25%;}
.vid-frame iframe{position:absolute;inset:0;width:100%;height:100%;border:0;}
.vid-empty{padding:34px 22px;text-align:center;background:var(--surface-sunk);border-bottom:1px solid var(--line);}
.vid-empty b{display:block;font-family:var(--display);font-size:17px;color:var(--ink-2);}
.vid-empty span{display:block;margin-top:5px;font-size:14px;color:var(--ink-4);}
.vid-cap{padding:11px 16px;font-size:13.5px;color:var(--ink-3);}
/* ---- what you walk out with ---- */
.deliv{margin:22px 0 2px;padding:16px 18px;border:1px solid var(--accent2-line);border-left:3px solid var(--accent2);border-radius:var(--radius-sm);background:var(--accent2-tint);}
.deliv b{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent2-deep);display:block;margin-bottom:5px;}
.deliv p{margin:0;color:var(--ink-2);font-size:16px;}
/* ---- authoring scaffold, delete as you fill each page ---- */
.todo{margin:4px 0 12px;padding:15px 17px;border:1px dashed var(--line-2);border-radius:var(--radius-sm);background:repeating-linear-gradient(135deg,var(--ground-2),var(--ground-2) 10px,var(--surface) 10px,var(--surface) 20px);}
.todo b{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-4);display:block;margin-bottom:7px;}
.todo ul{margin:0;padding-left:19px;}
.todo li{color:var(--ink-3);font-size:15px;margin:3px 0;}
/* ---- hub ---- */
.modlist{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:16px;}
.mod{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);padding:22px 24px;box-shadow:var(--shadow-sm);}
.mod-h{display:flex;align-items:baseline;gap:11px;flex-wrap:wrap;margin:0 0 4px;}
.mod-n{font-family:var(--mono);font-size:12px;font-weight:700;letter-spacing:.12em;color:var(--accent-deep);}
.mod-t{font-family:var(--display);font-size:21px;font-weight:700;color:var(--ink);}
.mod-b{margin:0 0 14px;color:var(--ink-3);font-size:15.5px;}
.mod ol{margin:0;padding-left:0;list-style:none;counter-reset:l;}
.mod ol li{counter-increment:l;margin:0;border-top:1px solid var(--line);}
.mod ol li a{display:flex;gap:12px;align-items:baseline;padding:11px 2px;text-decoration:none;color:var(--ink-2);}
.mod ol li a:hover{color:var(--accent-deep);}
.mod ol li a::before{content:counter(l,upper-alpha);font-family:var(--mono);font-size:12px;font-weight:700;color:var(--ink-4);flex:0 0 14px;}
.mod ol li a span{flex:1 1 auto;}
.mod ol li a small{flex:0 0 auto;font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;color:var(--ink-4);text-transform:uppercase;}
.hubnote{margin:30px 0 0;padding:18px 20px;border:1px solid var(--line);border-radius:var(--radius-sm);background:var(--surface-sunk);}
.hubnote h2{margin:0 0 7px;font-family:var(--display);font-size:17px;}
.hubnote p{margin:0 0 8px;font-size:15.5px;}
.hubnote p:last-child{margin:0;}
"""


def esc(s):
    return html.escape(s, quote=False)


# --------------------------------------------------------------- blocks
def p(text):
    return f"<p>{text}</p>"


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def prompt(text, label=None):
    """Something they paste into Jarvis. Long ones get the scroll treatment."""
    body = esc(text)
    if label:
        return (f'<div class="pwrap"><div class="plabel">{esc(label)}</div>'
                f'<button class="copy" onclick="cp(this)">Copy</button>'
                f"<pre>{body}</pre>"
                f'<span class="sfade" aria-hidden="true"></span>'
                f'<span class="shint">SCROLL TO READ IT, OR JUST TAP COPY</span></div>')
    return f'<div class="prompt">{body}</div>'


def script(text, label="ON THE PHONE"):
    """Words they say out loud, not a prompt."""
    return prompt(text, label=label)


def see(text):
    return f'<div class="see"><b>You should see:</b> {text}</div>'


def callout(text):
    return f'<div class="callout">{text}</div>'


def todo(*lines):
    """Authoring scaffold. Every one of these is a page that is not finished."""
    return ('<div class="todo"><b>To fill in</b>'
            + ul([esc(l) for l in lines]) + "</div>")


def step(n, title, blocks, last=False):
    inner = "".join(blocks)
    btn = "Finish this page" if last else "Done, next"
    return (
        '<li><section class="step is-locked">\n'
        '<div class="step-head">\n'
        f'<span class="step-badge" aria-hidden="true">{n}</span>\n'
        f'<div class="step-heading"><h2 class="step-title"><span class="step-n">Step {n:02d}</span>'
        f'<span class="step-title-text">{esc(title)}</span></h2></div>\n'
        '<span class="step-chip is-locked"></span>\n'
        "</div>\n"
        '<p class="step-locked-note" hidden>Finish the step above to unlock this one.</p>\n'
        f'<div class="step-body" hidden>{inner}\n'
        f'<button type="button" class="btn-done" hidden>{btn}</button>\n'
        "</div>\n"
        "</section></li>"
    )


def video(loom, caption):
    if loom:
        m = re.search(r"loom\.com/(?:share|embed)/([0-9a-f]+)", loom)
        src = f"https://www.loom.com/embed/{m.group(1)}" if m else loom
        inner = f'<div class="vid-frame"><iframe src="{src}" allowfullscreen title="Lesson video"></iframe></div>'
    else:
        inner = ('<div class="vid-empty"><b>Video goes here</b>'
                 '<span>Record the session, paste the Loom link into this lesson spec, rebuild.</span></div>')
    return f'<div class="vid">{inner}<div class="vid-cap">{esc(caption)}</div></div>'


# --------------------------------------------------------------- page
def letter(i):
    return chr(ord("A") + i)


def page_file(mod, i):
    return f"{mod['slug']}-{letter(i).lower()}.html"


def render_page(mod, i, pg, nxt):
    head = (SHELL / "head.html").read_text(encoding="utf-8")
    tail = (SHELL / "tail.html").read_text(encoding="utf-8")

    title = f"{mod['num']}: {pg['title']}"
    head = head.replace("{{TITLE}}", esc(title))
    head = head.replace("</style>", EXTRA_CSS + "</style>", 1)
    tail = tail.replace("{{KEY}}", f"ht.{mod['slug']}.{letter(i).lower()}")

    steps = pg["steps"]
    segs = '<span class="segment"></span>' * len(steps)
    steps_html = "\n".join(
        step(j + 1, s[0], s[1], last=(j == len(steps) - 1)) for j, s in enumerate(steps)
    )

    nxt_html = ""
    if nxt:
        nxt_html = f'<a class="next" href="{nxt[0]}">Next: {esc(nxt[1])} &rarr;</a>'

    deliv = ""
    if pg.get("deliverable"):
        deliv = ('<div class="deliv"><b>You walk out of this lesson with</b>'
                 f'<p>{pg["deliverable"]}</p></div>')

    body = f'''<body>
<div class="progress"><div class="progress-inner">
<div class="progress-row">
<div class="progress-lead"><span class="progress-count"><span id="done-count">0</span><span class="progress-of"> of {len(steps)}</span></span>
<span class="progress-title">{esc(mod["num"])} &middot; {letter(i)}: {esc(pg["title"])}</span></div>
</div>
<div class="segments">{segs}</div>
</div></div>
<main class="shell">
<header class="hero">
<div class="eyebrow">{esc(mod["num"])} {esc(mod["name"])} &middot; Lesson {letter(i)}</div>
<h1>{esc(pg["title"])}</h1>
<p class="lede">{pg["lede"]}</p>
{"".join(p(x) for x in pg.get("intro", []))}
{video(pg.get("loom"), pg.get("vidcap", "Blake walks a member through this live."))}
{deliv}
</header>
{pg.get("preamble", "")}
<ol class="steps">

{steps_html}
</ol>

<div class="outro" id="outro">
<div class="finish-badge" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4.5 12.5 9.5 17.5 19.5 6.5"/></svg></div>
<h2 class="finish-title">{esc(pg["finish"][0])}</h2>
<p class="finish-sub">{pg["finish"][1]}</p>
<button type="button" class="cblock-btn">Complete This Lesson</button>
{nxt_html}
</div>
<p class="helpline">Stuck on this lesson? Bring it to the next implementation call, or post it in the members group with a screenshot.</p>
<button type="button" class="startover">Start this lesson over</button>
</main>
'''
    return head + "\n" + body + tail


# --------------------------------------------------------------- hub
def render_hub(modules):
    head = (SHELL / "head.html").read_text(encoding="utf-8")
    head = head.replace("{{TITLE}}", "The High Ticket Course")
    head = head.replace("</style>", EXTRA_CSS + "</style>", 1)

    mods = []
    for mod in modules:
        lessons = []
        for i, pg in enumerate(mod["pages"]):
            done = "" if pg.get("loom") else "<small>to record</small>"
            lessons.append(
                f'<li><a href="{mod["slug"]}/{page_file(mod, i)}">'
                f'<span>{esc(pg["title"])}</span>{done}</a></li>'
            )
        mods.append(
            '<li class="mod">'
            f'<div class="mod-h"><span class="mod-n">{esc(mod["num"]).upper()}</span>'
            f'<span class="mod-t">{esc(mod["name"])}</span></div>'
            f'<p class="mod-b">{mod["blurb"]}</p>'
            "<ol>" + "".join(lessons) + "</ol></li>"
        )

    total = sum(len(m["pages"]) for m in modules)
    body = f'''<body>
<main class="shell">
<header class="hero">
<div class="eyebrow">Members only</div>
<h1>The High Ticket Course</h1>
<p class="lede">Seven modules, {total} lessons. One offer, one acquisition system, one way to close, two ways to deliver. Every lesson ends with something you can use that day.</p>
</header>
<ul class="modlist">
{"".join(mods)}
</ul>
<div class="hubnote">
<h2>How to use this</h2>
<p>Go in order. The offer you build in Module 2 is the thing every other module runs on, so do not skip it to get to the outreach.</p>
<p>The videos are recorded live with members going through their own build, so what you are watching is a real offer and a real pipeline, not a demo account.</p>
<p>Bring your calls, your offer and your builds to the implementation sessions. The useful ones get edited and added here as lessons.</p>
</div>
</main>
</body>
</html>
'''
    return head + "\n" + body


def render_nav(modules):
    rows = []
    for mod in modules:
        items = ",\n      ".join(
            f'[\'/{mod["slug"]}/{page_file(mod, i)}\', {js(pg["title"])}]'
            for i, pg in enumerate(mod["pages"])
        )
        rows.append(f'    [{js(mod["num"])}, {js(mod["name"])}, [\n      {items}]]')
    body = ",\n".join(rows)
    tpl = (ROOT / "shell" / "nav.template.js").read_text(encoding="utf-8")
    return tpl.replace("/*MODULES*/", body)


def js(s):
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"


# --------------------------------------------------------------- run
def main():
    from content import MODULES

    flat = []
    for mod in MODULES:
        for i, pg in enumerate(mod["pages"]):
            flat.append((mod, i, pg))

    OUT.mkdir(exist_ok=True)
    written = 0
    for n, (mod, i, pg) in enumerate(flat):
        nxt = None
        if n + 1 < len(flat):
            nmod, ni, npg = flat[n + 1]
            href = page_file(nmod, ni)
            if nmod is not mod:
                href = f"../{nmod['slug']}/{href}"
            nxt = (href, npg["title"])
        d = OUT / mod["slug"]
        d.mkdir(exist_ok=True)
        (d / page_file(mod, i)).write_text(render_page(mod, i, pg, nxt), encoding="utf-8")
        written += 1

    (OUT / "index.html").write_text(render_hub(MODULES), encoding="utf-8")
    (OUT / "nav.js").write_text(render_nav(MODULES), encoding="utf-8")
    shutil.copy(ROOT / "shell" / "netlify.toml", OUT / "netlify.toml")

    todos = sum(
        (OUT / mod["slug"] / page_file(mod, i)).read_text(encoding="utf-8").count('class="todo"')
        for mod, i, pg in flat
    )
    recorded = sum(1 for mod, i, pg in flat if pg.get("loom"))
    print(f"{len(MODULES)} modules, {written} lessons, {todos} blocks still to fill")
    print(f"videos: {recorded} of {written} recorded")


if __name__ == "__main__":
    main()
