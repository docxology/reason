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

**Finding.** §29.A places an epistemic gate before the Compass assessment is used: for broad
causal reach or irreversibility, WEAK or UNSTABLE model support cannot end in ordinary
ALLOW, and absence of represented harm is not treated as evidence of safety. The purpose is
sound. The gate cannot be computed from the text. EpistemicMargin lists ten signals and a
timestamp with no formula, scale, aggregation or threshold; model_support has no thresholds;
unresolved_blind_spot_pressure occurs once and is not a field of EpistemicMargin; "broad
causal reach" has no scale; and the text does not say who computes the gate. ALLOW is not an
output of evaluate_action or authorize_execution. Verification debt and the gates to larger
environments have the same gap.

## Evidence

- **Vol II §24.C.1, p. 26:** EpistemicMargin has fields from context_novelty to
  last_frame_reviewed_at, and "elevated EpistemicMargin launches frame_challenge()". No
  function maps the fields to "elevated".
- **Vol II §29.A, p. 72:** if "EpistemicMargin is high relative to the scale of the decision",
  the risk fields must be UNRESOLVED; "model_support: SUFFICIENT / WEAK / UNSTABLE" has no
  thresholds; "unresolved_blind_spot_pressure" appears only here.
- **Vol II §29.A, p. 72, and §30.A, p. 75:** "WEAK/UNSTABLE cannot end in ordinary ALLOW", but
  evaluate_action returns "preferred_result: CHOOSE / REVERSIBLE_TEST / PAUSE / DIALOGUE /
  REJECT" and authorize_execution returns "result: APPROVE / REJECT / REQUEST_REVISION /
  REQUEST_MORE_DATA".
- **Vol II §24.D.3, p. 31, and Ch. 26, p. 39:** "With high debt, the Core receives a separate
  VerificationGap"; "The environment may be made more complex only after metrics stabilize at
  the current level." Neither "high" nor "stabilize" has a criterion.
- **Already in the text (Vol II §29.A, p. 72):** the gate "prohibits treating absence of
  represented harm as positive evidence of safety", and §24.C.1 (p. 26) describes the margin
  as "a reserve of caution that grows with observable signs that the current semantic frame
  may be too narrow".

## Why it matters

Safety-relevant gating rests on quantities that cannot be computed. Two implementations can
reach different verdicts on the same case, and the gate cannot be tested for false passes.

## Recommendation

Define model_support as a function of EpistemicMargin fields, with preregistered scales and
thresholds, and say who computes it. Add or drop unresolved_blind_spot_pressure. Use one
decision vocabulary for the gate, evaluate_action and authorize_execution, and give
debt_priority, "high debt" and the environment-transition criteria computable definitions.

## Resolved when

- [ ] model_support and EpistemicMargin have defined inputs, scales, aggregation and
      preregistered thresholds for the first series.
- [ ] The gate's outputs use the decision vocabulary of evaluate_action and
      authorize_execution.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-03, MAJ-08, MED-29
