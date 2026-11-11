#!/usr/bin/env python3
"""One off: lift the page shell (head CSS + tail JS) out of the free course so
this course looks and behaves identically. Run again only if the free course
shell changes and you want to re-sync.

    python3 tools/extract_shell.py

Writes shell/head.html and shell/tail.html with {{TITLE}} and {{KEY}} tokens.
"""
import pathlib, re

SRC = pathlib.Path(
    "/Users/blakestephens/co-founder/projects/base44-course/portal/public/courses/receptionists/receptionists-b.html"
)
OUT = pathlib.Path(__file__).resolve().parent.parent / "shell"

t = SRC.read_text(encoding="utf-8")

head = t[: t.index("</head>") + len("</head>")]
tail = t[t.rindex("</main>"):]

# no auth gate on this course yet, see README
head = head.replace('<script src="/gate.js"></script>\n', "")
head = re.sub(r"<title>.*?</title>", "<title>{{TITLE}}</title>", head, count=1)
head = head.replace("<meta charset=\"utf-8\">",
                    "<meta charset=\"utf-8\">\n<meta name=\"robots\" content=\"noindex\">", 1)

# per page progress key, the free course builder left every page sharing one
tail = tail.replace("var KEY='course.m6.b';", "var KEY='{{KEY}}';", 1)
assert "{{KEY}}" in tail, "progress key not found, shell changed"

OUT.mkdir(exist_ok=True)
(OUT / "head.html").write_text(head, encoding="utf-8")
(OUT / "tail.html").write_text(tail, encoding="utf-8")
print(f"head {len(head)} bytes, tail {len(tail)} bytes")
