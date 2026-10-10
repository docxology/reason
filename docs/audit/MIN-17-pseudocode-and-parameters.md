---
id: MIN-17
title: Defects in pseudocode, parameters and the reproducibility rule
severity: minor
area: code
volumes: II
sections: Vol II Ch. 23, §24.B.2, §24.D.2, Ch. 26, §27.1, §31.2, §32.3, §33.C.1
review: §5.4
status: open
---

# MIN-17 · Defects in pseudocode, parameters and the reproducibility rule

**Finding.** Volume II's pseudocode, resource table, environment sizing, diagnostic example and
Stage 0 rule are not self-consistent as printed. Some names are never set or used, the recommended
grid looks too large for its step budget, a stated loss never enters the computation, and the
exact-repeat rule omits its own qualification.

## Evidence

- **Vol II §24.B.2, p. 24, and §24.D.2, p. 30:** `interpret_proposal` ends "return
  candidates_with_open_questions", a name never assigned; `resolve_fragment` loops on "while not
  required_distinction_found:", which no statement sets, and has no return on the success path.
- **Vol II Ch. 23, p. 18:** four of seven ResourceProfile limits, such as "analysis_passes_max",
  appear nowhere else, and W is defined only in §27.1 (p. 45).
- **Vol II Ch. 26, p. 39:** "5×5 grid with 5–10 types of objects/flags and no more than 8–12
  actions" is, with binary flags, up to 25,600 states and 307,200 state-action pairs, more than a
  tabular model can visit in "dozens or hundreds of steps".
- **Vol II §33.C.1, p. 110:** "# Equal priors, 12 units for a wrong targeted repair, 4 for
  deferral." names a loss the code never uses (`terminal` returns deferral for any two or more
  hypotheses), so "Optimal finite plan for supplied likelihoods" holds only for this matrix and
  equal priors. In the restored listing (`repro/diagnostic_cycle.py`), a hidden cause mimicking D
  draws REPAIR_D after one probe.
- **Vol II §31.2, p. 79, §32.3, p. 86, and Ch. 23, p. 18:** Stage 0 requires "identical causally
  significant records" from a repeated run, and "the system remains at Stage 0 regardless of model
  complexity". Chapter 23 limits it: "The exact-match rule in §32.3 applies to a declared
  deterministic or log-reproducible mode."

## Why it matters

These are the parts most likely to be implemented as written, and Stage 0 gates every later stage;
as stated, it conflicts with Chapter 23.

## Recommendation

Make the pseudocode executable or schematic, use or drop each parameter, size the first
environment to its step budget, and give Stage 0 the Chapter 23 qualification.

## Resolved when

- [ ] The pseudocode runs or is marked schematic, every parameter is used, and §§31.2 and 32.3
      carry the Chapter 23 qualification.

## Related

- Review: [§5.4](../../REVIEW.md#54-what-the-executable-examples-show)
- Issues: MAJ-03, MIN-08
