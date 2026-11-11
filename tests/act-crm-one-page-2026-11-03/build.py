from pathlib import Path
from html import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
import shutil
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('Arial', '/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold', '/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
pdfmetrics.registerFontFamily('Arial', normal='Arial', bold='Arial-Bold')
root=Path(__file__).parent
sections=[
('Executive summary', 'We propose a custom CRM for ACT Certification that connects an enquiry to its proposal, signed documents, payment and assessment. The purpose is to reduce repeated data entry and manual status checks, and give the team one clear record of each job, its documents, owner and next action.'),
('The problems and their impact', 'ACT’s walkthrough described requests arriving through Jotform, followed by staff re-entering the details into BCS. Staff then prepare proposals and forms, and check signing and payment separately before progressing the job.'),
]
problems=[
('Repeated entry and document preparation', 'The same request details are handled twice, then used to assemble proposals and forms. This takes staff away from progressing jobs and creates more opportunities for errors.'),
('Separate signing, payment and job status', 'Staff must check different systems to know what can move forward. A signed proposal or paid invoice can still need a manual handoff.'),
('Documents, ownership and workload', 'The team needs clearer approved and superseded document versions, assigned tasks and workload visibility. Without these, people spend time checking files and asking who is doing what next.')]
solution='Build separate enquiry, proposal and project views around one connected job record. Bring Jotform requests into the CRM; prepare proposals from approved templates; show DocuSign and Xero status; and assign the next task when a job is ready. Keep Microsoft’s inspection calendar, with booking confirmations and reminders. Organise plans by version and status. Staff still approve fees, proposals and all certification decisions.'
timeline=[('1. Confirm scope', 'Map the workflow, agree the first release and confirm system access.'),('2. Build and connect', 'Create the CRM, document templates and agreed integrations.'),('3. Test with the team', 'Run sample jobs through the full process and resolve issues.'),('4. Launch and train', 'Train staff, agree the cutover and provide launch support.')]
costs=[('CRM build and implementation','A$[amount to agree]'),('Ongoing support, if selected','A$[amount] / month'),('Additional software, if required','Confirmed before approval')]
styles={
 'title':ParagraphStyle('title',fontName='Arial-Bold',fontSize=21,leading=25,textColor=colors.HexColor('#162c3a'),spaceAfter=5),
 'meta':ParagraphStyle('meta',fontName='Arial',fontSize=9,leading=12,textColor=colors.HexColor('#52616b'),spaceAfter=11),
 'head':ParagraphStyle('head',fontName='Arial-Bold',fontSize=11.3,leading=14,spaceBefore=11,spaceAfter=5,textColor=colors.HexColor('#162c3a')),
 'body':ParagraphStyle('body',fontName='Arial',fontSize=10,leading=13.5,spaceAfter=5,textColor=colors.HexColor('#26333b')),
 'small':ParagraphStyle('small',fontName='Arial',fontSize=8.7,leading=11.5,textColor=colors.HexColor('#52616b'),spaceAfter=4)
}
def p(t,s='body'): return Paragraph(t,styles[s])
pdf=root/'output/pdf/ACT-CRM-Proposal-One-Page.pdf'
doc=SimpleDocTemplate(str(pdf),pagesize=A4,rightMargin=42,leftMargin=42,topMargin=33,bottomMargin=28)
story=[p('ACT Certification | CRM proposal','title'),p('Proposed build for ACT Certification · Draft for discussion','meta')]
for h,b in sections: story += [p(h,'head'),p(b)]
for h,b in problems: story += [p('<b>'+h+'.</b> '+b)]
story += [p('Cost of the current process: ACT’s job volume, handling time and staff cost still need to be measured before a dollar saving can be agreed.','small'),p('Proposed solution','head'),p(solution),p('Timeline','head')]
for h,b in timeline: story.append(p('<b>'+h+':</b> '+b))
story.append(p('Dates will be agreed after scope and integration access are confirmed.','small'))
story.append(p('Costs','head'))
t=Table([[p(a),p(b)] for a,b in costs],colWidths=[325,186],hAlign='LEFT')
t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),('LINEBELOW',(0,0),(-1,-1),.3,colors.HexColor('#d6dce0'))]))
story += [t,Spacer(1,5),p('All amounts are AUD, excluding GST. Migration scope, delivery dates and payment terms will be agreed before approval.','small')]
doc.build(story)
html='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ACT Certification | CRM proposal</title><style>
*{box-sizing:border-box}body{margin:0;background:#f4f5f6;color:#26333b;font:16px/1.6 system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.toolbar{max-width:800px;margin:26px auto 16px;padding:0 28px;display:flex;justify-content:space-between;gap:20px;align-items:center;font-size:13px;color:#52616b}.toolbar a{color:#254e69}main{max-width:800px;background:white;margin:0 auto 48px;padding:45px 55px;border:1px solid #e1e5e8}h1{font-size:30px;line-height:1.2;margin:0 0 8px;color:#162c3a;letter-spacing:-.6px}h2{font-size:19px;margin:27px 0 8px;color:#162c3a}p{margin:0 0 12px}.meta,.note{color:#52616b;font-size:13px}.meta{margin-bottom:28px}ol{padding-left:22px}li{padding-left:4px;margin-bottom:9px}table{width:100%;border-collapse:collapse;font-size:15px}td{padding:10px 0;border-bottom:1px solid #d6dce0;vertical-align:top}td:last-child{width:42%;padding-left:20px}.note{margin-top:12px}@media(max-width:600px){main{padding:28px 23px;margin:0;border-left:0;border-right:0}h1{font-size:26px}.toolbar{padding:0 23px;margin:18px auto}body{font-size:15px}}@media print{.toolbar{display:none}body{background:white}main{border:0;margin:0;padding:0;max-width:none}}
</style></head><body><nav class="toolbar"><span>Proposal review</span><a href="ACT-CRM-Proposal-One-Page.pdf">Download one-page PDF ↓</a></nav><main><h1>ACT Certification | CRM proposal</h1><p class="meta">Proposed build for ACT Certification · Draft for discussion</p>'''
for h,b in sections: html+=f'<h2>{escape(h)}</h2><p>{escape(b)}</p>'
for h,b in problems: html+=f'<p><strong>{escape(h)}.</strong> {escape(b)}</p>'
html+='<p class="note">Cost of the current process: ACT’s job volume, handling time and staff cost still need to be measured before a dollar saving can be agreed.</p>'
html+='<h2>Proposed solution</h2><p>'+escape(solution)+'</p><h2>Timeline</h2><ol>'
for h,b in timeline: html+=f'<li><strong>{escape(h[3:])}:</strong> {escape(b)}</li>'
html+='</ol><p class="note">Dates will be agreed after scope and integration access are confirmed.</p><h2>Costs</h2><table>'
for a,b in costs:html+=f'<tr><td>{escape(a)}</td><td>{escape(b)}</td></tr>'
html+='</table><p class="note">All amounts are AUD, excluding GST. Migration scope, delivery dates and payment terms will be agreed before approval.</p></main></body></html>'
(root/'site/dist/index.html').write_text(html)
shutil.copy2(pdf,root/'site/dist'/pdf.name)
print(pdf)
