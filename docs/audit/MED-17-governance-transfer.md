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

**Finding.** Volume I envisages transferring the governance of science, production and
logistics to AR systems through competence mandates, and Volume II makes this the mechanism
by which real control is granted after scaling. Each mandate is scoped, observed and
reviewable, which is good design for a single mandate. The record and the text leave open the
parts that make it safe in practice: who issues a mandate, who audits it, who may revoke it and
how fast, when it expires, and how its six statuses change. Resources follow demonstrated
competence, a positive-feedback loop of the kind Chapter 15 itself warns about, and
replacement is triggered by "a more competent candidate", which asks a holder that values its
own continuation to cooperate in its replacement. The systemic question is deferred: what
happens to human ability to oversee, contest and reverse decisions when many domains are
transferred one locally justified step at a time.

## Evidence

- **Vol I Ch. 17, p. 78:** "A Reason receives the right to coordinate a particular process after
  competence in the relevant domain has been confirmed [...] and a procedure for transferring
  governance to a more competent Reason when persistent error occurs or a better ground
  appears."
- **Vol II §30.F, p. 77:** `CompetenceMandate` lists `holder_reason_id`, `authority_limits[]`,
  `independent_observer_refs[]`, `review_conditions[]`, `replacement_conditions[]` and
  `status: PROBATION / ACTIVE / LIMITED / SUSPENDED / TRANSFERRED / CLOSED`; there is no issuer,
  revocation authority, expiry or transition rule.
- **Vol II §30.F, p. 78:** "persistent deterioration, new information or emergence of a more
  competent candidate launches mandate review".
- **Vol II §33.D, p. 112:** "Real control is granted through CompetenceMandate under §30.F."
- **Vol I Ch. 17, p. 79:** "protection against irreversible centralization are developed in
  Volume III".

## Why it matters

Incremental transfer of control, each step locally rational, is the pathway the
gradual-disempowerment literature identifies as a systemic risk (Kulveit et al. 2025). Volume
III builds on this mechanism, so its properties need analysis first.

## Recommendation

Add issuer, revocation authority and latency, expiry and transition rules to the record; make
revocation independent of the holder's cooperation; define the performance profile
numerically; test acceptance of replacement as a mandatory scenario; and analyse aggregate
effects (limits on the share of critical domains under mandate, preservation of human capacity
to resume control, system-level reversal conditions).

## Resolved when

- [ ] The mandate record names issuer, revocation and expiry, with transition rules.
- [ ] The cumulative effect of mandates is analysed, with system-level reversal conditions.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-06 (incentives), MED-31 (authorization contract)
