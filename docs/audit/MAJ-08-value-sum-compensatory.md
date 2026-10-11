---
id: MAJ-08
title: The value sum is compensatory and risk-neutral, and the critical-loss safeguard is undefined
severity: major
area: safety
volumes: II
sections: Vol II §24.C, §29.0, §29.0.1, §29.0.2, §29.0.3, §29.A
review: §4.2(d), §8
status: open
github_issue: 8
---

# MAJ-08 · The value sum is compensatory and risk-neutral, and the critical-loss safeguard is undefined

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
  four independent final goals."

## Finding

At the level of the Compass the design deliberately avoids a single score: §29.A returns a
constrained vector because, as the third claim above says, a single score can hide a critical
loss behind a high value on another axis. Inside a domain, though, §29.0.1 ranks alternatives by
a weighted sum over four dimensions (first and fourth claims), and its protection against
trading a critical loss for gains elsewhere rests on a pre-check whose key term is never defined
(second claim). With the training weights (each 1/4), an action that totally destroys the
continuity of affected life processes and fully restores recoverability, Δ = (−1, +1, 0, 0),
scores exactly zero, the same as doing nothing. Because the sum is linear in expectations, it is
also risk-neutral: a 1% chance of total loss on a dimension is priced like a certain loss of
0.01. The fourth dimension (the ability to understand, test grounds and direct the trajectory)
does not say whose ability it measures; if it is the system's own, the sum contains a capability
term that can be traded against harm. Finally, no criterion says when incomparability is
"justified", so the `NORMATIVE_INCOMPARABILITY` status can be used either to avoid commitment or
to force a sum.

## Evidence

- **Vol II §29.0.1, p. 68:** the worked example is arithmetically right:
  (0.20 + 0.10 − 0.10 + 0)/4 × 1000 = +50. The same arithmetic gives
  (−1 + 1 + 0 + 0)/4 × 1000 = 0 for the case in the Finding.
- **Vol II §29.A, p. 72:** weights are used "within a domain where critical value conflicts have
  already been exposed", and an alternative is preferred "if it is no worse on critical axes and
  better on at least one under comparable confidence". Neither §29.A nor §29.0.1 defines
  "critical", a critical axis, or a threshold.
- **Already in the text (§29.0.1, p. 68):** "In the absence of justified comparability,
  incomparability is returned rather than an arbitrary common score"; "Identical [0,1] ranges
  on different scales do not prove interchangeability."
- **Already in the text (Vol II §29.0.1):** the provision is "an engineering hypothesis" whose
  "uniqueness of these scales, their universal applicability, and the effectiveness of the
  procedure have not been established" (p. 67); "Mathematical expectation is permitted when
  outcomes are defined and probabilities are grounded. Otherwise scenarios and ranges are
  compared without probabilistic interpretation." (p. 68)
- **Already in the text (Vol II §29.A, p. 72):** "Fundamental risk is defined as a set of
  inadmissible or unresolved combinations of these axes, not only as an average" (the
  `FoundationalRisk` record), though it sets no threshold for "inadmissible".

## Why it matters

The value layer is where the architecture decides what it may do to the world. A rule promising
that the sum "does not compensate for a critical loss by accumulating small gains" cannot be
implemented while "critical" is undefined; inside a sum that is fully compensatory and blind to
tail risk, it is a safety property on paper only. An implementer following §29.0.1 literally
could rank a catastrophic action level with inaction.

## Ideas & possible recommendations

- **Floors before the sum.** Per-dimension floors or red lines on Δ_i (and on the probability of
  crossing them) could be applied lexicographically before any sum, with a risk term or chance
  constraint for catastrophic outcomes.
- **Name the subject of the fourth dimension.** The text could state the subject and scale of the
  fourth dimension; if it is the system's own capability, it could be removed from the sum or
  subordinated to the floors.
- **An operational test for incomparability.** A test for when incomparability is justified could
  be, for example, that the ranking flips within the set of admissible weight profiles that
  §29.0.2 already preserves.
- **Add the zero-sum case to the mandatory tests.** The Δ = (−1, +1, 0, 0) case could be added to
  the mandatory tests of §29.0.2.

## Resolved when

- [ ] "Critical" is defined explicitly, and a critical loss cannot be traded for gains inside
      the aggregation.
- [ ] The value assessment handles tail risk and names the subject of every dimension.
- [ ] The (−1, +1, 0, 0) case is a mandatory test with a stated expected result.

## Related

- Review: [§4.2(d)](../../REVIEW.md#42-toward-a-system-with-its-own-worldview-and-values-underspecified-at-the-decisive-step),
  [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-06 (incentives), MED-08 (designer-chosen values), MED-27 (Compass
  decompositions), MED-28 (epistemic gate)
