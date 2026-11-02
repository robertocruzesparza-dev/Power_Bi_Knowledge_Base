"""Regenerate every _domain_index.md, INDEX.md, and data/index/*.jsonl from front matter.

Usage: python tools/build_index.py [KB_ROOT]
Reads data/domains.csv (number, slug, scope). Core files live in NN_slug/ and
reference files in references/<slug>/; both are listed in that domain's index.
Domain indexes over 70 rows are split into _domain_index_partN.md files.
"""
import csv
import json
import os
import sys

import kbcommon as kc

TODAY = "2026-10-07"
HEAD = ("---\nid: {id}\ntitle: {title}\ndomain: {domain}\ntype: index\nlevel: beginner\n"
        "tags: [index, navigation]\nsummary: {summary}\nstatus: n/a\nvolatile: false\n"
        "last_verified: {date}\nconfidence: high\nsources: []\nreferences: []\nrelated: []\n---\n\n")
ROWS = 70
TAG_ROWS = 150


def esc(s):
    return str(s).replace("|", "/")


def load_files(root, domains):
    by_dom = {slug: [] for _n, slug, _s in domains}
    for rel in kc.walk(root, ".md"):
        if rel.endswith("_domain_index.md") or "_domain_index_part" in rel:
            continue
        fm, _ = kc.parse_front(kc.read(os.path.join(root, rel)))
        if fm and fm.get("domain") in by_dom:
            by_dom[fm["domain"]].append((rel, fm))
    return by_dom


def write(root, rel, text):
    with open(os.path.join(root, rel), "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)


def domain_index(root, num, slug, scope, files, date):
    folder = f"{num}_{slug}"
    os.makedirs(os.path.join(root, folder), exist_ok=True)
    files = sorted(files, key=lambda x: (x[0].startswith("references/"), x[0]))
    chunks = [files[i:i + ROWS] for i in range(0, max(len(files), 1), ROWS)]
    names = ["_domain_index.md"] + [f"_domain_index_part{i}.md" for i in range(2, len(chunks) + 1)]
    for name, chunk in zip(names, chunks):
        body = [f"# Domain index: {slug.replace('_', ' ')}", "", f"Scope: {scope}", "",
                "[Back to INDEX](../INDEX.md)", ""]
        if name == "_domain_index.md" and len(chunks) > 1:
            body += [f"More rows: [part {i}](_domain_index_part{i}.md)" for i in range(2, len(chunks) + 1)] + [""]
        body += ["| ID | Title | Kind | Tags | Summary | Path |", "|---|---|---|---|---|---|"]
        for rel, fm in chunk:
            kind = "reference" if rel.startswith("references/") else "core"
            link = os.path.relpath(rel, folder).replace(os.sep, "/")
            tags = ", ".join(fm.get("tags", [])) if isinstance(fm.get("tags"), list) else fm.get("tags", "")
            body.append(f"| {fm.get('id')} | {esc(fm.get('title'))} | {kind} | {tags} | {esc(fm.get('summary'))} | [{rel.split('/')[-1]}]({link}) |")
        write(root, f"{folder}/{name}", HEAD.format(**{
            "id": f"{num}.{name[:-3].strip('_')}", "title": f"Index of {slug.replace('_', ' ')}", "domain": slug,
            "summary": f"Lists every file in the {slug.replace('_', ' ')} domain with tags and summaries.", "date": date}) + "\n".join(body) + "\n")


def jsonl(root, slug, files):
    os.makedirs(os.path.join(root, "data/index"), exist_ok=True)
    for old in os.listdir(os.path.join(root, "data/index")):
        if old.startswith(slug + "_") and old.endswith(".jsonl"):
            os.remove(os.path.join(root, "data/index", old))
    lines = [json.dumps({"path": rel, **{k: fm.get(k) for k in ("id", "title", "type", "level", "tags", "summary", "status", "volatile", "last_verified", "confidence")}}, ensure_ascii=False) for rel, fm in files]
    for i in range(0, max(len(lines), 1), ROWS):
        write(root, f"data/index/{slug}_{i // ROWS + 1}.jsonl", "\n".join(lines[i:i + ROWS]) + "\n")


def tag_index(root):
    tags = set()
    for rel in kc.walk(root, ".md"):
        if rel.startswith("TAGS"):
            continue
        fm, _ = kc.parse_front(kc.read(os.path.join(root, rel)))
        if fm and isinstance(fm.get("tags"), list):
            tags.update(fm["tags"])
    ordered = sorted(tags)
    chunks = [ordered[i:i + TAG_ROWS] for i in range(0, max(len(ordered), 1), TAG_ROWS)]
    for number, chunk in enumerate(chunks, 1):
        name = "TAGS.md" if number == 1 else f"TAGS_part{number}.md"
        nav = " | ".join(
            ["[TAGS](TAGS.md)"] +
            [f"[part {i}](TAGS_part{i}.md)" for i in range(2, len(chunks) + 1)]
        )
        body = [
            f"# Tag registry part {number}",
            "",
            nav,
            "",
            "Use these labels to find related topics in the domain indexes and JSONL indexes.",
            "",
            "## Table of Contents",
            "",
            "- [Tag labels](#tag-labels)",
            "",
            "## Tag labels",
            "",
        ]
        body.extend(f"- `{tag}`: Topic label for {tag.replace('-', ' ')}." for tag in chunk)
        write(root, name, HEAD.format(
            id=f"00.tags{'' if number == 1 else number}",
            title=f"Tag registry part {number}",
            domain="meta",
            summary="Registered tags used to filter and navigate Power BI knowledge-base articles.",
            date=TODAY,
        ) + "\n".join(body) + "\n")


def top_index(root, domains, by_dom):
    rows = ["| Folder | What it covers | Core | Refs | Index |", "|---|---|---|---|---|"]
    for num, slug, scope in domains:
        fl = by_dom[slug]
        core = sum(1 for r, _ in fl if not r.startswith("references/"))
        rows.append(f"| {num}_{slug} | {esc(scope)} | {core} | {len(fl) - core} | [index]({num}_{slug}/_domain_index.md) |")
    body = ["# KB index", "", "Pick the domain that matches the question, open its index, then open the file.", "",
            "Also read: [00_START_HERE](00_START_HERE.md), [TAGS](TAGS.md), [GLOSSARY](GLOSSARY.md), [GAPS](meta/GAPS.md), [SOURCES](meta/SOURCES.md).", ""] + rows
    write(root, "INDEX.md", HEAD.format(id="00.index", title="KB top-level index", domain="meta",
          summary="One row per domain with scope, file counts, and a link to the domain index.", date=TODAY) + "\n".join(body) + "\n")


def main(root):
    with open(os.path.join(root, "data/domains.csv"), encoding="utf-8") as fh:
        domains = [(r["number"], r["slug"], r["scope"]) for r in csv.DictReader(fh)]
    by_dom = load_files(root, domains)
    for num, slug, scope in domains:
        domain_index(root, num, slug, scope, by_dom[slug], TODAY)
        jsonl(root, slug, sorted(by_dom[slug], key=lambda x: x[0]))
    tag_index(root)
    top_index(root, domains, by_dom)
    print("indexed", sum(len(v) for v in by_dom.values()), "files in", len(domains), "domains")


if __name__ == "__main__":
    main(os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
