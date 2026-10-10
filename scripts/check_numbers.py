#!/usr/bin/env python3
"""Fail if a computed number quoted in REVIEW.md or repro/README.md disagrees with its source.

Usage: python3 -I scripts/check_numbers.py OUTDIR

OUTDIR holds the outputs that `make verify` produces: v0_results/report.json,
diagnostic_cycle.json and dup_paragraphs.txt. Expected costs of the first probe are
recomputed here from the restored §33.C.1 listing, and page counts from the form feeds in
text/. Every number is rendered the way the documents print it and must appear verbatim.
"""
import importlib.util
import json
import re
import statistics
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = [ROOT / "REVIEW.md", ROOT / "repro" / "README.md"]


def load_listing():
    spec = importlib.util.spec_from_file_location("diagnostic_cycle", ROOT / "repro" / "diagnostic_cycle.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def first_probe_costs(dc, budget=3):
    """Expected cost of opening with each informative probe, then continuing optimally."""
    costs = {}
    for probe in dc.PROBES:
        groups = dc.partition(dc.CAUSES, probe)
        if len(groups) == 1 or probe.cost > budget:
            continue
        rest = tuple(q for q in dc.PROBES if q != probe)
        memory, counters = dc.Memory(), {"method_hits": 0, "evaluated_states": 0}
        total = Fraction(probe.cost)
        for group in groups:
            loss = dc.plan(group, rest, budget - probe.cost, memory, counters)[0]
            total += Fraction(len(group), len(dc.CAUSES)) * Fraction(loss).limit_denominator(100)
        costs[probe.name] = total
    return costs


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    out = Path(argv[0])
    report = json.loads((out / "v0_results" / "report.json").read_text())
    worlds = report["worlds"]
    diagnostic = json.loads((out / "diagnostic_cycle.json").read_text())
    dups = (out / "dup_paragraphs.txt").read_text()
    dc = load_listing()
    costs = first_probe_costs(dc)
    lo, hi = report["world_bootstrap_95_interval"]
    pages = {name: (ROOT / "text" / f"{name}.txt").read_text(encoding="utf-8").count("\f")
             for name in ("foundations-8.0", "engineering-3.5")}
    dup_counts = [int(n) for n in re.findall(r"near-duplicate pairs \(ratio>0\.80, window 3\): (\d+)", dups)]
    words = {11: "eleven"}

    expectations = [
        ("mean adaptation gain", f"{report['mean_gain']:.3f}", DOCS),
        ("95% world-bootstrap interval", f"{lo:.3f}–{hi:.3f}", DOCS),
        ("mean adaptive held-out error", f"{statistics.mean(w['adaptive_error'] for w in worlds):.2f}", DOCS[:1]),
        ("mean frozen held-out error", f"{statistics.mean(w['frozen_error'] for w in worlds):.2f}", DOCS[:1]),
        ("lowest held-out coverage", f"{min(w['test_transition_coverage'] for w in worlds):.3f}", DOCS[:1]),
        ("diagnostic episodes", f"{len(diagnostic['episodes'])} control episodes", DOCS[:1]),
        ("receipt-first expected cost", f"{costs['receipt'].numerator}/{costs['receipt'].denominator}", DOCS),
        ("motion-first expected cost", f"{costs['independent_motion'].numerator}/{costs['independent_motion'].denominator}", DOCS),
        ("page counts (Vol I and Vol II)", f"{pages['foundations-8.0']} and {pages['engineering-3.5']} pages", DOCS[:1]),
        ("Vol I near-duplicate pairs", words.get(dup_counts[0], str(dup_counts[0])), DOCS[:1]),
    ]
    checks = [
        ("v0 assertions (replay, checkpoint, reset)",
         all(w["replay_equal"] and w["checkpoint_equal"] and w["reset_equals_control"] for w in worlds)),
        ("diagnostic checks", diagnostic.get("checks") == "PASS"),
        ("Vol II has no near-duplicate pairs", dup_counts[1:] == [0]),
    ]

    failed = 0
    texts = {path: path.read_text(encoding="utf-8") for path in DOCS}
    for label, rendered, paths in expectations:
        missing = [p.relative_to(ROOT).as_posix() for p in paths if rendered not in texts[p]]
        status = "ok " if not missing else "MISSING in " + ", ".join(missing)
        failed += bool(missing)
        print(f"{status:<28} {label}: {rendered}")
    for label, passed in checks:
        failed += not passed
        print(f"{'ok ' if passed else 'FAILED':<28} {label}")
    print(f"\n{len(expectations) + len(checks) - failed}/{len(expectations) + len(checks)} checks pass")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
