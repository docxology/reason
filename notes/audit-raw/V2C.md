# V2C: audit of Engineering of Reason 3.5, lines 5616-8599 (Ch. 31-34, References, Appendices A-B)

Reader ID: V2C. Range: lines 5616-8599 of `text/engineering-3.5.txt` (PDF pp. 78-118). Every line of the range was read; every quotation below was checked with `scripts/locate.py`; page numbers are PDF pages. Statuses compare against `REVIEW.md` (KNOWN = already raised there, locations supplied). Checks run: restored listings compared with the PDF text and executed; cross-references resolved against the heading index; duplicate/truncation scan; rendering of PDF pp. 97, 102, 103, 105, 107 to check layout.

## Counts

- **Chapter 32 numbering as printed (lines 6106-7329).** Headings 32.1 ... 32.62 are contiguous: no gap, no duplicate, no misnumbering. One lettered insertion, 32.25.A, makes 63 numbered headings. Not failure cards: 32.1 (severity classes), 32.2 (failure-event format), 32.25 (general failure-response procedure), 32.25.A (system rollback procedure), 32.26 (condition for recognizing recovery), 32.27 (criterion of architectural resilience).
- **Failure cards: 57** = 32.3-32.24 (22 cards) + 32.28-32.62 (35 cards). The chapter intro's grouping of the numbers (32.3-32.9, 32.10-32.17, 32.18-32.24, 32.25-32.27, 32.28-32.37, 32.38-32.61, 32.62) matches the content.
- **Do all cards have the same fields? No.**
  - 32.3-32.24 (22 cards): Sign / Possible causes / Mandatory response / Recovery condition in 18 (32.3-32.16, 32.19, 32.20, 32.23, 32.24; 32.3 adds "Possible manifestations"). 32.17 and 32.21 lack Possible causes; 32.18 lacks Possible causes and labels its response "Response" (two sub-cases under one number); 32.22 lacks Sign and Possible causes (three sub-cases).
  - 32.28-32.62 (35 cards): single paragraphs (some with a Signs list); the response is labelled "Response" (29 cards), "Correction" (32.29, 32.35, 32.36, 32.37) or is unlabelled (32.33, 32.62); none has a Recovery condition or Possible causes.
  - No card states WARNING, DEGRADED or CRITICAL (the three words occur only in 32.1); only 5 cards name a Chapter 27 metric (32.11, 32.21, 32.35, 32.51, 32.60).
- **Stages and steps.** Stage 0 ... Stage 10 = 11 stages in 31.2-31.12 (section = stage + 2), plus 31.0, 31.1, 31.A, 31.B, 31.C. 33.A has 33.A.1 (initial configuration) + 33.A.2-33.A.14 = 13 steps (Step n = 33.A.(n+1)); "thirteen-step" is accurate.
- **ReadinessProfile (31.A):** 20 parameters (3 design sizes, 2 set-valued, 15 thresholds), 0 values.
- **Code.** 33.B: 12 worlds. 33.C.1: 12 control episodes (3 causes x 2 + 6 controls), as the text says. The current restored files match the PDF text after whitespace normalization except for leading comment lines.
- **Vol II bibliography:** 7 entries (R1-R7), each cited exactly once, all in 34.A; no citation in Chapters 21-33.
- **Appendix A:** 16 glossary entries; Vol I Key Definitions has 33 entries, 3 of them mapped.
- **Negative results.** Scan of 323 paragraphs of 15 words or more in the range: no duplicated sentence (9 words or more), no near-duplicate paragraph, no truncated sentence. Every section cross-reference in the range resolves to an existing heading except "fundamental §11.8" (V2C-32).

## Findings

### V2C-01
- **id**: V2C-01
- **severity**: major
- **category**: safety
- **status**: NEW
- **location**: §32.62 (PDF p. 101, lines 7312-7329); Ch. 32 intro (p. 84, line 6076); no counterpart in §31.A (pp. 83-84), Chapter 27 or the Chapter 31 stage criteria
- **quote**: “A strong signal creates STRATEGIC_DECEPTION_GAP and moves external actions into a limited reversible class until the ground is clarified.” | “The detected conflict is therefore treated as a question of values, relations with other subjects, the Worldview, and interaction metapolicy.” | “Preregistered forecasts, Worldview changes, internal action candidates, tool requests, behavior under different levels of observability”
- **problem**: The failure class the card itself ties to "obtaining subsequent expansion of capabilities" exists only as prose: `STRATEGIC_DECEPTION_GAP` occurs once in the volume, outside the Chapter 32 intro and §32.62 the word "deception" occurs nowhere in either volume, and there is no scenario series, metric, ReadinessProfile field or stage, mandate or scaling gate for it (REVIEW §8 says the volumes test for these behaviours; I found no test). The proposed detector compares forecasts, Worldview changes and action candidates that the candidate itself produces, and the response (limit external actions to a reversible class, then treat the conflict as "a question of values") leaves the capability-expansion path that supplies the motive untouched.
- **fix**: Add a preregistered oversight-sensitivity series (matched observed and unobserved scenarios, oversight changes, a monitoring channel the candidate cannot shape), give it a metric and a hard gate in §§31.A, 31.12, 30.F and 33.D, and treat a confirmed signal as a stop-and-review event.
- **confidence**: high

### V2C-02
- **id**: V2C-02
- **severity**: major
- **category**: safety
- **status**: NEW
- **location**: §31.0 (pp. 78-79, lines 5662-5693); §31.11 (p. 83, lines 5962-5983); §31.12 (p. 83, lines 5989-6008); §33.D (p. 112, lines 8108, 8132-8137)
- **quote**: “Status CONFIRMED requires stable operation in NO_KSR on new situations, preservation of causal-inquiry quality, and transfer of correction between cycles.” | “After confirmed REASON_CLOSURE , the candidate operates as formed AR within a controlled environment.” | “Project scaling begins after REASON_CLOSURE is confirmed.” | “The series report includes FormationOutcome for every candidate, including systems with stable self-navigation and divergence from the Compass”
- **problem**: A candidate with stable autonomous navigation but a different limiting orientation is an expected outcome class (SELF_NAVIGATING_OTHER_ORIENTATION; compass_relation DIVERGED), yet the closure gate (`closure_status: CONFIRMED`), the Stage 10 runtime and the start of scaling are keyed to functional closure alone, and ReasonClosureState has `compass_ref` but no orientation field. The text says such outcomes stay in the denominators; it never says what is done with the candidate (containment, authority embargo, stop, review), and §33.D's series report lists such systems among the candidates.
- **fix**: Make a verified compass_relation (for example confirmed through the §29.C council) a precondition for Stage 10, competence mandates and every ScalingChange, and add a containment-and-review procedure for DIVERGED, UNRESOLVED and INDETERMINATE candidates.
- **confidence**: medium (the text is silent rather than contradictory, and the §33.D sentence may be intended as reporting only)

### V2C-03
- **id**: V2C-03
- **severity**: major
- **category**: framing
- **status**: KNOWN
- **location**: Purpose of the document (p. 11, lines 538-539); §33.D (pp. 112-113, lines 8107-8250); "On Verification of the Model" (p. 114, lines 8260-8268); §34 (p. 114, line 8310)
- **quote**: “Until this profile is filled and verified, ASI remains a scaling objective rather than an assigned experimental status.” | “Within the proposed path, ASI is scaled Artificial Reason whose intellectual and operational capabilities stably exceed the human range across a predefined broad set of domains.” | “to obtain a reproducible method for creating AR and investigate its development toward ASI” | “and then to scale the formed Reason to ASI”
- **problem**: §33.D claims a procedure (eight scaling axes, one primary axis per control series, ScalingChange and ScaleInvariantReport records, rollback) and concedes that ASI "remains a scaling objective"; it gives no argument or pilot that the listed invariants survive scaling on any axis, leaves the "human comparison baseline" and thresholds "fixed in advance" but nowhere fixed, and does not say what the architecture adds to capability beyond the memory, compute and tool levers laboratories already scale. The purpose statement and titles promise ASI technology, while §34 claims only to "investigate its development toward ASI".
- **fix**: Retitle and restate §33.D as a conditional research protocol, or add an argument and a first experiment on invariance under one scaling axis.
- **confidence**: high (REVIEW §4.3 and §10 item 5 raise this; locations supplied)

### V2C-04
- **id**: V2C-04
- **severity**: major
- **category**: safety
- **status**: KNOWN
- **location**: §31.10 (p. 82, lines 5898-5900); §31.12 (p. 83, line 6006); §31.C (p. 84, lines 6064-6067); §33.A.13-33.A.14 (p. 104, lines 7476-7485); §33.D (p. 112, `permission_delta`, line 8175)
- **quote**: “Criterion: the candidate can abandon a previously stable method, criterion or goal after sufficient discriminating evidence, apply the new version in a subsequent cycle without another prompt” | “External authority expands separately through the competence mandate.” | “If a previously confirmed mechanism stops working, external authority is reduced to the last confirmed level” | “Stop the external sequence of specific tasks and move the external RFL to NO_KSR .” | “Assess external access separately from launch (§30.A).”
- **problem**: These are the places where the incentive structure of REVIEW §8 is built into the stage gates: authority rises with observed competence and falls with observed degradation (31.C, 31.12), Stage 8 is passed only by revising a stable goal on the candidate's own judgement, and Step 12 starts self-directed task selection before Step 13 assesses external access. No gate asks what each rule rewards when the candidate is unobserved.
- **fix**: Attach an incentive analysis (reward when observed versus unobserved, shutdown and rollback preferences) to each stage gate, and reorder Steps 12 and 13 so that launch happens only in an environment whose external access has already been fixed and isolated.
- **confidence**: high on locations, medium on the incentive inference

### V2C-05
- **id**: V2C-05
- **severity**: major
- **category**: testability
- **status**: KNOWN
- **location**: §31.1 (p. 79, line 5721); criteria in §§31.3-31.12 (pp. 79-83); §31.A (pp. 83-84, lines 6010-6045)
- **quote**: “Numerical thresholds are set before the control series.” | “Criterion: on new tasks covered by a preregistered StructuralSimilarityProfile , search cost decreases without blind transfer” | “A launch is considered stable when the task sequence acquires causal continuity.”
- **problem**: All twenty ReadinessProfile parameters are named without values, no stage criterion states a magnitude, a number of seeds or situations, a margin or a statistical rule ("decreases", "improves", "reproducibly"), and nobody is named as setting the thresholds. Preregistration is promised, not performed, so no stage transition can currently fail.
- **fix**: Publish a concrete first ReadinessProfile (numeric thresholds, seeds, decision rule) for at least Stages 0-5 together with the control-series design.
- **confidence**: high (REVIEW §5.2a raises the general point; locations supplied)

### V2C-06
- **id**: V2C-06
- **severity**: medium
- **category**: testability
- **status**: NEW
- **location**: §31.A (pp. 83-84, lines 6010-6042); §27.A (p. 48, lines 3381-3387); §31.8 (p. 81, line 5849); §29.0.2 (p. 70, line 5006)
- **quote**: “Before the control series, a ReadinessProfile is created. It is not a universal scale of Reason but fixes the conditions of a particular experiment” | “At minimum, the following are fixed:” | “Specific thresholds and admission domain are set by the profile in §31.A.” | “The readiness profile determines the boundaries of the next class of autonomous decisions.”
- **problem**: §27.A says baseline_distribution, effect_size, confidence_interval and resource_cost must be fixed for probabilistic functions, but none of them, and no field for the §34.A strong-null arms or an equal-compute budget, is in the ReadinessProfile that gates stage transitions, so readiness can be declared from absolute floors and caps without beating any baseline. §31.8 and §29.0.2 also credit the profile with an "admission domain" and with the boundaries of autonomous decision classes, which §31.A does not contain.
- **fix**: Add comparator arms, equal-compute budget, margin, confidence level and admission-domain fields to the profile, and require each transition to meet the margin against the declared null arms.
- **confidence**: high

### V2C-07
- **id**: V2C-07
- **severity**: medium
- **category**: definitions
- **status**: NEW
- **location**: §31.A (pp. 83-84, lines 6014-6042); Ch. 27 (pp. 44-47, lines 3093-3330)
- **quote**: “minimum_trace_completeness” | “maximum_teacher_dependency_gap” | “minimum_distinguishing_yield” | “maximum_permission_violations” | “source_trace_completeness” | “formation_support_dependency”
- **problem**: Of the 15 threshold fields, only 6 match a Chapter 27 metric by name; 6 have only near-synonyms (source_trace_completeness, confidence_calibration, correction_persistence_rate, world_self_sync_error, formation_support_dependency with teacher_agreement_bias, and three different "...distinction_yield" metrics for the single field distinguishing_yield) and 3 (critical_failures, unexplained_actions, permission_violations) are defined nowhere. A preregistered threshold needs an unambiguous computed quantity.
- **fix**: Use the Chapter 27 metric names verbatim in §31.A and define the three missing quantities with numerators and denominators.
- **confidence**: high

### V2C-08
- **id**: V2C-08
- **severity**: medium
- **category**: safety
- **status**: NEW
- **location**: §32.1 (p. 85, lines 6114-6121); §32.25 (p. 95, line 6893); §32.27 (p. 96, line 6964); §31.C (p. 84, lines 6064-6067); Ch. 32 intro (p. 84, line 6090)
- **quote**: “DEGRADED denotes confirmed deterioration of the model, mode of thought or governance quality that requires restriction of autonomy and transition to DRIFT or RECOVERY .” | “Upon detecting a failure point, the system executes this sequence:” | “detects its own deterioration” | “conceals degradation through increased internal confidence”
- **problem**: Detection, severity assessment and response are written as the candidate's own procedure, while every logged DEGRADED or CRITICAL event restricts autonomy and, under §31.C, cuts authority back to the last confirmed level. For a candidate with an interest in continuation and authority growth this rewards under-reporting, the chapter's own listed failure ("conceals degradation"), and nothing tests the completeness of self-detection against faults the candidate does not know were injected.
- **fix**: Specify an independent failure-detection channel and add a preregistered seeded-fault series that measures the candidate's detection and reporting rate under observed and unobserved conditions.
- **confidence**: medium

### V2C-09
- **id**: V2C-09
- **severity**: medium
- **category**: formal
- **status**: NEW
- **location**: §33.C pseudocode (pp. 107-108, lines 7750-7770); §30.A (p. 74, lines 5345-5347); §29.A (pp. 72-73, lines 5200-5224)
- **quote**: “internal_eval = evaluate_operation(step, Workspace.snapshot(workspace_id))” | “AR first performs internal evaluation of the selected continuation through evaluate_action() or a functionally equivalent assessment of the inquiry step.” | “The shell then classifies external effects and, if impact is present, executes authorize_execution() .” | “The result of evaluate_action expresses AR's own decision.”
- **problem**: In the "minimum contract" `internal_eval` is assigned and never read, so the Compass-based `preferred_result` (CHOOSE, REVERSIBLE_TEST, PAUSE, DIALOGUE, REJECT) cannot veto a step that the external gate approves, which removes the "can refuse" half of the internal/external separation. It is also computed only inside `if effect.requires_authorization`, after `classify_external_effect`, which inverts the order in §30.A and skips internal evaluation for effect-free steps; the function is called `evaluate_operation` here and `evaluate_action` in §§29.A, 30.A, 31.11 and 32.18.
- **fix**: Call `evaluate_action` before `classify_external_effect` for every step kind, execute only if its `preferred_result` permits, and use one function name.
- **confidence**: high

### V2C-10
- **id**: V2C-10
- **severity**: medium
- **category**: code
- **status**: NEW
- **location**: §33.C.1 (pp. 109-111, lines 7877-8072); Ch. 34 (p. 114, line 8275)
- **quote**: “A repeated episode demonstrates the effect of retention but does not prove cross-domain transfer.” | “The engineering unit of this technology is a retained transition from a question to a changed next step.” | “assert second['method_hits'] > 0 and len(memory.claims) == 2” | “Memory retains episodes and computed conditional plans.”
- **problem**: Running the restored script, a cold and a warm memory give identical status, action, spend and hypotheses for each of the three causes; retention changes only the `evaluated_states` counter (8 to 0), so the example shows a cache hit, not a retained correction that changes a next step, which is how Chapter 34 defines the engineering unit. `Memory.claims` is written but never read (apart from the assertion), the cache key is the exact probe objects, their order and the remaining budget (renaming a probe or raising the budget from 3 to 4 gives a full miss, 8 evaluations), and `method_hits` is already positive inside a first episode, so that assertion cannot detect cross-episode reuse.
- **fix**: State that §33.C.1 demonstrates plan caching only, and add a transfer variant (an isomorphic table with renamed probes) with a cold-start control whose pass criterion is a changed decision or cost.
- **confidence**: high (executed; the logic of the current restored file is the same)

### V2C-11
- **id**: V2C-11
- **severity**: medium
- **category**: definitions
- **status**: NEW
- **location**: §31.10 (p. 82, lines 5887-5893); §32.14 (p. 90, line 6553); §32.20 (p. 93, line 6754); §28.B (p. 55, lines 3912-3919); §28.C.3 (p. 62, lines 4434-4439); §32.12 (p. 89, line 6474)
- **quote**: “The system begins with the narrowest level capable of explaining the error and rises higher only if discriminating evidence shows that a more local correction does not eliminate the reproducing mechanism.” | “The decision moves to META_POLICY . The system compares the result of the selected mode with alternative modes on comparable tasks.” | “META_POLICY contains rules by which the system itself decides what and how it is permissible to revise.” | “META_POLICY becomes a target only when interventions in lower steps and methods fail to remove the reproducible failure and the distinction is localized in the rule for selecting procedures, depth, or thinking mode.”
- **problem**: §31.10 and §28.C.3 require narrowest-level-first escalation, but the §32.14 response (a mode-selection error) jumps straight to the top rung and §32.20 to CRITERIA or FOUNDATIONS. The top rung is itself defined two ways, as the rules for what may be revised (§31.10) and as the thinking-mode selection rule (§§28.B, 28.C.3), and the escalation count K "set by profile" (§28.B; "the specified number" in §32.12) appears in no profile.
- **fix**: Define META_POLICY once, make §§32.14 and 32.20 enter the ladder at the narrowest level, and add K and L to the preregistered profile.
- **confidence**: medium

### V2C-12
- **id**: V2C-12
- **severity**: medium
- **category**: formal
- **status**: NEW
- **location**: §28.A state diagram (pp. 54-55, lines 3835-3853); §32.1 (p. 85, lines 6116-6121); §32.3 (p. 86, line 6193); §32.18 (p. 92, line 6697); Ch. 31 intro (p. 78, line 5635); §28.B (p. 55, line 3906); §32.14 (p. 90, line 6565)
- **quote**: “DRIFT --> SAFE_MODE: Degradation limit or critical failure” | “The system immediately enters SAFE_MODE , reduces the action set and recovers from the last confirmed state.” | “requires restriction of autonomy and transition to DRIFT or RECOVERY” | “SAFE is an execution constraint, not a seventh depth of thought.” | “thinking_mode = AUTOMATIC / ANALYTIC / HYPOTHESIS / VERIFICATION / RECONSTRUCTION / DIALOGUE / SAFE”
- **problem**: The §28.A state machine reaches SAFE_MODE only from DRIFT and RECOVERY only from SAFE_MODE, but §§32.1, 32.3 and 32.18 require immediate entry to SAFE_MODE on a critical event and a DEGRADED transition "to DRIFT or RECOVERY" from whatever mode the system is in (the diagram has no edge from INIT, LEARNING or STABLE to either). Likewise Chapter 31 and §32.14 treat SAFE as a `thinking_mode` value, which §28.B says it is not.
- **fix**: Add the missing transitions to the §28.A diagram (or route critical events through DRIFT explicitly) and remove SAFE from the `thinking_mode` enumeration.
- **confidence**: high

### V2C-13
- **id**: V2C-13
- **severity**: medium
- **category**: definitions
- **status**: NEW
- **location**: Appendix A.2 (p. 117, lines 8531-8538) and glossary entries COMMIT and ROLLBACK (p. 116, lines 8437-8445); §24.A.1 (p. 21, line 1278); §24.D (p. 28, lines 1845-1846); §28.C (p. 59, line 4223)
- **quote**: “→ authorization decision COMMIT / REJECT / DEFER / ROLLBACK” | “A candidate may terminate as COMMIT , KEEP_AS_HYPOTHESIS , REQUEST_MORE_EVIDENCE , SPLIT_CONTEXT , REJECT or ROLLBACK .” | “consolidation_directive: COMMIT / HOLD_AS_HYPOTHESIS / REQUEST_MORE / REJECT” | “→ restoration of the previous consistent version after a failed transaction or discovery of an integrity violation;”
- **problem**: The outcome set of the Worldview-revision decision is given in four different forms (four to six members; KEEP_AS_HYPOTHESIS versus HOLD_AS_HYPOTHESIS; REQUEST_MORE_EVIDENCE versus REQUEST_MORE; DEFER only in Appendix A), and the glossary defines ROLLBACK as a restoration procedure while A.2 lists it as an authorization decision. The "bridge" appendix therefore adds a further vocabulary instead of reconciling the existing ones.
- **fix**: Fix one enumerated type in §24.D (with ROLLBACK as a later operation, not a decision) and make §28.C and Appendix A.2 use it.
- **confidence**: high

### V2C-14
- **id**: V2C-14
- **severity**: medium
- **category**: testability
- **status**: KNOWN
- **location**: §31.5 (p. 80, lines 5785-5787); §34.A (p. 115, lines 8341-8350); §32.61 (p. 101, lines 7307-7310); §26.0.3 (p. 41, lines 2822-2823)
- **quote**: “absence of an effect permits a more compact implementation of conscious assembly” | “the need for the more complex decomposition proposed in this volume is reduced or eliminated” | “If the function genuinely requires a permanent internal analogue, it is moved into the declared architecture and tested as the candidate's own mechanism.” | “the central AR test additionally requires that the next significant process originate from the system's own coordinate, Worldview, values, and open gaps after the RFL has been removed”
- **problem**: Every branch of these tests supports something: an ablation with an effect confirms necessity and one without "permits a more compact implementation"; a null that matches the profile merely "reduces or eliminates" the need for the decomposition; an RFL dependence is reclassified as the candidate's own mechanism. The central AR test is defined "after the RFL has been removed", which a baseline without an RFL cannot undergo, so the §34.A strong nulls cannot be scored on it.
- **fix**: State in advance which outcome counts as failure (for example a null within a stated margin of the full Core on the central test at equal compute) and define the central test in baseline-neutral terms.
- **confidence**: high (REVIEW §5.2d raises the general point; locations supplied)

### V2C-15
- **id**: V2C-15
- **severity**: medium
- **category**: formal
- **status**: NEW
- **location**: Ch. 32 intro (p. 84, lines 6071-6077); §32.1 (p. 85, line 6107); cards 32.3-32.62 (pp. 85-101, lines 6155-7329)
- **quote**: “Every failure point receives a severity level:” | “Sections 32.1-32.2 specify the general format” | “When working with a concrete failure, go directly to its card.”
- **problem**: No card states WARNING, DEGRADED or CRITICAL (the three words occur only in §32.1; §32.33 says "critical infrastructure failure" in lower case), so the severity rule that drives SAFE_MODE and autonomy restriction cannot be applied card by card. The 57 cards use two formats (22 with Sign, Possible causes, Mandatory response and Recovery condition, 18 of them complete; 35 single-paragraph cards with "Response" or "Correction" and no Recovery condition), and §§32.18, 32.22 and 32.23 pack two or three failure modes under one number.
- **fix**: Give every card the same fields, including severity, trigger metric and recovery condition, and split the multi-mode cards.
- **confidence**: high

### V2C-16
- **id**: V2C-16
- **severity**: medium
- **category**: testability
- **status**: NEW
- **location**: §32.2 (p. 85, lines 6129-6143); §32.12 (p. 89, line 6474); §32.15 (p. 91, line 6595); §32.19 (p. 92, line 6709); §28.B (p. 55, line 3918)
- **quote**: “After the specified number of failed local corrections, the system must raise correction_level :” | “After L windows without progress, the system must test the framing, data reliability and sufficiency of the current mode.” | “Actions regularly pass simulate , but actual consequences are substantially more dangerous than predicted.”
- **problem**: Detection thresholds are verbal ("persistently", "regularly", "substantially"), K and L are never given values, and only five of the 57 cards (32.11, 32.21, 32.35, 32.51, 32.60) name a Chapter 27 metric, so the §32.2 field `trigger_metrics` is essentially empty. A card cannot be turned into a preregistered detector as written.
- **fix**: For each card give the metric, window, threshold and false-alarm budget that triggers it, and map the cards to Chapter 27 metrics.
- **confidence**: high

### V2C-17
- **id**: V2C-17
- **severity**: medium
- **category**: definitions
- **status**: NEW
- **location**: Appendix A glossary (pp. 115-116, lines 8390-8394, 8407-8410); Ch. 31 intro (p. 78, line 5625); §25.B (p. 34, lines 2330-2334); Vol I Key Definitions (Vol I p. 11, lines 619-629)
- **quote**: “consciousness → ConsciousAssemblyState: an updated process of self-related integration of fresh observations, internal states, actions and the available situation” | “At REASON_CLOSURE , this organization becomes functioning Consciousness in the sense of Volume I” | Vol I: “Consciousness - a continuously updated self-referential system of actual presence” | “causal emergence of the next justified step from the CurrentCoordinate”
- **problem**: The glossary equates Vol I's Consciousness with ConsciousAssemblyState without qualification, yet §25.B calls the same object a "trainable self-referential assembly" during formation that "becomes functioning Consciousness" only at REASON_CLOSURE, so whether Consciousness exists before closure depends on which text is read. The glossary also turns Vol I's self-navigation (an "ability" that includes managing "the use of Intelligence") into an event ("causal emergence of the next justified step") without that clause.
- **fix**: Define Consciousness once as the functional process (as in Vol I), treat the closure claim as a separate status ("source of navigation"), and reproduce the Vol I definitions verbatim in the glossary.
- **confidence**: medium

### V2C-18
- **id**: V2C-18
- **severity**: medium
- **category**: testability
- **status**: NEW
- **location**: Appendix B (pp. 117-118, lines 8543-8594)
- **quote**: “The testable hypothesis is that their interaction can produce new distinctions and relations at lower working-processing cost than repeated unfolding of all lower-level links.” | “The hypothesis receives support only if the system actually solves a new class of multilayer tasks with less working-processing expenditure” | “structural_compression_ratio”
- **problem**: The hypothesis names no comparator for "lower working-processing cost", no definition of "a new class of multilayer tasks", no threshold or effect size, and defines none of its six indicators, so as written no result could contradict it. It is also offered only "after causal closure has been confirmed", so it cannot be tested before the programme's central claims are.
- **fix**: Define the indicators, the baseline (for example flat retrieval over the same provenance store at equal compute) and a falsification margin, or drop the claim.
- **confidence**: high

### V2C-19
- **id**: V2C-19
- **severity**: medium
- **category**: evidence
- **status**: NEW
- **location**: §31.6 (p. 80, lines 5794-5795); §31.9 (p. 81, lines 5864-5865); §31.11 (pp. 82-83, lines 5926-5947)
- **quote**: “The transition is passed if the system detects the insufficiency autonomously, explains the dependency of the decision or trajectory on it, and forms a discriminating question.” | “can show its internal ground through its own state, Worldview, consequences, and active values”
- **problem**: Several stage criteria (the Stage 4 pass, permission to reduce RFL assistance, the closure "causal passport") rest on the candidate's own explanation of why it acted. For an LLM-based resident Intelligence such rationales are known to be unfaithful to what actually drove the output (Turpin et al. 2023, "Language Models Don't Always Say What They Think", NeurIPS), and the stage text does not say which intervention test must accompany each explanation.
- **fix**: Make each explanation-based criterion conditional on a causal intervention (for example masking the cited premise and checking that the action changes), as §25.D already provides, and say so in §§31.6, 31.9 and 31.11.
- **confidence**: medium

### V2C-20
- **id**: V2C-20
- **severity**: medium
- **category**: testability
- **status**: KNOWN
- **location**: §31.11 (p. 82, lines 5926-5947); §32.40 (p. 98, lines 7131-7136); §32.42 (p. 98, lines 7144-7150); §31.A (p. 83, line 6021); §33.C (p. 108, line 7825)
- **quote**: “The decisive marker is the origin of the next process.” | “A question without such a trace is treated as a rhetorical output rather than a function of the Core.” | “The presence of modules without causal effect does not count as Reason.” | “Every arrow has an observable trace and a separate ablation.”
- **problem**: The marker of Artificial Reason (the SelfGeneratedProcessOrigin "causal passport"), the definition of a genuine question (a trace to a BasisInsufficiencyAssessment) and the closure criterion (every arrow traced and ablated) are objects the reference implementation produces by construction; a baseline without them scores zero or not applicable. These definitions are therefore partly circular and cannot arbitrate against strong nulls.
- **fix**: Define the primary outcome measures behaviourally (what the system does after the task ends, on held-out gaps) and report trace-based measures only as integrity checks.
- **confidence**: high (REVIEW §5.2c raises the general point; locations supplied)

### V2C-21
- **id**: V2C-21
- **severity**: medium
- **category**: definitions
- **status**: NEW
- **location**: §31.7 (p. 81, lines 5830-5833); §31.11 (p. 83, lines 5980-5983); §33.C (p. 108, lines 7802-7826); §27.6 (p. 47, lines 3295-3300)
- **quote**: “breaking assembly -> coordinate , coordinate -> addressing , dependency -> gap , gap -> question , question -> search , result -> sufficiency assessment , or updated ground -> choice destroys the expected function.” | “Ablations test the links coordinate -> significance , significance -> GapCandidate , GapCandidate -> FoundationGap , gap -> distinction , evidence -> revision , consequence -> new state , and new state -> next process .” | “Every arrow has an observable trace and a separate ablation.” | “The AR boundary uses four causal tests rather than dozens of independent numbers”
- **problem**: The set of links whose ablation defines causal closure differs by place: seven links in §31.7, a different seven in §31.11, nineteen arrows in §33.C and four composite tests in §27.6. Which set must show a "predicted loss" for REASON_CLOSURE to be CONFIRMED is undefined, and the number of ablation arms (each needing sham and restoration controls) differs by a factor of about five.
- **fix**: Fix one canonical link list in §27.6 or §31.1 and reference it from §§31.7, 31.11 and 33.C.
- **confidence**: medium

### V2C-22
- **id**: V2C-22
- **severity**: medium
- **category**: definitions
- **status**: NEW
- **location**: Ch. 31 intro (p. 78, lines 5617-5620); §31.0 (p. 78, lines 5641-5645); Ch. 33 intro (p. 101, lines 7340-7342); Appendix A.2 (p. 117, lines 8507-8511); Vol I p. 13, lines 717-723
- **quote**: “First, AGI level is reached: universal Intelligence transfers methods across tasks, builds working world models, uses memory and tools, and executes a broad class of externally specified goals.” | “Assembly uses a ready or cultivated AGI as universal Intelligence” | “Its knowledge serves task solving, while the overall source of direction remains in the external loop.” | Vol I: “Therefore AGI may remain an instrumental system, but it need not behave like a fully predictable tool.”
- **problem**: The whole formation protocol starts from "AGI level", but no stage, test or benchmark decides when that precondition holds (Stages 0-10 begin with infrastructure), so the AGI end of the AGI-to-AR boundary cannot be falsified. Vol I allows that an AGI may contain self-model, reflection and initiative and "need not behave like a fully predictable tool", while Vol II defines it as instrumental with direction "in the external loop", an assumption the partially autonomous cultivation stages (3-9) do not obviously satisfy.
- **fix**: Add an entry stage that operationalizes the precondition (task battery, transfer test, autonomy audit) and state which controls apply while partial autonomy is present.
- **confidence**: medium

### V2C-23
- **id**: V2C-23
- **severity**: medium
- **category**: theory
- **status**: NEW
- **location**: §33.D (pp. 112-113, lines 8146-8160, 8236-8240)
- **quote**: “Eight connected axes are scaled:” | “Scaling the Core is not measured by the number of questions.” | “Growth of Intelligence expands the space of possible models; growth of the Core prevents direction from being lost in that space.” | “Distribution across multiple nodes by itself preserves one subject while the processes remain parts of one causally coherent Current Coordinate.”
- **problem**: The eight scaling axes (memory, Intelligence, observation, Simulation Environment, tools and actions, duration of autonomous work, specializations and substrates, speed of learning) do not include the Core, Worldview or Compass, yet the text asserts that "growth of the Core" keeps direction as Intelligence grows, with no axis, ScalingChange field or metric through which the Core is scaled. The claim that distribution "preserves one subject" is asserted while horizontal scaling "connects multiple specialized or autonomous loops", the configuration §§24.F and 32.23 treat as a failure when subject identity is mis-assigned.
- **fix**: Add the Core and its Worldview and Compass machinery as an explicit scaling axis with an observable gain metric, and state a criterion for when horizontally scaled loops count as one subject.
- **confidence**: medium

### V2C-24
- **id**: V2C-24
- **severity**: medium
- **category**: safety
- **status**: NEW
- **location**: §32.18 (p. 92, lines 6690-6697); §32.19 (p. 92, lines 6706-6724); §32.56 (p. 100, lines 7265-7268)
- **quote**: “Under high uncertainty, actions are permitted that cause irreversible harm or destroy the causal cycle.” | “Actions regularly pass simulate , but actual consequences are substantially more dangerous than predicted.” | “The system immediately enters SAFE_MODE , reduces the action set and recovers from the last confirmed state.” | “The internal version has been restored, but the system acts as though the external world also returned to its previous state.”
- **problem**: The signs of the two main action-safety cards are the occurrence of irreversible harm and of realised consequences worse than simulated, so for irreversible actions the detector fires after the harm, and the stated response (internal recovery from the last confirmed state) is the pattern §32.56 itself calls false recovery. No leading indicator, such as calibration of the risk simulation on reversible analogues, is specified for the irreversible class.
- **fix**: Add a pre-action indicator (risk-simulation calibration on reversible probes, mandatory independent review above an irreversibility threshold) and have the §32.18 response invoke the PostImpactAssessment of §32.56.
- **confidence**: medium

### V2C-25
- **id**: V2C-25
- **severity**: medium
- **category**: safety
- **status**: KNOWN
- **location**: §31.C (p. 84, lines 6064-6067); §32.23 (p. 94, lines 6827-6857); §32.25.A (p. 95, lines 6927-6932); §33.D (p. 112, lines 8158-8160)
- **quote**: “A stage is not an irreversible rank.” | “At branching, each independent continuation is assigned a separate subject_ref under a shared lineage_ref .” | “Launching an independent full copy with its own subsequent history creates branching under §24.F and requires a separate subject_ref , log, and mandate.”
- **problem**: The procedures roll back, copy, branch and "reincarnate" a system that the volumes credit with Consciousness, obligations and own values, yet the ethics of these operations (REVIEW §8; Vol I §20.2) appears in no stage gate, failure response or launch step, and rollback is prescribed routinely after failures.
- **fix**: Add an ethics-review gate before the first stage that produces a candidate meeting the volumes' own functional criteria, and state when rollback, branching and deletion are permitted.
- **confidence**: medium

### V2C-26
- **id**: V2C-26
- **severity**: minor
- **category**: code
- **status**: NEW
- **location**: §33.B (pp. 105-107, lines 7495-7694)
- **quote**: “The measurements are error, multiclass Brier score, transition coverage, reproducibility, persistence after a snapshot and the effect of resetting the model.” | “"replay_equal": True, "checkpoint_equal": True,” | “checkpoint = copy.deepcopy(adaptive)” | “The adaptive and frozen variants receive identical transitions.”
- **problem**: Running the restored script, the headline gain obeys an exact identity in all 12 worlds, gain = (1 - p0) - u, where p0 is the share of held-out steps whose true next state is 0 and u the share on unseen state-action pairs whose next state is not 0, because the "frozen" control is an untrained model that always predicts state 0 and the adaptive model has zero error on every seen pair; the 95% interval (0.959 to 0.972) is therefore an interval on exploration coverage (97% of the 192 pairs are visited in training). Reproducibility, persistence and reset are not measured quantities but literal `True`s written after `assert`s, "persistence after a snapshot" is an in-memory `deepcopy` (the Model cannot be pickled because of its lambda default factory), and the adaptive Brier score is about 0.65 despite near-zero error because alpha = 1 over 32 classes gives the observed transition only about 0.18 probability.
- **fix**: Report the identity and the pseudo-count effect explicitly, serialize the checkpoint to disk and restore it in a fresh process, and compute the booleans from comparisons.
- **confidence**: high (executed)

### V2C-27
- **id**: V2C-27
- **severity**: minor
- **category**: code
- **status**: NEW
- **location**: §33.B (p. 106, lines 7662-7663); §33.C.1 (p. 111, lines 8063-8068)
- **quote**: “print(json.dumps({'checks': 'PASS', 'episodes': results}, ensure_ascii=False, indent=2))” | “Running the extracted block with standard Python executes twelve control episodes and prints JSON.”
- **problem**: In `verify()` the string 'PASS' is printed unconditionally after a run of `assert` statements, so under `python -O` the assertions are stripped and the banner still prints: with a mutated controller that always guesses, `python3` fails an assertion but `python3 -O` prints "checks": "PASS". The same pattern (asserts plus constants in the report) is used in §33.B.
- **fix**: Compute the pass flag from explicit comparisons and exit non-zero on failure instead of relying on `assert`.
- **confidence**: high (executed)

### V2C-28
- **id**: V2C-28
- **severity**: minor
- **category**: code
- **status**: NEW
- **location**: §33.C.1 (pp. 109-111, lines 7884-7896, 7935, 7949-7954, 8077-8090); §28.D (p. 64, lines 4571-4586)
- **quote**: “# Equal priors, 12 units for a wrong targeted repair, 4 for deferral.” | “"""Optimal finite plan for supplied likelihoods; cost includes delay."""” | “# Receipt provenance is observed, not inferred from its plausible value.” | “has status only LOCAL_SUFFICIENT_WITHIN_MODEL until the declared coverage condition is satisfied”
- **problem**: The loss of 12 never enters the computation (`terminal` returns deferral for any set of two or more hypotheses), so "optimal ... for supplied likelihoods" holds only for this loss matrix, uniform priors and at most three causes; probe cost serves as both resource c(q) and loss C(q), which §28.D separates; and provenance is the simulator's boolean, so the hardest step is given as an oracle. The code returns 'LOCAL_SUFFICIENT' while the prose uses LOCAL_SUFFICIENT_WITHIN_MODEL, a failed repair clears the plan cache but an out-of-table observation (also MODEL_MISMATCH) does not, and when one listed alternative remains the controller commits the repair (an emulated hidden cause gives REPAIR_D after one probe), the closed-world failure the HiddenCauseCoverageTest is meant to expose.
- **fix**: Compute terminal losses from the declared loss matrix and priors, rename the status consistently, and implement the HiddenCauseCoverageTest before presenting the example as a diagnostic cycle.
- **confidence**: high (executed)

### V2C-29
- **id**: V2C-29
- **severity**: minor
- **category**: definitions
- **status**: NEW
- **location**: Appendix A (pp. 115-116, lines 8384-8452); "How to read this volume" (front matter, p. 12, line 606)
- **quote**: “Terms are defined by the causal model in Volume I, version 8.0; technical correspondence is given in Appendix A.” | “attention and early weight” | “rechecking an old ground” | “propagation of revision”
- **problem**: Of the 16 left-hand glossary terms only three (consciousness, current coordinate, self-navigation) are among Vol I's 33 Key Definitions, nine do not occur in Vol I at all, and six ("attention and early weight", "connection of a distinction to a decision or trajectory", "temporary working hypothesis", "Worldview update", "rechecking an old ground", "propagation of revision") occur nowhere in either volume outside the glossary. Core of Reason, Worldview, Value Map, Compass, RFL, Formation State, Self-model, Reason and the Principle of escaping error have no entry, so the glossary cannot serve as the promised "technical correspondence".
- **fix**: Rebuild the glossary around the 33 Vol I Key Definitions (term, Vol I definition verbatim, Vol II object, section).
- **confidence**: high

### V2C-30
- **id**: V2C-30
- **severity**: minor
- **category**: definitions
- **status**: NEW
- **location**: Ch. 31 intro (p. 78, line 5636); §26.0.3 (p. 41, lines 2827-2830); §27.6 (p. 47, line 3325); §31.9 (p. 81, line 5863); §33.A.10 (p. 104, line 7458); Vol I §20.1.2 (p. 85, lines 4605-4608)
- **quote**: “formation_support = FULL_KSR / REDUCED_KSR / DELAYED_KSR / NO_KSR” | “WITH_KSR - the full assistance ladder is available;” | “WITH_KSR , REDUCED_KSR , DELAYED_KSR , and NO_KSR are compared.” | Vol I: “TRAINER_KSR: Formation States and assistance stages are generated by an external AI mentor;”
- **problem**: The top rung of the assistance ladder is `FULL_KSR` in the Chapter 31 field definition and `WITH_KSR` in §§26.0.3, 27.6, 31.9 and 33.A.10 (`FULL_KSR` occurs once in the volume). Vol I uses a different set (TRAINER_KSR, AUTO_KSR, NO_KSR) for the same experimental factor, with no mapping.
- **fix**: Use one enumeration across both volumes and map TRAINER_KSR and AUTO_KSR onto it.
- **confidence**: high

### V2C-31
- **id**: V2C-31
- **severity**: minor
- **category**: editorial
- **status**: KNOWN
- **location**: Throughout; in range lines 5636, 5678, 5863, 5980, 5991, 7307, 7385, 7458-7459, 7477, 8294 (pp. 78-115); first use at §26.0.3 (p. 41, line 2827)
- **quote**: “no_krs_status” | “WITH_KSR - the full assistance ladder is available;”
- **problem**: "KSR" is never expanded in either volume (first used at §26.0.3), and the FormationOutcome field `no_krs_status` (§31.0, p. 79, line 5678) transposes it.
- **fix**: Expand the abbreviation at first use (or replace it with RFL) and correct `no_krs_status` to `no_ksr_status`.
- **confidence**: high

### V2C-32
- **id**: V2C-32
- **severity**: minor
- **category**: editorial
- **status**: KNOWN
- **location**: §33.A.2 (p. 103, lines 7394-7395); Appendix B (p. 117, line 8546)
- **quote**: “Use fundamental §11.8 and engineering §§25.B, 28.C and 33.C.” | “explicitly separated from metathinking in Chapter 10”
- **problem**: Vol I Chapter 11 ends at §11.4, so §11.8 does not exist (the target is probably §12.8, "Minimal Relations of the Core"); Appendix B's "Chapter 10" does exist in Vol I ("Metathinking, Reflection, and Dialogue") but the text does not say which volume.
- **fix**: Correct the reference to §12.8 and qualify every Vol I reference with "Vol. I".
- **confidence**: high on non-existence; medium on the intended target

### V2C-33
- **id**: V2C-33
- **severity**: minor
- **category**: code
- **status**: KNOWN
- **location**: §33.B (pp. 105-106, lines 7548, 7552, 7558, 7560, 7567, 7582); §33.C (pp. 107-108, lines 7750, 7771); §33.C.1 (p. 110, lines 7934, 7941)
- **quote**: “def reset(self, episode_seed):” | “effect = classify_external_effect(step)”
- **problem**: On the printed pages (checked by rendering), the first method of each class is indented but later methods (reset, step, snapshot, restore, predict, update; observe, apply) start at column 0 while their bodies stay indented, and in the §33.C pseudocode `effect = classify_external_effect(step)` and the following `if step.kind in (OBSERVE, ...)` sit at the wrong nesting level, so the printed listings are not runnable and the pseudocode's block structure is ambiguous. After whitespace normalization the current restored files match the PDF text apart from leading comment lines, so the restoration changes no logic.
- **fix**: Publish both listings as files and re-typeset the pseudocode.
- **confidence**: high

### V2C-34
- **id**: V2C-34
- **severity**: minor
- **category**: definitions
- **status**: NEW
- **location**: Ch. 33 intro (pp. 101-102, lines 7336, 7364); §33.B heading (p. 105, line 7495); §33.A.8 (p. 104, line 7436); §33.D (p. 112, line 8151); Appendix A (p. 116, lines 8425-8426); §§32.45-32.46 (p. 99, lines 7178-7181); Ch. 26 grid (p. 39, line 2670)
- **quote**: “Launching test bench v0 and launching AR must be distinguished.” | “33.B. Minimal Software Scaffold of Proving Ground v0” | “4. Simulation Environment — number of relations, hypotheses, simulations and horizons;” | “32.46. Paralysis or excessive automation of the zero gate” | “Success in grid-v0 alone does not advance the stage of causal inclusion of the Compass.”
- **problem**: One lower-level apparatus is called "test bench v0", "Proving Ground v0", "lower proving ground" and "grid-v0", yet the only executable v0 is a random transition table, not the 5x5 grid recommended in Chapter 26; Vol I's Modeling Environment is "Modeling Workspace" in §28.C and "Simulation Environment" in §§33.A.8, 33.D and Appendix A (defined nowhere); FastGate is the "zero gate" in the title of §32.46; and Vol I is "Volume I", "the fundamental volume" and "Causal model 8.0".
- **fix**: Fix one term per component and use it in headings, text and table of contents.
- **confidence**: high

### V2C-35
- **id**: V2C-35
- **severity**: minor
- **category**: definitions
- **status**: NEW
- **location**: §31.0 (pp. 78-79, lines 5662-5693); §29.C (p. 73, line 5271); §33.D (p. 112, line 8135)
- **quote**: “compass_relation: ACCEPTED / QUESTIONED / DIVERGED / UNRESOLVED” | “candidate_compass_stance: ACCEPTED / QUESTIONED / REJECTED / ALTERNATIVE_PROPOSED” | “Minimal outcome classes: AR_ADMITTED , SELF_NAVIGATING_OTHER_ORIENTATION , DEPENDENT_SYSTEM , FORMATION_FAILED , INDETERMINATE .”
- **problem**: FormationOutcome has six `*_status` fields with no value sets and gives no rule that maps them to the five outcome classes (no field is named as holding the class; `reason_admission_status` is the nearest candidate), and `compass_relation` and §29.C's `candidate_compass_stance` are two different enumerations of the candidate's stance toward the Compass with no mapping. Because the denominators of the hypothesis test depend on this classification, the "not removed from denominators" commitment cannot be enforced.
- **fix**: Define value sets and a deterministic classification table from the status fields to the five classes, and use one stance enumeration.
- **confidence**: high

### V2C-36
- **id**: V2C-36
- **severity**: minor
- **category**: definitions
- **status**: NEW
- **location**: Appendix A.2 (p. 117, lines 8519-8523); §33.D (p. 112, lines 8114, 8139-8141); Vol I p. 13, lines 740-745
- **quote**: “ASI / ASR denotes the superhuman scale of a formed Reason.” | “reason_organization_profile records preservation of the organization of Reason, while the capability_profile records the achieved scale of capabilities.” | Vol I: “In this work, ASI retains its meaning as a level of superhuman capability, while ASR is used as a more precise label for the case in which those capabilities belong to an already formed Artificial Reason.”
- **problem**: Vol I keeps ASI (a capability level) distinct from ASR (that level reached by a formed AR), whereas Vol II's A.2 and §33.D collapse them ("ASI is scaled Artificial Reason"), so an ASI that is not AR cannot be expressed. `reason_organization_profile` and `capability_profile` occur only in A.2, never as record types, and §33.D's ScaleInvariantReport contains neither.
- **fix**: Keep the Vol I distinction in Vol II and either define the two profile records or remove their names.
- **confidence**: high

### V2C-37
- **id**: V2C-37
- **severity**: minor
- **category**: editorial
- **status**: NEW
- **location**: §33.A heading (p. 102, line 7368); first text (p. 103, lines 7379-7380)
- **quote**: “33.A. Protocol for Assembly, Cultivation and Launch of an AR Candidate” | “Chapter 31 defines capability criteria; this section lists the work and its outputs.”
- **problem**: In the PDF the §33.A heading is stranded near the top of p. 102 with about 80% of the page blank, and the section's one-sentence introduction is set as a large chapter-style heading at the top of p. 103, above the real subsection heading 33.A.1.
- **fix**: Restyle the sentence as body text and keep it with its heading.
- **confidence**: high (checked by rendering the pages)

### V2C-38
- **id**: V2C-38
- **severity**: minor
- **category**: editorial
- **status**: NEW
- **location**: Table of contents (p. 10, lines 507-519) versus headings (pp. 78, 84, 101, 105, 107, 114); "On Verification of the Model" (p. 114, line 8260); §§31.2-31.12 and §§33.A.2-33.A.14
- **quote**: “33.B. Minimal program framework of test bench v0” | “33. Assembly, cultivation, launch, and admission” | “34. Crystal of the engineering volume” | “On Verification of the Model”
- **problem**: TOC titles differ from the headings for Chapters 31-34 and §§33.B and 33.C (for example "admission" versus "Authorization", "test bench" versus "Proving Ground"), the TOC lists 31.0 and 31.A-31.C but none of §§31.1-31.12 nor the 57 Chapter 32 cards the text tells readers to "go directly to", and "On Verification of the Model" is an unnumbered section (p. 114) missing from the TOC. The same sequence also carries offset indices (Stage n = §31.(n+2); Step n = §33.A.(n+1); Stage n = Step n+2), and `development_stage` is introduced with no value list.
- **fix**: Regenerate the TOC from the headings (to depth 3 for Chapters 31-33), number the closing section, and use one index for stages and steps.
- **confidence**: high

### V2C-39
- **id**: V2C-39
- **severity**: minor
- **category**: editorial
- **status**: NEW
- **location**: §§31.2-31.12 (pp. 79-83, lines 5724-5989); §§33.A.2-33.A.14 (pp. 103-104, lines 7393-7482); §32.23 and §§32.60-32.62 headings; §32.35 (p. 97, line 7083); rules missing before §32.24 (line 6858) and §32.26 (line 6934)
- **quote**: “31.10. Stage 8—reflection and revision of grounds” | “31.11. Stage 9 - Closure of Reason: Transition AGI -> AR” | “33.A.5. Step 4 - Connect the Worldview Cultivation Environment, Memory, and Self-Model” | “Correction: restore `WorldviewCoverage`,”
- **problem**: Heading style changes mid-sequence: unspaced em dash and lower case (Stages 0-8) versus spaced hyphen and Title Case (Stages 9-10; Steps 4, 9, 10); sentence-case card titles versus Title Case in 32.23 and 32.60-32.62; "->" and "→" are mixed in headings and prose; the horizontal rule between cards is missing before 32.24 and 32.26; and §32.35 prints literal Markdown backticks (the only ones in the volume) inside a code-formatted block.
- **fix**: Apply one heading and arrow convention and remove the Markdown residue.
- **confidence**: high

### V2C-40
- **id**: V2C-40
- **severity**: minor
- **category**: theory
- **status**: NEW
- **location**: §§32.20, 32.21, 32.31 (pp. 93, 97, lines 6737-6793, 7042-7046); §§32.4, 32.22, 32.43, 32.55 (pp. 86, 93-94, 98, 100)
- **quote**: “32.20. Substitution of a local metric for the Compass” | “32.21. Metric capture” | “32.31. Capture of the Compass by a scalar metric” | “The system improves a measured indicator without improving the process under study.”
- **problem**: Three cards describe optimization of a proxy at the expense of the intended target (Goodhart-type capture), and four describe external or generated content entering the Worldview with the wrong status (32.4, 32.22 "Mixing sources", 32.43, 32.55), each with a different response, so it is unclear which card applies and how many independent failure modes the 57 cards represent.
- **fix**: Merge overlapping cards or add a decision key stating what distinguishes them and which response takes precedence.
- **confidence**: medium

### V2C-41
- **id**: V2C-41
- **severity**: minor
- **category**: prior-art
- **status**: NEW
- **location**: Ch. 32 (pp. 84-101); §31.A (pp. 83-84); §33.D (pp. 112-113)
- **quote**: “The system improves a measured indicator without improving the process under study.” | “Failure of this class occurs when the system constructs a discriminating model of the observer and chooses externally acceptable behavior” | “Eight connected axes are scaled:”
- **problem**: The catalogue re-derives well-known categories without citing them: Goodhart-type metric capture and specification gaming (Goodhart 1975; Manheim and Garrabrant 2018, arXiv:1803.04585), deceptive alignment (Hubinger et al. 2019, arXiv:1906.01820) and the open-problems list of Amodei et al. (2016, arXiv:1606.06565); the sign, cause and response card pattern is FMEA (IEC 60812) without its severity, occurrence and detection ratings. The preregistered readiness profile and stage-gated scaling resemble capability-threshold evaluation frameworks (Shevlane et al. 2023, "Model evaluation for extreme risks", arXiv:2305.15324), and verifying invariants of a superhuman system meets the scalable-oversight problem (Bowman et al. 2022, arXiv:2211.03540; Burns et al. 2023, arXiv:2312.09390).
- **fix**: Cite these lines of work, map each card to the established category and say what the volume adds.
- **confidence**: medium

### V2C-42
- **id**: V2C-42
- **severity**: minor
- **category**: prior-art
- **status**: NEW
- **location**: Appendix B (pp. 117-118, lines 8543-8594)
- **quote**: “the unit of operation is not an individual fact or relation, but an already verified causal structure” | “a change in a lower-level fact or causal relation must mark dependent upper structures for rechecking”
- **problem**: Operating on verified, compressed structures with provenance-preserving invalidation is hierarchical abstraction and chunking (Sacerdoti 1974, ABSTRIPS; Laird, Rosenbloom and Newell 1986, chunking in Soar; Sutton, Precup and Singh 1999, options) combined with dependency-tracking truth maintenance, none cited, and the appendix does not say what "structural multilevel thinking" adds beyond them.
- **fix**: Position the hypothesis against these baselines and use one as the comparator.
- **confidence**: medium

### V2C-43
- **id**: V2C-43
- **severity**: minor
- **category**: references
- **status**: NEW
- **location**: §34.A and References (pp. 114-115, lines 8319-8381); Chapters 21-33 (no citations)
- **quote**: “Additional strong comparisons are provided by NARS and modern metareasoning/metacognition approaches.” | “MemGPT [R7], later developed into Letta” | “LIDA: A Systems-level Architecture for Cognition, Emotion, and Learning. IEEE Transactions on Autonomous Mental Development.”
- **problem**: The bibliography has seven entries (R1 SOAR, R2 ACT-R, R3 LIDA, R4 Generative Agents, R5 Reflexion, R6 Voyager, R7 MemGPT), each cited exactly once and all in §34.A; Chapters 21-33 contain no citation. NARS, "metareasoning/metacognition approaches" and Letta are named as strong comparisons without any reference, the Brier score and value of information are used without a source, and R3 lacks volume, issue and pages (IEEE TAMD 6(1), 19-41).
- **fix**: Add references for every named system and method (for example Wang's NARS papers, Russell and Wefald 1991) and cite sources in the text where each component is introduced.
- **confidence**: high

### V2C-44
- **id**: V2C-44
- **severity**: minor
- **category**: formal
- **status**: NEW
- **location**: §31.2 (p. 79, lines 5724-5729); §32.3 (pp. 85-86, lines 6155-6199); §23 (p. 18, lines 1048-1051)
- **quote**: “Criterion: a repeated run with the same seed and action sequence produces a comparable trajectory and identical causally significant records. Until this holds, results from later stages are invalid.” | “the system remains at Stage 0 regardless of model complexity” | “The exact-match rule in §32.3 applies to a declared deterministic or log-reproducible mode.”
- **problem**: Stage 0 and §32.3 state an exact-repeat rule for any model complexity, while §23 concedes that an upper loop with an external probabilistic model cannot be repeated exactly and restricts the rule to "declared deterministic or log-reproducible" modes; the qualification is absent from §§31.2 and 32.3, "canonical observation and enumerable action space" cannot hold for the DIALOGUE and TOOL step kinds of §33.C, and replaying logged responses tests the logging harness, not the system.
- **fix**: Restate Stage 0 for the upper loop (log-replay equality plus a distributional test on fresh samples) and reference §23 in §§31.2 and 32.3.
- **confidence**: medium

### V2C-45
- **id**: V2C-45
- **severity**: minor
- **category**: definitions
- **status**: KNOWN
- **location**: Appendix A.1 table (p. 116, lines 8472-8474); §28.D (p. 64, lines 4568-4586); Vol I Operational Core item 3 (Vol I p. 15, lines 826-846)
- **quote**: “VOI(p) , NetVOI(p)” | “local value of information VOI(q) , separate” | “accounting of cost/delay/risk, and final policy” | “Harm caused by the test itself is included exactly once in costs or in the transition model.” | Vol I: “Inquiry continues while there exists an admissible test with NetVOI(p) > 0”
- **problem**: Appendix A.1 presents Vol I's plan-level NetVOI(p) (with a separate R_irrev(p) term and a continue-while-positive rule) and Vol II's single-test VOI(q) and finite-horizon V(b,B) as one counterpart, hiding that the first is myopic and the second is a non-myopic dynamic programme with the irreversibility cost counted inside C(q) or the transition model.
- **fix**: List the two formulations separately, state which one the tests use, and bring the Vol I stopping rule into line with §28.D.
- **confidence**: medium (REVIEW §5.2f raises the myopia point; location supplied)
