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
tree of depth two and is textbook model-based diagnosis, so a competent language-model agent
can be expected to solve it. Volume I already names such an agent stack as the strong null and
says that if it reproduces the full causal profile of inquiry obligations, "the necessity of
the author's decomposition is then not established" (A.4, p. 100). The volumes use the world as
the environment of the first series (§27.B, p. 49) and, in the §33.C.1 listing, as a
deterministic check of the mechanism (p. 111), with an exhaustive controller as the reference
for attainable cost. They also specify the variations where organization should matter: a
receipt for another command, a delayed measurement, an unreliable source, a hidden cause that
mimics a known one (the "next mandatory version" of the diagnostic test, §33.C.1, p. 111), a
tool change that invalidates a load model, and paired no-effect cases.

Three things are missing. First, §27.B names a principal outcome for the first series (p. 50),
which rests on the small three-cause environment and its variants without an independent
measurement, while the premise changes are introduced as "A separate series changes one
premise" (p. 49); the text never says that the perturbation families carry the headline
comparison. Second, the perturbation families are described in a sentence or a short paragraph
each; the profile has slots for a family generator, data splits and a pilot-sized series, but
no generator, parameters or instance counts are given. Third, Volume I calls "a digital
environment based on the example in §12.9" (A.4, p. 99) sufficient for an initial test, while
the same first series also includes transfer "to a substantively different domain" (p. 100);
Volume II §27.B handles transfer through source and target families declared in a
`StructuralSimilarityProfile` (p. 50), but neither volume gives a target domain or a generator
for the families. No external benchmark is mentioned anywhere.

## Evidence

- **Vol II §27.B, p. 49:** "An independent delivery receipt costs 1 unit and returns 0 only for
  D. An independent state measurement costs 2 units and returns 1 only for S. When both tests
  are available, the pairs of observations distinguish all three causes."
- **Already in the text (Vol II §27.B, p. 49):** "A separate series changes one premise: the
  receipt concerns another command, measurement is delayed, or the source itself is
  unreliable"; the exhaustive controller "provides a reference for attainable cost, not a
  deliberately weak opponent"; the controls include "routine Intelligence with ordinary memory,
  tools and self-verification".
- **Already in the text (Vol II §27.B, p. 50):** "The principal outcome of the first series is
  the share of new diagnostic tasks with a correct action or justified irresolvability under a
  fixed budget."; "Before launch, component versions, candidate boundary, family generator,
  train / selection / held_out_test split, primary metric and minimum practically significant
  effect are retained."; "A substantively different description with the same test structure
  checks transfer of the inquiry method. A changed structure with similar words tests rejection
  of false analogy."
- **Already in the text (Vol II §33.C.1, p. 111):** "This is a deterministic test of the
  mechanism; a statistical estimate of advantage requires the separate series in §27.B."; "The
  next mandatory version of the diagnostic test closes a harder open-world case: hidden cause X
  must produce the same familiar answers as one of the known causes".
- **Already in the text (Vol I A.4, pp. 99-100):** "a strong null hypothesis: an agent stack
  with ordinary planning, versioned memory of beliefs and provenance, self-checking, mismatch
  response, value-of-information assessment, and a log of failed attempts available to
  subsequent tasks"; "The primary measures are correct localization, verification cost, actual
  action, transfer, and regression."
- **Already in the text (Vol I §12.9, p. 61):** "The same scheme may be useful in another
  domain even though the names of objects and signals change."
- The restored §33.C.1 listing (`repro/diagnostic_cycle.py`) solves the base case at an
  expected cost of 7/3 by exact search over 8 planning states (the listing's
  `evaluated_states`; 6 distinct hypothesis sets).

## Why it matters

A ceiling effect would produce a null result that leaves the hypothesis untested, or a small
difference driven by prompt formatting. The perturbation families are where the organization
should help, and an external benchmark is what makes a positive result credible outside the
programme.

## Ideas & possible recommendations

- **Make the perturbation families the primary series.** The perturbation and hidden-cause
  families, where organization should matter, could carry the headline comparison, with the
  base world used only as infrastructure and an oracle reference.
- **Add an explicit generator.** A generator that scales to k components and m probes, with
  costs, unreliable channels and delays, would give the families stated parameters and instance
  counts.
- **Generate the target families.** §27.B already requires "a substantively different
  description with the same test structure" (transfer) and "a changed structure with similar
  words" (false analogy); a generator could render each structure in several surface
  descriptions and state the number of families.
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
