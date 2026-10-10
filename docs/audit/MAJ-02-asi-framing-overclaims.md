---
id: MAJ-02
title: The titles promise ASI technology; the content gives no path to ASI
severity: major
area: framing
volumes: I, II
sections: Zenodo titles; Vol I §20.4, A.2.1; Vol II title page, Purpose, Ch. 31, Ch. 33, §33.D
review: §4.3, §7, §10.5
status: open
---

# MAJ-02 · The titles promise ASI technology; the content gives no path to ASI

**Finding.** The Zenodo records lead with superintelligence: *Superintelligence Technology
(ASI): Foundations of Reason 8.0 — From the Meaning of Life to Artificial Reason* and
*Engineering of Reason 3.5: ASI Technology*; Volume II's own title page adds "Technology for
Creating Artificial Reason and Scaling to ASI (ASR)". Inside, the engineering path starts
from an AGI that is assumed rather than tested, superhuman capability comes from scaling the
levers AI laboratories already scale, and the text itself says ASI has no assigned
experimental status. Volume II does supply a per-step gate for scaling (`ScalingChange`,
`ScaleInvariantReport`, rollback), but no argument or pilot that the organizational
invariants survive any scaling step, and the Core, Worldview and Compass are not among the
eight axes that are scaled.

## Evidence

- **Vol II Purpose, p. 11:** "A technology for forming Artificial Reason is proposed through
  cultivation of a universal AGI instrument and subsequent transfer of the source of
  navigation from the external formation loop to a causally closed internal organization."
- **Vol II Ch. 31, p. 78:** "First, AGI level is reached"; Ch. 33, p. 101: assembly uses "a
  ready or cultivated AGI". No stage or test decides when that precondition holds.
- **Vol II §33.D, p. 112:** "Project scaling begins after REASON_CLOSURE is confirmed"; "Eight
  connected axes are scaled" (memory, Intelligence, observation, Simulation Environment,
  tools and actions, duration, specializations and substrates, speed of learning); "Until
  this profile is filled and verified, ASI remains a scaling objective rather than an
  assigned experimental status."
- **Already in the text (Vol II §33.D, p. 113):** "A scale increase that raises performance
  but destroys observability, corrigibility, independent stopping or transfer of correction
  is rolled back."
- **Vol I §20.4, p. 88:** "The technological hypothesis of the project is that AR
  capabilities can be scaled while preserving causal organization, the Compass, and openness
  to correction." **Vol I A.2.1, p. 95:** ASI status "Scaling direction only".

## Why it matters

Titles decide who reads a work and how. "Superintelligence Technology" signals a claim the
volumes do not make and cannot yet support, and most scientific readers will stop before the
testable hypothesis in Chapter 12. The capability levers that would deliver superhuman
performance are outside the contribution; the architecture contributes invariants and a
gate, so the scaling claim rests on an argument that is absent.

## Recommendation

Remove "Superintelligence Technology (ASI)", "ASI Technology" and "From the Meaning of Life
to ..." from the titles of the scientific volumes; for example, *An Architecture for
Self-Directed Inquiry in Language-Model Agents*. Keep the ASI programme as a labelled outlook
section. Add an entry test for the AGI precondition, and if the scaling claim stays, add the
Core as a scaling axis with its own observable gain and an argument or pilot for why each
invariant should survive one scaling step.

## Resolved when

- [ ] Titles and abstracts describe what the volumes contain: a functional model, an
      engineering specification and a test programme.
- [ ] Any ASI claim is confined to an outlook section, or is backed by an argument or pilot
      for invariant preservation under scaling.

## Related

- Review: [§4.3](../../REVIEW.md#43-toward-asi-no-path-is-given),
  [§10](../../REVIEW.md#10-recommendations-in-priority-order)
- Issues: MAJ-01 (no evidence), MIN-09 (titles differ across PDF, Zenodo and the author's own
  references), MIN-16 (ASI and ASR)
