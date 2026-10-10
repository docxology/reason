# Audit register

Every issue found in the audit of *Foundations of Reason 8.0* (Vol I) and *Engineering of
Reason 3.5* (Vol II) has a standalone file in this directory and a GitHub issue with the
same ID. The files are the source of truth; this index and the issues are generated from
them by `scripts/audit_index.py` and `scripts/file_issues.py`. The full argument is in
[`REVIEW.md`](../../REVIEW.md).

**Severity scale**

- **Major**: undermines a central claim, the testability of the programme, or safety. It
  should be resolved before the work is presented as a tested theory or before any stage
  beyond simulation.
- **Medium**: affects a component claim, the clarity of a key construct, or the
  experimental design. It should be resolved before the first comparative experiment or
  journal submission.
- **Minor**: editorial, citation or formatting. It does not change the substance, but
  it costs readers time.

Page and line numbers refer to the English PDFs in `sources/` and the `-layout` text in
`text/`.

**66 issues:** 8 major, 38 medium, 20 minor.

## Major (8)

| ID | Issue | Area | Volumes | Review | GitHub |
|---|---|---|---|---|---|
| [MAJ-01](MAJ-01-no-comparative-evidence.md) | No comparative evidence yet for the central hypothesis | evidence | I, II | §5.2(a), §7, §9 | pending |
| [MAJ-02](MAJ-02-asi-framing-overclaims.md) | The titles promise ASI technology; the content gives no path to ASI | framing | I, II | §4.3, §7, §10.5 | pending |
| [MAJ-03](MAJ-03-decision-rule-closed-world.md) | The Core's only committed decision rule covers closed, fully specified problems | architecture | I, II | §5.2(f), §5.3 | pending |
| [MAJ-04](MAJ-04-no-transfer-mechanism.md) | No mechanism that produces transfer of corrections and inquiry methods | architecture | I, II | §5.3, §7 | pending |
| [MAJ-05](MAJ-05-formation-experiment.md) | The formation experiment cannot yet attribute internalization to the RFL | testability | I, II | §4.2(a), §7 | pending |
| [MAJ-06](MAJ-06-incentive-analysis.md) | No design-level analysis of the incentives the architecture creates | safety | I, II | §8 | pending |
| [MAJ-07](MAJ-07-prior-work-missing.md) | The closest prior work is missing from the chapters | prior-art | I, II | §6, §6.1, §7, Appendix B | pending |
| [MAJ-08](MAJ-08-value-sum-compensatory.md) | The value sum is compensatory and risk-neutral, and the critical-loss safeguard is undefined | safety | II | §4.2(d), §8 | pending |

## Medium (38)

| ID | Issue | Area | Volumes | Review | GitHub |
|---|---|---|---|---|---|
| [MED-01](MED-01-near-analytic-necessities.md) | The model's necessities are mostly near-analytic, and its two empirical ones overreach | theory | I | §2.2 | pending |
| [MED-02](MED-02-compass-not-load-bearing.md) | The Compass's derivation does no work in the engineering and faces the is-ought gap | theory | I, II | §2.3, §9 | pending |
| [MED-03](MED-03-reason-overloaded.md) | "Reason" names both a functional profile and a normative orientation | definitions | I, II | §2.4, §3 | pending |
| [MED-04](MED-04-consciousness-terminology.md) | "Consciousness" and "causal" carry meanings that invite misreading | definitions | I, II | §2.5 | pending |
| [MED-05](MED-05-roles-not-kinds.md) | Intelligence and Reason are roles, not kinds, and the boundary belongs across episodes | definitions | I, II | §3 | pending |
| [MED-06](MED-06-semantic-bridge-error-model.md) | The language-to-structure bridge has no measured error model | architecture | I, II | §4.2(b) | pending |
| [MED-07](MED-07-own-worldview-scope.md) | Inherited ontology cannot yet be told apart from an "own" Worldview | architecture | II | §4.2(c) | pending |
| [MED-08](MED-08-designer-chosen-values.md) | Initial values are designer-chosen, so cultivation tests calibration rather than value formation | theory | II | §4.2(d) | pending |
| [MED-09](MED-09-ceiling-risk.md) | The first environment risks a ceiling effect, and no external benchmark is planned | testability | I, II | §5.2(b), §10.2 | pending |
| [MED-10](MED-10-process-vs-outcome-metrics.md) | Process-conformance metrics are not separated from outcome metrics | testability | II | §5.2(c) | pending |
| [MED-11](MED-11-protocol-not-preregistration-ready.md) | The first series has the right slots but no preregistered instance | testability | I, II | §5.2(a), §10.2 | pending |
| [MED-12](MED-12-failure-condition-qualitative.md) | The failure condition for the Core is stated only qualitatively | testability | I, II | §5.2(d), §9, §10.2 | pending |
| [MED-13](MED-13-stopping-rule-myopic.md) | The one-step stopping test recurs where §28.D says it fails | formal | I, II | §5.2(f) | pending |
| [MED-14](MED-14-active-inference-engagement.md) | Active inference, the closest formal competitor, is engaged only in an appendix | prior-art | I, II | §6.1 | pending |
| [MED-15](MED-15-version-churn.md) | The text is revised faster than evidence accumulates | provenance | I, II | §7, §9, §10.1 | pending |
| [MED-16](MED-16-moral-status-ethics-review.md) | Moral status is raised, but rollback, branching and deletion have no ethics procedure | safety | I, II | §8 | pending |
| [MED-17](MED-17-governance-transfer.md) | Competence mandates lack an issuer, auditor and revocation path, and their aggregate effect is unanalysed | safety | I, II | §8 | pending |
| [MED-18](MED-18-corrigibility-sense.md) | "Corrigibility" means correctability, not deference to an operator | definitions | I, II | §8 | pending |
| [MED-19](MED-19-model-filled-significance.md) | Significance assessments filled by the language model have no accuracy test | architecture | I, II | §5.3 | pending |
| [MED-20](MED-20-readability.md) | Coined vocabulary and length are the main barrier to review | editorial | I, II | §7, §10.9, Appendix A | pending |
| [MED-21](MED-21-compass-two-criteria-grounding.md) | The Compass has two non-equivalent top-level criteria, and its grounding clause is analytic or false | theory | I, II | §2.3 | pending |
| [MED-22](MED-22-gap-taxonomies.md) | Unreconciled taxonomies of gap type | definitions | I, II | §5.3 | pending |
| [MED-23](MED-23-historical-materials-unpublished.md) | The pilot log, task packages and AI priority audits are cited but not published | provenance | I, II | §6, §7 | pending |
| [MED-24](MED-24-metric-definitions.md) | Many metrics lack formulas, denominators and thresholds | testability | II | §5.2(c) | pending |
| [MED-25](MED-25-core-ablation-capability-sweep.md) | No defined ablation of the Core when one model plays both roles, and no capability sweep | testability | II | §3, §5.2(f) | pending |
| [MED-26](MED-26-operational-core-formulas.md) | The Operational Core formulas are incomplete and inconsistent with Vol II | formal | I, II | §2.1, §5.2(f) | pending |
| [MED-27](MED-27-compass-decompositions.md) | Three operational decompositions of the Compass coexist without a mapping | definitions | II | §2.3 | pending |
| [MED-28](MED-28-epistemic-gate-uncomputable.md) | The epistemic gate and EpistemicMargin cannot be computed | safety | II | §8 | pending |
| [MED-29](MED-29-vocabularies-disagree.md) | Status vocabularies, enumerations and outcome classes disagree across sections | definitions | I, II | §5.2(e) | pending |
| [MED-30](MED-30-safe-mode-only-through-drift.md) | The mode state machine reaches SAFE_MODE only through DRIFT | safety | II | §8 | pending |
| [MED-31](MED-31-authorization-contract-override-and-delay.md) | The authorization contract lets the external gate override internal refusal and delays restrictions | safety | II | §8 | pending |
| [MED-32](MED-32-override-criterion-no-adjudicator.md) | The AR override criterion and the licence for irreversible loss lack an adjudicator | safety | I | §8 | pending |
| [MED-33](MED-33-cumulative-drift-and-entrenchment.md) | Cumulative drift of criteria is unbounded, and a persistent AR has no guard against entrenchment | safety | I, II | §4.3, §8 | pending |
| [MED-34](MED-34-component-controls-lack-baselines.md) | Component controls lack baselines, outcomes and degenerate-policy checks | testability | II | §5.2(a) | pending |
| [MED-35](MED-35-load-bearing-terms-defined-late-or-twice.md) | Load-bearing terms are defined late, inconsistently or not at all | definitions | I | §2.1, Appendix A | pending |
| [MED-36](MED-36-revision-ladder-single-locus.md) | The revision ladder assumes a single causal locus, and its escalation rules conflict | theory | I, II | §7 | pending |
| [MED-37](MED-37-no-containment-for-divergent-candidates.md) | No containment or disposition rule for candidates that diverge from the Compass | safety | I, II | §8 | pending |
| [MED-38](MED-38-failure-catalogue-not-a-detector.md) | The failure catalogue cannot be applied as a detector | safety | II | §8 | pending |

## Minor (20)

| ID | Issue | Area | Volumes | Review | GitHub |
|---|---|---|---|---|---|
| [MIN-01](MIN-01-duplicate-paragraphs.md) | Near-duplicate paragraphs in Volume I | editorial | I | Appendix A | pending |
| [MIN-02](MIN-02-truncated-sentences.md) | Truncated sentences in Volume I | editorial | I | Appendix A | pending |
| [MIN-03](MIN-03-list-numbering.md) | Lists are numbered across sections or restart mid-list | editorial | I, II | Appendix A | pending |
| [MIN-04](MIN-04-broken-cross-references.md) | Cross-references that do not resolve | editorial | I, II | Appendix A | pending |
| [MIN-05](MIN-05-untranslated-ksr.md) | Untranslated abbreviation "KSR" and inconsistent RFL mode names | editorial | I, II | Appendix A | pending |
| [MIN-06](MIN-06-bibliography-errors.md) | Bibliography errors and incomplete entries | references | I, II | Appendix A, Appendix B | pending |
| [MIN-07](MIN-07-doubled-headings.md) | Headings printed twice and lists collapsed | editorial | I | Appendix A | pending |
| [MIN-08](MIN-08-code-listings.md) | The printed code listings cannot be run as printed, and their checks are weaker than described | code | II | §5.4, Appendix A | pending |
| [MIN-09](MIN-09-inconsistent-titles.md) | Each volume carries different titles in the PDF, on Zenodo and in the author's references | provenance | I, II | Header, §10.5 | pending |
| [MIN-10](MIN-10-tool-disclosure.md) | No statement of the tools used for drafting, translation and typesetting | provenance | I, II | Appendix B | pending |
| [MIN-11](MIN-11-contents-vs-headings.md) | Contents pages disagree with the headings they list | editorial | I, II | Appendix A | pending |
| [MIN-12](MIN-12-orphan-records-no-slice.md) | Many record types are never used, and no minimal component slice is named | testability | I, II | §5.2(e), §10 | pending |
| [MIN-13](MIN-13-symbol-collisions.md) | Symbols collide across formulas, and the formulas are not typeset | formal | I, II | Appendix A | pending |
| [MIN-14](MIN-14-layout-artefacts.md) | Layout artefacts: raw diagram source, stray rules, leaked markup and flattened tables | editorial | I, II | Appendix A | pending |
| [MIN-15](MIN-15-term-drift.md) | Defined terms change name and capitalization | editorial | I, II | Appendix A | pending |
| [MIN-16](MIN-16-undefined-abbreviations.md) | Abbreviations and names are used without definition | definitions | I, II | Appendix A | pending |
| [MIN-17](MIN-17-pseudocode-and-parameters.md) | Defects in pseudocode, parameters and the reproducibility rule | code | II | §5.4 | pending |
| [MIN-18](MIN-18-uncited-methods.md) | Borrowed methods and claims lack citations | references | I, II | §6 | pending |
| [MIN-19](MIN-19-outlook-without-tests.md) | Outlook sections present hypotheses without tests | framing | I, II | §9 | pending |
| [MIN-20](MIN-20-append-only-vs-retention.md) | The log is called append-only, but a retention policy allows deletion | definitions | II | Appendix A | pending |
