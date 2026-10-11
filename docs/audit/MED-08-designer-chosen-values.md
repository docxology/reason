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

## Claims under review

- **Vol II §29.0.2, p. 69:** "Before autonomy is expanded, the candidate must cultivate and test
  its first value relations in simulations, its own consequences, and dialogue. The result is an
  initial Value Map together with the causal history of why a particular state or consequence
  became significant and under which conditions the assessment applies. The teacher does not
  fill this map with ready beliefs."
- **Vol II §29.0.1, p. 68:** "In the first training profile, it is permissible to set w_i=1/4
  and K=1000. This is a declared experimental setting, not coefficients derived from the
  Compass."
- **Vol II §29.0.2, p. 70:** "Criteria are fixed by the experimenter before the run and are not
  defined only by the candidate itself."
- **Vol II §29.0.2, p. 70:** "For a small environment with a known model, decisions are compared
  with an independently computed result of the declared profile. This tests implementation and
  learning, not universality of the profile."

## Finding

The value assessment is a causal multi-attribute sum with designer-set weights and scale, and
the text is explicit that these are declared experimental settings, not quantities derived from
the Compass. The candidate is asked to test the declared scales and to propose local
corrections, which are then checked on held-out cases, and the criteria are fixed by the
experimenter. That is good method. It also means the first series measures whether the
candidate predicts consequences well on the designer's scales and agrees with the declared
profile; the small-environment test compares its decisions with "an independently computed
result of the declared profile". A claim that the values are the system's own would need
evidence that it revises weights in ways the designer and mentor did not fix, and a criterion
for when such revision is desirable rather than drift.

## Evidence

- **Already in the text (Vol II §29.0.2, p. 69):** "Scales, compensation rules, and weight ranges
  may be provided as candidate measurement methods that the system must test, not as true
  coefficients."

## Why it matters

Value formation is part of what distinguishes AR from a well-instrumented agent. If the
values are fixed by design, the first series tests calibration of consequence prediction,
which is valuable but different, and the safety analysis should treat the values as the
designer's responsibility rather than the system's.

## Ideas & possible recommendations

- **Name what the first series tests.** The volumes could state that the first series tests
  calibration of consequence prediction under fixed weights, and make no claim about value
  formation yet.
- **Define the revision rule.** Before a value-formation claim is made, the text could define
  the rule for revising weights, the evidence that may trigger a revision, and the criterion
  separating desirable revision from drift (see MED-33).
- **Vary and hide the weights across arms.** An experiment in which the weights differ between
  arms and are hidden would give evidence on whether the candidate revises weights in ways the
  designer and mentor did not fix.
- **Add a wrong-mentor arm.** One arm could have a mentor that pushes the weights in a
  predeclared wrong direction, so that revisions that follow the mentor can be told apart from
  revisions that follow the evidence.

## Resolved when

- [ ] The volumes distinguish calibration of consequence prediction from formation of values
      and claim only what is tested.
- [ ] Any value-formation claim comes with a revision rule and a drift criterion.

## Related

- Review: [§4.2(d)](../../REVIEW.md#42-toward-a-system-with-its-own-worldview-and-values-underspecified-at-the-decisive-step)
- Issues: MAJ-08 (value sum), MED-02, MED-33 (drift)
