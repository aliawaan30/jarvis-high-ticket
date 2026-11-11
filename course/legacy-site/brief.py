#!/usr/bin/env python3
"""Briefing format renderer, the premium layout.

Not a checklist. A briefing: thesis, idea, mechanism, worked example, the work,
the decision. No gating, no progress bar, no confetti. The reader is an
operator, not a beginner being walked across a road.

    python3 brief.py        writes site/preview/<slug>.html
"""
import html, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
OUT = ROOT / "site" / "preview"

CSS = """
:root{
  --paper:#fbfbfc; --surface:#ffffff; --sunk:#f5f5f8;
  --ink:#0e1016; --ink-2:#333945; --ink-3:#69707e; --ink-4:#9aa1ad;
  --rule:#e6e6ec; --rule-2:#d2d2dc;
  --accent:#4b2fc4; --accent-soft:#f1edfd; --accent-line:#cfc2f6;
  --brass:#8a6210; --brass-soft:#fbf4e6; --brass-line:#e7d2a4;
  --display:'Fraunces',Georgia,serif;
  --body:'Instrument Sans',system-ui,-apple-system,sans-serif;
  --mono:'IBM Plex Mono',ui-monospace,SFMono-Regular,Menlo,monospace;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink-2);font-family:var(--body);
  font-size:18px;line-height:1.68;-webkit-font-smoothing:antialiased;}
::selection{background:#e3dafb;color:#2c1a7a}
a{color:var(--accent)}

.wrap{max-width:1140px;margin:0 auto;padding:0 24px 120px;}
.grid{display:block}
@media(min-width:1060px){
  .grid{display:grid;grid-template-columns:200px minmax(0,1fr);gap:56px;align-items:start}
}

/* ---------- masthead ---------- */
.top{border-bottom:1px solid var(--rule);background:var(--surface);}
.top-in{max-width:1140px;margin:0 auto;padding:16px 24px;display:flex;gap:14px;
  align-items:baseline;justify-content:space-between;}
.brandmark{font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--ink-4);text-decoration:none}
.brandmark b{color:var(--ink-2);font-weight:600}
.top a.back{font-family:var(--mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;
  text-decoration:none;color:var(--ink-3)}
.top a.back:hover{color:var(--accent)}

/* ---------- head of the briefing ---------- */
.head{padding:76px 0 0;max-width:720px}
.kicker{font-family:var(--mono);font-size:11.5px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--accent);margin:0 0 20px}
.kicker span{color:var(--ink-4)}
h1{font-family:var(--display);font-weight:600;font-size:clamp(38px,5.6vw,60px);line-height:1.02;
  letter-spacing:-0.02em;color:var(--ink);margin:0 0 26px;text-wrap:balance;
  font-variation-settings:'opsz' 60,'SOFT' 0,'WONK' 1;}
.thesis{font-family:var(--display);font-weight:400;font-size:clamp(21px,2.6vw,26px);line-height:1.38;
  color:var(--ink);margin:0 0 30px;padding:0 0 0 20px;border-left:2px solid var(--accent);
  font-variation-settings:'opsz' 20,'WONK' 1;}
.meta{display:flex;flex-wrap:wrap;gap:8px 20px;font-family:var(--mono);font-size:11.5px;
  letter-spacing:.1em;text-transform:uppercase;color:var(--ink-4);
  border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:13px 0;margin:0 0 8px}
.meta b{font-weight:500;color:var(--ink-3)}

/* ---------- contents rail ---------- */
.rail{margin:40px 0 0}
@media(min-width:1060px){.rail{position:sticky;top:34px;margin:118px 0 0}}
.rail h2{font-family:var(--mono);font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--ink-4);font-weight:500;margin:0 0 14px}
.rail ol{list-style:none;margin:0;padding:0}
.rail li{margin:0 0 2px}
.rail a{display:flex;gap:10px;align-items:baseline;padding:6px 0;text-decoration:none;
  font-size:14.5px;line-height:1.3;color:var(--ink-3);border-top:1px solid var(--rule)}
.rail li:first-child a{border-top:0}
.rail a i{font-style:normal;font-family:var(--mono);font-size:10.5px;color:var(--ink-4);flex:0 0 18px}
.rail a:hover{color:var(--accent)}
.rail a.on{color:var(--ink);font-weight:600}
.rail a.on i{color:var(--accent)}

/* ---------- body ---------- */
.main{max-width:720px}
section.beat{padding:54px 0 0;scroll-margin-top:24px}
.beat-n{font-family:var(--mono);font-size:11.5px;letter-spacing:.2em;text-transform:uppercase;
  color:var(--ink-4);margin:0 0 10px;display:flex;align-items:center;gap:11px}
.beat-n::after{content:'';flex:1;height:1px;background:var(--rule)}
h2.beat-h{font-family:var(--display);font-weight:600;font-size:clamp(26px,3.4vw,34px);line-height:1.12;
  letter-spacing:-0.015em;color:var(--ink);margin:0 0 20px;text-wrap:balance;
  font-variation-settings:'opsz' 36,'WONK' 1}
h3{font-family:var(--body);font-weight:600;font-size:19px;color:var(--ink);margin:30px 0 10px}
p{margin:0 0 19px}
.main>section p:first-of-type{font-size:18px}
strong{color:var(--ink);font-weight:600}
ul,ol.plain{margin:0 0 19px;padding-left:22px}
li{margin:0 0 8px}
.lead{font-size:19.5px;line-height:1.6;color:var(--ink-2)}

/* ---------- framework card ---------- */
.frame{margin:30px 0;border:1px solid var(--rule-2);border-radius:4px;background:var(--surface);
  overflow:hidden}
.frame-h{padding:15px 22px;border-bottom:1px solid var(--rule);background:var(--sunk);
  font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-3)}
.frame-b{padding:6px 22px 8px}
.frame-row{display:flex;gap:18px;padding:16px 0;border-top:1px solid var(--rule)}
.frame-row:first-child{border-top:0}
.frame-row dt{flex:0 0 108px;font-family:var(--display);font-weight:600;font-size:17px;color:var(--ink);
  font-variation-settings:'opsz' 18}
.frame-row dd{margin:0;flex:1 1 auto;font-size:16.5px;line-height:1.55;color:var(--ink-2)}
.frame-row dd em{font-style:normal;display:block;margin-top:4px;color:var(--ink-4);font-size:14.5px}

/* ---------- worked example ---------- */
.work-ex{margin:30px 0;padding:26px 24px;background:var(--surface);border:1px solid var(--rule);
  border-radius:4px}
.work-ex .tag{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--accent);margin:0 0 12px}
.work-ex h3{margin-top:0}
table{width:100%;border-collapse:collapse;margin:18px 0 10px;font-size:16px}
th,td{text-align:left;padding:10px 12px 10px 0;border-bottom:1px solid var(--rule);vertical-align:top}
th{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--ink-4);font-weight:500}
td.n{font-family:var(--mono);font-variant-numeric:tabular-nums;color:var(--ink);text-align:right;
  padding-right:0;white-space:nowrap}
th.n{text-align:right;padding-right:0}
.sum td{border-bottom:0;border-top:2px solid var(--ink);font-weight:600;color:var(--ink);padding-top:12px}

/* ---------- aside ---------- */
.aside{margin:28px 0;padding:18px 20px;border-left:2px solid var(--rule-2);background:transparent}
.aside p{margin:0;font-size:16.5px;color:var(--ink-3)}
.aside p+p{margin-top:12px}
.aside b{color:var(--ink-2)}

/* ---------- the work panel ---------- */
.do{margin:26px 0;border:1px solid var(--rule-2);border-radius:4px;background:var(--surface)}
.do-h{display:flex;gap:12px;align-items:baseline;padding:16px 22px;border-bottom:1px solid var(--rule)}
.do-h b{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--ink-4);font-weight:500}
.do-h span{font-family:var(--display);font-size:18px;font-weight:600;color:var(--ink);
  font-variation-settings:'opsz' 18}
.do-b{padding:20px 22px 22px}
.do-b p:last-child{margin-bottom:0}
.paste{position:relative;margin:16px 0;background:#12131a;border-radius:4px;overflow:hidden}
.paste .plab{display:flex;justify-content:space-between;align-items:center;padding:9px 14px;
  border-bottom:1px solid #23242e;font-family:var(--mono);font-size:10px;letter-spacing:.18em;
  text-transform:uppercase;color:#7f8699}
.paste pre{margin:0;padding:16px 14px;overflow-x:auto;font-family:var(--mono);font-size:13.5px;
  line-height:1.62;color:#d8dbe6;white-space:pre-wrap;word-break:break-word}
.paste button{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  background:#23242e;color:#c3c8d6;border:0;border-radius:3px;padding:5px 11px;cursor:pointer}
.paste button:hover{background:#30323f;color:#fff}
.paste button.did{background:var(--accent);color:#fff}
.expect{margin:16px 0 0;padding:14px 16px;background:var(--sunk);border-radius:4px;font-size:16px;
  color:var(--ink-2)}
.expect b{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--ink-4);display:block;margin-bottom:5px;font-weight:500}

/* ---------- decision ---------- */
.decide{margin:34px 0 0;padding:28px 26px;background:var(--brass-soft);border:1px solid var(--brass-line);
  border-radius:4px}
.decide .tag{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--brass);margin:0 0 12px}
.decide h3{margin-top:0;font-family:var(--display);font-size:22px;font-variation-settings:'opsz' 22}
.decide ol{margin:0;padding-left:22px}
.decide li{color:var(--ink-2);margin-bottom:9px}
.decide li:last-child{margin-bottom:0}

/* ---------- video ---------- */
.session{margin:34px 0;border:1px solid var(--rule);border-radius:4px;overflow:hidden;background:var(--surface)}
.session-h{padding:14px 20px;border-bottom:1px solid var(--rule);font-family:var(--mono);font-size:10.5px;
  letter-spacing:.18em;text-transform:uppercase;color:var(--ink-4)}
.session-f{position:relative;padding-top:56.25%}
.session-f iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.session-c{padding:12px 20px;font-size:15.5px;color:var(--ink-3)}

/* ---------- foot ---------- */
.foot{margin:72px 0 0;padding:28px 0 0;border-top:1px solid var(--rule);display:flex;
  justify-content:space-between;gap:20px;flex-wrap:wrap;align-items:baseline}
.foot a{text-decoration:none;color:var(--ink)}
.foot .nxt b{display:block;font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;
  text-transform:uppercase;color:var(--ink-4);margin-bottom:5px;font-weight:500}
.foot .nxt span{font-family:var(--display);font-size:20px;font-weight:600;
  font-variation-settings:'opsz' 20}
.foot .nxt:hover span{color:var(--accent)}
.foot .ask{font-size:15px;color:var(--ink-4);max-width:300px}
"""

JS = """
(function(){
  document.querySelectorAll('.paste').forEach(function(box){
    var btn=box.querySelector('button'), pre=box.querySelector('pre');
    if(!btn||!pre)return;
    btn.addEventListener('click',function(){
      var t=pre.innerText;
      function ok(){btn.textContent='Copied';btn.classList.add('did');
        setTimeout(function(){btn.textContent='Copy';btn.classList.remove('did');},1800);}
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(ok,function(){});}
      else{var a=document.createElement('textarea');a.value=t;document.body.appendChild(a);a.select();
        try{document.execCommand('copy');ok();}catch(e){}a.remove();}
    });
  });
  var links=[].slice.call(document.querySelectorAll('.rail a'));
  var secs=links.map(function(a){return document.querySelector(a.getAttribute('href'));});
  function mark(){
    var y=window.scrollY+140, cur=0;
    secs.forEach(function(s,i){if(s&&s.offsetTop<=y)cur=i;});
    links.forEach(function(a,i){a.classList.toggle('on',i===cur);});
  }
  window.addEventListener('scroll',mark,{passive:true});mark();
})();
"""


def esc(s):
    return html.escape(s, quote=False)


def paste(text, label="PASTE INTO JARVIS"):
    return (f'<div class="paste"><div class="plab"><span>{esc(label)}</span>'
            f'<button type="button">Copy</button></div>'
            f"<pre>{esc(text)}</pre></div>")


def expect(text):
    return f'<div class="expect"><b>What good looks like</b>{text}</div>'


def render(b):
    beats = b["beats"]
    rail = "".join(
        f'<li><a href="#b{i+1}"><i>{i+1:02d}</i><span>{esc(t)}</span></a></li>'
        for i, (t, _) in enumerate(beats)
    )
    body = "".join(
        f'<section class="beat" id="b{i+1}"><p class="beat-n">{i+1:02d} &middot; {esc(lbl)}</p>{content}</section>'
        for i, (lbl, content) in enumerate(beats)
    )
    session = ""
    if b.get("loom"):
        m = re.search(r"loom\.com/(?:share|embed)/([0-9a-f]+)", b["loom"])
        src = f"https://www.loom.com/embed/{m.group(1)}" if m else b["loom"]
        session = (f'<div class="session"><div class="session-h">Watch it done</div>'
                   f'<div class="session-f"><iframe src="{src}" allowfullscreen title="Session recording"></iframe></div>'
                   f'<div class="session-c">{esc(b.get("loomcap",""))}</div></div>')

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(b['title'])}</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700&family=Instrument+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>{CSS}</style>
</head>
<body>
<div class="top"><div class="top-in">
<a class="brandmark" href="/index.html">The <b>High Ticket</b> Course</a>
<a class="back" href="/index.html">All briefings</a>
</div></div>

<div class="wrap">
<header class="head">
<p class="kicker">{esc(b['module'])} <span>&middot; Briefing {esc(b['letter'])} of {esc(b['of'])}</span></p>
<h1>{esc(b['title'])}</h1>
<p class="thesis">{b['thesis']}</p>
<p class="meta"><span><b>Read</b> {esc(b['read'])}</span><span><b>Work</b> {esc(b['worktime'])}</span><span><b>You leave with</b> {esc(b['leave'])}</span></p>
</header>

<div class="grid">
<nav class="rail">
<h2>In this briefing</h2>
<ol>{rail}</ol>
</nav>

<div class="main">
{body}
{session}
<div class="foot">
<a class="nxt" href="{b['next'][0]}"><b>Next briefing</b><span>{esc(b['next'][1])} &rarr;</span></a>
<p class="ask">Stuck, or want this looked at on your own business? Bring it to the next implementation session.</p>
</div>
</div>
</div>
</div>
<script>{JS}</script>
</body>
</html>
"""


if __name__ == "__main__":
    from content._specimen import BRIEF
    OUT.mkdir(parents=True, exist_ok=True)
    f = OUT / BRIEF["file"]
    f.write_text(render(BRIEF), encoding="utf-8")
    print("wrote", f, f.stat().st_size, "bytes")
