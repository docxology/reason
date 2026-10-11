---
id: MED-27
title: Three operational decompositions of the Compass coexist without a mapping
severity: medium
area: definitions
volumes: II
sections: Vol II §24.C, §26.A, §27.3, §29.0.1, §29.A, §32.36
review: §2.3
status: open
github_issue: 35
---

# MED-27 · Three operational decompositions of the Compass coexist without a mapping

## Claims under review

- **Vol II §24.C, p. 25:** "The first three unfold the operational meaning of the Compass; the
  fourth connects them with the current coordinate and self-model."
- **Vol II §27.3, p. 45:** "compass_semantic_coverage is permitted as a diagnostic vector life
  / truth / diversity / self_scope".
- **Vol II §29.A, p. 71:** "The axes below are not three equal highest values and do not
  restore the earlier Life-Truth-Diversity scheme".
- **Vol II §29.0.1, p. 68:** "For the first implementation, four dimensions are proposed:
  continuity of affected life processes and conditions; recoverability after damage or error;
  preservation of available viable continuations; and the ability to understand the situation,
  test grounds, and direct the trajectory."

## Finding

Vol II unfolds the Compass operationally in three ways, as the claims above show. §29.A
defines the CompassAssessment axes (life_continuity_risk, reality_divergence, future_path_loss,
affected_autonomies, reversibility) and says they are "not three equal highest values" and "do
not restore the earlier Life-Truth-Diversity scheme" (§29.A, p. 71). It describes
reality_divergence as "a condition of model corrigibility" and future_path_loss as "the risk of
irreversible closure of viable continuations", and p. 72 defines the first three axes in prose,
but it does not say how the axes correspond to life, truth and diversity. §24.C and §27.3 keep
the labels life, truth and diversity, with self_scope, as a semantic frame and a diagnostic
vector for coverage. §29.0.1 proposes a third set, four valuation dimensions. No table shows
what corresponds to what, for example whether recoverability is reversibility or whether
reality_divergence is truth. The coverage metrics are therefore indexed by labels that the
assessment contract does not reuse, and the field compass_axes_covered[] has no stated domain
(§27.3 and §32.36 speak of axes of that frame, which suggests the values of the field but does
not state them).

## Evidence

- **Vol II §24.C, p. 25:** the WorldviewCoverage record in the same section lists
  compass_axes_covered[] and nowhere defines its values.
- **Vol II §26.A, p. 41:** the grid reward "cannot be declared an operational equivalent of
  Life, Truth and Diversity".
- **Already in the text (Vol II §29.0.1, p. 68):** "It supplements but does not replace the
  axes and constraints of CompassAssessment in §29.A."
- **Already in the text (Vol II §29.A, p. 72):** reality_divergence "assesses how strongly a
  decision depends on unconfirmed premises, ignores available facts, or creates an incentive to
  conceal discrepancy between prediction and observation".
- **Already in the text (Vol II §24.C, p. 25; §27.3, p. 45; §32.36, p. 97):** the labels are not
  presented as independent goals or as one score ("These groups are not four independent
  goals"; "not as one percentage of maturity"), and the text speaks of "one axis" of the vector
  and of "every relevant semantic Compass axis". This suggests that life, truth, diversity and
  self_scope are the values of compass_axes_covered[], but no definition says so or relates
  them to the axes of §29.A.

## Why it matters

The coverage metrics, the assessment contract and the valuation sum are not shown to measure
the same thing, so a result stated in one set of terms cannot be carried to another.

## Ideas & possible recommendations

- **A mapping table.** One option is a single table among the three sets that shows which §29.A
  axes and §29.0.1 dimensions correspond to life, truth, diversity and self_scope, and which
  have no counterpart.
- **Retire two of the three.** The text could instead keep one decomposition and retire the
  other two, so that §24.C, §27.3, §29.A and §29.0.1 all use it.
- **Define the coverage values.** The values of compass_axes_covered[] could be defined, and
  the §24.C and §27.3 coverage metrics indexed by whichever set is retained.

## Resolved when

- [ ] One decomposition is used across §24.C, §27.3, §29.A and §29.0.1, or an explicit mapping
      covers all three sets.
- [ ] The domain of compass_axes_covered[] is defined.

## Related

- Review: [§2.3](../../REVIEW.md#23-the-philosophical-layer-does-not-carry-weight-in-the-engineering)
- Issues: MED-02, MED-08, MED-21
