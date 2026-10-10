---
id: MED-25
title: No defined ablation of the Core when one model plays both roles, and no capability sweep
severity: medium
area: testability
volumes: II
sections: Vol II Ch. 28 (introduction), §28.C.2, §27.B, §31.11
review: §3, §5.2(f)
status: open
---

# MED-25 · No defined ablation of the Core when one model plays both roles, and no capability sweep

**Finding.** Vol II §28.C.2 credits the Core with question formulation even when Intelligence
constructed the question, and lets one model play both roles if they are "experimentally
distinguishable". With one model, removing the Core leaves the model that produced the
questions, and a baseline's questions can be counted as Core function. The text forbids
relabelling a control as a "hidden Core" afterwards and includes link ablations (§31.11), but
does not say how the Core is ablated when one model plays both roles. Chapter 28 also
concludes that stronger Intelligence does not replace the Core without an argument, and the
first series holds Intelligence fixed, so nothing tests whether the Core's advantage shrinks
as the base model improves.

## Evidence

- **Vol II §28.C.2, p. 61:** "Question formulation counts as a function of the Core as an
  organization even when Intelligence proposed the substantive construction of the question."
  Generation and control "may therefore use the same computational substrates and even one
  model if the causal roles are experimentally distinguishable."
- **Vol II Ch. 28, p. 51:** "Increasing the power of Intelligence therefore does not by itself
  replace the Core: it only expands the space of alternatives that still requires management
  relative to the current trajectory, values, and Compass."
- **Vol II §27.B, p. 49:** the comparisons are "routine Intelligence with ordinary memory,
  tools and self-verification; the same mechanism with the proposed relations; and declared
  replacements or ablations". The guide (p. 6) says "Compare with the same Intelligence".
- **Already in the text (Vol II §27.B, p. 50; §31.11, p. 83):** "Any successful control
  cannot be retrospectively called a “hidden Core”: equivalence features are declared before
  comparison."; §31.11 lists link ablations such as "gap -> distinction".

## Why it matters

Without a defined ablation, a result cannot be attributed to the Core alone. Without a sweep,
a gain at one model strength says nothing about the next.

## Recommendation

Define the Core ablation through a measurable interface: remove the typed gap and sufficiency
records and their gating of actions, and keep free question generation by the model in every
arm. Add a preregistered sweep over base-model capability (at least three levels, same tools
and budget) and report the Core-minus-baseline gap by level.

## Resolved when

- [ ] The Core ablation is specified as an interface-level intervention, with the model's free
      question generation present in every arm.
- [ ] The first series includes a preregistered capability sweep (at least three levels), with
      the gap reported per level.

## Related

- Review: [§3](../../REVIEW.md#3-is-the-intelligencereason-distinction-meaningful-and-useful),
  [§5.2(f)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test)
- Issues: MAJ-01, MAJ-03, MED-05, MED-12
