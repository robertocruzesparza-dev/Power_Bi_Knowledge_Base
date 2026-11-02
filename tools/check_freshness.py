"""List volatile KB files by age of last_verified (oldest first).

Usage: python tools/check_freshness.py [KB_ROOT] [--days N] [--today YYYY-MM-DD]
Prints files with volatile: true whose last_verified is older than N days (default 30).
Exit code 0 always; this is a report, not a gate.
"""
import datetime
import os
import sys

import kbcommon as kc


def main(argv):
    pos = [a for a in argv if not a.startswith("--") and not a[:1].isdigit() and not a.startswith("20")]
    root = os.path.abspath(pos[0] if pos else os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
    days = int(argv[argv.index("--days") + 1]) if "--days" in argv else 30
    today = (datetime.date.fromisoformat(argv[argv.index("--today") + 1])
             if "--today" in argv else datetime.date.today())
    rows = []
    for rel in kc.walk(root, ".md"):
        fm, _ = kc.parse_front(kc.read(os.path.join(root, rel)))
        if fm and fm.get("volatile") == "true":
            try:
                age = (today - datetime.date.fromisoformat(fm.get("last_verified", ""))).days
            except ValueError:
                age = 9999
            rows.append((age, rel))
    for age, rel in sorted(rows, reverse=True):
        if age >= days:
            print(f"{age:5d} days  {rel}")
    print(f"volatile={len(rows)} stale(>={days}d)={sum(1 for a, _ in rows if a >= days)}")


if __name__ == "__main__":
    main(sys.argv[1:])
