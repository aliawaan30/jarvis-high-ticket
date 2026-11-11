"""Apply Blake's compact VSL / no-VSL offer-testing split to the retained example."""
from pathlib import Path
import re
import shutil

HERE=Path(__file__).parent
src=HERE/'archive/before-compact-2026-10-31'
dist=HERE/'dist'
html=(src/'index.html').read_text()
for pattern in [
    r'<section class="section shell center">.*?</section>',
    r'<section class="section light">.*?</section>',
    r'<section class="section shell">.*?</section>',
    r'<section class="final shell">.*?</section>',
    r'<p class="undercta">.*?</p>',
    r'<div class="microstrip">.*?</div>'
]:
    html,count=re.subn(pattern,'',html,flags=re.S)
    assert count==1,(pattern,count)
assert 'Questions worth asking' not in html
assert '<details' not in html
html=html.replace('</head>','<style>.hero{padding-bottom:44px}@media(max-width:700px){.hero{padding-bottom:32px}}</style></head>')
testing=re.sub(r'<div class="vsl">.*?</div><p class="caption">.*?</p>','',html,count=1,flags=re.S)
assert testing!=html
testing=re.sub(r'<dialog id="demo">.*?</dialog>','',testing,count=1,flags=re.S)
testing=testing.replace('<title>Roofline | Reopen the estimates you already earned</title>','<title>Roofline | Offer Testing Landing Page</title>')
testing=testing.replace('PRIVATE OFFER TEST · Fictional brand. No campaign or client system is live.','OFFER TESTING LANDING PAGE · Fictional brand. No data is sent or saved.')
(dist/'index.html').write_text(html)
(dist/'offer-testing.html').write_text(testing)

# Share the form implementation without assuming the optional VSL controls exist.
js=(src/'app.js').read_text()
begin=js.index("document.querySelector('#show-demo').onclick")
end=js.index('const questions=')
handlers=js[begin:end]
js=js[:begin]+"if(dialog && document.querySelector('#show-demo')){"+handlers+'}\n'+js[end:]
(dist/'app.js').write_text(js)

public=Path('/Users/blakestephens/co-founder/projects/high-ticket-course/hosting/funnel-examples/dist')
for name in ['index.html','offer-testing.html']:
    body=(dist/name).read_text()
    label='OFFER TESTING LANDING PAGE' if name=='offer-testing.html' else 'VSL LANDING PAGE EXAMPLE'
    body=re.sub(r'<div class="reviewbar">.*?</div>',f'<div class="reviewbar">{label} · Fictional brand. No data is sent or saved. Calendar not connected.</div>',body,count=1,flags=re.S)
    body=body.replace('Private creative benchmark.','Course creative example.')
    (public/name).write_text(body)
shutil.copy2(dist/'app.js',public/'app.js')
print('Built compact VSL page and Offer Testing Landing Page; shared optional-video-safe form script.')
