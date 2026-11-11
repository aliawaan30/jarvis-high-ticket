import subprocess,os,json,select,time
from pathlib import Path
root=Path('/Users/blakestephens/co-founder/jarvis/.claude/worktrees/jarvis-os')
dest=Path(__file__).resolve().parent/'ACT-agent-reply.json'
env=os.environ.copy();env.update(JARVIS_AGENT='offer',JARVIS_CHAIN='offer',JARVIS_HUB_DIR='/Users/blakestephens/co-founder/jarvis/brain/hub',JARVIS_ROOT='/Users/blakestephens/co-founder/jarvis',JARVIS_CODE_ROOT=str(root))
p=subprocess.Popen(['/usr/local/bin/node',str(root/'node_modules/tsx/dist/cli.mjs'),str(root/'scripts/hub/mcp.ts')],cwd=root,env=env,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,text=True,bufsize=1)
question='Blake explicitly asks for ACT CRM information to populate a plain ten-page sales proposal. The screenshot identifies Codex session 01a10f75-1dd6-7d72-a026-aebca4853748, which is not registered in hub messaging. I read its saved conversation and its brief at projects/high-ticket-program/tests/custom-ai-crm-proposal/proposal-brief.md. Please cross-check ACT client name, original discovery call path, actual workflow/pains, included CRM features, integrations, what is built versus still unaccepted, approved fee/support/timing if evidenced. Return exact evidence paths and discrepancies. Do not invent commercial terms or change code/live systems. If you can reach that exact session through supported messaging, ask it to confirm the brief; otherwise state you are a separate ACT agent. Draft research only, no client contact.'
for req in [{'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':'2024-11-05','capabilities':{},'clientInfo':{'name':'offer ACT brief request','version':'1'}}},{'jsonrpc':'2.0','method':'notifications/initialized'},{'jsonrpc':'2.0','id':2,'method':'tools/call','params':{'name':'ask_agent','arguments':{'agent':'act','question':question}}}]:p.stdin.write(json.dumps(req)+'\n')
p.stdin.flush();print('ACT agent cross-check requested.',flush=True)
deadline=time.time()+300
while time.time()<deadline:
 if not select.select([p.stdout],[],[],1)[0]:continue
 line=p.stdout.readline()
 if not line:break
 try:r=json.loads(line)
 except:continue
 if r.get('id')==2:
  dest.write_text(json.dumps(r,indent=2));print(json.dumps(r),flush=True);break
else:print('ACT response pending; no reply claimed.',flush=True)
p.terminate()
