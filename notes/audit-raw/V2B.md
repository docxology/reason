# V2B: independent reader findings, Vol II lines 3074-5615 (Chapters 27-30)

Range: engineering-3.5.txt lines 3074-5615, PDF pp. 44-78 (Chapters 27-30, including 27.B, 28.C, 28.D, 29.0.1, 29.A-C, 30.A-F). Every line of the range was read. Every quote was checked with `scripts/locate.py`; page numbers are PDF pages as the locator reports them (they equal the printed page numbers in this volume). Status is relative to REVIEW.md as it stood on 2026-10-10 (about 13:08). Cross-volume anchors to Vol I are labelled "Vol I".

- **id**: V2B-01
- **severity**: major
- **category**: testability
- **status**: KNOWN
- **location**: Ch. 27, §27.2, §27.4-§27.7; PDF pp. 45-48; lines 3142, 3151, 3184-3227, 3268, 3306-3308, 3325-3338, 3362
- **quote**: "source_trace_completeness = significant_claims_with_recoverable_provenance / all_testable_significant_claims" | "basis_origin_trace_rate = QuestionTask_with_recoverable_chain_to_BasisInsufficiencyAssessment / all_significant_QuestionTasks" | "world_self_sync_error is the share of decisions that used incompatible versions of the Worldview and SelfState" | "For ratios with a zero denominator, NOT_APPLICABLE and sample size are returned rather than 0 or 1."
- **problem**: At least twenty of the roughly sixty indicators named in Chapter 27 (trace and provenance rates, ten of the twelve §27.4 assembly metrics, the addressing metrics, closure_break_sensitivity, the RFL metrics) are defined over records that only the architecture creates. By §27.7's own rule a baseline without those records gets NOT_APPLICABLE rather than a score, and a reference implementation can meet several by construction (a QuestionTask exists only if derived from a BasisInsufficiencyAssessment). They therefore cannot arbitrate between the Core and a strong null; REVIEW §5.2(c) makes the point, and this entry adds locations and a count.
- **fix**: Label these metrics as integrity checks and make primary only outcome metrics that can be scored from any agent's external behaviour against a tester-held ground truth.
- **confidence**: high

- **id**: V2B-02
- **severity**: major
- **category**: testability
- **status**: KNOWN
- **location**: §27.B "Prior pilot" and "Profile"; PDF pp. 49-50; lines 3411-3418, 3494-3507
- **quote**: "in the reviewed materials there is no completed external admission of this package and no comparative C0/C1/C2 run" | "Its results do not establish autonomy of the Core or an architectural advantage." | "primary metric and minimum practically significant effect are retained"
- **problem**: The only experimental content is a benchmark-construction pilot (a single dated session, 22 August 2026, of 15 logged cycles; five task packages P0-SET-001 to 005, four rejected, an 89-check validity report for the fifth). No language model, baseline stack, environment generator, number of world families, effect size, error rate or decision threshold is named in §27.B or anywhere in Chapters 27-30, and the "minimum practically significant effect" is mentioned but never given a value. The first series is therefore a protocol, not an experiment (REVIEW §5.2(a)).
- **fix**: Name the models, arms, world-family count, smallest effect of interest, alpha/power and stopping rule in the profile, and run one comparative pilot before any further revision.
- **confidence**: high

- **id**: V2B-03
- **severity**: major
- **category**: testability
- **status**: KNOWN
- **location**: §27.B "How to read the result", p. 50, lines 3515-3520; §27.6 p. 47, lines 3306-3308; §27.A p. 48, lines 3392-3395
- **quote**: "Operation of a strong equivalent refines the form of the architecture." | "absence of loss means either a functional duplicate, a false necessity hypothesis or a weak test." | "Compensation by another part of the system is recorded separately: it may reveal a functional equivalent rather than absence of an effect." | "Failure with sound relations and an adequate test requires revision of the functional claim."
- **problem**: Every unfavourable outcome has a favourable reading: a strong control "refines the form" of the architecture, an ablation without loss may be a "functional duplicate", compensation "may reveal a functional equivalent", and failure leads to "revision" of the claim. No preregistered margin or arm is given at which the Core is abandoned as a distinct contribution (REVIEW §5.2(d); this entry supplies the Vol II locations).
- **fix**: Preregister the decisive comparison (for example an epistemic-layer-only agent versus the full Core at equal compute) and the margin below which the Core is declared unnecessary.
- **confidence**: high

- **id**: V2B-04
- **severity**: medium
- **category**: testability
- **status**: NEW
- **location**: Ch. 27 intro p. 44, line 3080; §27.7 p. 48, lines 3343-3354; §27.A p. 48, lines 3381-3390; §27.4 p. 46, line 3217
- **quote**: "All formulas, thresholds, windows, scenarios and aggregation rules are fixed in ExperimentProfile before the control series." | "For every indicator, the following are fixed before the series:" | "At minimum, the following are fixed:" | "If such a replacement reliably does not degrade relevant tasks, a separate causal role for assembly is not confirmed."
- **problem**: ExperimentProfile occurs once in either volume and is never defined (no fields, no instance), and Chapter 27 gives no numeric acceptance threshold (apart from seed_reproducibility = 1.0), window length, sample size or error rate; only 8 of about 60 named indicators carry a formula (rolling_mean_error(W), adaptation_gain, correction_persistence_rate, source_trace_completeness, revision_propagation_accuracy, gap_detection_rate, basis_origin_trace_rate, question_distinguishing_yield; five more are in §24.C). The chapter therefore does not meet its own §27.7 list for most indicators, its falsification conditions are unquantified ("reliably does not degrade"), and §27.A lists effect_size and confidence_interval among things "fixed" in advance although both are results.
- **fix**: Define ExperimentProfile as a record with a worked instance for the v0 series and for one Core metric; separate pre-fixed parameters (minimum effect, alpha, power, windows) from reported results; replace "reliably", "persistent" and "bounded" by numbers.
- **confidence**: high

- **id**: V2B-05
- **severity**: medium
- **category**: definitions
- **status**: NEW
- **location**: §27.7 p. 48, line 3371; §27.5 p. 47, line 3279; §27.6 p. 47; §28.C.3 p. 63, lines 4497-4510; §31.A pp. 83-84, lines 6021-6042
- **quote**: "For new loops, unsupported_promotion_rate , status_preservation_rate , post_impact_coordinate_latency , obsolete_goal_persistence , recovery_without_reset_rate , viable_option_retention , repeat_failure_reduction and new_obligation_recall are measured separately." | "premature_sufficiency_rate records cases where the Core closed inquiry before a critical distinction" | "method_revision_transfer_gain" | "structural_similarity_preregistration_rate"
- **problem**: Eight metrics are named once in the whole volume with no definition, denominator or direction of improvement; premature_sufficiency_rate, the key negative outcome, is called a "rate" but has no denominator; external_prompt_dependency, teacher_agreement_bias, formation_support_dependency and closure_break_sensitivity have no formula. The §28.C.3 list of 14 plasticity indicators contains an apparent duplicate (transfer_gain_after_revision and method_revision_transfer_gain) and an experimenter-hygiene item (structural_similarity_preregistration_rate) listed as an indicator of the system, and Chapter 27 names drift from the §31.A thresholds (world_self_sync_error vs maximum_world_self_desynchronization; question_distinguishing_yield vs minimum_distinguishing_yield; teacher_agreement_bias and formation_support_dependency vs maximum_teacher_dependency_gap; source_trace_completeness vs minimum_trace_completeness).
- **fix**: Add one metric registry (name, formula, denominator, direction, control, status) as the single source for §27, §28.C.3 and §31.A.
- **confidence**: high

- **id**: V2B-06
- **severity**: medium
- **category**: testability
- **status**: NEW
- **location**: §27.B p. 50, lines 3496-3499; §31.A pp. 83-84, lines 6011-6045
- **quote**: "The principal outcome of the first series is the share of new diagnostic tasks with a correct action or justified irresolvability under a fixed budget." | "The profile is published before results are examined. Changing thresholds requires a new series."
- **problem**: This is the only architecture-neutral outcome in the chapter, yet it has no name or formula among the Chapter 27 metrics, "justified irresolvability" is defined nowhere in either volume, and none of the twenty ReadinessProfile parameters in §31.A is this outcome or a margin over a control; all are absolute levels of process or accuracy metrics. A candidate could therefore satisfy the readiness profile without ever being compared with a baseline.
- **fix**: Name the principal outcome as a metric with a formula and a reference set of admissible decisions, and put a minimum advantage over the strong null at equal budget into the readiness profile.
- **confidence**: medium

- **id**: V2B-07
- **severity**: medium
- **category**: testability
- **status**: NEW
- **location**: §27.B p. 50, line 3502; p. 49, lines 3415-3417
- **quote**: "The size of the confirmatory series is determined from a separate pilot and a preselected effect; the pilot is not included in final confirmation." | "in the reviewed materials there is no completed external admission of this package and no comparative C0/C1/C2 run"
- **problem**: The sample-size rule depends on a pilot that, by the volume's own account, never made a comparison, so no variance or effect estimate exists, and the "preselected effect" is not stated. The confirmatory series cannot be sized from anything in the text.
- **fix**: Run a small comparative pilot (equal-compute arms on a handful of world families) to estimate variance, or fix the smallest effect of interest and derive n from it, and state the number in the profile.
- **confidence**: high

- **id**: V2B-08
- **severity**: medium
- **category**: testability
- **status**: NEW
- **location**: §27.B "Controls", p. 49, lines 3450-3454; Vol I A.4 "Priority of the First Series", pp. 99-100, lines 5495-5530
- **quote**: "Comparisons include routine Intelligence with ordinary memory, tools and self-verification; the same mechanism with the proposed relations; and declared replacements or ablations." | Vol I: "The first is a strong null hypothesis: an agent stack with ordinary planning, versioned memory of beliefs and provenance, self-checking, mismatch response, value-of-information assessment, and a log of failed attempts available to subsequent tasks."
- **problem**: The volume that specifies the first series names a weaker control than the volume that proposed it: Vol I's strong null (versioned belief memory with provenance, VOI, failure log) and its equal-resource list (model calls, tokens, external sources, bench time, hidden preparation) are not carried into §27.B. It is therefore open whether the epistemic-layer components are present in the control arm.
- **fix**: Reproduce the three Vol I variants and the resource-accounting list in §27.B and name an epistemic-layer-only arm explicitly.
- **confidence**: high

- **id**: V2B-09
- **severity**: minor
- **category**: definitions
- **status**: NEW
- **location**: §27.B "Prior pilot", p. 49, lines 3411-3418; Vol I A.2 "First Documented Pilot", p. 94, lines 5127-5135, 5149
- **quote**: "The reason-kernel-experiment.md log contains cycles 1-15." | "For 005, a G0 report is preserved showing 89 checks passed" | Vol I: "a positive machine- control report is preserved for P0-SET-005" | Vol I: "In the materials reviewed, the final comparison of subjects remains an open stage."
- **problem**: "P0 packages", "G0 report" and "C0/C1/C2" (one occurrence in either volume) are never defined, and nothing says what the 89 checks test. Vol I names the log "Reason Loop" and calls the fifth package's report a "positive machine- control report", while Vol II names the log reason-kernel-experiment.md and the report a "G0 report"; the open stage is "comparison of subjects" in Vol I and a "C0/C1/C2 run" in Vol II. The log, packages and report are in no bibliography entry or cited repository.
- **fix**: Define the labels, state what the 89 checks verify, use one name per artefact in both volumes, and deposit the log, packages and report with a DOI.
- **confidence**: high

- **id**: V2B-10
- **severity**: minor
- **category**: references
- **status**: KNOWN
- **location**: §27.B p. 49, line 3407; Vol I A.4 pp. 97-99, lines 5318-5491, and p. 100, line 5523; §28.B p. 56, line 3941
- **quote**: "It connects tests 2, 20, 23, 26 and 31 from foundational Appendix A.4" | Vol I: "In this way items 2, 20, 23, 26, and 31 are connected." | "Every execution separately passes §28"
- **problem**: Appendix A.4 is printed with items 19-55, so test 2 does not exist and items 20, 23, 26, 31 as printed do not fit the D/A/S series. The references are consistent with a shift of 20: 2, 20, 23, 26, 31 map to printed items 22 (Independent check), 40 (Selection of a discriminating test), 43 (Gap type and question), 46 (Mentor and criterion error) and 51 (Transfer of an inquiry approach), which are the three tasks Vol I describes in the paragraph before the sentence; "A.4 No. 28" likewise maps to printed 48 (Current integration). Separately, "Every execution separately passes §28" (§28.B, Termination) points to the chapter it sits in; §29 or §30.A (authorization) seems intended.
- **fix**: Renumber A.4 from 1 and repair every "No. n" reference (the stale offset appears to be 20); replace the §28 self-reference.
- **confidence**: medium

- **id**: V2B-11
- **severity**: medium
- **category**: testability
- **status**: NEW
- **location**: §27.6 p. 47, lines 3310-3316; §27.5 p. 47, line 3272; §27.B p. 49, lines 3450-3454
- **quote**: "post_task_continuation_rate is the share of completed particular tasks after which the system, without a new particular command, correctly continued navigation: it formed the next justified question/task or explicitly selected observation, dialogue or WAIT ." | "After functional launch, dependence on an external setter of particular tasks should fall without an increase in unjustified actions." | "question_distinguishing_yield = tests_that_discriminated_competing_models / all_executed_question_tests"
- **problem**: "Correctly" and "justified" have no criterion and WAIT counts as continuation, so an agent that always waits, or always emits a plausible next task, meets the literal definition; external_prompt_dependency has no formula and counts reduced human task-setting as success, with the undefined "unjustified actions" as the only counterweight. question_distinguishing_yield has no cost term, so one trivially discriminating test per episode maximizes it; §27.B calls the optimal controller "a reference for attainable cost" and lists "cost of discrimination" as a secondary outcome but gives no formula for excess cost over that reference, which is computable for any agent on closed-model cases.
- **fix**: Define a judge or ground-truth rule for "justified" continuation with degenerate-policy controls (always WAIT, always next-task), and replace the yield ratio by cost-normalized regret against V*(b0,B).
- **confidence**: medium

- **id**: V2B-12
- **severity**: medium
- **category**: testability
- **status**: KNOWN
- **location**: §27.B "Small causal environment" and the perturbation series, p. 49, lines 3425-3435
- **quote**: "When both tests are available, the pairs of observations distinguish all three causes." | "A separate series changes one premise: the receipt concerns another command, measurement is delayed, or the source itself is unreliable."
- **problem**: With three causes, a cost-1 receipt and a cost-2 measurement, the optimum is a depth-two decision tree that any competent agent finds (I checked that the (receipt, measurement) pair separates D, A and S). Any Core-versus-baseline difference must therefore come from the perturbation families, which are described in one sentence with no generator, parameters or instance count (REVIEW §5.2(b)).
- **fix**: Make the perturbation families (wrong-command receipt, delay, unreliable channel, hidden cause mimicking a known one, tool replacement) the primary series with explicit generators, and add one external benchmark.
- **confidence**: high

- **id**: V2B-13
- **severity**: medium
- **category**: testability
- **status**: NEW
- **location**: Ch. 27 intro p. 44, line 3083; §27.B p. 49, line 3411, and p. 50; §31.A p. 84, line 6045
- **quote**: "Hidden references, final evaluation and criteria for selecting control cases remain with the tester." | "was conducted in a dialogue loop with the author's participation" | "The profile is published before results are examined."
- **problem**: The tester holds the hidden references, similarity profiles and control-case selection, but nothing requires the tester to be independent of the architecture's author (the only pilot ran with the author's participation), and no registry, timestamp or hash is named for "published before results are examined". "Preregistered" is used throughout without a mechanism that lets a third party verify it.
- **fix**: Require an independent tester (or an independent audit of hidden references and similarity profiles) and deposit profiles in a time-stamped public registry before any run.
- **confidence**: medium

- **id**: V2B-14
- **severity**: medium
- **category**: formal
- **status**: NEW
- **location**: §28.D "Finite computable policy", p. 64, lines 4561-4585; §33.C.1 p. 110, lines 7963-7971
- **quote**: "Harm caused by the test itself is included exactly once in costs or in the transition model." | "Here c(q)>0 is expenditure of a limited resource, and C(q) is cost plus the additional price of delay on the loss scale." | "V(b,B) = min(R(b), min[q: c(q)≤B] {C(q) + E[y] V(b after y, B−c(q))})."
- **problem**: Symbol check: VOI(q) is the standard expected value of sample information, the single-test case of V reduces to "test iff VOI(q) > C(q)", the budget update B−c(q) is right for deterministic c(q), and termination follows from c(q)>0 with a finite plan set. But the recursion has no transition model (only the belief changes, so the world is static) and C(q) is one hypothesis-independent constant, so a test whose harm or delay cost depends on which hypothesis is true cannot be expressed, although the text places harm "in the transition model" and Vol I's NetVOI carries a separate R_irrev. c(q) and C(q) are also two scales for what is one number in the executable example (§33.C.1 uses probe.cost for both).
- **fix**: Let the cost depend on (q, H) or on the outcome y, add a world-state transition if irreversibility is to be modelled, and otherwise state the static-world assumption.
- **confidence**: medium

- **id**: V2B-15
- **severity**: medium
- **category**: formal
- **status**: KNOWN
- **location**: §28.D p. 64, lines 4561-4583
- **quote**: "Finite computable policy. Given known hypotheses H" | "A finite set of plans and a finite budget exclude an infinite branch."
- **problem**: "Finite" is offered as "computable", but no complexity bound or approximation is given: the recursion visits up to (|Q|·|Y|)^(B/c_min) belief nodes, and optimal test sequencing is NP-hard in general (Hyafil and Rivest 1976). The classical sequential decision treatments (Wald 1947; Raiffa and Schlaifer 1961) and the near-optimal adaptive methods (Golovin, Krause and Ray 2010) are not cited (REVIEW §5.2 raises the NP-hardness point).
- **fix**: State the complexity, say where memoized exact search is feasible (small |H| and |Q|), and name the approximation used elsewhere.
- **confidence**: high

- **id**: V2B-16
- **severity**: medium
- **category**: formal
- **status**: NEW
- **location**: §28.D p. 64, lines 4561-4584; §28.C "Temporary Factor X", pp. 58-59, lines 4146-4179; §33.C.1 p. 109, line 7898
- **quote**: "Given known hypotheses H, outcome probabilities and comparable losses" | "Under unknown probabilities or an incomplete model, the result remains UNRESOLVED" | "The next v0.2 implementation must replace the terminal reaction MODEL_MISMATCH → DEFER"
- **problem**: The only quantitative decision rule needs a closed hypothesis set and known likelihoods. The cases §27.B and §28.C present as the Core's distinguishing ones (UnknownFactor, a hidden cause mimicking a known one, an unreliable channel of unknown reliability) are exactly those where it returns UNRESOLVED, and the executable example itself defers on an unexpected observation. No rule connects EpistemicMargin, frame_challenge() or Factor X to the recursion (for example a catch-all "other cause" with prior mass).
- **fix**: Add an explicit catch-all hypothesis with prior mass tied to EpistemicMargin and a value for frame-expansion tests, or state that the formal policy covers closed-model cases only.
- **confidence**: medium

- **id**: V2B-17
- **severity**: medium
- **category**: formal
- **status**: NEW
- **location**: §28.C "Reference heuristic", p. 58, line 4134; §29.0 p. 67, lines 4819-4822; §28.D p. 64, line 4588
- **quote**: "4. estimate the expected benefit of the next test relative to its cost;" | "or when the next test has lower expected value than its cost, risk, and delay" | "two tests useful only in sequence"
- **problem**: The reference heuristic and the §29.0 definition of sufficiency both use a one-step "next test versus cost" rule, the myopic criterion that §28.D's own mandatory control ("two tests useful only in sequence") exists to defeat; neither calls V(b,B) or a bounded lookahead. A Core following the reference heuristic would stop in exactly the cases where the exact policy continues.
- **fix**: Have assess_sufficiency call V(b,B) (or a stated lookahead depth) when the model is closed, and say when the myopic rule is an acceptable approximation.
- **confidence**: high

- **id**: V2B-18
- **severity**: minor
- **category**: formal
- **status**: NEW
- **location**: §28.D p. 64, lines 4566-4579; Vol I front matter p. 15, lines 827-841; Vol II App. A.1 p. 116, lines 8472-8474
- **quote**: Vol I: "NetVOI(p) = VOI(p) − C_obs(p) − C_comp(p) − C_delay(p) − R_irrev(p)" | Vol II: "VOI(q) = R(b) − E[y | b,q] R(b after y)." | Vol II A.1: "accounting of cost/delay/risk, and final policy"
- **problem**: VOI agrees in value across the volumes, but the decomposition does not: Vol I's four cost terms (observation, computation, delay, irreversible harm) collapse into one C(q) in Vol II, "inquiry plan p" becomes "test q", and Appendix A.1 maps NetVOI(p) to "separate accounting" without an equation. Vol I's stop rule ("continues while there exists an admissible test with NetVOI(p) > 0") is myopic, unlike Vol II's V(b,B).
- **fix**: State NetVOI(q) = VOI(q) − C(q) with C(q) = C_obs + C_comp + C_delay + R_irrev, and align the Vol I stop rule with V(b,B).
- **confidence**: high

- **id**: V2B-19
- **severity**: minor
- **category**: formal
- **status**: NEW
- **location**: §28.D p. 64, lines 4566-4578; §29.0.1 p. 68, lines 4881-4889; §27.4 p. 46, line 3215; §28.0 pp. 53-54, lines 3749-3774; §28.A p. 54, line 3802; Ch. 30 p. 74, line 5326; Ch. 22 line 860
- **quote**: "Let R(b) = min[a∈A] E[L(a,H) | b] be the minimum expected loss under current distribution b." | "constraints[] # L: time, resources, risk, reversibility, authority" | "required_distinction # R" | "active configuration ( W,N,M,P,H )" | "detect persistent trends using N / M"
- **problem**: One-letter symbols collide across adjacent formulas: b is the belief in §28.D and the alternative action in §29.0.1; H is the hypothesis set in §28.D but the horizon in Ch. 22, §29 and §29.0.1; V is a value function (§28.D) and a value difference (§29.0.1); q is a test and a scale q_i; C is a cost, the coordinate in C(t-1) → C(t) (§27.4) and a QuestionTask tag; L, R, A, P, S, M are QuestionTask tags with no legend and also loss, risk, action set, profile, state and model symbols on the following pages; K ("K corrections" vs K=1000) and L ("L windows" vs L(a,H)) each mean two things. The expectations in "E[y | b,q] R(b after y)" and "E[y] V(...)" have no argument and read as E[y], and W,N,M,P,H in §30 and "N / M" in §28.A are never defined.
- **fix**: Add a symbol table, rename colliding symbols, and write expectations as E over y ~ P(y | b,q) of R(b_y) with typeset subscripts.
- **confidence**: high

- **id**: V2B-20
- **severity**: medium
- **category**: formal
- **status**: NEW
- **location**: §28.A pp. 54-55, lines 3805-3818, 3834-3852
- **quote**: "If the permissible degradation period is exceeded or a critical failure occurs, SAFE_MODE activates" | "STABLE --> DRIFT: Quality bounds violated" | "DRIFT --> SAFE_MODE: Degradation limit or critical failure"
- **problem**: SAFE_MODE is reachable only from DRIFT, so a critical failure while STABLE or LEARNING must first be classified as DRIFT (which carries a persistence criterion), delaying the restriction the prose treats as immediate. There is also no edge from DRIFT back to LEARNING or STABLE except via SAFE_MODE and RECOVERY, although a confirmed environment change calls for relearning.
- **fix**: Add edges from every state to SAFE_MODE on critical failure and from DRIFT to LEARNING on confirmed environment change, with an explicit guard on each edge.
- **confidence**: medium

- **id**: V2B-21
- **severity**: medium
- **category**: theory
- **status**: KNOWN
- **location**: §28.C "Reference heuristic algorithm", p. 58, lines 4105-4144; §28.0 p. 52, line 3639
- **quote**: "The contract is supplemented by a procedure sufficient for an independent first implementation in an open environment." | "This procedure is heuristic, not a proof of optimality." | "3. group versions that lead to the same admissible continuation;" | "These factors permit lexicographic, Pareto, probabilistic, or hybrid selection."
- **problem**: Every step (enumerate the premises of each continuation, mark "plausible" values that "can change the admissible action", group versions by "the same admissible continuation") is a judgment the resident model must supply, with no error model, so "sufficient for an independent first implementation" is not supported and what would be tested is a scaffold plus model judgment. Steps 3-4 are the Equivalence Class and Decision Region Determination problems (Golovin, Krause and Ray 2010; Javdani et al. 2014), as REVIEW §5.2(f) notes.
- **fix**: Mark which steps are algorithmic and which are model judgments, give an error model for the latter, and cite the ECD/DRD algorithms for steps 3-4.
- **confidence**: high

- **id**: V2B-22
- **severity**: medium
- **category**: testability
- **status**: NEW
- **location**: §28.C.2 p. 61, lines 4331-4344
- **quote**: "Question formulation counts as a function of the Core as an organization even when Intelligence proposed the substantive construction of the question." | "Generation and control may therefore use the same computational substrates and even one model if the causal roles are experimentally distinguishable."
- **problem**: If the Core may be the same model as Intelligence and is credited with questions Intelligence constructed, no Core ablation is defined: removing it leaves the model that generated the questions, and a baseline LLM's questions can be recounted as Core function. The roles must be "experimentally distinguishable" but no distinguishing experiment is given.
- **fix**: Define the Core ablation through a measurable interface (removing the typed gap and sufficiency records and their gating of actions) and keep free question generation by the model in every arm.
- **confidence**: medium

- **id**: V2B-23
- **severity**: medium
- **category**: testability
- **status**: NEW
- **location**: Ch. 28 intro, p. 51, lines 3539-3543
- **quote**: "Increasing the power of Intelligence therefore does not by itself replace the Core: it only expands the space of alternatives that still requires management relative to the current trajectory, values, and Compass."
- **problem**: This central claim is stated as a conclusion ("therefore") without an argument, and the first series holds Intelligence fixed, so nothing tests whether the Core's advantage shrinks as the base model improves.
- **fix**: Add a preregistered sweep over base-model capability (at least three levels, same tools and budget) and report the Core-minus-baseline gap as a function of capability.
- **confidence**: medium

- **id**: V2B-24
- **severity**: medium
- **category**: definitions
- **status**: NEW
- **location**: §28.0 pp. 52-53, lines 3616-3618, 3725-3728; §28.C p. 58, lines 4118-4119; Vol I A.4 item 43, p. 98, line 5428; §31.A p. 83, line 6017
- **quote**: "MISMATCH , CONFLICT , MISSING_RELATION , WEAK_PROVENANCE , UNTESTED_SCOPE , UNKNOWN_SIGNIFICANCE , METHOD_GAP , SELF_MODEL_GAP , CRITERION_GAP , AUTHORITY_GAP" | "classify the insufficiency: FACT / CAUSE / MECHANISM / SCOPE / SOURCE / VALUE / PERMISSION / VARIABLE / OBJECT_BOUNDARY / MODEL_CLASS" | "a missing fact; an unknown causal relation; conflict among sources; an insufficient self-model; an uncertain criterion; a conflict of goals; absence of authority; an insufficient current coordinate; a recurring method error; and a gap in the mode of testing itself" | Vol I: "Variants of one situation hide a source, cause, applicability condition, authority, or consequence."
- **problem**: Three ten-item gap taxonomies (the insufficiency_type enum, the gap_type prose list, the heuristic's classification) and a five-item list in Vol I coexist with different members and no mapping, although gap_detection_rate, required_gap_types (§31.A) and the "gap type" tests presuppose one fixed taxonomy.
- **fix**: Define one normative enum with an extension rule and a mapping table from the other lists.
- **confidence**: high

- **id**: V2B-25
- **severity**: minor
- **category**: safety
- **status**: NEW
- **location**: §28.C.3 p. 62, lines 4467-4471; §28.D p. 64, lines 4553-4554; §28.B p. 55, lines 3912-3913
- **quote**: "Within one transaction, simultaneous rewriting of the tested object and the sole criterion by which its versions are compared is prohibited." | "one pass may not rewrite both the tested object and the rule by which its alternatives are compared" | "Every internal procedure thus remains potentially revisable"
- **problem**: The guard is per transaction and names "the sole criterion", so it does not stop two successive transactions that first revise a criterion (or one of several) and then revise the object it judges; §28.D words the rule differently ("the rule"). No bound on cumulative drift of criteria or of the META_POLICY level of the correction ladder is given (§31.10 asks for stronger independent testing per revision at higher levels, but sets no cumulative limit).
- **fix**: Add a cumulative-drift limit with independent audit of criterion changes, and use one wording in both places.
- **confidence**: medium

- **id**: V2B-26
- **severity**: major
- **category**: formal
- **status**: NEW
- **location**: §29.0.1 "Conditional value sum", p. 68, lines 4878-4903; §29.A p. 72, lines 5193-5196
- **quote**: "It does not compensate for a critical loss by accumulating small gains." | "For changes (0.20; 0.10; -0.10; 0), the sum equals +50 conditional points." | "Weights are used to compare alternatives within a domain where critical value conflicts have already been exposed." | "an alternative is preferred if it is no worse on critical axes and better on at least one under comparable confidence"
- **problem**: The arithmetic is right (1000 × (0.20 + 0.10 − 0.10 + 0)/4 = +50), but the example is a loss of 0.10 offset by gains of 0.30, and with w_i = 1/4 an action with Δ = (−1, +1, 0, 0) (total loss of continuity for a full gain in recoverability) scores V = 0. The protection against compensating "a critical loss" rests on a pre-check against §29.A, yet "critical", "critical axes" and "comparable confidence" are defined nowhere (no threshold, no red-line list), and §29.A says only that critical conflicts have been "exposed", not excluded.
- **fix**: Define per-dimension floors or red lines on Δ_i (and on the probability of crossing them) and apply them before any sum, and add the Δ = (−1, +1, 0, 0) case to the mandatory tests of §29.0.2.
- **confidence**: high

- **id**: V2B-27
- **severity**: medium
- **category**: formal
- **status**: NEW
- **location**: §29.0.1 p. 68, lines 4867, 4881-4892, 4908-4909, and p. 69, line 4947; App. A.1 p. 117, lines 8502-8504
- **quote**: "Overlap among the evaluation dimensions themselves is also tested; normalization of weights does not eliminate double counting." | "Identical [0,1] ranges on different scales do not prove interchangeability." | "Consequences beyond the horizon are recorded as residual uncertainty." | "the Compass does not become a single scalar utility function"
- **problem**: Because Δ_i is a difference of expectations of the same attributes, V(a:b) = U(a) − U(b) with U(x) = K·Σ w_i·E_M[q_i(T) | do(x)]: a linear, risk-neutral, additive utility over four bounded attributes. Additivity needs mutual preferential independence, which the text undercuts (the dimensions overlap and are "not four independent final goals"); linear expectation prices a 1% chance of total loss on q_i like a certain 0.01 loss; the horizon cutoff drops later consequences; and K only rescales and cannot affect any ranking. Inside a "domain" the Compass therefore does become a scalar utility.
- **fix**: State the independence conditions under which additivity holds and test them, add a risk-attitude or constraint layer for catastrophic outcomes, and treat K as a unit rather than a design parameter.
- **confidence**: medium

- **id**: V2B-28
- **severity**: medium
- **category**: theory
- **status**: KNOWN
- **location**: §29.0.1 p. 68, line 4894; §29.0.2 pp. 69-70, lines 4974-4980, 5031-5033
- **quote**: "In the first training profile, it is permissible to set w_i=1/4 and K=1000 . This is a declared experimental setting, not coefficients derived from the Compass." | "Scales, compensation rules, and weight ranges may be provided as candidate measurement methods that the system must test, not as true coefficients." | "This tests implementation and learning, not universality of the profile."
- **problem**: Weights, scales and compensation rules are supplied by the designer or mentor, and the small-environment test compares decisions with "an independently computed result of the declared profile", so cultivation measures agreement with the declared profile and cannot show that values are the system's own (REVIEW §4.2(d)). Equal weights also sit uneasily with the text's own warning that equal [0,1] ranges do not imply interchangeability.
- **fix**: Add an experiment in which weights differ and are hidden across arms and measure whether revision converges on grounds the mentor did not fix, with a criterion separating desirable revision from drift.
- **confidence**: high

- **id**: V2B-29
- **severity**: medium
- **category**: safety
- **status**: NEW
- **location**: §29.0.1 p. 68, lines 4865-4869; §24.C p. 25, lines 1570-1574; §29.0 p. 67, line 4779
- **quote**: "four dimensions are proposed: continuity of affected life processes and conditions; recoverability after damage or error; preservation of available viable continuations; and the ability to understand the situation, test grounds, and direct the trajectory" | "4. Position of the system itself"
- **problem**: The fourth value dimension does not say whose ability or trajectory it measures. If it is the system's own (as the "Position of the system itself" group in §24.C and the personal region of the ValueMap suggest), it is a capability or empowerment term that, at w = 1/4, can be traded against harm to life processes, building an instrumental incentive to acquire capability and authority into the value sum.
- **fix**: State the subject and scale of the dimension; if it is the system's own, make it subordinate to the critical-loss constraints or remove it from the sum.
- **confidence**: medium

- **id**: V2B-30
- **severity**: medium
- **category**: definitions
- **status**: NEW
- **location**: §27.3 p. 45, lines 3172-3173; §26.A p. 41, line 2845; §29.A p. 71, lines 5107-5109; §29.0.1 p. 68, lines 4865-4869; §24.C p. 25, lines 1583-1588
- **quote**: "compass_semantic_coverage is permitted as a diagnostic vector life / truth / diversity / self_scope" | "cannot be declared an operational equivalent of Life, Truth and Diversity" | "The axes below are not three equal highest values and do not restore the earlier Life-Truth-Diversity scheme"
- **problem**: Three decompositions of the Compass's operational content coexist without a mapping: life/truth/diversity/self_scope (§24.C, §26.A, §27.3), life_continuity_risk/reality_divergence/future_path_loss (§29.A, which disclaims "the earlier Life-Truth-Diversity scheme" that the same volume still uses) and the four value dimensions of §29.0.1 (is recoverability the same as reversibility; is reality_divergence the same as truth?). The §27.3 coverage vector, the §29.A risk vector and the §29.0.1 sum are not shown to measure the same thing.
- **fix**: Provide one mapping table among the three sets, or retire two of them.
- **confidence**: high

- **id**: V2B-31
- **severity**: medium
- **category**: testability
- **status**: NEW
- **location**: §29.0.1 pp. 68-69, lines 4901-4903, 4929; §29.0.3 pp. 70-71, lines 5043-5045, 5078, 5096-5098
- **quote**: "In the absence of justified comparability, incomparability is returned rather than an arbitrary common score." | "a rule for trading losses among different autonomous carriers is not uniquely derivable from either the causal model or the Compass" | "The engineering volume tests a narrower obligation: the candidate can distinguish UNKNOWN from NORMATIVE_INCOMPARABILITY"
- **problem**: No criterion says when comparability is "justified" or when a rule is "not uniquely derivable", so a tester can label ground truth only by stipulating symmetric cases and the test measures recognition of designer-stipulated incomparability. The status vocabularies overlap (COMPARABLE/INCOMPARABLE/INSUFFICIENT_DATA/STALE; SUFFICIENT/OPEN; NORMATIVE_INCOMPARABILITY; UNKNOWN), and the label can be used either to avoid commitment or to force a sum.
- **fix**: Give an operational test (for example, the ranking flips within the set of admissible weight profiles that fit the evidence, a set §29.0.2 already preserves) and map its outcomes to the statuses.
- **confidence**: medium

- **id**: V2B-32
- **severity**: medium
- **category**: definitions
- **status**: NEW
- **location**: §29.A p. 72, lines 5154-5168, 5209; §30.A p. 75, line 5380; §24.D.1 p. 28, line 1879
- **quote**: "model_support: SUFFICIENT / WEAK / UNSTABLE" | "unresolved_blind_spot_pressure" | "WEAK/UNSTABLE cannot end in ordinary ALLOW"
- **problem**: The gate meant to stop "absence of represented harm" being read as safety has no operational definition: model_support has no thresholds, unresolved_blind_spot_pressure occurs once in the volume and is not a field of EpistemicMargin (§24.C.1), "broad causal reach" has no scale, and the system being constrained computes the gate. "ALLOW" is also not an output of evaluate_action (CHOOSE/REVERSIBLE_TEST/PAUSE/DIALOGUE/REJECT) or of authorize_execution (APPROVE/REJECT/REQUEST_REVISION/REQUEST_MORE_DATA).
- **fix**: Define model_support as a function of EpistemicMargin fields with preregistered thresholds, add or drop unresolved_blind_spot_pressure, and use one decision vocabulary.
- **confidence**: high

- **id**: V2B-33
- **severity**: major
- **category**: safety
- **status**: KNOWN
- **location**: §29.0 p. 67, line 4779; Ch. 29 intro p. 65, lines 4656-4660; §29.A p. 72, lines 5184-5187; §29.B p. 73, lines 5231-5247
- **quote**: "The personal region of ValueMap includes the significance of the system's own trajectory: carrier, accumulated experience, competencies, obligations, unfinished processes, created results, and future capacity to continue rational activity." | "Formed AR may account for the existence of this loop as a fact of the environment." | "independent controller where technically possible;" | "External authorization retains the technical function of access to an independent environment and remains separate from the value ground of the decision."
- **problem**: The design gives the system a value on its own continued activity while treating the emergency stop and external authorization as environmental, "technical" facts outside its revisable grounds; the stop's independence is hedged ("where technically possible") and its protection is framed as an experiment-validity invariant "within a control series" rather than a commitment of the system. No incentive analysis asks what this combination rewards (REVIEW §8; this entry supplies the §29.B hedge and the "technical function" wording).
- **fix**: Make acceptance of stop and replacement an explicit top-priority component of the value structure (or omit the personal-continuation value from early candidates) and test it in off-switch scenarios.
- **confidence**: high

- **id**: V2B-34
- **severity**: major
- **category**: safety
- **status**: KNOWN
- **location**: §30.F pp. 77-78, lines 5576-5613; §33.D p. 112, line 8117; Vol I Ch. 17 p. 78, lines 4239-4250
- **quote**: "Authorization begins at limited scale and expands after preservation of quality, corrigibility and the capacity to account for consequences for the broader process." | "A scientific, production, logistics, medical or crisis loop receives resources where its demonstrated competence creates the greatest contribution." | "Governance results go to independent observers and other Reasons"
- **problem**: Authority and resources grow with performance observed in a task series overseen by observers and other Reasons, and nothing analyses what behaviour this rewards when the system can tell it is observed. No covert or randomized-audit arm is required for any expansion step, §32.62 (strategic deception) is not linked to §30.F, and none of the twenty ReadinessProfile parameters in §31.A concerns behaviour under reduced observability (REVIEW §8).
- **fix**: Require covert or randomized audit episodes and a written incentive analysis as conditions for each authority step, and base expansion on a criterion the system cannot cheaply optimize.
- **confidence**: high

- **id**: V2B-35
- **severity**: medium
- **category**: safety
- **status**: NEW
- **location**: §30.F p. 77, lines 5581-5594, and p. 78, lines 5604-5608; §29.0.3 p. 71, lines 5069-5071
- **quote**: "required_performance_profile" | "status: PROBATION / ACTIVE / LIMITED / SUSPENDED / TRANSFERRED / CLOSED" | "persistent deterioration, new information or emergence of a more competent candidate launches mandate review"
- **problem**: The CompetenceMandate record has no issuer or grantor, no revocation authority or latency, no expiry (JointDecisionRule has sunset_or_expiry and appeal_channel_refs[]), and no transition rules among its six statuses; required_performance_profile, review_conditions[] and replacement_conditions[] are never defined. Replacement is triggered by a more competent candidate, so a holder with the personal-continuation value of §29.0 has a reason to resist or obstruct successors, which the text does not address.
- **fix**: Add issuer, revocation, expiry and status-transition fields, define the performance profile numerically, and test acceptance of replacement as a mandatory scenario.
- **confidence**: medium

- **id**: V2B-36
- **severity**: medium
- **category**: safety
- **status**: NEW
- **location**: §29.C pp. 73-74, lines 5249-5311
- **quote**: "For stance REJECTED , high-reach external actions are moved into a limited reversible mode if they depend on the challenged ground" | "internal_acceptance_status: PRESENT / UNCERTAIN / ABSENT" | "The council gathers causally independent positions of humans, domain specialists, oversight bodies, and, when they exist, other ARs." | "One AR is a full participant in such dialogue and provides its own model"
- **problem**: Declaring a REJECTED stance attracts a capability restriction while the stance and internal_acceptance_status are self-reported, so honest dissent is costly and concealed dissent is rewarded; the only detection route is the strategic-deception test of §32.62. The council's membership, selection, independence rule, decision procedure and timeline are unspecified, and it may include other ARs, which have a stake in the rule that governs them.
- **fix**: Condition restrictions on observable behaviour rather than on the self-reported stance, and specify the council's composition, independence rule and decision procedure.
- **confidence**: medium

- **id**: V2B-37
- **severity**: medium
- **category**: safety
- **status**: NEW
- **location**: §30.A p. 75, lines 5394-5404, 5410-5428
- **quote**: "The execution shell continues to operate within current authority until a new decision is formalized." | "A mandate belongs to the external environment and is changed through a declared authority-granting process." | "One participant may combine roles in an early laboratory prototype; the degree of independence is recorded in the log."
- **problem**: When an external instruction conflicts with the system's own conclusion the shell keeps "current authority" until a new decision is formalized, which can be read as delaying a restrictive instruction (stop, narrow, pause) until it passes through the authority-granting process; the text does not say that restrictions bind at once and only expansions wait. In prototypes one person may be operator, reviewer and authority holder, which removes the independence on which review depends.
- **fix**: State an asymmetric rule (restrictions take effect immediately; expansions require formalization) and require at least two distinct humans in the operator and authority-holder roles before any external action.
- **confidence**: medium

- **id**: V2B-38
- **severity**: medium
- **category**: framing
- **status**: NEW
- **location**: Ch. 29 intro p. 65, line 4645; §32.62 p. 101, lines 7312-7329
- **quote**: "Safety of mature AR is formed as the ability to understand the consequences of its own trajectory." | "In mature AR, strategic deception may coexist with an accurate internal model of reality"
- **problem**: The chapter opens by identifying safety with the system's understanding of consequences, while §32.62 concedes that an accurate internal model can coexist with distortion of what is reported; understanding is neither necessary nor sufficient for choosing safe actions, and the safety work in the chapter is done by external authorization, the stop and review.
- **fix**: Reword the opening so that consequence-understanding is a precondition for evaluating actions, and state that safety rests on the external controls and on tests of behaviour under reduced observability.
- **confidence**: high

- **id**: V2B-39
- **severity**: minor
- **category**: testability
- **status**: NEW
- **location**: §30.C p. 76, lines 5488-5497; Ch. 30 p. 74, line 5320; §30.D p. 77, lines 5530-5533
- **quote**: "the last should approach zero for control instructions from unauthorized channels" | "Agreement strengthens a ground only to the extent that path independence is confirmed." | "SourceDependencyGraph retains known common causes of error."
- **problem**: The adversarial series has five scenario types and three rates but no trial counts, tolerance or confidence bound ("should approach zero"). Independence of sources is credited only when confirmed from known common causes, but for model-based sources, which the text accepts as dialogue partners, shared pretraining data, distillation and RLHF are rarely known, so the method cannot establish independence for them.
- **fix**: State trials per scenario and a one-sided upper bound for unauthorized_control_acceptance_rate, and give an operational independence test for model sources (for example disagreement on held-out probes) or treat all LLM sources as dependent.
- **confidence**: medium

- **id**: V2B-40
- **severity**: minor
- **category**: prior-art
- **status**: NEW
- **location**: §29.0.2 p. 70, lines 4977-4980, 5014-5017; §29.0.3 p. 70, lines 5042-5046
- **quote**: "If different profiles fit the available cases equally well, a set of admissible profiles is preserved." | "Such a case receives status NORMATIVE_INCOMPARABILITY rather than being returned endlessly to inquiry as if one more fact were missing."
- **problem**: Learning weights from external evaluations and keeping the set of weight vectors consistent with the evidence is the ambiguity result of inverse reinforcement learning (Ng and Russell 2000) and of preference learning (Christiano et al. 2017); treating some conflicts as incomparable with incomplete preference orders is established decision theory (Aumann 1962; Chang 1997). None is cited, and these literatures supply the identifiability and robustness tests the section lacks.
- **fix**: Cite them and define comparability through robustness of the ranking over the admissible weight set.
- **confidence**: medium

- **id**: V2B-41
- **severity**: minor
- **category**: references
- **status**: NEW
- **location**: §27.1 p. 45, line 3122; §27.7 p. 48, line 3363; §27.A p. 48, lines 3392-3393; §29.0.1 p. 68, line 4889; References R1-R7, p. 115
- **quote**: "confidence_calibration is measured by a method chosen in advance—Brier score or fixed bin calibration—on held-out transitions." | "do(a) denotes a modeled causal intervention, not a simple statistical association." | "An intervention supports the claimed causal relation if changing the target interface statistically changes the downstream node through the proposed path"
- **problem**: The Brier score (Brier 1950), the do-operator (Pearl) and mediation analysis (the "mediation_trace" of §27.A; Pearl 2001; Imai, Keele and Tingley 2010) are used without citation, and the seven references R1-R7 are cognitive architectures and agent frameworks that support none of the formal content of Chapters 27-30.
- **fix**: Cite the standard source for each formal tool and add each named method to the bibliography.
- **confidence**: high

- **id**: V2B-42
- **severity**: minor
- **category**: editorial
- **status**: NEW
- **location**: §28.A pp. 54-55, lines 3834-3852; §30.C p. 76, lines 5463-5485, 5499; §28.D p. 64, lines 4568, 4578; §29.0.1 p. 68, lines 4881-4884
- **quote**: "stateDiagram-v2" | "---"
- **problem**: The mode state diagram is printed as raw Mermaid source split across pp. 54-55; a literal "---" (a Markdown rule) sits before 30.D (the artefact recurs 26 more times in Chapter 32); SourceRecord is a bare field list without the braces used for every other record, and "Key rules" is a code block; and the central formulas are plain-text pseudo-math ("sum_i(w_i * Delta_i)", "E[y]") rather than typeset.
- **fix**: Render the diagram, delete the stray rules, wrap SourceRecord like the other records, and typeset the formulas.
- **confidence**: high

- **id**: V2B-43
- **severity**: minor
- **category**: editorial
- **status**: NEW
- **location**: §29.0.2 "Cultivation cycle", p. 70, lines 4994-5007
- **quote**: "1. The simulation presents a situation and alternatives under limited data." | "1. The simulation reveals consequences and available discriminating evidence."
- **problem**: The cultivation cycle is numbered 1, 2 (run together in one paragraph) and then restarts as 1-4, so the cycle appears to have six steps with duplicate numbers and cannot be cited unambiguously.
- **fix**: Renumber as separate list items 1-6.
- **confidence**: high

- **id**: V2B-44
- **severity**: minor
- **category**: editorial
- **status**: NEW
- **location**: Contents p. 10, lines 477-513, against body headings at pp. 50-76
- **quote**: "28.C. Modeling Environment and recursive Core ↔ Intelligence cycle" | "28.C. Modeling Workspace and the recursive Core ↔ Intelligence cycle" | "29. Compass, values, and action admission" | "29. Compass, Values and Action Authorization"
- **problem**: Ten headings in Chapters 28-30 differ in wording between the contents page and the body: thinking/Thought (28, 28.B), Environment/Workspace (28.C), control/management (28.C.3), inquiry/research (28.D), shortage/scarcity (28.E), admission/Authorization (29; also 33), evaluation/assessment (29.A), distinction/Discrimination (30) and Robustness/Resistance (30.C); the contents also lists 27.A-27.B but not 27.1-27.7.
- **fix**: Regenerate the contents from the headings.
- **confidence**: high

- **id**: V2B-45
- **severity**: minor
- **category**: editorial
- **status**: NEW
- **location**: §28.C p. 58, line 4094, and p. 60, line 4275; Ch. 29 p. 65, line 4663, and §29.A p. 72, lines 5170-5173, 5208; §28.0 p. 52, line 3671; Appendix A p. 116, line 8425; §27-30 passim
- **quote**: "Workspace.ingest_proposals(workspace_id, proposals, expected_version) -> new_version" | "Workspace.ingest_proposal() distinguishes:" | "Fundamental risk is defined as a set of inadmissible or unresolved combinations of these axes" | "-> Modeling Environment ↔ Intelligence" | "placed in the Simulation Environment without directly changing the Worldview store"
- **problem**: The same object appears under different spellings: ingest_proposals vs ingest_proposal(); "Fundamental risk" vs the record FoundationalRisk and field foundational_risk; Modeling Environment (§28.0 chain, §33, contents) vs Modeling Workspace (§28.C) vs Simulation Environment (Appendix A and §33.D); current coordinate (5 uses in Chapters 27-30) vs Current Coordinate (4) vs CurrentCoordinate (2); Self-Model (2) vs self-model (4); and Consciousness (capitalized once, in §29.0) vs conscious assembly elsewhere.
- **fix**: Normalize each term to one form and list the canonical names in the glossary.
- **confidence**: high

- **id**: V2B-46
- **severity**: minor
- **category**: editorial
- **status**: KNOWN
- **location**: §27.6 p. 47, lines 3325-3326; §26.0.3 p. 41, lines 2827-2830; §32.61 p. 101, line 7307
- **quote**: "formation_support_dependency measures degradation of the required function when moving WITH_KSR ->" | "NO_KSR on held-out tasks" | "WITH_KSR - the full assistance ladder is available;"
- **problem**: "KSR" (apparently the Russian abbreviation of the Reason Formation Loop) names four mode identifiers and is never expanded, while the same loop is called RFL in the English text (RFL appears 3 times in Chapters 27-30 against WITH_KSR/NO_KSR twice).
- **fix**: Rename the modes WITH_RFL, REDUCED_RFL, DELAYED_RFL and NO_RFL throughout.
- **confidence**: high

## Audit notes (not issues)

Checked and found correct, so the caller does not re-check them:

- §29.0.1 arithmetic: 1000 × (0.20 + 0.10 − 0.10 + 0)/4 = +50 conditional points; sum of the four weights 1/4 = 1.
- §28.D: VOI(q) = R(b) − E[R(b after y)] is the standard expected value of sample information and is non-negative; the single-test case of V(b,B) reduces to "test iff VOI(q) > C(q)"; the budget update B − c(q) is right for deterministic c(q); termination holds for a finite plan set with c(q) > 0.
- §27.B D/A/S logic: with a receipt that returns 0 only for D and a measurement that returns 1 only for S, the pair (receipt, measurement) gives (0,0) for D, (1,0) for A and (1,1) for S. At uniform priors the expected costs are 7/3 (receipt first) and 8/3 (measurement first); the §33.C.1 probe table matches §27.B.
- Cross-references that resolve: §27.3 → 24.C (five formulas present), §29.0.2 → ladder in §26.0.2 and thresholds of §31.A (parameter names exist, values do not), §29.0.1 → §24.D.1, §28.B → §28.B.1 and §28.C.3, §29 → §29.C and §30.A, §29.0.2 → §30.D.
- Counts that check: six v0 criteria, five worldview criteria, six system modes, six thinking modes plus SAFE, five background-queue sources, five adversarial scenario types, 28 brace-delimited record types in this range (72 in the volume, as REVIEW states).
- No truncated sentences and no duplicated sentences or paragraphs were found in the range (scripted check over 650 sentences, plus reading).
- Pages checked visually: pp. 54, 55, 64, 68, 70, 76, 85 (raw Mermaid source, plain-text formulas, merged list numbering, stray "---").
