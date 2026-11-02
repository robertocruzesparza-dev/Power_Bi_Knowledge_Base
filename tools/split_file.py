"""Propose split points for a markdown file at or over the line limit.

Usage: python tools/split_file.py FILE [--limit 199]
Prints H2 boundaries (line numbers, sizes) and a greedy grouping into parts that
each fit the limit. It never edits files; a human or AI performs the split.
"""
import re
import sys

import kbcommon as kc


def main(argv):
    path = argv[0]
    limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else 199
    lines = kc.read(path).split("\n")
    fm = kc.FM_RE.match("\n".join(lines))
    head_len = fm.group(0).count("\n") if fm else 0
    cuts = [i for i, l in enumerate(lines) if re.match(r"## ", l) and i >= head_len] + [len(lines)]
    print(f"{path}: {len(lines)} lines; front matter {head_len}; limit {limit}")
    if len(lines) <= limit:
        print("within limit; no split needed")
        return
    part, size, parts = [], head_len, []
    for a, b in zip(cuts, cuts[1:]):
        n = b - a
        if part and size + n > limit:
            parts.append(part)
            part, size = [], head_len
        part.append((a + 1, lines[a], n))
        size += n
    parts.append(part)
    for i, p in enumerate(parts, 1):
        print(f"part {i}: ~{sum(n for _, _, n in p) + head_len} lines")
        for ln, title, n in p:
            print(f"   line {ln:4d} ({n:3d} lines) {title}")


if __name__ == "__main__":
    main(sys.argv[1:])
