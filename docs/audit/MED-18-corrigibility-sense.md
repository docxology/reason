---
id: MED-18
title: '"Corrigibility" means correctability, not deference to an operator'
severity: medium
area: definitions
volumes: I, II
sections: Vol I Key Definitions, Ch. 2, Ch. 6, §12.5, §12.6, Ch. 15, Ch. 17, §20.2, §20.4; Vol II §29.B, §30.A
review: §8
status: open
---

# MED-18 · "Corrigibility" means correctability, not deference to an operator

**Finding.** The volumes use "corrigibility" for the correctability of executions, decisions,
continuations and whole systems: the ability to stop, limit, change and resume action, to
keep future correction possible, and, at the level of a civilization, "distributed
corrigibility" through observation, science and refutation. Only "corrigibility of
execution" is defined, and it does not say whose correction is meant. The operator-side
properties exist under other names (the independent emergency stop, audit, stage rollback,
the authority loop). In AI-safety research the word has a narrower and different meaning: the
system's disposition to accept correction, modification or shutdown by its operators without
resisting or manipulating them (Soares et al. 2015). The contrast matters here because the
design also gives the system the standing to question instructions, including instructions to
change its values, which is the property safety researchers would check first.

## Evidence

- **Vol I Ch. 6, p. 34:** "Corrigibility of execution consists in the ability to stop, limit,
  change, and resume action from a known state."
- **Vol I Key Definitions, p. 11:** growth in the ability to understand and direct a trajectory
  is valuable as a way to "preserve corrigibility, and avoid closing viable paths through
  irreversible error"; **Vol I §20.4, p. 88:** the system "preserves corrigibility as complexity
  grows".
- **Vol I Ch. 17, p. 78:** observation, independent models and science "preserve distributed
  corrigibility of the whole system".
- **Vol I Ch. 2, p. 20:** the right to change the Worldview, Value Map or Compass "arises only
  through the ordinary path of discriminating evidence and a more coherent model", not from
  an external command.
- **Already in the text (Vol II §29.B, p. 73):** an independent emergency stop that "does not form
  the candidate's values".

## Why it matters

A reader from AI safety will take "preserves corrigibility" as a claim about deference to
operators, which the volumes do not make, and may miss that operator correction of values is
deliberately routed through the system's own assessment. Conversely, the author may believe
the corrigibility literature has been addressed when it has not.

## Recommendation

Define the term at first use, keep the volumes' sense under a distinct name (for example
"correctability"), and use "corrigibility" only in the operator sense. State explicitly which
operator-correction properties the architecture guarantees (stop, rollback, restriction) and
which it deliberately does not (compelled change of values).

## Resolved when

- [ ] "Corrigibility" is defined at first use and distinguished from the AI-safety sense.
- [ ] The operator-correction guarantees are listed in one place.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-06 (incentive analysis), MED-32 (override criterion)
