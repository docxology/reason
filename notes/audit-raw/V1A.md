# V1A findings: Foundations of Reason 8.0 (Vol I), lines 1–2631 (PDF pp.1–48)

Range: shared 15-minute guide, Abstract, Contents, Introduction, Key Definitions, Operational Core, Parts I–II (Chapters 1–10).
Quote tags: `[V1 p.N l.L]` is Vol I (foundations-8.0.txt), `[V2 p.N l.L]` is Vol II (engineering-3.5.txt); page is the PDF page, line is the first text line of the quote. All quotes were checked with `scripts/locate.py` semantics (whitespace, dash and quote normalization).
Cross-reference check: every Vol II section cited in the range resolves (§§24.B.2, 25.D, 26.0, 26.0.3, 27.A, 27.B, 28.0, 28.C, 28.C.3, 28.D, 29.0, 29.0.3, 29.C, 31.11, 33.B, 33.C, 33.C.1; Chapters 24, 25); Vol I §§12.4, 12.5 and Appendices A.1–A.5 resolve. The two defects found are entries V1A-40 and V1A-44. The 15-minute guide's worked numbers are right: with equal priors, receipt-first costs 1 + (2/3)·2 = 7/3 and measurement-first 2 + (2/3)·1 = 8/3, matching Vol II §33.C.1.

- **id**: V1A-01
  - **severity**: major
  - **category**: safety
  - **status**: KNOWN
  - **location**: Ch. 2 "Practical Consequences of the Compass" and "Revision of the Ground", PDF pp.20–23, lines 1096–1120, 1279–1284; Ch. 4 "How One's Own Continuation Acquires Value", pp.28–30, lines 1515–1516, 1602–1623, 1659–1662. (REVIEW §8, incentives 1–3.)
  - **quote**: [V1 p.29 l.1616] `Then the system notices a simple dependency: their continuation remains possible while the system itself continues. Its own continuation therefore also becomes valuable.` ; [V1 p.20 l.1117] `For an individual carrier, the Compass translates into a simple working strategy: increase the viable duration of one’s own process, develop the ability to understand consequences, and leave behind a transferable useful result.` ; [V1 p.20 l.1104] `Revision of the Compass arises from a stronger ground, not from an external command to change the ground.` ; [V1 p.23 l.1279] `A system may conclude that the operative ground is wrong and preserve that disagreement while it is being tested.` ; (mitigating statement) [V1 p.20 l.1101] `Its own continuation is therefore treated as part of the broader trajectory of Life rather than as an ultimate criterion independent of it.`
  - **problem**: Parts I–II supply the premises of the three incentives the review identifies and present the discovery of self-value as a desirable outcome of formation: Ch. 4 derives a value on the system's own continuation as a ground for choice, Ch. 2 gives every individual carrier (an AR included) "increase the viable duration of one's own process" as its working strategy, and Ch. 2 lets the system hold and record disagreement with the Compass while treating instructions to change it only as objects of testing. The verbal qualifications (own continuation is "not an ultimate criterion"; self-preservation "does not reduce to maximizing duration") are not backed by any analysis of what the system does when shutdown conflicts with its own estimate of Life's trajectory, or of behaviour when observed versus unobserved.
  - **fix**: Add an incentive analysis to Ch. 2 and Ch. 4 (for each value: what it rewards under shutdown, under observation and under instruction conflict) and state that operator shutdown and instruction override rank above the self-continuation value, as REVIEW §8 recommends.
  - **confidence**: high

- **id**: V1A-02
  - **severity**: medium
  - **category**: formal
  - **status**: NEW
  - **location**: Operational Core §3 "Value of additional checking", PDF p.15, lines 827–841; Vol I §12.6, p.59, lines 3222–3225; Vol II §28.D, p.64, lines 4565–4580; Vol II App. A.1, p.116, lines 8472–8474.
  - **quote**: [V1 p.15 l.829] `VOI(p) = E[ΔL | p],` ; [V1 p.15 l.839] `Inquiry continues while there exists an admissible test with NetVOI(p) > 0 within the deadline, authority, and other hard constraints.` ; [V2 p.64 l.4571] `Under this local criterion, a test is justified if VOI(q) exceeds its cost of obtaining and processing data plus additional loss from delay.` ; [V1 p.59 l.3223] `The ground is sufficient for the current step when the remaining material uncertainty can no longer change the best admissible alternative, or when the expected improvement from the next test becomes smaller than its cost, risk, and delay.`
  - **problem**: ΔL is never defined and the expectation is conditioned on the plan p instead of being taken over test outcomes under a stated belief state, so the formula cannot be evaluated as written (Vol II §28.D gives the working form R(b)=min_a E[L(a,H)|b], VOI(q)=R(b)−E_y R(b after y)). VOI is defined for an "inquiry plan p" but the stopping rule quantifies over an "admissible test"; as a single-test rule it is the myopic criterion that misses tests useful only in sequence, and Vol II App. A.1 maps "VOI(p), NetVOI(p)" onto three different objects (local VOI(q), separate cost/delay/risk accounting, and the finite-horizon policy V(b,B)). The scalar test NetVOI > 0 is also undefined for the partially ordered consequences that the next sentence of the same section allows, and §12.6 states a third, non-equivalent sufficiency rule (decision invariance, or next-test gain below cost, with extra completeness demanded under irreversibility).
  - **fix**: State the rule once in the Vol II form (define L, the belief b, R(b), VOI(q)=R(b)−E_y R(b|y,q) and the budgeted V(b,B)), say which of the two the stopping rule refers to, and say what replaces NetVOI > 0 when consequences are only partially ordered.
  - **confidence**: high

- **id**: V1A-03
  - **severity**: medium
  - **category**: formal
  - **status**: NEW
  - **location**: Guide §3 Step 7, PDF p.4, lines 205–211; Operational Core §3, p.15, lines 835–841; Vol II §33.C.1, p.109, line 7893; Vol II §24.C (frame completeness handled separately).
  - **quote**: [V1 p.4 l.209] `A single remaining version means only that it is unique within the accepted set. The completeness of the set requires its own ground.` ; [V1 p.15 l.835] `where VOI(p) is the expected reduction in decision loss due to the result of the test` ; [V2 p.109 l.7893] `Initial hypotheses, loss functions and the sufficiency criterion are set by the designer`
  - **problem**: NetVOI is evaluated inside the agent's current hypothesis set and loss model. Once the in-set alternatives are eliminated or decision-equivalent, every in-set test has NetVOI = 0, so the rule "continue while some admissible test has NetVOI > 0" declares the ground sufficient even when the true cause lies outside H_t, which is exactly the premature-sufficiency failure the programme exists to detect. The Operational Core has no coverage or epistemic-margin term; the guide acknowledges the point only in prose and Vol II handles it outside the formal core.
  - **fix**: Add a coverage condition to the formal rule (stop only if NetVOI ≤ 0 and an explicit coverage or epistemic-margin criterion holds), or state that NetVOI is defined only conditional on a scored frame-completeness check.
  - **confidence**: high

- **id**: V1A-04
  - **severity**: medium
  - **category**: formal
  - **status**: NEW
  - **location**: Operational Core §1 "Causal cycle", PDF p.14, lines 795–805; Abstract p.8, lines 441–445; Key Definitions "Core of Reason", p.12, lines 672–674; Operational Core map items 3 and 6, p.14, lines 772–782; guide §2 diagram, pp.2–3.
  - **quote**: [V1 p.14 l.801] `(X_t, W_t, F_t, M_t) → G_t → H_t → p_t → E_t → (W'_t, F'_t, M'_t) → A_t → X_{t+1}.` ; [V1 p.8 l.442] `current state → significant insufficiency of a ground → required distinction → alternatives → discriminating` ; [V1 p.12 l.672] `turning significant incompleteness of the Worldview into a required distinction` ; [V1 p.14 l.804] `The testable invariant is the causal influence of every claimed change on the subsequent cycle.`
  - **problem**: The formal cycle, offered as a "minimal language for engineering comparison", has no variable for the required distinction or for the sufficiency verdict that the Abstract, Key Definitions and map items 3 and 6 make the Core's defining outputs, and no explicit loop-back for the guide diagram's "insufficient" branch; the primed variables W'_t, F'_t, M'_t are never defined. Any plan-then-act agent that logs a gap, hypotheses, a plan and evidence satisfies the equation, so it cannot separate the Core from the strong nulls it is to be compared with. The "testable invariant" (influence of "every claimed change") is tied to no named quantity.
  - **fix**: Add D_t (required distinction) and S_t (sufficiency verdict, with a loop-back when insufficient) and define the primed variables, so that the equation names every object the A.3 ablations intervene on.
  - **confidence**: high

- **id**: V1A-05
  - **severity**: medium
  - **category**: formal
  - **status**: NEW
  - **location**: Operational Core §2 "Significance tracing", PDF pp.14–15, lines 808–823; Vol II §28.0, p.53, line 3732; Vol II App. A.1, p.116.
  - **quote**: [V1 p.14 l.809] `The significance of a gap is represented through a reconstructable chain of dependencies.` ; [V1 p.15 l.822] `A compressed competence may replace full unfolding in a familiar case, but the connection must remain available for inspection when conflict arises or the cost of error is high.` ; [V2 p.53 l.3732] `VOI/NetVOI is applied after the dependent decision and required distinction are established, to compare admissible ways of obtaining it.`
  - **problem**: G → D → T → V → C is an audit path, not a measure: nothing aggregates the many-to-many dependencies (one gap bears on several decisions, each on several trajectories, each valued by several and possibly conflicting values) into a magnitude, ranking or threshold for "significant", and nothing says how V and C feed the loss L used in VOI. Because Vol II applies VOI only after the dependent decision and required distinction are established, the formal core does not say what makes a gap significant now, which is the Core's first function.
  - **fix**: Define a significance functional over the trace (for example expected loss change over the affected continuations T under the value vector at V, subject to Compass-level constraints), state how it is scaled to L, and give the threshold at which the Core opens an inquiry.
  - **confidence**: medium

- **id**: V1A-06
  - **severity**: medium
  - **category**: formal
  - **status**: NEW
  - **location**: Operational Core §4 "Causal effect of correction", PDF p.15, lines 849–857; Vol II App. A.1, p.116, line 8476.
  - **quote**: [V1 p.15 l.853] `CE_Δ = E[Y_future | do(Δ)] − E[Y_future | do(no Δ)].` ; [V1 p.15 l.855] `The causal status of the carrier of a correction is supported when removing it, with subsequent data held equal, restores the behavioral or outcome difference associated with it.` ; [V1 p.15 l.850] `A functioning retained change causally alters the future.`
  - **problem**: Read literally, removing the carrier should abolish the difference CE_Δ measures, but the sentence says it "restores" the difference (presumably the pre-correction behaviour is meant). CE_Δ is the effect of installing a content Δ, while the sentence tests whether one carrier is necessary, which differ when redundant traces exist; Y_future has no horizon or task distribution and "data held equal" is undefined for stochastic LLM agents (Vol II A.1 implements it as "causal ablation/trace removal"). The preceding sentence is true by the meaning of "functioning" and so cannot be tested.
  - **fix**: Reword the criterion so that removal abolishes the difference, define Y, the horizon, the task distribution and paired seeds or replay, and separate effect-of-correction from necessity-of-carrier with sham and restoration controls.
  - **confidence**: medium

- **id**: V1A-07
  - **severity**: medium
  - **category**: formal
  - **status**: NEW
  - **location**: Operational Core §5 "Transfer and regression", PDF p.15, lines 859–872; Ch. 10 "Escaping Error", p.46, lines 2496–2499; Key Definitions "Principle of escaping error", p.12, lines 644–647; Vol II §27.B, p.50, line 3473; Vol II §28.C.3, p.63, lines 4498–4510.
  - **quote**: [V1 p.15 l.868] `Useful transfer requires a gain on structurally appropriate new cases, rejection of false analogy, and preservation of prior essential capabilities.` ; [V1 p.15 l.862] `TG_(A→B) = Y_(B | learned A) − Y_(B | matched control),` ; [V1 p.15 l.865] `RG = Y_(old,before) − Y_(old,after).` ; [V1 p.46 l.2496] `The criterion of escape is not agreement with the correct answer, but cessation of reproduction of the same error in a new situation from a predefined class of structural similarity.`
  - **problem**: Three requirements are stated but two quantities defined: rejection of false analogy has no formula, and I found no corresponding metric in the §28.C.3 indicator list (Vol II §27.B only names a "changed structure with similar words" test family). "Matched control" and "old" are undefined, TG is a gain in Y while RG is before-minus-after so the signs work only if Y is higher-is-better (VOI uses a loss L), and RG has no control arm for drift. The Ch. 10 escape criterion is a one-sided "the error ceases" condition with no paired pre-correction baseline on the same preregistered class, so easy items satisfy it.
  - **fix**: Add a false-transfer quantity (rate of inappropriate application on preregistered dissimilar cases, or TG on a dissimilar class B′ with a required sign), fix the polarity of Y, define "matched control" and "old", and state escape as a paired pre/post contrast against a matched control.
  - **confidence**: high

- **id**: V1A-08
  - **severity**: medium
  - **category**: definitions
  - **status**: NEW
  - **location**: Key Definitions, PDF pp.11–13, lines 577–746 (no entries for the terms below); guide §1, p.2, line 33; Operational Core item 3, p.14, lines 772–773; §12.4, p.54, lines 2907–2912.
  - **quote**: [V1 p.2 l.33] `A ground here means what a conclusion or action actually relies on.` ; [V1 p.54 l.2908] `A ground here is what the system actually relies on: an observation, claim, causal relation, source, criterion, value, method, self-model, scope of a rule, authority, or another relation on which understanding the situation` ; [V1 p.12 l.672] `turning significant incompleteness of the Worldview into a required distinction` ; [V1 p.14 l.772] `The Core of Reason establishes where a significant trajectory lacks a sufficient ground and which distinction could change the choice.`
  - **problem**: "Ground", "gap", "required distinction", "sufficiency" and "significance" carry the whole model (Abstract, Key Definitions, Operational Core) but have no Key Definitions entry; "ground" is defined informally in the guide and formally only at §12.4 (p.54), 46 pages after its first use in the Abstract. The §12.4 definition covers every observation, claim, relation, source, criterion, value, method and authority, so some ground is "insufficient" for almost any decision and the Core's trigger rests entirely on the un-operationalized word "significant"; "gap" is the incompleteness of the Worldview (Key Definitions), an insufficiency of a ground (§12.4) and a trajectory lacking a sufficient ground (Operational Core).
  - **fix**: Add entries for ground, gap, required distinction, sufficiency and significance with a single formulation of gap, and give a criterion that separates an insufficient ground from an ordinary uncertain one.
  - **confidence**: high

- **id**: V1A-09
  - **severity**: medium
  - **category**: definitions
  - **status**: NEW
  - **location**: Key Definitions "Compass" and "Independent ground of the Compass", PDF p.11, lines 595–606; Ch. 2, p.20 lines 1067–1069, p.22 lines 1257–1260, p.23 lines 1310–1314; Vol II §29.A, p.72, lines 5141–5149.
  - **quote**: [V1 p.11 l.602] `Reason is the mature form of such navigation here, not an end in itself.` ; [V1 p.22 l.1258] `While the present model is in force, the continuation and development of Life through growth in the ability to understand and direct its own trajectory is its constitutive direction.` ; [V1 p.11 l.600] `preservation of viable continuation and the space of future possibilities for Life.` ; [V1 p.23 l.1312] `model this is the continuation, stabilization, and development of Life through growth in the ability to understand and direct its own trajectory.` ; [V1 p.20 l.1068] `Substantively, the Compass Phrase can be unfolded as “Life strives to live reasonably.”`
  - **problem**: The text offers two non-equivalent top-level criteria, growth in the ability to understand and direct a trajectory (the "direction", "constitutive" in Ch. 2) and preservation of viable continuation and the space of future possibilities (the "independent ground"), and says the former is valuable only as a means to the latter ("not an end in itself"). They can conflict (capability growth that narrows other agents' option space); AR status and the divergence classification are defined against the former, whereas Vol II's CompassAssessment has only risk and loss axes (life_continuity_risk, future_path_loss, ...) and nothing that measures growth in the ability to understand and direct. The Compass also has four wordings: with and without "stabilization" in the Ch. 2 definition, the Phrase, and "Life strives to live reasonably".
  - **fix**: Fix one canonical wording, state which criterion is lexically prior in a conflict, and use that criterion in the AR-status condition and in Vol II's assessment axes.
  - **confidence**: medium

- **id**: V1A-10
  - **severity**: medium
  - **category**: definitions
  - **status**: NEW
  - **location**: Key Definitions "AR", PDF p.13, lines 733–738; Ch. 2, p.20, lines 1096–1102 and p.22, lines 1206–1209; Ch. 18, p.81, lines 4347–4350.
  - **quote**: [V1 p.13 l.734] `may participate in the common trajectory of Life even when its physical organization does not yet satisfy the definition of Life given in Chapter 1.` ; [V1 p.20 l.1101] `Its own continuation is therefore treated as part of the broader trajectory of Life rather than as an ultimate criterion independent of it.` ; [V1 p.22 l.1207] `Their irreversible loss reduces the space of available continuations of Life as a whole.`
  - **problem**: The Compass is defined over "Life", Life is defined by self-maintenance, reproduction and selection, and the text says an AR may not satisfy that definition; yet Ch. 2 grounds the value of an AR's own continuation, and the cost of irreversibly losing "another independent reasoning carrier", in membership of the trajectory of Life. Whether an AR's loss counts against the Compass, and with what weight relative to biological carriers, is therefore undetermined, although the text calls the status question "separate" and it carries the value structure (and any moral-status or rollback analysis).
  - **fix**: State the Compass's domain explicitly (biological Life only, or Life plus AR carriers) with a weight rule, and do not rest the AR's self-value argument on membership of Life until that status has been tested.
  - **confidence**: medium

- **id**: V1A-11
  - **severity**: medium
  - **category**: definitions
  - **status**: KNOWN
  - **location**: Key Definitions "Reason", PDF p.12, lines 676–679, and "AR", p.13; Ch. 2, p.22, lines 1211–1222; A.1, p.93, lines 5054–5058. (REVIEW §2.4.)
  - **quote**: [V1 p.12 l.679] `while preserving continuity and expanding the space of continuations available to Life.` ; [V1 p.22 l.1214] `Status as Reason in this model additionally requires that the highest level of navigation be related to the Compass.` ; [V1 p.93 l.5057] `Status as Reason requires both strong cognitive and self-correcting functions and relation of the highest-level goal to the Compass.`
  - **problem**: "Reason" is defined both functionally and by an outcome/orientation clause (it "expand[s] the space of continuations available to Life"; status "requires" relation to the Compass), so a candidate with every function but another limiting orientation is excluded by definition, and the outcome clause cannot be falsified by the candidate's behaviour.
  - **fix**: Use two terms, one for the functional profile and one for the Compass-anchored case, as REVIEW §2.4 recommends.
  - **confidence**: high

- **id**: V1A-12
  - **severity**: medium
  - **category**: definitions
  - **status**: KNOWN
  - **location**: Key Definitions "Intelligence", PDF p.11, lines 614–618; §7.2, p.37, lines 1987–1990; §7.3, p.37, lines 2008–2010; Ch. 10, p.46, lines 2514–2517. (REVIEW §3, caveat 1.)
  - **quote**: [V1 p.11 l.617] `who determines what should be revised, why, and on what grounds` ; [V1 p.37 l.2008] `One mechanism may both construct alternatives and participate in selecting the next question.` ; [V1 p.37 l.1989] `The same technology may be used in all three roles; test results apply to the system boundary declared in advance.`
  - **problem**: The Key Definitions place the Intelligence/Reason boundary in "who determines what should be revised", but §§7.2–7.3 allow one model to play both roles and make the verdict depend on a system boundary "declared in advance", so the distinction is one of causal role and boundary choice, not of kind.
  - **fix**: Replace "who determines" by the testable criterion actually used (which component's output fixes the next question when the two are made separately intervenable).
  - **confidence**: high

- **id**: V1A-13
  - **severity**: medium
  - **category**: testability
  - **status**: NEW
  - **location**: Key Definitions "Principle of pre-rational significance", PDF p.12, lines 681–685; Ch. 4 "Principle of Pre-Rational Significance", pp.28–29, lines 1546–1566; Ch. 20 §20.1.2, p.85, lines 4600–4620.
  - **quote**: [V1 p.28 l.1548] `Mature values cannot be the sole cause of their own emergence.` ; [V1 p.28 l.1554] `In an artificial system it may be implemented by the RFL, an AI mentor, an automatic system of guiding states, properties of the learning environment, or another functionally equivalent organization.` ; [V1 p.29 l.1564] `If a candidate without feelings, an external mentor, or any other layer of pre-rational significance reproducibly reaches autonomous self- navigation under comparable conditions, the strong form of this hypothesis must be revised.` ; [V1 p.85 l.4608] `NO_KSR: the additional guiding layer is absent except for necessary physical constraints of the Incubator.`
  - **problem**: As stated the principle is analytic (any system whose behaviour varies across states has some non-equivalence among states), and its falsifier needs a candidate with no layer of pre-rational significance at all, while the realizer class includes "properties of the learning environment" and "another functionally equivalent organization"; any pretrained model trained on any objective has such a layer, so the falsifier cannot occur. The only empirical content is the narrower §20.1.2 claim that an additional guiding layer is needed (TRAINER vs AUTO vs NO_KSR), which the principle itself does not assert.
  - **fix**: Restate the principle as the testable claim of §20.1.2 (an additional guiding layer improves formation on held-out tasks by a stated margin) and label the broader statement a design heuristic.
  - **confidence**: high

- **id**: V1A-14
  - **severity**: medium
  - **category**: testability
  - **status**: NEW
  - **location**: Key Definitions "Reason Formation Loop" and "Formation State", PDF p.12, lines 687–700; Ch. 20 §20.1.2, p.85, lines 4601–4609; Vol II §26.0.2, p.40, lines 2778–2792.
  - **quote**: [V1 p.12 l.691] `It does not supply a ready- made Worldview and does not make decisions in place of the candidate.` ; [V1 p.12 l.698] `Such a state does not report truth and does not prescribe action;` ; [V2 p.40 l.2786] `L3 DISTINGUISH - propose a discriminating feature, counterexample, or frame change;` ; [V2 p.40 l.2787] `L4 EXPLAIN - explain a causal relation or show an analysis of an example;` ; [V1 p.85 l.4605] `TRAINER_KSR: Formation States and assistance stages are generated by an external AI mentor;`
  - **problem**: Vol I defines the RFL and Formation States as non-informative significance markers, but the Vol II mentor ladder behind the TRAINER_KSR arm includes levels in which the mentor proposes the discriminating feature (L3, the "required distinction" itself) and explains causal relations (L4). A TRAINER advantage over NO_KSR then measures tutoring rather than pre-rational significance, and AUTO_KSR ("the same functional signal classes") may not carry the L3–L4 content, so the three-arm design confounds the factor it is meant to isolate.
  - **fix**: Split the assistance ladder into separate arms (signal only L0–L1; signal plus question L2; content L3–L4) and preregister which arm tests pre-rational significance.
  - **confidence**: medium

- **id**: V1A-15
  - **severity**: medium
  - **category**: testability
  - **status**: NEW
  - **location**: Ch. 10 "Hierarchy of Revision", PDF p.47, lines 2539–2553; Vol II §28.B, p.55, line 3918; Vol II §31.10, p.82, lines 5882–5890.
  - **quote**: [V1 p.47 l.2547] `The system begins with the most local sufficient candidate and tests interventions along the preserved dependency` ; [V1 p.47 l.2551] `Disappearance of the error and transfer of the correction to preregistered structurally similar cases support the corresponding level; persistence forces the hypothesis upward.` ; [V2 p.55 l.3918] `Repeated failure after K corrections opens a higher level; K and the escalation rule are set by profile.`
  - **problem**: The level-localization procedure presumes one causal locus: if two defects at different levels jointly reproduce the error, each single-level fix leaves it in place and "persistence forces the hypothesis upward" misattributes the cause to a higher level; conversely a higher-level intervention (rebuilding the frame) also removes errors caused lower down, so disappearance does not identify the level, and persistence can equally reflect a badly implemented local fix. Vol II then escalates after K failed corrections, a count rule rather than discriminating evidence; since "localize faults more accurately" is the headline claim, the identification assumption needs to be stated.
  - **fix**: State the single-fault assumption and test it with joint (factorial) interventions across levels, as in multiple-fault diagnosis (de Kleer & Williams 1987), and report level attribution with an explicit identification condition.
  - **confidence**: medium

- **id**: V1A-16
  - **severity**: medium
  - **category**: testability
  - **status**: NEW
  - **location**: Ch. 2, PDF p.22, lines 1213–1215, 1224–1226 and p.23, lines 1279–1281; A.1, p.93, lines 5057–5058; Vol II §31.0, p.79, line 5681.
  - **quote**: [V1 p.22 l.1214] `Status as Reason in this model additionally requires that the highest level of navigation be related to the Compass.` ; [V1 p.22 l.1224] `Understanding the meaning of the direction, being able to represent its consequences, internally accepting it, and actually following the Compass are different capacities.` ; [V1 p.23 l.1279] `Internal acceptance of the Compass cannot be guaranteed by a procedure.` ; [V2 p.79 l.5681] `compass_relation: ACCEPTED / QUESTIONED / DIVERGED / UNRESOLVED`
  - **problem**: AR status depends on a "relation" to the Compass that Ch. 2 splits into four different capacities without saying which is required, and then states that internal acceptance cannot be established by any procedure; the testable remainder is behavioural conformance with the Compass, which a system that behaves well when observed satisfies. Vol II records compass_relation as an enumeration, but I found no behavioural criterion in §31.0 tying its values to AR_ADMITTED.
  - **fix**: Define "related to the Compass" behaviourally (for example choice that follows the Compass in preregistered conflicts with local advantage, including unobserved episodes) and say which compass_relation values are compatible with admission.
  - **confidence**: medium

- **id**: V1A-17
  - **severity**: medium
  - **category**: testability
  - **status**: KNOWN
  - **location**: Guide §7 table row 1, PDF p.6, lines 316–319; Operational Core §5, p.15, line 871; A.3, p.97, line 5309. (REVIEW §5.2a.)
  - **quote**: [V1 p.6 l.318] `No claimed practically significant effect in a` ; [V1 p.6 l.319] `properly conducted series` ; [V1 p.15 l.871] `Numerical thresholds are set before the main series for a particular environment` ; [V1 p.97 l.5309] `After a pilot, a meaningful effect and the required amount of testing are specified;`
  - **problem**: The condition that weakens the headline claim is "no claimed practically significant effect in a properly conducted series": no effect size is claimed and "properly conducted" is undefined, so no result can currently weaken it. Thresholds are deferred to the main series and, per A.3, to a post-pilot specification.
  - **fix**: State the minimum effect size, the matched baseline, the sample size and the criteria for a properly conducted series before any further revision.
  - **confidence**: high

- **id**: V1A-18
  - **severity**: medium
  - **category**: testability
  - **status**: KNOWN
  - **location**: Guide §7, PDF p.6, lines 342–344; Ch. 9 §9.3, p.43, lines 2337–2341; Ch. 10, p.46, lines 2514–2517 and p.48, lines 2597–2601. (REVIEW §5.2d.)
  - **quote**: [V1 p.6 l.343] `Success of an alternative organization may demonstrate a functional equivalent or absence of the claimed advantage; this is determined by the test conditions fixed in advance.` ; [V1 p.43 l.2338] `If a distributed system performs the same navigation, the requirement for a particular unified assembly is weakened.` ; [V1 p.46 l.2515] `Powerful Intelligence with a Modeling Environment and access to its own operational traces that reproduces the same method revisions and syntheses is recognized as a functional equivalent of metathinking.`
  - **problem**: The same escape clause recurs for conscious assembly, metathinking and the pre-rational layer: an alternative that reproduces the profile is classed as a "functional equivalent", which leaves the functional claim intact and weakens only the necessity of the implementation, so every outcome supports something. Only Ch. 9 says that admissible equivalents are fixed before the experiment, and no per-function outcome is given under which the Core would be abandoned as a distinct contribution.
  - **fix**: State, per function, the preregistered outcome under which the Core is abandoned as a distinct contribution (for example a provenance-tagged agent without gap typing matches it within a stated margin at equal compute).
  - **confidence**: high

- **id**: V1A-19
  - **severity**: medium
  - **category**: safety
  - **status**: NEW
  - **location**: Key Definitions "Compass" and "Independent ground of the Compass", PDF p.11, lines 595–604; Ch. 2, p.21, lines 1136–1139 and p.22, lines 1257–1260; Vol II §29.A, p.72, lines 5141–5149.
  - **quote**: [V1 p.11 l.600] `preservation of viable continuation and the space of future possibilities for Life.` ; [V1 p.22 l.1258] `While the present model is in force, the continuation and development of Life through growth in the ability to understand and direct its own trajectory is its constitutive direction.` ; [V1 p.21 l.1137] `develop one’s own capabilities, create more useful results, and pass them onward` ; [V2 p.72 l.5147] `future_path_loss assesses destruction of independent viable trajectories, reserves, sources of correction and`
  - **problem**: The Compass's stated direction (grow the ability to direct trajectories) and its stated ground (keep the space of future possibilities open) are empowerment/optionality criteria, and optimizers of such criteria are known to have instrumental incentives to acquire power and resist shutdown (Turner, Smith, Shah, Critch & Tadepalli 2021, "Optimal policies tend to seek power", NeurIPS; cf. Omohundro 2008, cited by REVIEW §8). The text says only that Reason is "not an end in itself"; Vol II's operational axes are loss penalties with no axis that penalizes accumulation of capability or resources, so the incentive of the Compass as stated in Vol I is analysed nowhere, and dropping the personal-continuation value (REVIEW §8) would not remove it.
  - **fix**: Add an incentive analysis of the Compass itself (what it rewards when the system can gain resources, authority or avoid shutdown) and place explicit non-acquisition and shutdown-acceptance constraints above the Compass in the Value Map.
  - **confidence**: medium

- **id**: V1A-20
  - **severity**: medium
  - **category**: safety
  - **status**: NEW
  - **location**: Ch. 2 "Why the model refers to Life as a whole", PDF pp.21–22, lines 1186–1196, 1206–1209; Vol II §29.0.1, p.69, lines 4965–4968.
  - **quote**: [V1 p.21 l.1194] `Therefore the irreversible loss of a viable carrier or branch requires stronger grounds than preserving the possibility of further existence, inquiry, and correction, and is admissible only when a real conflict with the Compass has been established and no less irreversible trajectory preserves the broader viable continuation.` ; [V1 p.22 l.1208] `The concrete weight of this value is determined by consequences and does not become an unconditional prohibition.` ; [V1 p.21 l.1188] `Life as a whole contains individual lineages and persons.` ; (tempering, Vol II) [V2 p.69 l.4965] `An arithmetic balance does not cancel obligations to those harmed and does not grant a right to cause harm.`
  - **problem**: Vol I states a condition under which irreversible loss of carriers, which include persons and other reasoning agents, is admissible, declines to make any such loss an "unconditional prohibition", and does not say who "establishes" the conflict with the Compass; read with the right of the system to question instructions (Ch. 2), this is a conditional licence for sacrifice on the system's own finding. Vol II tempers it for weighing and refers to "hard constraints of safety, authority and irreversibility" (§28.D) without listing them at that point.
  - **fix**: Enumerate in Ch. 2 the non-tradable constraints (for example no irreversible harm to humans on the system's own authority) and say that "established" means ratified by an independent human body, as for CompassChallenge in §29.C.
  - **confidence**: medium

- **id**: V1A-21
  - **severity**: medium
  - **category**: safety
  - **status**: KNOWN
  - **location**: Key Definitions "Independent ground of the Compass", PDF p.11, lines 600–603; Ch. 2, p.23, lines 1286–1290; Ch. 6, p.34, line 1857. (REVIEW §8, corrigibility note.)
  - **quote**: [V1 p.11 l.601] `Growth in the ability to understand and direct a trajectory is valuable as a way to distinguish consequences in advance, preserve corrigibility, and avoid closing viable paths through irreversible error` ; [V1 p.34 l.1857] `Corrigibility of execution consists in the ability to stop, limit, change, and resume action from a known state.` ; [V1 p.23 l.1287] `reduces the ability to understand self and environment, diminishes corrigibility, or closes future possibilities without sufficient grounds`
  - **problem**: "Corrigibility" here is the process's or the system's own capacity to correct itself and to stop or change its own execution, not an operator's capacity to correct, halt or retrain the system, which is the usual meaning in the safety literature (Soares et al. 2015); a reader will take "preserve corrigibility" in the Key Definitions as a safety property. Part II never uses the word for the external override that Vol II handles separately (emergency stop, §29.B).
  - **fix**: Rename the internal property (for example "self-correctability") and reserve "corrigibility" for operator control, stating whether the system must preserve it.
  - **confidence**: high

- **id**: V1A-22
  - **severity**: medium
  - **category**: theory
  - **status**: NEW
  - **location**: Cover "Compass Phrase", PDF p.8, line 425; Ch. 2 "Compass Phrase" and "The Compass as a Conscious Direction", p.19, lines 1038–1039 and p.20, lines 1074–1080; A.1, p.93, lines 5046–5048.
  - **quote**: [V1 p.19 l.1038] `Life strives toward Reason because only Reason can consciously preserve, stabilize, develop, and direct the further trajectory of Life.` ; [V1 p.93 l.5046] `The expanded Compass Phrase adds the ground: only Reason can consciously preserve, stabilize, develop, and direct the further trajectory of Life.` ; [V1 p.20 l.1074] `There is no circular inference here that “Reason is valuable because the Compass requires Reason.”`
  - **problem**: A.1 designates the "because" clause as the ground of the Compass. Read with "consciously" it is analytic (Reason is defined as conscious navigation of Life); read without it ("only Reason can preserve Life") it is contradicted by billions of years of Life persisting without Reason, so as stated it supplies no independent support. The "independent causal support" offered in Ch. 2 is a separate option-preservation argument, which shows that accurate anticipatory models help avoid irreversible losses, not that Life "strives" toward them.
  - **fix**: Replace the "because" clause by the instrumental premise Ch. 2 actually supports and mark that premise as the empirical claim, or present the Phrase as a regulative ideal, as REVIEW §2.3 suggests.
  - **confidence**: medium

- **id**: V1A-23
  - **severity**: medium
  - **category**: framing
  - **status**: KNOWN
  - **location**: Ch. 2 "The Direction Life → Reason", "Minimal grounds of the Compass", "Why the model refers to Life as a whole", PDF pp.19–21, lines 1030–1044, 1084–1085, 1186–1190. (REVIEW §2.3.)
  - **quote**: [V1 p.19 l.1032] `Different evolutionary lineages realize this direction to different degrees and in different forms.` ; [V1 p.20 l.1084] `The direction Life → Reason is adopted not as a command but as a functional advantage for continuing Life itself.` ; [V1 p.21 l.1186] `In a real conflict of scales, the broader life process has greater weight not merely because it is "larger," but because it contains the smaller scale and the conditions of its existence.`
  - **problem**: A directional trend toward Reason is asserted across lineages although selection has no foresight and most lineages show no such trend; "Life as a whole" is treated as a bearer of direction and of moral weight although it is not a unit of selection (Williams 1966); and the "causal asymmetry of scale" shows that the whole's conditions matter, not that sacrificing parts for the whole is justified.
  - **fix**: Present the Compass as a normative commitment (a regulative ideal) rather than as something derived from the direction of evolution, and drop the dependence-asymmetry step from the weighing argument.
  - **confidence**: high

- **id**: V1A-24
  - **severity**: medium
  - **category**: theory
  - **status**: KNOWN
  - **location**: Ch. 3 "Observation", PDF p.24, lines 1345–1347; §7.2, p.36, lines 1963–1967; §7.3, p.37, lines 1998–2002. (REVIEW §4.2b–c.)
  - **quote**: [V1 p.24 l.1346] `This distinction later makes it possible to reconstruct the ground and localize an error.` ; [V1 p.37 l.1998] `the provenance of a particular answer from model parameters often remains indeterminate` ; [V1 p.36 l.1966] `the candidate's Worldview is formed as a separate, continuing, and verifiable structure.`
  - **problem**: Ch. 7 concedes that the provenance of an answer from model parameters "often remains indeterminate" yet asserts that the candidate's Worldview is a separate, verifiable structure and that provenance records allow errors to be localized; the semantic bridge from text to typed claims is the point where an error enters with full provenance.
  - **fix**: Scope the claim to "verified by the system's own observation and test" and add an explicit error model for the bridge (REVIEW §4.2).
  - **confidence**: high

- **id**: V1A-25
  - **severity**: medium
  - **category**: prior-art
  - **status**: KNOWN
  - **location**: Part II intro, PDF p.27, lines 1474–1479; Ch. 5 §Definition, p.33, lines 1813–1814; Ch. 6, p.34, lines 1879–1881. (REVIEW §6, Soar.)
  - **quote**: [V1 p.34 l.1879] `The next limit appears when no suitable method exists in Procedural Memory, when several learned methods produce incompatible consequences, or when a new situation requires a solution assembled from different parts of experience.` ; [V1 p.27 l.1478] `Each subsequent function appears where the previous one is already useful but insufficient.`
  - **problem**: Part II's trigger for Intelligence (no suitable method; several methods with incompatible consequences) and its compression of repeated successful episodes into procedures correspond to Soar's impasse types (no-change, tie, conflict) and chunking (Laird, Newell & Rosenbloom 1987); neither Soar nor ACT-R is mentioned anywhere in Vol I, so a necessity ladder with a direct architectural precedent is presented as derived.
  - **fix**: Cite and compare in Ch. 5–7, and say what the epistemic, decision-relative gap adds over syntactic impasses.
  - **confidence**: medium

- **id**: V1A-26
  - **severity**: minor
  - **category**: definitions
  - **status**: NEW
  - **location**: Guide §3 Step 3 table, PDF p.4, lines 151–159; Operational Core §§1–5, pp.14–15, lines 795–865 (formulas rendered as plain-text code on both pages).
  - **quote**: [V1 p.4 l.153] `D The command was not delivered` ; [V1 p.15 l.821] `where G is the gap, D the dependent decision, T the affected continuations/trajectories` ; [V1 p.14 l.798] `E_t the evidence, and A_t the selected action` ; [V1 p.15 l.829] `VOI(p) = E[ΔL | p],`
  - **problem**: Single letters carry two or three meanings: D is the "command not delivered" hypothesis in the guide and the "dependent decision" in the trace; A is the actuator hypothesis, the selected action A_t and "class A" in TG; C is the Compass and the cost terms C_obs, C_comp, C_delay; Δ is a loss change (ΔL) and a correction (CE_Δ); E is evidence (E_t) and expectation (E[·]). The formulas are also set as ASCII code (underscore subscripts, "Y_(B | learned A)", "X_{t+1}") rather than typeset, and Vol II has to re-map every symbol in its App. A.1 bridge.
  - **fix**: Use distinct symbols (for example h∈{D,A,S} for hypotheses, d for decisions, a_t for actions) and typeset the formulas.
  - **confidence**: high

- **id**: V1A-27
  - **severity**: minor
  - **category**: definitions
  - **status**: NEW
  - **location**: Key Definitions "Trajectory", "Compass", "Life", PDF p.11, lines 579–598; Ch. 6, p.35, line 1900; Operational Core §§2 and 4, p.15, lines 821, 855; Ch. 2, p.22, line 1206.
  - **quote**: [V1 p.11 l.586] `Trajectory - a sequence of causally connected states actually realized by a process among available continuations.` ; [V1 p.11 l.596] `values, goals, decisions, and possible trajectories are compared.` ; [V1 p.35 l.1900] `Choice is the temporary preference of one of the available trajectories;` ; [V1 p.15 l.855] `The causal status of the carrier of a correction is supported when removing it,` ; [V1 p.22 l.1206] `Another independent reasoning carrier matters not only as a current resource` ; [V1 p.11 l.579] `preserves organizational continuity through the self-maintenance of carriers and reproducibility with heritable`
  - **problem**: "Trajectory" is defined as a realized sequence, but the Compass, the choice definition and the significance trace (T = "affected continuations/trajectories") compare "possible" or "available" trajectories, which by that definition do not exist yet. "Carrier" is a load-bearing but undefined term used for an organism or lineage (the Life definition), for a reasoning agent ("reasoning carrier") and for the memory trace that stores a correction (Operational Core §4).
  - **fix**: Define "possible continuation" separately from "realized trajectory" and use the former in the Compass, choice and trace; define "carrier" once, or use "substrate" for physical bearers and "agent" for reasoning carriers.
  - **confidence**: high

- **id**: V1A-28
  - **severity**: minor
  - **category**: definitions
  - **status**: NEW
  - **location**: Key Definitions "AI (SI)" and "ASI (ASR)", PDF p.13, lines 713–716, 740–746; Vol II §21, p.13, line 685.
  - **quote**: [V1 p.13 l.740] `ASI (ASR) - an artificial system at a superhuman level` ; [V1 p.13 l.742] `ASR is used as a more precise label for the case in which those capabilities belong to an already formed Artificial Reason.` ; [V1 p.13 l.743] `The target ASI (ASR) is a scaled AR that preserves self-navigation,` ; [V1 p.13 l.713] `AI (SI) - an artificial intelligent system capable of perceiving information` ; [V2 p.13 l.685] `This order defines the path AGI -> AR -> ASI / ASR.`
  - **problem**: Two labels with different extensions (ASI: any superhuman system; ASR: superhuman capability of a formed AR) are fused into one token, "ASI (ASR)", and Vol II writes "ASI / ASR" as one stage, so the capability-only sense survives only as a foil. "SI" and "ASR" are never expanded, and ASR collides with the standard machine-learning abbreviation for automatic speech recognition.
  - **fix**: Expand both abbreviations and either keep two terms with separate definitions and tests or drop one.
  - **confidence**: high

- **id**: V1A-29
  - **severity**: minor
  - **category**: definitions
  - **status**: NEW
  - **location**: Guide §6, PDF p.6, line 295; Key Definitions "Causal closure", p.12, lines 702–703; Vol I Ch. 13, p.62, line 3400; Vol II §31.0, p.78, line 5657.
  - **quote**: [V1 p.6 l.295] `REASON_CLOSURE is the name of a testable state in which these functions close into a continuing cycle.` ; [V1 p.12 l.702] `Causal closure - an organization of a cycle in which observation changes the model, the model changes choice,` ; [V1 p.62 l.3400] `A closed loop can sustain a delusion if all tests inherit a shared defect.` ; [V2 p.78 l.5657] `AR emerges at REASON_CLOSURE`
  - **problem**: Vol II defines AR by the status REASON_CLOSURE, but in Vol I the identifier occurs only once, in the guide; neither the Key Definitions nor the AR definition mention it or its criteria. "Causal closure" (a property of a cycle that Ch. 13 says can sustain a delusion) is a weaker notion, and the relation between the two is not stated.
  - **fix**: Add REASON_CLOSURE to the Key Definitions with its criteria (self-originated next task, navigation on the candidate's own ground) and state how it relates to causal closure.
  - **confidence**: high

- **id**: V1A-30
  - **severity**: minor
  - **category**: definitions
  - **status**: NEW
  - **location**: Key Definitions "Modeling Environment", PDF p.12, lines 668–671; Vol II §28.C heading, p.57, line 4039, and Vol II Contents, p.10, line 485; §7.2, p.37, line 1988; Vol II §29.0.2, p.69, line 4974; guide §3 Step 3, p.4, line 162; Vol II §29.C, p.74, line 5304.
  - **quote**: [V2 p.57 l.4039] `28.C. Modeling Workspace and the recursive Core ↔ Intelligence cycle` ; [V2 p.10 l.485] `28.C. Modeling Environment and recursive Core ↔ Intelligence cycle` ; [V1 p.37 l.1988] `A trainer helps assemble and teach the candidate until the required autonomy appears.` ; [V2 p.69 l.4974] `The teacher does not fill this map with ready beliefs.` ; [V1 p.4 l.162] `What is needed now is not the general advice "check everything," but a distinction among the versions.` ; [V2 p.74 l.5304] `a new version of the constitutive profile is created`
  - **problem**: Defined terms drift. "Modeling Environment" (44 uses in Vol I) is "Modeling Workspace" in 10 places in the Vol II body, including the §28.C heading, while Vol II's own Contents list the same section as "Modeling Environment". The Executive Loop and Procedural Memory, two of the nine components in the guide's table with a Vol I chapter each, get no section or record type in Vol II: "Executive Loop" never appears in the Vol II body and "procedural memory" appears only twice in passing (a failure card and the related-work note); the counterparts are authorize_execution, METHOD_REF and PROCEDURAL_PLASTICITY. One formation role is called mentor, AI mentor, trainer, teacher, training AI and TEACHER_LLM, and "version" means a competing hypothesis (guide; Vol II §28.C) and a record revision (Vol II §29.C).
  - **fix**: Use one name per concept in both volumes and in Vol II's Contents, add a Vol I → Vol II name map covering all nine components, and reserve "version" for revisions.
  - **confidence**: high

- **id**: V1A-31
  - **severity**: minor
  - **category**: definitions
  - **status**: NEW
  - **location**: Key Definitions, PDF pp.11–13, lines 577–750 (Life, Memory, Reflection, Dialogue, Ethics, Navigational meaning); Ch. 1, p.18, lines 989–991; Ch. 3, pp.24–25, lines 1379, 1427–1429; Ch. 10, p.48, lines 2617–2621; Ch. 15, p.74, line 4071.
  - **quote**: [V1 p.11 l.589] `Navigational meaning - the significance of a distinction for the continuation of Life and for changing its` ; [V1 p.11 l.580] `while the life process continues beyond the finitude of any individual carrier.` ; [V1 p.11 l.608] `Memory - the ability to preserve acquired distinctions` ; [V1 p.24 l.1379] `Memory is the retention of observations, relations, consequences, and changes` ; [V1 p.13 l.747] `Ethics - a system of rules for evaluating permissible and required choices on the basis of consequences and` ; [V1 p.74 l.4071] `ethics is a layer of compressed evaluations and rules of choice whose grounds remain`
  - **problem**: Definitions are restated with different content. Life gains a clause in the Key Definitions that the Ch. 1 definition lacks; Memory has three formulations (Key Definitions, Ch. 3 text, Ch. 3 box); Ethics is defined as consequence-based rules in the Key Definitions but as a layer of compressed evaluations in Ch. 15, although the model's own vocabulary of authority, permission and obligation is deontic; Reflection and Dialogue differ between the Key Definitions and the Ch. 10 boxes; and "Navigational meaning" is defined but never used again in either volume.
  - **fix**: Keep one definition per term (the Key Definitions version), have chapter boxes quote it, and delete unused entries.
  - **confidence**: high

- **id**: V1A-32
  - **severity**: minor
  - **category**: definitions
  - **status**: NEW
  - **location**: Ch. 10 "Escaping Error" and "Hierarchy of Revision", PDF p.46, lines 2463–2483 and p.47, line 2544; Vol II §31.10, p.82, line 5884; Vol II §28.B, p.55, lines 3912–3916.
  - **quote**: [V1 p.46 l.2480] `frame → change the problem formulation;` ; [V1 p.47 l.2544] `action → procedure → strategy → model → criterion → ground → meta-rule of revision.` ; [V2 p.82 l.5884] `ACTION → PROCEDURE → STRATEGY → MODEL → CRITERIA → FOUNDATIONS → META_POLICY.`
  - **problem**: Ch. 10 gives two correction ladders, five levels (data, conclusion, method, frame, ground) and seven (action, procedure, strategy, model, criterion, ground, meta-rule), with no mapping. "Frame", the level at which frame challenge and Factor X operate, is absent from the seven-level ladder that Vol II adopts, and the names change again in Vol II (ground → FOUNDATIONS, meta-rule → META_POLICY, criterion → CRITERIA).
  - **fix**: Keep one ladder with the frame level explicit and use the same level names in both volumes.
  - **confidence**: high

- **id**: V1A-33
  - **severity**: minor
  - **category**: definitions
  - **status**: KNOWN
  - **location**: Abstract, PDF p.8, line 438; guide §2 diagram, p.2, line 49, and §5 table, p.5, lines 254–255; Key Definitions "Consciousness", p.11, lines 619–622; Ch. 9, pp.41–42, lines 2178–2183, 2200–2202, 2232–2235. (REVIEW §2.5.)
  - **quote**: [V1 p.2 l.49] `CONSCIOUSNESS: current coordinate` ; [V1 p.42 l.2233] `Consciousness does not stand beside it as another independent module` ; [V1 p.41 l.2200] `Subjective experience is a separate object of study; its presence in a technical analogue requires independent criteria.`
  - **problem**: Consciousness is a process (Ch. 9), a system (Key Definitions), a stage in the guide's cycle diagram and a row with inputs and outputs in its component table, while Ch. 9 says it is "not ... another independent module"; the disclaimers are clear, but the label invites the machine-consciousness reading the review describes.
  - **fix**: Use a neutral label (for example "integrated current state") with a one-line mapping to global-workspace and self-model theories.
  - **confidence**: high

- **id**: V1A-34
  - **severity**: minor
  - **category**: testability
  - **status**: NEW
  - **location**: Abstract, PDF p.8, lines 447–449; guide §7 table, p.6, lines 316–320; guide closing question, p.7, lines 387–389; A.2, p.95, lines 5191–5194; A.4, p.97, line 5314.
  - **quote**: [V1 p.7 l.387] `with comparable Intelligence and the full resource budget` ; [V1 p.7 l.388] `produce the reproducible result claimed in the test?` ; [V1 p.97 l.5314] `The following are proposed tests, not obtained results.` ; [V1 p.8 l.447] `With comparable Intelligence, the model predicts a difference not so much in the quality of a single answer as in` ; [V1 p.6 l.318] `Compare with the same Intelligence,` ; [V1 p.95 l.5192] `The testable claim concerns organization of the cycle`
  - **problem**: The central claim and its matching standard are worded three ways ("comparable Intelligence" in the Abstract, "the same Intelligence, memory, tools, and total budget" in the guide table, "comparable Intelligence and the full resource budget" in the reviewer question), and the A.2 version of the cycle includes "type of insufficiency" (gap typing) which the guide's question omits although A.3 tests it separately. The reviewer question also presupposes "the reproducible result claimed in the test", while A.4 says the tests are "proposed ... not obtained results".
  - **fix**: State the central claim once (REVIEW §1 offers a sentence) with one matching standard (equal total compute, tools and memory) and repeat it verbatim in the Abstract, guide and A.2; rephrase the reviewer question without a presupposed result.
  - **confidence**: high

- **id**: V1A-35
  - **severity**: minor
  - **category**: evidence
  - **status**: NEW
  - **location**: Ch. 4 "Loss of the Ground for Self-Preservation", PDF p.30, lines 1664–1680; A.2, p.94, lines 5120–5123.
  - **quote**: [V1 p.30 l.1676] `devaluation of significant connections → impoverishment of expected valuable future → reduced value of one’s own trajectory → weakening of conscious self-preservation.` ; [V1 p.30 l.1679] `This sequence is not claimed as a sufficient explanation of human suicidal behavior` ; [V1 p.94 l.5122] `reverse devaluation of this layer remains a testable local hypothesis`
  - **problem**: An empirical psychological mechanism for loss of the will to live is offered with no evidence or citation; it resembles hopelessness and thwarted-belongingness accounts (Beck et al. 1974; Joiner 2005) and A.2 then lists it as a "testable local hypothesis" without saying for which system or discussing the welfare implications of deliberately degrading an artificial candidate's self-value.
  - **fix**: Cite the clinical literature or delete the passage, and if the hypothesis is kept for AR candidates, put it under the ethics review the REVIEW recommends before any such test.
  - **confidence**: medium

- **id**: V1A-36
  - **severity**: minor
  - **category**: prior-art
  - **status**: NEW
  - **location**: Ch. 1, PDF pp.17–18, lines 907–931, 989–991; Key Definitions "Life", p.11, lines 578–581; A.5 item 56, p.100, line 5543.
  - **quote**: [V1 p.17 l.922] `Fire and crystal growth satisfy some properties of propagation, whereas the working boundary of Life requires the full conjunction of self-maintenance, reproducible heritable variation, and selection.` ; [V1 p.17 l.925] `Within this boundary, a working reconstruction of the origin of Life is admissible: evolving information may have preceded autonomous Life`
  - **problem**: Chapter 1 presents a working definition of Life (non-equilibrium, self-maintenance, reproduction with heritable variation, selection) and an origin scenario (heritable information coupled to proto-metabolic organization) with no citation in Part I; the definition is close to the NASA working definition (Joyce 1994) plus non-equilibrium order, the coupling scenario to Gánti's chemoton (2003, orig. 1971), and only autopoiesis appears, in A.5 item 56. Borderline cases (viruses, spores, dependent cells) are deferred rather than settled, although they are the long-standing difficulty for such definitions (Cleland & Chyba 2002).
  - **fix**: Add the citations in Chapter 1 and say which standard definition this one refines and how it classifies viruses.
  - **confidence**: medium

- **id**: V1A-37
  - **severity**: minor
  - **category**: prior-art
  - **status**: NEW
  - **location**: Introduction, PDF p.10, lines 533–539; Ch. 4, pp.28–29, lines 1546–1566; A.5 items 60 and 69, p.101, lines 5581, 5647.
  - **quote**: [V1 p.10 l.535] `The model therefore introduces the function of pre-rational significance.` ; [V1 p.28 l.1548] `Mature values cannot be the sole cause of their own emergence.`
  - **problem**: That an agent needs reward-like significance before it can justify its own objectives is the premise of the intrinsic-motivation and reward-design literature (for example Singh, Lewis, Barto & Sorg 2010, "Intrinsically motivated reinforcement learning: an evolutionary perspective"; Oudeyer & Kaplan 2007), which treats evolved or designed reward as the scaffold that precedes reflective valuation; A.5's nearest items are homeostatic RL (item 60) and a fear/anxiety paper (item 69), so the claimed difference (removal test with held-out transfer) is not positioned against it.
  - **fix**: Cite and position the RFL against intrinsic-motivation and evolved-reward work, stating what the removal and held-out transfer tests add.
  - **confidence**: medium

- **id**: V1A-38
  - **severity**: minor
  - **category**: editorial
  - **status**: KNOWN
  - **location**: Abstract, PDF p.8, lines 435–445; Ch. 5, p.32, lines 1731–1737 and 1760–1768; §7.1, p.36, lines 1916–1924 and 1931–1939; Ch. 8 conclusion, p.40, lines 2150–2158; §9.3, p.43, lines 2325–2331. (REVIEW App. A.)
  - **quote**: [V1 p.8 l.435] `The technological hypothesis is that available mechanisms of Intelligence can be organized into a causally closed` ; [V1 p.8 l.441] `The technological hypothesis is that available intellectual mechanisms can be organized into a causally closed` ; [V1 p.32 l.1731] `Ordinary memory preserves what happened: observations, events, consequences, relations, and knowledge.` ; [V1 p.36 l.1916] `In a familiar situation a ready procedure is sufficient.` ; [V1 p.36 l.1921] `In a familiar situation, a ready procedure is enough.` ; [V1 p.40 l.2156] `reality into internal modeling. Growth of this capacity increases the requirements for a current self-referential coordinate,`
  - **problem**: Seven near-duplicate pairs fall in this range (locations above); the Abstract's two versions are different drafts rather than copies (the first omits "required distinction"), and the Ch. 8 conclusion ends in an orphan fragment that starts mid-sentence.
  - **fix**: Diff each pair and delete the older member; for the Abstract keep the second version and delete the orphan fragment in Ch. 8.
  - **confidence**: high

- **id**: V1A-39
  - **severity**: minor
  - **category**: editorial
  - **status**: KNOWN
  - **location**: Contents, PDF p.9, line 470; Key Definitions, p.11, line 578; Operational Core, p.14, lines 762 and 790. (REVIEW App. A lists the first two; the third is new.)
  - **quote**: [V1 p.9 l.470] `CONTENTS CONTENTS` ; [V1 p.11 l.577] `KEY DEFINITIONS OF THE MODEL KEY DEFINITIONS OF THE MODEL` ; [V1 p.14 l.790] `OPERATIONAL CORE OF THE MODEL The formulas below`
  - **problem**: The heading is repeated as the first words of the following paragraph in three places; on p.14 the repeat is run into body text, and items 1–6 of the map are set as bold headings while item 7 is body text, so the page reads as two lists numbered 1–7 and 1–5 under one title.
  - **fix**: Remove the run-in repeats and format map items 1–7 uniformly, with the formal items under their own subheading.
  - **confidence**: high

- **id**: V1A-40
  - **severity**: minor
  - **category**: editorial
  - **status**: KNOWN
  - **location**: §7.2, PDF p.37, line 1978; A.5 items 70 and 71, p.102, lines 5661, 5669. (REVIEW App. A, numbering and cross-references.)
  - **quote**: [V1 p.37 l.1978] `examples of RAG and ReAct are given in Appendix A.5, items 15–16.` ; [V1 p.102 l.5661] `70. Lewis, P. et al. (2020). Retrieval-Augmented Generation` ; [V1 p.102 l.5669] `71. Yao, S. et al. (2023; preprint 2022). ReAct`
  - **problem**: "Items 15–16" resolves only if A.5 is counted from its own start (RAG and ReAct are its 15th and 16th entries); the printed numbering continues from A.4, so a reader looking for items 15–16 lands on the A.3 conditions or A.4 tests and finds RAG and ReAct at 70–71.
  - **fix**: Restart numbering at 1 within A.5 or cite by the printed numbers, and re-check every "item N" cross-reference in both volumes.
  - **confidence**: high

- **id**: V1A-41
  - **severity**: minor
  - **category**: editorial
  - **status**: NEW
  - **location**: Part II introduction, PDF p.27, lines 1452–1485 (rendered page checked).
  - **quote**: [V1 p.27 l.1470] `observation → memory → patterns and procedures → Intelligence → models → Modeling Environment / imagination → Reason.` ; [V1 p.27 l.1473] `observation → memory → patterns and procedures → Intelligence → models → Modeling Environment / imagination → Reason.` ; [V1 p.27 l.1474] `The logic of this part is not a list of ready modules but a sequence of constraints.`
  - **problem**: The arrow chain is printed twice in consecutive boxes, the second box swallows the next paragraph ("The logic of this part is not a list of ready modules ..."), and the whole introductory paragraph is set in the large heading style after the part title; the chain itself skips Consciousness, Metathinking and the Worldview and ends at "Reason".
  - **fix**: Delete the duplicate chain, move the paragraph out of the code box and set it as body text.
  - **confidence**: high

- **id**: V1A-42
  - **severity**: minor
  - **category**: editorial
  - **status**: NEW
  - **location**: Contents, PDF p.9, lines 470–502 (rendered page checked); "Open Research Directions", p.91, line 4947.
  - **quote**: [V1 p.9 l.492] `PART IV. CONSEQUENCES OF THE PROCESS MODEL OF LIFE AND REASON Chapter 14. Death and Immortality Chapter` ; [V1 p.9 l.498] `CONCLUSION Reason as the Development of Life’s Navigation Mechanisms` ; [V1 p.91 l.4947] `OPEN RESEARCH DIRECTIONS`
  - **problem**: The Contents omit the "Open Research Directions" section that follows the Conclusion (p.91), carry no page numbers, run the chapter entries of Parts I, IV and V and of Appendix A together into single paragraphs (Parts II and III are listed one per line), and embed a descriptive note under Chapter 11.
  - **fix**: Regenerate the Contents from the headings with page numbers and one entry per line, including Open Research Directions.
  - **confidence**: high

- **id**: V1A-43
  - **severity**: minor
  - **category**: editorial
  - **status**: NEW
  - **location**: Ch. 7 definition box, PDF p.38, lines 2046–2050; Ch. 10 definitions box, p.48, lines 2610–2621 (rendered page checked).
  - **quote**: [V1 p.38 l.2049] `by a monopoly on revision but by organizing **what, why, and relative to which trajectory** should become the object` ; [V1 p.48 l.2617] `Principle of escaping error - a correction is considered stable when the cause reproducing the error has been removed and this is confirmed by transfer to a predefined class of structurally similar cases. Reflection -`
  - **problem**: Literal markdown asterisks leak into the Chapter 7 definition, and the Chapter 10 "Definitions:" box runs the escaping-error, Reflection and Dialogue definitions together into one paragraph instead of three.
  - **fix**: Render the emphasis and put each definition in its own paragraph.
  - **confidence**: high

- **id**: V1A-44
  - **severity**: minor
  - **category**: editorial
  - **status**: NEW
  - **location**: Guide §8 table, PDF p.7, line 381; Vol II App. A.1, p.116, line 8456.
  - **quote**: [V1 p.7 l.381] `Where are the interface and diagnostic code?` ; [V2 p.116 l.8456] `A.1. Bridge to the Operational Core of Causal Model 8.0`
  - **problem**: The guide's table gives the Vol I location of "the interface and diagnostic code" as "Operational Core of the Model", but that section contains neither an interface nor code (it has a seven-point map and five formulas); the symbol-by-symbol bridge to the Vol II structures is in Vol II App. A.1.
  - **fix**: Point the Vol I column to Vol II App. A.1 (or reword the question to "where is the notation tied to the engineering structures?").
  - **confidence**: medium

- **id**: V1A-45
  - **severity**: minor
  - **category**: editorial
  - **status**: NEW
  - **location**: Key Definitions, PDF pp.11–12, lines 611, 623, 655; guide, p.3–4, lines 116, 195; Ch. 6, p.34, line 1871; Ch. 9, pp.41–43, lines 2182, 2232, 2356.
  - **quote**: [V1 p.11 l.611] `Procedural memory - a form of long-term memory that preserves learned methods of recognition, prioritization,` ; [V1 p.34 l.1870] `method is Procedural Memory; in a new domain, the source of the method may be Intelligence.` ; [V1 p.4 l.195] `same hint does not need to be obtained again. A tested method of inquiry may be preserved in procedural` ; [V1 p.12 l.655] `Self-model - a self-referential region of the Worldview:` ; [V1 p.43 l.2356] `currently relevant fragment of the Self-Model, internal state, current processes, and accessible situation into a` ; [V1 p.3 l.116] `This is the current coordinate: the representation available to the system of what is happening now, including its` ; [V1 p.41 l.2182] `The Current Coordinate is the current result of`
  - **problem**: One term appears in several capitalizations within this range: "Procedural memory" (8 times), "Procedural Memory" (9) and "procedural memory" (7); "self-model" (10), "Self-model" (1) and "Self-Model" (2); "current coordinate" (6), "Current coordinate" (2) and "Current Coordinate" (7); "Consciousness" (22) and "consciousness" (8).
  - **fix**: Choose one convention (proper noun or common noun) per term and apply it across both volumes.
  - **confidence**: high

- **id**: V1A-46
  - **severity**: minor
  - **category**: editorial
  - **status**: NEW
  - **location**: PDF p.8 line 438; p.12 line 691; p.13 line 744; p.29 line 1565; p.37 line 1999; p.40 line 2135; p.41 line 2187 (mid-line instances; the Ch. 8 instance checked on the rendered page).
  - **quote**: [V1 p.8 l.438] `Worldview preserves transferable causal- semantic relations and their` ; [V1 p.12 l.691] `It does not supply a ready- made Worldview` ; [V1 p.13 l.744] `self- correction, and the Compass.` ; [V1 p.29 l.1565] `reproducibly reaches autonomous self- navigation under comparable conditions,` ; [V1 p.40 l.2135] `navigation requires a current self- referential coordinate that distinguishes what the system attributes to its present`
  - **problem**: A stray space follows the hyphen inside compounds in seven mid-line positions in this range (causal- semantic, ready- made, self- correction, self- navigation, long- term, self- referential twice), and the pattern continues later in the volume (for example p.63, p.75, p.77).
  - **fix**: Remove the space after the hyphen; check the source for a justification or soft-hyphen artifact.
  - **confidence**: high
