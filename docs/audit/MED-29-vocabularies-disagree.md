---
id: MED-29
title: Status vocabularies, enumerations and outcome classes disagree across sections
severity: medium
area: definitions
volumes: I, II
sections: Vol I §20.1.1; Vol II §24.A.1, §24.D, §25.D, §26.0.1, §27.6, §28.C, §29.C, §31.0, §31.7, §31.11, §33.C, App. A.2
review: §5.2(e)
status: open
github_issue: 37
---

# MED-29 · Status vocabularies, enumerations and outcome classes disagree across sections

## Claims under review

- **Vol II §31.0, pp. 78–79:** "Every cultivated subject receives an independent outcome
  record"; "Minimal outcome classes: AR_ADMITTED, SELF_NAVIGATING_OTHER_ORIENTATION,
  DEPENDENT_SYSTEM, FORMATION_FAILED, INDETERMINATE."
- **Vol II §31.11, p. 83:** "Ablations test the links coordinate -> significance, significance
  -> GapCandidate, GapCandidate -> FoundationGap, gap -> distinction, evidence -> revision,
  consequence -> new state, and new state -> next process." **Vol II §33.C, p. 108:** "Every
  arrow has an observable trace and a separate ablation."
- **Vol II §24.D, p. 28:** "A candidate may terminate as COMMIT, KEEP_AS_HYPOTHESIS,
  REQUEST_MORE_EVIDENCE, SPLIT_CONTEXT, REJECT or ROLLBACK." **Vol II App. A.2, p. 117:**
  "authorization decision COMMIT / REJECT / DEFER / ROLLBACK"
- **Vol II §24.D, p. 28:** "status: OBSERVED / REPORTED / INFERRED / SIMULATED / HYPOTHESIS /
  SUPPORTED / CONTRADICTED / UNKNOWN"; "GENERATED_TEXT != WORLD_CLAIM, SIMULATED_OUTCOME !=
  OBSERVATION, and HIGH_CONFIDENCE != SUPPORTED". **Vol II §24.A.1, p. 21:** "status:
  PROVISIONAL / TESTING / SUPPORTED / REJECTED / SPLIT"

## Finding

The volumes enumerate the same constructs in different ways, as the claims above show, and four
mismatches change how a test would be scored. (1) The five formation outcome classes have no
assignment rule, so the denominators the text commits to cannot be computed. (2) The links
whose ablation defines causal closure number seven, seven, nineteen or four. (3) A revision
transaction has four different outcome lists. (4) SUPPORTED belongs to three lists, and the
status rules use symbols outside them. Similar mismatches affect Worldview membership,
ConsciousAssemblyState and CurrentCoordinate fields, and the correction ladder (MED-36).

## Evidence

- **Vol II §31.0, p. 79, and §29.C, p. 73:** FormationOutcome has six `*_status` fields with no
  value sets and no field for the class; its "compass_relation: ACCEPTED / QUESTIONED /
  DIVERGED / UNRESOLVED" differs from "candidate_compass_stance: ACCEPTED / QUESTIONED /
  REJECTED / ALTERNATIVE_PROPOSED".
- **Vol II §31.7, §33.C, §27.6 (pp. 81, 108, 47):** §31.7 names seven links of its own, from
  "breaking assembly -> coordinate" to "updated ground -> choice"; §31.11 names seven others;
  the chain in §33.C has nineteen arrows; and §27.6 says "The AR boundary uses four causal
  tests rather than dozens of independent numbers".
- **Vol II §24.A.1, §28.C (pp. 21, 59):** two further lists of revision outcomes: "COMMIT /
  KEEP_AS_HYPOTHESIS / SPLIT_CONTEXT / REJECT" in the cycle of relation formation, and "COMMIT
  / HOLD_AS_HYPOTHESIS / REQUEST_MORE / REJECT" as the consolidation_directive of
  CoreSufficiencyAssessment. The six values of §24.D add REQUEST_MORE_EVIDENCE and ROLLBACK to
  the four of §24.A.1, and only COMMIT and REJECT occur in all four lists.
- **Vol II §25.D, p. 38:** SUPPORTED is also a value of a third list, "result: SUPPORTED /
  NOT_SUPPORTED / INCONCLUSIVE". In the rule quoted above from §24.D, GENERATED_TEXT and
  WORLD_CLAIM belong to none of the three lists.
- **Vol I §20.1.1, p. 84; Vol II §26.0.1, p. 40:** Vol I names five Formation State classes:
  "possible danger, possible favorable outcome, significant unknown, contradiction, and dead
  end of the current method". Vol II lists seven, adding UNRESOLVED_IMPORTANCE and
  NEED_EXPLANATION.
- **Already in the text (Vol II §31.0, p. 79):** a divergent candidate "is not removed from
  metric denominators".

## Why it matters

These inventories set the denominators and manipulated variables of the formation experiment
and the closure ablations.

## Ideas & possible recommendations

- **One enumeration per construct.** Each construct could be published once, with a transition
  table for statuses, and ROLLBACK could be treated as an operation and removed from the
  decision list.
- **A deterministic class table.** A table from the FormationOutcome fields to the five classes
  would make the denominators computable.
- **One canonical closure link list.** A single list of links could serve the closure ablations
  in §§27.6, 31.7, 31.11 and 33.C.
- **One Formation State inventory.** A single inventory could be used by both volumes.

## Resolved when

- [ ] FormationOutcome has value sets and a rule that assigns each candidate to one class.
- [ ] Closure links, revision outcomes and statuses each have a single enumeration.

## Related

- Review: [§5.2(e)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test)
- Issues: MAJ-05 (removal arms), MED-28, MED-36
