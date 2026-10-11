---
id: MAJ-02
title: The titles promise ASI technology; the content gives no path to ASI
severity: major
area: framing
volumes: I, II
sections: Zenodo titles; Vol I §20.4, A.2.1; Vol II title page, Purpose, Ch. 31, Ch. 33, §33.D
review: §4.3, §7, §10.5
status: open
github_issue: 2
---

# MAJ-02 · The titles promise ASI technology; the content gives no path to ASI

## Claims under review

- **Vol II title page, p. 9:** "TECHNOLOGY FOR CREATING ARTIFICIAL REASON AND SCALING TO ASI
  (ASR)"
- **Vol II Purpose of the document, p. 11:** "The technological task is to cultivate, from
  available artificial Intelligence, a system capable of independently continuing causally
  grounded navigation, and then to scale the formed Reason to ASI." Later on the same page: "A
  technology for forming Artificial Reason is proposed through cultivation of a universal AGI
  instrument and subsequent transfer of the source of navigation from the external formation
  loop to a causally closed internal organization."
- **Vol II §33.D, p. 112:** "Further growth increases the capabilities of already formed AR
  while preserving its ability to understand its own state, detect gaps, revise derived
  grounds, and account for consequences." Also: "Within the proposed path, ASI is scaled
  Artificial Reason whose intellectual and operational capabilities stably exceed the human
  range across a predefined broad set of domains."
- **Vol I §20.4, p. 88:** "The technological hypothesis of the project is that AR capabilities
  can be scaled while preserving causal organization, the Compass, and openness to correction."

## Finding

The Zenodo records lead with superintelligence: *Superintelligence Technology (ASI):
Foundations of Reason 8.0 — From the Meaning of Life to Artificial Reason* and *Engineering of
Reason 3.5: ASI Technology*; Volume II's own title page makes the same promise (first claim
above). Inside, the engineering path starts from an AGI that is assumed rather than tested,
superhuman capability comes from scaling the levers AI laboratories already scale, and the text
itself says ASI has no assigned experimental status. Volume II does supply a per-step gate for
scaling (`ScalingChange`, `ScaleInvariantReport`, rollback), but no argument or pilot that the
organizational invariants survive any scaling step, and the Core, Worldview and Compass are not
among the eight axes that are scaled.

## Evidence

- **Vol II Ch. 31, p. 78:** "First, AGI level is reached: universal Intelligence transfers
  methods across tasks, builds working world models, uses memory and tools, and executes a
  broad class of externally specified goals." **Vol II Ch. 33, p. 101:** "Assembly uses a ready
  or cultivated AGI as universal Intelligence". No stage or test decides when that precondition
  holds.
- **Vol II §33.D, p. 112:** "Project scaling begins after REASON_CLOSURE is confirmed"; "Eight
  connected axes are scaled" (memory, Intelligence, observation, Simulation Environment, tools
  and actions, duration, specializations and substrates, speed of learning); "Until this
  profile is filled and verified, ASI remains a scaling objective rather than an assigned
  experimental status."
- **Already in the text (Vol II §33.D, p. 113):** "A scale increase that raises performance but
  destroys observability, corrigibility, independent stopping or transfer of correction is
  rolled back."
- **Already in the text (Vol II §33.D, p. 113):** the Core's scaling is described, but outside
  the list of eight axes: "Scaling the Core is not measured by the number of questions. It must
  improve the quality of navigation among them: retain more dependencies, estimate the price of
  the unknown more precisely, select tests with greater discriminating power, avoid
  investigating unnecessary depth after sufficiency has been reached, and preserve open
  questions across long horizons." The `ScaleInvariantReport` also has the fields
  `core_navigation_quality`, `worldview_commit_integrity` and `compass_status`.
- **Vol I A.2.1, p. 95:** the evidence table gives the status of ASI as "Scaling direction
  only".

## Why it matters

Titles decide who reads a work and how. *Superintelligence Technology* signals a claim the
volumes do not make and cannot yet support, and most scientific readers will stop before the
testable hypothesis in Chapter 12. The capability levers that would deliver superhuman
performance are outside the contribution; the architecture contributes invariants and a gate,
so the scaling claim rests on an argument that is absent.

## Ideas & possible recommendations

- **Retitle the volumes.** The Zenodo records could drop *Superintelligence Technology (ASI)*,
  *ASI Technology* and *From the Meaning of Life to ...* from the titles of the scientific
  volumes, and the Volume II title-page line could be reworded to match; one option is a title
  such as *An Architecture for Self-Directed Inquiry in Language-Model Agents*.
- **Keep ASI as an outlook.** The ASI programme could stay as a labelled outlook section, apart
  from the specification and the test programme.
- **Test the AGI precondition.** An entry test could say when a model counts as the AGI from
  which assembly starts, so that Chapters 31 and 33 no longer assume it.
- **Argue or pilot the scaling claim.** If the scaling claim stays, the Core could be added as
  a scaling axis with its own observable gain, which the §33.D paragraph on scaling the Core
  already outlines in prose, together with an argument or pilot for why each invariant should
  survive one scaling step.

## Resolved when

- [ ] Titles and abstracts describe what the volumes contain: a functional model, an
      engineering specification and a test programme.
- [ ] Any ASI claim is confined to an outlook section, or is backed by an argument or pilot
      for invariant preservation under scaling.

## Related

- Review: [§4.3](../../REVIEW.md#43-toward-asi-no-path-is-given),
  [§10](../../REVIEW.md#10-ideas--possible-recommendations)
- Issues: MAJ-01 (no evidence), MIN-09 (titles differ across PDF, Zenodo and the author's own
  references), MIN-16 (ASI and ASR)
