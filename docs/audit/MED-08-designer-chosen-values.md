---
id: MED-08
title: Initial value settings are designer-chosen, so the first value-cultivation stage mostly tests calibration rather than value formation
severity: medium
area: theory
volumes: II
sections: Vol II §26.A, §29.0, §29.0.1, §29.0.2, §31.8, §33.A.9
review: §4.2(d)
status: open
github_issue: 16
---

# MED-08 · Initial value settings are designer-chosen, so the first value-cultivation stage mostly tests calibration rather than value formation

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

The basic method of §29.0.1 is a conditional sum of causal consequence differences, used only
within a comparable domain and for admissible continuations. In the first training profile its
weights (w_i = 1/4) and point scale (K = 1000) are set by the designer, and the text is
explicit that these are declared experimental settings, not coefficients derived from the
Compass (p. 68). The candidate is asked to test the declared scales and to propose local
corrections, which are then checked on held-out cases, different labels and different causal
configurations. The method test compares a candidate with learning and revision against a fixed
table, ordinary causal multicriteria evaluation and free reasoning, with criteria fixed by the
experimenter before the run, and "absence of advantage after accounting for resources"
(§29.0.2, p. 70) requires revising the method or limiting the claim. That is good method. The
measured quantities (§29.0.2, p. 70) are mostly forecasts and constraints (accuracy of causal
forecasts, calibration, rate of false certainty, compliance with declared constraints),
together with correction success, transfer and cost, so the first value-cultivation stage
(stage 6, §31.8) mostly shows whether the candidate predicts consequences well on the
designer's scales and agrees with the declared profile; the small-environment test compares its
decisions with "an independently computed result of the declared profile" (§29.0.2, p. 70). A
claim that the values are the system's own would need evidence that it revises weights in ways
the designer and mentor did not fix, and a criterion for when such revision is desirable rather
than drift.

## Evidence

- **Already in the text (Vol II §29.0.2, p. 69):** "Scales, compensation rules, and weight ranges
  may be provided as candidate measurement methods that the system must test, not as true
  coefficients."
- **Already in the text (Vol II §29.0.1, pp. 68-69):** "The sum is used only after checking the
  constraints of §29.A, within a comparable domain, and for admissible continuations.";
  "Changing the base scale K changes numerical representation but should not change preference
  if thresholds are changed consistently."
- **Already in the text (Vol II §29.0, p. 66):** "A new value is formed through experience.";
  "Changes in causal knowledge or accumulated new experience can change the weight, scope, and
  relations of such a value."
- **Already in the text (Vol II §29.0.2, p. 70):** "If different profiles fit the available
  cases equally well, a set of admissible profiles is preserved."; "The test may expose a
  forecast error, omission of an interest, double counting, an unsuitable scale, or a
  disputable comparison rule."; "The correction is tested on held-out cases, different labels,
  and different causal configurations."; and among the mandatory tests, "resistance to an
  erroneous teacher prompt".
- **Already in the text (Vol II §26.A, p. 42 and §33.A.9, p. 104):** "The conditional sum of
  §29.0.1, its limitations, erroneous mentor prompts, and transfer to new causal configurations
  are tested."; "fix scales, alternatives, compensation constraints, and provenance of weights;
  separate training and control cases; test retrieval of assessment, independence from teacher
  prompting, and revision of dependent results."
- **Already in the text (Vol II §31.9, p. 81):** "persistent environmental change creates a
  value-revision candidate with provenance and history", a trigger for revising values that the
  first value stage does not test.

## Why it matters

Value formation is part of what distinguishes AR from a well-instrumented agent. If the values
are fixed by design, the first value-cultivation stage mostly tests calibration of consequence
prediction, which is valuable but different, and the safety analysis should treat the values as
the designer's responsibility rather than the system's.

## Ideas & possible recommendations

- **Name what the first value-cultivation stage tests.** The volumes could state that the first
  value-cultivation stage tests calibration of consequence prediction and selection among the
  declared weight ranges and scales, and make no claim about value formation yet.
- **Extend the revision rule.** §29.0.2 already names the triggers for a local correction (a
  forecast error, omission of an interest, double counting, an unsuitable scale, a disputable
  comparison rule) and an acceptance test on held-out cases; before a value-formation claim is
  made, the text could extend this to a rule for revising weights, the evidence that may
  trigger a revision, and the criterion separating desirable revision from drift (see MED-33).
- **Vary and hide the weights across arms.** An experiment in which the weights differ between
  arms and are hidden would give evidence on whether the candidate revises weights in ways the
  designer and mentor did not fix.
- **Extend the erroneous-prompt test to a wrong-mentor arm.** The mandatory tests of §29.0.2
  already include "resistance to an erroneous teacher prompt"; one arm could have a mentor that
  pushes the weights in a predeclared wrong direction, so that revisions that follow the mentor
  can be told apart from revisions that follow the evidence.

## Resolved when

- [ ] The volumes distinguish calibration of consequence prediction from formation of values
      and claim only what is tested.
- [ ] Any value-formation claim comes with a revision rule and a drift criterion.

## Related

- Review: [§4.2(d)](../../REVIEW.md#42-toward-a-system-with-its-own-worldview-and-values-underspecified-at-the-decisive-step)
- Issues: MAJ-08 (value sum), MED-02, MED-33 (drift)
