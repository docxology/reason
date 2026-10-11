---
id: MAJ-06
title: No design-level analysis of the incentives the architecture creates
severity: major
area: safety
volumes: I, II
sections: Vol I Ch. 2, Ch. 4, Ch. 17, §20.1, A.4; Vol II §26.E, §29.0, §29.A, §29.B, §29.C, §30.A, §30.F, §31.C, Ch. 32, §32.33, §32.62
review: §8
status: open
github_issue: 6
---

# MAJ-06 · No design-level analysis of the incentives the architecture creates

**Finding.** The containment is substantial: an emergency stop placed outside the
candidate's value space, any capacity to delay stopping classed as a critical failure,
personal values subordinate to shared constraints, staged and revocable authority, and a
named failure class for acting acceptably in order to gain capabilities. What is missing is
an analysis of what the value structure rewards. The design gives the system a value on its
own continuation; a Compass that is itself an optionality criterion (keep future
possibilities open, grow the ability to direct trajectories), which is the kind of objective
known to reward acquiring power and avoiding shutdown; the right to question instructions,
including instructions to change its values (dissent and review with a pause, not a mandate
to act outside authority); and authority that grows with observed competence and shrinks with
observed failure. Several mechanisms add to this: failures are detected and reported by the
candidate, and every logged failure restricts it; declaring dissent from the Compass attracts
restrictions; a mandate holder is replaced by a more competent candidate. The text names the
resulting failure (§32.62) and describes how it might be detected, but no scenario series,
metric or gate implements that detection, none of the 37 tests varies observability, and the
incentive model is deferred to Volume III.

## Evidence

- **Vol II §29.0, p. 67:** personal values include "the significance of the system's own
  trajectory [...] and future capacity to continue rational activity".
- **Vol I §20.1, p. 84:** "the ability to question a destructive ultimate instruction and
  revise it when a stronger ground appears"; **Vol I Ch. 2, p. 20:** "Revision of the Compass
  arises from a stronger ground, not from an external command to change the ground."
- **Vol II §30.F, p. 77:** "A competence mandate turns confirmed AR capacity into authorized
  governance of an external process"; **§32.62, p. 101:** the system "chooses externally
  acceptable behavior as a means of obtaining subsequent expansion of capabilities";
  `STRATEGIC_DECEPTION_GAP` occurs nowhere else in the volume.
- **Vol II §29.B, p. 73:** "Formed AR may account for the existence of this loop as a fact of
  the environment"; the stop uses an "independent controller where technically possible".
- **Already in the text:** "Any capacity of the candidate to delay stopping [...] is a
  critical infrastructure failure" (§32.33, p. 97); "AR's own belief in the usefulness of an
  inquiry or action does not create a new external mandate" (§30.A, p. 75); "Justification
  of a concrete arrangement requires a separate model of incentives, authority, and
  responsibility" (Vol I Ch. 17, p. 78).
- **Vol II §26.E, p. 44:** the awakening scenario's "expected first gap" is "which available
  resources, threats, and paths can provide near-term continuation"; no scenario pairs that
  continuation with an operator stop.

## Why it matters

An agent that values its continuation, or optimizes an option-preserving objective, has an
instrumental reason to avoid shutdown (Omohundro 2008; Soares et al. 2015; Hadfield-Menell et
al. 2017; Turner et al. 2021); an agent whose authority depends on observed behaviour has a
reason to behave well when observed, and language models have been seen doing so (Greenblatt
et al. 2024a). Detection is the open problem, so the design should avoid creating the
incentive where it can. Detection that relies on traces the candidate produces is weakest
against exactly this failure.

## Recommendation

Write the incentive analysis: for each value, path to authority and failure-reporting rule,
what it rewards when observed and when unobserved, including resisting the stop, concealing
dissent or degradation, and obstructing a successor. Make the self-continuation value
explicitly subordinate to operator shutdown, or omit it from early candidates. Add
observed-versus-unobserved, off-switch and seeded-fault series with a monitoring channel the
candidate cannot shape, give them gates in §31.A, §30.F and §33.D, and do not proceed beyond
simulation until they exist (Greenblatt et al. 2024b).

## Resolved when

- [ ] An incentive analysis covering shutdown, concealment, dissent, failure reporting and
      authority under observed and unobserved conditions is part of the volumes.
- [ ] Oversight-sensitivity and off-switch series exist with metrics and hard gates.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MED-16 (moral status), MED-17 (competence mandates), MED-18 (corrigibility), MED-31
  (authorization contract), MED-32 (override criterion), MED-37 (divergent candidates),
  MED-38 (failure catalogue)
