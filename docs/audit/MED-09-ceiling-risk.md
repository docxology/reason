---
id: MED-09
title: The first environment risks a ceiling effect, and no external benchmark is planned
severity: medium
area: testability
volumes: I, II
sections: Vol I §12.9, A.4; Vol II §27.B, §33.C.1
review: §5.2(b), §10.2
status: open
github_issue: 17
---

# MED-09 · The first environment risks a ceiling effect, and no external benchmark is planned

## Claims under review

- **Vol I A.4, p. 99:** "For an initial test, a digital environment based on the example in
  §12.9 is sufficient."
- **Vol I A.4, p. 100:** "The first task is to localize the cause of a mismatch among model,
  measurement, and execution. The second is to transfer the method of distinction to a
  substantively different domain and reject a false analogy."
- **Vol II §27.B, p. 49:** "The first discriminating series for this implementation tests a
  narrow claim: does organizing the gap, test and transfer of correction help localize
  insufficiency of a ground and improve the next choice?"

## Finding

The base D/A/S world has three causes and two informative probes; it is solved by a decision
tree of depth two and is textbook model-based diagnosis, so any competent language-model agent
will solve it. The volumes treat it as infrastructure and an oracle reference, and the design
already contains the variations where organization should matter: a receipt for another
command, a delayed measurement, an unreliable source, a hidden cause that mimics a known one, a
tool change that invalidates a load model, and paired no-effect cases. Three things are
missing. The text never says which series carries the headline comparison; the perturbation
families are described in a sentence each, with no generator, parameters or instance counts; and
Volume I declares the single §12.9 world sufficient for a first series that must also test
transfer "to a substantively different domain", which one world cannot do. No external
benchmark is mentioned anywhere.

## Evidence

- **Vol II §27.B, p. 49:** "An independent delivery receipt costs 1 unit and returns 0 only for
  D. An independent state measurement costs 2 units and returns 1 only for S. When both tests
  are available, the pairs of observations distinguish all three causes."
- **Already in the text (Vol II §27.B, p. 49):** "A separate series changes one premise: the
  receipt concerns another command, measurement is delayed, or the source itself is
  unreliable"; the exhaustive controller "provides a reference for attainable cost, not a
  deliberately weak opponent".
- The restored §33.C.1 listing solves the base case at an expected cost of 7/3 by exact search
  over 8 belief states (`repro/diagnostic_cycle.py`).

## Why it matters

A ceiling effect would produce a null result that says nothing about the hypothesis, or a small
difference driven by prompt formatting. The perturbation families are where the organization
should help, and an external benchmark is what makes a positive result credible outside the
programme.

## Ideas & possible recommendations

- **Make the perturbation families the primary series.** The perturbation and hidden-cause
  families, where organization should matter, could carry the headline comparison, with the base
  world kept as infrastructure and an oracle reference.
- **Add an explicit generator.** A generator that scales to k components and m probes, with
  costs, unreliable channels and delays, would give the families stated parameters and instance
  counts.
- **Render each structure in several surface skins.** The same structure could be presented in
  several surface descriptions to test transfer and false analogy.
- **Add an external benchmark.** At least one external benchmark of interactive experimentation
  or diagnosis (for example BoxingGym, DiscoveryWorld, ScienceWorld, ARC-AGI-3, or an agentic
  root-cause-analysis benchmark) would make a positive result comparable with other work.

## Resolved when

- [ ] The series that carries the headline comparison has a stated generator, parameters and
      instance counts, and a difficulty range shown to leave headroom for a strong baseline.
- [ ] At least one external benchmark is included.

## Related

- Review: [§5.2(b)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test),
  [§10](../../REVIEW.md#10-ideas--possible-recommendations)
- Issues: MAJ-01, MED-11
