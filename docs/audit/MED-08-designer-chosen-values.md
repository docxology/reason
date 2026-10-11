---
id: MED-08
title: Initial values are designer-chosen, so cultivation tests calibration rather than value formation
severity: medium
area: theory
volumes: II
sections: Vol II §29.0, §29.0.1, §29.0.2
review: §4.2(d)
status: open
github_issue: 16
---

# MED-08 · Initial values are designer-chosen, so cultivation tests calibration rather than value formation

**Finding.** The value assessment is a causal multi-attribute sum with designer-set weights
and scale, and the text is explicit that these are declared experimental settings, not
quantities derived from the Compass. The candidate is asked to test the declared scales and
to propose local corrections, which are then checked on held-out cases, and the criteria are
fixed by the experimenter. That is good method. It also means the first series measures
whether the candidate predicts consequences well on the designer's scales and agrees with the
declared profile; the small-environment test compares its decisions with "an independently
computed result of the declared profile". A claim that the values are the system's own would
need evidence that it revises weights in ways the designer and mentor did not fix, and a
criterion for when such revision is desirable rather than drift.

## Evidence

- **Vol II §29.0.1, p. 68:** "In the first training profile, it is permissible to set w_i=1/4
  and K=1000. This is a declared experimental setting, not coefficients derived from the
  Compass."
- **Already in the text (Vol II §29.0.2, p. 69):** "Scales, compensation rules, and weight ranges
  may be provided as candidate measurement methods that the system must test, not as true
  coefficients."
- **Vol II §29.0.2, p. 70:** "This tests implementation and learning, not universality of the
  profile."

## Why it matters

Value formation is part of what distinguishes AR from a well-instrumented agent. If the
values are fixed by design, the first series tests calibration of consequence prediction,
which is valuable but different, and the safety analysis should treat the values as the
designer's responsibility rather than the system's.

## Recommendation

State that the first series tests calibration under fixed weights. Before claiming value
formation, define the revision rule for weights, the evidence that may trigger it, the
criterion separating desirable revision from drift, and an experiment in which weights differ
and are hidden across arms, with a wrong-mentor arm that pushes weights in a predeclared
wrong direction.

## Resolved when

- [ ] The volumes distinguish calibration of consequence prediction from formation of values
      and claim only what is tested.
- [ ] Any value-formation claim comes with a revision rule and a drift criterion.

## Related

- Review: [§4.2(d)](../../REVIEW.md#42-toward-a-system-with-its-own-worldview-and-values-underspecified-at-the-decisive-step)
- Issues: MAJ-08 (value sum), MED-02, MED-33 (drift)
