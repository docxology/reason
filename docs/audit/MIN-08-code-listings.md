---
id: MIN-08
title: The printed code listings cannot be run as printed, and their checks are weaker than described
severity: minor
area: code
volumes: II
sections: Vol II §33.B, §33.C, §33.C.1
review: §5.4, Appendix A
status: open
---

# MIN-08 · The printed code listings cannot be run as printed, and their checks are weaker than described

**Finding.** Volume II prints two Python listings: the lower-loop demonstration (§33.B) and the
executable diagnostic cycle (§33.C.1). On the printed pages later methods start at column 0
while their bodies stay indented, and in extracted text the offset shifts at page breaks, so
neither runs without re-indenting. Restored with nothing else changed (`repro/`, checked
line by line against the PDF text by `scripts/check_listings.py`), both run and every assertion
passes. Three things are weaker than the prose suggests. The §33.B headline gain obeys an exact
identity: the frozen control always predicts state 0 and the adaptive model is right on every
visited transition, so gain equals the share of held-out steps not leading to state 0 minus the
share on unvisited pairs; the reported interval (0.959–0.972) measures exploration coverage.
The reproducibility, checkpoint and reset results are literal `True` values written after
`assert` statements, and the "checkpoint" is an in-memory copy. And both scripts print their
pass banner unconditionally after `assert`s, which Python removes under `-O`.

## Evidence

- **Vol II §33.B, p. 105:** "The measurements are error, multiclass Brier score, transition
  coverage, reproducibility, persistence after a snapshot and the effect of resetting the
  model." The report writes `"replay_equal": True, "checkpoint_equal": True` after asserts, and
  `checkpoint = copy.deepcopy(adaptive)`.
- **Vol II §33.C.1, p. 111:** "Running the extracted block with standard Python executes twelve
  control episodes and prints JSON"; the code ends `print(json.dumps({'checks': 'PASS', ...}))`
  after a run of `assert` statements.
- **Vol II §33.C, pp. 107–108:** in the pseudocode, `effect = classify_external_effect(step)` and
  the following `if` sit at an ambiguous nesting level.
- Restored files and checks: `repro/v0_lower_loop.py`, `repro/diagnostic_cycle.py`,
  `scripts/check_listings.py`; adaptive Brier score about 0.65 despite near-zero error, because a
  pseudo-count of 1 over 32 classes leaves the observed transition about 0.18 probability.

## Why it matters

The listings are the only executable artefacts of the programme and the natural seed of the
first experimental harness. Code that cannot be run as printed will not be run, and checks that
cannot fail do not check.

## Recommendation

Publish both listings as files in a public repository with tests, refer to them from the PDF,
compute pass flags from explicit comparisons and exit non-zero on failure, serialize the
checkpoint and restore it in a fresh process, and report the coverage identity and the
pseudo-count effect in the text.

## Resolved when

- [ ] The listings are available as runnable files at a stable link, and their reported checks
      are computed rather than written as constants.

## Related

- Review: [§5.4](../../REVIEW.md#54-what-the-executable-examples-show)
- Issues: MAJ-04 (retention is caching), MIN-17 (pseudocode defects)
