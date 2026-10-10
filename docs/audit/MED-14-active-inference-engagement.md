---
id: MED-14
title: Active inference, the closest formal competitor, is engaged only in an appendix
severity: medium
area: prior-art
volumes: I, II
sections: Vol I A.5 (item 63 and the comparative map); Vol II (absent)
review: §6.1
status: open
---

# MED-14 · Active inference, the closest formal competitor, is engaged only in an appendix

**Finding.** Active inference maps closely onto the architecture: the Worldview and
Self-Model onto a generative model with self-states; the Current Coordinate onto the posterior
over current hidden states; attention onto precision; test selection onto the epistemic term
of expected free energy; Factor X and model expansion onto structure learning and Bayesian
model expansion and reduction; Formation States onto affective precision or valence signals;
metathinking onto deep parametric models of meta-awareness. Volume I's A.5 annotates the
process-theory paper and gives active inference a row in its comparative map, naming what
remains a separate claim and a control. None of the chapters of either volume mentions it, and
Volume II never does. The two frameworks also differ in ways that generate experiments, which
the volumes do not exploit.

## Evidence

- **Vol I A.5, item 63, p. 101:** Friston et al. (2017), *Active Inference: A Process Theory*:
  "This is a close alternative for organizing epistemic search; its relation to the author's
  Compass is a separate level of comparison."
- **Already in the text (Vol I A.5, p. 104):** a comparative-map row headed "Active inference / epistemic [...]
  action" (the cell is split across lines).
- An exhaustive search finds "active inference" twice in Volume I (both in A.5) and never in
  Volume II.

## Why it matters

Active inference offers what the Core lacks (MAJ-03): one objective that trades epistemic
against pragmatic value without extra parameters, and model evidence as a principled criterion
for revising a frame. The volumes offer what active inference lacks: provenance and
status-promotion rules, typed non-informational gaps (authority, criterion, normative
incomparability) and transactional revision. The disagreement is testable: in active inference
epistemic value is intrinsic, so an expected-free-energy agent should spend more on salient
uncertainty that no decision depends on; the volumes predict less, plus a bounded exploration
budget. The attention-capture scenario of §26.E is a ready-made testbed. The free-energy
principle is descriptive, while the Compass is prescriptive; the two should be kept apart.

## Recommendation

Compare the Core with active inference in Chapters 12 and 28, include an active-inference agent
(for example built with `pymdp`, Heins et al. 2022) as a strong null or as a candidate formal
backbone, and run the §26.E attention-capture scenario as a discriminating experiment between
decision-relative and intrinsic epistemic value.

## Resolved when

- [ ] The chapters compare the Core with active inference component by component.
- [ ] An active-inference agent appears among the strong nulls or the discriminating
      experiments.

## Related

- Review: [§6.1](../../REVIEW.md#61-active-inference-specifically)
- Issues: MAJ-03, MAJ-07
