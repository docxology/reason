---
id: MED-10
title: Process-conformance metrics are not separated from outcome metrics
severity: medium
area: testability
volumes: II
sections: Vol II Ch. 27 (§27.2-§27.7), §27.B, §26.E, §31.11
review: §5.2(c)
status: open
github_issue: 18
---

# MED-10 · Process-conformance metrics are not separated from outcome metrics

**Finding.** The principal outcome of the first series is an outcome metric (correct action or
justified irresolvability under a fixed budget), and Chapter 27 has a rule against metric
capture. The chapter does not, however, separate its integrity checks from its outcomes. At
least twenty of its roughly sixty indicators (trace and provenance rates, most of the §27.4
assembly metrics, the addressing metrics, `closure_break_sensitivity`, the RFL metrics) are
defined over records only this architecture creates; by §27.7's own rule a baseline gets
NOT_APPLICABLE, and a reference implementation meets several by construction (a `QuestionTask`
exists only if derived from a `BasisInsufficiencyAssessment`). The same circularity appears in
the success criterion of the §26.E test matrix (emitting the architecture's own record chain)
and in the marker of Artificial Reason itself (the "causal passport" of a self-generated
process).

## Evidence

- **Vol II §27.5, p. 47:** `basis_origin_trace_rate` is defined as
  `QuestionTask_with_recoverable_chain_to_BasisInsufficiencyAssessment / all_significant_QuestionTasks`.
- **Vol II §27.7, p. 48:** "For ratios with a zero denominator, NOT_APPLICABLE and sample size
  are returned rather than 0 or 1."
- **Vol II §26.E, p. 44:** "Success is not matching the wording of the question but a recoverable
  chain GapCandidate -> BasisInsufficiencyAssessment -> FoundationGap -> required_distinction".
- **Vol II §31.11, p. 82:** "The decisive marker is the origin of the next process."
- **Already in the text (Vol II §27.B, p. 50 and §27.7, p. 48):** "The principal outcome of the
  first series is the share of new diagnostic tasks with a correct action or justified
  irresolvability under a fixed budget"; "Improvement in a metric without improvement in an
  independent observable outcome is treated as possible metric capture".

## Why it matters

A comparison in which one arm cannot score is not a comparison. If conformance metrics enter
the evidence for the Core, or define AR status, the result is fixed before the experiment runs.

## Recommendation

Label every Chapter 27 metric as an outcome (computable for any agent from behaviour and the
tester's ground truth: correct action, cost, premature sufficiency, transfer, regression) or an
integrity check for implementations of the Core. Preregister only outcomes as primary or
secondary, define the AR marker behaviourally (what the system does after the task ends, on
held-out gaps), and keep record-chain checks as diagnostics.

## Resolved when

- [ ] Every Chapter 27 metric is labelled as outcome or integrity.
- [ ] Arms are compared, and AR status is decided, only on outcome metrics computable for all
      arms.

## Related

- Review: [§5.2(c)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test)
- Issues: MED-12 (failure condition), MED-11, MED-24 (metric definitions)
