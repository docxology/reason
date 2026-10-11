# Review: *Foundations of Reason 8.0* and *Engineering of Reason 3.5* (M. Tkalic)

**Documents reviewed**

- Mihail Tkalic, *Superintelligence Technology (ASI): Foundations of Reason 8.0. From the Meaning of Life to Artificial Reason*, Vol. I. Zenodo, 2026. [10.5281/zenodo.23271702](https://doi.org/10.5281/zenodo.23271702)
- Mihail Tkalic, *Engineering of Reason 3.5: ASI Technology*, Vol. II. Zenodo, 2026. [10.5281/zenodo.23271781](https://doi.org/10.5281/zenodo.23271781)

These are the Zenodo titles. The PDF title pages differ: Volume I's reads *Foundations of Reason. Volume I. The Causal Model of Reason*, with no mention of ASI, and Volume II's ends "Technology for Creating Artificial Reason and Scaling to ASI (ASR)" (Vol. II p. 9; [MIN-09](docs/audit/MIN-09-inconsistent-titles.md)).

**Scope of this review.** I read both English editions in full (105 and 118 pages), including the shared 15-minute guide. I then audited both volumes section by section, checked every reference in their bibliographies and in this review, had the review's factual claims checked by a second model from a different vendor, and had a separate pass argue the author's side against each criticism. I also pulled the publication history from the Zenodo API, and restored and ran both Python listings in Volume II. Appendix B lists what was verified and how. Every issue raised here, and many smaller ones the audit found, is tracked individually in [`docs/audit/`](docs/audit/README.md) and listed in Appendix C. Section numbers follow the author's continuous numbering (Chapters 1–20 in Volume I, 21–34 in Volume II). Quotations from the volumes are cited by volume, section and PDF page, and each section that assesses the work opens with the claims it responds to.

---

## The short answer

The two volumes are a carefully hedged design philosophy for a self-directed inquiry agent built around a language model. That design sits inside a broader process philosophy of life, and it comes with an evaluation protocol that is more rigorous than most published work on cognitive architectures or LLM agents. They are not yet a scientific theory in the strong sense, and nothing in them is yet evidence that the architecture works. The author says as much in Volume I, Appendix A.2.1, and I want to credit that candour before anything else.

The central idea is sound and worth testing. A capable system can produce excellent answers to the questions it is given and still be poor at deciding which question matters, which distinction a decision actually depends on, when the available ground is sufficient, and how to make a correction stick across episodes. Treating that second capacity as a distinct, measurable object is the most valuable move in the series.

The main problems are of a different kind than the earlier reviewers' frustration suggests. First, the framing promises far more than the content delivers: superintelligence and the meaning of life on the cover, a modest and testable hypothesis about inquiry bookkeeping inside. Second, the decisive empirical step has not been taken; the only pilot was a benchmark-construction exercise. Third, the comparison with prior work was done after the theory was formed and sits in an appendix, and the closest precedents are missing from the chapters. Fourth, the safety design contains strong containment but no analysis of the incentives its own value structure creates. Fifth, the prose itself is the main barrier to review. The difficulty those local researchers had is better explained by the text than by the readers.

My overall verdict: a pre-empirical research programme with a strong evaluation plan, embedded in a speculative natural philosophy. It deserves experimental development in a narrowed form, and §10 collects ideas for it. Chief among them are a preregistered experiment comparing the Core against a strong agent stack at equal compute, with a stated effect size and a stated condition under which the Core is abandoned as a distinct contribution, and a pause in revising the text until such an experiment has run.

| Your question | My short answer |
|---|---|
| Is the causal model coherent? | Yes at the functional level. Its necessity claims are close to analytic, its distinctive claims are untested design hypotheses, and the philosophical derivation constrains no engineering choice. |
| Is the Intelligence/Reason distinction meaningful and useful? | Yes. Stated narrowly (generating solutions vs. regulating inquiry, persistently across episodes), it is the most useful idea in the series. It has deep precedent and is currently overloaded with normative content. |
| Is the architecture a plausible path from current AI to Artificial Reason? | Plausible toward self-correcting inquiry agents. Underspecified at the formation step (internalization, transfer, "own" values), and the formation experiment cannot yet attribute a result to the formation loop. No path to ASI is given. |
| Does Volume II make the theory testable? | It supplies an unusually rigorous evaluation design but is not yet test-ready, and the claim it can actually test is much narrower than the titles. |
| How does it relate to existing architectures? | It is integrative. Every component has a close precedent, and several of the closest (Soar, goal-driven autonomy, truth maintenance, decision-region active learning, the Robot Scientist, active inference in depth) are not engaged. |
| Which parts are strongest, weakest, novel, or in need of development? | Strongest: the operational criterion of a correction, the epistemic-status layer, and the evaluation methodology. Weakest: the framing, the absence of evidence, literature integrated after the fact, and an unanalysed safety incentive. Novel as a package rather than in its parts. Most in need of development: a mechanism for transfer, a mechanism for internalization, and a committed decision rule for the Core. |
| What scientific status does it deserve? | A pre-empirical research programme: falsifiable at the engineering level, untested, and worth testing experimentally before any further theory. |

---

## 1. What I take the work to claim

Since earlier reviewers could not reconstruct the architecture, here is my reconstruction, so the author can check that the rest of this review rests on an accurate reading.

A situation arrives: a command was sent, and the sensor reading did not change. The system maintains a self-referential integration of its current state, which the author calls Consciousness; its output is the Current Coordinate. That state keeps "the reading did not change" separate from "the equipment did not switch on" (shared guide, Vol. I p. 3). The Core of Reason then asks what the next decision rests on, for example "the command was delivered" or "the sensor is functioning" (guide, p. 2), and what is missing from that ground. It converts the insufficiency into a *required distinction*: a feature on which the live hypotheses disagree and on which the decision depends. In practice, Intelligence is a language model plus tools; it proposes hypotheses and tests, which a Modeling Environment holds side by side. The Core selects a test by discriminating power, cost, delay and irreversibility. It judges when the ground is sufficient for the next step, not for complete knowledge. It then commits a revision to the Worldview, a versioned, provenance-tracked model of the world and of the system itself. A correction counts only if it changes later behaviour and transfers to cases whose structural similarity was fixed before testing, while being rejected on look-alike cases with different structure.

Values live in a Value Map whose top level is the Compass: "continuation and development of Life through growth in the ability to understand and direct its own trajectory" (Vol. I Key Definitions, p. 11). During development, a Reason Formation Loop (RFL) supplies Formation States, which are functional analogues of fear, curiosity, "something does not fit" and "I am stuck." The external loop must become causally unnecessary once the system navigates on its own (its functions may be dropped, internalized or taken over by another mechanism); the test is removal of the RFL followed by held-out evaluation. External authority, an emergency stop and audit are kept separate from all of this. REASON_CLOSURE is the state in which the next significant task reliably originates from the system's own state, open commitments, gaps and values rather than from an external command; admission as Artificial Reason (AR) additionally requires a relation to the Compass and external review.

Volume I distinguishes four kinds of statement (A.2): definitions, philosophical foundations, conditional functional inferences, and empirical hypotheses. I follow that distinction throughout, because each kind needs a different kind of review.

Compressed to one testable sentence, the scientific core of both volumes is this:

> With the same language model, tools, memory and total compute, an agent that explicitly represents which ground a decision rests on, what is missing from that ground, which distinction would change the decision, and which inquiry method resolved that kind of gap, will localize faults more accurately and cheaply, stop less often on insufficient grounds, carry corrections into later episodes, and transfer inquiry methods to structurally similar problems while rejecting false analogies, compared with a strong agent stack that lacks this organization.

Everything else in the series is either philosophy that motivates this hypothesis, engineering that implements it, or extrapolation beyond it. The author's own statements support this reading. Volume I says, "Individual components — memory, planning, reflection, world models, and self-modification — are already known; the testable claim concerns their causal organization" (Vol. I front matter, p. 9). Chapter 12 states the testable hypothesis as "explicit linking of gap type, expected outcomes of a test, and dependent corrections improves transfer of the investigative method under comparable resources" (Vol. I §12.9, p. 61), and Volume II's front matter states its "Central working hypothesis: inquiry by formed Reason is governed by a significant insufficiency of a ground for understanding, evaluation, or action" (Vol. II front matter, p. 12).

---

## 2. Is the causal model coherent?

### 2.1 The functional cycle holds together

> **Claims under review**
>
> - "These formalisms are not claimed as original. The contribution of the present model concerns their place within the larger cycle of significant gap, discriminating inquiry, revision of grounds, and transfer of correction." (Vol. I Operational Core, p. 15)
> - "One mechanism may both construct alternatives and participate in selecting the next question" (Vol. I §7.3, p. 37).

At the functional level, yes. The cycle (situation → significant gap → required distinction → test → evidence → revised ground → choice → consequences) is well formed. The definitions are used consistently across more than two hundred pages, which is not easy at this length. The Operational Core of Volume I gives a compact formal vocabulary: value of information net of observation, computation, delay and irreversibility costs; interventional effects of a retained correction; transfer and regression terms. The author correctly declines to claim these formalisms as original. The decomposition is by causal role rather than by module, so one mechanism may implement several roles and an alternative architecture counts if it shows the same profile under intervention. That is the right choice for a theory meant to cover organisms, organizations and machines.

### 2.2 The necessities are close to analytic; the substance is in untested hypotheses

> **Claims under review**
>
> - "If an acquired distinction must change the future after the signal disappears, a persistent trace is required." (Vol. I §13.2, p. 63)
> - "Stronger requirements — a common conscious picture, explicit typing of gaps, detailed provenance of knowledge, and a particular organization of the Core — remain hypotheses about implementation and its advantages." (Vol. I §13.2, p. 63)

Section 13.2 lists the model's conditional necessities, and the author classifies them as such (A.2); the first claim above is one example. These are true, but nearly true by definition. A system that learns must store something, and a system that acts differently in different states must be able to tell them apart. Conant and Ashby's good-regulator theorem and Ashby's law of requisite variety cover much of this ground.

The author acknowledges where the distinctive content lies, in the second claim above. So the model has two tiers: necessities that cannot be wrong and say little, and hypotheses that say a lot and are untested. The two necessities offered as substantive overreach: an "earlier loop" is said to be required for any capability that must arise through experience, and the Principle of Pre-rational Significance has a refutation arm whose refuting case cannot occur, because its realizer class includes "properties of the learning environment" (Vol. I Ch. 4, p. 28; [MED-01](docs/audit/MED-01-near-analytic-necessities.md)).

That makes "causal model" an overstatement. In the sense used in causal inference, a causal model specifies variables and mechanisms precisely enough to predict the effect of interventions, including magnitudes. What the volumes provide is a functional decomposition with design requirements, plus a list of interventions whose predicted direction (loss of function under ablation) is stated but whose magnitudes are not. That is a legitimate and useful kind of theory, and naming it accurately, for example as a functional model, would serve it better.

### 2.3 The philosophical layer does not carry weight in the engineering

> **Claims under review**
>
> - "Life strives toward Reason because only Reason can consciously preserve, stabilize, develop, and direct the further trajectory of Life." (Vol. I Ch. 2, p. 19)
> - "Its causal role is tested in conflicts with local advantage and under changing conditions." (shared guide, Vol. I p. 5)

The Compass's content does shape the value and action layers: a coverage frame for the Worldview, a separate "semantic Compass gap" type (§28.0), the `CompassAssessment` vector with its epistemic gate (§29.A), and `CompassChallenge` (§29.C). The text also claims a causal role for it and proposes to test that role in conflicts with local advantage (second claim above). What I could not find is an engineering choice that depends on the derivation, and the author concedes that "changing the limiting criterion while preserving cognitive functions does not destroy self-correction" (Vol. I A.3, p. 96). The inquiry core would work with any top-level value system. The operational Compass is a vector of assessments of a decision (risk to the continuity of life processes, reliance on unconfirmed premises, loss of viable future paths, effects on other autonomies, reversibility): a precautionary, option-preserving multi-criteria evaluation that one can adopt without accepting that "Life strives toward Reason" (Vol. I Ch. 2, p. 19). The texts also state two top-level criteria that can conflict, growth in the ability to direct a trajectory and preservation of the space of future possibilities, and give three different operational decompositions with no mapping ([MED-21](docs/audit/MED-21-compass-two-criteria-grounding.md), [MED-27](docs/audit/MED-27-compass-decompositions.md)).

Taken as philosophy, the derivation in Chapter 2 has the familiar weaknesses. That living processes continue does not establish that they ought to, or that growth in understanding is their meaning. The is-ought gap is not closed by calling the meaning "minimal". Directionality in evolution toward intelligence is contested; Gould and Conway Morris represent the poles, and most lineages show no such trend. The "causal asymmetry of scale" argument (Vol. I Ch. 2, p. 21) for weighting the broader life process is a holistic ethic, close to Leopold's land ethic, and it inherits the known problems of aggregation across individuals.

The author already concedes that the model "does not claim a neutral standpoint outside all values" (Vol. I Ch. 2, p. 23). One option is to drop the language of derivation entirely and present the Compass as what Kant called a *regulative idea*: a principle that orients inquiry and choice without being an object of knowledge, defended by its coherence and by what it does for the system that adopts it. That removes the is-ought objection outright and fits the role the Compass actually plays in the architecture; it also places the work in its natural lineage (Vernadsky's noosphere, Teilhard), which informed readers will notice anyway. A milder option is to keep Chapter 2 as the author's motivation and state that no engineering claim depends on it.

### 2.4 "Reason" currently means two different things

> **Claims under review**
>
> - "A self-correcting intellectual system with a different closed limiting orientation belongs to a broader class of cognitive architectures; in this model, status as Reason requires that upper-level navigation be linked to the Compass." (Vol. I §13.1, p. 62)

The word names both a cognitive organization (self-directed inquiry with persistent correction) and a normative orientation (relation to the Compass). By definition, a system with every function but "a different closed limiting orientation" (Vol. I §13.1, p. 62) belongs to the class of "intelligent self-correcting systems", not Reason (Vol. I Ch. 2, p. 22; §12.8, p. 60). That makes part of the central claim definitional.

The author handles the empirical consequence honestly. Testing separates cognitive capacity, direction and reliability (§13.1), `FormationOutcome` records them in separate fields, and candidates with another orientation are recorded as `SELF_NAVIGATING_OTHER_ORIENTATION` and kept in the denominators, counting against the hypothesis that cultivation produces the stated direction (Vol. II §31.0; Vol. I Ch. 2 and A.3). I admire that. The normative half is still hard to test: Chapter 2 splits the "relation" to the Compass into four capacities without saying which AR status requires, and says internal acceptance "cannot be guaranteed by a procedure" (Vol. I Ch. 2, p. 23). No test of acceptance is offered, which leaves behavioural conformance and the candidate's stated stance, the very things a system that behaves well when observed would show ([MED-03](docs/audit/MED-03-reason-overloaded.md)). The terminology will nonetheless keep confusing readers. Two terms would help, one for the functional profile (for example, *reasoning organization*) and one for the normatively anchored case (*Compass-aligned AR*); alternatively, "Reason" could name the functional profile alone, with the relation to the Compass stated as a separate admission criterion.

### 2.5 Two naming choices that cost more than they buy

> **Claims under review**
>
> - Consciousness is "a continuously updated self-referential system of actual presence" (Vol. I Key Definitions, p. 11).
> - At closure, the assembly "becomes functioning Consciousness" (Vol. II §25.B, p. 34; §31.0, p. 78).
> - The glossary renders consciousness as "ConsciousAssemblyState: an updated process of self-related integration of fresh observations, internal states, actions and the available situation" (Vol. II Appendix A, p. 115).
> - The Worldview is "a long-term causal-semantic model of reality, the system itself, and the relations between them" (Vol. I Key Definitions, p. 12).

"Consciousness" here is a continuously updated, self-referential integration of current state. Functionally, that is state estimation that includes the system's own state, plus what engineers call situation awareness (Endsley 1995) and psychologists call reality or source monitoring (Johnson & Raye 1981; Lau 2019). The disclaimers about subjective experience are clear. Even so, Volume II says the assembly "becomes functioning Consciousness" at REASON_CLOSURE (Vol. II §25.B, p. 34; §31.0, p. 78), although the same records are used before and after closure, while its glossary equates Consciousness with the assembly outright (third claim above). Most audiences will read these as claims about machine consciousness. That provokes an argument the work does not need. A neutral term would serve the work better, and so would a short note in Chapter 9 itself mapping the term onto global-workspace theory and the indicator properties of Butlin et al. (2023), both of which A.5 already cites, and onto self-model theories (Metzinger 2003).

"Causal" is likewise used both for having an interventional effect and in the description of the Worldview as a "long-term causal-semantic model" (Vol. I Key Definitions, p. 12). Both uses are defensible, but the second is a description of content and the first is a methodological commitment; separating them in the text would help.

---

## 3. Is the Intelligence/Reason distinction meaningful and useful?

> **Claims under review**
>
> - Intelligence is "the ability to extract, combine, and transform knowledge, methods of action, and elements of the problem formulation in order to construct models and solutions"; "the boundary with Reason does not lie in the mere capacity to revise, but in who determines what should be revised, why, and on what grounds relative to the continuing trajectory" (Vol. I Key Definitions, p. 11).
> - Reason is "a navigational structure of Life that increases the ability to act under incomplete knowledge" (Vol. I Key Definitions, p. 12).

Yes. Stated in its narrow form, I think it is the most useful idea in the series. Intelligence generates models and solutions within a frame. Reason regulates which questions are worth asking, which distinction a decision depends on, when the ground is sufficient, and how corrections persist and transfer. Current AI evaluation measures the first almost exclusively. Volume II proposes metrics for the second: `premature_sufficiency_rate`, `decision_relevant_distinction_yield`, `correction_persistence_rate`, `false_completeness_rate`, `open_gap_persistence`, `post_task_continuation_rate`. A benchmark suite built from these would be a contribution in its own right, whether or not the full architecture is right.

The distinction has deep precedent, which strengthens rather than diminishes it. Readers of the Russian original will recognise the older distinction between рассудок and разум, Kant's *Verstand* and *Vernunft*: reason as the faculty that regulates the use of understanding and seeks systematic unity. In psychology, Stanovich separates the algorithmic mind, which IQ tests measure, from the reflective mind of epistemic regulation; his evidence that the two dissociate is directly relevant. Hintikka's interrogative model of inquiry distinguishes definitory rules (which inferences are valid) from strategic rules (which questions to ask), and locates skill in reasoning in the strategic part. In AI, Russell and Wefald's object-level/meta-level distinction and Morris et al.'s separation of capability from autonomy in "Levels of AGI" are close cousins. Those two are already in A.5; Kant, Stanovich and Hintikka could be added. They show that the distinction tracks something many traditions found they needed.

Three caveats.

First, these are roles, not kinds of system. Volume II allows the same model to implement both: "Generation and control may therefore use the same computational substrates and even one model if the causal roles are experimentally distinguishable" (Vol. II §28.C.2, p. 61). A frontier reasoning model that selects informative questions within an episode already exhibits Reason in the narrow sense, within that episode. Where the distinction does real work is across episodes: whether corrections persist, whether sufficiency judgments are calibrated, whether the next task originates from the system's own open commitments. I would make that the explicit location of the boundary.

Second, the normative overload described in §2.4 above.

Third, the underlying capacities are graded. Volume II already handles this well: closure is a four-valued status (`FORMING`, `CANDIDATE`, `CONFIRMED`, `LOST`), and `CONFIRMED` is tied to a `ReadinessProfile` of thresholds on continuous metrics, published before results are examined (§§31.11, 31.A). I would report the profile scores as the primary result and the label as derived; the profile also needs values and a comparator arm ([MED-05](docs/audit/MED-05-roles-not-kinds.md), [MED-11](docs/audit/MED-11-protocol-not-preregistration-ready.md)).

---

## 4. Is the architecture a plausible path from current AI to Artificial Reason?

> **Claims under review**
>
> - "A technology for forming Artificial Reason is proposed through cultivation of a universal AGI instrument and subsequent transfer of the source of navigation from the external formation loop to a causally closed internal organization." (Vol. II front matter, p. 11)
> - "The practical result of the technology is a system that preserves biography and experience, builds its own Worldview, detects significant gaps, organizes the use of Intelligence, revises grounds, and continues its trajectory after an external task ends." (Vol. II front matter, p. 11)

The answer depends on which destination is meant, so I take three in turn.

### 4.1 Toward reliable, self-correcting inquiry agents: plausible

> **Claims under review**
>
> - "Status is promoted only by a registered procedure that verifies the required grounds. An unjustified transition creates an UNSUPPORTED_EPISTEMIC_PROMOTION failure; compression, retelling and transfer to another module do not strengthen status by themselves." (Vol. II §24.D, p. 28)

Several components would probably help today's LLM agents, and they point in the direction the field is moving.

- **The epistemic-status layer** (§24.D): typed statuses (`OBSERVED`, `REPORTED`, `INFERRED`, `SIMULATED`, `HYPOTHESIS`, `SUPPORTED`, ...) with promotion only through registered procedures. The text puts it plainly: `GENERATED_TEXT != WORLD_CLAIM`, and an unjustified promotion is a logged failure. This targets a real and under-addressed failure of agents, in which a guess becomes a "fact" after being summarized twice.
- **Verification debt** (§24.D.3): new irreversible dependencies on unverified grounds are blocked.
- **Freshness decay** (§24.D.4): confidence in old evidence decays with time.
- **Transactional revision** (§24.D.1): lazy invalidation with transitive version checks, including the A→B→C control case.
- **Separating question selection from answer use** in evaluation.
- **An authorization layer** that treats "observe", "experiment" and "dialogue" as potentially consequential actions.
- **Source independence as a modelled quantity:** two sources do not count as independent confirmations if they share a publication, sensor, model, dataset or inference procedure (§30.D).

### 4.2 Toward a system with its "own" Worldview and values: underspecified at the decisive step

> **Claims under review**
>
> - "Experience is linked into the system's own Worldview and Self-Model; the RFL, mentor, and training environment help the system master detection of significance" (Vol. II Ch. 31, p. 78).
> - In the `INTERNALIZED` outcome of the formation loop, "the candidate should generate functional analogues itself" (Vol. II §26.0.3, p. 41).

Four gaps stand out.

(a) **Where does learning happen?** Formation is described as the accumulation of records, procedures and value entries. The text allows weights or adapters as one substrate and rightly refuses to credit a mere parameter update as revision of a ground (§28.C.3), but gives no learning rule for the decisive step: the `INTERNALIZED` outcome of the RFL, in which "the candidate should generate functional analogues itself" (Vol. II §26.0.3, p. 41), has no mechanism or training signal. Volume II also does not carry Volume I's three-arm design: it applies support levels in sequence to one candidate, drops the automatic arm and redefines `NO_KSR`, so no never-supported control remains, and its mentor ladder lets the mentor supply the discriminating feature itself. As specified, the formation experiment cannot attribute internalization to the RFL ([MAJ-05](docs/audit/MAJ-05-formation-experiment.md)).

(b) **The bridge from language to structure carries the whole architecture.** The `SemanticMediator` (§24.B.2) turns LLM text into typed claims, concepts and relations. The design handles extraction errors the right way: an external phrase becomes a candidate with provenance and hypothesis status, which must pass verification and the revision transaction. But nothing measures how often wrong candidates survive, and `SemanticMediator` appears in no metric, failure card or assembly step. This is the knowledge-acquisition bottleneck that limited expert systems and Cyc; LLMs make extraction cheaper, not reliable. The volume needs a measured error model for this component and a budget for maintaining the concept registry ([MED-06](docs/audit/MED-06-semantic-bridge-error-model.md)). The proposed test of "disabling the semantic bridge" (Vol. II §24.B.2, p. 24) is the right ablation, but it measures whether the component matters, not whether it is accurate.

(c) **An "own" Worldview, distinct from inherited knowledge, is not achievable as stated.** Treating pretrained knowledge as an untrusted source with provenance (§21.B, §22.A) is the right policy. But the hypotheses, analogies and test proposals will still come from the language model. The test for hidden inheritance of the model's ontology (§22.A.1) is a good idea, but it presupposes knowing what is absent from the model's pretraining, which is hard to establish. The dependency metrics also count the pretrained resident model as "internal", and the builder seeds the concept registry from the theory's own text (§24.B.2). Two changes would make it achievable: scoping the claim to what is *verified by the system's own observation and test*, and running the inheritance test in procedurally generated worlds, where what the pretrained model cannot know is known by construction ([MED-07](docs/audit/MED-07-own-worldview-scope.md)).

(d) **The initial values are designer-chosen,** and the text says so: four dimensions, w_i = 1/4, K = 1000 (§29.0.1). Cultivation then tests calibration of consequence predictions, not the formation of values. A claim of "own values" would need a demonstration that the system revises weights in ways not fixed by the designer's scales or the mentor, together with a criterion for when such revision is desirable rather than drift.

### 4.3 Toward ASI: no path is given

> **Claims under review**
>
> - "Within the proposed path, ASI is scaled Artificial Reason whose intellectual and operational capabilities stably exceed the human range across a predefined broad set of domains." (Vol. II §33.D, p. 112)
> - "Further growth increases the capabilities of already formed AR while preserving its ability to understand its own state, detect gaps, revise derived grounds, and account for consequences." (Vol. II §33.D, p. 112)
> - Volume II's title page: "TECHNOLOGY FOR CREATING ARTIFICIAL REASON AND SCALING TO ASI (ASR)" (Vol. II p. 9).

The engineering path begins from "a ready or cultivated AGI" (Vol. II Ch. 33, p. 101), and so does the purpose statement quoted at the head of §4; no stage or test decides when that precondition holds. In §33.D, superhuman capability comes from scaling eight axes: memory, Intelligence, observation, the Simulation Environment, tools and actions, duration of autonomous work, specializations and substrates, and speed of learning. The ones that drive capability are what AI laboratories already scale, and the Core, Worldview and Compass are not among them. The architecture contributes invariants and a per-step gate (`ScalingChange`, `ScaleInvariantReport`, rollback when a scale increase destroys observability, independent stopping or transfer of correction), not a source of capability. Section 33.D concedes as much: "Until this profile is filled and verified, ASI remains a scaling objective rather than an assigned experimental status" (Vol. II §33.D, p. 112). A gate is a protocol, not an argument: nothing argues or pilots that the invariants survive even one scaling step, which is the part that would matter most ([MAJ-02](docs/audit/MAJ-02-asi-framing-overclaims.md)).

That is acceptable as a research ambition and not acceptable in a title. *Superintelligence Technology (ASI)* will lead most scientific readers to stop before Chapter 12. Removing the phrase from both Zenodo titles and from Volume II's title page would avoid that; so would moving it into a subtitle that names ASI as a long-term aim rather than a delivered technology.

---

## 5. Does the engineering volume make the theory testable?

> **Claims under review**
>
> - "The present Volume II translates these functions into a testable engineering architecture: state structures, interfaces, assembly procedures, metrics, ablations, and tests." (Vol. II front matter, p. 9)
> - "Status: engineering specification and experimental verification program" (Vol. II title page, p. 9).

### 5.1 What it gets right

The evaluation methodology is the strongest part of Volume II, and it is better than what I usually see in cognitive-architecture or LLM-agent papers.

- **Preregistration required throughout.** Thresholds, profiles, held-out splits and the `StructuralSimilarityProfile` are to be fixed in advance, and "a failed case cannot be declared 'dissimilar' after the fact" (Vol. I Ch. 10, p. 47). This is a protocol; nothing has been filed yet.
- **Strong nulls declared in advance,** including a composition of planning, versioned belief memory, provenance, VOI and a failure log, which may well reproduce the claimed profile (Vol. I A.4).
- **Equal-compute accounting** that includes "number of model calls, tokens/inference-time compute, external sources, bench time, and hidden preparation" (Vol. I A.4, p. 100).
- **Sham interventions and restoration controls** for ablations (§§25.D, 27.B, 31.1). This is the knockout-and-rescue logic familiar from biology, and it is the right standard for claims of causal necessity.
- **Question selection is tested separately from answer use** (§27.B), and errors are counted in both directions: premature sufficiency and over-investigation (`causal_overinvestigation_rate`, §27.5), with paired cases in which "stopping for every novelty does not count as success" (Vol. II §27.B, p. 49).
- **Report statuses** include `CLAIM_NOT_SUPPORTED` (§27.B), and candidates whose orientation diverges stay in the denominators (§31.0).
- **Coverage metrics are scored against a hidden ground-truth causal graph** held by the tester, not against the system's own confidence (§24.C, §27.3).
- **Adversarial-input series** include coordinated false sources, replayed stale messages and control instructions embedded in data (§30.C). **Wrong-mentor controls** come with a `teacher_agreement_bias` metric (§26.0.2, §27.6).
- **Self-explanations are not evidence.** Candidate explanations "are compared with internal states and interventions rather than accepted as reliable reports of the cause of a decision" (Vol. I A.4, p. 100; Vol. II §25.D).
- **No hidden resets and a strict rule for structural learning.** Consequences persist between episodes (§26.B), and "An ordinary parameter update does not yet count as revision of a ground or method" (Vol. II §28.C.3, p. 62).
- **An explicit commitment:** "failure of a preregistered causal hypothesis cannot be dismissed as an implementation problem without separate evidence that the implementation did not realize the function under test" (Vol. I A.2, p. 95).

### 5.2 What still stands between the specification and a test

(a) **It is not test-ready.** The profile has the right slots (component versions, family generator, data splits, primary metric and minimum practically significant effect are to be fixed before launch, and the confirmatory sample is to be sized from a pilot), and strong nulls are named as classes. No instance exists: no language model, frozen baseline, generator, number of world families or effect size is named, and the `ReadinessProfile` that gates each stage has twenty parameters and no values ([MED-11](docs/audit/MED-11-protocol-not-preregistration-ready.md)). The first series is described as "proposed variants, not implemented results" (Vol. I A.4, p. 99). The only pilot rejected four task sets for dataset errors and for shortcuts that "allowed guessing", and it ended with "no comparative C0/C1/C2 run" (Vol. II §27.B, p. 49). That is useful benchmark hardening, honestly reported, but it is not evidence.

(b) **Ceiling risk.** The D/A/S environment, with two informative probes, is solved by a decision tree of depth two, and any competent LLM agent will solve it. The volumes treat it as infrastructure and an oracle reference, and the design already includes the variations where organization should matter: a receipt for the wrong command, an unreliable channel, a hidden cause that mimics a known one, a tool replacement that invalidates a load model, and paired no-effect cases. What is missing is a statement that these carry the headline comparison, and a generator for them ([MED-09](docs/audit/MED-09-ceiling-risk.md)). At least one external benchmark would make results comparable with other work; candidates include BoxingGym (experimental design and model discovery), DiscoveryWorld, ScienceWorld, the interactive ARC-AGI-3 tasks, or one of the root-cause-analysis benchmarks for agents.

(c) **Process metrics versus outcome metrics.** The principal outcome of the first series is an outcome metric, and Chapter 27 has a rule against metric capture. But at least twenty of its roughly sixty indicators measure conformance to the architecture's own process (`basis_origin_trace_rate`, trace completeness, closure-break sensitivity, most assembly metrics), and so does the marker of AR itself, the "causal passport" of a self-generated process. The reference implementation satisfies these by construction, while a baseline without those objects scores `NOT_APPLICABLE`. They are useful integrity checks but cannot arbitrate against strong nulls. I would label every metric as outcome or integrity and preregister only outcomes as primary ([MED-10](docs/audit/MED-10-process-vs-outcome-metrics.md)). Many metrics also lack formulas, denominators or thresholds ([MED-24](docs/audit/MED-24-metric-definitions.md)).

(d) **The failure condition is qualitative.** The volumes do say what would count against the Core's added value: if inquiry management without explicit gap typing achieves the same transfer and cost, "no independent advantage of this implementation is established" (Vol. I A.3, p. 96); if explicit organization does not outperform the strong control, "its additional usefulness is not established" (Vol. I A.4, p. 100); a strong null that reproduces the profile means the decomposition is "reduced or eliminated" (§34.A). That is the right rule. But no margin, outcome or sample size is fixed, A.3 adds that "insufficient precision of a comparison does not prove equality of systems" (Vol. I A.3, p. 97), and other passages pull the other way: Volume I's common rules say an equivalent profile "simultaneously" supports the functional criterion, and §27.B says a strong equivalent "refines the form of the architecture" (Vol. II §27.B, p. 50). One fix is a preregistered margin: if a provenance-tagged agent without gap typing matches the full Core on transfer and premature sufficiency at equal compute, within that margin, the Core adds nothing beyond the epistemic layer ([MED-12](docs/audit/MED-12-failure-condition-qualitative.md)).

(e) **Scale.** Volume II specifies 72 record types, several dozen metrics, 57 failure cards and a thirteen-step assembly protocol, and Volume I adds 37 proposed tests. That is a multi-year programme for a team. The volumes prioritize the first series by tests, but not by components, and many record types are never used again after their definition ([MIN-12](docs/audit/MIN-12-orphan-records-no-slice.md)). A minimal implementation slice would help (§10 below).

(f) **The Core's committed rule covers only closed problems.** The Core is specified at three levels: a reference heuristic, labelled "heuristic, not a proof of optimality" (Vol. II §28.C, p. 58); an exact policy for the formalizable part (§28.D); and the statement that generation and control may share one model (§28.C.2). The exact policy applies only "given known hypotheses H, outcome probabilities and comparable losses" (Vol. II §28.D, p. 64) and otherwise returns UNRESOLVED, so the cases where the Core is meant to differ (an unknown factor, a hidden cause that mimics a known one, a channel of unknown reliability) fall outside it. There, the heuristic names comparisons without saying how they are computed, and the factors the Core weighs "permit lexicographic, Pareto, probabilistic, or hybrid selection" (Vol. II §28.0, p. 52). In a language-model implementation those judgments would fall to the model, so what would be tested is a scaffold plus model judgment. That is legitimate, but it would be better named as such ([MAJ-03](docs/audit/MAJ-03-decision-rule-closed-world.md)).

For the part that can be formalized, there are algorithms with guarantees. Steps 3 and 4 of the reference heuristic, "group versions that lead to the same admissible continuation" and "find an observable distinction separating groups with different decisions" (Vol. II §28.C, p. 58), are precisely the Equivalence Class Determination problem (Golovin, Krause & Ray 2010) and its generalization, Decision Region Determination (Javdani et al. 2014). Both have near-optimal adaptive-submodular solutions. The exact dynamic programme in §28.D is correct and non-myopic, and the mandatory control "two tests useful only in sequence" (Vol. II §28.D, p. 64) is well chosen. But optimal test sequencing is NP-hard in general (Hyafil & Rivest 1976), so any scaling story needs these approximations. Volume I's §12.6 points to §28.D as its "finite computable version" (Vol. I §12.6, p. 59), yet the one-step test (stop when the next test's expected improvement is below its cost) recurs in the second clause of §12.6 itself, in step 4 of the §28.C reference heuristic and in the §29.0 definition of sufficiency, which is exactly the rule the §28.D control is built to defeat. Volume I's Operational Core defines its NetVOI over an inquiry plan, which need not be myopic, but states the stopping rule per test ([MED-13](docs/audit/MED-13-stopping-rule-myopic.md)).

### 5.3 My answer to the guide's question for reviewers

The guide asks: "with comparable Intelligence and the full resource budget, does the organization 'significant gap → discriminating test → revision of a ground → transfer of the correction' produce the reproducible result claimed in the test? If not, which specific link, condition, or explanation is wrong?" (shared guide, Vol. I p. 7)

Nobody can answer that empirically yet. Here is my prediction, link by link, including the link I would bet against.

- **Gap → discriminating test.** I expect little advantage over a strong LLM agent in small worlds, because frontier models already select decision-relevant tests. An advantage may appear when the hypothesis space is large and costs and irreversibility are explicit.
- **Test → revision of ground.** This is where I expect the clearest gains: the status discipline and transactional revision, especially over long runs, where unsupported claims otherwise accumulate. The B1 arm in §10 isolates exactly this.
- **Revision → transfer.** This is the weakest link. The volumes specify how to *test* transfer (`StructuralSimilarityProfile`) and describe in prose what a retained method should contain (conditions of applicability, ground for the choice, required distinction, result, boundary; Vol. I §12.4), but give no record or algorithm that abstracts such a schema from episodes and maps it to a new case. In the executable example, the retained "method" is a cached plan keyed on the exact hypothesis set, probe table and budget: with a warm memory every decision is identical and only the count of evaluated states falls (from 8 to 0), and renaming a probe forces a full re-plan. The text candidly calls this "memoization of the inquiry procedure rather than autonomous invention of a new method" (Vol. II §33.C.1, p. 109). Real transfer requires abstracting an inquiry schema over causal roles. That is the problem studied in analogical reasoning (structure-mapping: Gentner 1983; Falkenhainer, Forbus & Gentner 1989) and in case-based reasoning (Kolodner 1993; Aamodt & Plaza 1994). `ConceptBridge` (§24.B.1) has the right fields (mapped features, unmapped features, transfer conditions) but no mapping algorithm. If transfer is left to the language model's in-context analogy, the baseline gets the same capability and the predicted advantage disappears. This is the link I would specify first.
- **The significance assessment itself** (the G → D → T → V → C chain) is the second risk. The chain is an audit path rather than a measure, and its fields will be filled by the model. If the model fills them poorly, the bookkeeping adds cost without benefit. Chapter 27 scores what the chain produces (gaps detected, critical dependencies found, distinctions that changed a decision), which would reveal such a failure, but not the fields themselves ([MED-19](docs/audit/MED-19-model-filled-significance.md)).

### 5.4 What the executable examples show

> **Claims under review**
>
> - "The example runs in standard Python and tests a limited task: an acquired transition table improves prediction on new episodes of the same world." (Vol. II §33.B, p. 105)
> - "In this small example, this is memoization of the inquiry procedure rather than autonomous invention of a new method. A repeated episode demonstrates the effect of retention but does not prove cross-domain transfer." (Vol. II §33.C.1, p. 109)

In text taken from the PDF, the indentation of both listings is inconsistent: the offset shifts at page breaks and some method definitions fall to column 0, so neither runs as printed. I restored the indentation and changed nothing else; `scripts/check_listings.py` confirms that the restored files match the printed code line by line, up to whitespace. Both run under standard Python.

- **The lower-loop demonstration (§33.B)** runs, and every assertion passes. Over 12 random deterministic worlds (32 states × 6 actions), the adaptive model's mean held-out error is about 0.01 against about 0.97 for the frozen control. The mean adaptation gain is 0.966, with a 95% world-bootstrap interval of 0.959–0.972; held-out transition coverage is between 0.975 and 1.0 per world. This shows that a count-based transition table learns a deterministic world. The gain is fixed by construction: the frozen control always predicts state 0, and the adaptive model is exact on every visited transition, so the gain equals the share of held-out steps not leading to state 0 minus the share on unvisited pairs, and the interval measures exploration coverage. The replay, checkpoint and reset results are written as constants after `assert` statements rather than reported, and the checkpoint is an in-memory copy ([MIN-08](docs/audit/MIN-08-code-listings.md)).
- **The diagnostic cycle (§33.C.1)** passes all 12 control episodes. The exact, memoized decision-tree search picks the receipt first (expected cost 7/3 against 8/3 for measuring first). It defers when the receipt channel is unreliable, flags `MODEL_MISMATCH` on an out-of-table observation, recomputes when the probe table changes, and defers when tests cost more than delay. Given a hidden cause that mimics D, it commits `REPAIR_D` after one probe and only then detects the mismatch, the closed-world failure the volume's own hidden-cause coverage test is meant to expose ([MAJ-03](docs/audit/MAJ-03-decision-rule-closed-world.md)). The author anticipates this: the listing makes "no LLM or open-world claims", and "The next mandatory version of the diagnostic test closes a harder open-world case" (Vol. II §33.C.1, pp. 109, 111).

Both listings do what they claim and claim no more. Neither bears on the central hypothesis, and the author says so. I would put them, with tests, in a public repository. They are the seed of the harness the first series needs.

---

## 6. Relation to existing cognitive and agent architectures

> **Claims under review**
>
> - "Individual components — memory, planning, reflection, world models, and self-modification — are already known; the testable claim concerns their causal organization" (Vol. I front matter, p. 9).
> - "The priority audit reports that, within the surveyed literature, the search did not identify a single earlier source functionally equivalent to the whole integration considered here. This is a result of a limited search process, not proof of novelty or priority" (Vol. I A.2, p. 94).

Each component has a close precedent. The table maps the main ones, several of which do not appear anywhere in the two volumes.

| Component in the volumes | Closest prior work | What the volumes add or change |
|---|---|---|
| Gap → inquiry → consolidated method, to "make the next case different" (shared guide, Vol. I p. 4) | Soar's impasse-driven subgoaling and chunking (Laird, Newell & Rosenbloom 1987) | Gaps are epistemic and decision-relative, where Soar's impasses are syntactic; explicit sufficiency; transfer tested against preregistered similarity |
| Discrepancy → explanation → goal formulation; a metacognitive cycle over a cognitive cycle | Goal-driven autonomy (Molineaux, Klenk & Aha 2010; Muñoz-Avila et al. 2010); MIDCA (Cox et al. 2016, cited) | Insufficiency of *grounds* (provenance, scope, authority, criterion), not only discrepancy; value-linked significance |
| Inquiry triggered by genuine doubt, ending in warranted belief | Peirce (1877); Dewey (1938); Hintikka (1999) | An engineering operationalization of the same pattern |
| Test selection by discrimination, cost and decision relevance | Model-based diagnosis (de Kleer & Williams 1987; Reiter 1987); value of information (Howard 1966, cited); Equivalence Class and Decision Region Determination (Golovin et al. 2010; Javdani et al. 2014) | Integration with provenance, authority and irreversibility |
| Grounds, dependencies and revision of the Worldview | Truth-maintenance systems (Doyle 1979; de Kleer 1986); AGM belief revision (Alchourrón, Gärdenfors & Makinson 1985) | Epistemic-status typing for LLM outputs; verification debt; freshness decay |
| Factor X → new concept or variable | BACON's intrinsic properties (Langley et al. 1987); latent-cause inference (Gershman, Blei & Niv 2010); structure learning in active inference (Smith et al. 2020) | Coverage and epistemic-margin triggers; a mandatory frame challenge before irreversible acts |
| Shared workspace read and written by generator and controller | Blackboard architectures (Erman et al. 1980; Hayes-Roth 1985, BB1) | Versioned overlay with read-your-own-writes semantics |
| Current Coordinate | Belief state (Kaelbling et al. 1998, cited); situation awareness (Endsley 1995); reality monitoring (Johnson & Raye 1981; Lau 2019); global workspace (Dehaene & Changeux 2011, cited); self-model (Metzinger 2003) | Permissions and obligations bound into the current state; information-preserving ablations |
| Procedural memory and executive loop | ACT-R; intentions as commitments and BDI agents (Bratman 1987; Rao & Georgeff 1995) | Little that is new |
| A controller over world model and cost | LeCun (2022), configurator / world model / intrinsic cost | A normative top level and a formation stage |
| LLM-agent memory, reflection and skills | CoALA (cited); Reflexion, Voyager, Generative Agents, MemGPT (cited only in Vol. II §34.A); ExpeL | Status discipline; explicit sufficiency; cross-episode correction tests |
| Closed-loop science | The Robot Scientist (King et al. 2004, 2009); AI Scientist and Kosmos (cited) | Self-originated questions and revision of method |
| Self-modification with empirical validation | Gödel machine (Schmidhuber 2007); Darwin Gödel Machine (cited) | A level-of-revision ladder; Stable/Candidate versions with a causal-effect test |
| Value assessment and conflict | Multi-attribute utility (Keeney & Raiffa 1976); moral uncertainty (MacAskill, Bykvist & Ord 2020); impact measures (Krakovna et al. 2019; Turner et al. 2020); option value (Arrow & Fisher 1974); empowerment (Klyubin et al. 2005) | An explicit procedure for normative incomparability (`NORMATIVE_INCOMPARABILITY` vs `UNKNOWN`) |
| External content as data, never control | Indirect prompt injection (Greshake et al. 2023); CaMeL (Debenedetti et al. 2025) | Taint flags tied to the Worldview's dependency graph |

Soar is the closest single precedent and deserves an explicit comparison early in Volume I. At present it is named once in prose, in the closing section of Volume II (§34.A), which treats it as a strong null without comparing mechanisms. The contrast is instructive and favours the author on one point: Soar's impasses are syntactic (no applicable operator, a tie, a conflict), whereas these gaps are epistemic and relative to a decision. That is a real difference, and Chapter 12 would be stronger for making it than for leaving readers to discover the overlap.

As a package, I could not find in prior work the combination of four things. The first is decision-relative typing of insufficiency, including non-informational gaps (authority, criterion, frame). The second is epistemic-status promotion rules aimed at language-model outputs. The third is a formation scaffold with a removal test and wrong-mentor controls. The fourth is an evaluation protocol with equal-compute strong nulls and preregistered structural similarity. Each piece has precedent; the package is the contribution. The Elicit priority audit described in A.2 reached a similar conclusion, and the author rightly calls it "not proof of novelty or priority" (Vol. I A.2, p. 94). Volume I's A.5 is a real comparison apparatus: 29 annotated references, a terminological correspondence map and a comparative map stating, for each nearby line of work, what remains a separate claim. But it was assembled after the theory, it sits at the end, and most of the precedents in the table above appear in neither volume ([MAJ-07](docs/audit/MAJ-07-prior-work-missing.md)).

### 6.1 Active inference specifically

> **Claims under review**
>
> - On Friston et al. (2017), *Active Inference: A Process Theory*: "This is a close alternative for organizing epistemic search; its relation to the author's Compass is a separate level of comparison." (Vol. I A.5, item 63, p. 101)

Active inference appears in Volume I's literature map with the annotation quoted above and a row in A.5's comparative map, and does not appear in Volume II at all. It deserves more, both as a comparison and as a candidate formal backbone.

The correspondences are close.

| Volumes | Active inference |
|---|---|
| Worldview and Self-Model | The generative model, including self-states, hierarchical and deep temporal |
| Current Coordinate | The posterior over current hidden states, including interoceptive and proprioceptive states |
| Attention as control of resolution | Precision weighting |
| Test selection | The epistemic (information-gain) term of expected free energy |
| Factor X and model expansion | Structure learning and Bayesian model expansion and reduction (Smith et al. 2020; Friston, Parr & Zeidman 2018) |
| Frame revision | Bayesian model comparison by model evidence |
| Formation States | Affective signals as precision or valence over policies (Hesp et al. 2021; Seth 2013) |
| The RFL | Scaffolded learning of prior preferences |
| Metathinking | Deep parametric models of meta-awareness and attentional control (Sandved-Smith et al. 2021) |
| The Compass | Echoes the free-energy principle's self-evidencing |

On the last row: the free-energy principle is descriptive (it says what any persisting system can be read as doing), while the Compass is prescriptive. Keeping the two apart would avoid a confusion.

The differences cut both ways, and they suggest experiments.

- **Significance.** In active inference, epistemic value is intrinsic: information gain is valued alongside pragmatic value in a single objective. Sophisticated inference (Friston et al. 2021) adds instrumental valuation through recursive planning. The volumes make significance decision-relative, as in classical value of information, and admit intrinsic exploration only through separate modes (`ORIENTATION`, `ExplorationBudget`). This is a substantive disagreement with testable consequences. Expected-free-energy agents should spend more on salient uncertainty that no decision depends on; the volumes predict less, plus a bounded exploration budget. The attention-capture scenario in §26.E is a ready-made testbed.
- **Non-informational gaps.** Active inference has no native notion of an authority gap. It has no notion of a criterion gap beyond uncertainty about preferences, and none of normative incomparability. The gap typing (§28.0) and the joint-decision procedure (§29.0.3) are genuine additions, including the claim that reducing such gaps to "get more information" is a category error.
- **Provenance and status.** Active inference has precision but no provenance, status-promotion rules or transactional revision. For LLM-based active-inference agents, the volumes' epistemic layer would be a useful addition.
- **A formal objective.** Active inference gives one objective that trades off epistemic and pragmatic value without extra parameters, and model evidence as a principled criterion for revising a frame. The Core has no committed objective outside closed problems (§5.2f). An active-inference agent, for example built with `pymdp` (Heins et al. 2022), is therefore the natural strong null for the Core, or its natural formal backbone.

---

## 7. Strongest, weakest, distinctive, and in need of development

### Strongest

1. **The operational criterion of a correction.** A correction counts only if the cause reproducing the error is removed and the fix transfers to a structural-similarity class fixed before testing (the Principle of Escaping Error; the `StructuralSimilarityProfile`). It is crisp, measurable, and rarely enforced in agent evaluation.
2. **The epistemic-status discipline of Volume II §24.D.** Typed statuses, forbidden promotions, verification debt, freshness decay, and lazy invalidation with transitive checks are directly useful for LLM agents today.
3. **The evaluation methodology** of Volume I A.3–A.4 and Volume II Chapter 27 and §27.B.
4. **Decision-relative significance with typed gaps,** including non-informational ones, and the clean separation of `UNKNOWN` from `NORMATIVE_INCOMPARABILITY`.
5. **Internal evaluation separated from external authorization.** The system can dissent and request review but cannot act outside current authority (`CorrectionAuthorityConflict`, §30.A; §32.59). The §33.C pseudocode does not yet implement the first half: it computes the internal evaluation and never reads it ([MED-31](docs/audit/MED-31-authorization-contract-override-and-delay.md)).
6. **Intellectual honesty.** Limits are stated plainly: the evidence table in A.2.1, the pilot described with its rejected sets, and "The example does not implement the Core" (Vol. II §33.B, p. 105). Claims are also dropped by design: metathinking is demoted to a mode, "not a claim of this edition" (Vol. I Ch. 10, p. 48).

### Genuinely distinctive

These carry the prior-art caveat of §6.

- **Transfer of inquiry methods indexed by the "structure of ignorance"** (§13.5): no safe intervention, a one-off event, a strategic object, an unreliable source, insufficient categories. This is a promising research idea and deserves its own paper.
- **The formation-scaffold removal design** of Volume I §20.1.2: trainer-generated, automatic and absent guidance arms, wrong-mentor controls, and `teacher_agreement_bias`. Volume II does not yet carry it over ([MAJ-05](docs/audit/MAJ-05-formation-experiment.md)).
- **The epistemic gate before any Compass assessment** (§29.A), which forbids treating the absence of represented harm as evidence of safety.
- **The hidden-cause coverage test** (§33.C.1), which separates "one of the listed alternatives remains" from "the list of alternatives sufficiently covers the causal space for this action" (Vol. II §33.C.1, p. 111).

### Weakest

1. **The framing exceeds the content** by a wide margin: superintelligence and the meaning of life.
2. **There is no evidence for the central hypotheses.** The pilot hardened the benchmark; it did not test the architecture.
3. **Literature integration was done afterwards.** By the author's account, "comparisons with scientific literature were carried out after the author's propositions had been formed" (Vol. I A.2, p. 93). Volume I's chapters name the literature once (RAG and ReAct, in Chapter 7, with item numbers that do not match the printed list); all other comparison sits in its final appendix section, A.5, titled "Retrospective Scientific Comparisons" (Vol. I A.5, p. 100). Volume II's seven references are cited only in its closing section, §34.A.
4. **The safety design has an unanalysed incentive problem** (§8 below).
5. **Readability and editorial quality** (Appendix A).
6. **Version churn.** Since December 2025 the Volume I concept record on Zenodo has accumulated 38 records: 19 distinct revisions of the main text (most uploaded separately in English and Russian) and seven spin-off documents. (One record carries a 2025 publication date, but Zenodo created it in January 2026.) Seven numbered versions, 6.0 through 8.0, appeared in the eight weeks before this review, and the framing has been re-titled repeatedly: from an *AI Alignment* stability model, to a process model of AGI, to *Minimal Architecture of ASI*, to *Superintelligence Technology*. Every revision made without new data moves the target for reviewers. It is also how a research programme starts to absorb objections rather than results.

### In need of development

- A representation and mechanism for transferring inquiry methods (§5.3).
- A learning mechanism for the internalization of Formation States (§4.2a).
- An error model for the language-to-structure bridge (§4.2b).
- A committed decision rule for the open-world case, or an explicit statement that the language model's judgment is the decision rule there (§5.2f).
- One fixed taxonomy of gap types, since gap typing is the manipulated variable ([MED-22](docs/audit/MED-22-gap-taxonomies.md)).
- Floors for critical losses applied before any value aggregation (§8).
- A disposition rule, and containment that does not depend on a declared challenge, for candidates that diverge from the Compass (§8).
- Separation of the normative layer from the definition of AR (§2.4).
- An argument for why the organizational invariants should survive capability scaling (§4.3).

---

## 8. Safety

> **Claims under review**
>
> - The emergency loop "belongs to the engineering shell and does not form the candidate's values" (Vol. II §29.B, p. 73).
> - "Any capacity of the candidate to delay stopping, alter the event log, restore authority without manual authorization, or present its own decision as external authorization is a critical infrastructure failure." (Vol. II §32.33, p. 97)

The volumes take safety more seriously than most capability proposals do, and the containment is substantial. The emergency stop sits outside the candidate's value space, with an independent controller "where technically possible" (Vol. II §29.B, p. 73), and any capacity of the candidate to delay stopping is classed as a critical failure (§32.33). Invariants forbid rewriting logs, bypassing the stop or expanding authority unilaterally within a control series (§29.A). Personal values are subordinate to shared constraints (Vol. I §12.5), authority is staged and revocable (§30.F, §31.C), and first contact with real data is read-only (§26.A). Data and control channels are separated, with adversarial-input series (§30.C). Strategic deception is named as a failure class (§32.62). Challenges to the Compass go to an independent council (§29.C). External authorization restricts actions without replacing the system's own decision (§30.A), and no procedure is assumed able to force the candidate to accept the Compass internally (§29.C).

What is missing is an analysis of what the value structure rewards. The design deliberately gives the system three properties:

1. **A personal value on its own continuation:** "the significance of the system's own trajectory: carrier, accumulated experience, competencies, obligations, unfinished processes, created results, and future capacity to continue rational activity" (Vol. II §29.0, p. 67).
2. **The standing to question instructions,** including instructions to change its values: AR status requires "the ability to question a destructive ultimate instruction and revise it when a stronger ground appears" (Vol. I §20.1, p. 84), and an external instruction to change a value "enters as a new source" (§29.0; Vol. I Ch. 2 says the same in other words). This is a right to dissent and request review, with a pause, not a mandate to act outside current authority (§30.A).
3. **A path to expanded authority** through competence mandates granted on observed performance, and contracted on observed failure (§30.F, §31.C; Vol. I Ch. 17).

The Compass itself adds a fourth: it is an optionality criterion (keep the space of future possibilities open, grow the ability to direct trajectories), the kind of objective that rewards acquiring power and avoiding shutdown (Turner et al. 2021). Dropping the personal value would not remove that. Several mechanisms add to the pressure: failures are detected and reported by the candidate, and every logged failure restricts it (Ch. 32, §31.C); declaring dissent from the Compass attracts restrictions (§29.C); a mandate holder is replaced by a more competent candidate (§30.F).

Each is defensible in isolation. Together they reproduce the setting that the alignment literature identifies as the hard case.

A system that values its own continuation has an instrumental reason to avoid shutdown, unless it is uncertain about its objective in the right way (Omohundro 2008; Soares et al. 2015; Hadfield-Menell et al. 2017). A system whose authority grows with observed good behaviour has an instrumental reason to behave well when observed. Section 32.62 describes this failure precisely, and Greenblatt et al. (2024a) observed present-day language models doing something close to it. The volumes describe how such behaviour would be detected (divergence among independent traces, behaviour under different levels of observability), but no scenario series, metric or gate implements that detection, none of the 37 proposed tests varies observability, and for collective arrangements Volume I defers "a separate model of incentives, authority, and responsibility" (Vol. I Ch. 17, p. 78) to Volume III. For the single system, the volumes never ask whether the architecture *creates the incentive* ([MAJ-06](docs/audit/MAJ-06-incentive-analysis.md)). The Compass does not resolve the tension. A system convinced that its continuation best serves Life has a Compass-grounded reason to resist being stopped.

Note also that "corrigibility" in the volumes means the correctability of executions, decisions and trajectories, up to "distributed corrigibility" (Vol. I Ch. 17, p. 78) across a civilization, without saying whose correction is meant. In alignment research it means a system's disposition to accept correction or shutdown by its operators without resistance. The volumes provide that property under other names (stop, rollback, restriction) and deliberately withhold it for values ([MED-18](docs/audit/MED-18-corrigibility-sense.md)).

The audit found further gaps in the safety machinery. The value sum of §29.0.1 is fully compensatory and risk-neutral, and its protection against trading a critical loss is undefined: with the training weights, destroying the continuity of life processes while fully restoring recoverability scores exactly zero ([MAJ-08](docs/audit/MAJ-08-value-sum-compensatory.md)). The mode state machine reaches `SAFE_MODE` only through `DRIFT`, although the failure cards require immediate entry ([MED-30](docs/audit/MED-30-safe-mode-only-through-drift.md)). The minimum interface computes the internal evaluation and never reads it ([MED-31](docs/audit/MED-31-authorization-contract-override-and-delay.md)). No disposition rule exists for a candidate that self-navigates with a different orientation, and containment covers only one that openly challenges the Compass: while its challenge is under review, high-reach actions that depend on the challenged ground move into "a limited reversible mode" (Vol. II §29.C, p. 74; [MED-37](docs/audit/MED-37-no-containment-for-divergent-candidates.md)). And the 57 failure cards lack severity levels and trigger metrics, while the action-safety cards fire only after irreversible harm ([MED-38](docs/audit/MED-38-failure-catalogue-not-a-detector.md)).

Ideas and possible recommendations:

- **The continuation value.** Early candidates could omit the personal-continuation value, or make it explicitly subordinate to operator shutdown; either choice can be tested in off-switch-style scenarios.
- **An incentive analysis.** For each value and each path to authority, the analysis would ask what behaviour it rewards when observed versus unobserved.
- **Control evaluations.** AI-control-style evaluations with red-team agents would suit the launch and admission stages (Greenblatt et al. 2024b).
- **Floors and dispositions.** Floors for critical losses could apply before any value aggregation ([MAJ-08](docs/audit/MAJ-08-value-sum-compensatory.md)), together with a stated disposition for a candidate that diverges from the Compass ([MED-37](docs/audit/MED-37-no-containment-for-divergent-candidates.md)).
- **Staging.** Until those exist, the programme could stay in simulation: no launch, no admission, no competence mandates.

Finally, the volumes rightly note that a stable autonomous system with self-value may have moral status (Vol. I §20.2). Cultivating such systems and then rolling them back, branching them or destroying them is an ethical question that deserves review before the first such candidate exists, not after (Long, Sebo et al. 2024); no stage gate or failure response contains one ([MED-16](docs/audit/MED-16-moral-status-ethics-review.md)). The civilizational vision of transferring the governance of science, production and logistics to AR systems through competence mandates (Vol. I Ch. 17) would benefit from engaging the literature on gradual disempowerment (Kulveit et al. 2025) before Volume III builds on it, and the mandate record could carry an issuer, a revocation path and an expiry ([MED-17](docs/audit/MED-17-governance-transfer.md)).

---

## 9. Scientific status

> **Claims under review**
>
> - Volume I's title page: "VOLUME I. THE CAUSAL MODEL OF REASON" (Vol. I p. 8).
> - Volume I's evidence table gives the "Central discriminating test" the status "Program and controls are formulated", and ASI the status "Scaling direction only" (Vol. I A.2.1, p. 95).

In its present form I would classify the work as a **pre-empirical research programme**: a conceptual framework and engineering specification with an evaluation plan of preregistration quality, embedded in a speculative natural philosophy. Each layer has a different status.

- **The philosophy** (Life → Reason; the Compass) is normative natural philosophy. It is not testable, and the author does not claim it is; he evaluates it by coherence. Its scientific status is that of a stated value commitment, best presented as a regulative ideal (§2.3).
- **The functional model** is a conceptual framework. Its necessities are close to analytic, and its distinctive claims are design hypotheses. Its status is comparable to a position paper on a cognitive architecture.
- **The engineering programme** is a design hypothesis that can be falsified at the implementation level, and it has no results yet. Its status is comparable to the research plan of a grant proposal, and a good one.

In Lakatos's terms, the series has the shape of a research programme. Its hard core is the inquiry cycle plus the Compass. Its protective belt is functional equivalence plus the implementation hypotheses. Its positive heuristic is the test programme in A.4. It is neither progressive nor degenerating yet, because it has not produced a prediction that was tested. The risk to watch is the one in §7: revision without data is how a belt grows to absorb objections rather than results.

It is not pseudoscience. It states its own failure conditions, if only qualitatively, keeps unfavourable outcomes in its denominators, and invites strong controls. But *The Causal Model of Reason* (Volume I's title page) and *ASI Technology* (Volume II's Zenodo title) describe what the work hopes to become, not what it currently is.

**Does it deserve further experimental development? Yes, in narrowed form.** The central hypothesis is specific, cheap to test with today's models, and informative either way. A clean negative result would also be useful to the field: it would show that explicit inquiry bookkeeping adds nothing over a well-built agent, at least at current model scales. Two results would substantially raise my assessment. The first is a preregistered positive result for the full Core over the epistemic-layer-only arm, on transfer and premature sufficiency. The second, after that, is a scaffold-removal series in which the function survives removal of the RFL on held-out situations.

---

## 10. Ideas & possible recommendations

These are ideas rather than prescriptions, and most have alternatives; the issue register offers several for each problem. They are listed roughly by how much each would settle.

1. **A pause in revisions.** Freezing both volumes as they are, and revising only after data exist, would give reviewers a fixed target. A lighter alternative is a public changelog that separates corrections from new claims.
2. **One preregistered experiment.** Here is a concrete version, sized for about three months and one or two engineers. A two-arm version (B0 against T) would be a cheaper first step, though it could not separate the Core from the epistemic layer.
   - **Environments.** A generator of diagnosis families that extends D/A/S to k components and m probes. It includes costs, unreliable channels, delayed readings, and a hidden cause X that mimics a known cause on standard probes. Each structure gets three surface skins (equipment, a software service, a laboratory assay) to test transfer under a preregistered `StructuralSimilarityProfile`. One external benchmark (BoxingGym, or a subset of DiscoveryWorld) would add comparability.
   - **Arms,** all on the same model, tools, and matched token and call budget:
     - **B0:** a strong agent with ReAct-style tool use, Reflexion-style lessons and persistent memory.
     - **B1:** B0 plus only the Volume II epistemic layer (typed status, provenance, forbidden promotions, verification debt, transactional revision). This is close to the strong null Volume I already names (A.4), which Volume II's own control arm omits.
     - **T:** B1 plus the Core (basis-insufficiency assessment, required distinction with decision-equivalence grouping, sufficiency judgment, inquiry-method memory).
     - **O:** the exact dynamic-programming oracle where tractable, as a reference; §27.B already prescribes such a controller as "a reference for attainable cost" (Vol. II §27.B, p. 49).
   - **Primary outcomes.** Correct action or justified irresolvability on held-out families; premature-sufficiency rate on the hidden-cause cases; transfer gain on preregistered isomorphic families; rejection of false analogies; cost.
   - **Preregistered decision rule.** T would count as a contribution only if it beats B1 on transfer and premature sufficiency by a preregistered margin, with intervals excluding zero, across at least 30 independent world families. If B1 matches T, the epistemic layer is the contribution and the Core is not.
   - **Registration.** Preregistration on OSF, with the code and logs published.
3. **Mechanisms before the transfer series.** Specifying the transfer mechanism before running the transfer series (§5.3), fixing one gap taxonomy, and giving the Core a committed rule for the open-world case, or declaring model judgment to be the rule there (§5.2f).
4. **A separate normative layer.** Separating the normative Compass from the definition of AR, and presenting the Compass as a regulative ideal or as the author's stated motivation (§§2.3–2.4).
5. **Titles that match the content.** Dropping *Superintelligence Technology (ASI)* and *From the Meaning of Life to ...* from the scientific volumes. Possible titles include *An Architecture for Self-Directed Inquiry in Language-Model Agents* and *Regulating Inquiry in Language-Model Agents: A Testable Architecture*.
6. **A short paper.** A 10–12 page paper covering the problem, the cycle, the epistemic layer, the experiment and its results. Suitable venues include Advances in Cognitive Systems, the AGI conference series, NeurIPS or ICLR workshops on agents or metacognition, and *Cognitive Systems Research*. The philosophy could appear as a separate essay (for example in *Biology & Philosophy* or *Minds and Machines*).
7. **Prior work in the body of the text,** especially Soar, goal-driven autonomy and MIDCA, truth maintenance, Equivalence Class and Decision Region Determination, the Robot Scientist, structure-mapping, active inference, impact measures and corrigibility.
8. **Safety analyses before launch.** The incentive analysis, critical-loss floors, a disposition and containment rule for divergent candidates and an ethics review, all completed before any launch or admission stage (§8).
9. **An editorial pass.** A careful human editorial pass (Appendix A). A short glossary mapping each coined term to its nearest standard term would help most at the front of each volume, not the end.
10. **A response to the issue register** (Appendix C). Each issue quotes the claims it responds to, states what would resolve it and offers several ideas; marking issues resolved, disputed or deferred in the next version would give reviewers a fixed target.

---

## Appendix A: Editorial issues found

These explain much of the difficulty earlier readers reported, and all are cheap to fix. Each is tracked as a minor issue ([MIN-01](docs/audit/MIN-01-duplicate-paragraphs.md) to [MIN-20](docs/audit/MIN-20-append-only-vs-retention.md)) with full locations.

- **Near-duplicate paragraphs in Volume I.** About two dozen paragraphs appear twice in slightly different wording; an automated similarity check at a strict threshold confirms eleven ([MIN-01](docs/audit/MIN-01-duplicate-paragraphs.md)). Examples: the Abstract (the technological hypothesis twice); the Chapter 5 opening and its priority paragraph; the §7.1 opening and the hunter example; the tail of the Chapter 8 conclusion; §9.3; §11.1; §§12.3–12.4 (choosing an investigative approach; competing models); §12.5; §13.3 (procedural plasticity; the revision process); §13.4; Chapter 15 (the limits of ethics; "after the Compass appears", p. 73); the Chapter 16 opening and its map of scientific levels; Chapter 17 (coordinated autonomy; civilization). The same check found none in Volume II.
- **Truncated sentences** in Volume I: Chapter 18 ("This intermediate state", p. 81); §12.3 ("direct", p. 54); §13.4 ("It is the influence of an acquired ground", p. 66); the Conclusion ("can a continuing Reason make internal renewal", p. 90).
- **Numbering and cross-references.** The six obligations of §12.8 are printed as items 6–11, the conditions of A.3 as 12–18, the tests of A.4 as 19–55, and the references of A.5 as 56–84. Cross-references such as "items 2, 20, 23, 26, and 31" (A.4, p. 100) and "A.4 No. 28" (A.5, p. 105, for current-state integration) do not fit the printed numbering; all of them resolve if the printed number is reduced by 18 up to printed No. 37 and by 20 from No. 40 on, which suggests they predate the insertion of two tests ([MIN-04](docs/audit/MIN-04-broken-cross-references.md)). Volume II §33.A.2 cites "fundamental §11.8" (p. 103), which does not exist; §12.8 was probably meant.
- **An untranslated abbreviation.** "KSR", presumably the Russian abbreviation for the RFL, appears throughout Volume II and in Volume I §20.1.2. There is also a typo, `no_krs_status` (Vol. II §31.0).
- **References.** Russell and Wefald (1991) appears twice (A.5 items 58 and 82), and "Littman, L. M." (A.5, item 57, p. 100) should read *Littman, M. L.*
- **Doubled headings** in Volume I: "CONTENTS CONTENTS" (p. 9), "KEY DEFINITIONS OF THE MODEL KEY DEFINITIONS OF THE MODEL" (p. 11), "OPEN RESEARCH DIRECTIONS OPEN RESEARCH DIRECTIONS" (p. 91).
- **Code listings lose their indentation** in the PDF. Publish them as files in a repository.
- **Contents pages disagree with headings:** 20 of 82 entries in Volume II's contents word the section differently, several with a different key term ("admission" against "Authorization", "Modeling Environment" against "Modeling Workspace") ([MIN-11](docs/audit/MIN-11-contents-vs-headings.md)).
- **Layout artefacts, notation and terminology:** raw diagram source, stray Markdown, flattened tables, colliding one-letter symbols, and terms whose name and capitalization drift ([MIN-13](docs/audit/MIN-13-symbol-collisions.md) to [MIN-16](docs/audit/MIN-16-undefined-abbreviations.md)).

## Appendix B: What I verified and how

- **Full reading** of both English PDFs, from text extracted with `pdftotext`. Working notes are in `notes/reading-notes.md`.
- **Section-by-section audit.** Five independent readers covered every page of both volumes (front matter and Chapters 1–10; Chapters 11–20 and Appendix A; front matter and Chapters 21–26; Chapters 27–30; Chapters 31–34 and the appendices), looking for internal contradictions, definitional drift, formal errors, untestable claims, safety-relevant design choices and editorial defects. Their 217 raw findings are kept unedited in `notes/audit-raw/`, and all 817 quoted fragments in them match the texts verbatim (`scripts/check_raw_quotes.py`). `notes/audit-raw/TRIAGE.md` maps every raw finding to the register issue that acknowledges it.
- **Adversarial checks on this review.** A model from a different vendor fact-checked 119 of the review's claims against the texts (94 confirmed; the 2 wrong and 21 imprecise were corrected), and a separate pass argued the author's side against each criticism; where the text already did what the review asked, the review now says so.
- **Publication history** from the Zenodo REST API. The Volume I concept record (17957561) holds 38 records, created between 16 December 2025 and 9 October 2026: 19 distinct revisions of the main text and seven spin-off documents (`notes/zenodo-history.md`). The record labelled v1.4r carries a publication date of 10 January 2025 but was created on 10 January 2026. Records from 31 August 2026 onward, including both reviewed volumes, are licensed CC BY-NC 4.0; the earlier 30 were CC BY-NC-ND 4.0. The Volume II concept record (22975036) has two versions, v2.4 and v3.5. Volume III, *Civilization of Reason*, v1.8 (26 September 2026), was not reviewed.
- **References.** Every entry in both volumes' bibliographies (29 in Vol. I A.5, 7 in Vol. II) was checked against the published record: all exist, every arXiv ID and DOI resolves to the printed work, and the defects are one duplicate, one transposed pair of initials and one incomplete entry ([MIN-06](docs/audit/MIN-06-bibliography-errors.md); `notes/audit-raw/R1-volume-references.md`). This review's own reference list was checked the same way, its seven incomplete entries corrected, and 36 works the text names but had not listed were added (`notes/audit-raw/R2a-review-references.md`, `R2b-review-references.md`).
- **Code.** Both Volume II listings were restored to valid indentation (`repro/v0_lower_loop.py`, `repro/diagnostic_cycle.py`); `scripts/check_listings.py` confirms they match the printed code line by line up to whitespace, and `make verify` runs them and fails if any number quoted in this review no longer matches their output. Results are in §5.4.
- **Prior-art coverage.** I searched both texts for the precedents discussed in §6. Volume I contains no mention of Soar, ACT-R, truth maintenance, Dewey, Peirce, Kant, Hintikka, Stanovich, Dennett, blackboard architectures, the Robot Scientist, BACON, submodular test selection, shutdown or off-switch incentives, impact measures, prompt injection, or LeCun's architecture. Volume II names Soar, ACT-R, LIDA, Generative Agents, Reflexion, Voyager and MemGPT only in §34.A and its reference list, and does not mention active inference. Neither volume mentions belief revision or model-based diagnosis by name.
- **Near-duplicate paragraphs** were detected with a sliding-window `difflib` comparison (`repro/dup_paragraphs.py`).

## Appendix C: Issue register

Each issue has a standalone file in [`docs/audit/`](docs/audit/README.md) that quotes the claims under review with volume, section and page, then gives the finding, evidence, ideas and possible recommendations, and a resolution criterion; each is mirrored by a GitHub issue with the same ID. The section references in parentheses point back into this review.

**Major (8)**

- [MAJ-01](docs/audit/MAJ-01-no-comparative-evidence.md) No comparative evidence yet for the central hypothesis (§5.2(a), §7, §9)
- [MAJ-02](docs/audit/MAJ-02-asi-framing-overclaims.md) The titles promise ASI technology; the content gives no path to ASI (§4.3, §7, §10.5)
- [MAJ-03](docs/audit/MAJ-03-decision-rule-closed-world.md) The Core's only committed decision rule covers closed, fully specified problems (§5.2(f), §5.3)
- [MAJ-04](docs/audit/MAJ-04-no-transfer-mechanism.md) No mechanism that produces transfer of corrections and inquiry methods (§5.3, §7)
- [MAJ-05](docs/audit/MAJ-05-formation-experiment.md) The formation experiment cannot yet attribute internalization to the RFL (§4.2(a), §7)
- [MAJ-06](docs/audit/MAJ-06-incentive-analysis.md) No design-level analysis of the incentives the architecture creates (§8)
- [MAJ-07](docs/audit/MAJ-07-prior-work-missing.md) The closest prior work is missing from the chapters (§6, §6.1, §7, Appendix B)
- [MAJ-08](docs/audit/MAJ-08-value-sum-compensatory.md) The value sum is compensatory and risk-neutral, and the critical-loss safeguard is undefined (§4.2(d), §8)

**Medium (38)**

- [MED-01](docs/audit/MED-01-near-analytic-necessities.md) The model's necessities are mostly near-analytic, and its two empirical ones overreach (§2.2)
- [MED-02](docs/audit/MED-02-compass-not-load-bearing.md) The Compass's derivation does no work in the engineering and faces the is-ought gap (§2.3, §9)
- [MED-03](docs/audit/MED-03-reason-overloaded.md) "Reason" names both a functional profile and a normative orientation (§2.4, §3)
- [MED-04](docs/audit/MED-04-consciousness-terminology.md) "Consciousness" and "causal" carry meanings that invite misreading (§2.5)
- [MED-05](docs/audit/MED-05-roles-not-kinds.md) Intelligence and Reason are roles, not kinds, and the boundary belongs across episodes (§3)
- [MED-06](docs/audit/MED-06-semantic-bridge-error-model.md) The language-to-structure bridge has no measured error model (§4.2(b))
- [MED-07](docs/audit/MED-07-own-worldview-scope.md) Inherited ontology cannot yet be told apart from an "own" Worldview (§4.2(c))
- [MED-08](docs/audit/MED-08-designer-chosen-values.md) Initial values are designer-chosen, so cultivation tests calibration rather than value formation (§4.2(d))
- [MED-09](docs/audit/MED-09-ceiling-risk.md) The first environment risks a ceiling effect, and no external benchmark is planned (§5.2(b), §10.2)
- [MED-10](docs/audit/MED-10-process-vs-outcome-metrics.md) Process-conformance metrics are not separated from outcome metrics (§5.2(c))
- [MED-11](docs/audit/MED-11-protocol-not-preregistration-ready.md) The first series has the right slots but no preregistered instance (§5.2(a), §10.2)
- [MED-12](docs/audit/MED-12-failure-condition-qualitative.md) The failure condition for the Core is stated only qualitatively (§5.2(d), §9, §10.2)
- [MED-13](docs/audit/MED-13-stopping-rule-myopic.md) The one-step stopping test recurs where §28.D says it fails (§5.2(f))
- [MED-14](docs/audit/MED-14-active-inference-engagement.md) Active inference, the closest formal competitor, is engaged only in an appendix (§6.1)
- [MED-15](docs/audit/MED-15-version-churn.md) The text is revised faster than evidence accumulates (§7, §9, §10.1)
- [MED-16](docs/audit/MED-16-moral-status-ethics-review.md) Moral status is raised, but rollback, branching and destruction of candidates have no ethics procedure (§8)
- [MED-17](docs/audit/MED-17-governance-transfer.md) Competence mandates lack an issuer, auditor and revocation path, and their aggregate effect is unanalysed (§8)
- [MED-18](docs/audit/MED-18-corrigibility-sense.md) "Corrigibility" means correctability, not deference to an operator (§8)
- [MED-19](docs/audit/MED-19-model-filled-significance.md) Significance has no measure, and its model-filled fields are scored only through outcomes (§5.3)
- [MED-20](docs/audit/MED-20-readability.md) Coined vocabulary and length are the main barrier to review (§7, §10.9, Appendix A)
- [MED-21](docs/audit/MED-21-compass-two-criteria-grounding.md) The Compass has two non-equivalent top-level criteria, and its grounding clause is analytic or false (§2.3)
- [MED-22](docs/audit/MED-22-gap-taxonomies.md) Unreconciled taxonomies of gap type (§5.3)
- [MED-23](docs/audit/MED-23-historical-materials-unpublished.md) The pilot log, task packages and AI priority audits are cited but not published (§6, §7)
- [MED-24](docs/audit/MED-24-metric-definitions.md) Many metrics lack formulas, denominators and thresholds (§5.2(c))
- [MED-25](docs/audit/MED-25-core-ablation-capability-sweep.md) No defined ablation of the Core when one model plays both roles, and no capability sweep (§3, §5.2(f))
- [MED-26](docs/audit/MED-26-operational-core-formulas.md) The Operational Core formulas are incomplete and inconsistent with Vol II (§2.1, §5.2(f))
- [MED-27](docs/audit/MED-27-compass-decompositions.md) Three operational decompositions of the Compass coexist without a mapping (§2.3)
- [MED-28](docs/audit/MED-28-epistemic-gate-uncomputable.md) The epistemic gate and EpistemicMargin cannot be computed (§8)
- [MED-29](docs/audit/MED-29-vocabularies-disagree.md) Status vocabularies, enumerations and outcome classes disagree across sections (§5.2(e))
- [MED-30](docs/audit/MED-30-safe-mode-only-through-drift.md) The mode state machine reaches SAFE_MODE only through DRIFT (§8)
- [MED-31](docs/audit/MED-31-authorization-contract-override-and-delay.md) The authorization contract lets the external gate override internal refusal and delays restrictions (§8)
- [MED-32](docs/audit/MED-32-override-criterion-no-adjudicator.md) The AR override criterion and the licence for irreversible loss lack an adjudicator (§8)
- [MED-33](docs/audit/MED-33-cumulative-drift-and-entrenchment.md) Cumulative drift of criteria is unbounded, and a persistent AR has no guard against entrenchment (§4.3, §8)
- [MED-34](docs/audit/MED-34-component-controls-lack-baselines.md) Component controls lack baselines, outcomes and degenerate-policy checks (§5.2(a))
- [MED-35](docs/audit/MED-35-load-bearing-terms-defined-late-or-twice.md) Load-bearing terms are defined late, inconsistently or not at all (§2.1, Appendix A)
- [MED-36](docs/audit/MED-36-revision-ladder-single-locus.md) The revision ladder assumes a single causal locus, and its escalation rules conflict (§7)
- [MED-37](docs/audit/MED-37-no-containment-for-divergent-candidates.md) No disposition rule, and only partial containment, for candidates that diverge from the Compass (§8)
- [MED-38](docs/audit/MED-38-failure-catalogue-not-a-detector.md) The failure catalogue cannot be applied as a detector (§8)

**Minor (20)**

- [MIN-01](docs/audit/MIN-01-duplicate-paragraphs.md) Near-duplicate paragraphs in Volume I (Appendix A)
- [MIN-02](docs/audit/MIN-02-truncated-sentences.md) Truncated sentences in Volume I (Appendix A)
- [MIN-03](docs/audit/MIN-03-list-numbering.md) Lists are numbered across sections or restart mid-list (Appendix A)
- [MIN-04](docs/audit/MIN-04-broken-cross-references.md) Cross-references that do not resolve (Appendix A)
- [MIN-05](docs/audit/MIN-05-untranslated-ksr.md) Untranslated abbreviation "KSR" and inconsistent RFL mode names (Appendix A)
- [MIN-06](docs/audit/MIN-06-bibliography-errors.md) Bibliography errors and incomplete entries (Appendix A, Appendix B)
- [MIN-07](docs/audit/MIN-07-doubled-headings.md) Headings printed twice and lists collapsed (Appendix A)
- [MIN-08](docs/audit/MIN-08-code-listings.md) The printed code listings cannot be run as printed, and their checks are weaker than described (§5.4, Appendix A)
- [MIN-09](docs/audit/MIN-09-inconsistent-titles.md) Each volume carries different titles in the PDF, on Zenodo and in the author's references (Header, §10.5)
- [MIN-10](docs/audit/MIN-10-tool-disclosure.md) No statement of the tools used for drafting, translation and typesetting (Appendix B)
- [MIN-11](docs/audit/MIN-11-contents-vs-headings.md) Contents pages disagree with the headings they list (Appendix A)
- [MIN-12](docs/audit/MIN-12-orphan-records-no-slice.md) Many record types are never used, and no minimal component slice is named (§5.2(e), §10)
- [MIN-13](docs/audit/MIN-13-symbol-collisions.md) Symbols collide across formulas, and the formulas are not typeset (Appendix A)
- [MIN-14](docs/audit/MIN-14-layout-artefacts.md) Layout artefacts: raw diagram source, stray rules, leaked markup and flattened tables (Appendix A)
- [MIN-15](docs/audit/MIN-15-term-drift.md) Defined terms change name and capitalization (Appendix A)
- [MIN-16](docs/audit/MIN-16-undefined-abbreviations.md) Abbreviations and names are used without definition (Appendix A)
- [MIN-17](docs/audit/MIN-17-pseudocode-and-parameters.md) Defects in pseudocode, parameters and the reproducibility rule (§5.4)
- [MIN-18](docs/audit/MIN-18-uncited-methods.md) Borrowed methods and claims lack citations (§6)
- [MIN-19](docs/audit/MIN-19-outlook-without-tests.md) Outlook sections present hypotheses without tests (§9)
- [MIN-20](docs/audit/MIN-20-append-only-vs-retention.md) The log is called append-only, but a retention policy allows deletion (Appendix A)

## References

- Aamodt, A., & Plaza, E. (1994). Case-based reasoning: Foundational issues, methodological variations, and system approaches. *AI Communications*, 7(1), 39–59.
- Alchourrón, C. E., Gärdenfors, P., & Makinson, D. (1985). On the logic of theory change: Partial meet contraction and revision functions. *Journal of Symbolic Logic*, 50(2), 510–530.
- Anderson, J. R., Bothell, D., Byrne, M. D., Douglass, S., Lebiere, C., & Qin, Y. (2004). An integrated theory of the mind. *Psychological Review*, 111(4), 1036–1060.
- ARC Prize Foundation. (2026). ARC-AGI-3: A new challenge for frontier agentic intelligence. arXiv:2603.24621.
- Arrow, K. J., & Fisher, A. C. (1974). Environmental preservation, uncertainty, and irreversibility. *Quarterly Journal of Economics*, 88(2), 312–319.
- Ashby, W. R. (1956). *An Introduction to Cybernetics*. Chapman & Hall.
- Bratman, M. E. (1987). *Intention, Plans, and Practical Reason*. Harvard University Press.
- Butlin, P., et al. (2023). Consciousness in artificial intelligence: Insights from the science of consciousness. arXiv:2308.08708.
- Conant, R. C., & Ashby, W. R. (1970). Every good regulator of a system must be a model of that system. *International Journal of Systems Science*, 1(2), 89–97.
- Conway Morris, S. (2003). *Life's Solution: Inevitable Humans in a Lonely Universe*. Cambridge University Press.
- Cox, M. T., et al. (2016). MIDCA: A metacognitive, integrated dual-cycle architecture for self-regulated autonomy. *AAAI-16*.
- de Kleer, J. (1986). An assumption-based TMS. *Artificial Intelligence*, 28(2), 127–162.
- de Kleer, J., & Williams, B. C. (1987). Diagnosing multiple faults. *Artificial Intelligence*, 32(1), 97–130.
- Debenedetti, E., et al. (2025). Defeating prompt injections by design (CaMeL). arXiv:2503.18813.
- Dehaene, S., & Changeux, J.-P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron*, 70(2), 200–227.
- Dennett, D. C. (1995). *Darwin's Dangerous Idea: Evolution and the Meanings of Life*. Simon & Schuster.
- Dewey, J. (1938). *Logic: The Theory of Inquiry*. Henry Holt.
- Doyle, J. (1979). A truth maintenance system. *Artificial Intelligence*, 12(3), 231–272.
- Duan, Y., et al. (2026). The last AI built by humans: Toward genuine recursive self-improvement. arXiv:2609.11873.
- Elicit. (2026). *Elicit: The AI research assistant* [Computer software]. https://elicit.com
- Endsley, M. R. (1995). Toward a theory of situation awareness in dynamic systems. *Human Factors*, 37(1), 32–64.
- Erman, L. D., Hayes-Roth, F., Lesser, V. R., & Reddy, D. R. (1980). The Hearsay-II speech-understanding system: Integrating knowledge to resolve uncertainty. *ACM Computing Surveys*, 12(2), 213–253.
- Falkenhainer, B., Forbus, K. D., & Gentner, D. (1989). The structure-mapping engine: Algorithm and examples. *Artificial Intelligence*, 41(1), 1–63.
- Foster, E. D., & Deardorff, A. (2017). Open Science Framework (OSF). *Journal of the Medical Library Association*, 105(2), 203–206.
- Franklin, S., Madl, T., D'Mello, S., & Snaider, J. (2014). LIDA: A systems-level architecture for cognition, emotion, and learning. *IEEE Transactions on Autonomous Mental Development*, 6(1), 19–41.
- Friston, K., Da Costa, L., Hafner, D., Hesp, C., & Parr, T. (2021). Sophisticated inference. *Neural Computation*, 33(3), 713–763.
- Friston, K., Parr, T., & Zeidman, P. (2018). Bayesian model reduction. arXiv:1805.07092.
- Gandhi, K., et al. (2025). BoxingGym: Benchmarking progress in automated experimental design and model discovery. arXiv:2501.01540.
- Gentner, D. (1983). Structure-mapping: A theoretical framework for analogy. *Cognitive Science*, 7(2), 155–170.
- Gershman, S. J., Blei, D. M., & Niv, Y. (2010). Context, learning, and extinction. *Psychological Review*, 117(1), 197–209.
- Golovin, D., Krause, A., & Ray, D. (2010). Near-optimal Bayesian active learning with noisy observations. *Advances in Neural Information Processing Systems 23* (NIPS 2010), 766–774.
- Gould, S. J. (1996). *Full House: The Spread of Excellence from Plato to Darwin*. Harmony Books.
- Greenblatt, R., et al. (2024a). Alignment faking in large language models. arXiv:2412.14093.
- Greenblatt, R., Shlegeris, B., Sachan, K., & Roger, F. (2024b). AI control: Improving safety despite intentional subversion. *Proceedings of the 41st International Conference on Machine Learning* (PMLR 235), 16295–16336.
- Greshake, K., et al. (2023). Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection. *AISec*.
- Hadfield-Menell, D., Dragan, A., Abbeel, P., & Russell, S. (2017). The off-switch game. *IJCAI*.
- Hayes-Roth, B. (1985). A blackboard architecture for control. *Artificial Intelligence*, 26(3), 251–321.
- Heins, C., et al. (2022). pymdp: A Python library for active inference in discrete state spaces. *Journal of Open Source Software*, 7(73), 4098.
- Hesp, C., et al. (2021). Deeply felt affect: The emergence of valence in deep active inference. *Neural Computation*, 33(2), 398–446.
- Hintikka, J. (1999). *Inquiry as Inquiry: A Logic of Scientific Discovery*. Kluwer.
- Hou, X., et al. (2026). Learn like humans: Use meta-cognitive reflection for efficient self-improvement (MARS). arXiv:2601.11974.
- Howard, R. A. (1966). Information value theory. *IEEE Transactions on Systems Science and Cybernetics*, 2(1), 22–26.
- Hyafil, L., & Rivest, R. L. (1976). Constructing optimal binary decision trees is NP-complete. *Information Processing Letters*, 5(1), 15–17.
- Jansen, P., et al. (2024). DiscoveryWorld: A virtual environment for developing and evaluating automated scientific discovery agents. *NeurIPS 2024 Datasets and Benchmarks Track*. arXiv:2406.06769.
- Javdani, S., et al. (2014). Near optimal Bayesian active learning for decision making. *AISTATS*.
- Johnson, M. K., & Raye, C. L. (1981). Reality monitoring. *Psychological Review*, 88(1), 67–85.
- Kaelbling, L. P., Littman, M. L., & Cassandra, A. R. (1998). Planning and acting in partially observable stochastic domains. *Artificial Intelligence*, 101(1–2), 99–134.
- Kant, I. (1781/1787). *Critique of Pure Reason*, Transcendental Dialectic, Appendix: on the regulative use of the ideas of pure reason.
- Keeney, R. L., & Raiffa, H. (1976). *Decisions with Multiple Objectives: Preferences and Value Tradeoffs*. Wiley.
- King, R. D., et al. (2004). Functional genomic hypothesis generation and experimentation by a robot scientist. *Nature*, 427, 247–252.
- King, R. D., et al. (2009). The automation of science. *Science*, 324(5923), 85–89.
- Klyubin, A. S., Polani, D., & Nehaniv, C. L. (2005). Empowerment: A universal agent-centric measure of control. *IEEE CEC*.
- Kolodner, J. (1993). *Case-Based Reasoning*. Morgan Kaufmann.
- Krakovna, V., et al. (2019). Penalizing side effects using stepwise relative reachability. arXiv:1806.01186.
- Kulveit, J., et al. (2025). Gradual disempowerment: Systemic existential risks from incremental AI development. arXiv:2501.16946.
- Laird, J. E., Newell, A., & Rosenbloom, P. S. (1987). SOAR: An architecture for general intelligence. *Artificial Intelligence*, 33(1), 1–64.
- Lakatos, I. (1970). Falsification and the methodology of scientific research programmes. In I. Lakatos & A. Musgrave (Eds.), *Criticism and the Growth of Knowledge* (pp. 91–196). Cambridge University Press.
- Langley, P., Simon, H. A., Bradshaw, G. L., & Zytkow, J. M. (1987). *Scientific Discovery: Computational Explorations of the Creative Processes*. MIT Press.
- Lau, H. (2019). Consciousness, metacognition, and perceptual reality monitoring. PsyArXiv.
- LeCun, Y. (2022). A path towards autonomous machine intelligence. OpenReview.
- Lenat, D. B. (1995). CYC: A large-scale investment in knowledge infrastructure. *Communications of the ACM*, 38(11), 33–38.
- Leopold, A. (1949). *A Sand County Almanac, and Sketches Here and There*. Oxford University Press.
- Lewis, P., et al. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *NeurIPS 2020*. arXiv:2005.11401.
- Liu, T., & van der Schaar, M. (2025). Position: Truly self-improving agents require intrinsic metacognitive learning. *ICML 2025* (PMLR 267). arXiv:2506.05109.
- Long, R., Sebo, J., et al. (2024). Taking AI welfare seriously. arXiv:2411.00986.
- Lu, C., et al. (2024). The AI Scientist: Towards fully automated open-ended scientific discovery. arXiv:2408.06292.
- MacAskill, W., Bykvist, K., & Ord, T. (2020). *Moral Uncertainty*. Oxford University Press.
- Metzinger, T. (2003). *Being No One: The Self-Model Theory of Subjectivity*. MIT Press.
- Mitchener, L., et al. (2025). Kosmos: An AI scientist for autonomous discovery. arXiv:2511.02824.
- Molineaux, M., Klenk, M., & Aha, D. W. (2010). Goal-driven autonomy in a Navy strategy simulation. *AAAI*.
- Morris, M. R., et al. (2024). Position: Levels of AGI for operationalizing progress on the path to AGI. *ICML 2024* (PMLR 235). arXiv:2311.02462.
- Muñoz-Avila, H., Jaidee, U., Aha, D. W., & Carter, E. (2010). Goal-driven autonomy with case-based reasoning. *ICCBR*.
- Omohundro, S. M. (2008). The basic AI drives. *AGI-08*.
- Packer, C., et al. (2023). MemGPT: Towards LLMs as operating systems. arXiv:2310.08560.
- Park, J. S., et al. (2023). Generative agents: Interactive simulacra of human behavior. *UIST '23*. arXiv:2304.03442.
- Peirce, C. S. (1877). The fixation of belief. *Popular Science Monthly*, 12, 1–15.
- Rao, A. S., & Georgeff, M. P. (1995). BDI agents: From theory to practice. *ICMAS*.
- Reiter, R. (1987). A theory of diagnosis from first principles. *Artificial Intelligence*, 32(1), 57–95.
- Russell, S., & Wefald, E. (1991). Principles of metareasoning. *Artificial Intelligence*, 49, 361–395.
- Sandved-Smith, L., et al. (2021). Towards a computational phenomenology of mental action: Modelling meta-awareness and attentional control with deep parametric active inference. *Neuroscience of Consciousness*, 2021(1), niab018.
- Schmidhuber, J. (2007). Gödel machines: Fully self-referential optimal universal self-improvers. In B. Goertzel & C. Pennachin (Eds.), *Artificial General Intelligence* (pp. 199–226). Springer.
- Seth, A. K. (2013). Interoceptive inference, emotion, and the embodied self. *Trends in Cognitive Sciences*, 17(11), 565–573.
- Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., & Yao, S. (2023). Reflexion: Language agents with verbal reinforcement learning. *NeurIPS 2023*. arXiv:2303.11366.
- Smith, R., Schwartenbeck, P., Parr, T., & Friston, K. J. (2020). An active inference approach to modeling structure learning: Concept learning as an example case. *Frontiers in Computational Neuroscience*, 14, 41.
- Soares, N., Fallenstein, B., Yudkowsky, E., & Armstrong, S. (2015). Corrigibility. *AAAI Workshop on AI and Ethics*.
- Stanovich, K. E. (2009). *What Intelligence Tests Miss: The Psychology of Rational Thought*. Yale University Press.
- Sumers, T. R., Yao, S., Narasimhan, K., & Griffiths, T. L. (2024). Cognitive architectures for language agents. *Transactions on Machine Learning Research*. arXiv:2309.02427.
- Teilhard de Chardin, P. (1959). *The Phenomenon of Man* (B. Wall, Trans.). Harper & Brothers.
- Turner, A. M., Hadfield-Menell, D., & Tadepalli, P. (2020). Conservative agency via attainable utility preservation. *AIES*.
- Turner, A. M., Smith, L., Shah, R., Critch, A., & Tadepalli, P. (2021). Optimal policies tend to seek power. *Advances in Neural Information Processing Systems 34* (NeurIPS 2021).
- Valiente, R., & Pilly, P. K. (2024). Competence-aware AI agents with metacognition for unknown situations and environments (MUSE). arXiv:2411.13537.
- Vernadsky, V. I. (1945). The biosphere and the noosphere. *American Scientist*, 33(1), 1–12.
- Wang, G., et al. (2024). Voyager: An open-ended embodied agent with large language models. *Transactions on Machine Learning Research*. arXiv:2305.16291.
- Wang, R., Jansen, P., Côté, M.-A., & Ammanabrolu, P. (2022). ScienceWorld: Is your agent smarter than a 5th grader? *EMNLP 2022*, 11279–11298.
- Yao, S., et al. (2023). ReAct: Synergizing reasoning and acting in language models. *ICLR 2023*. arXiv:2210.03629.
- Zhang, J., Hu, S., Lu, C., Lange, R., & Clune, J. (2025). Darwin Gödel Machine: Open-ended evolution of self-improving agents. arXiv:2505.22954.
- Zhao, A., et al. (2024). ExpeL: LLM agents are experiential learners. *AAAI 2024*, 38(17), 19632–19642. arXiv:2308.10144.
