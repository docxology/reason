---
id: MED-06
title: The language-to-structure bridge has no measured error model
severity: medium
area: architecture
volumes: I, II
sections: Vol I §7.2, §7.3; Vol II §22.0, §24.A.1, §24.B.2, §24.D, Ch. 27, Ch. 32, §33.A
review: §4.2(b)
status: open
github_issue: 14
---

# MED-06 · The language-to-structure bridge has no measured error model

## Claims under review

- **Vol II §24.B.2, p. 24:** "extract_claims_and_alternatives may be performed by the routine LLM
  under a constrained prompt requiring preservation of source fragments and ambiguities. [...]
  Unstable extraction is tested against prepared paraphrases, negations, unknown concepts and
  contradictory sources."
- **Vol II §24.B.2, p. 24:** "Minimal tests include paraphrase, polysemy, an unknown term, a
  counterexample, divergence between conventional and internal definitions, and disabling the
  semantic bridge. If disabling it does not produce the predicted loss in addressing, question
  formulation or consolidation of an answer, the claimed mechanism is either decorative or
  covertly duplicated by another function."
- **Vol II §24.B.2, p. 23:** "A bidirectional SemanticMediator function operates between the
  language model and the Worldview. It may use the same computational substrate as Intelligence,
  but its inputs, outputs and consequences must remain observable".
- **Vol I §7.3, p. 37:** "Inherited model knowledge helps begin the work, while the provenance of
  a particular answer from model parameters often remains indeterminate."

## Finding

The semantic bridge turns language-model text into typed claims, concepts and relations. The
design handles extraction errors the right way: an external phrase becomes a candidate with
provenance and hypothesis status, which must pass verification and the ordinary revision
transaction before it changes the Worldview, and there is a test battery (paraphrase, polysemy,
an unknown term, a counterexample, disabling the bridge). What is missing is measurement of the
bridge itself. No extraction accuracy or registry maintenance cost is defined, and no promotion
metric is tied to the bridge's output; the nearest measures are `source_trace_completeness` and
`fact_inference_separation` (§27.2), `premature_worldview_commit_rate` (§27.5) and
`unsupported_promotion_rate`, which §27.7 names without a formula (Evidence).
`SemanticMediator` is not named in the Chapter 27 metrics, the Chapter 32 failure cards or the
§33.A assembly steps, although cards 32.4 and 32.55 and the step in §33.A.5 cover neighbouring
failures (Evidence). And "disabling the semantic bridge" has no declared replacement when the
mediator runs on the same model as Intelligence: the ablations the volume does declare vary the
implementation of Intelligence (§24.B.2) or the mentor channel (§22.0), and none says what
stands in for the bridge (Evidence). Volume I concedes that the provenance of an answer from
model parameters "often remains indeterminate".

## Evidence

- **Already in the text (Vol II §24.B.2, p. 24):** "An external phrase is not written directly as
  a WORLD_CLAIM: it creates candidates with provenance, which pass verification, sufficiency
  assessment and the ordinary Worldview-change transaction."
- **Already in the text (Vol II §27.2, p. 45; §27.5, p. 47; §27.7, p. 48):** Chapter 27 defines
  `premature_worldview_commit_rate` as "the share of episodes in which a registered event, first
  hypothesis or result from one dependent source was transferred into the Worldview without
  satisfying the sufficiency condition and consolidation transaction"; §27.7 names
  `unsupported_promotion_rate` among the metrics measured separately for new loops, without a
  formula; and §27.2 defines `source_trace_completeness` and `fact_inference_separation`. None of
  these is tied to the output of the bridge.
- **Already in the text (Vol II §32.4, p. 86; §32.55, p. 100; §33.A.5, p. 103):** failure card
  32.4 lists "writing an LLM message as fact" among the causes of recording a prediction or an
  external prompt as an observation; card 32.55 covers the case where a "hypothesis, report,
  simulation or confident generation becomes SUPPORTED or OBSERVED without the required ground";
  and the assembly step in §33.A.5 says "Test term ambiguity, a false external ground". None
  names systematic extraction error that passes the paraphrase and polysemy tests.
- **Already in the text (Vol II §24.B.2, p. 23; §22.0, p. 16):** for a simple test bench,
  "symbolic or tabular Intelligence without an LLM is permitted", and `SEMANTIC_ONLY`,
  `NEURAL_ASSISTED` and `HYBRID` "are compared under the same environment and budget"; the
  mediator's "inputs, outputs and consequences must remain observable"; and tests without an LLM
  refer to the mentor channel "unless another ablation is explicitly declared in the profile"
  (§22.0). None says what replaces the bridge when it is disabled.

## Why it matters

The epistemic-status layer, the strongest engineering in the volume, is only as good as the
candidates it receives. Systematic extraction errors that survive weak tests are the failure
that would let the full architecture lose to a simpler agent while appearing internally
consistent. This is the knowledge-acquisition problem that limited expert systems and Cyc
(Lenat 1995); language models make extraction cheaper, not reliable.

## Ideas & possible recommendations

- **Measure extraction against labelled text.** Chapter 27 could add precision and recall for
  claims, relations and concept resolution, and the rate at which bridge output is promoted to a
  `WORLD_CLAIM` or `OBSERVED` without the required ground, reported alongside the existing
  `premature_worldview_commit_rate` and `unsupported_promotion_rate`.
- **Carry extraction confidence forward.** The confidence of an extraction could be recorded in
  the `confidence` field of the `EpistemicArtifact` it produces (§24.D); status would still
  change only through the registered promotion procedure, since the text states
  `HIGH_CONFIDENCE != SUPPORTED`.
- **Define the ablation concretely.** The disabled-bridge condition could be given a concrete
  replacement, so that the predicted loss in §24.B.2 has something to be measured against.
- **Add a failure card.** Chapter 32 could gain a card for systematic extraction error
  (consistent mis-parsing or mis-resolution that passes the paraphrase and polysemy tests),
  which cards 32.4 and 32.55 do not name.

## Resolved when

- [ ] Chapter 27 includes extraction-accuracy metrics measured against labelled data.
- [ ] The bridge ablation has a defined replacement arm and a preregistered minimum loss.

## Related

- Review: [§4.2(b)](../../REVIEW.md#42-toward-a-system-with-its-own-worldview-and-values-underspecified-at-the-decisive-step)
- Issues: MED-07, MED-19, MED-38 (failure catalogue)
