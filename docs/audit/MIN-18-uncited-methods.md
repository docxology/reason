---
id: MIN-18
title: Borrowed methods and claims lack citations
severity: minor
area: references
volumes: I, II
sections: Vol I Introduction, Ch. 1, Ch. 4, §13.2, §20.1.1; Vol II §§24.B.2, 24.C.1, 24.F, 26.0, 26.0.2, 27.1, 27.A, 29.0.1–29.0.3, Ch. 32, §33.D, App. B
review: §6
status: open
github_issue: 64
---

# MIN-18 · Borrowed methods and claims lack citations

**Finding.** Many methods and empirical claims are used without a source. Volume I says its claim
is "not the invention of reinforcement, mentoring, or artificial emotions" (§20.1.1, p. 85) but
cites none of the work on intrinsic motivation, reward shaping or scaffolding.

## Evidence

| Concept in the volumes | Location | Literature to cite |
|---|---|---|
| Loss of the will to live | I Ch. 4, p. 30 | Beck et al. 1974; Joiner 2005 |
| Definition and origin of Life; viruses | I Ch. 1, p. 17 | Joyce 1994; Gánti 2003; Cleland & Chyba 2002 |
| Reward-like significance, mentoring, artificial emotions | I pp. 10, 63; II p. 40 | Schmidhuber 1991; Singh et al. 2004, 2010; Oudeyer & Kaplan 2007; Ng et al. 1999 |
| Graded assistance with fading; RESCAFFOLD | II §26.0.2, p. 40 | Wood et al. 1976; Collins et al. 1989; Bengio et al. 2009 |
| Branching of a subject | II §24.F, p. 32 | Parfit 1984 |
| LLM-extracted beliefs; unknown unknowns | II §§24.B.2, 24.C.1, pp. 23–26 | Carlson et al. 2010 (NELL); Lakkaraju et al. 2017 |
| Learned weights; incomparable values | II §§29.0.2–29.0.3, p. 70 | Ng & Russell 2000; Christiano et al. 2017; Aumann 1962; Chang 1997 |
| Brier score, do-operator, mediation | II §§27.1, 27.A, 29.0.1, pp. 45–68 | Brier 1950; Pearl (do-operator; mediation, 2001); Imai et al. 2010 |
| Failure cards (FMEA), metric capture, deception, scaling, oversight | II Ch. 32, §33.D, pp. 84–112 | Goodhart 1975; Manheim & Garrabrant 2018; Hubinger et al. 2019; Amodei et al. 2016; IEC 60812; Shevlane et al. 2023; Bowman et al. 2022; Burns et al. 2023 |
| Structural multilevel thinking | II App. B, pp. 117–118 | Sacerdoti 1974; Laird et al. 1986; Sutton et al. 1999 |

## Why it matters

Each source supplies a baseline, error model or failure mode, and lets a reader judge what the
volumes add.

## Recommendation

Cite these works where each method is introduced, add them to the bibliography, and state what
each passage adds.

## Resolved when

- [ ] Each passage cites its source and states what it adds.

## Related

- Review: [§6](../../REVIEW.md#6-relation-to-existing-cognitive-and-agent-architectures)
- Issues: MAJ-07, MIN-06
