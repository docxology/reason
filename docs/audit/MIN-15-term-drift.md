---
id: MIN-15
title: Defined terms change name and capitalization
severity: minor
area: editorial
volumes: I, II
sections: Vol I guide, §7.2, Conclusion, A.5; Vol II §§22.A, 26.0.1, 27.6, 28.0, 28.C, 29.0.2, 29.A, 32.46, Ch. 33, App. A
review: Appendix A
status: open
---

# MIN-15 · Defined terms change name and capitalization

**Finding.** The volumes name one component in several ways and print one name in several
capitalizations, so a reader cannot tell whether a coined term or an ordinary phrase is meant, or
whether two names denote one component. The drift reaches identifiers too: `ingest_proposals` and
`ingest_proposal()` (§28.C), "Fundamental risk" and `FoundationalRisk` (§29.A).

## Evidence

- **Modeling Environment.** Volume I's component is "Modeling Environment" (guide, p. 4; Vol II
  §28.0, p. 52), but Vol II's §28.C heading says "Modeling Workspace" (p. 57), and §33.A.8 and
  Appendix A say "Simulation Environment" (pp. 104, 116). Appendix A has no entry reconciling
  them.
- **Formation guide.** "trainer" (Vol I §7.2, p. 37), "teacher" (Vol II §29.0.2, p. 69),
  `TEACHER_LLM` (§22.A, p. 17), `TRAINER_AI` (§26.0.1, p. 40) and "mentor" in prose, as in
  "teacher_agreement_bias tests how strongly the candidate tends to accept a mentor's" (§27.6,
  p. 47).
- **Test apparatus.** "test bench v0" (Vol II Ch. 33, p. 102), "Proving Ground v0" (§33.B, p. 105)
  and "lower proving ground" (Ch. 33, p. 101) name one thing; FastGate is the "zero gate" in the
  §32.46 heading (p. 99).
- **Capitalization.** In the chapters, headings excluded, Vol I prints Self-Model 8 times and
  self-model 13, Current Coordinate 21 and current coordinate 6, Procedural Memory 11, Procedural
  memory 7 and procedural memory 10; Vol II prints Self-Model 18 and self-model 20. "Meta-Thinking
  (working hypothesis)" (Vol I A.5, p. 105) sits against "in the metathinking mode" (Conclusion,
  p. 90).
- **Name map.** Executive Loop, one of the nine functions in Vol I's guide table, never appears in
  Vol II's body, which uses identifiers such as `authorize_execution`.

## Why it matters

"Modeling Environment" is a component of the Volume I architecture, and `ModelingWorkspace` is a
Volume II record, so a reader cannot tell whether they are one thing. Case changes blur coined
terms and common nouns.

## Recommendation

Fix one English name and one capitalization per concept, use it in prose, headings and
identifiers, and add a Volume I to Volume II name map covering every component.

## Resolved when

- [ ] Each component and role has one name in both volumes, and each coined term has one
      capitalization.

## Related

- Review: [Appendix A](../../REVIEW.md#appendix-a-editorial-issues-found)
- Issues: MED-20, MED-35, MIN-11
