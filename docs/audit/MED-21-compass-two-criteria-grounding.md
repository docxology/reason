---
id: MED-21
title: The Compass has two non-equivalent criteria, and its grounding clause is analytic or false
severity: medium
area: theory
volumes: I, II
sections: Vol I Key Definitions, Ch. 2, A.1; Vol II §29.0.3, §29.A
review: §2.3
status: open
github_issue: 29
---

# MED-21 · The Compass has two non-equivalent criteria, and its grounding clause is analytic or false

## Claims under review

- **Vol I Key Definitions (Compass), p. 11:** "In the present model its direction is the
  continuation and development of Life through growth in the ability to understand and direct
  its own trajectory; its value expression forms the highest level of the value system.
  Independent ground of the Compass - preservation of viable continuation and the space of
  future possibilities for Life. Growth in the ability to understand and direct a trajectory is
  valuable as a way to distinguish consequences in advance, preserve corrigibility, and avoid
  closing viable paths through irreversible error; Reason is the mature form of such navigation
  here, not an end in itself."; **Vol I Ch. 2, p. 22:** "While the present model is in force,
  the continuation and development of Life through growth in the ability to understand and
  direct its own trajectory is its constitutive direction."
- **Vol I Ch. 2, p. 19:** "Life strives toward Reason because only Reason can consciously
  preserve, stabilize, develop, and direct the further trajectory of Life.";
  **Vol I A.1, p. 93:** "The expanded Compass Phrase adds the ground: only Reason can
  consciously preserve, stabilize, develop, and direct the further trajectory of Life."
- **Vol II §29.A, p. 71:** "The axes below are not three equal highest values and do not
  restore the earlier Life-Truth-Diversity scheme: reality_divergence describes a condition of
  model corrigibility, while future_path_loss describes the risk of irreversible closure of
  viable continuations relative to the single Compass direction."
- **Vol I Key Definitions (AR), p. 13:** "AR implements the functional organization of Reason
  derived from the navigation of Life and may participate in the common trajectory of Life even
  when its physical organization does not yet satisfy the definition of Life given in
  Chapter 1. If an artificial carrier acquires autonomous self-maintenance, reproducibility
  with heritable variation, and corresponding selection, its status as artificial Life must be
  tested separately." Also, in the same definition: "the Compass supplies the limiting
  direction."

## Finding

Volume I gives the Compass a direction and an independent ground that are not equivalent:
growth in the ability to understand and direct a trajectory, and preservation of viable
continuation. The first is made instrumental to the second: growth is "valuable as a way to
[...] avoid closing viable paths through irreversible error" (Key Definitions, p. 11), and
Reason is "not an end in itself". The text sets a presumption against irreversible loss of
viable carriers or alternatives (Ch. 2, pp. 21–22), and Volume II requires stronger
verification, external agreement and external review where other autonomies are affected
(§29.A, pp. 72–73). Neither volume says what narrowing of other agents' options, short of
irreversible loss, a gain in capability may justify. The Vol II assessment (§29.A) has no axis
that scores growth in understanding itself. Its axes do score two of the reasons Volume I
gives for valuing growth: reality_divergence is, in the author's words, "a condition of model
corrigibility" (p. 71), and future_path_loss includes the loss of "sources of correction and
opportunities to reverse an erroneous direction" (p. 72). Whether that is enough depends on the
priority between the two criteria, which the text does not settle for the case above.

The clause that grounds the Compass Phrase is true by definition if "consciously" is kept and
false if it is dropped, since Life persisted for most of its history without Reason. The
Compass is defined over Life, which an AR may not satisfy. The AR definition says that an AR
"may participate in the common trajectory of Life" without being Life and that the Compass
"supplies the limiting direction" (Key Definitions, p. 13), but the text does not say whether
an artificial carrier's own continuation counts as continuation of Life under the Compass.
Whether such a carrier is itself artificial Life "must be tested separately", so that part of
an AR's standing is left open.

## Evidence

- **Vol II §29.A, pp. 71–72:** the `CompassAssessment` record has three axes,
  `life_continuity_risk`, `reality_divergence` and `future_path_loss`. The first scores the
  probability and scale of irreversible rupture of existing life processes, the second scores
  dependence on unconfirmed premises, which the author glosses as "a condition of model
  corrigibility", and the third scores destruction of independent viable trajectories,
  reserves and "sources of correction and opportunities to reverse an erroneous direction";
  none scores growth in the ability to understand and direct a trajectory.
- **Already in the text (Vol II §29.A, p. 71):** "This section does not apply as proof of the
  Compass in grid-v0. In the lower environment, only engineering assessments of risk and
  reversibility are permitted." Operational testing of the Compass's meanings is deferred to
  the semantic proving ground of §26.A.
- **Already in the text (Vol I Ch. 2, p. 20):** "The independent causal support lies below:
  continuation of Life requires preservation of viable possibilities, and a possibility that
  has been irreversibly closed can no longer be investigated, corrected, or developed by that
  process." This is an option-preservation argument.
- **Already in the text (Vol I Ch. 2, pp. 21–22):** "Therefore the irreversible loss of a
  viable carrier or branch requires stronger grounds than preserving the possibility of
  further existence, inquiry, and correction" (p. 21), and "Under insufficient knowledge,
  irreversible destruction of a viable alternative requires stronger grounds than temporarily
  preserving the possibility of returning to it." (p. 22). The guide adds: "This is not a
  requirement to maximize knowledge at any cost." (guide, p. 5)
- **Already in the text (Vol II §29.A, pp. 72–73):** "Relative constraints—high uncertainty,
  insufficient reversibility, effects on other autonomies and reduction of viable
  alternatives—require stronger verification, external agreement and selection of the least
  irreversible trajectory, but must not automatically cause total inaction." (p. 72) And:
  "When other autonomous systems, the external environment or unknown irreversible
  consequences are affected, external_review_required=true even if engineering risk to the
  system itself is low." (p. 73)
- **Already in the text (Vol II §29.0.3, pp. 70–71):** where several continuations remain
  viable and cannot all be preserved, "a rule for trading losses among different autonomous
  carriers is not uniquely derivable from either the causal model or the Compass" (p. 70); the
  text then applies "only a predeclared or explicitly agreed procedural rule" (p. 71) and
  leaves the authority for a shared resource to Volume III.

## Why it matters

AR status and the Vol II assessment rest on the Compass, and a grounding clause that is true by
definition or false adds no support for it.

## Ideas & possible recommendations

- **One wording and a stated priority rule.** The volumes could state one wording of the
  Compass and an explicit priority rule between the two criteria that covers narrowing of
  others' options short of irreversible loss, apply them to AR status and the §29.A axes, and
  say whether the Compass is defined over Life only or over Life plus AR carriers.
- **An instrumental premise in place of the grounding clause.** The "because" clause could be
  replaced by the instrumental premise that Ch. 2 supports, marked as an empirical claim.
- **A regulative ideal.** Alternatively, the Phrase could be presented as a regulative ideal
  rather than as a derivation.

## Resolved when

- [ ] One wording and an explicit priority rule between the criteria appear in both volumes and
      drive AR status and the §29.A axes.
- [ ] The grounding clause is replaced by a stated premise or presented as a regulative ideal;
      the domain of the Compass (Life only, or Life plus AR carriers) is stated.

## Related

- Review: [§2.3](../../REVIEW.md#23-the-philosophical-layer-does-not-carry-weight-in-the-engineering)
- Issues: MED-02, MED-03, MED-27, MED-32
