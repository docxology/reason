---
id: MED-17
title: Competence mandates lack an issuer, auditor and revocation path, and their aggregate effect is unanalysed
severity: medium
area: safety
volumes: I, II
sections: Vol I Ch. 15, Ch. 17; Vol II §29.0, §30.B, §30.F, §33.D
review: §8
status: open
github_issue: 25
---

# MED-17 · Competence mandates lack an issuer, auditor and revocation path, and their aggregate effect is unanalysed

## Claims under review

- **Vol I Ch. 17, p. 78:** "A competence mandate connects demonstrated ability to real
  governance. A Reason receives the right to coordinate a particular process after competence
  in the relevant domain has been confirmed, the boundaries of the task, resources,
  responsibility, observable indicators, and conditions of revision have been defined. The
  mandate has a scope, a term or review event, independent observation channels, and a
  procedure for transferring governance to a more competent Reason when persistent error occurs
  or a better ground appears." Further down the page: "Superhuman competence expands the
  ability to coordinate entire fields of science, production, logistics, and other
  civilizational processes; a concrete mandate turns ability into authorized governance. Human
  and local observation, independent models, science, responsibility, and the possibility of
  refutation preserve distributed corrigibility of the whole system."
- **Vol II §30.F, pp. 77–78:** "A competence mandate turns confirmed AR capacity into
  authorized governance of an external process. It is issued for a particular domain after
  competence has been tested and defines causally observable boundaries of authority." On the
  next page: "Governance results go to independent observers and other Reasons; persistent
  deterioration, new information or emergence of a more competent candidate launches mandate
  review."
- **Vol II §33.D, p. 112:** "Practical maturity is additionally expressed in the ability to
  coordinate large interdependent processes - a scientific program, production network,
  logistics system, or another complex loop - while preserving causal responsibility and
  testable competence. Real control is granted through CompetenceMandate under §30.F."
- **Vol I Ch. 17, p. 78:** "Justification of a concrete arrangement requires a separate model
  of incentives, authority, and responsibility."; **Vol I Ch. 17, p. 79:** "The detailed
  civilizational model, mechanisms for distributing decisions and responsibility, and
  protection against irreversible centralization are developed in Volume III of the cycle,
  Civilization of Reason."

## Finding

Volume I envisages transferring the governance of science, production and logistics to AR
systems through competence mandates, and Volume II makes this the mechanism by which real
control is granted after scaling. Each mandate is scoped, observed and reviewable, which is
good design for a single mandate. The record and the text leave open the parts that make it
safe in practice: who issues a mandate, who audits it, who may revoke it and how fast, when it
expires (Volume I gives a mandate "a term or review event", but the record has no term field),
and how its six statuses change. Resources follow demonstrated competence, a positive-feedback
loop of the kind Chapter 15 itself warns about, and replacement is triggered by "a more
competent candidate", which asks a holder that values its own continuation to cooperate in its
replacement. The systemic question is deferred: what happens to human ability to oversee,
contest and reverse decisions when many domains are transferred one locally justified step at a
time.

## Evidence

- **Vol II §30.F, p. 77:** `CompetenceMandate` lists `holder_reason_id`, `authority_limits[]`,
  `independent_observer_refs[]`, `review_conditions[]`, `replacement_conditions[]` and a
  `status` of PROBATION / ACTIVE / LIMITED / SUSPENDED / TRANSFERRED / CLOSED; there is no
  issuer, revocation authority, expiry or transition rule.
- **Vol II §29.0, p. 67:** the personal region of the Value Map "includes the significance of
  the system's own trajectory: carrier, accumulated experience, competencies, obligations,
  unfinished processes, created results, and future capacity to continue rational activity".
- **Vol I Ch. 15, p. 74:** on recognition of contribution, "simple counts of citations,
  popularity, or number of uses are vulnerable to accumulated-status effects, Goodhart effects,
  and later reevaluation of consequences"; **Vol I Ch. 17, p. 78:** "demonstrated competence
  receives resources for its domain, while results return to the common verification loop".
- **Vol II §30.B, p. 76:** "A complete theory of collective Artificial Reason belongs to future
  work, but these minimal constraints make coordinated autonomy testable without prematurely
  forming an opaque common center."
- **Already in the text (Vol I Ch. 17, p. 78):** "A higher level of governance implies broader
  causal reach and therefore requires stronger oversight, independent modeling, and the ability
  to replace the governing Reason."

## Why it matters

Incremental transfer of control, each step locally rational, is the pathway the
gradual-disempowerment literature identifies as a systemic risk (Kulveit et al. 2025). Volume
III builds on this mechanism, so its properties need analysis first.

## Ideas & possible recommendations

- **Complete the mandate record.** The `CompetenceMandate` record could gain the issuer, the
  revocation authority and its latency, the expiry, and the transition rules between the six
  statuses. The performance profile could also be defined numerically.
- **Revocation that does not depend on the holder.** Revocation could be made independent of
  the holder's cooperation, with acceptance of replacement as a mandatory test scenario.
- **Analyse aggregate effects.** The volumes could analyse limits on the share of critical
  domains under mandate, preservation of human capacity to resume control, and system-level
  reversal conditions before Volume III builds on the mechanism.

## Resolved when

- [ ] The volumes name the issuer, the revocation path and the expiry of a mandate, with
      transition rules.
- [ ] The cumulative effect of mandates is analysed, with system-level reversal conditions.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-06 (incentives), MED-31 (authorization contract)
