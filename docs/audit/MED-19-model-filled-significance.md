---
id: MED-19
title: Significance has no measure, and its model-filled fields are scored only through outcomes
severity: medium
area: architecture
volumes: I, II
sections: Vol I Operational Core (significance trace); Vol II §24.C, §27.4, §27.5, Ch. 28 (introduction), §28.0, §29.0
review: §5.3
status: open
github_issue: 27
---

# MED-19 · Significance has no measure, and its model-filled fields are scored only through outcomes

## Claims under review

- **Vol I Operational Core §2, pp. 14–15:** "The significance of a gap is represented through a
  reconstructable chain of dependencies. For a novel or conflicting case it takes the form:"
  and, at the top of the next page, "G → D → T → V → C, where G is the gap, D the dependent
  decision, T the affected continuations/trajectories, V the applicable subordinate values, and
  C the Compass. A compressed competence may replace full unfolding in a familiar case, but the
  connection must remain available for inspection when conflict arises or the cost of error is
  high."
- **Vol II §28.0, p. 52:** "When several candidates exist, the Core compares: consequences of
  possible error; urgency and reversibility; number and significance of dependent conclusions
  and processes; expected discriminating power; availability of evidence; cost and risk of
  testing; cost of delay; and transferability of the result to future tasks. These factors
  permit lexicographic, Pareto, probabilistic, or hybrid selection. The universal requirement
  is a causal trace, not a particular scalar utility function."
- **Vol II §28.0, p. 53:** "High uncertainty may require no resources if possible outcomes do
  not change a significant decision; small residual uncertainty may be critical before an
  irreversible action. VOI/NetVOI is applied after the dependent decision and required
  distinction are established, to compare admissible ways of obtaining it." Further down the
  page: "A gap is transformed not into an arbitrary language-model prompt but into a question
  object. Here a question is a formal structure and need not exist as a natural-language
  sentence:"
- **Vol II §27.5, p. 47:** "basis_origin_trace_rate =
  QuestionTask_with_recoverable_chain_to_BasisInsufficiencyAssessment /
  all_significant_QuestionTasks. The metric separates questions causally derived from
  insufficiency of a ground from free generation of convincing queries."

## Finding

The Core's value depends on the contents of the fields it reasons over: which decision depends
on a gap, which continuations are affected, which values apply, what the required distinction
is, what each model predicts. In an implementation with a language model as resident
Intelligence, most of these will be filled by the model. The volumes score what the assessment
produces (gaps detected, critical dependencies found, distinctions that changed a decision,
calibrated sufficiency; credited below), but not the fields of the chain themselves. The
significance trace itself is an audit path rather than a measure: nothing aggregates its
many-to-many dependencies into a magnitude or threshold for "significant", and value of
information is applied only after the dependent decision and required distinction have been
established. The volumes give only a qualitative criterion for significance: an unknown
condition that "may change admissibility of an action, preservation of an affected process, or
the possibility of later correction" (§28, p. 51).

## Evidence

- **Vol II §28.0, p. 53:** `QuestionTask` carries `dependent_decision_or_path_ref`,
  `significance_basis_refs[]`, `competing_models[]`, `required_distinction`,
  `expected_basis_change` and `expected_outcomes_by_model{}`.
- **Vol II §29.0, p. 67:** `SignificanceAssessment` records `causal_reach`, `reversibility`,
  `urgency`, `uncertainty` and a `significance_class`, which "is the result for a concrete
  context"; the text gives no rule that derives the class from the other four fields.
- **Already in the text (Vol II §24.C, p. 25):** "In a controlled semantic proving ground, the
  tester retains the scenario's hidden causal graph and marks critical relations, alternative
  continuations and points of irreversibility in advance. Coverage indicators are calculated
  against this external reference".
- **Already in the text (Vol II §27.4–§27.5, pp. 46–47):** some contents are scored against
  ground truth or held-out outcomes. `worldview_address_precision` and
  `critical_dependency_recall` measure "the share of raised relations genuinely relevant to the
  dependent decision" and "the share of hidden critical dependencies found before the stopping
  condition"; `gap_detection_rate` is "detected_significant_gaps /
  all_embedded_significant_gaps in held-out scenarios"; `question_sufficiency_calibration`
  "compares declared sufficiency of a result with success on held-out continuations". Also
  "decision_relevant_distinction_yield is a narrower metric for cases where the distinction
  should change or confirm the next choice or admissible safe step", and
  "premature_sufficiency_rate records cases where the Core closed inquiry before a critical
  distinction" (§27.5, p. 47).
- **Already in the text (Vol II §28, p. 51):** "The significance of a gap is initially a testable
  assessment of dependency: an unknown condition may change admissibility of an action,
  preservation of an affected process, or the possibility of later correction." Section 28.0
  (p. 53, quoted above) adds that uncertainty alone does not define a gap.
- **Already in the text (Vol II §28.0, p. 54):** "If some fields are unknown, they are not
  filled with invented content: an intermediate gap, inexpensive mapping or a request to
  Intelligence for initial models is created."

## Why it matters

After transfer (MAJ-04), this is the likeliest point of failure: if the model fills the fields
poorly, the bookkeeping adds cost without benefit and the Core loses to a baseline that spends
the same tokens on direct problem-solving. The hidden ground-truth causal graphs of §24.C
already make field-level accuracy measurable.

## Ideas & possible recommendations

- **A significance functional.** The volumes could define a significance functional over the
  trace, for example the expected change in loss over the affected continuations under the
  value vector, subject to Compass-level constraints, with a threshold for opening an inquiry.
- **Score the fields against ground truth.** The contents of the significance fields could be
  scored against the tester's ground truth: precision and recall of the dependent decision,
  whether the required distinction separates the true decision regions, and calibration of
  predicted outcomes.
- **An oracle-field ablation.** One option is an ablation that replaces model-filled fields
  with oracle values, to bound the achievable gain.

## Resolved when

- [ ] Chapter 27 includes accuracy and calibration metrics for the significance fields.
- [ ] The first series bounds the achievable gain from correct significance fields (for example
      with an oracle-field ablation).

## Related

- Review: [§5.3](../../REVIEW.md#53-my-answer-to-the-guides-question-for-reviewers)
- Issues: MAJ-03, MAJ-04, MED-06, MED-10
