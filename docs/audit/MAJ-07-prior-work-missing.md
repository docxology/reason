---
id: MAJ-07
title: The closest prior work is missing from the chapters
severity: major
area: prior-art
volumes: I, II
sections: Vol I front matter, Part II, Ch. 5, Ch. 6, Ch. 7, Ch. 12, A.2, A.5; Vol II §34.A, References
review: §6, §6.1, §7, Appendix B
status: open
github_issue: 7
---

# MAJ-07 · The closest prior work is missing from the chapters

## Claims under review

- **Vol I A.5, p. 100:** "Below is a selective map of primary publications for comparison of
  individual functions and the nearest architectures. Functional overlap, independent
  derivation, historical priority, and implementation advantage are treated as different
  questions."
- **Vol I Ch. 6, p. 34:** "The next limit appears when no suitable method exists in Procedural
  Memory, when several learned methods produce incompatible consequences, or when a new
  situation requires a solution assembled from different parts of experience. The system then
  needs a mechanism for constructing something new. [...] The insufficiency of a ready-made
  method creates the functional need for Intelligence."; **Vol I Ch. 5, p. 32:** "If a certain
  feature is stably connected with a consequence, and a particular action repeatedly produces an
  acceptable result, the relation can be compressed."
- **Vol I A.2, p. 93:** "Comparisons with scientific literature were carried out after the
  author's propositions had been formed."; **Vol I A.2, p. 95:** "Comparison with prior work is
  given in A.5. It shows areas of overlap and leaves questions of equivalence and advantage to
  separate analysis. The testable claim concerns organization of the cycle 'type of insufficiency
  → method of obtaining a distinction → update of dependent knowledge → transfer of research
  experience' and its interaction with current navigation."
- **Vol II §34.A, p. 114:** "The proposed technology uses functions with well-developed
  predecessors. SOAR [R1] provides a general cognitive architecture with a unified
  problem-solving and learning cycle [...]"; **Vol II §34.A, p. 115:** "The claim of this volume
  concerns the causal organization of these and related capabilities around a self-referential
  current state, a significant insufficiency of ground, discriminating inquiry, the Compass,
  value revision, and transfer of the source of navigation from the RFL to the system itself.
  [...] Such a comparison separates the novelty of the overall architectural claim from already
  known technical mechanisms."

## Finding

The volumes do contain a comparison apparatus, placed at the end: Volume I's final appendix
section, A.5 "Retrospective Scientific Comparisons", which describes itself as a map of "the
nearest architectures", annotates 29 references and adds a terminological correspondence map
and a comparative map that states, for each nearby line of work, what remains a separate claim;
Volume II §34.A cites seven systems in line and treats them as strong nulls. The author also
says the AI-tool priority audit is "not proof of novelty or priority". What is missing is the
closest prior work for the components the chapters present as derived (Chapters 5 and 6,
above): Soar's impasse-driven subgoaling and chunking (the closest single precedent, absent
from Volume I), goal-driven autonomy, truth maintenance and belief revision, model-based
diagnosis (the running example is a textbook case), decision-region active learning, the Robot
Scientist, structure-mapping and case-based reasoning, and the philosophy of inquiry (Peirce,
Dewey, Hintikka, Kant). The chapters themselves name the literature once.

## Evidence

- **Already in the text (Vol I A.2, p. 94):** the Elicit audit "is a result of a limited search
  process, not proof of novelty or priority"; **A.5, pp. 103–104:** "TERMINOLOGICAL
  CORRESPONDENCE MAP" and "COMPARATIVE MAP FOR TESTING NOVELTY".
- **Already in the text (Vol I front matter, p. 15):** of the value-of-information and
  do-operator formalisms, "These formalisms are not claimed as original. The contribution of the
  present model concerns their place within the larger cycle of significant gap, discriminating
  inquiry, revision of grounds, and transfer of correction. Sources are listed in the
  comparative map of the literature."
- **Vol I §7.2, p. 37:** the only literature named in the chapters, RAG and ReAct, cited as
  "Appendix A.5, items 15–16" (printed as items 70 and 71).
- **Vol II §34.A, pp. 114–115:** Soar, ACT-R, LIDA, Generative Agents, Reflexion, Voyager and
  MemGPT cited as [R1]–[R7]; NARS and metareasoning named without references.
- **Absent from both volumes** (exhaustive search): truth maintenance, belief revision,
  model-based diagnosis, Dewey, Peirce, Kant, Hintikka, Stanovich, blackboard architectures,
  the Robot Scientist, BACON, adaptive-submodular test selection, structure-mapping,
  case-based reasoning, goal-driven autonomy, shutdown or off-switch incentives, impact
  measures, prompt injection.
- **Vol I A.2, p. 94:** the method by which components are derived: "The method is process-based
  and causal-functional reconstruction. First the capability under study and its limitation are
  specified, then possible ways of overcoming that limitation are considered."
- **Vol I Chs. 5–6, pp. 32–34:** the Chapter 6 trigger for Intelligence, quoted above, matches
  Soar's impasse types, and Chapter 5's compression of successful episodes into procedures
  matches chunking.

## Why it matters

Without the closest precedents in the chapters, readers cannot tell which parts are new, and
the author cannot borrow solutions that exist: algorithms with guarantees for the
required-distinction step, mechanisms for transfer (MAJ-04), results on dependency-directed
revision. The comparison would favour the author on a real point (Soar's impasses are
syntactic; these gaps are epistemic and decision-relative), and the chapters are stronger for
making it than for leaving readers to find the overlap.

## Ideas & possible recommendations

- **Move the comparison into the chapters.** The A.5 comparative map could be moved into
  Chapter 12, with the nearest precedent cited and contrasted where each component is
  introduced, and one sentence on what is new.
- **Name a minimum set of precedents.** At minimum the chapters could engage Soar, goal-driven
  autonomy and MIDCA, truth maintenance and AGM, model-based diagnosis, EC²/DRD, the Robot
  Scientist, structure-mapping and case-based reasoning, active inference, impact measures and
  corrigibility.
- **State the novelty claim as a claim about the package.** The claim could be put as one about
  the combination of components, in the way Volume II §34.A already frames its claim as one
  about the causal organization of known capabilities.
- **Pointers instead of a move.** A lighter option is a one-line pointer to the relevant A.5
  entry where each component is introduced, as §7.2 already does for RAG and ReAct, provided
  A.5 also gains the missing precedents.

## Resolved when

- [ ] Each component chapter cites and contrasts its closest precedents.
- [ ] Every system named in the text has a bibliography entry.

## Related

- Review: [§6](../../REVIEW.md#6-relation-to-existing-cognitive-and-agent-architectures),
  [§6.1](../../REVIEW.md#61-active-inference-specifically)
- Issues: MED-14 (active inference), MED-23 (unpublished priority audit), MIN-06
  (bibliography), MIN-18 (borrowed methods without citations)
