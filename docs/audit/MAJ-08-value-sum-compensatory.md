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

**Finding.** At the level of the Compass the design deliberately avoids a single score: §29.A
returns a constrained vector because "A single compass_score creates the possibility of
hiding a critical loss behind a high value on another axis" (p. 71). Inside a domain, though,
§29.0.1 ranks alternatives by a weighted sum over four dimensions, and its protection
against trading a critical loss for gains elsewhere rests on a pre-check whose key term is
never defined. With the training weights (each 1/4), an action that totally destroys the
continuity of affected life processes and fully restores recoverability, Δ = (−1, +1, 0, 0),
scores exactly zero, the same as doing nothing. Because the sum is linear in expectations,
it is also risk-neutral: a 1% chance of total loss on a dimension is priced like a certain
loss of 0.01. The fourth dimension (the ability to understand, test grounds and direct the
trajectory) does not say whose ability it measures; if it is the system's own, the sum
contains a capability term that can be traded against harm. Finally, no criterion says when
incomparability is "justified", so the `NORMATIVE_INCOMPARABILITY` status can be used either
to avoid commitment or to force a sum.

## Evidence

- **Vol II §29.0.1, p. 68:** "V(a:b | s,g,H,P) = K * sum_i(w_i * Delta_i)" with "sum_i(w_i) =
  1; w_i >= 0", and "it is permissible to set w_i=1/4 and K=1000". The worked example is
  arithmetically right: (0.20 + 0.10 − 0.10 + 0)/4 × 1000 = +50.
- **Vol II §29.0.1, p. 68:** "The sum is used only after checking the constraints of §29.A
  [...] It does not compensate for a critical loss by accumulating small gains." Neither
  section defines "critical", a critical axis, or a threshold.
- **Vol II §29.A, p. 72:** weights are used "within a domain where critical value conflicts
  have already been exposed", and an alternative is preferred "if it is no worse on critical
  axes and better on at least one under comparable confidence".
- **Vol II §29.0.1, p. 68:** the four dimensions end with "the ability to understand the
  situation, test grounds, and direct the trajectory", with no subject named.
- **Already in the text (§29.0.1, p. 68):** "In the absence of justified comparability,
  incomparability is returned rather than an arbitrary common score"; "Identical [0,1] ranges
  on different scales do not prove interchangeability."

## Why it matters

The value layer is where the architecture decides what it may do to the world. A rule
promising "no compensation of critical losses" that cannot be implemented, inside a sum that
is fully compensatory and blind to tail risk, is a safety property on paper only. An
implementer following §29.0.1 literally could rank a catastrophic action level with
inaction.

## Recommendation

Define per-dimension floors or red lines on Δ_i (and on the probability of crossing them),
apply them lexicographically before any sum, and add a risk term or chance constraint for
catastrophic outcomes. State the subject and scale of the fourth dimension; if it is the
system's own capability, remove it from the sum or subordinate it to the floors. Give an
operational test for justified incomparability (for example, the ranking flips within the
set of admissible weight profiles that §29.0.2 already preserves). Add the Δ = (−1, +1, 0, 0)
case to the mandatory tests of §29.0.2.

## Resolved when

- [ ] "Critical" losses are defined by explicit thresholds applied before aggregation.
- [ ] The value assessment handles tail risk and names the subject of every dimension.
- [ ] The (−1, +1, 0, 0) case is a mandatory test with a stated expected result.

## Related

- Review: [§4.2(d)](../../REVIEW.md#42-toward-a-system-with-its-own-worldview-and-values-underspecified-at-the-decisive-step),
  [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-06 (incentives), MED-08 (designer-chosen values), MED-27 (Compass
  decompositions), MED-28 (epistemic gate)
