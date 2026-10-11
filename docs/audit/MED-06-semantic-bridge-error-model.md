---
id: MED-06
title: The language-to-structure bridge has no measured error model
severity: medium
area: architecture
volumes: I, II
sections: Vol I §7.2, §7.3; Vol II §24.A.1, §24.B.2, Ch. 27, Ch. 32, §33.A
review: §4.2(b)
status: open
github_issue: 14
---

# MED-06 · The language-to-structure bridge has no measured error model

**Finding.** The semantic bridge turns language-model text into typed claims, concepts and
relations. The design handles extraction errors the right way: an external phrase becomes a
candidate with provenance and hypothesis status, which must pass verification and the
ordinary revision transaction before it changes the Worldview, and there is a test battery
(paraphrase, polysemy, an unknown term, a counterexample, disabling the bridge). What is
missing is measurement. No extraction accuracy, rate of wrong promotions or registry
maintenance cost is defined; `SemanticMediator` does not appear in the Chapter 27 metrics, the
Chapter 32 failure cards or the §33.A assembly steps; and "disabling the semantic bridge" is
undefined when the mediator runs on the same model as Intelligence. Volume I concedes that the
provenance of an answer from model parameters "often remains indeterminate".

## Evidence

- **Already in the text (Vol II §24.B.2, p. 24):** "An external phrase is not written directly as
  a WORLD_CLAIM: it creates candidates with provenance, which pass verification, sufficiency
  assessment and the ordinary Worldview-change transaction."
- **Vol II §24.B.2, p. 24:** "extract_claims_and_alternatives may be performed by the routine LLM
  under a constrained prompt requiring preservation of source fragments and ambiguities";
  p. 23: "It may use the same computational substrate as Intelligence".
- **Vol II §24.B.2, p. 24:** "If disabling it does not produce the predicted loss [...] the
  claimed mechanism is either decorative or covertly duplicated by another function."
- **Vol I §7.3, p. 37:** "the provenance of a particular answer from model parameters often
  remains indeterminate".

## Why it matters

The epistemic-status layer, the strongest engineering in the volume, is only as good as the
candidates it receives. Systematic extraction errors that survive weak tests are the failure
that would let the full architecture lose to a simpler agent while appearing internally
consistent. This is the knowledge-acquisition problem that limited expert systems and Cyc
(Lenat 1995); language models make extraction cheaper, not reliable.

## Recommendation

Add measured extraction metrics against labelled text (precision and recall of claims,
relations and concept resolution; the rate of generated text promoted as observation),
propagate extraction confidence into claim status, define the "bridge disabled" condition as
a concrete replacement, and add a failure card for systematic extraction error.

## Resolved when

- [ ] Chapter 27 includes extraction-accuracy metrics measured against labelled data.
- [ ] The bridge ablation has a defined replacement arm and a preregistered minimum loss.

## Related

- Review: [§4.2(b)](../../REVIEW.md#42-toward-a-system-with-its-own-worldview-and-values-underspecified-at-the-decisive-step)
- Issues: MED-07, MED-19, MED-38 (failure catalogue)
