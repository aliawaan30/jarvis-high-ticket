#!/usr/bin/env python3
"""Explicit project learning log and artifact checkpoint. No background monitoring."""
import argparse,datetime,hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];CTX=ROOT/'context';LOG=CTX/'events.jsonl'
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
def append(item):
 with LOG.open('a') as f:f.write(json.dumps({'at':now(),**item})+'\n')
p=argparse.ArgumentParser();s=p.add_subparsers(dest='cmd',required=True)
s.add_parser('brief');r=s.add_parser('record');r.add_argument('--kind',choices=['decision','learning','inspection','test','blocker'],required=True);r.add_argument('--summary',required=True);r.add_argument('--evidence',required=True);r.add_argument('--consequence',required=True);s.add_parser('checkpoint');a=p.parse_args()
if a.cmd=='record':append({'kind':a.kind,'summary':a.summary,'evidence':a.evidence,'consequence':a.consequence});print('Recorded.')
elif a.cmd=='brief':
 print((CTX/'state.json').read_text());print('\nRECENT EVENTS')
 if LOG.exists():
  for l in LOG.read_text().splitlines()[-8:]:
   e=json.loads(l);print(e['at'],e['kind'],e.get('summary',''))
 print('\nSOURCE OF TRUTH:',ROOT)
else:
 files={str(f.relative_to(ROOT)):hashlib.sha256(f.read_bytes()).hexdigest() for f in ROOT.rglob('*') if f.is_file() and not any(x in f.relative_to(ROOT).parts for x in ['archive','.git']) and f!=LOG and f.name!='artifact-hashes.json'}
 old=json.loads((CTX/'artifact-hashes.json').read_text()) if (CTX/'artifact-hashes.json').exists() else {}
 changed=[k for k,v in files.items() if old.get(k)!=v];removed=[k for k in old if k not in files]
 (CTX/'artifact-hashes.json').write_text(json.dumps(files,indent=2));append({'kind':'checkpoint','summary':f'{len(changed)} changed artifacts; {len(removed)} removed','changed':changed,'removed':removed});print('Checkpoint saved:',len(changed),'changes.')
