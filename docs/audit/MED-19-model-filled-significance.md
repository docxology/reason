---
id: MED-19
title: Significance assessments filled by the language model have no accuracy test
severity: medium
area: architecture
volumes: I, II
sections: Vol I Operational Core (significance trace); Vol II §24.C, §27.5, §28.0, §29.0
review: §5.3
status: open
github_issue: 27
---

# MED-19 · Significance assessments filled by the language model have no accuracy test

**Finding.** The Core's value depends on the contents of the fields it reasons over: which
decision depends on a gap, which continuations are affected, which values apply, what the
required distinction is, what each model predicts. In an implementation with a language model
as resident Intelligence, most of these will be filled by the model. The volumes test whether
the chain exists, not whether its contents are right. The significance trace itself is an
audit path rather than a measure: nothing aggregates its many-to-many dependencies into a
magnitude or threshold for "significant", and value of information is applied only after the
dependent decision and required distinction have been established, so the formal core does
not say what makes a gap significant in the first place.

## Evidence

- **Vol I Operational Core, p. 15:** the significance trace "G → D → T → V → C, where G is the
  gap, D the dependent decision, T the affected continuations/trajectories, V the applicable
  subordinate values, and C the Compass."
- **Vol II §28.0, p. 53:** `QuestionTask` carries `dependent_decision_or_path_ref`,
  `significance_basis_refs[]`, `competing_models[]`, `required_distinction`,
  `expected_basis_change` and `expected_outcomes_by_model{}`; and "VOI/NetVOI is applied after
  the dependent decision and required distinction are established, to compare admissible ways
  of obtaining it."
- **Vol II §27.5, p. 47:** `basis_origin_trace_rate` measures whether a question has a recoverable
  chain to a `BasisInsufficiencyAssessment`, not whether the chain is correct.

## Why it matters

After transfer (MAJ-04), this is the likeliest point of failure: if the model fills the fields
poorly, the bookkeeping adds cost without benefit and the Core loses to a baseline that spends
the same tokens on direct problem-solving. The hidden ground-truth causal graphs of §24.C
already make field-level accuracy measurable.

## Recommendation

Define a significance functional over the trace (for example the expected change in loss over
the affected continuations under the value vector, subject to Compass-level constraints) with
a threshold for opening an inquiry. Score the contents of the significance fields against the
tester's ground truth: precision and recall of the dependent decision, whether the required
distinction separates the true decision regions, and calibration of predicted outcomes. Add an
ablation that replaces model-filled fields with oracle values, to bound the achievable gain.

## Resolved when

- [ ] Chapter 27 includes accuracy and calibration metrics for the significance fields.
- [ ] The first series includes an oracle-field ablation.

## Related

- Review: [§5.3](../../REVIEW.md#53-my-answer-to-the-guides-question-for-reviewers)
- Issues: MAJ-03, MAJ-04, MED-06, MED-10
