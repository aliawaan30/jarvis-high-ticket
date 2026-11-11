# Generates the four static-ad slides (ads1-ads4): twenty designed 1080x1080 creatives for the worked example (Kestrel Bay
# Resort), each in a realistic Facebook lead-ad frame, with an ad-set chip on top and a "Why it works" flip underneath.
# Every creative is drawn in container-query units (cqw of the image box), so it scales like a real file.
# Facts: source/facts.md only. No returns, no yields, no tenure, no dates, no sold-out claims.
# For a real client: rewrite SETS, the twenty C_* creatives, the cells and HEADS from their facts file, keep every treatment.
import os
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', 'src')
SC = ':is(#ads1,#ads2,#ads3,#ads4)'
css = lambda s: s.replace('@A', SC)

GLOBE = '<svg width="10" height="10" viewBox="0 0 16 16" fill="currentColor"><path d="M8 1a7 7 0 1 0 0 14A7 7 0 0 0 8 1Zm0 1.5c.9 0 2 1.9 2.3 4.2H5.7C6 4.4 7.1 2.5 8 2.5Zm-3.8 4.2H2.7A5.5 5.5 0 0 1 5.6 3a11 11 0 0 0-1.4 3.7Zm0 2.6c.2 1.4.7 2.7 1.4 3.7a5.5 5.5 0 0 1-2.9-3.7h1.5Zm1.5 0h4.6C10 11.6 8.9 13.5 8 13.5s-2-1.9-2.3-4.2Zm6.1 0h1.5a5.5 5.5 0 0 1-2.9 3.7c.7-1 1.2-2.3 1.4-3.7Zm0-2.6a11 11 0 0 0-1.4-3.7 5.5 5.5 0 0 1 2.9 3.7h-1.5Z"/></svg>'
DOTS = '<svg width="15" height="15" viewBox="0 0 20 20" fill="currentColor"><circle cx="4" cy="10" r="1.6"/><circle cx="10" cy="10" r="1.6"/><circle cx="16" cy="10" r="1.6"/></svg><svg width="13" height="13" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4l12 12M16 4L4 16"/></svg>'
LIKE = '<svg viewBox="0 0 16 16"><path d="M8 1.5 6 5H3.2A1.2 1.2 0 0 0 2 6.2v6.6A1.2 1.2 0 0 0 3.2 14h8.3c.6 0 1.1-.4 1.2-1l1.2-5.4c.2-.8-.4-1.6-1.2-1.6H9.3l.4-2.6A1.5 1.5 0 0 0 8 1.5Z"/></svg>'
COMMENT = '<svg viewBox="0 0 16 16"><path d="M8 1.8c-3.6 0-6.5 2.4-6.5 5.4 0 1.7.9 3.2 2.4 4.2l-.6 2.3 2.5-1.3c.7.2 1.4.3 2.2.3 3.6 0 6.5-2.4 6.5-5.5S11.6 1.8 8 1.8Z"/></svg>'
SHARE = '<svg viewBox="0 0 16 16"><path d="M14.5 8 8 2.5v3C4.4 5.9 2.2 8.3 1.5 12c1.6-1.9 3.7-2.8 6.5-2.8v3L14.5 8Z"/></svg>'
ACTIONS = f'<div class="fba"><div>{LIKE}Like</div><div>{COMMENT}Comment</div><div>{SHARE}Share</div></div>'

# brand logos: the stacked mark (≈1.7:1) for most slots, the wide wordmark (≈4.6:1) where a slot is wide and short;
# the partner (operator) logo is white only, so it sits on dark grounds
LOGO_L = '<img class="xa-logo" src="assets/brand-logo-light.png" alt="Kestrel Bay Resort">'
LOGO_D = '<img class="xa-logo" src="assets/brand-logo-dark.png" alt="Kestrel Bay Resort">'
WORD_L = '<img class="xa-wm" src="assets/brand-wordmark-light.png" alt="Kestrel Bay Resort">'
PARTNER_L = '<img class="xa-partner" src="assets/partner-logo-light.png" alt="Tidewater Hospitality">'

# the four always-on ad sets (facts.md) and their chip colours
SETS = {
    'gar': ('The Garden Suite', '#B57A2E'),
    'oce': ('The Ocean Suite', '#13283A'),
    'club': ('The Owners&rsquo; Club', '#2F7F9A'),
    'kxt': ('Kestrel &times; Tidewater', '#6B7F4E'),
}


def frame_top(text):
    return f'''<div class="fbh"><div class="fbav brav"><img src="assets/brand-avatar.png" alt=""></div>
      <div class="fbid"><div class="nm">Kestrel Bay Resort</div><div class="sp">Sponsored &middot; {GLOBE}</div></div>
      <div class="fbx">{DOTS}</div></div>
    <div class="fbt">{text} <span class="mr">&#8230; See more</span></div>'''


def why_back(w, setlabel):
    rows = ''.join(f'<div class="wr"><span>{k}</span><b>{v}</b></div>' for k, v in
                   [('Audience', w['who']), ('Format', w['fmt']), ('Ad set', setlabel), ('Stands apart', w['diff'])])
    return f'''<div class="adback" aria-hidden="true">
      <div class="wk">Why it works</div>
      <div class="wa">{w['angle']}</div>
      <div class="wl">{w['line']}</div>
      {rows}
      <button type="button" class="wback">&larr; Back to the ad</button>
    </div>'''


def chip(n, st, retarget):
    name, col = SETS[st]
    label = (name.replace('The ', '') + ' &middot; warm') if retarget else name
    return label, f'<div class="xa-set" style="--c:{col}"><i></i><span>Ad set &middot; {label}</span><b>{n:02d}<small>/20</small></b></div>'


def cell(n, st, kind, text, creative, hl, cta, why, tag, retarget=False):
    label, top = chip(n, st, retarget)
    return f'''
<div class="adcell xa-cell k-xa-{kind}">
  {top}
  <div class="adflip">
  <div class="fb">
    {frame_top(text)}
    <div class="fbi xa-fbi"><div class="cr xa-cr xa-{kind}">{creative}</div></div>
    <div class="fbl"><div class="lk"><div class="dm">Form on Facebook</div><div class="hl">{hl}</div></div><div class="fbc">{cta}</div></div>
    {ACTIONS}
  </div>
  {why_back(why, label)}
  </div>
  <div class="adtag"><em>&#9679;</em>&ensp;{tag}<button type="button" class="whyb">Why it works &#8635;</button></div>
</div>'''


def carousel(n, st, text, hook, cards, why, tag, retarget=False):
    """hook = (kicker, title, sub, hl, cta); cards = [(img, pos, num, title, sub, hl, cta)] — the last one is the end card."""
    label, top = chip(n, st, retarget)
    k, t, s, hhl, hcta = hook
    cs = f'''<div class="xa-cc hook"><div class="xa-cci"><div class="cn">{k}</div><div class="ct2"><b>{t}</b><span>{s}</span></div>
          <div class="hk-sw">{LOGO_D}<span>Swipe &rarr;</span></div></div>
          <div class="xa-ccf"><div class="hl">{hhl}</div><div class="fbc">{hcta}</div></div></div>'''
    for i, (img, pos, num, title, sub, hl, cta) in enumerate(cards):
        cls = ' end' if i == len(cards) - 1 else ''
        cs += f'''<div class="xa-cc{cls}"><div class="xa-cci"><img src="assets/{img}" alt="" style="object-position:{pos};"><div class="cs"></div>
          <div class="cn">{num}</div><div class="ct2"><b>{title}</b><span>{sub}</span></div></div>
          <div class="xa-ccf"><div class="hl">{hl}</div><div class="fbc">{cta}</div></div></div>'''
    return f'''
<div class="adcell xa-cell k-xa-car">
  {top}
  <div class="adflip">
  <div class="fb">
    {frame_top(text)}
    <div class="xa-car at-start"><div class="xa-car-in">{cs}</div>
      <button type="button" class="xa-prev" aria-label="Previous card">&lsaquo;</button><button type="button" class="xa-next" aria-label="Next card">&rsaquo;</button></div>
    {ACTIONS}
  </div>
  {why_back(why, label)}
  </div>
  <div class="adtag"><em>&#9679;</em>&ensp;{tag}<button type="button" class="whyb">Why it works &#8635;</button></div>
</div>'''


# ─────────────────────────── shared CSS (lives in ads1, scoped to all four pages) ───────────────────────────
SHARED = css('''
  @A .wrap { max-width:1380px; }
  @A .adgrid.xa-grid { grid-template-columns:repeat(5,minmax(0,1fr)); gap:14px; align-items:start; }
  @A .xa-cell { gap:7px; }
  @A .xa-set { display:flex; align-items:center; gap:5px; font-size:8px; letter-spacing:.07em; text-transform:uppercase;
    font-weight:700; color:var(--soft); padding:0 2px; white-space:nowrap; min-width:0; }
  @A .xa-set i { flex:none; width:7px; height:7px; border-radius:50%; background:var(--c); box-shadow:0 0 0 2px rgba(0,0,0,.04); }
  @A .xa-set span { overflow:hidden; text-overflow:ellipsis; }
  @A .xa-set b { margin-left:auto; font-family:'Playfair',serif; font-size:12px; letter-spacing:0; color:var(--ink); font-weight:500; }
  @A .xa-set b small { font-family:'Jost',sans-serif; font-size:8px; color:var(--taupe); margin-left:1px; }
  @A .xa-cell .fbt { min-height:calc(3 * 1.36em + 9px); }
  @A .xa-cell .fbt b { font-weight:600; }
  @A .xa-cell .fbl .dm { font-size:9px; letter-spacing:.02em; }
  @A .xa-cell .fbl .hl { font-size:12px; }
  @A .xa-cell .fba { margin-top:0; }
  @A .fbav.brav { background:#fff; }
  @A .fbav.brav img { object-fit:cover; transform:none; }
  @A .xa-cell .adback .wr b { font-size:11.5px; }
  @A .xa-cell .adback .wl { font-size:13px; }
  /* the legend of ad sets */
  @A .xa-legend { display:flex; flex-wrap:wrap; justify-content:center; gap:8px 18px; margin:18px auto 0; font-size:9.5px;
    letter-spacing:.14em; text-transform:uppercase; font-weight:700; color:var(--soft); }
  @A .xa-legend span { display:inline-flex; align-items:center; gap:7px; }
  @A .xa-legend i { width:8px; height:8px; border-radius:50%; background:var(--c); }
  @A .xa-legend .lw { color:var(--taupe); font-weight:600; }
  /* the canvas every creative is drawn on */
  @A .xa-fbi { container-type:inline-size; background:#13283A; }
  @A .xa-cr { overflow:hidden; color:#fff; line-height:1.2; font-family:'Jost',sans-serif; }
  @A .xa-cr * { box-sizing:border-box; }
  @A .xa-cr .xa-ph { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }
  @A .xa-cr .xa-logo { display:block; height:auto; width:22cqw; }
  @A .xa-cr .xa-wm { display:block; height:auto; width:34cqw; }
  @A .xa-cr .xa-partner { display:block; height:auto; width:16cqw; }
  @A .xa-cr .xa-eb { font-size:3cqw; letter-spacing:.2em; text-transform:uppercase; font-weight:700; line-height:1.3; }
  @A .xa-cr .xa-ai { position:absolute; font-size:2cqw; letter-spacing:.14em; text-transform:uppercase; font-weight:600; color:rgba(255,255,255,.72); }
  @A .xa-cr em { font-style:italic; }
  /* the carousel */
  @A .xa-car { position:relative; background:#fff; padding-bottom:10px; }
  @A .xa-car-in { display:flex; gap:6px; overflow-x:auto; scroll-snap-type:x mandatory; padding:0 11px; scrollbar-width:none; scroll-behavior:smooth; }
  @A .xa-car-in::-webkit-scrollbar { display:none; }
  @A .xa-cc { flex:0 0 78%; scroll-snap-align:start; border:1px solid #E4E6EB; border-radius:8px; overflow:hidden; background:#fff; }
  @A .xa-cci { position:relative; aspect-ratio:1/1; overflow:hidden; container-type:inline-size; background:#13283A; color:#fff; font-family:'Jost',sans-serif; }
  @A .xa-cci img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }
  @A .xa-cci .cs { position:absolute; inset:0; background:linear-gradient(180deg,rgba(10,22,32,.55) 0%,rgba(10,22,32,0) 34%,rgba(10,22,32,.15) 55%,rgba(10,22,32,.88) 100%); }
  @A .xa-cci .cn { position:absolute; left:7cqw; top:5cqw; font-family:'Anton',sans-serif; font-size:24cqw; line-height:1; color:var(--gold-lite); letter-spacing:.01em; }
  @A .xa-cci .ct2 { position:absolute; left:7cqw; right:7cqw; bottom:7cqw; }
  @A .xa-cci .ct2 b { display:block; font-family:'Playfair',serif; font-weight:500; font-size:10.5cqw; line-height:1.05; }
  @A .xa-cci .ct2 span { display:block; font-size:4.6cqw; line-height:1.35; margin-top:2.4cqw; color:rgba(255,255,255,.9); }
  @A .xa-cc.hook .xa-cci { background:#FBF7F0; color:#13283A; }
  @A .xa-cc.hook .cn { font-family:'Jost',sans-serif; font-size:4.6cqw; letter-spacing:.22em; text-transform:uppercase; font-weight:700; color:var(--gold-d); top:9cqw; }
  @A .xa-cc.hook .ct2 { top:19cqw; bottom:auto; }
  @A .xa-cc.hook .ct2 b { font-size:10cqw; }
  @A .xa-cc.hook .ct2 b em { color:var(--gold-d); }
  @A .xa-cc.hook .ct2 span { color:#5A5249; font-size:5cqw; }
  @A .xa-cc.hook .hk-sw { position:absolute; left:7cqw; right:7cqw; bottom:7cqw; display:flex; align-items:center; justify-content:space-between;
    font-size:4.6cqw; letter-spacing:.18em; text-transform:uppercase; font-weight:700; }
  @A .xa-cc.hook .hk-sw img { width:27cqw; height:auto; position:static; }
  @A .xa-cc.end .cn { font-size:5cqw; font-family:'Jost',sans-serif; letter-spacing:.2em; text-transform:uppercase; font-weight:700; top:8cqw; }
  @A .xa-ccf { display:flex; align-items:center; gap:6px; padding:7px 9px; background:#F0F2F5; }
  @A .xa-ccf .hl { flex:1; min-width:0; font-size:11px; font-weight:600; line-height:1.25; }
  @A .xa-ccf .fbc { font-size:10px; padding:6px 9px; }
  @A .xa-car .xa-prev, @A .xa-car .xa-next { position:absolute; top:38%; width:28px; height:28px; border-radius:50%; border:0; z-index:3; cursor:pointer;
    background:rgba(255,255,255,.95); box-shadow:0 2px 8px rgba(0,0,0,.25); font-size:18px; line-height:26px; color:#13283A; }
  @A .xa-car .xa-prev { left:5px; } @A .xa-car .xa-next { right:5px; }
  @A .xa-car .xa-prev, @A .xa-car .xa-next { transition:opacity .25s; }
  @A .xa-car.at-start .xa-prev, @A .xa-car.at-end .xa-next { opacity:0; pointer-events:none; }
  @media print {
    @A .wrap { zoom:.86 !important; }
    @A .head { margin-bottom:14px !important; }
    @A .adgrid.xa-grid { grid-template-columns:repeat(5,minmax(0,1fr)) !important; gap:12px !important; }
    @A .xa-car .xa-prev, @A .xa-car .xa-next { display:none !important; }
    @A .xa-car-in { overflow:hidden !important; }
  }
  @media screen and (max-width:1180px){ @A .adgrid.xa-grid { grid-template-columns:repeat(3,minmax(0,1fr)); } }
  @media screen and (max-width:760px){ @A .adgrid.xa-grid { grid-template-columns:repeat(2,minmax(0,1fr)); } }
  @media screen and (max-width:560px){ @A .adgrid.xa-grid { grid-template-columns:minmax(0,1fr); max-width:420px; margin:0 auto; } }
''')

# ─────────────────────────── the twenty creatives ───────────────────────────
K = {}   # kind -> css

# ═══ ANGLE ONE · own a suite at Kestrel Bay ═══

# 01 · editorial magazine cover — own a suite in Bali, run by the operator ─────
K['mag'] = '''
  @A .xa-mag .xa-ph { object-position:50% 62%; }
  @A .xa-mag .m-sc { position:absolute; inset:0; background:linear-gradient(90deg,rgba(10,22,32,.72) 0%,rgba(10,22,32,.4) 48%,rgba(10,22,32,0) 72%),
    linear-gradient(180deg,rgba(10,22,32,.82) 0%,rgba(10,22,32,.5) 24%,rgba(10,22,32,.2) 42%,rgba(10,22,32,.34) 56%,rgba(10,22,32,.94) 100%); }
  @A .xa-mag .m-top { position:absolute; left:5cqw; right:5cqw; top:5cqw; }
  @A .xa-mag .m-top .xa-wm { width:62cqw; margin:0 auto; }
  @A .xa-mag .m-iss { display:flex; justify-content:space-between; border-top:.35cqw solid rgba(255,255,255,.7); margin-top:2.6cqw; padding-top:1.4cqw;
    font-size:2.6cqw; letter-spacing:.2em; text-transform:uppercase; font-weight:600; }
  @A .xa-mag .m-lines { position:absolute; left:5cqw; top:29cqw; width:56cqw; display:grid; gap:2cqw; }
  @A .xa-mag .m-lines div { font-family:'Playfair',serif; font-size:4.3cqw; line-height:1.1; padding-left:2.4cqw; border-left:.55cqw solid var(--gold-lite);
    text-shadow:0 .3cqw 2cqw rgba(0,0,0,.65); }
  @A .xa-mag .m-lines small { display:block; font-family:'Jost',sans-serif; font-size:2.5cqw; letter-spacing:.2em; text-transform:uppercase; font-weight:700; color:var(--gold-lite); margin-bottom:.5cqw; }
  @A .xa-mag .m-cov { position:absolute; left:5cqw; right:5cqw; bottom:4.6cqw; }
  @A .xa-mag .m-cov .xa-eb { color:var(--gold-lite); }
  @A .xa-mag .m-hd { font-family:'Playfair',serif; font-weight:500; font-size:7.6cqw; line-height:1.05; margin-top:1.2cqw; }
  @A .xa-mag .m-hd em { color:var(--gold-lite); }
  @A .xa-mag .m-cta { display:flex; justify-content:space-between; font-size:2.8cqw; letter-spacing:.16em; text-transform:uppercase; font-weight:700; margin-top:2.6cqw;
    padding-top:1.8cqw; border-top:.3cqw solid rgba(255,255,255,.35); }
'''
C_MAG = ('<img class="xa-ph" src="assets/ph-hero-pool.jpg" alt=""><div class="m-sc"></div>'
         '<div class="m-top">' + WORD_L + '<div class="m-iss"><span>For Australian buyers</span><span>Bali</span></div></div>'
         '<div class="m-lines"><div><small>The suites</small>From US$165,000</div><div><small>The owners</small>The Owners&rsquo; Club</div><div><small>Run by</small>Tidewater Hospitality</div></div>'
         '<div class="m-cov"><div class="xa-eb">Cover story</div><div class="m-hd">Own a suite in Bali. <em>Tidewater runs it.</em></div>'
         '<div class="m-cta"><span>Six questions to enquire</span><span>&rarr;</span></div></div>')

# 02 · the two suites, side by side ─────────────────────────────────────
K['two'] = '''
  @A .xa-two { background:#F4EFE7; color:#13283A; }
  @A .xa-two .w-hd { position:absolute; left:5cqw; right:5cqw; top:4.4cqw; display:flex; align-items:center; justify-content:space-between; gap:3cqw; }
  @A .xa-two .w-hd .xa-eb { color:var(--gold-d); }
  @A .xa-two .w-t { position:absolute; left:5cqw; right:5cqw; top:13cqw; font-family:'Playfair',serif; font-size:6.9cqw; line-height:1; white-space:nowrap; }
  @A .xa-two .w-t em { color:var(--gold-d); }
  @A .xa-two .w-hd .xa-logo { width:13cqw; flex:none; }
  @A .xa-two .w-cols { position:absolute; left:4cqw; right:4cqw; top:24cqw; bottom:4cqw; display:grid; grid-template-columns:1fr 1fr; gap:3cqw; }
  @A .xa-two .w-c { position:relative; border-radius:2cqw; overflow:hidden; background:#fff; box-shadow:0 1cqw 3cqw rgba(19,40,58,.14); display:flex; flex-direction:column; }
  @A .xa-two .w-c.hi { background:#13283A; color:#FBF7F0; }
  @A .xa-two .w-im { height:28cqw; position:relative; flex:none; }
  @A .xa-two .w-im img { width:100%; height:100%; object-fit:cover; display:block; }
  @A .xa-two .w-bd { padding:2.8cqw 3.2cqw 3cqw; display:flex; flex-direction:column; flex:1; }
  @A .xa-two .w-nm { font-size:2.3cqw; letter-spacing:.12em; text-transform:uppercase; font-weight:800; color:var(--gold-d); white-space:nowrap; }
  @A .xa-two .hi .w-nm { color:var(--gold-lite); }
  @A .xa-two .w-pr { font-family:'Playfair',serif; font-size:7cqw; line-height:1; margin-top:1.4cqw; white-space:nowrap; }
  @A .xa-two .w-pr small { font-family:'Jost',sans-serif; font-size:3.2cqw; font-weight:700; letter-spacing:.04em; margin-right:.6cqw; vertical-align:.6cqw; }
  @A .xa-two .w-au { font-size:3cqw; font-weight:600; margin-top:1.1cqw; color:#5A5249; }
  @A .xa-two .hi .w-au { color:rgba(251,247,240,.78); }
  @A .xa-two .w-sp { margin-top:auto; border-top:.25cqw solid rgba(19,40,58,.14); padding-top:1.8cqw; display:grid; gap:1.1cqw; font-size:2.8cqw; line-height:1.2; }
  @A .xa-two .hi .w-sp { border-top-color:rgba(251,247,240,.2); }
  @A .xa-two .w-sp div { display:flex; gap:1.4cqw; }
  @A .xa-two .w-sp div::before { content:''; flex:none; width:1.3cqw; height:1.3cqw; border-radius:50%; background:var(--sand); margin-top:1cqw; }
  @A .xa-two .hi .w-sp div::before { background:var(--gold-lite); }
  @A .xa-two .w-or { position:absolute; left:50%; top:52cqw; transform:translate(-50%,-50%); width:8cqw; height:8cqw; border-radius:50%; background:var(--gold-lite); color:#13283A;
    display:flex; align-items:center; justify-content:center; font-family:'Playfair',serif; font-style:italic; font-size:3.6cqw; z-index:2; box-shadow:0 0 0 .8cqw #F4EFE7; }
'''
C_TWO = ('<div class="w-hd"><div class="xa-eb">The suites &middot; Kestrel Bay</div>' + LOGO_D + '</div><div class="w-t">Two suites. <em>Side by side.</em></div>'
         '<div class="w-cols">'
         '<div class="w-c"><div class="w-im"><img src="assets/ph-suite-a.jpg" alt="" style="object-position:50% 55%"></div><div class="w-bd">'
         '<div class="w-nm">Garden Suite</div><div class="w-pr"><small>US$</small>165,000</div><div class="w-au">from about A$240k</div>'
         '<div class="w-sp"><div>34 m&sup2; &middot; 1 bedroom</div><div>Garden terrace</div><div>The Owners&rsquo; Club</div></div></div></div>'
         '<div class="w-c hi"><div class="w-im"><img src="assets/ph-balcony.jpg" alt="" style="object-position:62% 55%"></div><div class="w-bd">'
         '<div class="w-nm">Ocean Suite</div><div class="w-pr"><small>US$</small>260,000</div><div class="w-au">about A$375k</div>'
         '<div class="w-sp"><div>52 m&sup2; &middot; 1 bedroom</div><div>Balcony with daybed</div><div>Ocean outlook</div></div></div></div>'
         '</div><div class="w-or">or</div>')

# 03 · the Ocean Suite, room by room — prints on linen ────────────────────────
K['prints'] = '''
  @A .xa-prints { background:radial-gradient(120% 90% at 30% 20%,#F6F0E6 0%,#E8DECE 70%,#DDD1BE 100%); color:#13283A; }
  @A .xa-prints .p-hd { position:absolute; left:6cqw; top:6cqw; width:62cqw; }
  @A .xa-prints .p-hd .xa-eb { color:var(--gold-d); }
  @A .xa-prints .p-t { font-family:'Playfair',serif; font-size:8.4cqw; line-height:1.02; margin-top:1.4cqw; }
  @A .xa-prints .p-t em { color:var(--gold-d); }
  @A .xa-prints .pol { position:absolute; background:#fff; padding:1.8cqw 1.8cqw 0; box-shadow:0 1.4cqw 3.4cqw rgba(19,40,58,.28); }
  @A .xa-prints .pol img { display:block; width:100%; aspect-ratio:1/1; object-fit:cover; }
  @A .xa-prints .pol span { display:block; font-family:'Caveat',cursive; font-weight:700; font-size:4.6cqw; line-height:1; padding:1.6cqw 0 2cqw; color:#3A3230; }
  @A .xa-prints .pol.a { left:4cqw; top:36.5cqw; width:34cqw; transform:rotate(-7deg); }
  @A .xa-prints .pol.b { left:33cqw; top:32.5cqw; width:35cqw; transform:rotate(3deg); z-index:2; }
  @A .xa-prints .pol.c { right:4cqw; top:38.5cqw; width:32cqw; transform:rotate(-2deg); }
  @A .xa-prints .p-st { position:absolute; right:5cqw; top:78.4cqw; transform:rotate(-6deg); border:.6cqw solid #13283A; color:#13283A; border-radius:1cqw;
    padding:1.4cqw 2.2cqw 1.2cqw; font-size:2.7cqw; letter-spacing:.16em; text-transform:uppercase; font-weight:800; line-height:1.3; text-align:center; opacity:.85; z-index:3; }
  @A .xa-prints .p-ft { position:absolute; left:0; right:0; bottom:0; background:#13283A; color:#FBF7F0; padding:2.8cqw 5cqw; display:flex; align-items:center; justify-content:space-between; gap:2cqw; font-size:3cqw; z-index:4; }
  @A .xa-prints .p-ft b { color:var(--gold-lite); font-weight:700; }
  @A .xa-prints .p-ft .xa-wm { width:25cqw; flex:none; }
  @A .xa-prints .p-pk { position:absolute; left:6cqw; top:85cqw; font-size:2.2cqw; letter-spacing:.16em; text-transform:uppercase; font-weight:700; color:#8C8173; z-index:3; }
'''
C_PRINTS = ('<div class="p-hd"><div class="xa-eb">The Ocean Suite</div><div class="p-t">52 m&sup2;, <em>room by room.</em></div></div>'
            '<div class="p-st">Interconnecting<br>options</div>'
            '<div class="pol a"><img src="assets/ph-suite-b.jpg" alt="" style="object-position:40% 55%"><span>the bedroom</span></div>'
            '<div class="pol b"><img src="assets/ph-suite-b2.jpg" alt="" style="object-position:50% 55%"><span>the lounge</span></div>'
            '<div class="pol c"><img src="assets/ph-view.jpg" alt="" style="object-position:50% 50%"><span>the outlook</span></div>'
            '<div class="p-pk">Artist&rsquo;s impressions</div>'
            '<div class="p-ft"><span>US$260,000 &middot; <b>about A$375k</b></span>' + WORD_L + '</div>')

# 04 · kids under 12 stay free — four tiles around one fact ──────────────────
K['four'] = '''
  @A .xa-four { background:#FBF7F0; }
  @A .xa-four .f-g { position:absolute; inset:0; display:grid; grid-template-columns:1fr 1fr; grid-template-rows:1fr 1fr; gap:.8cqw; }
  @A .xa-four .f-t { position:relative; overflow:hidden; }
  @A .xa-four .f-t img { width:100%; height:100%; object-fit:cover; }
  @A .xa-four .f-t::after { content:''; position:absolute; inset:0; background:linear-gradient(180deg,rgba(10,22,32,.6) 0%,rgba(10,22,32,0) 42%,rgba(10,22,32,0) 58%,rgba(10,22,32,.6) 100%); }
  @A .xa-four .f-l { position:absolute; z-index:2; text-shadow:0 .2cqw 1.6cqw rgba(0,0,0,.7); }
  @A .xa-four .f-l b { display:block; font-family:'Playfair',serif; font-weight:500; font-size:6.2cqw; line-height:1; }
  @A .xa-four .f-l span { display:block; font-size:2.5cqw; letter-spacing:.18em; text-transform:uppercase; font-weight:700; margin-top:1cqw; color:#fff; }
  @A .xa-four .f-t:nth-child(1) .f-l { left:4cqw; top:4cqw; } @A .xa-four .f-t:nth-child(2) .f-l { right:4cqw; top:4cqw; text-align:right; }
  @A .xa-four .f-t:nth-child(3) .f-l { left:4cqw; bottom:4cqw; } @A .xa-four .f-t:nth-child(4) .f-l { right:4cqw; bottom:4cqw; text-align:right; }
  @A .xa-four .f-c { position:absolute; left:50%; top:50%; width:44cqw; height:44cqw; transform:translate(-50%,-50%); border-radius:50%; background:#FBF7F0; color:#13283A;
    display:flex; flex-direction:column; align-items:center; justify-content:center; text-align:center; box-shadow:0 0 0 .8cqw rgba(251,247,240,.45),0 1.6cqw 4cqw rgba(0,0,0,.35); z-index:3; padding:0 4.4cqw; }
  @A .xa-four .f-c small { font-size:2.4cqw; letter-spacing:.2em; text-transform:uppercase; font-weight:800; color:var(--gold-d); }
  @A .xa-four .f-c b { font-family:'Playfair',serif; font-weight:500; font-size:5.8cqw; line-height:1.04; margin:1.2cqw 0 1.6cqw; }
  @A .xa-four .f-c b em { color:var(--gold-d); }
  @A .xa-four .f-c .xa-logo { width:15cqw; }
'''
C_FOUR = ('<div class="f-g">'
          '<div class="f-t"><img src="assets/ph-kids.jpg" alt="" style="object-position:50% 50%"><div class="f-l"><b>Kids&rsquo; Club</b><span>On site</span></div></div>'
          '<div class="f-t"><img src="assets/ph-family.jpg" alt="" style="object-position:62% 55%"><div class="f-l"><b>Lagoon</b><span>The main pool</span></div></div>'
          '<div class="f-t"><img src="assets/ph-suite-day.jpg" alt="" style="object-position:50% 50%"><div class="f-l"><b>Ocean Suite</b><span>Interconnecting</span></div></div>'
          '<div class="f-t"><img src="assets/ph-dining.jpg" alt="" style="object-position:40% 50%"><div class="f-l"><b>Dining</b><span>Poolside</span></div></div></div>'
          '<div class="f-c"><small>For families</small><b>Kids under 12 <em>stay free.</em></b>' + LOGO_D + '</div>')

# 05 · everything on site — a resort directory sign ──────────────────────────
K['dir'] = '''
  @A .xa-dir .xa-ph { object-position:66% 50%; }
  @A .xa-dir .d-sc { position:absolute; inset:0; background:linear-gradient(90deg,rgba(10,22,32,.6) 0%,rgba(10,22,32,.2) 60%,rgba(10,22,32,.05) 100%); }
  @A .xa-dir .d-pn { position:absolute; left:6cqw; top:5cqw; bottom:5cqw; width:57cqw; background:#13283A; border-radius:2.6cqw; box-shadow:0 2cqw 5cqw rgba(0,0,0,.45);
    padding:4cqw 5cqw 4cqw; display:flex; flex-direction:column; border:.35cqw solid rgba(226,184,114,.6); }
  @A .xa-dir .d-pn .xa-logo { width:19cqw; margin:0 auto; }
  @A .xa-dir .d-k { text-align:center; font-size:2.3cqw; letter-spacing:.24em; text-transform:uppercase; font-weight:700; color:var(--gold-lite); margin-top:1.8cqw; padding-bottom:1.4cqw; border-bottom:.3cqw solid rgba(226,184,114,.45); }
  @A .xa-dir ul { list-style:none; margin:.6cqw 0 0; padding:0; }
  @A .xa-dir li { display:flex; justify-content:space-between; align-items:center; gap:2cqw; font-size:3cqw; line-height:1.2; letter-spacing:.05em; font-weight:500; padding:1.05cqw 0; border-bottom:.2cqw solid rgba(251,247,240,.12); }
  @A .xa-dir li i { font-style:normal; color:var(--gold-lite); font-size:3.4cqw; line-height:1; }
  @A .xa-dir .d-h { margin-top:auto; padding-top:2cqw; font-family:'Playfair',serif; font-size:5cqw; line-height:1.06; }
  @A .xa-dir .d-h em { color:var(--gold-lite); }
  @A .xa-dir .xa-ai { right:4cqw; bottom:4cqw; }
'''
C_DIR = ('<img class="xa-ph" src="assets/ph-wellness.jpg" alt=""><div class="d-sc"></div>'
         '<div class="d-pn">' + LOGO_L + '<div class="d-k">On site</div><ul>'
         '<li>Lagoon pool<i>&rarr;</i></li><li>Adults&rsquo; pool<i>&rarr;</i></li><li>Kids&rsquo; club<i>&rarr;</i></li>'
         '<li>Spa<i>&rarr;</i></li><li>Gym &amp; yoga deck<i>&rarr;</i></li><li>Poolside dining<i>&rarr;</i></li>'
         '<li>Beach-club access<i>&rarr;</i></li></ul>'
         '<div class="d-h">All at the resort. <em>Suites from US$165,000.</em></div></div>'
         '<div class="xa-ai">Spa &middot; artist&rsquo;s impression</div>')

# ═══ ANGLE TWO · the doubts that stop a sale ═══

# 06 · the big number — US$165,000 in Australian dollars ───────────────────
K['num'] = '''
  @A .xa-num { background:#FBF7F0; color:#13283A; }
  @A .xa-num .u-top { position:absolute; left:6cqw; right:6cqw; top:6cqw; }
  @A .xa-num .u-top .xa-eb { color:var(--gold-d); display:flex; justify-content:space-between; }
  @A .xa-num .u-pre { font-family:'Playfair',serif; font-size:5.4cqw; line-height:1.1; margin-top:2.4cqw; }
  @A .xa-num .u-pre em { color:var(--gold-d); }
  @A .xa-num .u-n { font-family:'Anton',sans-serif; font-size:19.5cqw; line-height:1; letter-spacing:-.005em; margin-top:.6cqw; white-space:nowrap; }
  @A .xa-num .u-src { font-size:2.4cqw; letter-spacing:.12em; text-transform:uppercase; color:#8C8173; font-weight:600; margin-top:1.4cqw; }
  @A .xa-num .u-ph { position:absolute; left:0; right:0; bottom:0; height:42cqw; overflow:hidden; }
  @A .xa-num .u-ph img { width:100%; height:100%; object-fit:cover; object-position:50% 62%; }
  @A .xa-num .u-ph::after { content:''; position:absolute; inset:0; background:linear-gradient(180deg,rgba(10,22,32,.1) 0%,rgba(10,22,32,.62) 34%,rgba(10,22,32,.93) 100%); }
  @A .xa-num .u-sp { position:absolute; left:6cqw; right:6cqw; top:46cqw; display:grid; grid-template-columns:repeat(3,auto); justify-content:space-between; border-top:.3cqw solid rgba(19,40,58,.16); padding-top:2cqw;
    font-size:2.6cqw; letter-spacing:.14em; text-transform:uppercase; font-weight:700; color:#5A5249; }
  @A .xa-num .u-q { position:absolute; left:6cqw; right:6cqw; bottom:5.4cqw; z-index:2; color:#fff; display:flex; align-items:flex-end; justify-content:space-between; gap:3cqw; }
  @A .xa-num .u-q div { font-family:'Playfair',serif; font-size:6.6cqw; line-height:1.06; text-shadow:0 .3cqw 2cqw rgba(0,0,0,.6); }
  @A .xa-num .u-q div em { color:var(--gold-lite); }
  @A .xa-num .u-q span { flex:none; background:var(--gold-lite); color:#13283A; border-radius:10cqw; padding:1.8cqw 3cqw 1.6cqw; font-size:2.8cqw; letter-spacing:.12em; text-transform:uppercase; font-weight:800; }
  @A .xa-num .u-lg { position:absolute; right:6cqw; top:6cqw; z-index:2; }
  @A .xa-num .u-lg .xa-logo { width:17cqw; }
'''
C_NUM = ('<div class="u-top"><div class="xa-eb"><span>The Garden Suite</span></div>'
         '<div class="u-pre">US$165,000 is <em>about</em></div>'
         '<div class="u-n" data-to="240000" data-pre="A$">A$240,000</div><div class="u-src">At 0.69 US$ per A$ &middot; approximate</div></div>'
         '<div class="u-lg">' + LOGO_D + '</div>'
         '<div class="u-sp"><span>34 m&sup2;</span><span>1 bedroom</span><span>Garden terrace</span></div>'
         '<div class="u-ph"><img src="assets/ph-suite-a2.jpg" alt=""></div>'
         '<div class="u-q"><div>Priced in US dollars. <em>Here it is in yours.</em></div><span>Ask us</span></div>')

# 07 · the pictogram — 600+ units delivered (one house = 20 units) ─────────────
UNIT = '<svg viewBox="0 0 40 44"><path d="M20 2 38 16v26H25V30H15v12H2V16Z"/></svg>'
K['pict'] = '''
  @A .xa-pict { background:#F4EFE7; color:#13283A; }
  @A .xa-pict .i-top { position:absolute; left:6cqw; right:6cqw; top:6cqw; }
  @A .xa-pict .i-top .xa-eb { color:var(--gold-d); display:flex; justify-content:space-between; }
  @A .xa-pict .i-row { display:flex; gap:3cqw; margin-top:2.6cqw; align-items:center; }
  @A .xa-pict .i-units { display:grid; grid-template-columns:repeat(10,1fr); gap:1.2cqw 1cqw; width:46cqw; flex:none; }
  @A .xa-pict .i-units svg { width:100%; height:auto; fill:#B57A2E; }
  @A .xa-pict .i-units svg:nth-child(3n) { fill:#C99A57; } @A .xa-pict .i-units svg:nth-child(5n) { fill:#13283A; }
  @A .xa-pict .i-n { margin-left:auto; font-family:'Playfair',serif; font-size:16cqw; line-height:.86; color:#13283A; white-space:nowrap; }
  @A .xa-pict .i-l { font-family:'Playfair',serif; font-size:5.2cqw; line-height:1.08; margin-top:2.4cqw; white-space:nowrap; }
  @A .xa-pict .i-l em { color:var(--gold-d); }
  @A .xa-pict .i-st { display:grid; grid-template-columns:repeat(2,1fr); margin-top:2.6cqw; border-top:.3cqw solid rgba(19,40,58,.18); }
  @A .xa-pict .i-st div { padding:1.8cqw 0 0 2cqw; border-left:.3cqw solid rgba(19,40,58,.12); font-family:'Playfair',serif; font-size:5.4cqw; line-height:1; }
  @A .xa-pict .i-st div:first-child { border-left:0; padding-left:0; }
  @A .xa-pict .i-st small { display:block; font-family:'Jost',sans-serif; font-size:2.2cqw; letter-spacing:.12em; text-transform:uppercase; font-weight:700; color:#8C8173; margin-top:1cqw; line-height:1.25; }
  @A .xa-pict .i-ph { position:absolute; left:0; right:0; bottom:0; height:29cqw; overflow:hidden; }
  @A .xa-pict .i-ph img { width:100%; height:100%; object-fit:cover; object-position:50% 30%; }
  @A .xa-pict .i-ph::after { content:''; position:absolute; inset:0; background:linear-gradient(90deg,rgba(10,22,32,.92) 0%,rgba(10,22,32,.7) 55%,rgba(10,22,32,.45) 100%); }
  @A .xa-pict .i-bt { position:absolute; left:6cqw; right:6cqw; bottom:4.6cqw; z-index:2; color:#fff; display:flex; justify-content:space-between; align-items:flex-end; gap:3cqw; }
  @A .xa-pict .i-bt div { font-family:'Playfair',serif; font-size:5.4cqw; line-height:1.1; }
  @A .xa-pict .i-bt div em { color:var(--gold-lite); }
  @A .xa-pict .i-lk { display:flex; flex-direction:column; align-items:flex-end; gap:1.6cqw; flex:none; }
  @A .xa-pict .i-lk .xa-logo { width:17cqw; }
'''
C_PICT = ('<div class="i-top"><div class="xa-eb"><span>Who builds it</span><span>Kestrel Developments</span></div>'
          '<div class="i-row"><div class="i-units">' + UNIT * 30 + '</div><div class="i-n">600+</div></div>'
          '<div class="i-l">units delivered <em>by Kestrel.</em></div>'
          '<div class="i-st"><div>18<small>Years building resorts</small></div><div>9<small>Developments</small></div></div></div>'
          '<div class="i-ph"><img src="assets/ph-team-signing.jpg" alt=""></div>'
          '<div class="i-bt"><div>The developer <em>behind the resort.</em></div><div class="i-lk">' + LOGO_L + '</div></div>')

# 08 · myth vs fact — who runs it while you're in Australia ────────────────
K['myth'] = '''
  @A .xa-myth .xa-ph { height:66%; object-position:50% 50%; }
  @A .xa-myth .y-sc { position:absolute; inset:0; background:linear-gradient(180deg,rgba(10,22,32,.86) 0%,rgba(10,22,32,.72) 36%,rgba(10,22,32,.3) 62%); }
  @A .xa-myth .y-m { position:absolute; left:6cqw; right:12cqw; top:7cqw; }
  @A .xa-myth .y-stp { display:inline-block; border:.6cqw solid #E5483F; color:#FF6A5F; padding:1cqw 2.4cqw .8cqw; font-family:'Anton',sans-serif; font-size:5cqw;
    letter-spacing:.14em; transform:rotate(-6deg); border-radius:.8cqw; }
  @A .xa-myth .y-mt { font-family:'Playfair',serif; font-size:7.4cqw; line-height:1.08; margin-top:3cqw; text-decoration:line-through; text-decoration-color:#E5483F;
    text-decoration-thickness:.6cqw; text-shadow:0 .3cqw 2cqw rgba(0,0,0,.5); }
  @A .xa-myth .y-f { position:absolute; inset:0; background:#FBF7F0; clip-path:polygon(0 58%,100% 40%,100% 100%,0 100%); }
  @A .xa-myth .y-fb { position:absolute; left:6cqw; right:6cqw; bottom:5.4cqw; color:#13283A; }
  @A .xa-myth .y-fl { display:inline-flex; align-items:center; gap:1.4cqw; background:#13283A; color:var(--gold-lite); font-family:'Anton',sans-serif; font-size:4.4cqw;
    letter-spacing:.16em; padding:1cqw 2.6cqw .8cqw; border-radius:.8cqw; }
  @A .xa-myth .y-ft { font-family:'Playfair',serif; font-size:6.4cqw; line-height:1.1; margin-top:2.4cqw; }
  @A .xa-myth .y-ft em { color:var(--gold-d); }
  @A .xa-myth .y-fs { display:flex; justify-content:space-between; align-items:center; gap:3cqw; margin-top:2.6cqw; font-size:2.7cqw; letter-spacing:.14em; text-transform:uppercase; font-weight:700; color:#5A5249; }
  @A .xa-myth .y-fs .xa-logo { width:18cqw; flex:none; }
'''
C_MYTH = ('<img class="xa-ph" src="assets/ph-venue-2.jpg" alt=""><div class="y-sc"></div>'
          '<div class="y-m"><span class="y-stp">MYTH</span><div class="y-mt">&ldquo;I&rsquo;d have to run it myself, from Australia.&rdquo;</div></div>'
          '<div class="y-f"></div>'
          '<div class="y-fb"><span class="y-fl">FACT</span><div class="y-ft">Tidewater Hospitality runs the resort, <em>day to day.</em></div>'
          '<div class="y-fs"><span>12 venues &middot; close to 900,000 guests a year</span>' + LOGO_D + '</div></div>')

# 09 · the chat — returns, answered on a private call ──────────────────────
K['chat'] = '''
  @A .xa-chat { background:#EFE9E1; color:#111; font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;
    background-image:radial-gradient(rgba(19,40,58,.05) 12%,transparent 13%); background-size:4cqw 4cqw; }
  @A .xa-chat .h-bar { position:absolute; left:0; right:0; top:0; height:14cqw; background:#FBF9F6; border-bottom:.3cqw solid #E2DCD3; display:flex; align-items:center; gap:2.4cqw; padding:0 4.4cqw; }
  @A .xa-chat .h-bk { font-size:6cqw; color:#8C8173; line-height:1; }
  @A .xa-chat .h-av { width:8.6cqw; height:8.6cqw; border-radius:50%; overflow:hidden; background:#fff; border:.25cqw solid #E2DCD3; flex:none; }
  @A .xa-chat .h-av img { width:100%; height:100%; object-fit:cover; display:block; }
  @A .xa-chat .h-nm { font-size:3.7cqw; font-weight:700; line-height:1.15; }
  @A .xa-chat .h-nm small { display:block; font-size:2.6cqw; font-weight:400; color:#2E8B57; }
  @A .xa-chat .h-ms { position:absolute; left:4.6cqw; right:4.6cqw; top:16cqw; display:flex; flex-direction:column; gap:1.5cqw; }
  @A .xa-chat .h-day { align-self:center; background:#FBF9F6; border-radius:2cqw; padding:.8cqw 2.4cqw; font-size:2.4cqw; color:#8C8173; font-weight:600; letter-spacing:.04em; }
  @A .xa-chat .h-b { max-width:80%; border-radius:3cqw; padding:1.4cqw 2.6cqw 1.3cqw; font-size:3.1cqw; line-height:1.26; box-shadow:0 .3cqw .6cqw rgba(0,0,0,.08); }
  @A .xa-chat .h-b.me { align-self:flex-end; background:#D9EEDB; border-bottom-right-radius:.8cqw; }
  @A .xa-chat .h-b.us { align-self:flex-start; background:#fff; border-bottom-left-radius:.8cqw; }
  @A .xa-chat .h-b small { float:right; font-size:2.2cqw; color:#7A6E60; margin:1.1cqw 0 0 2.4cqw; }
  @A .xa-chat .h-b small i { font-style:normal; color:#3C9BD6; letter-spacing:-.2em; margin-left:.8cqw; }
  @A .xa-chat .h-pn { position:absolute; left:0; right:0; bottom:0; height:29cqw; background:#13283A; color:#FBF7F0; padding:3.6cqw 5.6cqw; font-family:'Jost',sans-serif;
    display:flex; align-items:center; justify-content:space-between; gap:4cqw; }
  @A .xa-chat .h-pn::before { content:''; position:absolute; left:0; right:0; top:-6cqw; height:6cqw; background:linear-gradient(180deg,rgba(19,40,58,0),rgba(19,40,58,.3)); }
  @A .xa-chat .h-t { font-family:'Playfair',serif; font-size:6.4cqw; line-height:1.05; }
  @A .xa-chat .h-t em { color:var(--gold-lite); }
  @A .xa-chat .h-s { margin-top:1.8cqw; font-size:2.9cqw; line-height:1.35; color:rgba(251,247,240,.82); }
  @A .xa-chat .h-pn .xa-logo { width:17cqw; flex:none; }
'''
C_CHAT = ('<div class="h-bar"><span class="h-bk">&lsaquo;</span><span class="h-av"><img src="assets/brand-avatar.png" alt=""></span>'
          '<div class="h-nm">Kestrel Bay Resort &middot; Sales<small>online</small></div></div>'
          '<div class="h-ms"><span class="h-day">Today</span>'
          '<div class="h-b me">Hi! What returns do the Ocean Suites make?<small>9:14<i>&#10003;&#10003;</i></small></div>'
          '<div class="h-b us">Good question. We go through returns on a private call, with the numbers in front of you.<small>9:16</small></div>'
          '<div class="h-b me">Great. Can we do Thursday?<small>9:17<i>&#10003;&#10003;</i></small></div>'
          '<div class="h-b us">Thursday works. We&rsquo;ll send you a time.<small>9:18</small></div></div>'
          '<div class="h-pn"><div><div class="h-t">Returns? <em>Explained on a private call.</em></div>'
          '<div class="h-s">Asked and answered one to one, by our sales team.</div></div>' + LOGO_L + '</div>')

# 10 · the buyer file — buying off-plan: what the buyer is choosing between ───
K['file'] = '''
  @A .xa-file { background:radial-gradient(120% 90% at 75% 8%,#24445E 0%,#13283A 55%,#0C1B28 100%); }
  @A .xa-file .fl-hd { position:absolute; left:6cqw; right:6cqw; top:5.4cqw; display:flex; justify-content:space-between; align-items:flex-start; gap:3cqw; }
  @A .xa-file .fl-hd .xa-eb { color:var(--gold-lite); }
  @A .xa-file .fl-t { font-family:'Playfair',serif; font-size:7.4cqw; line-height:1.04; margin-top:1.2cqw; }
  @A .xa-file .fl-t em { color:var(--gold-lite); }
  @A .xa-file .fl-lk { flex:none; display:flex; flex-direction:column; align-items:center; gap:1.2cqw; padding-top:.6cqw; }
  @A .xa-file .fl-lk .xa-logo { width:17cqw; }
  @A .xa-file .fl-lk .xa-partner { width:15cqw; }
  @A .xa-file .fl-lk span { font-size:2.6cqw; color:var(--gold-lite); font-weight:600; line-height:1; }
  @A .xa-file .fl-fd { position:absolute; left:7cqw; right:7cqw; top:33cqw; bottom:5cqw; transform:rotate(-2deg); }
  @A .xa-file .fl-tabs { display:flex; gap:1.2cqw; padding-left:3cqw; }
  @A .xa-file .fl-tabs span { background:#D3B077; color:#5B4220; border-radius:1.6cqw 1.6cqw 0 0; padding:1.5cqw 3cqw 1.1cqw; font-size:2.4cqw; letter-spacing:.14em; text-transform:uppercase; font-weight:800; }
  @A .xa-file .fl-tabs span.on { background:#E6C890; }
  @A .xa-file .fl-bd { position:absolute; left:0; right:0; top:5.2cqw; bottom:0; background:linear-gradient(180deg,#E6C890,#DBBA80); border-radius:0 1.6cqw 1.6cqw 1.6cqw;
    box-shadow:0 2cqw 5cqw rgba(0,0,0,.5); padding:4cqw 5cqw; color:#3B2A14; }
  @A .xa-file .fl-lb { display:inline-block; background:#FEFDFB; border:.25cqw solid rgba(59,42,20,.25); padding:1cqw 2cqw; font-family:'Space Mono',monospace; font-weight:700; font-size:2.3cqw; letter-spacing:.04em; color:#3B2A14; }
  @A .xa-file .fl-h { font-family:'Playfair',serif; font-size:5.2cqw; line-height:1.08; margin-top:2.4cqw; color:#13283A; }
  @A .xa-file ul { list-style:none; margin:2.6cqw 0 0; padding:0; display:grid; gap:1.5cqw; width:44cqw; }
  @A .xa-file .fl-h em { color:#9A6420; }
  @A .xa-file li { display:flex; align-items:center; gap:2cqw; font-size:3.3cqw; font-weight:600; color:#2B2010; }
  @A .xa-file li::before { content:'\\2713'; flex:none; width:4cqw; height:4cqw; border-radius:50%; background:#13283A; color:var(--gold-lite); font-size:2.4cqw; font-weight:800;
    display:flex; align-items:center; justify-content:center; }
  @A .xa-file .fl-ph { position:absolute; right:4.4cqw; bottom:4.6cqw; width:28cqw; background:#fff; padding:1.2cqw 1.2cqw 3.4cqw; transform:rotate(5deg); box-shadow:0 1cqw 2.4cqw rgba(0,0,0,.3); }
  @A .xa-file .fl-ph img { display:block; width:100%; aspect-ratio:4/3; object-fit:cover; }
  @A .xa-file .fl-ph span { position:absolute; left:1.2cqw; right:1.2cqw; bottom:.9cqw; font-family:'Caveat',cursive; font-weight:700; font-size:3.4cqw; color:#3A3230; line-height:1; }
  @A .xa-file .fl-ph::before { content:''; position:absolute; left:4cqw; top:-2.4cqw; width:3cqw; height:8cqw; border:.5cqw solid #9AA3AA; border-radius:2cqw; z-index:2; }
'''
C_FILE = ('<div class="fl-hd"><div><div class="xa-eb">From Australia</div><div class="fl-t">Buying <em>off-plan?</em></div></div>'
          '<div class="fl-lk">' + LOGO_L + '<span>&times;</span>' + PARTNER_L + '</div></div>'
          '<div class="fl-fd"><div class="fl-tabs"><span class="on">Suites</span><span>Prices</span><span>Operator</span></div>'
          '<div class="fl-bd"><div class="fl-lb">BUYER FILE &middot; KESTREL BAY RESORT</div>'
          '<div class="fl-h">Under construction. <em>Here&rsquo;s what you choose.</em></div>'
          '<ul><li>Two suites &middot; 34 or 52 m&sup2;</li><li>Prices in US$ and A$</li><li>The Owners&rsquo; Club</li><li>Run by Tidewater</li></ul>'
          '<div class="fl-ph"><img src="assets/ph-site-1.jpg" alt="" style="object-position:50% 50%"><span>the site</span></div></div></div>')

# ═══ ANGLE THREE · the owners' membership ═══

# 11 · the swing tag — valued up to US$15,000 ──────────────────────────────
K['tag'] = '''
  @A .xa-tag .xa-ph { object-position:46% 50%; }
  @A .xa-tag .g-sc { position:absolute; inset:0; background:linear-gradient(90deg,rgba(10,22,32,.9) 0%,rgba(10,22,32,.66) 42%,rgba(10,22,32,.08) 72%); }
  @A .xa-tag .g-tx { position:absolute; left:6cqw; top:7cqw; width:46cqw; }
  @A .xa-tag .g-tx .xa-eb { color:var(--gold-lite); }
  @A .xa-tag .g-t { font-family:'Playfair',serif; font-size:7.6cqw; line-height:1.04; margin-top:1.6cqw; }
  @A .xa-tag .g-t em { color:var(--gold-lite); }
  @A .xa-tag .g-l { list-style:none; margin:3.6cqw 0 0; padding:0; display:grid; gap:1.6cqw; }
  @A .xa-tag .g-l li { font-size:3.3cqw; line-height:1.25; padding-left:3.4cqw; position:relative; }
  @A .xa-tag .g-l li::before { content:''; position:absolute; left:0; top:1.1cqw; width:1.5cqw; height:1.5cqw; border-radius:50%; background:var(--gold-lite); }
  @A .xa-tag .g-lg { position:absolute; left:6cqw; bottom:6cqw; width:44cqw; border-top:.3cqw solid rgba(226,184,114,.55); padding-top:2cqw; font-size:2.6cqw; letter-spacing:.16em; text-transform:uppercase; font-weight:700; line-height:1.5; }
  @A .xa-tag .g-lg b { display:block; font-family:'Playfair',serif; font-size:5cqw; letter-spacing:0; text-transform:none; font-weight:500; color:var(--gold-lite); }
  @A .xa-tag .g-str { position:absolute; left:75cqw; top:-1cqw; width:.4cqw; height:19cqw; background:linear-gradient(#F3EAD6,#C9B48C); z-index:2; }
  @A .xa-tag .g-tw { position:absolute; left:55cqw; top:12cqw; width:40cqw; transform:rotate(5deg); transform-origin:50% 6cqw; filter:drop-shadow(0 1.6cqw 2.6cqw rgba(0,0,0,.5)); z-index:3; }
  @A .xa-tag .g-tg { background:#FBF7F0; color:#13283A; clip-path:polygon(24% 0,76% 0,100% 11%,100% 100%,0 100%,0 11%); padding:12cqw 4cqw 5cqw; text-align:center;
    display:flex; flex-direction:column; align-items:center; position:relative; }
  @A .xa-tag .g-tg::before { content:''; position:absolute; left:50%; top:4cqw; width:4.6cqw; height:4.6cqw; margin-left:-2.3cqw; border-radius:50%; background:#0C1B28; box-shadow:0 0 0 .9cqw #C9A25A; }
  @A .xa-tag .g-tg .xa-logo { width:20cqw; }
  @A .xa-tag .g-r { width:70%; border-top:.3cqw solid rgba(19,40,58,.2); margin:2.6cqw 0; }
  @A .xa-tag .g-nm { font-family:'Playfair',serif; font-size:4.4cqw; line-height:1.1; }
  @A .xa-tag .g-k { font-size:2.3cqw; letter-spacing:.2em; text-transform:uppercase; font-weight:700; color:var(--gold-d); margin-top:2.4cqw; }
  @A .xa-tag .g-v { font-family:'Anton',sans-serif; font-size:7.6cqw; line-height:1; margin-top:.8cqw; white-space:nowrap; }
  @A .xa-tag .g-f { font-size:2.3cqw; letter-spacing:.18em; text-transform:uppercase; font-weight:700; color:#5A5249; }
'''
C_TAG = ('<img class="xa-ph" src="assets/ph-aerial.jpg" alt=""><div class="g-sc"></div>'
         '<div class="g-tx"><div class="xa-eb">The Owners&rsquo; Club</div><div class="g-t">Owners get <em>a membership.</em></div>'
         '<ul class="g-l"><li>Complimentary resort stays</li><li>Priority bookings</li><li>Member rates at Tidewater venues</li></ul></div>'
         '<div class="g-lg">Suites from<b>US$165,000</b></div>'
         '<div class="g-str"></div><div class="g-tw"><div class="g-tg">' + LOGO_D + '<div class="g-r"></div>'
         '<div class="g-nm">The Owners&rsquo; Club</div><div class="g-k">Valued up to</div><div class="g-v">US$15,000</div>'
         '<div class="g-r"></div><div class="g-f">For suite owners</div></div></div>')

# 12 · the member pass — member rates across Tidewater venues ───────────────
K['pass'] = '''
  @A .xa-pass { background:#13283A; }
  @A .xa-pass .xa-ph { height:54%; object-position:50% 40%; }
  @A .xa-pass .b-sc { position:absolute; left:0; right:0; top:0; height:54%; background:linear-gradient(180deg,rgba(10,22,32,.88) 0%,rgba(10,22,32,.62) 34%,rgba(10,22,32,.25) 62%,rgba(10,22,32,.6) 100%); }
  @A .xa-pass .b-hd { position:absolute; left:6cqw; right:6cqw; top:5.4cqw; font-family:'Playfair',serif; font-size:8.4cqw; line-height:1.02; text-shadow:0 .3cqw 2cqw rgba(0,0,0,.5); }
  @A .xa-pass .b-hd em { color:var(--gold-lite); }
  @A .xa-pass .b-hd small { display:block; font-family:'Jost',sans-serif; font-size:3cqw; letter-spacing:.14em; text-transform:uppercase; font-weight:700; margin-top:1.8cqw; }
  @A .xa-pass .b-tk { position:absolute; left:4cqw; right:4cqw; top:44cqw; bottom:4cqw; display:grid; grid-template-columns:1fr 26cqw; color:#13283A; filter:drop-shadow(0 1.6cqw 3cqw rgba(0,0,0,.45)); }
  @A .xa-pass .b-mn, @A .xa-pass .b-sb { background:#FBF7F0; }
  @A .xa-pass .b-mn { border-radius:2.4cqw 0 0 2.4cqw; padding:3.4cqw 4cqw; display:flex; flex-direction:column;
    -webkit-mask:radial-gradient(circle 2.4cqw at 100% 0,transparent 98%,#000) top/100% 51% no-repeat,radial-gradient(circle 2.4cqw at 100% 100%,transparent 98%,#000) bottom/100% 51% no-repeat;
            mask:radial-gradient(circle 2.4cqw at 100% 0,transparent 98%,#000) top/100% 51% no-repeat,radial-gradient(circle 2.4cqw at 100% 100%,transparent 98%,#000) bottom/100% 51% no-repeat; }
  @A .xa-pass .b-sb { border-radius:0 2.4cqw 2.4cqw 0; border-left:.45cqw dashed #C9BFAE; padding:3.4cqw 3cqw; display:flex; flex-direction:column; gap:2cqw; background:#13283A; color:#FBF7F0;
    -webkit-mask:radial-gradient(circle 2.4cqw at 0 0,transparent 98%,#000) top/100% 51% no-repeat,radial-gradient(circle 2.4cqw at 0 100%,transparent 98%,#000) bottom/100% 51% no-repeat;
            mask:radial-gradient(circle 2.4cqw at 0 0,transparent 98%,#000) top/100% 51% no-repeat,radial-gradient(circle 2.4cqw at 0 100%,transparent 98%,#000) bottom/100% 51% no-repeat; }
  @A .xa-pass .b-top { display:flex; justify-content:space-between; align-items:center; }
  @A .xa-pass .b-top .xa-logo { width:15cqw; }
  @A .xa-pass .b-top span { font-size:2.4cqw; letter-spacing:.22em; text-transform:uppercase; font-weight:800; color:var(--gold-d); text-align:right; line-height:1.4; }
  @A .xa-pass .b-vn { margin-top:auto; display:grid; gap:.6cqw; }
  @A .xa-pass .b-vn div { font-family:'Playfair',serif; font-size:4.6cqw; line-height:1.1; display:flex; align-items:center; gap:1.6cqw; }
  @A .xa-pass .b-vn div::before { content:''; width:1.4cqw; height:1.4cqw; transform:rotate(45deg); background:var(--sand); flex:none; }
  @A .xa-pass .b-fl { display:flex; justify-content:space-between; margin-top:auto; padding-top:2.2cqw; border-top:.3cqw solid rgba(19,40,58,.1); }
  @A .xa-pass .b-fl div, @A .xa-pass .b-sb div { font-size:3.1cqw; font-weight:700; line-height:1.15; }
  @A .xa-pass .b-fl small, @A .xa-pass .b-sb small { display:block; font-size:2cqw; letter-spacing:.18em; text-transform:uppercase; font-weight:700; color:#8C8173; margin-bottom:.6cqw; }
  @A .xa-pass .b-sb small { color:rgba(251,247,240,.55); }
  @A .xa-pass .b-sb b { font-family:'Anton',sans-serif; font-weight:400; font-size:8cqw; line-height:1; color:var(--gold-lite); letter-spacing:.04em; }
  @A .xa-pass .b-bc { margin-top:auto; height:8cqw; background:repeating-linear-gradient(90deg,#FBF7F0 0 .4cqw,transparent .4cqw 1cqw,#FBF7F0 1cqw 1.8cqw,transparent 1.8cqw 2.2cqw,#FBF7F0 2.2cqw 2.5cqw,transparent 2.5cqw 3.2cqw); }
'''
C_PASS = ('<img class="xa-ph" src="assets/ph-venue-1.jpg" alt=""><div class="b-sc"></div>'
         '<div class="b-hd">Member rates <em>across Tidewater.</em><small>For suite owners &middot; the Owners&rsquo; Club</small></div>'
         '<div class="b-tk"><div class="b-mn"><div class="b-top">' + LOGO_D + '<span>Owners&rsquo; Club<br>pass</span></div>'
         '<div class="b-vn"><div>Tidewater venues</div><div>Member rates</div><div>Beach-club access</div></div>'
         '<div class="b-fl"><div><small>Holder</small>You</div><div><small>Rate</small>Member</div><div><small>Bookings</small>Priority</div></div></div>'
         '<div class="b-sb"><div><small>Admit</small>One owner</div><div><small>Venues</small><b>12</b></div><div class="b-bc"></div></div></div>')

# 13 · the calendar — owners book first ────────────────────────────────────
K['cal'] = '''
  @A .xa-cal .xa-ph { object-position:50% 50%; }
  @A .xa-cal .l-sc { position:absolute; inset:0; background:linear-gradient(90deg,rgba(10,22,32,.25) 0%,rgba(10,22,32,.6) 48%,rgba(10,22,32,.82) 100%),linear-gradient(180deg,rgba(10,22,32,0) 55%,rgba(10,22,32,.85) 100%); }
  @A .xa-cal .l-pg { position:absolute; left:5.4cqw; top:7cqw; width:47cqw; background:#FEFDFB; color:#13283A; border-radius:1.6cqw; overflow:hidden;
    transform:rotate(-4deg); box-shadow:0 2cqw 5cqw rgba(0,0,0,.45); padding-bottom:3cqw; }
  @A .xa-cal .l-pg.bk { transform:rotate(3deg) translate(1.5cqw,1.2cqw); background:#EFE9E0; height:58cqw; padding:0; }
  @A .xa-cal .l-hd { background:#B57A2E; color:#fff; font-size:3.2cqw; letter-spacing:.2em; text-transform:uppercase; font-weight:700; padding:3.6cqw 0 2.2cqw; position:relative; text-align:center; }
  @A .xa-cal .l-hd::before, @A .xa-cal .l-hd::after { content:''; position:absolute; top:1.1cqw; width:2.2cqw; height:2.2cqw; border-radius:50%; background:#7A4F18; }
  @A .xa-cal .l-hd::before { left:9cqw; } @A .xa-cal .l-hd::after { right:9cqw; }
  @A .xa-cal .l-gr { display:grid; grid-template-columns:repeat(7,1fr); gap:.5cqw 0; padding:2.4cqw 2.2cqw 0; text-align:center; position:relative; }
  @A .xa-cal .l-gr span { font-size:2.7cqw; font-weight:600; line-height:1; padding:1.1cqw 0; position:relative; z-index:1; }
  @A .xa-cal .l-gr span.w { font-size:2cqw; letter-spacing:.1em; color:#8C8173; font-weight:700; }
  @A .xa-cal .l-gr span.on { background:#13283A; color:var(--gold-lite); }
  @A .xa-cal .l-gr span.s { border-radius:1.6cqw 0 0 1.6cqw; } @A .xa-cal .l-gr span.e { border-radius:0 1.6cqw 1.6cqw 0; }
  @A .xa-cal .l-gr span.x { color:#C9BFAE; }
  @A .xa-cal .l-ci { position:absolute; left:2cqw; right:2cqw; top:13.6cqw; height:14cqw; border:.5cqw solid #D2312A; border-radius:50%; transform:rotate(-3deg); z-index:2; pointer-events:none; }
  @A .xa-cal .l-hw { font-family:'Caveat',cursive; font-weight:700; font-size:4.6cqw; color:#D2312A; text-align:center; margin-top:2.2cqw; transform:rotate(-3deg); }
  @A .xa-cal .l-tx { position:absolute; left:57cqw; right:5cqw; top:9cqw; }
  @A .xa-cal .l-tx .xa-eb { color:var(--gold-lite); font-size:2.6cqw; }
  @A .xa-cal .l-t { font-family:'Playfair',serif; font-size:7.6cqw; line-height:1.04; margin-top:1.4cqw; }
  @A .xa-cal .l-t em { color:var(--gold-lite); }
  @A .xa-cal .l-s { font-size:3.4cqw; line-height:1.35; margin-top:2.4cqw; color:rgba(255,255,255,.9); }
  @A .xa-cal .l-ft { position:absolute; left:6cqw; right:6cqw; bottom:5cqw; display:flex; justify-content:space-between; align-items:flex-end; gap:3cqw; }
  @A .xa-cal .l-ft div { font-family:'Playfair',serif; font-size:5.6cqw; line-height:1.08; }
  @A .xa-cal .l-ft div em { color:var(--gold-lite); }
  @A .xa-cal .l-ft .xa-logo { width:19cqw; flex:none; }
'''
def _cal_grid():
    days = ''.join(f'<span class="w">{d}</span>' for d in 'MTWTFSS')
    cells = []
    for i in range(35):
        n = i - 1                     # month starts on a Tuesday; numbers only, no month named
        if n < 1 or n > 31:
            cells.append(f'<span class="x">{(n + 30) if n < 1 else n - 31}</span>')
            continue
        cls = []
        if 13 <= n <= 19:
            cls.append('on')
            if n == 13: cls.append('s')
            if n == 19: cls.append('e')
        cells.append(f'<span class="{" ".join(cls)}">{n}</span>' if cls else f'<span>{n}</span>')
    return days + ''.join(cells)
C_CAL = ('<img class="xa-ph" src="assets/ph-pool-3.jpg" alt=""><div class="l-sc"></div>'
         '<div class="l-pg bk"></div><div class="l-pg"><div class="l-hd">School holidays</div><div class="l-gr">' + _cal_grid() + '<i class="l-ci"></i></div>'
         '<div class="l-hw">owners book first</div></div>'
         '<div class="l-tx"><div class="xa-eb">The Owners&rsquo; Club</div><div class="l-t">Owners book <em>first.</em></div>'
         '<div class="l-s">Priority bookings and complimentary resort stays.</div></div>'
         '<div class="l-ft"><div>The Garden Suite, <em>from US$165,000.</em></div>' + LOGO_L + '</div>')

# 14 · the invitation — Owners' Club events ────────────────────────────────
K['inv'] = '''
  @A .xa-inv .xa-ph { object-position:78% 50%; }
  @A .xa-inv .v-sc { position:absolute; inset:0; background:linear-gradient(180deg,rgba(10,22,32,.5) 0%,rgba(10,22,32,.05) 22%,rgba(10,22,32,.05) 44%,rgba(10,22,32,.7) 70%,rgba(10,22,32,.9) 100%); }
  @A .xa-inv .v-eb { position:absolute; left:6cqw; top:5.6cqw; color:#fff; text-shadow:0 .3cqw 1.6cqw rgba(0,0,0,.6); }
  @A .xa-inv .v-cd { position:absolute; left:6cqw; right:6cqw; top:54.5cqw; bottom:4.5cqw; background:#FBF7F0; color:#13283A; transform:rotate(-2deg);
    box-shadow:0 2cqw 6cqw rgba(0,0,0,.55); padding:2.2cqw; }
  @A .xa-inv .v-in { height:100%; border:.35cqw solid #13283A; outline:.2cqw solid rgba(19,40,58,.35); outline-offset:-1.3cqw; display:grid; grid-template-columns:19cqw 1fr;
    grid-template-rows:auto auto 1fr auto; column-gap:4cqw; align-items:start; padding:3.4cqw 4.6cqw 2.4cqw; }
  @A .xa-inv .v-in .xa-logo { width:19cqw; grid-row:1 / 4; align-self:center; }
  @A .xa-inv .v-k { font-size:2.3cqw; letter-spacing:.22em; text-transform:uppercase; font-weight:700; color:var(--gold-d); }
  @A .xa-inv .v-t { font-family:'Playfair',serif; font-size:6.2cqw; line-height:1.04; margin-top:1.2cqw; }
  @A .xa-inv .v-t em { color:var(--gold-d); }
  @A .xa-inv .v-s { font-family:'Playfair',serif; font-style:italic; font-size:3.3cqw; line-height:1.3; color:#5A5249; margin-top:1.2cqw; }
  @A .xa-inv .v-r { grid-column:1 / 3; margin-top:1.6cqw; width:100%; display:flex; justify-content:space-between; border-top:.25cqw solid rgba(19,40,58,.25); padding-top:1.6cqw;
    font-size:2.3cqw; letter-spacing:.16em; text-transform:uppercase; font-weight:700; }
  @A .xa-inv .xa-ai { right:4cqw; top:5.6cqw; }
'''
C_INV = ('<img class="xa-ph" src="assets/ph-event.jpg" alt=""><div class="v-sc"></div>'
         '<div class="xa-eb v-eb">For suite owners</div>'
         '<div class="v-cd"><div class="v-in">' + LOGO_D + '<div class="v-k">The Owners&rsquo; Club</div>'
         '<div class="v-t">Invitations, <em>for owners.</em></div><div class="v-s">Owners&rsquo; events, part of the membership.</div>'
         '<div class="v-r"><span>RSVP</span><span>Enquire about a suite</span></div></div></div>'
         '<div class="xa-ai">Owners&rsquo; Club event</div>')

# 15 · the key-card sleeve — complimentary resort stays ────────────────────
K['key'] = '''
  @A .xa-key .xa-ph { object-position:40% 62%; }
  @A .xa-key .y-sc { position:absolute; inset:0; background:linear-gradient(180deg,rgba(10,22,32,.85) 0%,rgba(10,22,32,.55) 30%,rgba(10,22,32,.1) 52%,rgba(10,22,32,.3) 100%); }
  @A .xa-key .y-tx { position:absolute; left:6cqw; right:6cqw; top:5.6cqw; }
  @A .xa-key .y-tx .xa-eb { color:var(--gold-lite); }
  @A .xa-key .y-t { font-family:'Playfair',serif; font-size:8cqw; line-height:1.03; margin-top:1.4cqw; }
  @A .xa-key .y-t em { color:var(--gold-lite); }
  @A .xa-key .y-s { font-size:3.3cqw; margin-top:1.8cqw; color:rgba(255,255,255,.9); }
  @A .xa-key .y-wr { position:absolute; left:31cqw; top:44cqw; width:61cqw; height:50cqw; transform:rotate(-5deg); }
  @A .xa-key .y-kc { position:absolute; left:7cqw; right:7cqw; top:-9cqw; height:28cqw; border-radius:2.2cqw; background:linear-gradient(135deg,#24445E,#0C1B28);
    box-shadow:0 1cqw 3cqw rgba(0,0,0,.4); display:flex; justify-content:center; padding-top:2.6cqw; border:.3cqw solid rgba(226,184,114,.5); }
  @A .xa-key .y-kc .xa-wm { width:30cqw; height:auto; align-self:flex-start; }
  @A .xa-key .y-sv { position:absolute; left:0; right:0; top:7cqw; bottom:0; background:#FBF7F0; color:#13283A; border-radius:1.6cqw; box-shadow:0 2cqw 5cqw rgba(0,0,0,.5);
    padding:4cqw 5cqw 3.6cqw; display:flex; flex-direction:column; }
  @A .xa-key .y-sv::before { content:''; position:absolute; left:50%; top:-.2cqw; width:16cqw; height:3cqw; margin-left:-8cqw; border-radius:0 0 8cqw 8cqw; background:rgba(19,40,58,.12); }
  @A .xa-key .y-w { font-family:'Playfair',serif; font-size:5.2cqw; line-height:1; }
  @A .xa-key .y-w em { color:var(--gold-d); }
  @A .xa-key .y-f { display:flex; align-items:baseline; gap:1.6cqw; margin-top:2cqw; font-size:2.3cqw; letter-spacing:.16em; text-transform:uppercase; font-weight:700; color:#8C8173; }
  @A .xa-key .y-f i { flex:1; border-bottom:.3cqw dotted #BDB3A6; }
  @A .xa-key .y-f b { font-family:'Caveat',cursive; font-size:5cqw; letter-spacing:0; text-transform:none; color:#13283A; font-weight:700; line-height:.8; }
'''
C_KEY = ('<img class="xa-ph" src="assets/ph-suite-b.jpg" alt=""><div class="y-sc"></div>'
         '<div class="y-tx"><div class="xa-eb">The Owners&rsquo; Club</div><div class="y-t">Check in <em>as an owner.</em></div>'
         '<div class="y-s">Complimentary resort stays for suite owners.</div></div>'
         '<div class="y-wr"><div class="y-kc">' + WORD_L + '</div><div class="y-sv"><div class="y-w">Welcome, <em>owner.</em></div>'
         '<div class="y-f">Suite<i></i><b>Ocean Suite</b></div><div class="y-f">Size<i></i><b>52 m&sup2;</b></div>'
         '<div class="y-f">Stay<i></i><b>complimentary</b></div><div class="y-f">Price<i></i><b>US$260,000</b></div></div></div>')

# ═══ ANGLE FOUR · for buyers still deciding (warm) ═══

# 16 · the quiz — question two of six ──────────────────────────────────────
K['quiz'] = '''
  @A .xa-quiz .xa-ph { object-position:50% 40%; filter:blur(.5cqw) brightness(.6) saturate(1.1); transform:scale(1.12); }
  @A .xa-quiz .z-lg { position:absolute; left:0; right:0; top:3.6cqw; }
  @A .xa-quiz .z-lg .xa-wm { width:36cqw; margin:0 auto; }
  @A .xa-quiz .z-cd { position:absolute; left:8cqw; right:8cqw; top:16cqw; bottom:6cqw; background:#FEFDFB; color:#13283A; border-radius:3.4cqw; padding:5cqw 5.4cqw 4.6cqw;
    box-shadow:0 2cqw 6cqw rgba(0,0,0,.4); display:flex; flex-direction:column; }
  @A .xa-quiz .z-pr { display:flex; align-items:center; gap:2cqw; font-size:2.6cqw; letter-spacing:.14em; text-transform:uppercase; font-weight:700; color:#8C8173; }
  @A .xa-quiz .z-pr i { flex:1; height:1cqw; border-radius:1cqw; background:#EDE6DA; position:relative; overflow:hidden; }
  @A .xa-quiz .z-pr i::after { content:''; position:absolute; left:0; top:0; bottom:0; width:33.3%; background:var(--sand); border-radius:1cqw; }
  @A .xa-quiz .z-q { font-family:'Playfair',serif; font-size:8cqw; line-height:1.05; margin-top:3cqw; }
  @A .xa-quiz .z-q em { color:var(--gold-d); }
  @A .xa-quiz .z-os { display:grid; gap:2cqw; margin-top:3.6cqw; }
  @A .xa-quiz .z-o { display:flex; align-items:center; gap:2.4cqw; border:.35cqw solid #E2DACE; border-radius:2.2cqw; padding:2.4cqw 3cqw; font-size:3.8cqw; font-weight:600; }
  @A .xa-quiz .z-o::before { content:''; flex:none; width:3.6cqw; height:3.6cqw; border-radius:50%; border:.45cqw solid #CFC4B3; box-sizing:border-box; }
  @A .xa-quiz .z-o.on { border-color:#13283A; background:#FBF3E4; }
  @A .xa-quiz .z-o.on::before { border-color:#13283A; background:#13283A; box-shadow:inset 0 0 0 .7cqw #FBF3E4; }
  @A .xa-quiz .z-ft { display:flex; justify-content:space-between; align-items:center; gap:2cqw; margin-top:auto; font-size:2.6cqw; color:#8C8173; font-weight:600; }
  @A .xa-quiz .z-ft b { flex:none; background:#13283A; color:var(--gold-lite); border-radius:10cqw; padding:1.6cqw 3.4cqw 1.4cqw; font-size:2.8cqw; letter-spacing:.12em; text-transform:uppercase; }
'''
C_QUIZ = ('<img class="xa-ph" src="assets/ph-hero-pool.jpg" alt=""><div class="z-lg">' + WORD_L + '</div>'
          '<div class="z-cd"><div class="z-pr"><span>Question 2 of 6</span><i></i></div>'
          '<div class="z-q">What would you use it <em>for?</em></div>'
          '<div class="z-os"><div class="z-o">Rental income</div><div class="z-o">Holidays</div><div class="z-o on">A bit of both</div></div>'
          '<div class="z-ft"><span>Then a call from our sales team</span><b>Next &rarr;</b></div></div>')

# 17 · the receipt — what US$165,000 gets you ─────────────────────────────
K['rcpt'] = '''
  @A .xa-rcpt .xa-ph { object-position:30% 50%; filter:brightness(.48) saturate(.85); }
  @A .xa-rcpt .e-hd { position:absolute; left:6cqw; width:37cqw; top:7cqw; }
  @A .xa-rcpt .e-hd .xa-eb { color:var(--gold-lite); }
  @A .xa-rcpt .e-t { font-family:'Playfair',serif; font-size:7.6cqw; line-height:1.04; margin-top:1.6cqw; }
  @A .xa-rcpt .e-t em { color:var(--gold-lite); }
  @A .xa-rcpt .e-s { font-size:3.3cqw; line-height:1.35; margin-top:3cqw; color:rgba(255,255,255,.88); }
  @A .xa-rcpt .e-lg { position:absolute; left:6cqw; bottom:6cqw; }
  @A .xa-rcpt .e-lg .xa-logo { width:22cqw; }
  @A .xa-rcpt .e-rc { position:absolute; left:45cqw; width:50cqw; top:4cqw; bottom:3cqw; background:#FEFDF9; color:#2B2522; transform:rotate(2.6deg);
    font-family:'Space Mono',monospace; font-weight:700; font-size:2.5cqw; line-height:1.35; padding:4.2cqw 3.8cqw 6cqw;
    box-shadow:0 2cqw 5cqw rgba(0,0,0,.5);
    -webkit-mask:conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/2.6cqw 51% repeat-x,linear-gradient(#000 0 0) top/100% 50% no-repeat;
            mask:conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) bottom/2.6cqw 51% repeat-x,linear-gradient(#000 0 0) top/100% 50% no-repeat; }
  @A .xa-rcpt .e-rc .xa-logo { width:17cqw; margin:0 auto; }
  @A .xa-rcpt .e-c { text-align:center; font-size:2.1cqw; letter-spacing:.06em; margin-top:1.4cqw; color:#6B625A; }
  @A .xa-rcpt .e-dl { border-top:.3cqw dashed #BDB3A6; margin:1.8cqw 0 1.2cqw; }
  @A .xa-rcpt .e-r { display:flex; align-items:baseline; gap:1cqw; margin-top:.8cqw; }
  @A .xa-rcpt .e-r i { flex:1; border-bottom:.3cqw dotted #BDB3A6; transform:translateY(-.6cqw); }
  @A .xa-rcpt .e-r b { color:#9A6420; }
  @A .xa-rcpt .e-n { font-size:2cqw; color:#6B625A; text-align:right; margin-top:.2cqw; }
  @A .xa-rcpt .e-tot { display:flex; justify-content:space-between; font-size:3.1cqw; margin-top:.4cqw; }
  @A .xa-rcpt .e-tot b { color:#13283A; }
  @A .xa-rcpt .e-au { text-align:right; font-size:2.4cqw; color:#6B625A; margin-top:.6cqw; }
  @A .xa-rcpt .e-th { text-align:center; margin-top:2cqw; font-size:2.1cqw; color:#6B625A; }
  @A .xa-rcpt .e-bc { height:5.4cqw; margin:1.8cqw 3cqw 0; background:repeating-linear-gradient(90deg,#2B2522 0 .35cqw,transparent .35cqw .9cqw,#2B2522 .9cqw 1.5cqw,transparent 1.5cqw 1.9cqw,#2B2522 1.9cqw 2.15cqw,transparent 2.15cqw 2.8cqw); }
'''
C_RCPT = ('<img class="xa-ph" src="assets/ph-suite-a2.jpg" alt="">'
          '<div class="e-hd"><div class="xa-eb">Still deciding?</div><div class="e-t">What the price <em>gets you.</em></div>'
          '<div class="e-s">The Garden Suite, line by line.</div></div><div class="e-lg">' + LOGO_L + '</div>'
          '<div class="e-rc">' + LOGO_D + '<div class="e-c">GARDEN SUITE &middot; KESTREL BAY</div><div class="e-dl"></div>'
          '<div class="e-r">Size<i></i><b>34 m&sup2;</b></div><div class="e-r">Bedroom<i></i><b>1</b></div>'
          '<div class="e-r">Terrace<i></i><b>garden</b></div><div class="e-r">Spa &amp; gym<i></i><b>on site</b></div>'
          '<div class="e-r">Owners&rsquo; club<i></i><b>member</b></div><div class="e-n">valued up to US$15,000</div>'
          '<div class="e-r">Run by<i></i><b>Tidewater</b></div>'
          '<div class="e-dl"></div><div class="e-tot"><span>FROM</span><b>US$165,000</b></div><div class="e-au">about A$240,000</div>'
          '<div class="e-th">** returns: on a private call **</div><div class="e-bc"></div></div>')

# 18 · the lock screen — your enquiry is half done ─────────────────────────
K['lock'] = '''
  @A .xa-lock { font-family:'Helvetica Neue',Helvetica,Arial,sans-serif; }
  @A .xa-lock .xa-ph { object-position:50% 40%; filter:brightness(.7); }
  @A .xa-lock .o-dt { position:absolute; left:0; right:0; top:4.4cqw; text-align:center; font-size:3.4cqw; font-weight:600; color:rgba(255,255,255,.9); }
  @A .xa-lock .o-tm { position:absolute; left:0; right:0; top:8cqw; text-align:center; font-size:19cqw; font-weight:600; letter-spacing:-.02em; line-height:1; color:rgba(255,255,255,.94); }
  @A .xa-lock .o-n { position:absolute; left:5cqw; right:5cqw; border-radius:3.6cqw; background:rgba(246,242,237,.86); -webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px); color:#111; padding:2.8cqw 3.4cqw; }
  @A .xa-lock .o-n.a { top:32cqw; z-index:2; }
  @A .xa-lock .o-n.ghost { top:33.8cqw; left:8cqw; right:8cqw; height:22cqw; background:rgba(246,242,237,.5); }
  @A .xa-lock .o-h { display:flex; align-items:center; gap:1.8cqw; font-size:2.6cqw; letter-spacing:.06em; text-transform:uppercase; color:#6B625A; font-weight:600; }
  @A .xa-lock .o-h img { width:6cqw; height:6cqw; border-radius:1.4cqw; background:#fff; object-fit:cover; }
  @A .xa-lock .o-h span { margin-left:auto; text-transform:none; letter-spacing:0; font-weight:400; }
  @A .xa-lock .o-n b { display:block; font-size:4cqw; margin-top:1.4cqw; }
  @A .xa-lock .o-n p { font-size:3.3cqw; line-height:1.3; margin:.6cqw 0 0; color:#333; }
  @A .xa-lock .o-w { position:absolute; left:5cqw; right:5cqw; top:60cqw; border-radius:3.6cqw; background:rgba(19,40,58,.66); -webkit-backdrop-filter:blur(8px); backdrop-filter:blur(8px); padding:2.8cqw 3.4cqw 3cqw; }
  @A .xa-lock .o-wk { display:flex; justify-content:space-between; font-size:2.5cqw; letter-spacing:.16em; text-transform:uppercase; font-weight:700; color:var(--gold-lite); }
  @A .xa-lock .o-bar { display:grid; grid-template-columns:repeat(6,1fr); gap:.8cqw; margin:1.8cqw 0 2.2cqw; }
  @A .xa-lock .o-bar i { height:1.1cqw; border-radius:1cqw; background:rgba(255,255,255,.25); }
  @A .xa-lock .o-bar i.on { background:var(--gold-lite); }
  @A .xa-lock .o-w ol { list-style:none; margin:0; padding:0; display:grid; grid-template-columns:1fr 1fr; gap:1.4cqw 3cqw; }
  @A .xa-lock .o-w li { display:flex; gap:1.6cqw; align-items:center; font-size:3cqw; line-height:1.2; font-weight:500; color:rgba(255,255,255,.62); }
  @A .xa-lock .o-w li::before { content:''; flex:none; width:2.8cqw; height:2.8cqw; border-radius:50%; border:.4cqw solid rgba(255,255,255,.5); box-sizing:border-box; }
  @A .xa-lock .o-w li.ok { color:#fff; }
  @A .xa-lock .o-w li.ok::before { border-color:var(--gold-lite); background:var(--gold-lite); box-shadow:inset 0 0 0 .5cqw #13283A; }
  @A .xa-lock .o-hm { position:absolute; left:50%; bottom:2.2cqw; width:30cqw; height:1.2cqw; border-radius:1cqw; background:rgba(255,255,255,.85); transform:translateX(-50%); }
'''
C_LOCK = ('<img class="xa-ph" src="assets/ph-resort-tall.jpg" alt="">'
          '<div class="o-dt">Saturday</div><div class="o-tm">7:42</div>'
          '<div class="o-n ghost"></div>'
          '<div class="o-n a"><div class="o-h"><img src="assets/brand-avatar.png" alt="">Kestrel Bay Resort<span>now</span></div>'
          '<b>Your suite enquiry is half done</b><p>3 of 6 questions answered. Tap to finish &mdash; then our sales team calls you.</p></div>'
          '<div class="o-w"><div class="o-wk"><span>Your enquiry</span><span>3 of 6</span></div>'
          '<div class="o-bar"><i class="on"></i><i class="on"></i><i class="on"></i><i></i><i></i><i></i></div>'
          '<ol><li class="ok">Which suite?</li><li>When?</li><li class="ok">What&rsquo;s it for?</li><li>Funding</li><li class="ok">Budget</li><li>Stayed at Tidewater?</li></ol></div>'
          '<div class="o-hm"></div>')

# 19 · the clipboard — before you reserve, ask us these five ──────────────
K['clip'] = '''
  @A .xa-clip .xa-ph { object-position:50% 50%; filter:brightness(.5) saturate(.85); transform:scale(1.04); }
  @A .xa-clip .p-bd { position:absolute; left:11cqw; right:11cqw; top:6cqw; bottom:3.4cqw; background:linear-gradient(160deg,#3F5468,#22313F); border-radius:3cqw; transform:rotate(-2.2deg);
    box-shadow:0 2.4cqw 6cqw rgba(0,0,0,.55); }
  @A .xa-clip .p-cl { position:absolute; left:50%; top:-3cqw; width:26cqw; height:9cqw; transform:translateX(-50%); border-radius:2.4cqw 2.4cqw 1cqw 1cqw;
    background:linear-gradient(180deg,#F1F3F5,#A9B0B6); box-shadow:0 .6cqw 1.4cqw rgba(0,0,0,.35); z-index:3; }
  @A .xa-clip .p-cl::after { content:''; position:absolute; left:50%; top:1.8cqw; width:9cqw; height:2.6cqw; margin-left:-4.5cqw; border-radius:2cqw; background:#3F5468; }
  @A .xa-clip .p-pp { position:absolute; left:3.2cqw; right:3.2cqw; top:4.4cqw; bottom:3.2cqw; background:#FEFDFB; color:#13283A; border-radius:.6cqw; padding:7cqw 5cqw 3.6cqw; display:flex; flex-direction:column; }
  @A .xa-clip .p-hd { display:flex; justify-content:space-between; align-items:flex-end; gap:2cqw; border-bottom:.35cqw solid #13283A; padding-bottom:1.8cqw; }
  @A .xa-clip .p-t { font-family:'Playfair',serif; font-size:6.2cqw; line-height:1.02; }
  @A .xa-clip .p-t em { color:var(--gold-d); }
  @A .xa-clip .p-hd .xa-logo { width:14cqw; flex:none; }
  @A .xa-clip .p-s { font-size:2.4cqw; letter-spacing:.14em; text-transform:uppercase; font-weight:700; color:var(--gold-d); margin-top:1.8cqw; }
  @A .xa-clip ol { list-style:none; margin:1cqw 0 0; padding:0; counter-reset:q; }
  @A .xa-clip li { counter-increment:q; display:flex; gap:2.2cqw; align-items:flex-start; font-size:3.1cqw; line-height:1.25; padding:1.5cqw 0; border-bottom:.25cqw solid #ECE6DC; }
  @A .xa-clip li::before { content:''; flex:none; width:3.2cqw; height:3.2cqw; border:.4cqw solid #13283A; border-radius:.5cqw; margin-top:.1cqw; }
  @A .xa-clip .p-hw { font-family:'Caveat',cursive; font-weight:700; font-size:5.2cqw; line-height:1; color:#B57A2E; margin-top:auto; transform:rotate(-2deg); text-align:right; }
'''
C_CLIP = ('<img class="xa-ph" src="assets/ph-dining.jpg" alt="">'
          '<div class="p-bd"><div class="p-cl"></div><div class="p-pp">'
          '<div class="p-hd"><div class="p-t">Before you <em>reserve.</em></div>' + LOGO_D + '</div>'
          '<div class="p-s">Five things to ask our sales team</div>'
          '<ol><li>Which suite fits what I want it for?</li><li>What is the price in A$ today?</li><li>What does the Owners&rsquo; Club include?</li>'
          '<li>Who runs the resort while I&rsquo;m home?</li><li>How are the projected returns worked out?</li></ol>'
          '<div class="p-hw">ask them on a private call &rarr;</div></div></div>')

# ─────────────────────────── the cells ───────────────────────────
W = lambda angle, line, who, fmt, diff: dict(angle=angle, line=line, who=who, fmt=fmt, diff=diff)

ADS1 = [
    cell(1, 'kxt', 'mag', 'Australians who holiday in Bali: <b>you can now own a suite at Kestrel Bay Resort.</b> Built by Kestrel, run by Tidewater &mdash; from US$165,000 (about A$240k).',
         C_MAG, 'Own a suite at Kestrel Bay Resort', 'Learn more',
         W('Own a suite in Bali', 'Owning in Bali is the idea that stops the scroll, so the cover leads with it and lets the price and the operator follow.',
           'Australians who holiday in Bali', 'Editorial cover &middot; 1:1', 'The only full-bleed magazine layout'),
         'Own a suite &middot; magazine cover'),
    cell(2, 'gar', 'two', 'Two suites at Kestrel Bay Resort. <b>The Garden Suite from US$165,000 (about A$240k)</b>, or the Ocean Suite at US$260,000 (about A$375k).',
         C_TWO, 'Compare the two suites', 'Learn more',
         W('Two suites, side by side', 'The first question is &ldquo;which one?&rdquo;, so both prices sit side by side in both currencies.',
           'Every cold buyer in the campaign', 'Comparison cards &middot; 1:1', 'The only side-by-side layout'),
         'Two suites &middot; side by side'),
    cell(3, 'oce', 'prints', 'The Ocean Suite: 52&nbsp;m&sup2;, one bedroom, a daybed on the balcony and an ocean outlook. <b>Interconnecting options for families.</b> US$260,000.',
         C_PRINTS, 'The Ocean Suite &middot; US$260,000', 'Learn more',
         W('Room by room', 'Buyers want to see inside before they enquire, so three rooms are laid out like prints on a table.',
           'Couples and families looking at the bigger suite', 'Print set &middot; 1:1 &middot; artist&rsquo;s impressions', 'The only light, tactile layout'),
         'Ocean Suite &middot; print set'),
    cell(4, 'oce', 'four', 'Kids under 12 stay free at Kestrel Bay Resort, with their own Kids&rsquo; Club and a lagoon pool. <b>The Ocean Suite has interconnecting options.</b>',
         C_FOUR, 'A suite for the family holidays', 'Learn more',
         W('Kids stay free', 'One fact in the middle and four reasons around it, so a parent sees what the kids get before the price.',
           'Parents who holiday in Bali', 'Four-tile grid &middot; 1:1', 'The only grid'),
         'Kids stay free &middot; tile grid'),
    cell(5, 'gar', 'dir', 'Lagoon pool, adults&rsquo; pool, spa, gym, yoga deck and beach-club access &mdash; <b>all at Kestrel Bay Resort.</b> Suites from US$165,000 (about A$240k).',
         C_DIR, 'Everything on site &middot; from US$165,000', 'Learn more',
         W('All on site', 'The resort reads like a hotel sign, so the buyer sees the lifestyle before the price.',
           'Buyers who want a full resort, not just a room', 'Directory sign &middot; 1:1', 'The only signage layout'),
         'All on site &middot; directory sign'),
]

ADS2 = [
    cell(6, 'gar', 'num', 'The Garden Suite is from US$165,000. <b>In Australian dollars, that&rsquo;s about A$240,000.</b> Our sales team confirms today&rsquo;s figure on the call.',
         C_NUM, 'The Garden Suite in A$', 'Get quote',
         W('In Australian dollars', 'A US-dollar price makes Australians do maths before they enquire, so the ad does it for them, rate on the image.',
           'Cold Australian buyers', 'Big number &middot; 1:1 &middot; rate on the image', 'The only number-led layout'),
         'In A$ &middot; big number'),
    cell(7, 'kxt', 'pict', 'Built by Kestrel: 18 years building resorts and homes, 9 developments and <b>600+ units delivered.</b> See who&rsquo;s behind Kestrel Bay Resort.',
         C_PICT, 'Who builds Kestrel Bay Resort', 'Learn more',
         W('Who builds it', 'An off-plan buyer&rsquo;s first worry is the builder, so three numbers from Kestrel&rsquo;s own record answer it.',
           'Careful buyers &middot; first time buying overseas', 'Pictogram stat &middot; 1:1 &middot; Kestrel&rsquo;s figures', 'The only pictogram'),
         'Who builds it &middot; pictogram'),
    cell(8, 'kxt', 'myth', 'Owning from Australia? <b>You don&rsquo;t run it &mdash; Tidewater Hospitality does</b>: 12 venues and close to 900,000 guests a year.',
         C_MYTH, 'Who runs the resort', 'Learn more',
         W('Who runs it', 'It names the worry of owning from a distance, then answers it with an operator that already runs 12 venues.',
           'Buyers who&rsquo;ve never owned overseas', 'Myth vs fact &middot; diagonal split &middot; 1:1', 'The only diagonal'),
         'Who runs it &middot; myth vs fact'),
    cell(9, 'oce', 'chat', '&ldquo;What will it earn?&rdquo; is the right question. <b>Our sales team answers it on a private call</b>, with the numbers in front of you &mdash; not in an ad.',
         C_CHAT, 'Book a private call', 'Book now',
         W('What will it earn?', 'Returns are answered honestly, on a call and not in the ad, which is what Meta allows and what a careful buyer trusts.',
           'Buyers who&rsquo;d rent the suite out', 'Chat screen &middot; 1:1', 'The only messaging-app screen'),
         'Returns, on a call &middot; chat screen'),
    cell(10, 'kxt', 'file', 'Kestrel Bay Resort is under construction, so <b>here&rsquo;s exactly what you&rsquo;d choose between</b>: two suites, prices in US$ and A$, and the operator.',
         C_FILE, 'Buying off-plan &middot; the facts', 'Learn more',
         W('Buying off-plan', 'An unbuilt resort is a quiet doubt, so the ad lays out exactly what the buyer is choosing between &mdash; suites, prices, operator.',
           'First-time overseas buyers', 'Document folder &middot; 1:1', 'The only folder'),
         'Off-plan &middot; buyer file'),
]

ADS3 = [
    cell(11, 'club', 'tag', 'Owners at Kestrel Bay Resort join the Owners&rsquo; Club, <b>valued up to US$15,000</b>: resort stays, priority bookings and member rates.',
         C_TAG, 'The Owners&rsquo; Club', 'Learn more',
         W('What it&rsquo;s worth', 'It puts their own figure on what owners get beyond the suite, printed on a tag.',
           'Buyers who&rsquo;d use the suite themselves', 'Swing tag &middot; 1:1', 'The only price-tag object'),
         'Valued up to US$15,000 &middot; swing tag'),
    cell(12, 'club', 'pass', 'Owners get <b>member rates across Tidewater&rsquo;s 12 venues</b> with the Owners&rsquo; Club &mdash; plus complimentary stays at Kestrel Bay Resort.',
         C_PASS, 'Member rates across Tidewater', 'Learn more',
         W('Member rates', 'People who already go to Tidewater venues understand this perk instantly, so it&rsquo;s printed as the pass they&rsquo;d carry.',
           'People who&rsquo;ve stayed at a Tidewater venue', 'Member pass &middot; 1:1', 'The only ticket'),
         'Member rates &middot; venue pass'),
    cell(13, 'gar', 'cal', 'School holidays at Kestrel Bay? <b>Owners get priority bookings</b> and complimentary resort stays. Garden Suites from US$165,000.',
         C_CAL, 'Owners book first', 'Learn more',
         W('Priority bookings', 'Australian parents know the school-holiday booking scramble, so the ad shows owners get priority.',
           'Families who travel in the school holidays', 'Calendar page &middot; 1:1', 'The only calendar'),
         'Owners book first &middot; calendar'),
    cell(14, 'club', 'inv', 'Owners at Kestrel Bay Resort get <b>invitations to Owners&rsquo; Club events</b>, as part of their membership.',
         C_INV, 'Owners&rsquo; Club events', 'Learn more',
         W('Invitations', 'It sells belonging rather than a booking, shown as a real invitation over a real Owners&rsquo; Club event.',
           'Social buyers &middot; Tidewater regulars', 'Invitation card &middot; 1:1 &middot; their event photo', 'The only stationery layout'),
         'Owners&rsquo; events &middot; invitation'),
    cell(15, 'oce', 'key', 'Own an Ocean Suite and <b>get complimentary resort stays</b> through the Owners&rsquo; Club. 52&nbsp;m&sup2;, US$260,000 (about A$375k).',
         C_KEY, 'The Ocean Suite', 'Learn more',
         W('Owner stays', 'Every hotel guest knows the key-card sleeve, so &ldquo;complimentary resort stays&rdquo; becomes something they can picture.',
           'Buyers who&rsquo;d holiday at the resort', 'Key-card sleeve &middot; 1:1', 'The only key card'),
         'Owner stays &middot; key-card sleeve'),
]

ADS4 = [
    cell(16, 'club', 'quiz', 'Rental income, holidays, or a bit of both? <b>Your answer decides which suite fits.</b> Six quick questions.',
         C_QUIZ, 'Six questions to enquire', 'Sign up',
         W('What&rsquo;s it for?', 'The form starts inside the ad: this is question two of the six they answer on the next screen.',
           'Engaged with the ads but didn&rsquo;t enquire', 'Quiz card &middot; 1:1 &middot; mirrors the instant form', 'The only form-style creative'),
         'What&rsquo;s it for? &middot; quiz card', retarget=True),
    cell(17, 'gar', 'rcpt', 'What US$165,000 gets you: <b>a 34&nbsp;m&sup2; Garden Suite with a garden terrace, and membership of the Owners&rsquo; Club.</b> About A$240k.',
         C_RCPT, 'The Garden Suite, line by line', 'Get quote',
         W('What the price gets you', 'For the buyer still weighing it up: every line comes from Kestrel&rsquo;s own listing, with nothing added.',
           'Visited, watched or opened the form', 'Receipt &middot; 1:1', 'The only receipt'),
         'Line by line &middot; receipt', retarget=True),
    cell(18, 'oce', 'lock', 'You started an enquiry about a suite at Kestrel Bay Resort. <b>Three questions to go</b> &mdash; then our sales team calls you.',
         C_LOCK, 'Finish your enquiry', 'Sign up',
         W('Finish what you started', 'Shown only to people who opened the form and left, it looks like a reminder on their own phone.',
           'Opened the form, didn&rsquo;t submit', 'Lock screen &middot; 1:1', 'The only lock screen'),
         'Half done &middot; lock screen', retarget=True),
    cell(19, 'club', 'clip', 'Before you reserve a suite, <b>ask us these five things.</b> Our sales team answers every one on a private call.',
         C_CLIP, 'Book a private call', 'Book now',
         W('Before you reserve', 'It hands the careful buyer the right questions and makes the private call the place to ask them.',
           'Engaged in the last 30 days', 'Clipboard checklist &middot; 1:1', 'The only checklist'),
         'Five questions &middot; clipboard', retarget=True),
    carousel(20, 'kxt', 'Buying a suite at Kestrel Bay from Australia takes four steps. <b>Swipe &mdash; it starts with six questions.</b>',
             ('Kestrel Bay Resort', 'How an Australian <em>buys a suite.</em>', 'Four steps, from your phone to a reserved suite.', 'How it works', 'Learn more'),
             [('ph-view.jpg', '50% 50%', '01', 'Six questions', 'The enquiry form, on your phone.', 'Tell us what you&rsquo;re after', 'Sign up'),
              ('ph-facade.jpg', '42% 50%', '02', 'A call', 'Our sales team calls you to talk it through.', 'We call you', 'Sign up'),
              ('ph-suite-b2.jpg', '50% 55%', '03', 'A private call', 'The suites and the Owners&rsquo; Club, one to one.', 'Your questions, answered', 'Book now'),
              ('ph-signing.jpg', '50% 50%', '04', 'Reserve', 'Choose your suite and reserve it with Kestrel.', 'Reserve with Kestrel', 'Learn more'),
              ('ph-pool-3.jpg', '40% 50%', 'Start here', 'Six questions.', 'Then our sales team calls you.', 'Start your enquiry', 'Sign up')],
             W('How it works', 'Five swipes answer &ldquo;what actually happens next?&rdquo;, and every card is its own headline.',
               'Anyone still deciding', 'Carousel &middot; six cards', 'The only carousel &mdash; the next card always peeks'),
             'Four steps &middot; carousel &middot; swipe it', retarget=True),
]

LEGEND = ('<div class="xa-legend">' + ''.join(f'<span style="--c:{c}"><i></i>{n}</span>' for n, c in SETS.values())
          + '<span class="lw">&middot; warm = retargeting</span></div>')

HEADS = {
 'ads1': ('The buyer campaign&ensp;&middot;&ensp;the creative', 'Angle one: <em>own a suite at Kestrel Bay.</em>',
          '&ldquo;Everything from here is finished creative, running from your page in your name &mdash; twenty ads, no two alike, because look-alike ads bid against each other and push your costs up.&rdquo; '
          'Point at the first one: <b>&ldquo;owning a suite in Bali is what stops the scroll, so the cover leads with it and Tidewater follows.&rdquo;</b> Then the second: &ldquo;both suites, both currencies, side by side.&rdquo; '
          'Then what&rsquo;s missing, as a strength: &ldquo;no yields, no return promises &mdash; Meta rejects them, and the numbers belong on your team&rsquo;s call.&rdquo;'),
 'ads2': ('The creative&ensp;&middot;&ensp;the objections', 'Angle two: <em>the doubts that stop a sale.</em>',
          '&ldquo;These five answer the reasons people don&rsquo;t enquire: the price in US dollars, who builds it, who runs it, what it earns, and buying off-plan.&rdquo; '
          'Point at the chat: <b>&ldquo;that&rsquo;s how returns are handled &mdash; never in the ad, always on your team&rsquo;s call.&rdquo;</b> Then: &ldquo;every figure here is from your own site &mdash; only the Australian-dollar conversions are ours, and they all say &lsquo;about&rsquo;.&rdquo;'),
 'ads3': ('The creative&ensp;&middot;&ensp;the owners&rsquo; club', 'Angle three: <em>the owners&rsquo; membership.</em>',
          '&ldquo;The Owners&rsquo; Club is what makes a Kestrel Bay suite different, so it gets its own angle &mdash; one perk per ad.&rdquo; '
          'Point at the tag: <b>&ldquo;that&rsquo;s your own figure &mdash; valued up to US$15,000.&rdquo;</b> Then across the row: &ldquo;member rates, priority bookings, events, owner stays.&rdquo;'),
 'ads4': ('The creative&ensp;&middot;&ensp;the warm audience', 'Angle four: <em>for buyers still deciding.</em>',
          '&ldquo;These only show to people who&rsquo;ve already looked &mdash; clicked, watched, or opened the form.&rdquo; '
          'Point at the lock screen: <b>&ldquo;anyone who opens the form and leaves sees this &mdash; three questions to go.&rdquo;</b> Then the carousel: &ldquo;four steps, and every step after the form is your team&rsquo;s.&rdquo;'),
}

PAGES = [('ads1', 's15_ads1.html', ADS1, ['mag', 'two', 'prints', 'four', 'dir']),
         ('ads2', 's16_ads2.html', ADS2, ['num', 'pict', 'myth', 'chat', 'file']),
         ('ads3', 's17_ads3.html', ADS3, ['tag', 'pass', 'cal', 'inv', 'key']),
         ('ads4', 's18_ads4.html', ADS4, ['quiz', 'rcpt', 'lock', 'clip'])]

# the one motion layer: each creative settles in once, then rests (none of it runs under ?noanim or reduced motion)
MOTION = {
 'ads1': '''
    body.anim @A .xa-grid.in .xa-mag .xa-ph { animation:xaZoom 7s ease-out var(--ad) both; }
    body.anim @A .xa-grid.in .xa-mag .m-lines div { animation:xaUp .6s ease calc(var(--ad) + .3s) both; }
    body.anim @A .xa-grid.in .xa-mag .m-lines div:nth-child(2) { animation-delay:calc(var(--ad) + .5s); } body.anim @A .xa-grid.in .xa-mag .m-lines div:nth-child(3) { animation-delay:calc(var(--ad) + .7s); }
    body.anim @A .xa-grid.in .xa-two .w-c { animation:xaUp .6s ease calc(var(--ad) + .2s) both; }
    body.anim @A .xa-grid.in .xa-two .w-c.hi { animation-delay:calc(var(--ad) + .45s); }
    body.anim @A .xa-grid.in .xa-two .w-or { animation:xaPop .45s cubic-bezier(.3,1.6,.5,1) calc(var(--ad) + .9s) both; }
    body.anim @A .xa-grid.in .xa-prints .pol { animation:xaDrop .7s cubic-bezier(.2,.75,.2,1) both; }
    body.anim @A .xa-grid.in .xa-prints .pol.a { animation-delay:var(--ad); } body.anim @A .xa-grid.in .xa-prints .pol.b { animation-delay:calc(var(--ad) + .2s); }
    body.anim @A .xa-grid.in .xa-prints .pol.c { animation-delay:calc(var(--ad) + .4s); }
    body.anim @A .xa-grid.in .xa-prints .p-st { animation:xaStamp .45s cubic-bezier(.3,1.6,.5,1) calc(var(--ad) + 1s) both; }
    body.anim @A .xa-grid.in .xa-four .f-c { animation:xaPop .6s cubic-bezier(.3,1.4,.5,1) calc(var(--ad) + .4s) both; }
    body.anim @A .xa-grid.in .xa-dir li { animation:xaUp .45s ease both; animation-delay:calc(var(--ad) + .3s); }''',
 'ads2': '''
    body.anim @A .xa-grid.in .xa-num .u-q { animation:xaUp .7s ease calc(var(--ad) + 1.2s) both; }
    body.anim @A .xa-grid.in .xa-pict .i-units svg { animation:xaPop .4s ease calc(var(--ad) + .3s) both; }
    body.anim @A .xa-grid.in .xa-myth .y-mt { animation:xaStrike 1s ease calc(var(--ad) + .2s) both; }
    body.anim @A .xa-grid.in .xa-myth .y-fb { animation:xaUp .6s ease calc(var(--ad) + .9s) both; }
    body.anim @A .xa-grid.in .xa-chat .h-b { animation:xaPop .4s ease both; }
    body.anim @A .xa-grid.in .xa-chat .h-b:nth-of-type(1) { animation-delay:calc(var(--ad) + .1s); } body.anim @A .xa-grid.in .xa-chat .h-b:nth-of-type(2) { animation-delay:calc(var(--ad) + .6s); }
    body.anim @A .xa-grid.in .xa-chat .h-b:nth-of-type(3) { animation-delay:calc(var(--ad) + 1.1s); } body.anim @A .xa-grid.in .xa-chat .h-b:nth-of-type(4) { animation-delay:calc(var(--ad) + 1.6s); }
    body.anim @A .xa-grid.in .xa-file .fl-fd { animation:xaRise .8s cubic-bezier(.2,.75,.2,1) var(--ad) both; }''',
 'ads3': '''
    body.anim @A .xa-grid.in .xa-tag .g-tw { animation:xaSwing 1.6s cubic-bezier(.3,1.3,.5,1) calc(var(--ad) + .2s) both; }
    body.anim @A .xa-grid.in .xa-pass .b-tk { animation:xaRise .8s cubic-bezier(.2,.75,.2,1) var(--ad) both; }
    body.anim @A .xa-grid.in .xa-cal .l-pg:not(.bk) { animation:xaDrop .8s cubic-bezier(.2,.75,.2,1) var(--ad) both; }
    body.anim @A .xa-grid.in .xa-cal .l-ci { animation:xaPop .5s ease calc(var(--ad) + .9s) both; }
    body.anim @A .xa-grid.in .xa-inv .v-cd { animation:xaRise .9s cubic-bezier(.2,.75,.2,1) var(--ad) both; }
    body.anim @A .xa-grid.in .xa-key .y-kc { animation:xaRise .8s cubic-bezier(.2,.75,.2,1) calc(var(--ad) + .5s) both; }''',
 'ads4': '''
    body.anim @A .xa-grid.in .xa-quiz .z-o.on { animation:xaPick .5s ease calc(var(--ad) + 1s) both; }
    body.anim @A .xa-grid.in .xa-quiz .z-pr i::after { animation:xaGrow 1s ease calc(var(--ad) + .3s) both; }
    body.anim @A .xa-grid.in .xa-rcpt .e-rc { animation:xaPrint 1.4s steps(14) var(--ad) both; }
    body.anim @A .xa-grid.in .xa-lock .o-n.a { animation:xaDrop .6s cubic-bezier(.2,.75,.2,1) calc(var(--ad) + .3s) both; }
    body.anim @A .xa-grid.in .xa-lock .o-w { animation:xaUp .6s ease calc(var(--ad) + .8s) both; }
    body.anim @A .xa-grid.in .xa-clip .p-bd { animation:xaRise .8s cubic-bezier(.2,.75,.2,1) var(--ad) both; }''',
}
KEYS = '''
  @keyframes xaZoom { from { transform:scale(1.12); } }
  @keyframes xaUp { from { opacity:0; transform:translateY(3cqw); } }
  @keyframes xaDrop { from { opacity:0; translate:0 -6cqw; } }
  @keyframes xaRise { from { opacity:0; translate:0 12cqw; } }
  @keyframes xaStamp { from { opacity:0; scale:1.8; } }
  @keyframes xaPop { from { opacity:0; scale:.7; } }
  @keyframes xaStrike { from { text-decoration-color:transparent; } }
  @keyframes xaSwing { 0% { rotate:-14deg; } 45% { rotate:6deg; } 75% { rotate:-3deg; } 100% { rotate:0deg; } }
  @keyframes xaPick { 0%,40% { background:#fff; border-color:#E2DACE; } }
  @keyframes xaGrow { from { width:0; } }
  @keyframes xaPrint { from { clip-path:inset(0 0 100% 0); } to { clip-path:inset(0 0 0 0); } }
'''

TAIL = """
    </div>
  </div>
</section>
"""

for sid, fn, ads, kinds in PAGES:
    k, h2, note = HEADS[sid]
    style = (SHARED + css(KEYS) if sid == 'ads1' else '') + css(''.join(K[x] for x in kinds))
    style += css('\n  @media (prefers-reduced-motion:no-preference) {' + MOTION[sid] + '\n  }\n')
    head = f'''<section class="slide" id="{sid}">
<style>{style}</style>
  <div class="wrap">
    <div class="head rv">
      <div class="k">{k}</div>
      <h2>{h2}</h2>{LEGEND if sid == 'ads1' else ''}
      <div class="note"><b>Say this</b>{note}</div>
    </div>
    <div class="adgrid xa-grid rv">'''
    open(os.path.join(SRC, fn), 'w', encoding='utf8').write(head + ''.join(ads) + TAIL)
print('ads written: 20')
