#!/usr/bin/env python3
"""Write notes/audit-raw/TRIAGE.md: where every raw audit finding went in the register.

Usage: python3 -I scripts/triage.py [--check]

The raw passes (notes/audit-raw/V1A.md ... V2C.md) list findings by their own IDs. Each
one is mapped here to the register issue (docs/audit/) that acknowledges it, so nothing
found by any pass is silently dropped. Run after editing the mapping; the script fails if
a raw ID in the files is unmapped or a mapped register ID has no file.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "notes" / "audit-raw"

MAP = {
    # Vol I front matter and Chapters 1-10
    "V1A-01": "MAJ-06", "V1A-02": "MED-26", "V1A-03": "MAJ-03", "V1A-04": "MED-26",
    "V1A-05": "MED-19", "V1A-06": "MED-26", "V1A-07": "MED-26", "V1A-08": "MED-35",
    "V1A-09": "MED-21", "V1A-10": "MED-21", "V1A-11": "MED-03", "V1A-12": "MED-05",
    "V1A-13": "MED-01", "V1A-14": "MAJ-05", "V1A-15": "MED-36", "V1A-16": "MED-03",
    "V1A-17": "MED-11", "V1A-18": "MED-12", "V1A-19": "MAJ-06", "V1A-20": "MED-32",
    "V1A-21": "MED-18", "V1A-22": "MED-21", "V1A-23": "MED-02", "V1A-24": "MED-06",
    "V1A-25": "MAJ-07", "V1A-26": "MIN-13", "V1A-27": "MED-35", "V1A-28": "MIN-16",
    "V1A-29": "MED-35", "V1A-30": "MIN-15", "V1A-31": "MED-35", "V1A-32": "MED-29",
    "V1A-33": "MED-04", "V1A-34": "MED-11", "V1A-35": "MIN-18", "V1A-36": "MIN-18",
    "V1A-37": "MIN-18", "V1A-38": "MIN-01", "V1A-39": "MIN-07", "V1A-40": "MIN-04",
    "V1A-41": "MIN-07", "V1A-42": "MIN-11", "V1A-43": "MIN-14", "V1A-44": "MIN-04",
    "V1A-45": "MIN-15", "V1A-46": "MIN-14",
    # Vol I Chapters 11-20, Conclusion, Appendix A
    "V1B-01": "MED-13", "V1B-02": "MED-12", "V1B-03": "MED-01", "V1B-04": "MED-22",
    "V1B-05": "MED-12", "V1B-06": "MED-12", "V1B-07": "MAJ-05", "V1B-08": "MED-09",
    "V1B-09": "MED-11", "V1B-10": "MED-33", "V1B-11": "MED-33", "V1B-12": "MED-32",
    "V1B-13": "MAJ-06", "V1B-14": "MED-17", "V1B-15": "MED-16", "V1B-16": "MED-23",
    "V1B-17": "MAJ-01", "V1B-18": "MED-01", "V1B-19": "MED-23", "V1B-20": "MAJ-07",
    "V1B-21": "MIN-18", "V1B-22": "MED-35", "V1B-23": "MED-18", "V1B-24": "MED-35",
    "V1B-25": "MED-29", "V1B-26": "MED-35", "V1B-27": "MIN-04", "V1B-28": "MIN-03",
    "V1B-29": "MIN-01", "V1B-30": "MIN-02", "V1B-31": "MIN-07", "V1B-32": "MIN-14",
    "V1B-33": "MIN-15", "V1B-34": "MIN-11", "V1B-35": "MIN-05", "V1B-36": "MIN-06",
    "V1B-37": "MIN-19",
    # Vol II front matter and Chapters 21-26
    "V2A-01": "MED-07", "V2A-02": "MAJ-05", "V2A-03": "MAJ-05", "V2A-04": "MED-06",
    "V2A-05": "MAJ-06", "V2A-06": "MED-07", "V2A-07": "MED-34", "V2A-08": "MED-12",
    "V2A-09": "MED-10", "V2A-10": "MAJ-05", "V2A-11": "MED-34", "V2A-12": "MED-07",
    "V2A-13": "MED-29", "V2A-14": "MED-29", "V2A-15": "MED-29", "V2A-16": "MED-34",
    "V2A-17": "MED-28", "V2A-18": "MED-34", "V2A-19": "MED-29", "V2A-20": "MED-22",
    "V2A-21": "MED-27", "V2A-22": "MIN-15", "V2A-23": "MED-16", "V2A-24": "MAJ-02",
    "V2A-25": "MED-34", "V2A-26": "MED-24", "V2A-27": "MIN-05", "V2A-28": "MED-29",
    "V2A-29": "MIN-15", "V2A-30": "MIN-16", "V2A-31": "MIN-11", "V2A-32": "MIN-15",
    "V2A-33": "MIN-16", "V2A-34": "MIN-17", "V2A-35": "MIN-17", "V2A-36": "MIN-17",
    "V2A-37": "MIN-04", "V2A-38": "MIN-20", "V2A-39": "MED-04", "V2A-40": "MIN-18",
    "V2A-41": "MIN-18", "V2A-42": "MIN-18", "V2A-43": "MIN-12",
    # Vol II Chapters 27-30
    "V2B-01": "MED-10", "V2B-02": "MAJ-01", "V2B-03": "MED-12", "V2B-04": "MED-24",
    "V2B-05": "MED-24", "V2B-06": "MED-24", "V2B-07": "MED-11", "V2B-08": "MED-11",
    "V2B-09": "MED-23", "V2B-10": "MIN-04", "V2B-11": "MED-24", "V2B-12": "MED-09",
    "V2B-13": "MED-11", "V2B-14": "MED-26", "V2B-15": "MED-13", "V2B-16": "MAJ-03",
    "V2B-17": "MED-13", "V2B-18": "MED-26", "V2B-19": "MIN-13", "V2B-20": "MED-30",
    "V2B-21": "MAJ-03", "V2B-22": "MED-25", "V2B-23": "MED-25", "V2B-24": "MED-22",
    "V2B-25": "MED-33", "V2B-26": "MAJ-08", "V2B-27": "MAJ-08", "V2B-28": "MED-08",
    "V2B-29": "MAJ-08", "V2B-30": "MED-27", "V2B-31": "MAJ-08", "V2B-32": "MED-28",
    "V2B-33": "MAJ-06", "V2B-34": "MAJ-06", "V2B-35": "MED-17", "V2B-36": "MAJ-06",
    "V2B-37": "MED-31", "V2B-38": "MAJ-06", "V2B-39": "MED-34", "V2B-40": "MIN-18",
    "V2B-41": "MIN-18", "V2B-42": "MIN-14", "V2B-43": "MIN-03", "V2B-44": "MIN-11",
    "V2B-45": "MIN-15", "V2B-46": "MIN-05",
}
EXTRA = {
    # Vol II Chapters 31-34, References, Appendices
    "V2C-01": "MAJ-06", "V2C-02": "MED-37", "V2C-03": "MAJ-02", "V2C-04": "MAJ-06",
    "V2C-05": "MED-11", "V2C-06": "MED-11", "V2C-07": "MED-24", "V2C-08": "MAJ-06",
    "V2C-09": "MED-31", "V2C-10": "MAJ-04", "V2C-11": "MED-36", "V2C-12": "MED-30",
    "V2C-13": "MED-29", "V2C-14": "MED-12", "V2C-15": "MED-38", "V2C-16": "MED-38",
    "V2C-17": "MED-04", "V2C-18": "MIN-19", "V2C-19": "MED-34", "V2C-20": "MED-10",
    "V2C-21": "MED-29", "V2C-22": "MAJ-02", "V2C-23": "MAJ-02", "V2C-24": "MED-38",
    "V2C-25": "MED-16", "V2C-26": "MIN-08", "V2C-27": "MIN-08", "V2C-28": "MIN-17",
    "V2C-29": "MED-20", "V2C-30": "MIN-05", "V2C-31": "MIN-05", "V2C-32": "MIN-04",
    "V2C-33": "MIN-08", "V2C-34": "MIN-15", "V2C-35": "MED-29", "V2C-36": "MIN-16",
    "V2C-37": "MIN-14", "V2C-38": "MIN-11", "V2C-39": "MIN-14", "V2C-40": "MED-38",
    "V2C-41": "MIN-18", "V2C-42": "MIN-18", "V2C-43": "MIN-06", "V2C-44": "MIN-17",
    "V2C-45": "MED-26",
}


def main(argv):
    mapping = {**MAP, **EXTRA}
    rows, missing = [], []
    for path in sorted(RAW.glob("V*.md")):
        text = path.read_text(encoding="utf-8")
        for entry in re.split(r"\n(?=\s*- \*\*id\*\*)", text):
            ident = re.search(r"\*\*id\*\*: ?(\S+)", entry)
            if not ident:
                continue
            raw_id = ident.group(1)
            sev = re.search(r"\*\*severity\*\*: ?(\w+)", entry)
            prob = re.search(r"\*\*problem\*\*: ?(.+?)(?=\n\s*- \*\*fix|\Z)", entry, re.S)
            words = " ".join((prob.group(1) if prob else "").split()).split()
            gist = " ".join(words[:22]) + (" ..." if len(words) > 22 else "")
            target = mapping.get(raw_id)
            if not target:
                missing.append(raw_id)
                continue
            rows.append((raw_id, sev.group(1) if sev else "", target, gist.replace("|", "/")))
    files = {p.name.split("-")[0] + "-" + p.name.split("-")[1]: p.name
             for p in (ROOT / "docs" / "audit").glob("M*-*.md")}
    absent = sorted({t for _, _, t, _ in rows if t not in files})
    if missing or absent:
        print("unmapped raw IDs:", missing)
        print("register IDs without a file:", absent)
        return 1
    out = ["# Triage of the raw audit findings", "",
           "Every finding from the section-by-section passes in this directory is listed with the",
           "register issue in `docs/audit/` that acknowledges it. Several raw findings usually map to",
           "one register issue; severities in the register are the reviewer's, after checking each",
           "finding against the text, and may differ from the raw pass's proposal. Generated by",
           "`scripts/triage.py`.", "",
           "| Raw ID | Raw severity | Register | Raw finding (opening words) |", "|---|---|---|---|"]
    for raw_id, sev, target, gist in rows:
        out.append(f"| {raw_id} | {sev} | [{target}](../../docs/audit/{files[target]}) | {gist} |")
    text = "\n".join(out) + "\n"
    target = RAW / "TRIAGE.md"
    if "--check" in argv:
        if not target.exists() or target.read_text(encoding="utf-8") != text:
            print("notes/audit-raw/TRIAGE.md is stale; run scripts/triage.py")
            return 1
        print(f"triage OK: {len(rows)} raw findings, every one mapped to a register issue")
        return 0
    target.write_text(text, encoding="utf-8")
    print(f"wrote notes/audit-raw/TRIAGE.md ({len(rows)} raw findings)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
