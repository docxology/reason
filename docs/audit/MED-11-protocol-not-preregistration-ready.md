---
id: MED-11
title: The first series has the right slots but no preregistered instance
severity: medium
area: testability
volumes: I, II
sections: Vol I A.3, A.4, Abstract, guide; Vol II Ch. 27, §27.B, §31.1, §31.A
review: §5.2(a), §10.2
status: open
github_issue: 19
---

# MED-11 · The first series has the right slots but no preregistered instance

**Finding.** The evaluation rules are of preregistration quality, and the profile has the
right slots: component versions, candidate boundary, family generator, data splits, primary
metric and minimum practically significant effect are to be fixed before launch; sample size
comes from a separate pilot and a preselected effect; the unit of observation is a world
family; multiple-comparison and stopping rules are fixed in advance; resources include model
calls and tokens. Strong nulls are named as classes. No instance exists: no model, frozen
baseline, generator, number of world families or effect size is named, and the
`ReadinessProfile` that gates every stage has twenty parameters and no values. Several gaps
would matter even once values exist. The sample-size rule depends on a pilot that compared
nothing. Volume II's control arm is weaker than Volume I's strong null (no versioned belief
memory with provenance, no value-of-information assessment, no failure log). The readiness
profile has no comparator or effect-size field, so readiness could be declared without
beating any baseline. Resource parity is "comparable" in most places and "equal" in one, with
no tolerance. The tester holds the hidden references, but nothing requires independence from
the author, who took part in the only pilot.

## Evidence

- **Already in the text (Vol II §27.B, p. 50):** "Before launch, component versions, candidate
  boundary, family generator, train / selection / held_out_test split, primary metric and
  minimum practically significant effect are retained."
- **Vol II §27.B, p. 49:** "Comparisons include routine Intelligence with ordinary memory, tools
  and self-verification; the same mechanism with the proposed relations; and declared
  replacements or ablations." Compare Vol I A.4, p. 99: "an agent stack with ordinary
  planning, versioned memory of beliefs and provenance, self-checking, mismatch response,
  value-of-information assessment, and a log of failed attempts".
- **Vol II §31.A, p. 83:** "Before the control series, a ReadinessProfile is created"; its twenty
  fields are named without values or comparator arms.
- **Vol II Ch. 27, p. 44:** "Hidden references, final evaluation and criteria for selecting
  control cases remain with the tester."
- **Vol I A.4, p. 100:** "comparable total resources: number of model calls, tokens/inference-
  time compute, external sources, bench time, and hidden preparation are counted together".

## Why it matters

A procedure without parameters cannot be checked for power or fairness and leaves room for
choices made after seeing data. A readiness gate with no comparator can pass a system that adds
nothing.

## Recommendation

Publish a preregistration (for example on OSF) naming the model and version, the baseline stack
(Vol I's strong null, plus an epistemic-layer-only arm), the generator, budgets with a numeric
tolerance, outcomes, the minimum effect with a power calculation, the analysis model, the
stopping rule and the abandonment condition (MED-12). Add comparator, margin and equal-compute
fields to the ReadinessProfile, and require an independent tester or an audit of hidden
references.

## Resolved when

- [ ] A public preregistration with these elements exists before confirmatory data collection.
- [ ] The ReadinessProfile has values and requires a margin over a declared null.

## Related

- Review: [§5.2(a)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test),
  [§10](../../REVIEW.md#10-recommendations-in-priority-order)
- Issues: MAJ-01, MED-12, MED-09, MED-10, MED-24 (metric definitions)
