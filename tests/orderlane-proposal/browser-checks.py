from pathlib import Path
from playwright.sync_api import sync_playwright
import json

root=Path(__file__).resolve().parent
checks=[]
def ok(name,condition=True):
 checks.append({'check':name,'passed':bool(condition)})
 if not condition: raise AssertionError(name)

with sync_playwright() as w:
 browser=w.chromium.launch(channel='chrome',headless=True)
 page=browser.new_page(viewport={'width':1440,'height':1000})
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto((root/'index.html').as_uri(),wait_until='networkidle')
 ok('Eight-step proposal walkthrough exists',page.locator('main .slide').count()==8)
 ok('Initial state presents recommendation only',page.locator('#slide-recommendation').is_visible() and not page.locator('#slide-current').is_visible())
 ok('Agenda labels use the intended buyer-call sequence',page.locator('.agenda button').all_text_contents()==['01Recommendation','02Your current process','03The proposed system','04Watch an order','05What’s included','06Build & rollout','07Value & investment','08Decision & next step'])
 for phrase in ['current process','desired end state','The proposed system','What the team receives','Launch gate','Investment quoted after feasibility','Decision requested']:
  ok('Walkthrough contains: '+phrase,page.get_by_text(phrase,exact=False).count()>0)
 page.locator('#forward').click();ok('Next advances to current pain / end state',page.locator('#slide-current').is_visible())
 page.locator('#prev').click();ok('Back returns to recommendation',page.locator('#slide-recommendation').is_visible())
 page.locator('.agenda button[data-slide="3"]').click();ok('Agenda jumps to the order demo',page.locator('#slide-demo').is_visible())
 page.locator('#next').click();page.locator('#next').click();ok('Unclear unit blocks demo pending approval',page.locator('#approve').is_visible() and page.locator('#next').is_disabled())
 page.locator('#approve').click();page.locator('#next').click();ok('Staff decision leads to prepared draft state',page.locator('#stateTitle').inner_text()=='Ready for your order system')
 page.locator('#reset').click();page.locator('#duplicate').check();ok('Duplicate PO stops progression', 'Duplicate blocked' in page.locator('#notice').inner_text() and page.locator('#next').is_disabled())
 page.locator('#reset').click();ok('Demo reset clears exception and duplicate switch',not page.locator('#duplicate').is_checked() and page.locator('#stateTitle').inner_text()=='Waiting for intake')
 page.locator('.agenda button[data-slide="6"]').click()
 ok('Capacity calculator default: 150 hours and $63,000/year',page.locator('#capacity').inner_text()=='150' and page.locator('#annual').inner_text()=='$63,000')
 page.locator('#orders').fill('1500');ok('Changed order volume recomputes value to $31,500',page.locator('#annual').inner_text()=='$31,500')
 page.locator('#orders').fill('0');page.locator('#minutes').fill('0');ok('Zero inputs stay finite and readable',page.locator('#capacity').inner_text()=='0' and page.locator('#annual').inner_text()=='$0')
 page.set_viewport_size({'width':390,'height':844});page.goto((root/'index.html').as_uri(),wait_until='networkidle')
 ok('390px mobile layout has no horizontal overflow',page.evaluate('document.documentElement.scrollWidth <= innerWidth'))
 page.locator('#forward').click();ok('Mobile Next control advances slide',page.locator('#slide-current').is_visible())
 page.locator('.agenda button[data-slide="7"]').click();ok('Mobile agenda reaches the decision slide',page.locator('#slide-decision').is_visible())
 page.set_viewport_size({'width':1440,'height':1000});page.goto((root/'index.html').as_uri(),wait_until='networkidle');page.add_style_tag(content='header{position:static!important}')
 for i in range(8):
  page.locator(f'.agenda button[data-slide="{i}"]').click()
  page.locator('.slide.active').screenshot(path=str(root/'qa'/f'slide-{i+1:02d}.png'))
 page.goto((root/'review.html').as_uri(),wait_until='networkidle')
 ok('Internal review contains 13 labelled sources and links back',page.locator('.evidence').count()==13 and page.locator('a[href="index.html"]').count()==1)
 ok('No browser JavaScript errors in exercised walkthrough',len(errors)==0)
 browser.close()
(root/'qa'/'checks.json').write_text(json.dumps({'environment':'Local macOS Chrome via Playwright; static HTML, prototype only','checks':checks,'errors':errors,'not_tested':['Actual ERP/AI execution','Base44 runtime','Buyer validation','Real baseline or commercial acceptance','Production mail/ERP access']},indent=2))
print(json.dumps(checks,indent=2))
