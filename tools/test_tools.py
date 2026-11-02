"""Tests for the KB tools, using temporary mini knowledge bases.

Usage: python tools/test_tools.py
Checks that validate_kb.py accepts a clean KB and flags each seeded defect, and that
add_toc, build_index, split_file and build_glossary behave deterministically.
"""
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable


def run(script, *args):
    r = subprocess.run([PY, os.path.join(HERE, script), *args], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


def doc(id_, domain="alpha", tags="[power-bi]", body="Short body.", extra=""):
    return (f"---\nid: {id_}\ntitle: T\ndomain: {domain}\ntype: concept\nlevel: beginner\ntags: {tags}\n"
            f"summary: A summary.\nstatus: ga\nvolatile: false\nlast_verified: 2026-10-07\nconfidence: high\n"
            f"sources: []\nreferences: []\nrelated: []\n{extra}---\n\n# T\n\n{body}\n")


def write(root, rel, text):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def make_kb():
    root = tempfile.mkdtemp()
    write(root, "TAGS.md", doc("00.tags", "meta", "[power-bi]", "- `power-bi`: x\n- `index`: y\n- `navigation`: z"))
    write(root, "data/domains.csv", 'number,slug,scope\n01,alpha,"Alpha scope"\n')
    write(root, "01_alpha/01_topic.md", doc("01.topic", body="See [home](../00_START_HERE.md)."))
    write(root, "00_START_HERE.md", doc("00.start", "meta", body="[Index](INDEX.md) [Topic](01_alpha/01_topic.md)"))
    write(root, "GLOSSARY.md", doc("00.glossary", "meta"))
    write(root, "meta/GAPS.md", doc("meta.gaps", "meta"))
    write(root, "meta/SOURCES.md", doc("meta.sources", "meta"))
    return root


class Tools(unittest.TestCase):
    def test_clean_kb_passes_after_index_build(self):
        root = make_kb()
        self.assertEqual(run("build_index.py", root)[0], 0)
        write(root, "00_START_HERE.md", doc("00.start", "meta", body="[Index](INDEX.md) [Topic](01_alpha/01_topic.md)"))
        code, out = run("validate_kb.py", root)
        self.assertEqual(code, 0, out)

    def test_flags_unknown_tag_and_long_file(self):
        root = make_kb()
        write(root, "01_alpha/01_bad.md", doc("01.bad", tags="[nonsense]", body="x\n" * 210))
        code, out = run("validate_kb.py", root, "--paths", "01_alpha/")
        self.assertEqual(code, 1)
        self.assertIn("unknown tag 'nonsense'", out)
        self.assertIn("limit 199", out)

    def test_flags_duplicate_id_and_broken_link(self):
        root = make_kb()
        write(root, "01_alpha/01_dup.md", doc("01.topic", body="[x](missing.md)"))
        code, out = run("validate_kb.py", root, "--paths", "01_alpha/")
        self.assertEqual(code, 1)
        self.assertIn("duplicate id", out)
        self.assertIn("broken link", out)

    def test_toc_required_and_added(self):
        root = make_kb()
        body = "## Alpha\n\n" + "line\n" * 60 + "## Beta\n\n" + "line\n" * 60
        write(root, "01_alpha/01_long.md", doc("01.long", body=body))
        self.assertIn("no Table of Contents", run("validate_kb.py", root, "--paths", "01_alpha/")[1])
        run("add_toc.py", os.path.join(root, "01_alpha/01_long.md"))
        code, out = run("validate_kb.py", root, "--paths", "01_alpha/")
        self.assertEqual(code, 0, out)

    def test_split_proposal_and_glossary(self):
        root = make_kb()
        body = "\n".join(f"## S{i}\n" + "line\n" * 70 for i in range(4))
        write(root, "01_alpha/01_big.md", doc("01.big", body=body))
        out = run("split_file.py", os.path.join(root, "01_alpha/01_big.md"))[1]
        self.assertIn("part 2", out)
        write(root, "meta/glossary_in/a.txt", "Zed|last\nAlpha|first\nalpha|dup\n")
        self.assertIn("2 terms", run("build_glossary.py", root)[1])


if __name__ == "__main__":
    unittest.main()
