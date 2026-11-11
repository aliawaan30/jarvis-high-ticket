#!/usr/bin/env python3
"""Build a self-contained implementation handoff from the current course/skills."""
from pathlib import Path
import hashlib,importlib.util,json,re,subprocess,sys,tempfile,zipfile,shutil
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'handoffs/offer-module-jarvis2/Jarvis-Offer-Module-Handoff.zip'
def main():
 subprocess.run([sys.executable,str(ROOT/'scripts/build_reading_copy.py')],check=True)
 with tempfile.TemporaryDirectory() as tmp:
  stage=Path(tmp)/'Jarvis-Offer-Module-Handoff';stage.mkdir()
  impl=stage/'implementation';impl.mkdir()
  for name in ['START-HERE.md','ACCEPTANCE-CHECKS.md','student-record.example.json']:
   shutil.copy2(ROOT/'handoffs/offer-module-jarvis2'/name,impl/name)
  (stage/'START-HERE.md').write_text('Start with implementation/START-HERE.md. It explains the complete package, the student journey and what to connect in Jarvis 2.0.\n')
  shutil.copytree(ROOT/'skills',stage/'skills',ignore=shutil.ignore_patterns('__pycache__','.DS_Store'))
  reading=stage/'course/reading-copy';reading.mkdir(parents=True)
  shutil.copy2(ROOT/'course/reading-copy/index.html',reading/'index.html')
  shutil.copytree(ROOT/'course/reading-copy/downloads',reading/'downloads')
  shutil.copytree(ROOT/'skills/jarvis-course-guide/references/images',reading/'data/img')
  if (ROOT/'course/reading-copy/data/demos').exists():shutil.copytree(ROOT/'course/reading-copy/data/demos',reading/'data/demos')
  (stage/'course/reading-copy/README.txt').write_text('Serve this folder with python3 -m http.server 8877, then open http://localhost:8877/#m2-the-irresistible-offer . It contains the full current reading copy; some lessons outside Module 2 are unfinished. The current student pack is in downloads/.\n')
  source=ROOT/'course/studio/data';outline=json.loads((source/'outline.json').read_text());m=next(m for m in outline['modules'] if m['slug']=='m2');module=stage/'course/module-2';(module/'lessons').mkdir(parents=True)
  (module/'outline.json').write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
  spec=importlib.util.spec_from_file_location('course_export',ROOT/'course/studio/server.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
  markdown=['# Module 2: The Irresistible Offer','','Current full teaching text. Students study the course; Jarvis helps them understand and execute.','']
  for l in m['lessons']:
   p=source/'lessons'/(l['id']+'.json');d=json.loads(p.read_text());shutil.copy2(p,module/'lessons'/p.name)
   body=re.sub(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',r'[\2](\1)',d['body'])
   markdown.extend(['## '+d['title'],'',d.get('lede',''),'',mod.html_to_md(body).replace('/data/img/','images/'),''])
  (module/'MODULE-2.md').write_text('\n'.join(markdown)+'\n')
  shutil.copytree(ROOT/'skills/jarvis-course-guide/references/images',module/'images')
  ci=json.loads((ROOT/'skills/jarvis-course-guide/references/course-index.json').read_text());manifest={'course_snapshot_sha256':ci['snapshot_sha256'],'module_lesson_ids':[l['id'] for l in m['lessons']],'runtime_tested':False,'files':{}}
  for p in sorted(stage.rglob('*')):
   if p.is_file():manifest['files'][p.relative_to(stage).as_posix()]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
  (stage/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
  with zipfile.ZipFile(OUT,'w',zipfile.ZIP_DEFLATED) as z:
   for p in sorted(stage.rglob('*')):
    if p.is_file():z.write(p,p.relative_to(stage.parent))
 with zipfile.ZipFile(OUT) as z:
  prefix='Jarvis-Offer-Module-Handoff/';manifest=json.loads(z.read(prefix+'MANIFEST.json'))
  for name,meta in manifest['files'].items():assert hashlib.sha256(z.read(prefix+name)).hexdigest()==meta['sha256'],name
  assert len(manifest['module_lesson_ids'])==5
 print(f'Verified handoff: {len(manifest["files"])} files; 5 module lessons; {OUT.stat().st_size} bytes; {OUT}')
if __name__=='__main__':main()
