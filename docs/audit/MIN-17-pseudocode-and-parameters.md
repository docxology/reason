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
rule, quoted above, leave loose ends as printed. Some names are never set or used; the
recommended grid may be too large for a tabular model, and the passage states no training
budget to check it against; a stated loss enters only as a hard-coded result; and §§31.2 and
32.3 do not repeat the qualification that Chapter 23 gives for the exact-repeat rule.

## Evidence

- **Vol II §24.B.2, p. 24, and §24.D.2, p. 30:** `interpret_proposal` ends
  "return candidates_with_open_questions", a name never assigned; `resolve_fragment` loops on
  "while not required_distinction_found:" and tests `resolution_budget_exhausted`; neither is
  assigned by an explicit statement (only the final call `update_distinction_and_budget()`
  could change them, and its effect is not specified), and the function has no return on the
  success path.
- **Vol II Ch. 23, p. 18:** five of seven ResourceProfile limits (`active_hypotheses_max`,
  `active_foundation_gaps_max`, `architecture_candidates`, `meta_depth_max`,
  `analysis_passes_max`) appear nowhere else, and W is defined only in §27.1 (p. 45).
- **Vol II Ch. 26, p. 39:** with ten independent binary flags, the grid above has up to 25,600
  states and 307,200 state-action pairs (25 cells, 10 flags, 12 actions). The passage says
  only that causal dependencies should manifest "within dozens or hundreds of steps" and gives
  no training budget, so whether a tabular model can cover this space is undetermined.
- **Already in the text (Vol II Ch. 22, p. 15, and §24.B.2, p. 23):** "v0 permits a tabular
  record of transitions" and "For a simple test bench, symbolic or tabular Intelligence without
  an LLM is permitted." The text thus allows a tabular model for v0; what is missing is a
  budget.
- **Vol II §33.C.1, pp. 109–110:** the 12-unit loss appears only in a comment and in the prose,
  which says "The loss of an erroneous targeted correction is 12, and the loss of delay is 4".
  With equal priors, guessing among two or three alternatives costs 6 or 8 against 4 for
  deferral, so deferral for two or more hypotheses is what these losses give; but `terminal`
  hard-codes that result and would not follow a change of loss or priors, which the text
  treats as assumptions of the model or settings of the designer. In the restored listing
  (`repro/diagnostic_cycle.py`), a hidden cause mimicking D, which lies outside the predefined
  table of alternatives that the text assumes, draws REPAIR_D after one probe, and the listing
  records MODEL_MISMATCH only after that repair fails.
- **Already in the text (Vol II §33.C.1, pp. 109, 111):** the listing's docstring says "no LLM
  or open-world claims", and the text schedules the mimicking case: "The next mandatory
  version of the diagnostic test closes a harder open-world case: hidden cause X must produce
  the same familiar answers as one of the known causes, for example D, on all standard
  probes." That case is a limitation the author states, not one the listing hides.
- **Already in the text (Vol II Ch. 23, p. 18):** "The exact-match rule in §32.3 applies to a
  declared deterministic or log-reproducible mode." This qualification is stated here but not
  in §31.2 or §32.3, so the scope of Stage 0 has to be read from Chapter 23: §31.2 is limited
  to the test bench, §32.3 lists unfixed randomness and unlogged external signals as causes,
  and neither says how "the system remains at Stage 0" (§32.3, p. 86) applies to the upper
  loop with an external probabilistic model.
- **Already in the text (Vol II Ch. 23, p. 18):** the ResourceProfile values are presented as
  "initial budgets for a laboratory series", so some limits may simply not be exercised yet.

## Why it matters

These are the parts most likely to be implemented as written, and Stage 0 gates every later
stage; as stated, its scope is given only in Chapter 23.

## Ideas & possible recommendations

- **Make the pseudocode run, or mark it schematic.** The listings in §24.B.2 and §24.D.2 could
  be made executable, or be labelled schematic so that readers do not take them as complete.
- **Use or drop each parameter.** Each ResourceProfile limit could either enter a computation
  or be removed, and the §33.C.1 loss matrix could be computed instead of hard-coded in
  `terminal`.
- **State a training budget for the first environment.** The Chapter 26 grid, its number of
  flags and actions, or a stated training budget could be adjusted until a tabular model can
  visit the state space.
- **Give Stage 0 the Chapter 23 qualification.** §§31.2 and 32.3 could carry the limit that
  exact repetition applies to a declared deterministic or log-reproducible mode; another option
  is to state it once and have the other sections refer to it.

## Resolved when

- [ ] The pseudocode runs or is marked schematic, every parameter is used, and §§31.2 and 32.3
      state or point to the Chapter 23 qualification.

## Related

- Review: [§5.4](../../REVIEW.md#54-what-the-executable-examples-show)
- Issues: MAJ-03, MIN-08
