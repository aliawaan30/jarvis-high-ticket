import json,re,os,html,sys
from pathlib import Path
STUDIO=Path(__file__).resolve().parent.parent/'studio'
OUT=sys.argv[1]
o=json.load(open(f'{STUDIO}/data/outline.json'))
def lesson(i):
    p=f'{STUDIO}/data/lessons/{i}.json'
    return json.load(open(p)) if os.path.exists(p) else {'id':i,'title':i,'lede':'','deliverable':'','body':''}
def words(b): return len(re.sub('<[^>]+>',' ',b).split())
rail=[];secs=[];first=None;total=0
for m in o['modules']:
    review=m.get('review_status',{}); state=review.get('state'); badge=''
    if state in ('done','testing'):
        icon='✓' if state=='done' else '●'
        badge=f'<span class="module-status {state}" aria-label="{html.escape(review["label"])}">{icon} {html.escape(review["label"])}</span>'
    rail.append(f'<div class="mod"><div class="mnum">{html.escape(m["num"])} {badge}</div><div class="mname">{html.escape(m["name"])}</div><ol>')
    for n,l in enumerate(m['lessons'],1):
        d=lesson(l['id']); w=words(d.get('body','')); total+=w; done=bool(d.get('body','').strip())
        first=first or l['id']
        rail.append(f'<li><a href="#{l["id"]}" data-id="{l["id"]}" class="{"done" if done else "todo"}"><span class="n">{n}</span>{html.escape(d.get("title") or l["title"])}</a></li>')
        body=d.get('body','').replace('src="/data/img/','src="data/img/')
        status='' if done else '<p class="todo-tag">Not written yet. Title and promise only.</p>'
        deliv=''  # deliverable box removed from student view, 31 Oct 2026
        module_path=''
        if m.get('slug')=='m2':
            labels=['Understand','Explore services','Choose a niche','See an example','Build yours']
            items=[]
            for step,entry in enumerate(m['lessons']):
                label=labels[step] if step<len(labels) else entry['title']
                active=' aria-current="step"' if entry['id']==l['id'] else ''
                items.append(f'<a href="#{entry["id"]}"{active}><span>{step+1}</span>{html.escape(label)}</a>')
            module_path='<nav class="module-path" aria-label="Your offer-building path">'+''.join(items)+'</nav>'
        secs.append(f'''<article class="lesson" id="{l["id"]}" hidden>
<div class="crumb">{html.escape(m["num"])} · {html.escape(m["name"])} · Lesson {n} of {len(m["lessons"])}</div>
{module_path}
<h1>{html.escape(d.get("title") or l["title"])}</h1>
{f'<p class="lede">{html.escape(d["lede"])}</p>' if d.get("lede") else ''}
{deliv}{status}
<button type="button" class="jarvis-help" data-lesson="{l['id']}">Copy prompt for Jarvis</button>
<div class="body">{body}</div>
<div class="pager"><a class="prev" href="#"></a><a class="next" href="#"></a></div>
</article>''')
    rail.append('</ol></div>')
blurb=o.get('title','High Ticket Course')
page=f'''<title>High Ticket Course</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400&family=Instrument+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Layout: fixed reading rail on the left, one lesson at a time on the right; rail becomes a drawer on phones. Tokens mirror the studio. */
:root{{--paper:#fbfbfc;--card:#ffffff;--ink:#0e1016;--ink-2:#5a5d6b;--ink-3:#8b8e9c;--accent:#4b2fc4;--accent-soft:#efecfb;--brass:#8a6210;--brass-soft:#f8f1df;--brass-line:#ecdcb8;--line:#e6e4ee;--line-2:#d3d0e0;--rail:#f3f2f8;--dark:#12131a;--dark-fg:#e9e9f1;--dark-label:#8e8ca8;
--display:'Fraunces',Georgia,serif;--sans:'Instrument Sans','Helvetica Neue',Arial,sans-serif;--mono:'IBM Plex Mono',ui-monospace,Menlo,monospace}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--paper:#101117;--card:#171821;--ink:#eceaf3;--ink-2:#b4b2c2;--ink-3:#8b8e9c;--accent:#a99aee;--accent-soft:#241f3d;--brass:#d6ad5c;--brass-soft:#2a2214;--brass-line:#4a3a1c;--line:#262735;--line-2:#363749;--rail:#13141b;--dark:#06070b;color-scheme:dark}}}}
:root[data-theme="dark"]{{--paper:#101117;--card:#171821;--ink:#eceaf3;--ink-2:#b4b2c2;--ink-3:#8b8e9c;--accent:#a99aee;--accent-soft:#241f3d;--brass:#d6ad5c;--brass-soft:#2a2214;--brass-line:#4a3a1c;--line:#262735;--line-2:#363749;--rail:#13141b;--dark:#06070b;color-scheme:dark}}
body{{background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:17.5px;line-height:1.68;margin:0}}
a{{color:var(--accent)}}
.wrap{{display:flex;min-height:100vh}}
.rail{{width:300px;flex:0 0 300px;background:var(--rail);border-right:1px solid var(--line);padding-block:22px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:16px;position:sticky;top:0;height:100vh;overflow-y:auto;box-sizing:border-box}}
.brand{{font-family:var(--display);font-weight:600;font-size:18px;letter-spacing:-.01em;margin:0 0 2px}}
.brand small{{display:block;font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);margin-top:4px;font-weight:400}}
.mod{{margin-top:20px}}
.mnum{{font-family:var(--mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--accent)}}
.module-status{{display:inline-block;margin-left:5px;font-size:9px;letter-spacing:0;text-transform:none}}.module-status.done{{color:#42bc89}}.module-status.testing{{color:#e4a64e}}
.mname{{font-family:var(--display);font-size:15.5px;font-weight:600;margin:2px 0 6px}}
.rail ol{{list-style:none;margin:0;padding:0}}
.rail li a{{display:flex;gap:9px;align-items:baseline;padding:5px 8px;border-radius:7px;color:var(--ink-2);text-decoration:none;font-size:13.5px;line-height:1.35}}
.rail li a .n{{font-family:var(--mono);font-size:10.5px;color:var(--ink-3);min-width:14px}}
.rail li a.todo{{color:var(--ink-3)}}
.rail li a.todo:after{{content:'';width:6px;height:6px;border-radius:50%;border:1px solid var(--line-2);margin-left:auto;flex:0 0 auto;align-self:center}}
.rail li a.done:after{{content:'';width:6px;height:6px;border-radius:50%;background:var(--accent);margin-left:auto;flex:0 0 auto;align-self:center}}
.rail li a:hover,.rail li a.active{{background:var(--accent-soft);color:var(--ink)}}
.rail li a:focus-visible{{outline:2px solid var(--accent);outline-offset:1px}}
main{{flex:1;min-width:0;padding-block:48px 80px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}}
.lesson{{max-width:720px;margin:0 auto;scroll-margin-top:80px}}

[hidden]{{display:none!important}}
.module-path{{display:grid;grid-template-columns:repeat(5,1fr);gap:7px;margin:0 0 28px}}
.module-path a{{display:flex;align-items:center;gap:8px;border:1px solid var(--line-2);border-radius:8px;padding:11px 9px;text-decoration:none;color:var(--ink-2);font-size:12px;line-height:1.3}}
.module-path a span{{font-family:var(--mono);color:var(--ink-3);font-size:10px}}
.module-path a[aria-current=step]{{background:var(--accent-soft);border-color:var(--accent);color:var(--accent)}}
.section-nav{{display:flex;flex-wrap:wrap;gap:7px;margin:26px 0 12px}}
.section-nav button{{background:var(--card);color:var(--ink-2);border:1px solid var(--line-2);font:inherit;font-size:13px;line-height:1.35;padding:9px 12px;border-radius:7px;cursor:pointer;text-align:left}}
.section-nav button[aria-current=step]{{background:var(--accent-soft);color:var(--accent);border-color:var(--accent)}}
.section-nav button:focus-visible,.section-controls button:focus-visible{{outline:2px solid var(--accent);outline-offset:3px}}
.section-count{{font:11px var(--mono);color:var(--ink-3);letter-spacing:.04em;margin-bottom:22px!important}}
.jarvis-help{{font:inherit;font-size:13px;background:var(--accent-soft);color:var(--accent);border:1px solid var(--line-2);padding:9px 12px;border-radius:7px;margin:0 0 20px;cursor:pointer}}
.learning-section{{scroll-margin-top:85px}}.body .section-purpose{{border-left:3px solid var(--accent);padding:9px 15px;background:var(--accent-soft);color:var(--ink-2);font-size:15px;margin-bottom:25px}}
.body .learning-section>h2:first-of-type{{margin-top:0}}.learning-section:focus{{outline:none}}
.section-controls{{display:flex;justify-content:space-between;align-items:center;gap:16px;border-top:1px solid var(--line);margin-top:32px;padding-top:23px}}
.section-controls button{{font:inherit;font-size:14px;line-height:1.4;border-radius:7px;border:1px solid var(--line-2);background:var(--card);color:var(--ink-2);padding:12px 16px;cursor:pointer}}
.section-controls .section-next{{margin-left:auto;background:var(--accent);border-color:var(--accent);color:var(--paper);max-width:80%}}
@media(max-width:600px){{.module-path{{grid-template-columns:1fr 1fr;gap:6px}}.module-path a{{font-size:12px}}.section-nav{{gap:6px}}.section-nav button{{font-size:12px;padding:9px 10px}}.section-controls button{{font-size:13px;padding:11px 12px}}}}
@media print{{.module-path,.section-nav,.section-count,.section-controls,.pager,.menu,.rail{{display:none!important}}.lesson:not([hidden]) .learning-section[hidden]{{display:block!important}}main{{padding:0}}}}

.crumb{{font-family:var(--mono);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);margin:0 0 18px}}
h1{{font-family:var(--display);font-size:44px;font-weight:600;letter-spacing:-.02em;line-height:1.08;margin:0 0 18px;text-wrap:balance}}
.lede{{font-family:var(--sans);font-style:normal;font-size:21px;line-height:1.45;color:var(--ink-2);border-left:3px solid var(--accent);padding-left:18px;margin:0 0 24px}}
.deliv{{background:var(--brass-soft);border:1px solid var(--brass-line);border-radius:10px;padding:14px 18px;margin:0 0 30px;font-size:16px}}
.deliv .dl{{font-family:var(--mono);font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--brass);margin-bottom:4px}}
.todo-tag{{font-family:var(--mono);font-size:12px;color:var(--ink-3);border:1px dashed var(--line-2);border-radius:8px;padding:10px 14px}}
.body>*:first-child{{margin-top:0}}
.body p{{margin:0 0 1.05em}}
.body h2{{font-family:var(--display);font-size:27px;font-weight:600;letter-spacing:-.015em;line-height:1.2;margin:1.9em 0 .5em;text-wrap:balance}}
.body h3{{font-family:var(--sans);font-size:14px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--accent);margin:1.8em 0 .5em}}
.body ul,.body ol{{margin:0 0 1.1em;padding-left:1.3em}}
.body li{{margin:0 0 .42em}}
.body hr{{border:0;height:1px;background:var(--line);margin:2.4em 0}}
.body blockquote{{margin:1.4em 0;padding:0 0 0 20px;border-left:3px solid var(--line-2);font-family:var(--display);font-size:20px;font-style:italic;color:var(--ink-2)}}
.body figure.fig{{margin:2em 0;padding:0}}
.body figure.fig img{{display:block;width:100%;max-width:100%;height:auto;border-radius:12px;border:1px solid var(--line);background:#fff}}
.body figure.fig figcaption{{font-family:var(--mono);font-size:11.5px;letter-spacing:.04em;color:var(--ink-3);margin:10px 2px 0}}
.tblwrap{{overflow-x:auto}}
.body table.tbl{{width:100%;border-collapse:collapse;margin:1.6em 0;font-size:15.5px;font-variant-numeric:tabular-nums}}
.body table.tbl th{{font-size:12px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);text-align:left;padding:8px 10px;border-bottom:2px solid var(--line-2)}}
.body table.tbl td{{padding:10px;border-bottom:1px solid var(--line);vertical-align:top}}
.body .b-script{{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--brass);border-radius:10px;padding:34px 20px 16px;margin:1.6em 0;position:relative}}
.body .b-script:before{{content:'SAY THIS';position:absolute;top:11px;left:18px;font-family:var(--mono);font-size:10px;letter-spacing:.14em;color:var(--brass)}}
.body .b-script p{{margin:0 0 .8em}}
.body .b-prompt{{background:var(--dark);color:var(--dark-fg);border-radius:10px;padding:34px 20px 18px;margin:1.5em 0;font-family:var(--mono);font-size:14px;line-height:1.62;white-space:pre-wrap;position:relative;overflow-wrap:anywhere}}
.body .b-prompt:before{{content:'PASTE INTO JARVIS';position:absolute;top:12px;left:20px;font-size:9px;letter-spacing:.16em;color:var(--dark-label)}}
.body .b-prompt p{{margin:0 0 .8em}}
.body .b-note{{background:var(--brass-soft);border:1px solid var(--brass-line);border-radius:10px;padding:30px 18px 16px;margin:1.5em 0;font-size:16px;position:relative}}
.body .b-note:before{{content:'NOTE';position:absolute;top:11px;left:18px;font-family:var(--mono);font-size:9px;letter-spacing:.16em;color:var(--brass)}}
.body .b-ex{{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--accent);border-radius:0 10px 10px 0;padding:30px 18px 16px;margin:1.5em 0;font-size:16px;position:relative}}
.body .b-ex:before{{content:'WORKED EXAMPLE';position:absolute;top:11px;left:18px;font-family:var(--mono);font-size:9px;letter-spacing:.16em;color:var(--accent)}}
.pager{{display:flex;justify-content:space-between;gap:16px;margin-top:56px;padding-top:22px;border-top:1px solid var(--line);font-size:14.5px}}
.pager a{{text-decoration:none;max-width:48%}}
.pager a:empty{{visibility:hidden}}
.pager .prev:before{{content:'Previous: ';color:var(--ink-3)}}
.pager .next:before{{content:'Next: ';color:var(--ink-3)}}
.menu{{display:none;position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--paper);border-bottom:1px solid var(--line);padding:10px max(16px,env(safe-area-inset-right,0px)) 10px max(16px,env(safe-area-inset-left,0px))}}
.menu button{{font:inherit;font-size:14px;background:var(--card);color:var(--ink);border:1px solid var(--line-2);border-radius:8px;padding:7px 12px;cursor:pointer}}
@media (max-width:860px){{
 .wrap{{display:block}} .menu{{display:block}}
 .rail{{position:fixed;inset:0 auto 0 0;width:min(320px,88vw);height:100vh;z-index:20;transform:translateX(-105%);transition:transform .2s;box-shadow:0 0 40px rgba(0,0,0,.25)}}
 .rail.open{{transform:none}}
 h1{{font-size:34px}} main{{padding-block:28px 60px}}
 .pager{{flex-direction:column}} .pager a{{max-width:100%}}
}}
@media (prefers-reduced-motion:reduce){{.rail{{transition:none}}}}
</style>
<div class="menu"><button id="menubtn" type="button">Lessons</button></div>
<div class="wrap">
<nav class="rail" id="rail">
<div class="brand">High Ticket Course<small>Reading copy · {len(secs)} lessons · {total:,} words</small></div>
{''.join(rail)}
</nav>
<main>
{''.join(secs)}
</main>
</div>
<script>
(function(){{
 var links=[].slice.call(document.querySelectorAll('.rail a[data-id]'));
 var ids=links.map(function(a){{return a.dataset.id}});
 var titles={{}};links.forEach(function(a){{titles[a.dataset.id]=a.textContent.replace(/^\\d+/,'')}});
 document.querySelectorAll('table.tbl').forEach(function(t){{var w=document.createElement('div');w.className='tblwrap';t.parentNode.insertBefore(w,t);w.appendChild(t)}});

 document.querySelectorAll('.jarvis-help').forEach(function(button){{button.onclick=async function(){{
  var art=document.getElementById(button.dataset.lesson),current=art.querySelector('[data-learning-section]:not([hidden])');
  var prompt='Use the course guide skill to help me with '+button.dataset.lesson+(current?' / '+current.dataset.sectionTitle:'')+'. Read the actual lesson and reuse my saved business context. Explain what I need to understand, then help me do the next task. Ask me what I am stuck on before generating work.';
  try{{await navigator.clipboard.writeText(prompt);button.textContent='Copied. Paste into Jarvis';setTimeout(function(){{button.textContent='Copy prompt for Jarvis'}},2500)}}catch(e){{window.prompt('Copy this into Jarvis',prompt)}}
 }}}});
 var sectionGroups={{}};
 document.querySelectorAll('.lesson').forEach(function(art){{
  var blocks=[].slice.call(art.querySelectorAll('[data-learning-section]'));
  if(!blocks.length)return;
  var nav=document.createElement('nav');nav.className='section-nav';nav.setAttribute('aria-label','Sections in this lesson');
  var count=document.createElement('p');count.className='section-count';count.setAttribute('aria-live','polite');
  var controls=document.createElement('div');controls.className='section-controls';
  var back=document.createElement('button');back.type='button';back.className='section-back';back.textContent='Back';
  var next=document.createElement('button');next.type='button';next.className='section-next';
  controls.append(back,next);
  var group={{blocks:blocks,buttons:[],count:count,back:back,next:next,index:0,art:art}};sectionGroups[art.id]=group;
  blocks.forEach(function(block,i){{
   block.tabIndex=-1;
   var button=document.createElement('button');button.type='button';button.textContent=block.dataset.sectionTitle;
   button.onclick=function(){{setSection(art.id,i,true)}};nav.appendChild(button);group.buttons.push(button);
  }});
  blocks[0].before(nav,count);blocks[blocks.length-1].after(controls);
  back.onclick=function(){{setSection(art.id,group.index-1,true)}};
  next.onclick=function(){{setSection(art.id,group.index+1,true)}};
 }});
 function setSection(id,index,updateRoute){{
  var g=sectionGroups[id];if(!g)return;
  index=Math.max(0,Math.min(index,g.blocks.length-1));g.index=index;
  g.blocks.forEach(function(block,i){{block.hidden=i!==index}});
  g.buttons.forEach(function(button,i){{if(i===index)button.setAttribute('aria-current','step');else button.removeAttribute('aria-current')}});
  g.count.textContent='Section '+(index+1)+' of '+g.blocks.length;
  g.back.hidden=index===0;g.next.hidden=index===g.blocks.length-1;
  g.next.textContent=index<g.blocks.length-1?'Continue: '+g.blocks[index+1].dataset.sectionTitle:'';
  g.art.querySelector('.pager').hidden=index!==g.blocks.length-1;
  if(updateRoute){{history.replaceState(null,'','#'+id+'/'+g.blocks[index].dataset.learningSection);g.blocks[index].focus({{preventScroll:true}});g.buttons[index].scrollIntoView({{block:'nearest',inline:'nearest'}});window.scrollTo(0,0)}}
 }}

 function show(route){{
  var parts=route.split('/'),id=parts[0],section=parts[1]||'';
  if(ids.indexOf(id)<0) id=ids[0];
  document.querySelectorAll('.lesson').forEach(function(s){{s.hidden=s.id!==id}});
  links.forEach(function(a){{a.classList.toggle('active',a.dataset.id===id)}});
  var i=ids.indexOf(id),art=document.getElementById(id);
  var p=art.querySelector('.prev'),n=art.querySelector('.next');
  if(i>0){{p.href='#'+ids[i-1];p.textContent=titles[ids[i-1]]}}else{{p.textContent='';p.removeAttribute('href')}}
  if(i<ids.length-1){{n.href='#'+ids[i+1];n.textContent=titles[ids[i+1]]}}else{{n.textContent='';n.removeAttribute('href')}}
  document.getElementById('rail').classList.remove('open');
  var group=sectionGroups[id];
  if(group){{var index=group.blocks.findIndex(function(block){{return block.dataset.learningSection===section}});setSection(id,index<0?0:index,false)}}
  window.scrollTo(0,0);
  try{{localStorage.setItem('htc-last',id)}}catch(e){{}}
 }}
 var start=location.hash.replace('#','');
 if(!start){{try{{start=localStorage.getItem('htc-last')||''}}catch(e){{}}}}
 show(start);
 window.addEventListener('hashchange',function(){{show(location.hash.replace('#',''))}});
 document.getElementById('menubtn').addEventListener('click',function(){{document.getElementById('rail').classList.toggle('open')}});
}})();
</script>
'''
open(OUT,'w').write(page)
print('lessons',len(secs),'words',total,'bytes',len(page))
