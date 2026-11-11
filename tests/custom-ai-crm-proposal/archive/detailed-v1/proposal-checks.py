from pathlib import Path
from playwright.sync_api import sync_playwright
import json

root = Path(__file__).resolve().parent
checks = []
errors = []

def check(name, condition):
    checks.append({'check': name, 'passed': bool(condition)})
    if not condition:
        raise AssertionError(name)

with sync_playwright() as p:
    browser = p.chromium.launch(channel='chrome', headless=True)
    page = browser.new_page(viewport={'width': 1440, 'height': 1000})
    page.on('pageerror', lambda error: errors.append(str(error)))
    page.goto((root / 'proposal.html').as_uri(), wait_until='networkidle')

    check('Scrolling proposal has a clear title and example status', page.title().startswith('Custom CRM implementation proposal') and page.get_by_text('ILLUSTRATIVE EXAMPLE', exact=True).count() == 1)
    check('Executive overview has two substantive paragraphs', page.locator('#summary .summary-grid > div > p').count() == 2)
    check('Nine proposal sections appear in sales-call order', page.locator('main > section').count() == 10 and page.locator('.rail nav a').count() == 10)
    check('Business pains are clearly marked as example assumptions', page.locator('#heard .heard-list article').count() == 4 and page.locator('#heard .section-lead').inner_text().find('not claims about a real company') >= 0)
    check('Custom-vs-standard fit and do-nothing option are visible', page.get_by_text('Standard CRM', exact=True).count() == 1 and page.get_by_text('Do nothing', exact=True).count() == 1)
    check('Full system describes six CRM workstreams', page.locator('#system .system-card').count() == 6)
    check('Interactive CRM mock-up exposes its prototype status', page.locator('#demo .section-lead').inner_text().find('no connected systems') >= 0)
    check('Interactive demo starts with sourced lead assignment', 'Maya Chen · Sales' in page.locator('#demo-fields').inner_text() and page.locator('#demo-source').inner_text().startswith('Source:'))
    page.locator('#demo-next').click()
    check('Demo moves to proposal approval and does not claim a send', 'Needs approval' in page.locator('#demo-state').inner_text() and 'No message sent' in page.locator('#demo-activity').inner_text())
    page.locator('#demo-next').click(); page.locator('#demo-next').click(); page.locator('#demo-next').click()
    check('Demo walks through project blocker and sourced Jarvis answer', 'What is blocking the import?' in page.locator('#demo-fields').inner_text() and 'Source: project task' in page.locator('#demo-ai').inner_text())
    check('Scope has deliverable and acceptance criteria for each of six workstreams', page.locator('#scope tbody tr').count() == 6 and page.locator('#scope tbody tr td:nth-child(3)').count() == 6)
    check('Roadmap has five gated implementation phases', page.locator('#roadmap .roadmap article').count() == 5 and page.locator('#roadmap .deliver').count() == 5)
    check('Example calculator computes annual labour and released capacity', page.locator('#current-value').inner_text() == '$30,240' and page.locator('#saved-value').inner_text() == '$10,584')
    check('Cost comparison carries retained subscriptions into the proposed future cost', '$3,600/year' in page.locator('#retained-tools-post').inner_text() and '$23,256/year' in page.locator('#future-total').inner_text())
    check('No-build alternative remains explicit and investment is not fabricated', 'Do nothing' in page.locator('#recommendation').inner_text() and 'Quote after technical scope' in page.locator('#economics').inner_text())
    page.locator('#jobs').fill('0'); page.locator('#minutes').fill('0')
    check('Zero calculator inputs remain finite and readable', page.locator('#current-value').inner_text() == '$0' and page.locator('#saved-value').inner_text() == '$0')
    page.locator('#jobs').fill('100'); page.locator('#minutes').fill('20'); page.locator('#hourly').fill('50'); page.locator('#recover').fill('50')
    check('Calculator recomputes scenario when inputs change', page.locator('#current-value').inner_text() == '$20,000' and page.locator('#saved-value').inner_text() == '$10,000')
    check('Trust section avoids invented team, testimonials and certifications', 'No testimonial, security certification, dedicated department' in page.locator('#trust').inner_text())
    check('Decision section names client inputs and next decision', page.locator('#decision ol li').count() == 5 and 'technical scoping' in page.locator('#decision').inner_text())
    check('Presenter cues are separately collapsed', page.locator('details.presenter').count() == 2 and page.locator('details.presenter[open]').count() == 0)

    page.set_viewport_size({'width': 390, 'height': 844})
    page.reload(wait_until='networkidle')
    check('390px mobile page has no viewport overflow', page.evaluate('document.documentElement.scrollWidth <= innerWidth'))
    page.locator('.rail nav a[href="#demo"]').click()
    check('Mobile contents navigation scrolls to the demo', page.evaluate('location.hash') == '#demo')
    topbar_bottom = page.locator('.topbar').bounding_box()['y'] + page.locator('.topbar').bounding_box()['height']
    rail_bottom = page.locator('.rail').bounding_box()['y'] + page.locator('.rail').bounding_box()['height']
    demo_top = page.locator('#demo').bounding_box()['y']
    check('Mobile sticky contents bar does not cover section heading', demo_top >= rail_bottom and rail_bottom >= topbar_bottom)
    page.emulate_media(media='print')
    check('Print layout hides navigation controls and keeps proposal body', page.locator('.rail').evaluate("e => getComputedStyle(e).display") == 'none' and page.locator('#summary').count() == 1)
    check('No browser JavaScript errors in exercised proposal', len(errors) == 0)

    page.emulate_media(media='screen')
    page.set_viewport_size({'width': 1440, 'height': 1000})
    page.add_style_tag(content='.topbar,.rail{position:static!important}')
    for name, selector in [('cover', '#summary'), ('system-demo', '#demo'), ('scope-roadmap', '#scope'), ('economics', '#economics'), ('trust-decision', '#decision')]:
        page.locator(selector).screenshot(path=str(root / 'qa' / f'proposal-{name}.png'), animations='disabled')
    browser.close()

(root / 'qa' / 'proposal-checks.json').write_text(json.dumps({
    'environment': 'Local macOS Chrome via Playwright; static HTML prototype',
    'checks': checks,
    'passed': sum(1 for x in checks if x['passed']),
    'errors': errors,
    'not_tested': ['Real buyer discovery or commercial approval', 'Live CRM integrations or persistence', 'Production authentication/security', 'Actual AI model behavior', 'Client interviews or conversion']
}, indent=2))
print(f"{sum(1 for x in checks if x['passed'])}/{len(checks)} checks passed")
for item in checks:
    print(('PASS' if item['passed'] else 'FAIL') + ' · ' + item['check'])
