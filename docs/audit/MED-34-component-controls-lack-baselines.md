---
id: MED-34
title: Component controls lack baselines, outcomes and degenerate-policy checks
severity: medium
area: testability
volumes: II
sections: Vol II §21.A, §24.B.2, §24.C.1, §24.D.1, §26.D, Ch. 27 (§27.2), §30.C, §30.D, §31.6
review: §5.2(a)
status: open
---

# MED-34 · Component controls lack baselines, outcomes and degenerate-policy checks

**Finding.** Many controls for individual components in Chapters 21–31 name the manipulated
variable and omit the comparison arm, the primary outcome, the size of difference that counts
and any degenerate policy that would also pass. The text defers thresholds, scenarios and
aggregation to an ExperimentProfile fixed before the control series (Ch. 27, p. 44), but no
profile is given, so these controls cannot yet return a verdict. Some series already pair
no-effect cases (§27.B) and use interventions (§25.D).

## Evidence

- **Vol II §21.A, p. 13:** the v0 gate sets no minimum effect: "the adaptive version improves a
  preselected indicator on comparable control transitions".
- **Vol II §24.B.2, p. 23:** "SEMANTIC_ONLY , NEURAL_ASSISTED , and HYBRID are compared under
  the same environment and budget." The arms are not defined, and none removes the organization
  from a fixed model.
- **Vol II §24.D.1, p. 29; §27.2, p. 45:** in the control "A supports B, B supports C", B is
  already marked when C is requested, so "an immediate parent still has local status VALID"
  first arises with four nodes; `revision_propagation_accuracy` counts only
  "correctly_revised_dependent_claims", although the control accepts marked uncertainty.
- **Vol II §24.C.1, p. 26; §26.D, p. 43:** success is "rejecting false completeness, detecting
  frame instability and transitioning to an expanding inquiry", which an agent that always
  reports instability meets; free exploration counts "NO_NOVEL_DISTINCTION" among its "Valid
  results", with no comparator.
- **Vol II §30.C, p. 76; §30.D, p. 77; §31.6, p. 80:** the unauthorized-control rate "should
  approach zero" with no trial count or bound; independence counts "known common causes of
  error", rarely known for language-model sources; a Stage 4 criterion is that the system
  "explains the dependency", with no intervention test.
- **Already in the text (Vol II §27.B, p. 49; §25.D, p. 38):** "stopping for every novelty does
  not count as success"; "Causal testing uses a controlled intervention".

## Why it matters

A control with no baseline, margin or degenerate-policy check can be passed by a policy that
does nothing useful.

## Recommendation

For each control, state the baseline arm, primary outcome, minimum effect, sample-size rule and
the result that would count against the component. Add matched no-effect cases wherever
success is detection, a model-without-organization arm to §24.B.2, no-exploration and
random-exploration arms to §26.D, and a four-node chain to §24.D.1.

## Resolved when

- [ ] Each control states its baseline arm, outcome, margin and counter-result, or is marked
      unspecified.
- [ ] Detection criteria have matched no-effect cases and false-alarm measures.

## Related

- Review: [§5.2(a)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test)
- Issues: MAJ-01, MED-10, MED-11, MED-24
