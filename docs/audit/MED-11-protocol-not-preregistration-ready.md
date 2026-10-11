---
id: MED-11
title: The first series has the right slots but no preregistered instance
severity: medium
area: testability
volumes: I, II
sections: Vol I A.2.1, A.3, A.4, Abstract, guide; Vol II Ch. 27, §27.B, §31.1, §31.A
review: §5.2(a), §10.2
status: open
github_issue: 19
---

# MED-11 · The first series has the right slots but no preregistered instance

## Claims under review

- **Vol II §27.B, p. 50:** "The size of the confirmatory series is determined from a separate
  pilot and a preselected effect; the pilot is not included in final confirmation."
- **Vol II §31.A, pp. 83–84:** "Before the control series, a ReadinessProfile is created. It is
  not a universal scale of Reason but fixes the conditions of a particular experiment: [...] The
  profile is published before results are examined."
- **Vol II §27.B, p. 49:** "Comparisons include routine Intelligence with ordinary memory, tools
  and self-verification; the same mechanism with the proposed relations; and declared
  replacements or ablations." **Vol I A.4, p. 99:** "an agent stack with ordinary planning,
  versioned memory of beliefs and provenance, self-checking, mismatch response,
  value-of-information assessment, and a log of failed attempts available to subsequent tasks."
- **Vol I A.4, p. 100:** "All variants receive the same observations, tools, and comparable
  total resources: number of model calls, tokens/inference-time compute, external sources, bench
  time, and hidden preparation are counted together." **Vol I A.2.1, p. 95:** "Run a
  preregistered series under equal total resources".

## Finding

The evaluation rules are of preregistration quality, and the profile has the right slots:
component versions, candidate boundary, family generator, data splits, primary metric and
minimum practically significant effect are to be fixed before launch; sample size comes from a
separate pilot and a preselected effect; the unit of observation is a world family;
multiple-comparison and stopping rules are fixed in advance; resources include model calls and
tokens. Strong nulls are named as classes. No instance exists: no model, frozen baseline,
generator, number of world families or effect size is named, and the `ReadinessProfile` that
gates every stage has twenty parameters and no values. Several gaps would matter even once
values exist. The sample-size rule depends on a pilot that compared nothing. Volume II's control
arm is weaker than Volume I's strong null (no versioned belief memory with provenance, no
value-of-information assessment, no failure log). The readiness profile has no comparator or
effect-size field, so readiness could be declared without beating any baseline. Resource parity
is "comparable" in most places and "equal" in a few, with no tolerance. The tester holds the
hidden references, but nothing requires independence from the author, who took part in the only
pilot.

## Evidence

- **Already in the text (Vol II §27.B, p. 50):** "Before launch, component versions, candidate
  boundary, family generator, train / selection / held_out_test split, primary metric and
  minimum practically significant effect are retained."
- **Vol II §27.B, p. 49:** the only pilot was "conducted in a dialogue loop with the author's
  participation", and "in the reviewed materials there is no completed external admission of
  this package and no comparative C0/C1/C2 run".
- **Vol II Ch. 27, p. 44:** "Hidden references, final evaluation and criteria for selecting
  control cases remain with the tester."

## Why it matters

A procedure without parameters cannot be checked for power or fairness and leaves room for
choices made after seeing data. A readiness gate with no comparator can pass a system that adds
nothing.

## Ideas & possible recommendations

- **Publish a preregistration.** A preregistration could be published, for example on OSF,
  naming the model and version, the generator, the outcomes, the minimum effect with a power
  calculation, the analysis model, the stopping rule and the abandonment condition (MED-12).
- **Specify the arms and the budgets.** The baseline stack (Vol I's strong null, plus an
  epistemic-layer-only arm) and the budgets, with a numeric tolerance, could be written into the
  same document.
- **Extend the ReadinessProfile.** Comparator, margin and equal-compute fields could be added, so
  that readiness requires beating a declared null.
- **Make the tester independent.** An independent tester, or an audit of the hidden references,
  would remove the dependence on the author, who took part in the pilot.

## Resolved when

- [ ] A public preregistration (model and version, baseline arms, generator, budgets with a
      numeric tolerance, outcomes, minimum effect with a power calculation, analysis model,
      stopping rule, abandonment condition) exists before confirmatory data collection.
- [ ] The ReadinessProfile has values and requires a margin over a declared null.

## Related

- Review: [§5.2(a)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test),
  [§10](../../REVIEW.md#10-ideas--possible-recommendations)
- Issues: MAJ-01, MED-12, MED-09, MED-10, MED-24 (metric definitions)
