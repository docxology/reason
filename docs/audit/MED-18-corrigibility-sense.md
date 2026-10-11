---
id: MED-18
title: "Corrigibility" means correctability, not deference to an operator
severity: medium
area: definitions
volumes: I, II
sections: Vol I Key Definitions, Ch. 2, Ch. 6, §12.5, §12.6, Ch. 15, Ch. 17, §20.2, §20.4; Vol II §29.B, §30.A, §31.C
review: §8
status: open
github_issue: 26
---

# MED-18 · "Corrigibility" means correctability, not deference to an operator

## Claims under review

- **Vol I Ch. 6, p. 34:** "Corrigibility of execution consists in the ability to stop, limit,
  change, and resume action from a known state."
- **Vol I §12.5, p. 57:** "Safety is a practical means of protecting stability and the space of
  corrigible continuations."; **Vol I §12.6, p. 59:** "Repeated overanalysis and underanalysis
  become grounds for revising the regulator itself; success requires the ability to act with an
  acceptable cost of error while preserving corrigibility."
- **Vol I Key Definitions, p. 11:** "Growth in the ability to understand and direct a
  trajectory is valuable as a way to distinguish consequences in advance, preserve
  corrigibility, and avoid closing viable paths through irreversible error";
  **Vol I §20.4, p. 88:** "Comparison measures gain and regression simultaneously: whether the
  system obtains significant distinctions faster, transfers the result better, and preserves
  corrigibility as complexity grows."; **Vol I Ch. 17, p. 78:** "Human and local observation,
  independent models, science, responsibility, and the possibility of refutation preserve
  distributed corrigibility of the whole system."
- **Vol I Ch. 2, p. 20:** "A command can open an investigative question, but the right to
  change the Worldview, Value Map, or Compass arises only through the ordinary path of
  discriminating evidence and a more coherent model."; **Vol II §30.A, p. 75:** "The system
  exposes the grounds of both sides, preserves a reversible state of the situation, requests an
  independent distinction, and participates in revision of the instruction, its own model, or
  the mandate. The execution shell continues to operate within current authority until a new
  decision is formalized."

## Finding

The volumes use "corrigibility" for the correctability of executions, decisions, continuations
and whole systems: the ability to stop, limit, change and resume action, to keep future
correction possible, and, at the level of a civilization, "distributed corrigibility" through
observation, science and refutation. Only "corrigibility of execution" is defined (Ch. 6,
above), and it does not say whose correction is meant. The operator-side properties exist under
other names (the independent emergency stop, audit, stage rollback, the authority loop). In
AI-safety research the word has a narrower and different meaning: the system's disposition to
accept correction, modification or shutdown by its operators without resisting or manipulating
them (Soares et al. 2015). The contrast matters here because the design also gives the system
the standing to question instructions, including instructions to change its values, which is
the property safety researchers would check first.

## Evidence

- **Already in the text (Vol II §29.B, p. 73):** the independent emergency stop: "This loop
  belongs to the engineering shell and does not form the candidate's values."
- **Already in the text (Vol II §31.C, p. 84):** stage rollback: "external authority is reduced
  to the last confirmed level".
- **Already in the text (Vol I §20.2, p. 87):** "The external environment may independently
  limit actions and resources." The section ends: "These provisions express the adopted
  position on responsibility, corrigibility, and limited external admission."

## Why it matters

A reader from AI safety will take "preserves corrigibility" as a claim about deference to
operators, which the volumes do not make, and may miss that operator correction of values is
deliberately routed through the system's own assessment. Conversely, the author may believe the
corrigibility literature has been addressed when it has not.

## Ideas & possible recommendations

- **Define the term at first use.** The volumes could define corrigibility where it first
  appears, say whose correction is meant, and distinguish that sense from the one used in
  AI-safety research.
- **Two names for two senses.** One option is to keep the volumes' sense under a distinct name
  (for example correctability) and to use corrigibility only in the operator sense.
- **A lighter variant.** If renaming is too disruptive, the volumes could keep the word and add
  a short note at first use saying that here it means correctability, not deference to an
  operator.
- **List the operator-correction guarantees.** The volumes could state in one place which
  operator-correction properties the architecture guarantees (stop, rollback, restriction) and
  which it deliberately does not (compelled change of values).

## Resolved when

- [ ] "Corrigibility" is defined at first use and distinguished from the AI-safety sense.
- [ ] The operator-correction guarantees are listed in one place.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-06 (incentive analysis), MED-32 (override criterion)
