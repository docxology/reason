---
id: MED-05
title: Intelligence and the Core's regulation of inquiry are roles, not kinds, and the boundary belongs across episodes
severity: medium
area: definitions
volumes: I, II
sections: Vol I front matter, Key Definitions, §7.2, §7.3, §13.1; Vol II §27.6, §28.C.2, §31.11, §31.A
review: §3
status: open
github_issue: 13
---

# MED-05 · Intelligence and the Core's regulation of inquiry are roles, not kinds, and the boundary belongs across episodes

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
The volumes already treat it as a distinction of function, not of kind. Vol I §13.1 says that
"Intelligence and Reason are distinguished by functional role". Vol I §7.3 and Vol II §28.C.2
allow one mechanism to take part in both construction (Intelligence) and the regulation of
inquiry (the Core), and §28.C.2 adds the condition that "the causal roles are experimentally
distinguishable". Test results apply to a system boundary declared in advance (Vol I §7.2 and
§13.1). Reason as a whole is wider than the Core: it is defined as a navigational structure, and
an LLM or planner "by itself does not constitute Reason" (Vol I, AR entry, p. 13).

A frontier reasoning model that selects informative questions within an episode already does the
within-episode part of what the Core does. The distinction does its real work across episodes
(corrections that persist, calibrated sufficiency, the next task originating from the system's
own open commitments), and the volumes say so: §13.1 states that "Confirmation requires
subsequent cases", other Key Definitions entries define related properties, the abstract of
Volume I predicts a difference there, and Volume II rests its AR boundary on tests of this kind
and calls the origin of the next process the decisive marker (Evidence). The boundary sentence of
the Intelligence entry (first claim above) does not point to them. It puts the boundary in "who
determines what should be revised, why, and on what grounds relative to the continuing
trajectory", which is hard to apply when one model fills both roles unless the roles are made
experimentally distinguishable (§28.C.2).

## Evidence

- **Already in the text (Vol I §13.1, p. 62):** "Intelligence and Reason are distinguished by
  functional role. The same computational mechanism can solve a domain task and then participate
  in testing the way that task was framed." "The system boundary is functional and is defined
  before the test." On within-episode success, "Successful action under uncertainty alone does
  not distinguish Reason from powerful Intelligence"; on persistence of corrections,
  "Confirmation requires subsequent cases: the changed ground must actually influence choice".
- **Already in the text (Vol I Key Definitions, pp. 11–12):** Self-navigation is the system's
  ability, "from its own current state, Worldview, open commitments, and significant gaps, to
  independently determine the next justified investigative or practical step [...] without
  requiring a new specific command from outside" (p. 11). A correction counts as stable "when the
  cause reproducing the error has been removed and this is confirmed by transfer of the
  correction to a new situation" (Principle of escaping error, p. 12). The Core of Reason manages
  inquiry by, among other things, "assessing whether the grounds are sufficient" (p. 12).
- **Already in the text (Vol I abstract, p. 8; Vol II §27.6, p. 47; §31.11, p. 82):** the
  predicted difference is "not so much in the quality of a single answer as in the system's
  ability to independently detect a significant insufficiency, select a discriminating test,
  revise the ground that produced the error, and transfer the corrected method of inquiry across
  tasks"; "The AR boundary uses four causal tests", two of which (`post_task_continuation_rate`
  and `external_prompt_dependency`) concern what the system does between particular tasks; and
  "The decisive marker is the origin of the next process."
- **Already in the text (Vol II §31.11 and §31.A, pp. 83–84):** closure is a four-valued status
  (`FORMING / CANDIDATE / CONFIRMED / LOST`), and `CONFIRMED` "requires stable operation in
  NO_KSR on new situations, preservation of causal-inquiry quality, and transfer of correction
  between cycles". Separately, §31.A defines a `ReadinessProfile` of `minimum_*` and `maximum_*`
  thresholds (for example `maximum_premature_sufficiency_rate` and
  `minimum_correction_persistence`) that is "published before results are examined"; the text
  does not say that the closure status is computed from it, and calls the profile "not a
  universal scale of Reason".

## Why it matters

If the Intelligence entry is read as drawing the boundary within an episode, current models
already cross it and the distinction loses its power to discriminate. Drawn across episodes, it
names something current evaluations rarely measure. The ReadinessProfile already fixes
preregistered thresholds on mostly continuous measures, but the text does not link it to the
closure label; reporting the label rather than the profile scores would hide partial progress
and regressions.

## Ideas & possible recommendations

- **Use the criterion the tests actually use.** The definition could replace "who determines"
  with that criterion: which component's output fixes the next question when the two are made
  separately intervenable. §31.11 already calls "the origin of the next process" the decisive
  marker (p. 82), and §28.C.2 ties the boundary to roles that are experimentally distinguishable.
- **Place the boundary across episodes.** Cross-episode properties could be named in the
  Intelligence entry as the explicit location of the boundary: corrections that persist,
  calibrated sufficiency, and the next task originating from the system's own open commitments.
- **Report the profile first.** Results could present the ReadinessProfile scores as the primary
  result, with the closure label derived from them by a stated rule.
- **Use the Reason metrics as a benchmark.** The metrics proposed for Reason
  (`premature_sufficiency_rate`, `decision_relevant_distinction_yield`,
  `correction_persistence_rate`, `false_completeness_rate`, `open_gap_persistence`,
  `post_task_continuation_rate`) could form a benchmark suite in their own right.

## Resolved when

- [ ] The volumes state that Intelligence (construction) and the Core (regulation of inquiry) are
      causal roles, and the Intelligence entry locates the boundary in cross-episode properties.
- [ ] Results report the ReadinessProfile scores, not only the closure status.

## Related

- Review: [§3](../../REVIEW.md#3-is-the-intelligencereason-distinction-meaningful-and-useful)
- Issues: MED-03 ("Reason" overloaded), MED-25 (Core ablation)
