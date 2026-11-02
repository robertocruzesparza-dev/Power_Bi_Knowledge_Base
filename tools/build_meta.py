"""Build meta/GAPS.md, meta/CLAIMS.md and meta/SOURCES.md from hand-off notes and source shards.

Usage: python tools/build_meta.py [KB_ROOT]
Inputs: meta/gaps_in/*.txt ('domain|missing|why|next'), meta/claims_in/*.txt
('file|claim|source'), meta/sources/*.md. Outputs are sharded under 150 rows each.
Lines that do not fit the pipe format are kept as free-text notes.
"""
import os
import sys

import kbcommon as kc

HEAD = ("---\nid: {id}\ntitle: {title}\ndomain: meta\ntype: reference\nlevel: intermediate\n"
        "tags: [metadata, reference]\nsummary: {summary}\nstatus: n/a\nvolatile: false\n"
        "last_verified: 2026-10-07\nconfidence: moderate\nsources: []\nreferences: []\nrelated: []\n---\n\n")
PER = 70


def lines_of(root, folder):
    base = os.path.join(root, "meta", folder)
    out = []
    for name in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        for line in kc.read(os.path.join(base, name)).split("\n"):
            if line.strip():
                out.append((name[:-4], line.strip()))
    return out


def emit(root, stem, title, summary, cols, rows, intro):
    chunks = [rows[i:i + PER] for i in range(0, max(len(rows), 1), PER)]
    for n, ch in enumerate(chunks, 1):
        name = f"meta/{stem}.md" if n == 1 else f"meta/{stem}_part{n}.md"
        nav = " | ".join(f"[part {i}]({stem}{'' if i == 1 else f'_part{i}'}.md)" for i in range(1, len(chunks) + 1))
        body = [f"# {title}", "", intro, "", f"Parts: {nav}", "", "| " + " | ".join(cols) + " |",
                "|" + "---|" * len(cols)]
        body += ["| " + " | ".join(r) + " |" for r in ch]
        text = HEAD.format(id=f"meta.{stem}{'' if n == 1 else n}", title=f"{title} part {n}", summary=summary) + "\n".join(body) + "\n"
        with open(os.path.join(root, name), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)


def split(line, n, worker):
    parts = [p.strip().replace("|", "/") for p in line.split("|")]
    if len(parts) < n:
        parts = [parts[0]] + [""] * (n - 1 - len(parts)) + parts[1:] if False else parts + [""] * (n - len(parts))
    return [worker] + parts[:n]


def main(root):
    gaps = [split(l, 4, w) for w, l in lines_of(root, "gaps_in")]
    emit(root, "GAPS", "Known gaps", "Unfilled coverage gaps by domain, with reasons and where to look next.",
         ["Worker", "Domain", "Missing", "Why", "Look next"], gaps, "Each row is a gap logged during research on 2026-10-07. Verifiers filled some of them on 2026-10-08; see the re-verification log. Treat every domain as incomplete where listed.")
    claims = [split(l, 3, w) for w, l in lines_of(root, "claims_in")]
    emit(root, "CLAIMS", "High-impact volatile claims", "Highest-impact volatile claims queued for re-verification.",
         ["Worker", "File", "Claim", "Source"], claims, "Claims to re-check against official sources before each release of this KB.")
    ver = [split(l, 5, w) for w, l in lines_of(root, "verification_in")]
    emit(root, "VERIFICATION", "Re-verification log", "Claims re-checked against live sources on 2026-10-08, with results.",
         ["Verifier", "File", "Claim", "Result", "Note", "Source"], ver, "Result is confirmed, corrected, or unresolved. Rows come from the three verification passes.")
    shards = sorted(f for f in os.listdir(os.path.join(root, "meta/sources")) if f.endswith(".md"))
    total = sum(1 for f in shards for l in kc.read(os.path.join(root, "meta/sources", f)).split("\n") if l.startswith("| S"))
    body = ["# Sources register", "", f"{total} sources in {len(shards)} shards. Columns: ID, title, author, URL, type and tier, published, retrieved, access.",
            "Tier 1 official, 2 expert, 3 community, 4 other.", ""] + [f"- [{f}](sources/{f})" for f in shards]
    with open(os.path.join(root, "meta/SOURCES.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(HEAD.format(id="meta.sources", title="Sources register", summary="Index of source register shards with the tier scheme.") + "\n".join(body) + "\n")
    print(f"verification={len(ver)} gaps={len(gaps)} claims={len(claims)} sources={total} shards={len(shards)}")


if __name__ == "__main__":
    main(os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
