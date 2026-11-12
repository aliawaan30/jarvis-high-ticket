#!/usr/bin/env python3
"""Render a client proposal from proposal.json into one fixed, one page design.
Usage: python3 render_proposal.py proposal.json out.html
Standard library only. Exits with errors (and writes nothing) if a limit is broken.
"""
import json, sys, html, re

LIMITS = {"title": 8, "overview": 60, "problem_text": 25, "build_text": 25,
          "timeline_text": 12, "calc": 70, "next_step": 35}

def words(s): return len(str(s).split())
def e(s): return html.escape(str(s), quote=True)
def money(n, cur):
    n = float(n)
    s = f"{n:,.0f}" if n == int(n) else f"{n:,.2f}"
    sym = {"USD": "$", "AUD": "$", "CAD": "$", "NZD": "$", "GBP": "£", "EUR": "€"}.get(cur, "")
    return f"{sym}{s}" if sym else f"{s} {cur}"

def check(d):
    errs = []
    need = ["agency", "client", "date", "title", "overview", "problems", "build", "timeline", "costs"]
    for k in need:
        if not d.get(k): errs.append(f"missing: {k}")
    if errs: return errs
    if words(d["title"]) > LIMITS["title"]: errs.append("title over 8 words")
    if words(d["overview"]) > LIMITS["overview"]: errs.append("overview over 60 words")
    if not 1 <= len(d["problems"]) <= 2: errs.append("problems: 1 or 2 items")
    for p in d["problems"]:
        if words(p.get("text", "")) > LIMITS["problem_text"]: errs.append(f"problem text over 25 words: {p.get('unit','')}")
    if not 2 <= len(d["build"]) <= 4: errs.append("build: 2 to 4 parts")
    for b in d["build"]:
        if words(b.get("text", "")) > LIMITS["build_text"]: errs.append(f"build text over 25 words: {b.get('name','')}")
    if not 2 <= len(d["timeline"]) <= 4: errs.append("timeline: 2 to 4 stages")
    for t in d["timeline"]:
        if words(t.get("text", "")) > LIMITS["timeline_text"]: errs.append(f"timeline text over 12 words: {t.get('name','')}")
    if d.get("calc") and words(d["calc"]) > LIMITS["calc"]: errs.append("calculation over 70 words")
    c = d["costs"]
    for k in ["build_price", "currency", "payment"]:
        if c.get(k) in (None, ""): errs.append(f"missing costs.{k}")
    if d.get("next_step") and words(d["next_step"]) > LIMITS["next_step"]: errs.append("next step over 35 words")
    txt = json.dumps(d, ensure_ascii=False)
    if "\u2014" in txt or "\u2013" in txt: errs.append("remove em or en dashes")
    if re.search(r"\[(FILL|TBC|TODO)", txt, re.I): errs.append("placeholder left in")
    color = d["agency"].get("brand_color", "#1D4ED8")
    if not re.fullmatch(r"#[0-9A-Fa-f]{6}", color): errs.append("brand_color must be #RRGGBB")
    return errs

def render(d):
    a, cl, c = d["agency"], d["client"], d["costs"]
    cur = c["currency"]; brand = a.get("brand_color", "#1D4ED8")
    logo = (f'<img src="{e(a["logo_url"])}" alt="{e(a["name"])}" style="height:30px;width:auto">'
            if a.get("logo_url") else f'<div class="logo">{e(a["name"][:1].upper())}</div>')
    prepared = f'Prepared for {e(cl["contact_name"])} by {e(d.get("prepared_by", a["name"]))}' if cl.get("contact_name") else f'Prepared by {e(d.get("prepared_by", a["name"]))}'
    facts = "".join(f'<div class="fact"><div class="n">{e(p["number"])}</div><div class="u">{e(p["unit"])}</div><p>{e(p["text"])}</p></div>' for p in d["problems"])
    calc = f'<p class="calc">{e(d["calc"])}</p>' if d.get("calc") else ""
    build = "".join(f'<li><span class="k">{i}</span><p><b>{e(b["name"])}.</b> {e(b["text"])}</p></li>' for i, b in enumerate(d["build"], 1))
    sc = []
    if d.get("connects"): sc.append(f'<b>Connects to</b> {e(d["connects"])}.')
    if d.get("people_decide"): sc.append(f'<b>People still decide</b> {e(d["people_decide"])}.')
    if d.get("not_included"): sc.append(f'<b>Not included</b> {e(d["not_included"])}.')
    scope = f'<p class="scope">{" ".join(sc)}</p>' if sc else ""
    weeks = "".join(f'<div class="wk"><div class="w">{e(t["when"])}</div><b>{e(t["name"])}</b><p>{e(t["text"])}</p></div>' for t in d["timeline"])
    needs = f'<p class="needs">Needed from you: {e(d["needs"])}</p>' if d.get("needs") else ""
    anchor = ""
    pc = d.get("problem_cost_year")
    if pc:
        pct = max(1.5, min(100, float(c["build_price"]) / float(pc) * 100))
        anchor = (f'<div class="anchor" role="img" aria-label="The problem costs about {money(pc,cur)} a year. The build costs {money(c["build_price"],cur)}.">'
                  f'<div class="ar"><div class="v">{money(pc,cur)}<small>a year, the current cost</small></div><div class="bar"><span class="b1" style="flex:1"></span></div></div>'
                  f'<div class="ar"><div class="v">{money(c["build_price"],cur)}<small>once, the build</small></div><div class="bar"><span class="b3" style="width:{pct:.1f}%"></span></div></div></div>')
    rows = f'<tr class="main"><td>Build</td><td>{money(c["build_price"],cur)} {e(cur)}</td></tr><tr><td>Payment</td><td>{e(c["payment"])}</td></tr>'
    if c.get("running_monthly") not in (None, ""):
        rows += f'<tr><td>Running costs{": " + e(c["running_what"]) if c.get("running_what") else ""}</td><td>About {money(c["running_monthly"],cur)} a month</td></tr>'
    if c.get("support"): rows += f'<tr><td>Support</td><td>{e(c["support"])}</td></tr>'
    nxt = f'<p class="next"><b>To proceed:</b> {e(d["next_step"])}</p>' if d.get("next_step") else ""
    foot_l = e(", ".join(x for x in [a["name"], a.get("location", "")] if x))
    foot_r = e(a.get("contact", ""))
    css = CSS.replace("--brand:#1D4ED8", f"--brand:{brand}")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Proposal for {e(cl["business"])}</title>
{FONTS}
<style>{css}</style>
</head>
<body>
<article class="doc">
  <div class="top">
    <div class="agency">{logo}{"" if a.get("logo_url") else e(a["name"])}</div>
    <div class="meta"><b>Proposal for {e(cl["business"])}</b><br>{prepared}<br>{e(d["date"])}</div>
  </div>
  <h1>{e(d["title"])}</h1>
  <p class="lead">{e(d["overview"])}</p>
  <div class="row"><div class="label">The problem<span>and its impact</span></div><div><div class="facts">{facts}</div>{calc}</div></div>
  <div class="row"><div class="label">Proposed build</div><div><ol class="build">{build}</ol>{scope}</div></div>
  <div class="row"><div class="label">Timeline</div><div><div class="weeks" style="grid-template-columns:repeat({len(d["timeline"])},1fr)">{weeks}</div>{needs}</div></div>
  <div class="row"><div class="label">Costs<span>and next step</span></div><div>{anchor}<table class="costs">{rows}</table>{nxt}</div></div>
  <footer><span>{foot_l}</span><span>{foot_r}</span></footer>
</article>
</body>
</html>"""

def main():
    if len(sys.argv) != 3: sys.exit("Usage: python3 render_proposal.py proposal.json out.html")
    d = json.load(open(sys.argv[1], encoding="utf-8"))
    errs = check(d)
    if errs:
        print("NOT RENDERED. Fix these:"); [print(" - " + x) for x in errs]; sys.exit(1)
    open(sys.argv[2], "w", encoding="utf-8").write(render(d))
    print("Rendered " + sys.argv[2])

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap" rel="stylesheet">'
CSS = "\n:root{\n  --brand:#1D4ED8; --brand-soft:#EEF3FE;\n  --ink:#14213D; --ink-2:#4B5568; --ink-3:#8590A2; --line:#E3E7ED; --sunk:#F6F8FB; --bar:#14213D; --bar-2:#AEB8C8;\n  --paper:#FFFFFF; --page:#EDEFF3;\n  --sans:'Hanken Grotesk', Arial, Helvetica, sans-serif; --serif:'Newsreader', Georgia, serif; color-scheme: light;\n}\n*{box-sizing:border-box}\nhtml{height:100%}\nbody{margin:0;background:var(--page);color:var(--ink);font-family:var(--sans);font-size:14px;line-height:1.55;-webkit-font-smoothing:antialiased;\n  padding:max(24px, env(safe-area-inset-top, 0px)) 16px max(40px, env(safe-area-inset-bottom, 0px))}\n.doc{max-width:794px;margin:0 auto;background:var(--paper);padding:52px 60px 40px;border-top:3px solid var(--brand)}\np{margin:0}\n.top{display:flex;justify-content:space-between;align-items:flex-start;gap:16px}\n.agency{display:flex;align-items:center;gap:10px;font-weight:600;font-size:15px}\n.logo{width:30px;height:30px;border-radius:7px;background:var(--brand);color:#fff;display:grid;place-items:center;font-weight:700;font-size:14px}\n.meta{font-size:12.5px;color:var(--ink-3);text-align:right;line-height:1.5}\n.meta b{color:var(--ink);font-weight:600}\nh1{font-family:var(--serif);font-weight:400;font-size:34px;line-height:1.15;letter-spacing:-0.01em;margin:38px 0 12px;max-width:20ch}\n.lead{font-size:15px;color:var(--ink-2);max-width:64ch}\n\n.row{display:grid;grid-template-columns:150px 1fr;gap:28px;padding:22px 0;border-top:1px solid var(--line)}\n.row:first-of-type{margin-top:30px}\n.label{font-size:13px;font-weight:600;color:var(--ink);padding-top:2px}\n.label span{display:block;font-weight:400;color:var(--ink-3);margin-top:2px}\n\n.facts{display:grid;grid-template-columns:1fr 1fr;gap:22px}\n.fact .n{font-family:var(--serif);font-size:30px;line-height:1;color:var(--ink);font-variant-numeric:tabular-nums}\n.fact .u{font-size:12.5px;color:var(--ink-3);margin:4px 0 6px}\n.fact p{color:var(--ink-2)}\n.calc{margin-top:14px;font-size:12.5px;color:var(--ink-2);font-variant-numeric:tabular-nums}\n.calc b{color:var(--ink);font-weight:600}\n\n.build{list-style:none;margin:0;padding:0;display:grid;gap:9px}\n.build li{display:grid;grid-template-columns:22px 1fr;gap:10px}\n.build .k{width:22px;height:22px;border-radius:50%;border:1px solid var(--brand);color:var(--brand);font-size:11.5px;font-weight:600;display:grid;place-items:center;margin-top:1px}\n.build b{font-weight:600;color:var(--ink)}\n.build li p{color:var(--ink-2)}\n.scope{margin-top:12px;font-size:12.5px;color:var(--ink-3)}\n.scope b{color:var(--ink-2);font-weight:600}\n\n.weeks{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}\n.wk{border-top:2px solid var(--line);padding-top:8px}\n.wk:last-child{border-top-color:var(--brand)}\n.wk .w{font-size:12px;color:var(--ink-3)}\n.wk b{display:block;font-weight:600;margin:1px 0 2px}\n.wk p{color:var(--ink-2);font-size:13px}\n.needs{margin-top:12px;font-size:12.5px;color:var(--ink-3)}\n\n.anchor{background:var(--sunk);border-radius:6px;padding:14px 16px;margin-bottom:14px}\n.ar{display:grid;grid-template-columns:118px 1fr;gap:14px;align-items:center}\n.ar + .ar{margin-top:8px}\n.ar .v{font-family:var(--serif);font-size:20px;line-height:1.1;font-variant-numeric:tabular-nums}\n.ar .v small{display:block;font-family:var(--sans);font-size:11.5px;color:var(--ink-3)}\n.bar{height:10px;border-radius:5px;display:flex;overflow:hidden}\n.bar span{display:block;height:100%}\n.b1{background:var(--bar);flex:94}.b2{background:var(--bar-2);flex:20}\n.b3{background:var(--brand);width:6.6%}\n.costs{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums}\n.costs td{padding:7px 0;border-bottom:1px solid var(--line);color:var(--ink-2)}\n.costs td:last-child{text-align:right;color:var(--ink);font-weight:500}\n.costs tr.main td{color:var(--ink);font-weight:600;font-size:15px}\n.next{margin-top:12px;color:var(--ink-2)}\n.next b{color:var(--ink);font-weight:600}\n\nfooter{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:22px;padding-top:12px;border-top:1px solid var(--line);font-size:11.5px;color:var(--ink-3)}\n\n@media (max-width:700px){\n  .doc{padding:30px 22px 28px}\n  h1{font-size:28px}\n  .top{flex-direction:column}.meta{text-align:left}\n  .row{grid-template-columns:1fr;gap:10px}\n  .facts,.weeks{grid-template-columns:1fr}\n  .ar{grid-template-columns:1fr;gap:4px}\n}\n@media print{\n  :root{--brand:#1D4ED8;--ink:#14213D;--ink-2:#4B5568;--ink-3:#8590A2;--line:#E3E7ED;--sunk:#F6F8FB;--bar:#14213D;--bar-2:#AEB8C8;--paper:#fff;--page:#fff}\n  @page{size:A4;margin:0}\n  body{padding:0;background:#fff}\n  .doc{max-width:none;width:210mm;height:296mm;overflow:hidden;padding:10mm 15mm 6mm}\n  body{font-size:12.5px}\n  h1{font-size:27px;margin:16px 0 6px}\n  .lead{font-size:13.5px}\n  .row{padding:11px 0;gap:22px;grid-template-columns:130px 1fr}\n  .row:first-of-type{margin-top:18px}\n  .fact .n{font-size:24px}\n  .calc,.scope,.needs{margin-top:8px}\n  .anchor{padding:10px 14px;margin-bottom:8px}\n  .costs td{padding:5px 0}\n  footer{margin-top:12px}\n  *{-webkit-print-color-adjust:exact;print-color-adjust:exact}\n}\n"

if __name__ == '__main__':
    main()
