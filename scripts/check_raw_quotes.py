#!/usr/bin/env python3
"""Check every quotation in the raw audit-pass files against the volume texts.

Usage: python3 -I scripts/check_raw_quotes.py notes/audit-raw/V1A.md [...]

Entries are markdown lists whose `**quote**` field holds one or more quoted strings (straight
or curly double quotes, or backticks) separated by " | " or ";". A quote counts as found if,
after normalization (whitespace, typographic punctuation, quote nesting, bullets, hyphenated line
breaks), every part of it occurs in one volume; "[...]" and "..." mark gaps between parts.
Exits 1 if any quote is not found, so `make verify` fails on a miss.
"""
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("locate", ROOT / "scripts" / "locate.py")
locate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(locate)

def canon(text):
    """Fold differences that are layout, not wording: quote nesting, bullets, space before punctuation."""
    text = text.replace('"', "'").replace("\u2022", " ")
    text = re.sub(r"\s+", " ", text)
    return re.sub(r" ([,;:.)\]])", r"\1", text)


TEXTS = {}
for vol, name in (("I", "foundations-8.0"), ("II", "engineering-3.5")):
    raw = (ROOT / "text" / f"{name}.txt").read_text(encoding="utf-8")
    flat, _ = locate.normalize_with_offsets(raw)
    # Also a version with page furniture and hyphenated line breaks removed.
    flat2 = re.sub(r"(FOUNDATIONS OF REASON · 8\.0|ENGINEERING OF REASON · 3\.5)", " ", raw)
    flat2, _ = locate.normalize_with_offsets(flat2)
    flat2 = re.sub(r" \d{1,3} (?=[a-z])", " ", flat2)
    TEXTS[vol] = tuple(canon(v) for v in (flat, flat2, flat2.replace("- ", "-")))


def found(fragment):
    needle = locate.normalize(fragment).strip(" .,;:")
    needle = needle.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")
    needle = canon(needle)
    parts = [p.strip() for p in re.split(r"\s*(?:\[\.\.\.\]|\.\.\.|…)\s*", needle) if p.strip()]
    hits = set()
    for vol, variants in TEXTS.items():
        if all(any(p in v or p.lower() in v.lower() for v in variants) for p in parts):
            hits.add(vol)
    return hits


def main(paths):
    total = bad = 0
    for path in paths:
        text = Path(path).read_text(encoding="utf-8")
        for entry in re.split(r"\n(?=\s*- \*\*id\*\*)", text):
            ident = re.search(r"\*\*id\*\*: ?(\S+)", entry)
            quote = re.search(r"\*\*quote\*\*: ?(.+?)(?=\n\s*- \*\*problem)", entry, re.S)
            if not ident or not quote:
                continue
            body = quote.group(1)
            fragments = re.findall(r'"((?:[^"\\]|\\.){6,}?)"(?=\s*(?:\||$|\(|;|,|\n))', body, re.S)
            fragments += re.findall(r'\u201c([^\u201d]{6,}?)\u201d', body, re.S)
            fragments += [f for f in re.findall(r'`([^`]{12,}?)`', body, re.S) if " " in f]
            for fragment in fragments:
                total += 1
                if not found(fragment):
                    bad += 1
                    print(f"NOT FOUND {ident.group(1)}: {' '.join(fragment.split())[:120]}")
    print(f"\n{total - bad}/{total} quoted fragments found verbatim (normalized)")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
