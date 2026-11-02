"""Style lint for the three Cs: sentence length, undefined acronyms, banned syntax.

Usage: imported by validate_kb.py. Functions return lists of message strings.
"""
import re

ACRO_RE = re.compile(r"\b[A-Z][A-Z0-9]{1,6}s?\b")
COMMON = {"ANY", "ANYREF", "ANYVAL", "AS", "BASIC", "BOOLEAN", "BY", "COPY", "CORE", "DECIMAL", "DEFINE", "DELETE", "DOMAIN", "DOUBLE", "EXCLUDE", "GET", "GLOBAL", "GROUP", "IN", "INCLUDE", "INFO", "INNER", "INSERT", "INT64", "INTO", "JOIN", "NONE", "NUMERIC", "PICK", "REORG", "RETURN", "SCALAR", "STRING", "TABLE", "VACUUM", "VARIANT", "WHERE", "XOR", "DWORD", "CRLF", "TXT", "YYYY", "CTAS", "DDL", "OS", "PC", "NA", "OK", "ID", "IDs", "AI", "US", "UK", "AND", "OR", "NOT", "URL", "URLs",
          "BI", "KB", "CSV", "JSON", "XML", "HTML", "UTF", "YAML", "SQL", "API", "APIs", "PDF", "TBD"}


def prose_lines(body):
    out, fence = [], False
    for line in body.split("\n"):
        if line.startswith("```"):
            fence = not fence
            continue
        if fence or line.startswith("|") or line.startswith("#") or not line.strip():
            continue
        out.append(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", line))
    return out


def avg_sentence_len(body):
    text = " ".join(l if l.rstrip()[-1:] in ".!?:" else l.rstrip() + "." for l in prose_lines(body))
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"`[^`]*`", "x", text)
    parts = [p for p in re.split(r"(?<=[.!?])\s+", text) if p.strip()]
    if not parts:
        return 0.0
    return sum(len(p.split()) for p in parts) / len(parts)


def banned_syntax(body):
    msgs = []
    clean = re.sub(r"```.*?```", "", body, flags=re.S)
    clean = re.sub(r"`[^`]*`", "", clean)
    if "[[" in clean:
        msgs.append("wikilink syntax [[ ]] found")
    if re.search(r"!\[", clean):
        msgs.append("image syntax found")
    if re.search(r"</?[a-zA-Z][a-zA-Z0-9]*[ />]", clean):
        msgs.append("HTML tag found")
    return msgs


def table_problems(body):
    msgs, rows, cols = [], 0, 0
    for line in body.split("\n") + [""]:
        if line.startswith("|"):
            rows += 1
            cols = max(cols, line.count("|") - 1)
        else:
            if rows and (rows - 2 > 25 or cols > 8):
                msgs.append(f"table too large ({rows - 2} rows, {cols} cols)")
            rows = cols = 0
    return msgs


def undefined_acronyms(body, glossary):
    """Acronyms with no 'Term (ACR)' or 'ACR (Term)' definition and not in glossary."""
    clean = re.sub(r"```.*?```", "", body, flags=re.S)
    clean = re.sub(r"`[^`]*`", "", clean)
    clean = re.sub(r"\]\([^)]*\)", "]", clean)
    found = {}
    for m in ACRO_RE.finditer(clean):
        w = m.group(0)
        key = w[:-1] if w.endswith("s") and len(w) > 2 else w
        found.setdefault(key, m.start())
    bad = []
    for acr, pos in found.items():
        if acr in COMMON or acr in glossary or re.fullmatch(r"[A-Z]{1,2}\d+", acr):
            continue
        defined = re.search(r"\(" + re.escape(acr) + r"\)|\b" + re.escape(acr) + r" \(", clean)
        if not defined or defined.start() > pos + len(acr) + 2:
            bad.append(acr)
    return sorted(bad)
