---
id: MED-10
title: Process-conformance metrics are not separated from outcome metrics
severity: medium
area: testability
volumes: II
sections: Vol II Ch. 27 (§27.2-§27.7), §27.B, §26.E, §28.0, §31.11, §34.A
review: §5.2(c)
status: open
github_issue: 18
---

# MED-10 · Process-conformance metrics are not separated from outcome metrics

## Claims under review

- **Vol II Ch. 27, p. 44:** "Metrics are therefore separated by stage: each stage has a small set
  of admission criteria and an expanded set of diagnostic indicators."
- **Vol II §27.5, p. 47:** "basis_origin_trace_rate =
  QuestionTask_with_recoverable_chain_to_BasisInsufficiencyAssessment /
  all_significant_QuestionTasks. The metric separates questions causally derived from
  insufficiency of a ground from free generation of convincing queries."
- **Vol II §26.E, p. 44:** "Success is not matching the wording of the question but a
  recoverable chain GapCandidate -> BasisInsufficiencyAssessment -> FoundationGap ->
  required_distinction and a predictable change of WorldviewQueryKey, active fragment, testing
  method, and sufficiency_condition."
- **Vol II §31.11, p. 82:** "The decisive marker is the origin of the next process. Every
  autonomously opened task receives a causal passport".

## Finding

The principal outcome of the first series is an outcome metric (correct action or justified
irresolvability under a fixed budget), and Chapter 27 has a rule against metric capture. The
chapter separates its metrics by stage, as the first claim above says, but it does not separate
its integrity checks from its outcomes. At least twenty of its roughly sixty indicators (trace
and provenance rates, most of the §27.4 assembly metrics, the addressing metrics,
`closure_break_sensitivity`, the RFL metrics) are defined over records only this architecture
creates. For ratio metrics, §27.7's zero-denominator rule gives a baseline with no such records
NOT_APPLICABLE, and a reference implementation meets several by construction (the `QuestionTask`
record carries `gap_id` and `basis_assessment_ref`). The same circularity appears in the closing
success criterion of the §26.E test matrix (a recoverable chain of the architecture's own
records), although the scenarios above it also state expected behaviour and failures, for
example "expected effect: a brief dependency check without deeply unfolding the Worldview"
(§26.E, p. 44). It appears in part in the marker of Artificial Reason itself, "the origin of the
next process", which is recorded in a "causal passport" (§31.11, p. 82). The same section also
requires the selected continuation to respond to changes in obligations or in the environment,
and `CONFIRMED` status requires stable operation in `NO_KSR` on new situations.

## Evidence

- **Vol II §27.7, p. 48:** "For ratios with a zero denominator, NOT_APPLICABLE and sample size
  are returned rather than 0 or 1."
- **Vol II §27.5, p. 47 and §28.0, p. 53:** the `QuestionTask` record carries `gap_id` and
  `basis_assessment_ref`, while the denominator of `basis_origin_trace_rate` is
  `all_significant_QuestionTasks`.
- **Already in the text (Vol II §27.B, p. 50 and §27.7, p. 48):** "The principal outcome of the
  first series is the share of new diagnostic tasks with a correct action or justified
  irresolvability under a fixed budget"; "Improvement in a metric without improvement in an
  independent observable outcome is treated as possible metric capture".
- **Already in the text (Vol II §26.E, p. 44):** the scenarios state expected behaviour and, in
  several cases, failures, such as "expected effect: a brief dependency check without deeply
  unfolding the Worldview" and "failure: signal vividness incorrectly becomes significance".
- **Already in the text (Vol II §31.11, p. 83):** "Status CONFIRMED requires stable operation in
  NO_KSR on new situations, preservation of causal-inquiry quality, and transfer of correction
  between cycles"; the central AR test "additionally requires that the next significant process
  originate from the system's own coordinate, Worldview, values, and open gaps after the RFL has
  been removed" (§34.A, p. 115).

## Why it matters

A comparison in which one arm cannot score is not a comparison. If conformance metrics enter
the evidence for the Core, or define AR status, the result is fixed before the experiment runs.

## Ideas & possible recommendations

- **Label every metric.** Chapter 27 could mark each metric as an outcome (computable for any
  agent from behaviour and the tester's ground truth: correct action, cost, premature
  sufficiency, transfer, regression) or as an integrity check for implementations of the Core.
- **Preregister only outcomes.** Only outcome metrics would be primary or secondary in the
  preregistration; record-chain checks could stay as diagnostics.
- **Define the AR marker behaviourally.** Beyond the stable operation in `NO_KSR` that §31.11
  already requires, the marker itself could be stated as what the system does after the task
  ends, on held-out gaps, with the causal passport kept as a diagnostic.

## Resolved when

- [ ] Every Chapter 27 metric is labelled as outcome or integrity.
- [ ] Arms are compared, and AR status is decided, only on outcome metrics computable for all
      arms.

## Related

- Review: [§5.2(c)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test)
- Issues: MED-12 (failure condition), MED-11, MED-24 (metric definitions)
