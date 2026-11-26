#!/usr/bin/env python3
"""Build the onboarding hub.

1. Builds every skill pack zip from skills/ using hub/content/packs.json.
2. Turns hub/content/*.md into hub/dist/data/site.json and copies hub/src into hub/dist.
3. On Netlify production builds (or with --upload), uploads changed packs to Supabase
   Storage, records them in pack_versions, and posts an update notice to Discord.

Run locally:  python3 scripts/build_hub.py            (build only)
              python3 scripts/build_hub.py --sync-downloads   (also refresh course/downloads/jarvis-2)
"""
from pathlib import Path
import hashlib, html, json, os, re, shutil, sys, urllib.request, urllib.error, zipfile

ROOT = Path(__file__).resolve().parents[1]
HUB = ROOT / 'hub'
CONTENT = HUB / 'content'
DIST = HUB / 'dist'
PACKS_OUT = HUB / 'build' / 'packs'
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
SKIP = {'.DS_Store', '__pycache__'}


def fail(msg):
    print('BUILD FAILED:', msg)
    sys.exit(1)


# ---------- packs ----------

def skill_version(name):
    f = ROOT / 'skills' / name / 'SKILL.md'
    if not f.exists():
        fail(f'skill {name} has no SKILL.md')
    m = re.search(r'^Version:\s*(\S+)', f.read_text(), re.M)
    if not m:
        fail(f'skill {name} has no Version line')
    return m.group(1)


def add_file(z, src, arc):
    info = zipfile.ZipInfo(arc, FIXED_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    z.writestr(info, src.read_bytes())


def build_pack(p):
    PACKS_OUT.mkdir(parents=True, exist_ok=True)
    if p.get('prebuilt'):
        src = ROOT / p['prebuilt']
        if not src.exists():
            fail(f'prebuilt file missing for {p["id"]}: {src}')
        out = PACKS_OUT / src.name
        shutil.copy2(src, out)
        version, skills = p['version'], []
    else:
        out = PACKS_OUT / p['file']
        skills = [{'name': s, 'version': skill_version(s)} for s in p['skills']]
        version = max(s['version'] for s in skills)
        with zipfile.ZipFile(out, 'w') as z:
            for inc in p.get('include', []):
                add_file(z, ROOT / inc['from'], inc['as'])
            for s in p['skills']:
                base = ROOT / 'skills' / s
                for f in sorted(base.rglob('*')):
                    if f.is_file() and not (SKIP & set(f.parts)):
                        add_file(z, f, 'skills/' + f.relative_to(ROOT / 'skills').as_posix())
    data = out.read_bytes()
    return {
        'id': p['id'], 'module': p['module'], 'title': p['title'], 'file': out.name,
        'version': version, 'hash': hashlib.sha256(data).hexdigest(), 'size': len(data),
        'skills': skills, 'note': p.get('note', ''),
    }


# ---------- content ----------

def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
    t = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    return t


def front_matter(text, path):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        fail(f'{path} has no front matter')
    meta = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            meta[k.strip()] = v.strip()
    return meta, text[m.end():]


def parse_blocks(body):
    """Paragraphs, numbered lists, prompt fences, see/fix notes and [[tokens]]."""
    blocks, lines, i = [], body.split('\n'), 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith('```prompt'):
            label = line[len('```prompt'):].strip() or 'Send to Jarvis'
            buf, i = [], i + 1
            while i < len(lines) and not lines[i].startswith('```'):
                buf.append(lines[i])
                i += 1
            blocks.append({'type': 'prompt', 'label': label, 'text': '\n'.join(buf).strip()})
            i += 1
            continue
        m = re.match(r'^\[\[(pack|link):([\w-]+)\]\]$', line.strip())
        if m:
            blocks.append({'type': m.group(1), 'id': m.group(2)})
            i += 1
            continue
        m = re.match(r'^\[\[ext:([^|\]]+)\|(https?://[^\]]+)\]\]$', line.strip())
        if m:
            blocks.append({'type': 'ext', 'label': m.group(1), 'url': m.group(2)})
            i += 1
            continue
        m = re.match(r'^\[\[image:([\w./-]+)(?:\|([^\]]*))?\]\]$', line.strip())
        if m:
            if not (HUB / 'src' / 'media' / m.group(1)).exists():
                fail(f'image hub/src/media/{m.group(1)} not found')
            blocks.append({'type': 'image', 'src': 'media/' + m.group(1), 'caption': m.group(2) or '', 'phone': 'phone' in m.group(1)})
            i += 1
            continue
        m = re.match(r'^\[\[video:(https://[^\]|]+)(?:\|([^\]]*))?\]\]$', line.strip())
        if m:
            blocks.append({'type': 'video', 'url': m.group(1), 'caption': m.group(2) or ''})
            i += 1
            continue
        if line.strip() == '[[updatelink]]':
            blocks.append({'type': 'updatelink'})
            i += 1
            continue
        m = re.match(r'^>\s*(see|fix):\s*(.+)$', line)
        if m:
            blocks.append({'type': m.group(1), 'html': inline(m.group(2))})
            i += 1
            continue
        if re.match(r'^\d+\.\s', line):
            items = []
            while i < len(lines) and (re.match(r'^\d+\.\s', lines[i]) or not lines[i].strip()):
                if lines[i].strip():
                    items.append(inline(re.sub(r'^\d+\.\s', '', lines[i])))
                i += 1
                if i < len(lines) and lines[i].strip() and not re.match(r'^\d+\.\s', lines[i]):
                    break
            blocks.append({'type': 'list', 'items': items})
            continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r'^(```|>|\[\[|\d+\.\s)', lines[i]):
            buf.append(lines[i].strip())
            i += 1
        blocks.append({'type': 'p', 'html': inline(' '.join(buf))})
    return blocks


def slug(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')[:60]


def parse_page(path, pack_ids):
    meta, body = front_matter(path.read_text(), path)
    parts = re.split(r'^## ', body, flags=re.M)
    intro = parse_blocks(parts[0])
    steps, seen = [], set()
    for part in parts[1:]:
        head, _, rest = part.partition('\n')
        m = re.match(r'^(.*?)\s*(?:\{([^}]*)\})?\s*(optional)?\s*$', head.strip())
        title, time, optional = m.group(1), m.group(2) or '', bool(m.group(3))
        sid = slug(title)
        if sid in seen:
            fail(f'{path.name}: two steps called "{title}"')
        seen.add(sid)
        blocks = parse_blocks(rest)
        for b in blocks:
            if b['type'] == 'pack' and b['id'] not in pack_ids:
                fail(f'{path.name}: unknown pack {b["id"]}')
        steps.append({'id': sid, 'title': title, 'time': time, 'optional': optional, 'blocks': blocks})
    meta['packs'] = [p.strip() for p in meta.get('packs', '').split(',') if p.strip()]
    for p in meta['packs']:
        if p not in pack_ids:
            fail(f'{path.name}: front matter names unknown pack {p}')
    meta['module'] = int(meta.get('module', 0))
    return {**meta, 'intro': intro, 'steps': steps}


def parse_site():
    meta, body = front_matter((CONTENT / 'site.md').read_text(), 'site.md')
    sections = []
    for part in re.split(r'^## ', body, flags=re.M)[1:]:
        head, _, rest = part.partition('\n')
        sections.append({'title': head.strip(), 'blocks': parse_blocks(rest)})
    return {**meta, 'sections': sections}


# ---------- Supabase and Discord ----------

def api(method, url, key, body=None, headers=None, raw=None):
    h = {'apikey': key, 'Authorization': f'Bearer {key}'}
    h.update(headers or {})
    data = raw if raw is not None else (json.dumps(body).encode() if body is not None else None)
    if body is not None:
        h.setdefault('Content-Type', 'application/json')
    req = urllib.request.Request(url, data=data, method=method, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            txt = r.read().decode() or 'null'
            return json.loads(txt)
    except urllib.error.HTTPError as e:
        fail(f'{method} {url.split("?")[0]} returned {e.code}: {e.read().decode()[:300]}')


def upload(packs):
    url, key = os.environ.get('SUPABASE_URL', '').rstrip('/'), os.environ.get('SUPABASE_SERVICE_ROLE_KEY', '')
    if not url or not key:
        print('Upload skipped: SUPABASE_URL or SUPABASE_SERVICE_ROLE_KEY not set.')
        return
    current = {r['id']: r for r in api('GET', f'{url}/rest/v1/pack_versions?select=*', key)}
    changed = []
    for p in packs:
        old = current.get(p['id'])
        if old and old['hash'] == p['hash']:
            continue
        path = f'{p["id"]}/{p["version"]}-{p["hash"][:8]}.zip'
        api('POST', f'{url}/storage/v1/object/packs/{path}', key,
            raw=(PACKS_OUT / p['file']).read_bytes(),
            headers={'Content-Type': 'application/zip', 'x-upsert': 'true'})
        api('POST', f'{url}/rest/v1/pack_versions?on_conflict=id', key,
            body=[{'id': p['id'], 'title': p['title'], 'version': p['version'], 'hash': p['hash'],
                   'path': path, 'file': p['file'], 'note': p['note'], 'module': p['module']}],
            headers={'Prefer': 'resolution=merge-duplicates'})
        print(f'Uploaded {p["id"]} {p["version"]}')
        if old:
            changed.append(p)
    hook = os.environ.get('DISCORD_WEBHOOK_URL')
    if changed and hook:
        site = os.environ.get('URL', '')
        lines = ['**Jarvis 2.0 update**']
        for p in changed:
            lines.append(f'{p["title"]}: version {p["version"]}. {p["note"]}')
        lines.append(f'Update in Jarvis: send "Update my Jarvis 2.0 skills", or download the new file from the hub. {site}'.strip())
        req = urllib.request.Request(hook, data=json.dumps({'content': '\n'.join(lines)}).encode(),
                                     headers={'Content-Type': 'application/json', 'User-Agent': 'jarvis-hub'})
        try:
            urllib.request.urlopen(req, timeout=30)
            print('Discord notice sent.')
        except urllib.error.URLError as e:
            print('Discord notice failed (build continues):', e)


# ---------- main ----------

def main():
    if os.environ.get('NETLIFY') and not (os.environ.get('SUPABASE_URL') and os.environ.get('SUPABASE_ANON_KEY')):
        fail('Set SUPABASE_URL and SUPABASE_ANON_KEY in Netlify before deploying. Without them the hub would run in open preview mode.')
    manifest = json.loads((CONTENT / 'packs.json').read_text())
    # Output folders are overwritten, never cleared, so the build needs no delete rights.
    # Netlify always builds from a clean checkout, so stale local files never ship.
    packs = [build_pack(p) for p in manifest['packs']]
    ids = {p['id'] for p in packs}
    pages = [parse_page(f, ids) for f in sorted((CONTENT / 'modules').glob('*.md'))]

    shutil.copytree(HUB / 'src', DIST, dirs_exist_ok=True)
    (DIST / 'data').mkdir(exist_ok=True)
    site = {'site': parse_site(), 'packs': packs, 'pages': pages,
            'built': os.environ.get('COMMIT_REF', 'local')[:8]}
    site_json = json.dumps(site, ensure_ascii=False, indent=1)
    # Members only: the content is bundled into the /api/site function, never published as a public file.
    (HUB / 'build').mkdir(exist_ok=True)
    (HUB / 'build' / 'site-data.mjs').write_text('export default ' + site_json + ';\n')
    public_copy = DIST / 'data' / 'site.json'
    if '--demo' in sys.argv or '--preview' in sys.argv or not os.environ.get('SUPABASE_URL'):
        public_copy.write_text(site_json)  # local preview only
    elif public_copy.exists():
        public_copy.write_text('{}')
    cfg = {'supabaseUrl': os.environ.get('SUPABASE_URL', ''), 'supabaseAnonKey': os.environ.get('SUPABASE_ANON_KEY', ''),
           'siteName': site['site'].get('name', '')}
    (DIST / 'config.js').write_text('window.HUB_CONFIG = ' + json.dumps(cfg) + ';\n')

    for p in packs:
        print(f'{p["id"]:11} {p["version"]:14} {p["size"]//1024:6} KB  {p["file"]}')
    print(f'{len(pages)} pages, {sum(len(x["steps"]) for x in pages)} steps')

    if '--demo' in sys.argv:
        # Local preview only: packs become public files. Never use on Netlify.
        if os.environ.get('NETLIFY'):
            fail('--demo must not run on Netlify')
        shutil.copytree(PACKS_OUT, DIST / 'demo-packs', dirs_exist_ok=True)
        print('Demo packs copied (local preview only)')

    if '--preview' in sys.argv:
        # One file you can open or share for review. Gitignored. No login, no downloads.
        import base64
        data = (DIST / 'data/site.json').read_text()
        for img in (DIST / 'media').glob('*'):
            uri = 'data:image/png;base64,' + base64.b64encode(img.read_bytes()).decode()
            data = data.replace(f'"media/{img.name}"', f'"{uri}"')
        h = (DIST / 'index.html').read_text()
        h = h.replace('<link rel="stylesheet" href="style.css">', '<style>' + (DIST / 'style.css').read_text() + '</style>')
        h = h.replace('<script src="config.js"></script>', '<script>window.HUB_CONFIG={};window.__SITE=' + data.replace('</', '<\\/') + ';</script>')
        h = re.sub(r'<script src="https://cdn[^>]+></script>\n?', '', h)
        h = h.replace('<script src="app.js" defer></script>\n', '')
        h = h.replace('</body>', '<script>' + (DIST / 'app.js').read_text().replace('</script', '<\\/script') + '</script>\n</body>')
        (HUB / 'preview.html').write_text(h)
        print('Preview: hub/preview.html')

    if '--sync-downloads' in sys.argv:
        dl = ROOT / 'course/downloads/jarvis-2'
        for p in packs:
            if p['skills']:
                shutil.copy2(PACKS_OUT / p['file'], dl / p['file'])
        print('Synced course/downloads/jarvis-2')

    if os.environ.get('CONTEXT') == 'production' or '--upload' in sys.argv:
        upload(packs)


if __name__ == '__main__':
    main()
