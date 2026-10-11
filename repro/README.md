# Restored code listings

Volume II prints two Python listings. In text taken from the PDF their indentation is
inconsistent (the offset shifts at page breaks and some method definitions fall to column 0),
so they cannot be run without re-indenting. The files here restore the indentation and change
nothing else; a provenance comment at the top of each file is the only addition.
`scripts/check_listings.py` compares each file with the printed listing, line by line up to
whitespace, and is part of `make verify`.

| File | Source | What it shows | Result |
|---|---|---|---|
| `v0_lower_loop.py` | Vol II §33.B (pp. 105–106) | A count-based transition model learns 12 random deterministic worlds (32 states × 6 actions) and beats a frozen control; replay, checkpoint and reset are asserted | mean adaptation gain 0.966, 95% world-bootstrap interval 0.959–0.972; all assertions pass |
| `diagnostic_cycle.py` | Vol II §33.C.1 (pp. 109–111) | Exact memoized decision-tree search over three causes (D/A/S) and three probes, with 12 control episodes | all 12 checks pass; receipt-first expected cost 7/3 versus 8/3 for measuring first |
| `dup_paragraphs.py` | written for this review | Sliding-window `difflib` check for near-duplicate paragraphs | Vol I: 11 pairs with ratio > 0.80; Vol II: none |

What the results do and do not show is discussed in `REVIEW.md` §5.4 and in
`docs/audit/MIN-08-code-listings.md`. In short: the §33.B gain is fixed by construction (the
frozen control always predicts state 0 and the adaptive model is exact on every visited
transition), so the gain and its interval are set by held-out coverage and by the share of
transitions into state 0; and the retention in §33.C.1 is a
plan cache, so a warm memory changes the number of evaluated states but no decision.

Run everything with `make verify` from the repository root. That target checks the listings
against the PDF, writes all outputs under `$TMPDIR/reason-verify/`, and then runs
`scripts/check_numbers.py`, which fails if any number quoted in `REVIEW.md` no longer matches
what these scripts produce.

Run by hand:

```sh
(cd "$TMPDIR" && python3 -I "$OLDPWD/repro/v0_lower_loop.py")   # writes $TMPDIR/v0_results/
python3 -I repro/diagnostic_cycle.py                             # prints the 12 episodes as JSON
python3 -I repro/dup_paragraphs.py text/foundations-8.0.txt text/engineering-3.5.txt
```

As printed, `v0_lower_loop.py` writes `report.json` and a 27 MB `trace.jsonl` to
`./v0_results` in the current directory, so run it from a scratch directory.

Neither listing bears on the central hypothesis of the volumes, and the author says so. They
are the seed of the harness that the experiment in `REVIEW.md` §10 would need.
