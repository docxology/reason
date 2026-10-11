---
id: MED-25
title: No defined ablation of the Core when one model plays both roles, and no capability sweep in the first series
severity: medium
area: testability
volumes: II
sections: Vol II guide, Ch. 28 (introduction), §28.C.2, §27.B, §31.11, §33.D
review: §3, §5.2(f)
status: open
github_issue: 33
---

# MED-25 · No defined ablation of the Core when one model plays both roles, and no capability sweep in the first series

## Claims under review

- **Vol II §28.C.2, p. 61:** "Question formulation counts as a function of the Core as an
  organization even when Intelligence proposed the substantive construction of the question."
  The same section adds: "Generation and control may therefore use the same computational
  substrates and even one model if the causal roles are experimentally distinguishable."
- **Vol II Ch. 28, p. 51:** "Increasing the power of Intelligence therefore does not by itself
  replace the Core: it only expands the space of alternatives that still requires management
  relative to the current trajectory, values, and Compass."
- **Vol II §27.B, p. 49:** "Controls. Comparisons include routine Intelligence with ordinary
  memory, tools and self-verification; the same mechanism with the proposed relations; and
  declared replacements or ablations."; **Vol II guide, p. 6:** the table gives, as the
  discriminating test for "The Core usefully organizes inquiry", "Compare with the same
  Intelligence" (same memory, tools and total budget, a different organization of test
  selection).

## Finding

Vol II §28.C.2 credits the Core with question formulation even when Intelligence constructed
the question, and lets one model play both roles if they are "experimentally distinguishable".
With one model, removing the Core leaves the model that produced the questions, and a
baseline's questions can be counted as Core function. The text forbids relabelling a control as
a "hidden Core" afterwards, includes link ablations (§31.11), states a functional boundary
between generation and control (§28.C.2), sets a general criterion for an intervention (§27.B)
and requires a separate control for ready-made questions, but it does not say what the
intervention is when one model plays both roles.

Chapter 28 infers that stronger Intelligence "does not by itself replace the Core" (p. 51) from
a functional division of labour: Intelligence constructs models, methods and plans, and the
Core determines which insufficiency they must serve, which distinction can change the ground
and when the result is sufficient. That is a conceptual argument, not a measured result. The
first series compares arms that share the same Intelligence, and §33.D defers capability
scaling to a later stage in which a baseline and a scaled version are compared on the same
tasks, with operation of the Core among the invariants to be preserved. The text does not
describe a comparison of the Core with a no-Core baseline at several Intelligence levels, so
whether the Core's advantage shrinks as the base model improves remains untested.

## Evidence

- **Already in the text (Vol II §27.B, p. 50):** "Any successful control cannot be
  retrospectively called a 'hidden Core': equivalence features are declared before comparison."
- **Already in the text (Vol II §31.11, p. 83):** link ablations: "Ablations test the links
  coordinate -> significance, significance -> GapCandidate, GapCandidate -> FoundationGap, gap
  -> distinction, evidence -> revision, consequence -> new state, and new state -> next
  process."
- **Already in the text (Vol II §28.C.2, p. 61):** "The 'Core / Intelligence' boundary is
  functional: generation expands the possibility space; the organization of the Core
  determines which distinction becomes the current work, what resource to give it, and what to
  do with the result."
- **Already in the text (Vol II §27.B, pp. 49–50):** "An intervention must change the target
  information or relation while preserving an operative interface and comparable resources."
  Question selection and use of the answer are tested separately, and "Ready-made questions
  form a separate control with external assistance explicitly counted."
- **Already in the text (Vol II Ch. 28, p. 51):** "Intelligence is responsible for
  constructing possible models, methods, and plans; the Core determines which insufficiency
  they must serve, which distinction can change the ground, and when the result is
  sufficient."
- **Already in the text (Vol II §33.D, p. 113):** a later scaling stage in which "The baseline
  and scaled versions are compared on the same class of tasks with resources explicitly
  accounted for." The invariants to be preserved include "operation of the Core: gap → models →
  required distinction → test → sufficiency", and the ScaleInvariantReport has the fields
  capability_gain and core_navigation_quality. The section also says: "Growth of Intelligence
  expands the space of possible models; growth of the Core prevents direction from being lost
  in that space." The guide says: "ASI is treated as a later stage of scaling." (p. 6)

## Why it matters

Without a defined ablation, a result cannot be attributed to the Core alone. Without a sweep in
the first series, a gain at one model strength says nothing about the next.

## Ideas & possible recommendations

- **Define the ablation at an interface.** The Core ablation could be defined through a
  measurable interface, which would specialise the §27.B intervention criterion (change the
  target relation while preserving an operative interface and comparable resources) to the
  one-model case: remove the typed gap and sufficiency records and their gating of actions, and
  keep free question generation by the model in every arm.
- **A preregistered capability sweep.** The first series could add a preregistered sweep over
  base-model capability, at least three levels with the same tools and budget.
- **Report the gap by level.** The Core-minus-baseline gap could be reported at each capability
  level, so that readers can see whether the advantage grows or shrinks as the base model
  improves.

## Resolved when

- [ ] The Core ablation is specified as a measurable intervention for the one-model case, for
      example at the interface with the model's free question generation present in every arm.
- [ ] The first series includes a preregistered test of how the Core's advantage changes with
      base-model capability (for example a sweep over at least three levels), with the gap
      reported per level.

## Related

- Review: [§3](../../REVIEW.md#3-is-the-intelligencereason-distinction-meaningful-and-useful),
  [§5.2(f)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test)
- Issues: MAJ-01, MAJ-03, MED-05, MED-12
