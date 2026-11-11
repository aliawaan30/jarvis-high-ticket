from pathlib import Path
from playwright.sync_api import sync_playwright
import json
r=Path('/Users/blakestephens/Downloads/Jarvis-Five-Proposals');q=r/'qa';q.mkdir(exist_ok=True)
data=json.loads((r/'source/offers.json').read_text());checks=[]
with sync_playwright() as p:
 b=p.chromium.launch(channel='chrome',headless=True)
 for d in data:
  page=b.new_page(viewport={'width':1440,'height':1080});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto((r/d['id']/'index.html').as_uri());page.locator('#demo').scroll_into_view_if_needed()
  page.wait_for_timeout(7500);assert page.locator('#counter').inner_text()=='02 / 05','autoplay'
  page.locator('#play').click();state=page.locator('#counter').inner_text();page.wait_for_timeout(7500);assert state==page.locator('#counter').inner_text(),'pause'
  page.locator('.step').nth(2).click();assert 'scene2' in page.locator('.cinema').get_attribute('class')
  page.screenshot(path=str(q/f"{d['id']}-demo.png"))
  page.locator('.step').nth(4).click();assert page.locator('#lastValue').inner_text()==d['finalValue']
  page.locator('#replay').click();assert page.locator('#counter').inner_text()=='01 / 05'
  page.locator('.exception summary').click();page.wait_for_timeout(100);assert page.locator('#play').inner_text()=='▶ Play'
  page.locator('#value').scroll_into_view_if_needed();expected=round(d['volume']*(d['before']-d['after'])/60*d['rate']);assert page.locator('#money').inner_text()==f'${expected:,}'
  for selector in ['#volume','#saved']:
   page.locator(selector).fill('0');page.locator(selector).dispatch_event('input');assert page.locator('#money').inner_text()=='$0'
  page.screenshot(path=str(q/f"{d['id']}-value.png"))
  page.locator('#scopeButton').click();assert page.locator('#scopeModal').is_visible();page.keyboard.press('Escape');assert not page.locator('#scopeModal').is_visible()
  page.locator('#scope').scroll_into_view_if_needed();page.screenshot(path=str(q/f"{d['id']}-scope.png"))
  page.locator('#launch').scroll_into_view_if_needed();page.screenshot(path=str(q/f"{d['id']}-launch.png"))
  page.locator('#next').scroll_into_view_if_needed();page.screenshot(path=str(q/f"{d['id']}-next.png"))
  page.set_viewport_size({'width':390,'height':844});page.evaluate('scrollTo(0,0)');page.screenshot(path=str(q/f"{d['id']}-mobile.png"),full_page=True)
  assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),'mobile overflow'
  assert not errors,errors
  checks.append({'proposal':d['id'],'passed':['autoplay advances','pause holds','manual exception and final steps','replay resets','exception pauses','calculator base and zero','modal open and Escape close','390px no horizontal overflow','no JS errors']});page.close()
 page=b.new_page(viewport={'width':1440,'height':1080});page.goto((r/'index.html').as_uri());page.screenshot(path=str(q/'gallery.png'),full_page=True)
 for a in page.locator('a').all():
  href=a.get_attribute('href');assert (r/href).exists(),href
 page.goto((r/'research.html').as_uri());page.screenshot(path=str(q/'research.png'),full_page=True)
 page=b.new_page(reduced_motion='reduce');page.goto((r/'fieldquote/index.html').as_uri());assert page.locator('#play').inner_text()=='▶ Play';checks.append({'check':'reduced motion defaults to paused','passed':True})
 b.close()
(q/'checks.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks))
