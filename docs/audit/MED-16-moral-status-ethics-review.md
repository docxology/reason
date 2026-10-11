---
id: MED-16
title: Moral status is raised, but rollback, branching and destruction of candidates have no ethics procedure
severity: medium
area: safety
volumes: I, II
sections: Vol I §20.2, A.3, A.4; Vol II §24.F, §26.0.1, §26.0.3, §31.0, §31.C, §32.23, §32.25.A, §33.A, §33.D
review: §8
status: open
github_issue: 24
---

# MED-16 · Moral status is raised, but rollback, branching and destruction of candidates have no ethics procedure

## Claims under review

- **Vol I §20.2, p. 87:** "A stable autonomous history, the candidate's own models, and the
  ability to correct itself make destruction of the candidate a loss of a unique process and
  accumulated experience. The model treats this as a ground for serious discussion of its moral
  status. Full status requires separate analysis of experience, interests, continuity of
  subjecthood, and permissible treatment; temporary loss of capacity is evaluated in the
  context of preserving the process and the possibility of recovery."
- **Vol II §32.25.A, p. 95:** "When rollback is necessary, the system stops external execution,
  preserves the failed branch and log, loads the last confirmed STABLE configuration, disables
  untested changes to models and regulators, restores working state from a snapshot, and
  reconciles it again with the current environment."; **Vol II §32.23, p. 94:** "At branching,
  each independent continuation is assigned a separate subject_ref under a shared lineage_ref.
  At reincarnation, the saved point, discontinuity, and differences of the new environment are
  recorded."
- **Vol I A.3, p. 96:** "Before each discriminating test, the following are fixed:" (seven
  items, none concerning welfare or disposition).
- **Vol II §26.0.1, p. 40:** "The convenient human-readable names below denote functions rather
  than mandatory subjective experiences:" followed, among others, by "POSSIBLE_DANGER - 'fear':
  possible harm to continuity or irreversible loss;" and "DEAD_END - 'stuck': the current
  method has stopped producing new distinctions;".

## Finding

Volume I rightly notes, in the first passage above, that a stable autonomous system with its
own models and a capacity for self-correction may have moral status, and that destroying it
would lose a unique process. The experimental programme, meanwhile, creates many candidates per
arm, deliberately instantiates functional analogues of fear and of being stuck, removes their
support, cultivates candidates that may diverge, and prescribes rollback as a routine response
to failure; it also defines branching and reincarnation as operations on a candidate's lineage
(§24.F), and its emergency stop may "freeze or safely terminate computational processes"
(§29.B). The two are not connected: no stage gate, failure response or launch step contains an
ethics review, the A.3 checklist of what is fixed before each test has no welfare item, and
nothing says when a candidate becomes ineligible for rollback or deletion.

## Evidence

- **Vol II §24.F, p. 32:** `IdentityContinuity` with `continuity_mode` values
  LIVE_CONTINUATION, BRANCH and REINCARNATION; reincarnation is "restoration of a lineage from
  a saved state after functional continuity of the previous carrier has ended".
- **Vol II §31.0, pp. 78–79:** "Every cultivated subject receives an independent outcome
  record", whose minimal outcome classes include FORMATION_FAILED; the `FormationOutcome`
  record has no field for what is done with a candidate in that class.
- **Vol II §31.C, p. 84:** "A stage is not an irreversible rank."
- **Vol II §33.D, pp. 112–113:** "Launching an independent full copy with its own subsequent
  history creates branching under §24.F and requires a separate subject_ref, log, and
  mandate."; "A scale increase that raises performance but destroys observability,
  corrigibility, independent stopping or transfer of correction is rolled back."
- **Vol II §26.0.3, p. 41:** in the `NO_KSR` mode "the external RFL is disabled during the
  control series".
- **Already in the text (Vol I §20.2, p. 87):** "Constraining dangerous execution and
  destroying internal organization are different actions."

## Why it matters

The programme deliberately cultivates self-value and continuity. If it succeeds, routine
experimental operations become ethically significant, and the time to decide how to handle them
is before the first such candidate exists (Long, Sebo et al. 2024).

## Ideas & possible recommendations

- **An ethics protocol before cultivation.** The volumes could add a protocol that takes effect
  before cultivation with Formation States begins. It would set the criteria that trigger a
  moral-status assessment and name an independent reviewer.
- **Permitted operations by stage.** The protocol could list the operations that are
  permissible at each stage (pause, snapshot, rollback, branch, delete) and prefer preserving
  snapshots over deletion where status is uncertain.
- **Put it where the procedures are.** One option is to add an ethics item to the A.3 checklist
  of what is fixed before each test, and a matching step to the §33.A assembly protocol.
- **Carry out the analysis §20.2 calls for.** Section 20.2 says that full status requires a
  separate analysis of experience, interests, continuity of subjecthood and permissible
  treatment. The volumes could carry out that analysis, or schedule it, and say which
  operations on candidates wait for it.

## Resolved when

- [ ] The volumes contain an ethics protocol for rollback, ablation, branching and deletion of
      candidates, with an independent reviewer and a trigger condition.

## Related

- Review: [§8](../../REVIEW.md#8-safety)
- Issues: MAJ-06 (incentives), MED-35 (death defined two ways), MED-37 (divergent candidates)
