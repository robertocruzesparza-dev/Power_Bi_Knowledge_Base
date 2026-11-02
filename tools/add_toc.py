"""Insert or refresh '## Table of Contents' in markdown files over 100 lines.

Usage: python tools/add_toc.py FILE [FILE ...]   (paths relative to KB root or absolute)
The TOC goes directly after the front matter. Lists every H2 and H3 as an anchor link.
Files of 100 lines or fewer are left unchanged. Re-run after any heading edit.
"""
import os
import re
import sys

import kbcommon as kc


def build_toc(body):
    lines = ["## Table of Contents", ""]
    for lvl, h in kc.headings(body):
        if h == "Table of Contents":
            continue
        lines.append(f"{'  ' * (lvl - 2)}- [{h}](#{kc.slugify(h)})")
    return "\n".join(lines) + "\n"


def process(path):
    text = kc.read(path)
    m = kc.FM_RE.match(text)
    if not m:
        return "skip (no front matter)"
    head, body = text[:m.end()], text[m.end():]
    body = re.sub(r"\n*## Table of Contents\n.*?(?=\n## |\Z)", "\n", body, flags=re.S).lstrip("\n")
    for _ in range(3):  # TOC adds lines; iterate until the 100-line decision is stable
        toc = build_toc(body)
        total = (head + "\n" + toc + "\n" + body).count("\n")
        if total <= 100:
            new = head + body
            break
        new = head + "\n" + toc + "\n" + body
        break
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(new)
    return "toc" if new != head + body else "no toc needed"


if __name__ == "__main__":
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    for arg in sys.argv[1:]:
        p = arg if os.path.isabs(arg) else os.path.join(root, arg)
        print(arg, process(p))
