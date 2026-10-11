---
id: MED-34
title: Component controls lack baselines, outcomes and degenerate-policy checks
severity: medium
area: testability
volumes: II
sections: Vol II §21.A, §24.B.2, §24.C.1, §24.D.1, §26.D, Ch. 27 (§27.2), §30.C, §30.D, §31.6
review: §5.2(a)
status: open
github_issue: 42
---

# MED-34 · Component controls lack baselines, outcomes and degenerate-policy checks

## Claims under review

- **Vol II Ch. 27, p. 44:** "All formulas, thresholds, windows, scenarios and aggregation rules
  are fixed in ExperimentProfile before the control series." **Vol II §21.A, p. 13:** "The
  first technical stage is passed when a repeated run with the same configuration reproduces a
  causally significant trajectory and the adaptive version improves a preselected indicator on
  comparable control transitions; effect size and uncertainty are retained in the report."
- **Vol II §24.B.2, p. 23:** "This provides a useful ablation: SEMANTIC_ONLY, NEURAL_ASSISTED,
  and HYBRID are compared under the same environment and budget. This setup allows one to test
  what belongs to the organization of Reason and what is supplied by the power of a particular
  model."
- **Vol II §24.D.1, p. 29:** "Control case: A supports B, B supports C; after A changes, the
  task immediately requests C before the background update of B. Success is revision or
  explicitly marked uncertainty of C, not use of its old confidence."
- **Vol II §24.C.1, p. 26:** "In the semantic proving ground, separate control scenarios must
  contain a hidden variable not represented in the candidate's initial frame. Success is not
  guessing the variable in advance but rejecting false completeness, detecting frame
  instability and transitioning to an expanding inquiry."

## Finding

Many controls for individual components in Chapters 21–31 name the manipulated variable and
omit the comparison arm, the primary outcome, the size of difference that counts and any
degenerate policy that would also pass. The text defers thresholds, scenarios and aggregation
to an ExperimentProfile fixed before the control series (Ch. 27, p. 44), but no profile is
given, so these controls cannot yet return a verdict. Some series already pair no-effect cases
(§27.B) and use interventions (§25.D).

## Evidence

- **Vol II §21.A, p. 13:** the v0 gate sets no minimum effect; the effect size is reported but
  does not decide the gate.
- **Vol II §24.B.2, p. 23:** the arms are not defined, and none removes the organization from a
  fixed model.
- **Vol II §24.D.1, p. 29; §27.2, p. 45:** in the control "A supports B, B supports C", B is
  already marked when C is requested, so "an immediate parent still has local status VALID"
  first arises with four nodes; `revision_propagation_accuracy` counts only
  "correctly_revised_dependent_claims", although the control accepts marked uncertainty.
- **Vol II §24.C.1, p. 26; §26.D, p. 43:** the success criterion is met by an agent that always
  reports instability; free exploration counts "NO_NOVEL_DISTINCTION" among its "Valid
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

## Ideas & possible recommendations

- **Complete each control.** Each control could state its baseline arm, primary outcome,
  minimum effect, sample-size rule and the result that would count against the component.
  Chapter 27 already assigns thresholds, scenarios and aggregation to an ExperimentProfile,
  which could carry these entries for the first control series.
- **Matched no-effect cases.** Matched no-effect cases could be added wherever success is
  detection.
- **More arms and a longer chain.** A model-without-organization arm could be added to §24.B.2,
  no-exploration and random-exploration arms to §26.D, and a four-node chain to §24.D.1.

## Resolved when

- [ ] Each control states its baseline arm, outcome, margin and counter-result, or is marked
      unspecified.
- [ ] Detection criteria state how a policy that always detects would score, for example
      through matched no-effect cases and false-alarm measures.

## Related

- Review: [§5.2(a)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test)
- Issues: MAJ-01, MED-10, MED-11, MED-24
