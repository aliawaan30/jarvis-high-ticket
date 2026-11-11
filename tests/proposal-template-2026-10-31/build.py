"""Render a private sales proposal from discovery inputs, without client-facing drafting controls."""
from pathlib import Path
from html import escape as esc
import json
import argparse
import shutil
from copy import deepcopy

HERE=Path(__file__).parent
OUT=Path('/Users/blakestephens/Downloads/Jarvis-Proposal-Template')
ACT=Path('/Users/blakestephens/Downloads/ACT-CRM-Proposal')

def text(value, fallback='[TO CONFIRM]'):
    return esc(str(value)) if value is not None and value != '' else f'<span class="missing">{fallback}</span>'

def money(n):
    return f'A${n:,.0f}' if n is not None else '<span class="missing">[AMOUNT TO CONFIRM]</span>'

def ready_errors(d):
    errors=[]
    c=d['cost'];p=d['commercial']
    if not c.get('confirmed'):errors.append('Buyer has not confirmed the current-cost baseline.')
    if any(c.get(k) is None for k in ['volume','current_minutes','target_minutes','hourly_cost']):errors.append('Cost inputs are incomplete.')
    if not p.get('approved'):errors.append('Commercial terms are not approved.')
    if any(p.get(k) is None for k in ['build','support','tools']):errors.append('Build/support/software figures are incomplete.')
    if not d['timeline'].get('confirmed'):errors.append('Delivery dates are not approved.')
    return errors

def render(d):
    c=d['cost'];p=d['commercial'];errors=ready_errors(d)
    mode='Worked example · fictional company and figures' if d.get('example') else ('Internal review draft · inputs outstanding' if errors else 'Private proposal')
    pages=[]
    def page(title,body):pages.append((title,body))
    page(d['project'],f'''<p class="large">Prepared for {text(d['client'])}</p><p class="statement">{text(d['purpose'])}</p><div class="agreement"><span>THE OUTCOME WE DISCUSSED</span><p>{text(d['outcome'])}</p></div><p class="subtle">{text(d['supplier'])} · {text(d['date'])}</p>''')
    problem_rows=''.join(f'<tr><th>{text(x["problem"])}</th><td>{text(x["detail"])}</td><td>{text(x["impact"])}</td></tr>' for x in d['problems'])
    page('Problems',f'''<p class="intro">From our first conversation:</p><table><thead><tr><th>What is happening</th><th>What your team has to do</th><th>What it causes</th></tr></thead><tbody>{problem_rows}</tbody></table>''')
    valid=all(c.get(k) is not None for k in ['volume','current_minutes','target_minutes','hourly_cost'])
    if valid:
        now=c['volume']*c['current_minutes']/60;future=c['volume']*c['target_minutes']/60;released=now-future
        annual=now*c['hourly_cost']*12;value=released*c['hourly_cost']*12
        page('Current cost',f'''<div class="big-number">{money(annual)}<span>per year in manual handling</span></div><p class="equation">{c['volume']:g} jobs / month × {c['current_minutes']:g} minutes / job ÷ 60 × {money(c['hourly_cost'])} / hour × 12</p><div class="bars"><div><b>Current handling</b><span>{now:g} hours / month</span><i style="width:{now/max(now,future,1)*100}%"></i></div><div><b>Proposed handling target</b><span>{future:g} hours / month</span><i class="blue" style="width:{future/max(now,future,1)*100}%"></i></div></div><p class="result">Target: release <b>{released:g} hours a month</b>, equivalent to <b>{money(value)} a year</b> of staff capacity.</p><p class="footnote">Remaining handling includes staff review. Capacity value becomes cash savings only if an actual expense is removed. Build and running costs are shown separately.</p>''')
    else:
        page('Current cost','''<div class="big-number missing">[ANNUAL COST]<span>from the figures agreed on call one</span></div><p class="equation">[Jobs / month] × [manual minutes / job] ÷ 60 × [loaded hourly cost] × 12</p><div class="agreement"><span>THE WORK TO INCLUDE</span><p>Request entry, proposal preparation, document handling, signing/payment checks, and booking coordination. Count each minute once.</p></div><p class="result">[Hours released / month] after allowing for staff review and exceptions.</p>''')
    scope=''.join(f'<tr><th>{text(x["name"])}</th><td>{text(x["does"])}</td><td>{text(x["fixes"])}</td></tr>' for x in d['deliverables'])
    page('Proposed build out',f'''<p class="intro">{text(d['build_summary'])}</p><table><thead><tr><th>Included</th><th>What we will build</th><th>Problem it solves</th></tr></thead><tbody>{scope}</tbody></table><p class="footnote"><b>ACT staff retain control:</b> {text(d['human_control'])}</p><p class="footnote"><b>Scope boundary:</b> {text(d['scope_boundary'])}</p>'''.replace('ACT staff retain control:', 'Staff retain control:'))
    workflow=''.join(f'<button type="button" class="step{(" active" if i==0 else "")}" data-step="{i}" aria-pressed="{str(i==0).lower()}"><small>{i+1:02}</small><b>{text(x["title"])}</b></button>' for i,x in enumerate(d['workflow']))
    first=d['workflow'][0]
    page('How it will work',f'''<p class="intro">One job through the proposed system.</p><div class="steps">{workflow}</div><div class="screen"><header><b>{text(d['client'])}</b><span>Sample job · proposed layout</span></header><div><small id="screen-owner">{text(first['owner'])}</small><h2 id="screen-title">{text(first['title'])}</h2><p id="screen-detail">{text(first['detail'])}</p><div class="record-fields"><span>Documents<br><b>On the job record</b></span><span>Responsibility<br><b>Named owner</b></span><span>History<br><b>Recorded with the job</b></span></div></div></div><p class="footnote">Illustrative workflow using sample data. No live account connection is claimed.</p>''')
    schedule=''.join(f'<tr><th>{text(x["when"])}</th><td><b>{text(x["stage"])}</b><br>{text(x["work"])}</td><td>{text(x["approval"])}</td></tr>' for x in d['timeline']['rows'])
    page('Timeline',f'''<table><thead><tr><th>When</th><th>Delivery</th><th>Review point</th></tr></thead><tbody>{schedule}</tbody></table><p class="footnote"><b>Required from your team:</b> {text(d['dependencies'])}</p><p class="footnote">{text(d['timeline']['condition'])}</p>''')
    terms=''.join(f'<div><span>{text(x["label"])}</span><b>{money(p["build"]*x["share"]) if p["build"] is not None else "[AMOUNT]"}</b></div>' for x in p['payments'])
    year=p['build']+12*(p['support']+p['tools']) if all(p[k] is not None for k in ['build','support','tools']) else None
    page('Costs',f'''<div class="pricing"><div><small>ONE-OFF BUILD</small><strong>{money(p['build'])}</strong><p>Design, build, agreed integrations, testing, training and handover.</p><div class="recurring"><span>Support / month</span><b>{money(p['support'])}</b></div><div class="recurring"><span>Additional software / usage budget / month</span><b>{money(p['tools'])}</b></div></div><div class="payment"><small>PAYMENT STAGES</small>{terms}<div class="year"><span>First-year budget</span><b>{money(year)}</b></div></div></div><p class="footnote">AUD excluding GST. {text(p['conditions'])}</p><p class="footnote">{text(d['support_scope'])}</p>''')
    nexts=''.join(f'<li>{text(x)}</li>' for x in d['next_steps'])
    page('Next steps',f'''<p class="statement">{text(d['decision'])}</p><ol class="next-list">{nexts}</ol><div class="agreement"><span>PROPOSED START</span><p>{text(d['start'])}</p></div>''')
    css=(HERE/'proposal.css').read_text()
    jsdata=json.dumps(d['workflow'],ensure_ascii=False).replace('<','\\u003c')
    html='<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(d['client'])+' · '+esc(d['project'])+'</title><style>'+css+'</style></head><body>'
    for i,(title,body) in enumerate(pages,1):
        html+=f'<section><div class="meta">{text(d["client"])} · {text(d["supplier"])}</div><h1>{text(title)}</h1>{body}<footer><span>{mode}</span><span>{i:02} / 08</span></footer></section>'
    html+='''<script>const workflow='''+jsdata+''';document.querySelectorAll('.step').forEach(b=>b.addEventListener('click',()=>{const s=workflow[Number(b.dataset.step)];document.querySelectorAll('.step').forEach(x=>{const active=x===b;x.classList.toggle('active',active);x.setAttribute('aria-pressed',String(active));});document.getElementById('screen-owner').textContent=s.owner;document.getElementById('screen-title').textContent=s.title;document.getElementById('screen-detail').textContent=s.detail;}));</script></body></html>'''
    return html,errors

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--input',type=Path);parser.add_argument('--output',type=Path);parser.add_argument('--issue-ready',action='store_true');a=parser.parse_args()
    if a.input:
        d=json.loads(a.input.read_text());html,errors=render(d)
        if a.issue_ready and (errors or d.get('example')):raise SystemExit('NOT ISSUE-READY: '+('; '.join(errors) if errors else 'Fictional teaching example, not a real client quote.'))
        a.output.write_text(html);print('Built',a.output,'; review gaps:',len(errors));return
    OUT.mkdir(exist_ok=True)
    example=json.loads((HERE/'worked-example.json').read_text())
    act=deepcopy(example)
    act.update(example=False,client='ACT Certification',project='ACT CRM proposal',date='31 October 2026')
    act['cost']={"confirmed":False,"volume":None,"current_minutes":None,"target_minutes":None,"hourly_cost":None,"source":"ACT retained discovery notes describe the work but do not quantify the cost."}
    act['commercial']={"approved":False,"build":None,"support":None,"tools":None,"payments":[{"label":"[Agreed initial payment]","share":None},{"label":"[Agreed delivery milestone]","share":None},{"label":"[Agreed acceptance payment]","share":None}],"conditions":"Final fees, payment stages and support terms to be approved before issue."}
    act['timeline']['confirmed']=False
    for row in act['timeline']['rows']:row['when']='[DATE TO AGREE]'
    act['timeline']['condition']='Confirm dates after technical scoping, ACT access and the exact migration inventory.'
    act['support_scope']='[Confirm support fee, hours, response times and defect cover before issue.]'
    act['start']=None
    (HERE/'act-review.json').write_text(json.dumps(act,indent=2,ensure_ascii=False)+'\n')
    def blank(value,key=''):
        if isinstance(value,dict):return {k:blank(v,k) for k,v in value.items()}
        if isinstance(value,list):return [blank(v,key) for v in value]
        if isinstance(value,bool):return False
        if isinstance(value,(int,float)):return None
        return '['+key.replace('_',' ').upper()+']'
    master=blank(example);master['client']='[CLIENT]';master['project']='[PROJECT] proposal';master['supplier']='[YOUR BUSINESS]'
    (HERE/'blank-template.json').write_text(json.dumps(master,indent=2,ensure_ascii=False)+'\n')
    for name in ['worked-example','act-review','blank-template']:
        d=json.loads((HERE/f'{name}.json').read_text());html,errors=render(d);(OUT/f'{name}.html').write_text(html)
        shutil.copy2(HERE/f'{name}.json',OUT/f'{name}.json')
        print(name,':',len(errors),'unresolved readiness checks')
    for name in ['PROPOSAL-TEMPLATE.md','CALL-ONE-INPUTS.md','PRESENTER-NOTES.md','proposal.css','build.py']:
        shutil.copy2(HERE/name,OUT/name)
    shutil.copy2(OUT/'worked-example.html',OUT/'index.html')
    target=ACT/'template';shutil.copytree(OUT,target,dirs_exist_ok=True)
    shutil.copy2(OUT/'act-review.html',ACT/'ACT-CRM-Proposal.html')
    shutil.copy2(OUT/'act-review.html',ACT/'ACT-CRM-Proposal-Visual.html')
    print('Template pack and ACT review rendered; no drafting fields in client HTML.')

if __name__=='__main__':main()
