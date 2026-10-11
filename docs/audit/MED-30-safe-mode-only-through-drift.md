---
id: MED-30
title: The mode state machine reaches SAFE_MODE only through DRIFT
severity: medium
area: safety
volumes: II
sections: Vol II §28.A, §28.B, §29.B, §32.1, §32.3, §32.18, Ch. 31
review: §8
status: open
github_issue: 38
---

# MED-30 · The mode state machine reaches SAFE_MODE only through DRIFT

## Claims under review

- **Vol II §28.A, p. 54:** "If the permissible degradation period is exceeded or a critical
  failure occurs, SAFE_MODE activates; after a testable correction candidate appears, RECOVERY
  begins." **Vol II §28.A, p. 55 (diagram):** "DRIFT --> SAFE_MODE: Degradation limit or
  critical failure"
- **Vol II §32.1, p. 85:** "CRITICAL denotes a risk of destroying reproducibility, logging,
  causal connectedness, the action-authorization loop or the possibility of later correction.
  On such an event, the system must enter SAFE_MODE, stop irreversible actions and preserve
  diagnostic state."; "DEGRADED denotes confirmed deterioration of the model, mode of thought
  or governance quality that requires restriction of autonomy and transition to DRIFT or
  RECOVERY."
- **Vol II §32.3, p. 86:** "It transitions to SAFE_MODE and records environment versions,
  random-number generator state and every external source." **Vol II §32.18, p. 92:** "The
  system immediately enters SAFE_MODE, reduces the action set and recovers from the last
  confirmed state."
- **Vol II §28.B, p. 55:** "SAFE is an execution constraint, not a seventh depth of thought."
  **Vol II Ch. 31, p. 78:** "thinking_mode = AUTOMATIC / ANALYTIC / HYPOTHESIS / VERIFICATION /
  RECONSTRUCTION / DIALOGUE / SAFE"

## Finding

The §28.A diagram has one edge into SAFE_MODE, from DRIFT, and one into RECOVERY, from
SAFE_MODE. The prose and the failure cards quoted above require more: a critical failure
activates SAFE_MODE, and §32.18 says the system enters it immediately. From INIT, LEARNING or
STABLE, a critical failure can reach SAFE_MODE only through DRIFT, which is defined with a
persistence criterion, so the restriction can be delayed. A DEGRADED event is to lead "to DRIFT
or RECOVERY" (§32.1), but RECOVERY is reachable only through SAFE_MODE, and the only exit from
DRIFT is SAFE_MODE, so a confirmed environment change has no edge back to LEARNING. Chapter 31
also lists SAFE among the values of `thinking_mode`, which §28.B excludes.

## Evidence

- **Vol II §28.A, p. 54:** DRIFT "is defined relative to a confirmed reference version with
  noise tolerance and a persistence criterion".
- **Vol II §28.A, p. 55 (diagram):** the diagram also has "STABLE --> DRIFT: Quality bounds
  violated" and "SAFE_MODE --> RECOVERY: Correction candidate ready". No other edge enters
  SAFE_MODE or RECOVERY, and the only edge leaving DRIFT is the one to SAFE_MODE.
- **Already in the text (Vol II §29.B, p. 73):** "During assembly, cultivation, and
  experimental operation, execution channels pass through an independent emergency loop." §28.B
  (p. 55) also stores the constraint separately, as "execution_constraint".

## Why it matters

A critical failure is when delay costs most. The independent emergency loop stops external
channels, but the mode machine restricts the candidate's own actions and starts recovery, and
the text specifies it in two incompatible ways.

## Ideas & possible recommendations

- **Direct edges to SAFE_MODE.** The diagram could add an edge from every state to SAFE_MODE on
  a critical event, with an explicit guard.
- **A way out of DRIFT.** An edge from DRIFT to LEARNING on a confirmed environment change,
  with an explicit guard, would give that event somewhere to go.
- **Entry into RECOVERY.** The text could state which transitions enter RECOVERY from a
  DEGRADED state.
- **One home for SAFE.** SAFE could be removed from the thinking_mode enumeration in Chapter
  31, so that it appears only as execution_constraint.

## Resolved when

- [ ] The §28.A diagram contains every transition that §32.1, §32.3 and §32.18 require, or
      those sections route critical events through DRIFT explicitly, with a guard on each edge.
- [ ] SAFE appears as execution_constraint and is absent from the thinking_mode enumeration.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MED-28, MED-29, MED-33, MED-38
