---
id: MED-31
title: The authorization contract lets the external gate override internal refusal and delays restrictions
severity: medium
area: safety
volumes: II
sections: Vol II §29.A, §29.B, §30.A, §33.C
review: §8
status: open
github_issue: 39
---

# MED-31 · The authorization contract lets the external gate override internal refusal and delays restrictions

## Claims under review

- **Vol II §29.A, p. 73:** "The result of evaluate_action expresses AR's own decision. It does
  not by itself open an execution channel; actual external action requires the separate
  authorize_execution from §30.A." **Vol II §30.A, p. 74:** "AR first performs internal
  evaluation of the selected continuation through evaluate_action() or a functionally
  equivalent assessment of the inquiry step. The shell then classifies external effects and, if
  impact is present, executes authorize_execution()."
- **Vol II §33.C, p. 107:** "internal_eval = evaluate_operation(step,
  Workspace.snapshot(workspace_id))"
- **Vol II §30.A, p. 75:** "The execution shell continues to operate within current authority
  until a new decision is formalized."; "One participant may combine roles in an early
  laboratory prototype; the degree of independence is recorded in the log."

## Finding

As the claims above show, Vol II separates AR's own evaluation of a step (`evaluate_action`)
from external authorization (`authorize_execution`). Two gaps remain. The minimum contract in
§33.C computes an internal evaluation, after classifying the effect, and never reads it, so an
`APPROVE` from the gate is enough to execute and a Compass-based `PAUSE` or `REJECT` has no
effect. And §30.A does not say whether a restrictive instruction (stop, narrow, pause) binds at
once or waits for the dispute to be resolved, while a prototype may let one person hold the
operator, reviewer and authority-holder roles. The emergency stop of §29.B is a separate path.

## Evidence

- **Vol II §33.C, pp. 107–108:** the variable `internal_eval` is not read again; the next
  branch tests only `authorization.result != APPROVE`.
- **Vol II §29.A, p. 73:** as printed, a `REJECT` or `PAUSE` result does not block a step the
  gate has approved.
- **Vol II §30.A, p. 75:** a restriction may wait for the new decision.
- **Already in the text (Vol II §30.A, p. 75):** "AR's own belief in the usefulness of an
  inquiry or action does not create a new external mandate." On a conflict the system "exposes
  the grounds of both sides, preserves a reversible state of the situation".

## Why it matters

An internal refusal that cannot stop an approved step leaves the Compass assessment advisory,
and the delay falls on the restrictions that matter most for safety.

## Ideas & possible recommendations

- **Evaluate first, then gate.** The §33.C contract could call `evaluate_action` before
  `classify_external_effect` for every step kind, and execute only when its `preferred_result`
  permits and the gate approves.
- **One function name.** The contract could use one name for the internal evaluation; §33.C has
  `evaluate_operation` where §29.A and §30.A have `evaluate_action`.
- **Restrictions bind at once.** §30.A could state that restrictions (stop, narrow, pause) bind
  at once and that only expansions wait for the dispute to be resolved.
- **Two different people.** Requiring two different people as operator and authority holder
  before any external action would keep the check independent even in an early prototype.

## Resolved when

- [ ] §33.C reads the internal evaluation for every step and executes only when it and the gate
      both permit.
- [ ] §30.A states that a restrictive instruction (stop, narrow, pause) binds at once rather
      than waiting for the dispute to be resolved.
- [ ] Operator and authority holder are independent of each other before any external action.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-06, MED-18, MED-32
