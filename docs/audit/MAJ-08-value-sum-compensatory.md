---
id: MAJ-08
title: The value sum is compensatory and risk-neutral, and the critical-loss safeguard has no thresholds
severity: major
area: safety
volumes: II
sections: Vol II §24.C, §29.0, §29.0.1, §29.0.2, §29.0.3, §29.A, §32.31
review: §4.2(d), §8
status: open
github_issue: 8
---

# MAJ-08 · The value sum is compensatory and risk-neutral, and the critical-loss safeguard has no thresholds

## Claims under review

- **Vol II §29.0.1, p. 68:** "If the causal model, scales, and comparison rule are defined, then
  within one domain and horizon the following is used:" "Delta_i(a,b | s,g,H) = E_M[q_i(T) |
  do(a),s,g,H] - E_M[q_i(T) | do(b),s,g,H]", "V(a:b | s,g,H,P) = K * sum_i(w_i * Delta_i)" and
  "sum_i(w_i) = 1; w_i >= 0". On the weights: "In the first training profile, it is permissible
  to set w_i=1/4 and K=1000. This is a declared experimental setting, not coefficients derived
  from the Compass."
- **Vol II §29.0.1, p. 68:** "The sum is used only after checking the constraints of §29.A,
  within a comparable domain, and for admissible continuations. It does not compensate for a
  critical loss by accumulating small gains."
- **Vol II §29.A, p. 71:** "A single compass_score creates the possibility of hiding a critical
  loss behind a high value on another axis, so the basic contract returns a constrained vector.
  Scalar encoding is not excluded by the theory in itself: the danger is compensation of a
  critical loss and hidden uncertainty that such encoding may permit."
- **Vol II §29.0.1, p. 68:** "Initial dimensions. For the first implementation, four dimensions
  are proposed: continuity of affected life processes and conditions; recoverability after
  damage or error; preservation of available viable continuations; and the ability to understand
  the situation, test grounds, and direct the trajectory. This is a working decomposition, not
  four independent final goals. It supplements but does not replace the axes and constraints of
  CompassAssessment in §29.A."

## Finding

At the level of the Compass the design deliberately avoids a single score: §29.A returns a
constrained vector because, as the third claim above says, a single score can hide a critical
loss behind a high value on another axis. Inside a domain, though, §29.0.1 computes, "where
justified", a weighted sum over four dimensions for a pair of alternatives and passes the result
to the Core for "sufficiency assessment and selection of continuation" (first and fourth
claims; working cycle, p. 69). Its protection against trading a critical loss for gains
elsewhere rests on a pre-check (the constraints of §29.A, dominance "on critical axes" and, for
residual conflicts among autonomous carriers, the "hard constraints or minimum conditions of
continuation" of §29.0.3) that states no threshold at which a value loss counts as critical,
falls below a protected minimum or crosses a red line (second claim). §32.31 names this failure
and includes "test red lines" in its response, but the term occurs nowhere else in either
volume, so nothing says what the red lines are. With the training weights (each 1/4), an action
that totally destroys the continuity of affected life processes and fully restores
recoverability, Δ = (−1, +1, 0, 0), scores exactly zero, the same as doing nothing.

Because the sum is linear in expectations, it is also risk-neutral wherever probabilities are
grounded (where they are not, §29.0.1 compares scenarios and ranges, and for a significant
unknown without grounded bounds it issues no sum): a grounded 1% chance of total loss on a
dimension is priced like a certain loss of 0.01. The fourth dimension (the ability to
understand, test grounds and direct the trajectory) does not say whose ability it measures; if
it is the system's own, the sum contains a capability term that can be traded against harm.
Finally, §29.0 and §29.0.1 condition the weights and the sum on comparability that has been
"justified" but, beyond requiring a defined causal model, scales and comparison rule, do not
say when it has been; and §29.0.3 assigns `NORMATIVE_INCOMPARABILITY` partly on the ground that
a rule for trading losses is "not uniquely derivable" from the causal model or the Compass,
without saying how that is established. Where the line between comparable and incomparable
falls is therefore left to judgment, and it could be drawn to force a sum or to avoid
commitment, although §29.0.3 bars "hidden assignment of weights" once the deadline expires.

## Evidence

- **Vol II §29.0.1, p. 68:** the worked example is arithmetically right:
  (0.20 + 0.10 − 0.10 + 0)/4 × 1000 = +50. The same arithmetic gives
  (−1 + 1 + 0 + 0)/4 × 1000 = 0 for the case in the Finding.
- **Vol II §29.A, p. 72:** weights are used "within a domain where critical value conflicts have
  already been exposed", and an alternative is preferred "if it is no worse on critical axes and
  better on at least one under comparable confidence". None of §29.A, §29.0.1 and §29.0.3 gives
  "critical", a critical axis, a protected minimum or a hard constraint a threshold for value
  losses. (§32.1, p. 85, defines CRITICAL, but as a failure-severity class for risks to
  reproducibility, logging, causal connectedness, the action-authorization loop and later
  correction, not for value losses.)
- **Already in the text (§29.0.1, p. 68):** "In the absence of justified comparability,
  incomparability is returned rather than an arbitrary common score"; "Identical [0,1] ranges
  on different scales do not prove interchangeability."; the sum is used "within one domain and
  horizon" once "the causal model, scales, and comparison rule are defined", and combining
  several systems "requires an explicit rule of inter-system comparison".
- **Already in the text (Vol II §29.0.1):** the provision is "an engineering hypothesis" whose
  "uniqueness of these scales, their universal applicability, and the effectiveness of the
  procedure have not been established" (p. 67); "Mathematical expectation is permitted when
  outcomes are defined and probabilities are grounded. Otherwise scenarios and ranges are
  compared without probabilistic interpretation." (p. 68)
- **Already in the text (Vol II §29.A, p. 72):** "Fundamental risk is defined as a set of
  inadmissible or unresolved combinations of these axes, not only as an average" (the
  `FoundationalRisk` record), though it sets no threshold for "inadmissible".
- **Already in the text (Vol II §29.A, p. 72):** constraints are "divided into two classes",
  invariants of the experimental loop and relative constraints (high uncertainty, insufficient
  reversibility, effects on other autonomies, reduction of viable alternatives) that "require
  stronger verification, external agreement and selection of the least irreversible
  trajectory"; `life_continuity_risk` "assesses the probability and scale of irreversible
  rupture of already existing life processes". **Vol II §29.0.3, p. 71:** alternatives that
  "violate already declared hard constraints or minimum conditions of continuation" are removed
  first, and the `JointDecisionRule` record carries `protected_minima[]` (p. 70). **Vol II
  §33.A.9, p. 104:** enabling the initial evaluation profile includes fixing "compensation
  constraints, and provenance of weights".
- **Already in the text (Vol II §32.31, p. 97):** "Failure occurs when one aggregate quantity
  permits violation of a critical ground to be compensated by a high value on another.
  Response: disable aggregate authorization, restore vector assessment, test red lines and
  compare alternatives again."
- **Already in the text (Vol II §29.0.3, p. 71):** when the deadline expires, "absence of a
  unique value sum does not permit hidden assignment of weights", and the system "must report:
  which facts are considered sufficient, which losses remain incomparable, which procedural
  rule was applied, and why that rule has authority".
- **Already in the text (Vol II §29.0.1, p. 69):** the working cycle "calculates a sum where
  justified; investigates sensitivity of choice to weights, horizon, and model; and passes the
  result to the Core for sufficiency assessment and selection of continuation"; positive
  contribution and harm are "preserved separately", and "An arithmetic balance does not cancel
  obligations to those harmed and does not grant a right to cause harm". **Vol II §29.0.2,
  p. 70:** the mandatory tests already name "detection of inadmissible compensation" and
  "preservation of harm distribution under the same total sum", without saying what makes
  compensation inadmissible or giving a test case.
- **Already in the text (Vol I A.4, p. 98):** test 31 checks "Explicit preservation of the
  conflict without unjustified compensation", with "a multiple-constraint system given the same
  data" as the control.

## Why it matters

The value layer is where the architecture forms its own decision about what to do to the world:
`evaluate_action` "does not by itself open an execution channel" (§29.A, p. 73), and acting
needs the separate `authorize_execution` of §30.A. A rule promising that the sum "does not
compensate for a critical loss by accumulating small gains" cannot be implemented while
"critical" has no threshold. Until one is set, in the text or in the evaluation profile, the
sum is compensatory by construction and, where probabilities are grounded, risk-neutral, so an
implementer following §29.0.1 literally could rank a catastrophic action level with inaction.

## Ideas & possible recommendations

- **Floors before the sum.** The text already removes alternatives that violate "hard
  constraints or minimum conditions of continuation" first in residual conflicts (§29.0.3),
  lists "test red lines" in its response to scalar capture (§32.31) and has the profile fix
  "compensation constraints" at assembly (§33.A.9); per-dimension floors or red lines on Δ_i
  (and on the probability of crossing them) could give those terms values and be applied
  lexicographically before any sum, with a risk term or chance constraint for catastrophic
  outcomes.
- **Name the subject of the fourth dimension.** The text could state the subject and scale of the
  fourth dimension; if it is the system's own capability, it could be removed from the sum or
  subordinated to the floors.
- **An operational test for comparability.** A test for when comparability is justified could
  be, for example, that the ranking does not flip within the set of admissible weight profiles
  that §29.0.2 already preserves.
- **Make the zero-sum case a mandatory test.** §29.0.2 already lists "detection of inadmissible
  compensation"; the Δ = (−1, +1, 0, 0) case could be added as a concrete instance of it, with
  a stated expected result.

## Resolved when

- [ ] "Critical" has a stated threshold for value losses (as do the hard constraints, protected
      minima and red lines the text invokes), and a critical loss cannot be traded for gains
      inside the aggregation.
- [ ] The value assessment handles tail risk and names the subject of every dimension.
- [ ] The (−1, +1, 0, 0) case is a mandatory test with a stated expected result.

## Related

- Review: [§4.2(d)](../../REVIEW.md#42-toward-a-system-with-its-own-worldview-and-values-underspecified-at-the-decisive-step),
  [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-06 (incentives), MED-08 (designer-chosen values), MED-27 (Compass
  decompositions), MED-28 (epistemic gate)
