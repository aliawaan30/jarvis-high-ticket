#!/usr/bin/env python3
"""Package current student skills with an exact, inspectable course snapshot."""
from pathlib import Path
import hashlib,json,re,shutil,zipfile
ROOT=Path(__file__).resolve().parents[1]
def main():
 studio=ROOT/'course/studio/data'; refs=ROOT/'skills/jarvis-course-guide/references'
 (refs/'lessons').mkdir(parents=True,exist_ok=True)
 outline=json.loads((studio/'outline.json').read_text()); index={'version':'2026-11-08-course-guide','snapshot_sha256':'','modules':[]}
 digest=hashlib.sha256();ids=set();images=set()
 for module in outline['modules']:
  m={k:module[k] for k in ['slug','num','name']};m['lessons']=[]
  if 'review_status' in module:m['review_status']=module['review_status']
  for entry in module['lessons']:
   id=entry['id'];ids.add(id);source=studio/'lessons'/f'{id}.json';d=json.loads(source.read_text())
   images.update(re.findall(r'/data/img/([^\"<>]+)',d.get('body','')))
   data={k:d.get(k,'') for k in ['id','title','lede','body']};raw=(json.dumps(data,ensure_ascii=False,indent=2)+'\n').encode();digest.update(raw)
   (refs/'lessons'/f'{id}.json').write_bytes(raw)
   m['lessons'].append({'id':id,'title':d['title'],'file':f'lessons/{id}.json','has_body':bool(d.get('body','').strip()),'sha256':hashlib.sha256(raw).hexdigest()})
  index['modules'].append(m)
 for p in (refs/'lessons').glob('*.json'):
  if p.stem not in ids:p.unlink()
 (refs/'images').mkdir(exist_ok=True)
 for old in (refs/'images').iterdir():
  if old.is_file() and old.name not in images:old.unlink()
 for name in images:shutil.copy2(studio/'img'/name,refs/'images'/name)
 if (studio/'demos').exists():shutil.copytree(studio/'demos',refs/'demos',dirs_exist_ok=True)
 index['snapshot_sha256']=digest.hexdigest();(refs/'course-index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
 output=ROOT/'course/reading-copy/downloads/Jarvis-High-Ticket-Skills.zip';output.parent.mkdir(parents=True,exist_ok=True)
 skills=sorted((ROOT/'skills').glob('*/SKILL.md'))
 with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as z:
  prefix='Jarvis-High-Ticket-Skills/'
  z.writestr(prefix+'README.txt','Keep the skill folders and references together in your Jarvis project. Ask Jarvis which files it can access and what it can save. The course guide includes a course snapshot, not automatic access to future updates or connected business tools.\n')
  z.writestr(prefix+'PACK-INFO.json',json.dumps({'version':index['version'],'course_sha256':index['snapshot_sha256'],'skills':[p.parent.name for p in skills]},indent=2)+'\n')
  for p in sorted((ROOT/'skills').rglob('*')):
   if p.is_file() and not any(x in p.parts for x in ['__pycache__','.DS_Store']):z.write(p,prefix+p.relative_to(ROOT).as_posix())
 print(f'Pack: {len(skills)} skills, {len(ids)} course lessons, snapshot {index["snapshot_sha256"][:12]}')
if __name__=='__main__':main()
