"""Shared helpers for KB tools (front matter parsing, file walking, slugs).

Usage: imported by the other scripts in tools/. Python standard library only.
"""
import os
import re

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)")


def read(path):
    with open(path, encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


def parse_value(raw):
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        return [x.strip() for x in inner.split(",") if x.strip()]
    if len(raw) > 1 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    return raw


def parse_front(text):
    """Return (dict, body). dict is None when no front matter exists."""
    m = FM_RE.match(text)
    if not m:
        return None, text
    data = {}
    for line in m.group(1).split("\n"):
        if ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            data[key.strip()] = parse_value(val)
    return data, text[m.end():]


def walk(root, exts=None):
    """Yield relative posix paths of files under root, sorted."""
    out = []
    for base, dirs, files in os.walk(root):
        dirs[:] = [name for name in dirs if name not in (".git", "__pycache__")]
        for name in files:
            full = os.path.join(base, name)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            if exts is None or rel.endswith(exts):
                out.append(rel)
    return sorted(out)


def slugify(heading):
    """GitHub-style anchor slug for a heading."""
    s = heading.strip().lower()
    s = re.sub(r"[`*_]", "", s)
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def headings(body):
    """Return [(level, text)] for H2/H3 outside code fences."""
    out, fence = [], False
    for line in body.split("\n"):
        if line.startswith("```"):
            fence = not fence
        m = re.match(r"(#{2,3}) (.+)", line)
        if m and not fence:
            out.append((len(m.group(1)), m.group(2).strip()))
    return out


def load_tags(root):
    tags = set()
    for rel in walk(root, ".md"):
        if re.match(r"TAGS(_part\d+)?\.md$", rel):
            for line in read(os.path.join(root, rel)).split("\n"):
                m = re.match(r"- `([a-z0-9-]+)`", line)
                if m:
                    tags.add(m.group(1))
    return tags


def load_source_ids(root):
    ids = set()
    for rel in walk(root, ".md"):
        if rel.startswith("meta/sources/") or rel == "meta/SOURCES.md":
            for line in read(os.path.join(root, rel)).split("\n"):
                m = re.match(r"\| (S\d{3,}) \|", line)
                if m:
                    ids.add(m.group(1))
    return ids
