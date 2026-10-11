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

**Finding.** The volumes enumerate the same constructs in different ways, and four mismatches
change how a test would be scored. (1) The five formation outcome classes have no assignment
rule, so the denominators the text commits to cannot be computed. (2) The links whose
ablation defines causal closure number seven, seven, nineteen or four. (3) A revision
transaction has four different outcome lists. (4) SUPPORTED belongs to three lists, and the
status rules use symbols outside them. Similar mismatches affect Worldview membership,
ConsciousAssemblyState and CurrentCoordinate fields, and the correction ladder (MED-36).

## Evidence

- **Vol II §31.0, p. 79, and §29.C, p. 73:** FormationOutcome has six `*_status` fields with
  no value sets and no field for the class; its "compass_relation: ACCEPTED / QUESTIONED /
  DIVERGED / UNRESOLVED" differs from "candidate_compass_stance: ACCEPTED / QUESTIONED /
  REJECTED / ALTERNATIVE_PROPOSED".
- **Vol II §31.7, §31.11, §33.C, §27.6 (pp. 81, 83, 108, 47):** seven links ("breaking
  assembly -> coordinate"), another seven ("Ablations test the links coordinate ->
  significance"), nineteen arrows ("Every arrow has an observable trace and a separate
  ablation") and "four causal tests".
- **Vol II §24.A.1, §24.D, §28.C, App. A.2 (pp. 21, 28, 59, 117):** "COMMIT /
  KEEP_AS_HYPOTHESIS / SPLIT_CONTEXT / REJECT"; six values in §24.D, adding
  REQUEST_MORE_EVIDENCE and ROLLBACK; "COMMIT / HOLD_AS_HYPOTHESIS / REQUEST_MORE / REJECT";
  "COMMIT / REJECT / DEFER / ROLLBACK".
- **Vol II §24.D, §24.A.1, §25.D (pp. 28, 21, 38):** SUPPORTED is a value of "HYPOTHESIS /
  SUPPORTED / CONTRADICTED / UNKNOWN", of "PROVISIONAL / TESTING / SUPPORTED / REJECTED /
  SPLIT" and of "SUPPORTED / NOT_SUPPORTED / INCONCLUSIVE"; "GENERATED_TEXT != WORLD_CLAIM"
  uses symbols that belong to none of them.
- **Vol I §20.1.1, p. 84; Vol II §26.0.1, p. 40:** five Formation State classes ("possible
  danger" to "dead end of the current method") against seven, adding "UNRESOLVED_IMPORTANCE"
  and "NEED_EXPLANATION".
- **Already in the text (Vol II §31.0, p. 79):** a divergent candidate "is not removed from
  metric denominators".

## Why it matters

These inventories set the denominators and manipulated variables of the formation experiment
and the closure ablations.

## Recommendation

Publish one enumeration per construct, with a transition table for statuses. Add a
deterministic table from the FormationOutcome fields to the five classes, one canonical
closure link list, and one Formation State inventory that both volumes use. Treat ROLLBACK as
an operation and remove it from the decision list.

## Resolved when

- [ ] FormationOutcome has value sets and a rule that assigns each candidate to one class.
- [ ] Closure links, revision outcomes and statuses each have a single enumeration.

## Related

- Review: [§5.2(e)](../../REVIEW.md#52-what-still-stands-between-the-specification-and-a-test)
- Issues: MAJ-05 (removal arms), MED-28, MED-36
