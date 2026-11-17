import urllib.request,json,time,base64,sys
from pathlib import Path
r=Path(__file__).resolve().parents[1];sid=sys.argv[1];base='http://localhost:4445/session/'+sid

def call(route,data=None):
 req=urllib.request.Request(base+route,data=json.dumps(data).encode() if data is not None else None,headers={'Content-Type':'application/json'})
 with urllib.request.urlopen(req,timeout=30) as f:return json.load(f)['value']
def js(code):return call('/execute/sync',{'script':code,'args':[]})
def wait(test):
 for _ in range(90):
  if js('return '+test):return
  time.sleep(.2)
 raise RuntimeError('Timeout: '+test)
call('/url',{'url':'http://localhost:8766'});wait('window.__scene?.getState().ready');js("document.querySelector('#rotate').click();document.querySelector('#trace').click();return true");wait('window.__scene.getState().traceProgress===1');trace=js('return window.__scene.getState()');js("document.querySelector('#rebuild').click();return true");wait('window.__scene.getState().buildProgress===1');full=js('return window.__scene.getState()');(r/'qa/safari-full.png').write_bytes(base64.b64decode(call('/screenshot')));js("document.querySelector('#compare').click();return true");compare=js('return window.__scene.getState()');js("document.querySelector('#scan').click();return true");reset=js('return window.__scene.getState()');result={'browser':js('return navigator.userAgent'),'trace':trace,'full':full,'compare':compare,'reset':reset};assert trace['linesVisible'] and full['fullVisible'] and not full['scanVisible'] and compare['scanVisible'] and reset['phase']=='scan';(r/'qa/safari.json').write_text(json.dumps(result,indent=2));print('Safari: trace, reconstruction, comparison and reset PASS')
