from pathlib import Path
import json, html, sys
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('CRMText','/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('CRMText-Bold','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))

ROOT=Path(__file__).resolve().parent
d=json.loads((ROOT/(sys.argv[1] if len(sys.argv)>1 else 'proposal.json')).read_text())
OUT=ROOT/('act-output' if len(sys.argv)>1 else 'output'); OUT.mkdir(exist_ok=True)
pdf=OUT/'AI-CRM-Proposal.pdf'
c=canvas.Canvas(str(pdf),pagesize=(960,680))
c.setTitle('Custom AI CRM proposal'); c.setAuthor('Proposal draft')
ink=HexColor('#182432'); muted=HexColor('#596674'); line=HexColor('#dfe4e8')
body=ParagraphStyle('body',fontName='CRMText',fontSize=15,leading=22,textColor=ink)
cell=ParagraphStyle('cell',parent=body,fontSize=13,leading=18)
bold=ParagraphStyle('bold',parent=cell,fontName='CRMText-Bold')
note=ParagraphStyle('note',parent=body,fontSize=11,leading=16,textColor=muted)
esc=html.escape
sections=[]; markdown=['# Custom AI CRM proposal','',d['date'],'']
for i,p in enumerate(d['pages'],1):
 c.setFillColor(muted); c.setFont('CRMText',10); c.drawString(64,641,f"{d['client']}  /  {d['date']}")
 c.setStrokeColor(line); c.line(64,624,896,624)
 c.setFillColor(ink); c.setFont('CRMText-Bold',31); c.drawString(64,574,p['title'])
 y=545
 def para(text,style=body,after=13):
  global y
  q=Paragraph(esc(text),style); _,h=q.wrap(832,600); q.drawOn(c,64,y-h); y-=h+after
 para(p['intro'],body,18)
 if i==1:
  for text in p.get('paragraphs',[]):para(text)
 rows=[]
 for j,row in enumerate(p['rows']):
  rows.append([Paragraph(esc(row[0]),bold),Paragraph(esc(row[1]),cell)])
 t=Table(rows,colWidths=[250,582],hAlign='LEFT')
 t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),14),('TOPPADDING',(0,0),(-1,-1),11),('BOTTOMPADDING',(0,0),(-1,-1),11),('LINEBELOW',(0,0),(-1,-1),.5,line),('BACKGROUND',(0,0),(-1,-1),HexColor('#f7f9fa'))]))
 _,h=t.wrap(832,600); t.drawOn(c,64,y-h); y-=h+18
 if i!=1:
  for text in p.get('paragraphs',[]):para(text)
 if p.get('note'):para(p['note'],note,0)
 if y<63:raise RuntimeError(f'Page {i} content too low: {y}')
 c.setFillColor(muted);c.setFont('CRMText',9);c.drawString(64,30,'CUSTOM AI CRM  |  WORKING DRAFT');c.drawRightString(896,30,f'{i:02d} / {len(d["pages"]):02d}');c.showPage()
 paragraphs=''.join(f'<p>{esc(x)}</p>' for x in p.get('paragraphs',[]))
 table='<table>'+''.join('<tr><th>'+esc(a)+'</th><td>'+esc(b)+'</td></tr>' for a,b in p['rows'])+'</table>'
 content=paragraphs+table if i==1 else table+paragraphs
 sections.append(f'<section><div class="meta">{esc(d["client"])} · {esc(d["date"])}</div><h1>{esc(p["title"])}</h1><p class="intro">{esc(p["intro"])}</p>{content}<p class="note">{esc(p.get("note",""))}</p><div class="page">{i:02d} / {len(d["pages"]):02d}</div></section>')
 markdown+=['## '+p['title'],'',p['intro'],'']+p.get('paragraphs',[])+['']+[f'**{a}**: {b}\n' for a,b in p['rows']]+['',p.get('note',''),'']
c.save()
css='''*{box-sizing:border-box}body{margin:0;background:#eef0f2;color:#182432;font:18px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}section{max-width:1080px;margin:28px auto;background:white;padding:54px 65px 30px;min-height:650px}h1{font-size:36px;line-height:1.2;letter-spacing:-.7px;margin:32px 0 20px}.meta,.page{font-size:12px;color:#596674}.meta{border-bottom:1px solid #dfe4e8;padding-bottom:18px}.intro{color:#455361;margin-bottom:24px}table{border-collapse:collapse;width:100%;font-size:16px;background:#f7f9fa}th,td{padding:14px;text-align:left;vertical-align:top;border-bottom:1px solid #dfe4e8}th{width:31%;font-weight:600}p{margin:15px 0}.note{font-size:13px;color:#596674}.page{margin-top:25px;text-align:right}@media(max-width:650px){section{margin:0 0 14px;padding:25px 20px;min-height:0}h1{font-size:29px}body{font-size:17px}table{font-size:14px}th,td{padding:10px}}@media print{body{background:white}section{break-after:page;margin:0;min-height:0}}'''
(OUT/'AI-CRM-Proposal.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Custom AI CRM proposal</title><style>'+css+'</style></head><body>'+''.join(sections)+'</body></html>')
(OUT/'AI-CRM-Proposal-Editable.md').write_text('\n'.join(markdown))
print(pdf)
