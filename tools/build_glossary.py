"""Merge meta/glossary_in/*.txt ('TERM|definition' per line) into GLOSSARY*.md.

Usage: python tools/build_glossary.py [KB_ROOT]
Deduplicates case-insensitively (first definition wins), sorts alphabetically,
and shards into GLOSSARY.md, GLOSSARY_part2.md, ... of at most 75 entries each.
"""
import os
import sys

import kbcommon as kc

PER = 75


def entries(root):
    seen, out = set(), []
    base = os.path.join(root, "meta/glossary_in")
    for name in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        for line in kc.read(os.path.join(base, name)).split("\n"):
            if "|" not in line:
                continue
            term, _, d = line.partition("|")
            term, d = term.strip(), d.strip()
            if term and d and term.lower() not in seen:
                seen.add(term.lower())
                out.append((term, d))
    return sorted(out, key=lambda x: x[0].lower())


def main(root):
    items = entries(root)
    chunks = [items[i:i + PER] for i in range(0, max(len(items), 1), PER)]
    for n, chunk in enumerate(chunks, 1):
        name = "GLOSSARY.md" if n == 1 else f"GLOSSARY_part{n}.md"
        rng = f"{chunk[0][0]} to {chunk[-1][0]}" if chunk else "empty"
        head = (f"---\nid: 00.glossary{'' if n == 1 else n}\ntitle: Glossary part {n}\ndomain: meta\ntype: reference\n"
                f"level: beginner\ntags: [glossary, reference]\nsummary: Terms and acronyms {rng}, one line each.\n"
                "status: n/a\nvolatile: false\nlast_verified: 2026-10-07\nconfidence: moderate\nsources: []\n"
                "references: []\nrelated: []\n---\n\n")
        nav = " | ".join(["[GLOSSARY](GLOSSARY.md)"] + [f"[part {i}](GLOSSARY_part{i}.md)" for i in range(2, len(chunks) + 1)])
        body = f"# Glossary part {n}\n\nParts: {nav}\n\n" + "\n".join(f"- **{t}**: {d}" for t, d in chunk) + "\n"
        with open(os.path.join(root, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(head + body)
    print(f"{len(items)} terms in {len(chunks)} file(s)")


if __name__ == "__main__":
    main(os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
