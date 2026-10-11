---
id: MIN-17
title: Defects in pseudocode, parameters and the reproducibility rule
severity: minor
area: code
volumes: II
sections: Vol II Ch. 23, §24.B.2, §24.D.2, Ch. 26, §27.1, §31.2, §32.3, §33.C.1
review: §5.4
status: open
github_issue: 63
---

# MIN-17 · Defects in pseudocode, parameters and the reproducibility rule

## Claims under review

- **Vol II §31.2, p. 79:** "Criterion: a repeated run with the same seed and action sequence
  produces a comparable trajectory and identical causally significant records. Until this
  holds, results from later stages are invalid.";
  **Vol II §32.3, p. 86:** "Reproducibility is confirmed by a series of repeated runs. If the
  cause is not established, the system remains at Stage 0 regardless of model complexity."
- **Vol II §33.C.1, p. 110:** "# Equal priors, 12 units for a wrong targeted repair, 4 for
  deferral." and "Optimal finite plan for supplied likelihoods; cost includes delay."
- **Vol II Ch. 26, p. 39:** "For v0, an environment with a finite, small state and action space
  is recommended so that causal dependencies manifest within dozens or hundreds of steps. It is
  sufficient for the state to have a canonical identifier—for example position plus a set of
  flags/switches—and for the action set to be explicit and bounded. An example of a minimal
  environment is a 5×5 grid with 5–10 types of objects/flags and no more than 8–12 actions."
- **Vol II §24.B.2, p. 24:** "Reference procedure for accepting a natural-language proposal:";
  **Vol II Ch. 23, p. 18:** "An indicative ResourceProfile is introduced for the basic
  reproducible v0 series:"

## Finding

Volume II's pseudocode, resource table, environment sizing, diagnostic example and Stage 0
rule, quoted above, are not self-consistent as printed. Some names are never set or used, the
recommended grid looks too large for its step budget, a stated loss never enters the
computation, and the exact-repeat rule omits its own qualification.

## Evidence

- **Vol II §24.B.2, p. 24, and §24.D.2, p. 30:** `interpret_proposal` ends
  "return candidates_with_open_questions", a name never assigned; `resolve_fragment` loops on
  "while not required_distinction_found:", which no statement sets, and has no return on the
  success path.
- **Vol II Ch. 23, p. 18:** four of seven ResourceProfile limits, such as
  "analysis_passes_max", appear nowhere else, and W is defined only in §27.1 (p. 45).
- **Vol II Ch. 26, p. 39:** the grid above is, with binary flags, up to 25,600 states and
  307,200 state-action pairs (25 cells, 10 flags, 12 actions), more than a tabular model can
  visit within the step budget the passage gives.
- **Vol II §33.C.1, p. 110:** the loss named in the comment is never used (`terminal` returns
  deferral for any two or more hypotheses), so the claimed optimal plan holds only for this
  matrix and equal priors. In the restored listing (`repro/diagnostic_cycle.py`), a hidden
  cause mimicking D draws REPAIR_D after one probe.
- **Already in the text (Vol II Ch. 23, p. 18):** "The exact-match rule in §32.3 applies to a
  declared deterministic or log-reproducible mode." This qualification is stated here but not
  in §31.2 or §32.3, which is why Stage 0 as printed conflicts with Chapter 23.

## Why it matters

These are the parts most likely to be implemented as written, and Stage 0 gates every later
stage; as stated, it conflicts with Chapter 23.

## Ideas & possible recommendations

- **Make the pseudocode run, or mark it schematic.** The listings in §24.B.2 and §24.D.2 could
  be made executable, or be labelled schematic so that readers do not take them as complete.
- **Use or drop each parameter.** Each ResourceProfile limit and the §33.C.1 loss matrix could
  either enter a computation or be removed.
- **Size the first environment to its step budget.** The Chapter 26 grid, its number of flags
  and actions, or the step budget could be adjusted until a tabular model can visit the state
  space.
- **Give Stage 0 the Chapter 23 qualification.** §§31.2 and 32.3 could carry the limit that
  exact repetition applies to a declared deterministic or log-reproducible mode; another option
  is to state it once and have the other sections refer to it.

## Resolved when

- [ ] The pseudocode runs or is marked schematic, every parameter is used, and §§31.2 and 32.3
      state or point to the Chapter 23 qualification.

## Related

- Review: [§5.4](../../REVIEW.md#54-what-the-executable-examples-show)
- Issues: MAJ-03, MIN-08
