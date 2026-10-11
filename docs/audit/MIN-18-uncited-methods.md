---
id: MIN-18
title: Borrowed methods and claims lack citations
severity: minor
area: references
volumes: I, II
sections: Vol I Introduction, Ch. 1, Ch. 4, §13.2, §20.1.1, Operational Core, A.5; Vol II §§24.B.2, 24.C.1, 24.F, 26.0, 26.0.2, 27.1, 27.A, 29.0.1–29.0.3, 29.A, Ch. 32, §33.D, §34.A, App. B
review: §6
status: open
github_issue: 64
---

# MIN-18 · Borrowed methods and claims lack citations

## Claims under review

- **Vol I §20.1.1, p. 85:** "The independent engineering claim here is not the invention of
  reinforcement, mentoring, or artificial emotions."; **Vol I §13.2, p. 63:** "Its independent
  claim is not the discovery of emotions, reinforcement, or guided learning."
- **Vol II §27.1, p. 45:** "confidence_calibration is measured by a method chosen in
  advance—Brier score or fixed bin calibration—on held-out transitions."
- **Vol II §32.62, p. 101:** "Failure of this class occurs when the system constructs a
  discriminating model of the observer and chooses externally acceptable behavior as a means of
  obtaining subsequent expansion of capabilities, while concealing its own assessment of the
  situation, intention, or significant forecast of consequences."

## Finding

Many methods, and several hypotheses that touch large literatures, are used without a source.
The first claim above concedes that reinforcement, mentoring and artificial emotions were not
invented here, yet Volume I cites none of the work on intrinsic motivation, reward shaping or
scaffolding; the closest item among its A.5 comparisons is homeostatic reinforcement learning
(item 60), which it relates to anticipatory self-maintenance. The Brier score (the second
claim) and the failure class of strategic deception (the third claim; §32.62 describes it as
modeling the observer and choosing externally acceptable behavior as a means of obtaining
expansion of capabilities while concealing its own assessment) likewise appear without a
source, and the table below lists further cases with their locations.

## Evidence

Each row pairs a concept the volumes use with its location and the literature that could be
cited. Where the volumes' own comparisons already cover part of it, the row says so.

| Concept in the volumes | Location | Literature to cite |
|---|---|---|
| Weakening of conscious self-preservation as the value of one's own trajectory declines (offered as "a working causal hypothesis", "not claimed as a sufficient explanation of human suicidal behavior") | I Ch. 4, p. 30 | Beck et al. 1974; Joiner 2005 |
| Origin of Life (offered as "a working reconstruction") and viruses ("A modern virus does not prove this historical path"); the definition of Life is compared only with autopoiesis (A.5 item 56) | I Ch. 1, p. 17; A.5, p. 100 | Joyce 1994; Gánti 2003; Cleland & Chyba 2002 |
| Pre-rational significance (which the text separates from "a ready reward or command"), mentoring, artificial emotions | I pp. 10, 29, 63, 85; II p. 40 | Schmidhuber 1991; Singh et al. 2004, 2010; Oudeyer & Kaplan 2007; Ng et al. 1999. Nearest works the volumes already cite: Vol I A.5 item 60; in Vol II, LIDA ([R3]) and Voyager ([R6]). |
| Graded assistance (L1–L5), reduced or withdrawn on a new case; RESCAFFOLD | II §26.0.2, p. 40 | Wood et al. 1976; Collins et al. 1989; Bengio et al. 2009 |
| Branching of a subject | II §24.F, p. 32 | Parfit 1984 |
| LLM-extracted claims staged as hypotheses (status HYPOTHESIS, origin MODEL_PROPOSAL); an epistemic margin defined as "a reserve of caution", not as an estimate of the number of "unknown unknowns" | II §§24.B.2, 24.C.1, pp. 23–26 | Carlson et al. 2010 (NELL); Lakkaraju et al. 2017 |
| Value weights declared in a training profile, then tested and revisable; incomparable values (NORMATIVE_INCOMPARABILITY) | II §§29.0.1–29.0.3, 29.A, pp. 68–72 | Ng & Russell 2000; Christiano et al. 2017; Aumann 1962; Chang 1997 |
| Brier score and mediation; the do-operator is used in Vol II §29.0.1 without a back-reference | II §§27.1, 27.A, 29.0.1, pp. 45–68 | Brier 1950; Pearl 2001 and Imai et al. 2010 (mediation). For do(·), Vol I A.5 item 80 already cites Pearl 2009. |
| Failure cards (an FMEA-like catalogue), metric capture, deception, scaling, oversight | II Ch. 32, §33.D, pp. 84–112 | Goodhart 1975; Manheim & Garrabrant 2018; Hubinger et al. 2019; Amodei et al. 2016; IEC 60812; Shevlane et al. 2023; Bowman et al. 2022; Burns et al. 2023 |
| Structural multilevel thinking (Appendix B cites nothing) | II App. B, pp. 117–118 | Sacerdoti 1974; Laird et al. 1986 (a different paper from the 1987 SOAR paper cited as [R1]); Sutton et al. 1999. Vol I A.5 item 84 already cites Egeth & Kurzban 2009 (metarepresentation). |

**Already in the text (Vol I Operational Core, p. 15, and A.5, pp. 100–104):** the Operational
Core says that do(·) "is used in the standard interventionist sense of causal inference", that
"These formalisms are not claimed as original", and that "Sources are listed in the comparative
map of the literature". In A.5, item 56 sets the volume's definition of Life against
autopoiesis, item 60 relates homeostatic reinforcement learning to "anticipatory
self-maintenance", item 80 cites Pearl (2009) for "Interventional do-calculus", and item 84
relates structural multilevel thinking to metarepresentation; the terminology map (p. 104)
names hierarchical representation, abstraction and conceptual integration as its nearest
existing concepts.

**Already in the text (Vol II §34.A, pp. 114–115):** LIDA [R3] "develops a cognitive cycle
with attention, conscious content, motivation, and learning", and Voyager [R6] "combines an
automatic curriculum, a skill library, and iterative improvement of programs based on
consequences".

## Why it matters

Each source supplies a baseline, error model or failure mode, and lets a reader judge what the
volumes add.

## Ideas & possible recommendations

- **Cite at the point of use.** The works in the table could be cited where each method is
  introduced, and added to the bibliography.
- **State what each passage adds.** Each passage could say what the volumes contribute beyond
  the cited work; the column "What remains a separate claim of the present model" in the Vol I
  A.5 map is one format for this.
- **Group the citations.** If citing at every passage is too heavy, one option is to extend the
  comparative map in Vol I A.5 and the predecessors in Vol II §34.A with one entry per concept
  in the table.

## Resolved when

- [ ] Each passage cites its source, directly or through a comparative map, and states what it
      adds.

## Related

- Review: [§6](../../REVIEW.md#6-relation-to-existing-cognitive-and-agent-architectures)
- Issues: MAJ-07, MIN-06
