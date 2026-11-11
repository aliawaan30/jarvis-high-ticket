#!/usr/bin/env python3
"""Generate/check the portable course inventory. Does not invoke agents or send messages."""
import argparse
import hashlib
import html
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/REPOSITORY-MANIFEST.json"


class Assets(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sources = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key == "src" and value and not value.startswith(("http:", "https:", "data:", "//")):
                self.sources.append(value.split("?", 1)[0].split("#", 1)[0])


def paths():
    names = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"], cwd=ROOT
    ).decode().split("\0")
    return sorted({n for n in names if n and n != "docs/REPOSITORY-MANIFEST.json" and (ROOT / n).is_file()})


def inspect():
    outline = json.loads((ROOT / "course/studio/data/outline.json").read_text())
    modules = []
    seen = set()
    for module in outline["modules"]:
        lessons = []
        for entry in module["lessons"]:
            ident = entry["id"]
            if ident in seen:
                raise ValueError("Duplicate outline lesson: " + ident)
            seen.add(ident)
            path = ROOT / "course/studio/data/lessons" / (ident + ".json")
            data = json.loads(path.read_text())
            if data.get("id") != ident:
                raise ValueError("Lesson ID mismatch: " + ident)
            body = data.get("body", "")
            words = len(html.unescape(re.sub("<[^>]+>", " ", body)).split())
            parser = Assets()
            parser.feed(body)
            for source in parser.sources:
                target = ROOT / "course/studio" / source.lstrip("/")
                if not target.is_file():
                    raise ValueError("Missing lesson asset: " + ident + " -> " + source)
            lessons.append({"id": ident, "title": data.get("title") or entry["title"], "body_words": words})
        modules.append({"number": module["num"], "name": module["name"], "lessons": lessons})

    for skill in (ROOT / "skills").glob("*/SKILL.md"):
        text = skill.read_text()
        if not text.startswith("---\n") or not re.search(r"^name: .+", text, re.M) or not re.search(r"^description: .+", text, re.M):
            raise ValueError("Invalid skill frontmatter: " + str(skill.relative_to(ROOT)))
        for source in re.findall(r"\]\(((?:references|assets)/[^)#]+)(?:#[^)]*)?\)", text):
            if not (skill.parent / source).is_file():
                raise ValueError("Missing skill resource: " + str(skill.relative_to(ROOT)) + " -> " + source)
    for path in (ROOT / "skills").rglob("*.md"):
        if "\u2014" in path.read_text():
            raise ValueError("Em dash in canonical skill: " + str(path.relative_to(ROOT)))
    return modules


def write_reports(modules):
    total = sum(len(m["lessons"]) for m in modules)
    drafted = sum(l["body_words"] > 0 for m in modules for l in m["lessons"])
    lines = ["# Current course status", "", f"{len(modules)} modules, {total} ordered lessons. {drafted} have body text; {total-drafted} have no body text.", "",
             "Body text is an inventory measure, not proof of lesson quality, filmed video, tool functionality or student readiness. The studio JSON is the authoring source. This report does not change the course.", "",
             "| Module | Lessons | With body text | No body text |", "|---|---:|---:|---:|"]
    for m in modules:
        n = sum(l["body_words"] > 0 for l in m["lessons"])
        lines.append(f'| {m["number"]} {m["name"]} | {len(m["lessons"])} | {n} | {len(m["lessons"])-n} |')
    spec = importlib.util.spec_from_file_location("course_studio_export", ROOT / "course/studio/server.py")
    studio = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(studio)
    exported = ["# High ticket course working text", "", "Generated from current studio JSON. Drafts and empty lessons remain visible. Technical status is in docs/COURSE-STATUS.md.", ""]
    for m in modules:
        lines.extend(["", f'## {m["number"]} {m["name"]}', ""])
        exported.extend([f'## {m["number"]} {m["name"]}', ""])
        for lesson in m["lessons"]:
            ident = lesson["id"]
            lines.append(f'- [{lesson["title"]}](../course/studio/data/lessons/{ident}.json): {lesson["body_words"]} body words' + ("; no body text yet." if not lesson["body_words"] else "; draft text present."))
            data = json.loads((ROOT / "course/studio/data/lessons" / (ident + ".json")).read_text())
            exported.extend([f'### {lesson["title"]}', "", data.get("lede", ""), "", studio.html_to_md(data.get("body", "")) or "No lesson body written yet.", ""])
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs/COURSE-STATUS.md").write_text("\n".join(lines) + "\n")
    (ROOT / "course/studio/export").mkdir(exist_ok=True)
    (ROOT / "course/studio/export/COURSE.md").write_text("\n".join(line.rstrip() for line in "\n".join(exported).splitlines()) + "\n")
    files = {name: {"bytes": (ROOT / name).stat().st_size, "sha256": hashlib.sha256((ROOT / name).read_bytes()).hexdigest()} for name in paths()}
    MANIFEST.write_text(json.dumps({"scope": "Current repository files excluding this manifest and Git-ignored local state", "modules": len(modules), "lessons": total, "lessons_with_body": drafted, "canonical_skills": len(list((ROOT / "skills").glob("*/SKILL.md"))), "files": files}, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    modules = inspect()
    if args.write:
        write_reports(modules)
    if args.check:
        saved = json.loads(MANIFEST.read_text())
        expected = saved["files"]
        actual = set(paths())
        if actual != set(expected):
            raise ValueError("Manifest file list changed; regenerate with --write")
        for name, record in expected.items():
            if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != record["sha256"]:
                raise ValueError("Manifest hash mismatch: " + name)
    print(json.dumps({"modules": len(modules), "lessons": sum(len(m["lessons"]) for m in modules), "canonical_skills": len(list((ROOT / "skills").glob("*/SKILL.md"))), "status": "checks passed", "agent_execution_tested": False}))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError) as exc:
        sys.exit(str(exc))
