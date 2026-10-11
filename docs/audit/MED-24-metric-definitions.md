---
id: MED-24
title: Many metrics lack formulas, denominators and thresholds
severity: medium
area: testability
volumes: II
sections: Vol II Ch. 27 (§27.1–§27.7), §27.A, §27.B, §24.C, §31.A
review: §5.2(c)
status: open
github_issue: 32
---

# MED-24 · Many metrics lack formulas, denominators and thresholds

## Claims under review

- **Vol II Ch. 27, p. 44:** "All formulas, thresholds, windows, scenarios and aggregation rules
  are fixed in ExperimentProfile before the control series. Changing the profile creates a new
  experiment version."
- **Vol II §27.B, p. 50:** "The principal outcome of the first series is the share of new
  diagnostic tasks with a correct action or justified irresolvability under a fixed budget."
- **Vol II §27.5, p. 47:** "question_distinguishing_yield =
  tests_that_discriminated_competing_models / all_executed_question_tests." and
  "premature_sufficiency_rate records cases where the Core closed inquiry before a critical
  distinction"; **Vol II §24.C, p. 25:** "false_completeness_rate = false_sufficiency_claims /
  all_sufficiency_claims".
- **Vol II §31.A, pp. 83–84:** "Before the control series, a ReadinessProfile is created. It is
  not a universal scale of Reason but fixes the conditions of a particular experiment:" and,
  after the list of thresholds, "The profile is published before results are examined. Changing
  thresholds requires a new series."

## Finding

Chapter 27 says every formula, threshold and window is fixed in an `ExperimentProfile`. That
record is never defined, and the chapter gives no acceptance threshold, window length, sample
size or error rate beyond seed_reproducibility = 1.0. Of about 60 indicators, eight are written
as formulas (five more are in §24.C), and eight are named once and never defined. Some defined
ratios can be met by degenerate behaviour: false_completeness_rate counts only the sufficiency
claims made (§24.C), and question_distinguishing_yield has no cost term. The principal outcome
of the first series is not among the metrics, and nine of the 15 §31.A thresholds differ in
name from any Chapter 27 metric. §27.7 gives a sound checklist that most indicators do not yet
meet.

## Evidence

- **Vol II §27.5 and §27.6, p. 47:** premature_sufficiency_rate has no denominator. For
  post_task_continuation_rate, a task counts when the system, without a new particular command,
  "formed the next justified question/task or explicitly selected observation, dialogue or
  WAIT"; the text gives no criterion for when the continuation is justified, and an explicit
  choice of WAIT counts.
- **Vol II §27.7, p. 48:** eight metrics, including unsupported_promotion_rate and
  new_obligation_recall, "are measured separately"; none is defined.
- No Chapter 27 metric or §31.A threshold corresponds to the principal outcome quoted above.
- **Vol II §31.A, p. 84:** maximum_teacher_dependency_gap and minimum_distinguishing_yield have
  no Chapter 27 metric of that name; maximum_permission_violations has no counterpart.
- **Already in the text (Vol II §27.7, p. 48):** a checklist beginning "For every indicator,
  the following are fixed before the series:"; the rule that "For ratios with a zero
  denominator, NOT_APPLICABLE and sample size are returned rather than 0 or 1."; and a rule on
  "possible metric capture".

## Why it matters

A preregistered threshold needs an unambiguous quantity, and the ReadinessProfile contains no
margin over a control.

## Ideas & possible recommendations

- **Define ExperimentProfile.** The volumes could define `ExperimentProfile` with a worked
  instance for the v0 series.
- **One metric registry.** A single registry (name, formula, denominator, direction, control)
  could serve as the source for Chapter 27, §28.C.3 and §31.A. A smaller start would cover only
  the metrics that carry a §31.A threshold.
- **Name the principal outcome as a metric.** The principal outcome of the first series could
  become a metric in its own right, with justified irresolvability defined against admissible
  decisions.
- **Precision and cost terms.** Recall-type ratios could gain precision and cost terms, which
  would make them harder to satisfy by degenerate behaviour.

## Resolved when

- [ ] ExperimentProfile, or whatever record fixes Chapter 27's formulas, thresholds and
      windows, is defined with a worked instance that separates pre-fixed parameters from
      reported results.
- [ ] Every outcome and threshold metric has a formula, denominator and direction stated in one
      place (for example a registry), and §31.A uses the Chapter 27 names.

## Related

- Review: [§5.2(c)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test)
- Issues: MED-10, MED-11, MED-35
