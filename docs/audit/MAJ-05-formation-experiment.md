---
id: MAJ-05
title: The formation experiment cannot yet attribute internalization to the RFL
severity: major
area: testability
volumes: I, II
sections: Vol I §20.1.2, A.2.1; Vol II §26.0.2, §26.0.3, §28.C.3, §31.9, §33.A.8, §33.A.10
review: §4.2(a), §7
status: open
github_issue: 5
---

# MAJ-05 · The formation experiment cannot yet attribute internalization to the RFL

**Finding.** The formation programme stands on one transition: guidance first supplied by an
external Reason Formation Loop (RFL) must become the candidate's own, so that the RFL can be
removed without loss. Volume I designs a clean test (mentor-generated, automatic and absent
guidance from the start, then removal and held-out testing), and Volume II defines the three
possible outcomes without choosing among them. Three gaps keep the test from attributing a
result to the RFL. First, no learning rule is given: the text allows weights or adapters as
one substrate and rightly refuses to credit a mere parameter update as revision, but never
says what produces an internal `POSSIBLE_DANGER` or by which training signal. Second, Volume
II does not carry the Volume I design: it applies four support levels in sequence to one
candidate, drops the automatic arm, and redefines `NO_KSR` from "layer absent" to "disabled
during the control series", so no never-supported control remains. Third, the mentor ladder
lets the mentor supply the discriminating feature and causal explanations, so a mentor arm
that wins may be measuring tutoring, not pre-rational significance.

## Evidence

- **Vol I §20.1.2, p. 85:** arms `TRAINER_KSR`, `AUTO_KSR` and "NO_KSR: the additional guiding
  layer is absent except for necessary physical constraints of the Incubator", then removal
  and testing "on held-out new situations without current guiding assistance".
- **Vol II §26.0.3, p. 41:** "NO_KSR - the external RFL is disabled during the control
  series"; "Transfer of function is credited when NO_KSR preserves the required capability on
  held-out and new cases"; "the candidate should generate functional analogues itself: its
  own risk model creates an internal POSSIBLE_DANGER".
- **Vol II §26.0.2, p. 40:** mentor levels "L3 DISTINGUISH - propose a discriminating feature,
  counterexample, or frame change" and "L4 EXPLAIN - explain a causal relation".
- **Already in the text (Vol II §28.C.3, pp. 62–63):** "An ordinary parameter update does not
  yet count as revision of a ground or method"; "On a neural bearer, it may be implemented by
  changing a bounded set of weights or adapters, routing among specialized modules,
  external-memory structure".
- **Vol II §33.A.8, p. 104:** the builder is told to "Implement the heuristics" of the Core,
  which the Purpose says is "formed" through experience; what is built, written by the
  candidate or trained is not tabulated.

## Why it matters

"Technology" in the titles means cultivation, and this is its decisive step. A positive
result under the Volume II design could come from the base model's prior capability, from
learning that continues during staged removal, or from information the mentor leaked; none
of these can be excluded without the never-supported and information-matched arms.

## Recommendation

Restore the between-arm design at equal budget (mentor RFL, automatic RFL, none from the
start), with removal as a within-arm factor and a fixed non-inferiority margin. Add an
information-matched arm (the mentor's content supplied as a log, not as Formation States)
and split the ladder so that signal-only levels (L0–L2) test pre-rational significance.
Name the learning locus and rule for the first candidate (records, procedures or weights)
and give `NO_KSR` one meaning in both volumes.

## Resolved when

- [ ] Both volumes specify the same arms, including a never-supported control and an
      information-matched control.
- [ ] The first candidate's internalization mechanism (where learning happens, by what rule
      or signal) is stated.

## Related

- Review: [§4.2(a)](../../REVIEW.md#42-toward-a-system-with-its-own-worldview-and-values-underspecified-at-the-decisive-step)
- Issues: MED-01 (pre-rational significance), MED-07 ("own" Worldview), MED-29 (Formation
  State classes), MIN-05 (KSR)
