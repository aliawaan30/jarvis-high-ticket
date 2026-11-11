# -*- coding: utf-8 -*-
"""Authoring server for the high ticket course.

Serves the studio editor and reads/writes plain files on disk so nothing lives
only in a browser. Local only, no auth, not for the internet.

    python3 server.py            # http://127.0.0.1:4330

Layout on disk:
    data/outline.json            modules + lesson order + titles
    data/lessons/<id>.json       one lesson: fields, body html, sketch shapes
    data/sketches/<id>.png       flattened picture of the sketch, for sharing
    export/                      written when you hit Export
"""
import base64
import json
import os
import re
import shutil
import sys
import tempfile
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
LESSONS = os.path.join(DATA, "lessons")
SKETCH = os.path.join(DATA, "sketches")
EXPORT = os.path.join(HERE, "export")
OUTLINE = os.path.join(DATA, "outline.json")

ID_OK = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")


def write_atomic(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(path))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def load_json(path, fallback):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return fallback


def backup(path):
    """Keep one previous copy of the outline. Cheap insurance."""
    if os.path.exists(path):
        shutil.copy2(path, path + ".bak")


def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return s[:60] or "untitled"


# Very small HTML to text/markdown pass, enough to read an export in a terminal.
def html_to_md(html):
    h = html or ""
    h = re.sub(r"(?is)<br\s*/?>", "\n", h)
    h = re.sub(r"(?is)<div class=\"b-prompt\"[^>]*>(.*?)</div>", r"\n```\n\1\n```\n", h)
    h = re.sub(r"(?is)<div class=\"b-note\"[^>]*>(.*?)</div>", r"\n> NOTE: \1\n", h)
    h = re.sub(r"(?is)<div class=\"b-ex\"[^>]*>(.*?)</div>", r"\n> EXAMPLE: \1\n", h)
    h = re.sub(r"(?is)<div class=\"b-script\"[^>]*>(.*?)</div>", r"\n> SAY THIS: \1\n", h)
    h = re.sub(r"(?is)<figure[^>]*>\s*<img[^>]*src=\"([^\"]+)\"[^>]*>\s*(?:<figcaption[^>]*>(.*?)</figcaption>)?\s*</figure>", r"\n![\2](\1)\n", h)
    h = re.sub(r"(?is)<tr[^>]*>", "\n| ", h)
    h = re.sub(r"(?is)</t[hd]>", " | ", h)
    h = re.sub(r"(?is)<h2[^>]*>(.*?)</h2>", r"\n## \1\n", h)
    h = re.sub(r"(?is)<h3[^>]*>(.*?)</h3>", r"\n### \1\n", h)
    h = re.sub(r"(?is)<li[^>]*>(.*?)</li>", r"- \1\n", h)
    h = re.sub(r"(?is)<blockquote[^>]*>(.*?)</blockquote>", r"\n> \1\n", h)
    h = re.sub(r"(?is)<hr\s*/?>", "\n***\n", h)
    h = re.sub(r"(?is)</(p|div|ul|ol|h1)>", "\n\n", h)
    h = re.sub(r"(?is)<(b|strong)>(.*?)</\1>", r"**\2**", h)
    h = re.sub(r"(?is)<(i|em)>(.*?)</\1>", r"*\2*", h)
    h = re.sub(r"(?s)<[^>]+>", "", h)
    h = (h.replace("&nbsp;", " ").replace("&amp;", "&")
          .replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"')
          .replace("&#39;", "'"))
    h = re.sub(r"\n{3,}", "\n\n", h)
    return h.strip()


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=HERE, **kw)

    def log_message(self, fmt, *args):
        if "/api/" in (self.path or ""):
            sys.stderr.write("%s %s\n" % (self.command, self.path))

    # ---- helpers

    def send_json(self, obj, code=200):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def read_body(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n <= 0:
            return {}
        raw = self.rfile.read(n)
        try:
            return json.loads(raw.decode("utf-8"))
        except ValueError:
            return {}

    def qs_id(self):
        q = parse_qs(urlparse(self.path).query)
        lid = (q.get("id") or [""])[0]
        return lid if ID_OK.match(lid) else None

    # ---- routes

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/":
            self.path = "/app.html"
            return SimpleHTTPRequestHandler.do_GET(self)
        if path == "/api/outline":
            return self.send_json(load_json(OUTLINE, {"modules": []}))
        if path == "/api/lesson":
            lid = self.qs_id()
            if not lid:
                return self.send_json({"error": "bad id"}, 400)
            return self.send_json(load_json(os.path.join(LESSONS, lid + ".json"),
                                            {"id": lid, "body": "", "shapes": []}))
        if path.startswith("/api/"):
            return self.send_json({"error": "not found"}, 404)
        if path.startswith("/data/") or path.startswith("/export/"):
            return SimpleHTTPRequestHandler.do_GET(self)
        if path in ("/app.html", "/favicon.ico"):
            return SimpleHTTPRequestHandler.do_GET(self)
        return self.send_json({"error": "not found"}, 404)

    def do_PUT(self):
        return self.do_POST()

    def do_POST(self):
        path = urlparse(self.path).path
        if path == "/api/outline":
            data = self.read_body()
            if not isinstance(data.get("modules"), list):
                return self.send_json({"error": "bad outline"}, 400)
            backup(OUTLINE)
            write_atomic(OUTLINE, json.dumps(data, indent=1, ensure_ascii=False))
            return self.send_json({"ok": True})

        if path == "/api/lesson":
            lid = self.qs_id()
            if not lid:
                return self.send_json({"error": "bad id"}, 400)
            data = self.read_body()
            png = data.pop("png", None)
            data["id"] = lid
            write_atomic(os.path.join(LESSONS, lid + ".json"),
                         json.dumps(data, indent=1, ensure_ascii=False))
            if isinstance(png, str) and png.startswith("data:image/png;base64,"):
                try:
                    raw = base64.b64decode(png.split(",", 1)[1], validate=True)
                    os.makedirs(SKETCH, exist_ok=True)
                    with open(os.path.join(SKETCH, lid + ".png"), "wb") as fh:
                        fh.write(raw)
                except (ValueError, OSError):
                    pass
            return self.send_json({"ok": True})

        if path == "/api/delete-lesson":
            lid = self.qs_id()
            if not lid:
                return self.send_json({"error": "bad id"}, 400)
            for p in (os.path.join(LESSONS, lid + ".json"),
                      os.path.join(SKETCH, lid + ".png")):
                if os.path.exists(p):
                    os.unlink(p)
            return self.send_json({"ok": True})

        if path == "/api/export":
            return self.send_json(self.export())

        return self.send_json({"error": "not found"}, 404)

    # ---- export

    def export(self):
        out = load_json(OUTLINE, {"modules": []})
        lines = ["# High ticket course", "",
                 "Exported from the studio. One heading per module, one block per lesson.", ""]
        count = 0
        for m in out.get("modules", []):
            lines.append("## %s. %s" % (m.get("num", ""), m.get("name", "")))
            if m.get("blurb"):
                lines.append("")
                lines.append(m["blurb"])
            lines.append("")
            for i, les in enumerate(m.get("lessons", []), 1):
                d = load_json(os.path.join(LESSONS, les.get("id", "") + ".json"), {})
                title = d.get("title") or les.get("title") or "Untitled"
                lines.append("### %s.%d %s" % (m.get("slug", "m"), i, title))
                lines.append("")
                if d.get("lede"):
                    lines.append("*%s*" % d["lede"])
                    lines.append("")
                if d.get("deliverable"):
                    lines.append("**They leave with:** %s" % d["deliverable"])
                    lines.append("")
                body = html_to_md(d.get("body", ""))
                lines.append(body if body else "_blank_")
                lines.append("")
                shapes = d.get("shapes") or []
                if shapes:
                    lines.append("_sketch: %d shapes, data/sketches/%s.png_"
                                 % (len(shapes), les.get("id", "")))
                    lines.append("")
                count += 1
        os.makedirs(EXPORT, exist_ok=True)
        write_atomic(os.path.join(EXPORT, "COURSE.md"), "\n".join(lines) + "\n")
        return {"ok": True, "lessons": count,
                "path": os.path.join(EXPORT, "COURSE.md")}


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 4330
    for d in (DATA, LESSONS, SKETCH, EXPORT):
        os.makedirs(d, exist_ok=True)
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print("studio on http://127.0.0.1:%d" % port)
    srv.serve_forever()


if __name__ == "__main__":
    main()
