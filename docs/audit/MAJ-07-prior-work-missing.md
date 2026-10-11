---
id: MAJ-07
title: The closest prior work is missing from the chapters
severity: major
area: prior-art
volumes: I, II
sections: Vol I Part II, Ch. 7, Ch. 12, A.2, A.5; Vol II §34.A, References
review: §6, §6.1, §7, Appendix B
status: open
github_issue: 7
---

# MAJ-07 · The closest prior work is missing from the chapters

**Finding.** The volumes do contain a comparison apparatus, placed at the end: Volume I's
final appendix section, A.5 "Retrospective Scientific Comparisons", annotates 29 references
and adds a terminological correspondence map and a comparative map that states, for each
nearby line of work, what remains a separate claim; Volume II §34.A cites seven systems in
line and treats them as strong nulls. The author also says the AI-tool priority audit is
"not proof of novelty or priority". What is missing is the closest prior work for the
components the chapters present as derived: Soar's impasse-driven subgoaling and chunking
(the closest single precedent, absent from Volume I), goal-driven autonomy, truth
maintenance and belief revision, model-based diagnosis (the running example is a textbook
case), decision-region active learning, the Robot Scientist, structure-mapping and
case-based reasoning, and the philosophy of inquiry (Peirce, Dewey, Hintikka, Kant). The
chapters themselves name the literature once.

## Evidence

- **Vol I A.2, p. 93:** "Comparisons with scientific literature were carried out after the
  author's propositions had been formed."
- **Already in the text (Vol I A.2, p. 94):** the Elicit audit "is a result of a limited
  search process, not proof of novelty or priority"; **A.5, pp. 103–104:** "TERMINOLOGICAL
  CORRESPONDENCE MAP" and "COMPARATIVE MAP FOR TESTING NOVELTY".
- **Vol I §7.2, p. 37:** the only literature named in the chapters, RAG and ReAct, cited as
  "Appendix A.5, items 15–16" (printed as items 70 and 71).
- **Vol II §34.A, pp. 114–115:** Soar, ACT-R, LIDA, Generative Agents, Reflexion, Voyager and
  MemGPT cited as [R1]–[R7]; NARS and metareasoning named without references.
- **Absent from both volumes** (exhaustive search): truth maintenance, belief revision,
  model-based diagnosis, Dewey, Peirce, Kant, Hintikka, Stanovich, blackboard architectures,
  the Robot Scientist, BACON, adaptive-submodular test selection, structure-mapping,
  case-based reasoning, goal-driven autonomy, shutdown or off-switch incentives, impact
  measures, prompt injection.
- **Vol I Ch. 6, p. 34:** the trigger for Intelligence ("when no suitable method exists in
  Procedural Memory, when several learned methods produce incompatible consequences")
  matches Soar's impasse types, and Chapter 5's compression of successful episodes into
  procedures matches chunking.

## Why it matters

Without the closest precedents in the chapters, readers cannot tell which parts are new, and
the author cannot borrow solutions that exist: algorithms with guarantees for the
required-distinction step, mechanisms for transfer (MAJ-04), results on dependency-directed
revision. The comparison would favour the author on a real point (Soar's impasses are
syntactic; these gaps are epistemic and decision-relative), and the chapters are stronger for
making it than for leaving readers to find the overlap.

## Recommendation

Move the A.5 comparative map into Chapter 12, and cite and contrast the nearest precedent
where each component is introduced, with one sentence on what is new. At minimum engage
Soar, goal-driven autonomy and MIDCA, truth maintenance and AGM, model-based diagnosis,
EC²/DRD, the Robot Scientist, structure-mapping and case-based reasoning, active inference,
impact measures and corrigibility. State the novelty claim as a claim about the package.

## Resolved when

- [ ] Each component chapter cites and contrasts its closest precedents.
- [ ] Every system named in the text has a bibliography entry.

## Related

- Review: [§6](../../REVIEW.md#6-relation-to-existing-cognitive-and-agent-architectures),
  [§6.1](../../REVIEW.md#61-active-inference-specifically)
- Issues: MED-14 (active inference), MED-23 (unpublished priority audit), MIN-06
  (bibliography), MIN-18 (borrowed methods without citations)
