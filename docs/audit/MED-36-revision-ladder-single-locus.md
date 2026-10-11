---
id: MED-36
title: The revision ladder assumes a single causal locus, and its escalation rules conflict
severity: medium
area: theory
volumes: I, II
sections: Vol I Ch. 10; Vol II §28.B, §28.C.3, §31.10, §32.14, §32.20
review: §7
status: open
github_issue: 44
---

# MED-36 · The revision ladder assumes a single causal locus, and its escalation rules conflict

**Finding.** The ladder (action, procedure, strategy, model, criterion, ground, meta-rule)
localizes an error by testing interventions from the most local level upward, treating the
level as a hypothesis: disappearance of the error supports the level tried, and persistence
"forces the hypothesis upward". That holds if one defect at one level is responsible and each
local fix is applied correctly. If two defects at different levels jointly reproduce the
error, or a local fix is badly applied, every single-level test fails and the procedure points
too high; a higher-level repair also removes lower-level causes, so its success does not
identify the level. Better fault localization is the headline claim, so the identification
assumption needs stating. The escalation rules also conflict.

## Evidence

- **Vol I Ch. 10, p. 47:** "Disappearance of the error and transfer of the correction to
  preregistered structurally similar cases support the corresponding level; persistence forces
  the hypothesis upward."
- **Vol II §31.10, p. 82; §28.B, p. 55:** the system "rises higher only if discriminating
  evidence shows that a more local correction does not eliminate the reproducing mechanism",
  yet "Repeated failure after K corrections opens a higher level"; no profile gives K.
- **Vol II §32.14, p. 90; §32.20, p. 93:** for a mode-selection error "The decision moves to
  META_POLICY"; for local-metric substitution "The decision moves to CRITERIA or FOUNDATIONS".
- **Vol II §31.10, p. 82; §28.C.3, p. 62:** META_POLICY "contains rules by which the system
  itself decides what and how it is permissible to revise"; elsewhere it is "the rule for
  selecting procedures, depth, or thinking mode".
- **Already in the text (Vol I Ch. 10, p. 47):** "The level of the error is not assumed to be
  known in advance. It is a competing causal hypothesis."

## Why it matters

A wrong attribution revises a higher and riskier level than needed, and implementations with
different entry rules revise different things after the same failure.

## Recommendation

State the single-fault assumption, or relax it and test it with joint (factorial)
interventions across levels, as in multiple-fault diagnosis (de Kleer & Williams 1987),
reporting level attribution with an explicit identification condition. Define META_POLICY
once, enter the ladder at the narrowest level in §§32.14 and 32.20, and give K a preregistered
value.

## Resolved when

- [ ] The ladder's identification assumption is stated and tested with joint interventions.
- [ ] META_POLICY has one definition, entry rules agree across sections, and K has a value.

## Related

- Review: [§7](../../REVIEW.md#7-strongest-weakest-distinctive-and-in-need-of-development)
- Issues: MED-34, MED-38, MIN-15
