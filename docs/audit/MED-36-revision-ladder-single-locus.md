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

## Claims under review

- **Vol I Ch. 10, p. 47:** "The system begins with the most local sufficient candidate and
  tests interventions along the preserved dependency: replace data while keeping the method
  fixed; replace a step or rule of the method with the same data; change the frame while
  preserving lower-level relations; then, if the error persists, raise the test to the
  criterion and ground. Disappearance of the error and transfer of the correction to
  preregistered structurally similar cases support the corresponding level; persistence forces
  the hypothesis upward."
- **Vol II §31.10, p. 82:** "The system begins with the narrowest level capable of explaining
  the error and rises higher only if discriminating evidence shows that a more local correction
  does not eliminate the reproducing mechanism." **Vol II §28.B, p. 55:** "Repeated failure
  after K corrections opens a higher level; K and the escalation rule are set by profile."
- **Vol II §32.14, p. 90:** "the system persistently selects the same thinking_mode or expends
  resources inconsistent with the significance of the task"; "The decision moves to
  META_POLICY." **Vol II §32.20, p. 93:** "The decision moves to CRITERIA or FOUNDATIONS and is
  tested against the fundamental risk in Chapter 29."
- **Vol II §31.10, p. 82:** "META_POLICY contains rules by which the system itself decides what
  and how it is permissible to revise." **Vol II §28.C.3, p. 62:** "META_POLICY becomes a
  target only when interventions in lower steps and methods fail to remove the reproducible
  failure and the distinction is localized in the rule for selecting procedures, depth, or
  thinking mode."

## Finding

The ladder (action, procedure, strategy, model, criterion, ground, meta-rule) localizes an
error by testing interventions from the most local level upward, treating the level as a
hypothesis: disappearance of the error supports the level tried, and persistence "forces the
hypothesis upward". That holds if one defect at one level is responsible and each local fix is
applied correctly. If two defects at different levels jointly reproduce the error, or a local
fix is badly applied, every single-level test fails and the procedure points too high; a
higher-level repair also removes lower-level causes, so its success does not identify the
level. Vol II calls the ladder "a rule for localizing the cause" (§31.10, p. 82), so the
identification assumption needs stating. The escalation rules also conflict. §28.C.3 makes
META_POLICY a target only when "interventions in lower steps and methods fail to remove the
reproducible failure" (p. 62) and the distinction is localized in the rule for selecting
procedures, depth or thinking mode. §32.14 sends a persistent mis-selection of thinking_mode,
the subject of the second condition, to META_POLICY without mentioning that interventions at
lower levels must fail first, and §32.20 sends a failure to CRITERIA or FOUNDATIONS without that
step.

## Evidence

- **Vol II §28.B, p. 55; §32.12, p. 89:** no profile gives K; §32.12 states the count rule
  again as "After the specified number of failed local corrections, the system must raise
  correction_level".
- **Already in the text (Vol I Ch. 10, p. 47):** "The level of the error is not assumed to be
  known in advance. It is a competing causal hypothesis."

## Why it matters

A wrong attribution revises a higher and riskier level than needed, and implementations with
different entry rules revise different things after the same failure.

## Ideas & possible recommendations

- **State the assumption.** The single-fault assumption could be stated explicitly.
- **Test joint interventions.** Alternatively, the assumption could be relaxed and tested with
  joint (factorial) interventions across levels, as in multiple-fault diagnosis (de Kleer &
  Williams 1987), reporting level attribution with an explicit identification condition.
- **One META_POLICY.** META_POLICY could be defined once.
- **Common entry rules.** The failure cards in §§32.14 and 32.20 could enter the ladder at the
  narrowest level, and K could be given a preregistered value.

## Resolved when

- [ ] The ladder's identification assumption is stated and, where the text relies on it, tested
      (for example with joint interventions).
- [ ] META_POLICY has one definition and entry rules agree across sections; if an escalation
      count K is kept, it has a value.

## Related

- Review: [§7](../../REVIEW.md#7-strongest-weakest-distinctive-and-in-need-of-development)
- Issues: MED-34, MED-38, MIN-15
