---
id: MED-05
title: Intelligence and Reason are roles, not kinds, and the boundary belongs across episodes
severity: medium
area: definitions
volumes: I, II
sections: Vol I Key Definitions, §7.2, §7.3; Vol II §28.C.2, §31.11, §31.A
review: §3
status: open
github_issue: 13
---

# MED-05 · Intelligence and Reason are roles, not kinds, and the boundary belongs across episodes

## Claims under review

- **Vol I Key Definitions (Intelligence), p. 11:** "the boundary with Reason does not lie in the
  mere capacity to revise, but in who determines what should be revised, why, and on what
  grounds relative to the continuing trajectory."
- **Vol II §28.C.2, p. 61:** "Generation and control may therefore use the same computational
  substrates and even one model if the causal roles are experimentally distinguishable."
- **Vol I §7.3, p. 37:** "One mechanism may both construct alternatives and participate in
  selecting the next question."
- **Vol I §7.2, p. 37:** "Three roles occupy different causal positions. Resident Intelligence
  continuously constructs alternatives inside the AR candidate. An external tool provides a
  separate result through an observable interface. A trainer helps assemble and teach the
  candidate until the required autonomy appears. The same technology may be used in all three
  roles; test results apply to the system boundary declared in advance."

## Finding

Stated narrowly, the Intelligence/Reason distinction is the most useful idea in the series:
generating solutions within a frame versus regulating which questions are worth asking, which
distinction a decision depends on, when the ground is sufficient and how corrections persist.
Both volumes allow one model to play both roles (Vol I §7.3, Vol II §28.C.2) and make the
verdict depend on a system boundary declared in advance (Vol I §7.2), so these are causal
roles, not kinds of system. A frontier reasoning model that selects informative questions
within an episode already does what Reason does, within that episode. The distinction does its
real work across episodes (corrections that persist, calibrated sufficiency, the next task
originating from the system's own open commitments), and the Key Definitions do not put the
boundary there. They put it in "who determines what should be revised", which a single model
cannot settle.

## Evidence

- **Already in the text (Vol II §31.11 and §31.A, pp. 83–84):** closure is a four-valued status
  (`FORMING / CANDIDATE / CONFIRMED / LOST`), and `CONFIRMED` is tied to a `ReadinessProfile` of
  minimum and maximum thresholds on continuous metrics, "published before results are examined".

## Why it matters

If the boundary is drawn within an episode, current models already cross it and the
distinction loses its power to discriminate. Drawn across episodes, it names something
current evaluations rarely measure. The ReadinessProfile already makes closure a threshold on
continuous measures; reporting the label rather than the profile would hide partial progress
and regressions.

## Ideas & possible recommendations

- **Use the criterion the tests actually use.** The definition could replace "who determines"
  with that criterion: which component's output fixes the next question when the two are made
  separately intervenable. §28.C.2 already ties the boundary to roles that are experimentally
  distinguishable.
- **Place the boundary across episodes.** Cross-episode properties could be named as the
  explicit location of the boundary: corrections that persist, calibrated sufficiency, and the
  next task originating from the system's own open commitments.
- **Report the profile first.** Results could present the continuous ReadinessProfile scores as
  the primary result, with the closure label derived from them.
- **Use the Reason metrics as a benchmark.** The metrics proposed for Reason
  (`premature_sufficiency_rate`, `decision_relevant_distinction_yield`,
  `correction_persistence_rate`, `false_completeness_rate`, `open_gap_persistence`,
  `post_task_continuation_rate`) could form a benchmark suite in their own right.

## Resolved when

- [ ] The volumes state that Intelligence and Reason are causal roles and locate the
      boundary in cross-episode properties.
- [ ] Results report the ReadinessProfile scores, not only the closure status.

## Related

- Review: [§3](../../REVIEW.md#3-is-the-intelligencereason-distinction-meaningful-and-useful)
- Issues: MED-03 ("Reason" overloaded), MED-25 (Core ablation)
