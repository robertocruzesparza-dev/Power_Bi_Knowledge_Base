"""Validate the KB. Exit code 1 when any ERROR is found.

Usage:
  python tools/validate_kb.py [KB_ROOT] [--paths PREFIX ...] [--strict-lint]
KB_ROOT defaults to the parent of tools/. With --paths only files whose path
starts with a prefix get per-file checks; global checks (orphans, indexes) skip.
Warnings (style lint) are listed but do not fail unless --strict-lint is set.
"""
import os
import re
import sys
from collections import deque

import kbcommon as kc
import lint3c

REQ = ["id", "title", "domain", "type", "level", "tags", "summary", "status",
       "volatile", "last_verified", "confidence", "sources", "references", "related"]
ENUMS = {
    "type": {"concept", "how-to", "reference", "troubleshooting", "comparison", "decision", "index"},
    "level": {"beginner", "intermediate", "advanced"},
    "status": {"ga", "preview", "deprecated", "retired", "mixed", "n/a"},
    "volatile": {"true", "false"},
    "confidence": {"high", "moderate", "low"},
}
LIMIT = 200
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}$")


def glossary_terms(root):
    terms = set()
    for rel in kc.walk(root, ".md"):
        if rel.startswith("GLOSSARY"):
            text = kc.read(os.path.join(root, rel))
            terms |= set(re.findall(r"^- \*\*([A-Za-z0-9]+)\*\*", text, re.M))
    return terms


def dax_names(root):
    names = set()
    for rel in kc.walk(root, ".md"):
        if rel.startswith("references/dax/"):
            names |= set(re.findall(r"[A-Z][A-Z0-9]+", kc.read(os.path.join(root, rel))))
    return names


def as_list(v):
    return v if isinstance(v, list) else []


def check_file(root, rel, ctx, errs, warns):
    text = kc.read(os.path.join(root, rel))
    n = len(text.rstrip("\n").split("\n")) if text else 0
    if n >= LIMIT:
        errs.append(f"{rel}: {n} lines (limit {LIMIT - 1})")
    if not rel.endswith(".md"):
        return
    fm, body = kc.parse_front(text)
    if fm is None:
        errs.append(f"{rel}: missing front matter")
        return
    for k in REQ:
        if k not in fm:
            errs.append(f"{rel}: missing field '{k}'")
    for k, allowed in ENUMS.items():
        if k in fm and fm[k] not in allowed:
            errs.append(f"{rel}: bad {k} '{fm[k]}'")
    if "id" in fm:
        if fm["id"] in ctx["ids"]:
            errs.append(f"{rel}: duplicate id {fm['id']} (also {ctx['ids'][fm['id']]})")
        ctx["ids"][fm["id"]] = rel
    for t in as_list(fm.get("tags")):
        if t not in ctx["tags"]:
            errs.append(f"{rel}: unknown tag '{t}'")
    if len(str(fm.get("summary", "")).split()) > 25:
        errs.append(f"{rel}: summary over 25 words")
    if fm.get("volatile") == "true" and not DATE_RE.match(str(fm.get("last_verified", ""))):
        errs.append(f"{rel}: volatile file needs last_verified date")
    for s in as_list(fm.get("sources")):
        if s not in ctx["sources"]:
            errs.append(f"{rel}: unknown source {s}")
    hs = kc.headings(body)
    if n > 100:
        if "## Table of Contents" not in body:
            errs.append(f"{rel}: over 100 lines, no Table of Contents")
        else:
            toc = body.split("## Table of Contents", 1)[1].split("\n## ", 1)[0]
            for _lv, h in hs:
                if h != "Table of Contents" and f"(#{kc.slugify(h)})" not in toc:
                    errs.append(f"{rel}: TOC missing '{h}'")
    is_meta = rel.startswith(("meta/", "TAGS", "GLOSSARY", "INDEX")) or "_domain_index" in rel
    msgs = lint3c.banned_syntax(body) + ([] if is_meta else lint3c.table_problems(body))
    errs.extend(f"{rel}: {m}" for m in msgs)
    avg = lint3c.avg_sentence_len(body)
    if avg > 20 and not is_meta:
        warns.append(f"{rel}: average sentence length {avg:.1f} words")
    bad = [] if is_meta else lint3c.undefined_acronyms(body, ctx["gloss"])
    if bad:
        warns.append(f"{rel}: undefined acronyms {', '.join(bad)}")
    base = os.path.dirname(rel)
    for _t, href in kc.LINK_RE.findall(text):
        if re.match(r"[a-z]+:", href):
            continue
        target = href.split("#")[0]
        if not target:
            continue
        path = os.path.normpath(os.path.join(base, target)).replace(os.sep, "/")
        if not os.path.exists(os.path.join(root, path)):
            errs.append(f"{rel}: broken link {href}")
        else:
            ctx["links"].setdefault(rel, set()).add(path)


def global_checks(root, mds, ctx, errs):
    seen, queue = {"00_START_HERE.md"}, deque(["00_START_HERE.md"])
    while queue:
        for nxt in ctx["links"].get(queue.popleft(), ()):
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    for rel in mds:
        if rel not in seen:
            errs.append(f"{rel}: orphan (not reachable from 00_START_HERE.md)")
    dom_idx = {os.path.dirname(r): ctx["links"].get(r, set())
               for r in mds if r.endswith("/_domain_index.md")}
    if not dom_idx:
        errs.append("no _domain_index.md files found")
    for rel in mds:
        top = rel.split("/")[0]
        if "/" not in rel or rel.endswith("_domain_index.md") or top in ("meta", "data", "tools"):
            continue
        dom = ctx["domain_of"].get(rel)
        folder = next((d for d in dom_idx if d.split("_", 1)[-1] == dom), None)
        if folder is None or rel not in dom_idx[folder]:
            errs.append(f"{rel}: not listed in its domain index")


def main(argv):
    prefixes = []
    if "--paths" in argv:
        i = argv.index("--paths") + 1
        prefixes = [a for a in argv[i:] if not a.startswith("--")]
        argv = argv[:i - 1] + [a for a in argv[i:] if a.startswith("--")]
    pos = [a for a in argv if not a.startswith("--")]
    root = os.path.abspath(pos[0] if pos else os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    errs, warns = [], []
    ctx = {"ids": {}, "links": {}, "domain_of": {}, "tags": kc.load_tags(root),
           "sources": kc.load_source_ids(root), "gloss": glossary_terms(root) | dax_names(root)}
    files = kc.walk(root)
    for rel in files:
        if rel.endswith(".md"):
            fm, _ = kc.parse_front(kc.read(os.path.join(root, rel)))
            if fm:
                ctx["domain_of"][rel] = fm.get("domain")
    for rel in files:
        if prefixes and not any(rel.startswith(p) for p in prefixes):
            continue
        check_file(root, rel, ctx, errs, warns)
    mds = [f for f in files if f.endswith(".md")]
    if not prefixes:
        global_checks(root, mds, ctx, errs)
    for w in warns:
        print("WARN  " + w)
    for e in errs:
        print("ERROR " + e)
    print(f"files={len(files)} md={len(mds)} errors={len(errs)} warnings={len(warns)}")
    if "--strict-lint" in argv and warns:
        return 1
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
