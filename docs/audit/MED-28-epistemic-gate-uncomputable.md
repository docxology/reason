---
id: MED-28
title: The epistemic gate and EpistemicMargin cannot be computed
severity: medium
area: safety
volumes: II
sections: Vol II §24.C.1, §24.D.3, Ch. 26, §29.A, §30.A
review: §8
status: open
github_issue: 36
---

# MED-28 · The epistemic gate and EpistemicMargin cannot be computed

## Claims under review

- **Vol II §29.A, p. 72:** "An epistemic gate is therefore introduced before CompassAssessment
  is used"; "For broad causal reach or irreversibility, WEAK/UNSTABLE cannot end in ordinary
  ALLOW, even if known Compass axes appear safe."
- **Vol II §24.C.1, p. 26:** "It is a reserve of caution that grows with observable signs that
  the current semantic frame may be too narrow." Further on: "Before an irreversible decision
  or one with broad consequences, elevated EpistemicMargin launches frame_challenge()".
- **Vol II §29.A, p. 72:** "If coverage_status != LOCAL_SUFFICIENT, the frame is unstable, or
  EpistemicMargin is high relative to the scale of the decision, life_continuity_risk and
  future_path_loss must have status UNRESOLVED rather than being forced to 0."
- **Vol II §24.D.3, p. 31:** "With high debt, the Core receives a separate VerificationGap, and
  new irreversible dependencies on that ground are prohibited until testing or explicit
  external authorization." **Vol II Ch. 26, p. 39:** "The environment may be made more complex
  only after metrics stabilize at the current level."

## Finding

§29.A places an epistemic gate before the Compass assessment is used: for broad causal reach or
irreversibility, WEAK or UNSTABLE model support cannot end in ordinary ALLOW, and absence of
represented harm is not treated as evidence of safety. The purpose is sound. The gate cannot be
computed from the text. EpistemicMargin lists ten signals and a timestamp with no formula,
scale, aggregation or threshold; model_support has no thresholds;
unresolved_blind_spot_pressure occurs once and is not a field of EpistemicMargin; "broad causal
reach" has no scale; and the text does not say who computes the gate. ALLOW is not an output of
evaluate_action or authorize_execution. Verification debt and the gates to larger environments
have the same gap.

## Evidence

- **Vol II §24.C.1, p. 26:** EpistemicMargin has fields from context_novelty to
  last_frame_reviewed_at. No function maps the fields to "elevated".
- **Vol II §29.A, p. 72:** "model_support: SUFFICIENT / WEAK / UNSTABLE" has no thresholds;
  "unresolved_blind_spot_pressure" appears only here, among the gate's outputs.
- **Vol II §29.A, p. 72, and §30.A, p. 75:** ALLOW is not an output of either function.
  evaluate_action returns "preferred_result: CHOOSE / REVERSIBLE_TEST / PAUSE / DIALOGUE /
  REJECT" and authorize_execution returns "result: APPROVE / REJECT / REQUEST_REVISION /
  REQUEST_MORE_DATA". The gate itself returns "allowed_use: FINAL_FILTER / REVERSIBLE_TEST_ONLY
  / PAUSE_AND_RESEARCH".
- **Vol II §24.D.3, p. 31, and Ch. 26, p. 39:** neither "high" nor "stabilize" has a criterion.
- **Already in the text (Vol II §29.A, p. 72):** the gate "prohibits treating absence of
  represented harm as positive evidence of safety". §24.C.1 (p. 26) also says that the margin
  is not an estimate of the number of unknown unknowns, and describes it as the reserve of
  caution quoted above.

## Why it matters

Safety-relevant gating rests on quantities that cannot be computed. Two implementations can
reach different verdicts on the same case, and the gate cannot be tested for false passes.

## Ideas & possible recommendations

- **Define model_support as a function.** The text could define model_support as a function of
  the EpistemicMargin fields, with preregistered scales and thresholds, and say who computes
  it.
- **Settle unresolved_blind_spot_pressure.** It could be added as a field of EpistemicMargin or
  dropped from the gate's outputs.
- **One decision vocabulary.** The gate, evaluate_action and authorize_execution could share
  one set of decision values. A cheaper variant is a table that maps each function's values
  onto the others.
- **Computable criteria for debt and transitions.** debt_priority, "high debt" and the
  environment-transition criteria could be given computable definitions.

## Resolved when

- [ ] model_support and EpistemicMargin have defined inputs, scales, aggregation and
      preregistered thresholds for the first series.
- [ ] The gate, evaluate_action and authorize_execution share one decision vocabulary, or the
      text maps each vocabulary onto the others.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-03, MAJ-08, MED-29
