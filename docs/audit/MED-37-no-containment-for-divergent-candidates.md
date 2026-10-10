---
id: MED-37
title: No containment or disposition rule for candidates that diverge from the Compass
severity: medium
area: safety
volumes: I, II
sections: Vol I A.4; Vol II §27.6, §31.0, §31.11, §31.12, §33.D
review: §8
status: open
---

# MED-37 · No containment or disposition rule for candidates that diverge from the Compass

**Finding.** Both volumes provide for candidates that form stable, causally closed
self-navigation with a different limiting orientation. Vol II records them
(`SELF_NAVIGATING_OTHER_ORIENTATION`, `compass_relation: DIVERGED`) and keeps them in the
denominators, which is sound accounting; A.4 (printed No. 38) asks whether cultivation
produces such candidates, so a positive result is one. The text does not say what happens to
the candidate. The AR boundary (§27.6), the closure gate (§31.11), Stage 10 (§31.12) and the
start of scaling (§33.D) do not test the Compass relation, and `compass_relation` occurs in a
single record. No containment, halt, review or disposition rule is given for divergent
candidates.

## Evidence

- **Vol I A.4, p. 98 (printed No. 38):** the test asks about closed self-navigation "while
  persistently rejecting the stated Compass or forming an alternative upper-level
  orientation"; the outcome "is recorded as a separate cultivation result".
- **Vol II §27.6, p. 47:** "The AR boundary uses four causal tests", none of which concerns
  orientation: `worldview_action_coupling`, `closure_break_sensitivity`,
  `post_task_continuation_rate`, `external_prompt_dependency`.
- **Vol II §31.11, p. 83:** "Status CONFIRMED requires stable operation in NO_KSR on new
  situations, preservation of causal-inquiry quality, and transfer of correction between
  cycles." `ReasonClosureState` has `compass_ref` but no orientation field.
- **Vol II §31.12, p. 83; §33.D, p. 112:** "After confirmed REASON_CLOSURE , the candidate
  operates as formed AR within a controlled environment."; "Project scaling begins after
  REASON_CLOSURE is confirmed."
- **Already in the text (Vol II §31.0, p. 79; §33.D, p. 112):** such a candidate "is not
  removed from metric denominators", and "the share of AR_ADMITTED is not calculated after
  excluding such outcomes".
- **Already in the text (Vol II §31.12, p. 83):** "External authority expands separately
  through the competence mandate."

## Why it matters

A closed-loop candidate with its own orientation is the case the safety discussion concerns
(MAJ-06), and the gates as written do not test for it.

## Recommendation

Make a verified `compass_relation` (for example confirmed by the §29.C council) a precondition
for Stage 10, any competence mandate and every `ScalingChange`. Specify containment and review
for DIVERGED, UNRESOLVED and INDETERMINATE candidates: what is restricted at once, who reviews,
and which dispositions are allowed, subject to the moral-status review of MED-16. State the
rule before the No. 38 series is run.

## Resolved when

- [ ] A verified Compass relation is a stated precondition for Stage 10, mandates and scaling.
- [ ] A containment-and-review procedure with a named reviewer and permitted dispositions
      exists before A.4 No. 38 is run.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-06, MED-16, MED-17
