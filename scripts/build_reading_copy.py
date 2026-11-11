#!/usr/bin/env python3
"""Build a complete local review page from the current studio, without publishing."""
from pathlib import Path
import subprocess
import sys
import tempfile
import shutil

ROOT = Path(__file__).resolve().parents[1]


def main():
    shutil.copytree(ROOT / "skills/jarvis-confirmation-page/assets/course-demo", ROOT / "course/studio/data/demos/confirmation", dirs_exist_ok=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/build_student_pack.py")], check=True)
    target = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "course/reading-copy/index.html"
    with tempfile.TemporaryDirectory() as tmp:
        fragment = Path(tmp) / "fragment.html"
        subprocess.run([sys.executable, str(ROOT / "course/reading-copy/build.py"), str(fragment)], check=True)
        text = fragment.read_text(encoding="utf-8")
    head, body = text.split("</style>", 1)
    page = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
            '<meta name="robots" content="noindex,nofollow">\n' + head +
            '</style>\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(page, encoding="utf-8")
    for folder in ("img", "sketches", "demos"):
        assets = ROOT / "course/studio/data" / folder
        if assets.is_dir():
            shutil.copytree(assets, target.parent / "data" / folder, dirs_exist_ok=True)
    print(target)


if __name__ == "__main__":
    main()
