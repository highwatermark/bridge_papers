---
title: "Nominating computational correspondences across disconnected literatures: a three-space detector that does not beat its nulls, and one adjudicated case"
status: "Draft v2 — Paper B. Not submission-ready; see submission_checklist.md"
authors: "[AUTHOR NAMES — TO FILL]"
affiliations: "[AFFILIATIONS — TO FILL]"
corresponding: "[CORRESPONDING AUTHOR + EMAIL — TO FILL]"
---

## Abstract

Researchers in separate fields sometimes build models with the same computational structure but never cite each other. We ask whether such correspondences can be *nominated* automatically and then *adjudicated* by reading. The detector scores each cross-literature pair of papers in three spaces: a six-role computational signature (state, representation, objective, transition, search, feedback) taken from a fixed lexicon; semantic similarity from sentence embeddings; and citation overlap. It flags pairs that are high in the first space, low in the second, and share no references. We applied it to 522 papers: 404 on machine learning for evolution and 118 on biological state transitions. All sixteen previously reported summary numbers reproduce exactly from a frozen specification. **The aggregate claims do not survive null models.** Cross-literature role similarity (mean 0.710) is *lower* than within-literature similarity (0.734, 0.762). The flagged-pair rate (6.47%) falls at or below a vocabulary-shuffle null (10.2%) and a role-permutation null (7.7%). Under a threshold rule fixed before re-analysis it equals chance (6.16% vs 5.97%, *p* = 0.32). We then adjudicated one pair by full-text reading: a latent-space model of protein fitness (Ding et al. 2019) and a Hopfield attractor model of disease progression (Taherian Fard & Ragan 2017). The detector did not nominate this pair. Under an explicit rejection rule, the two models fill two of six roles on both sides — a state space and a scalar field over it — and fill three others complementarily. They **share a six-role computational template only in part, and diverge as mathematical objects**: on a synthetic capacity test, nonparametric fields recover four basins while quadratic energies recover none. We report the detector as a candidate generator with no measured precision. We also release a blind 150-pair annotation kit and a pre-registered protocol for the experiment that would test unification on real data.

## 1. Introduction

Swanson's fish-oil/Raynaud's inference showed that two literatures can jointly imply a result neither states, provided nobody reads both (Swanson 1986). Literature-based discovery has since automated the *connecting term* (Sourati et al. 2023, for a recent human-aware formulation). Analogy research asks a harder question: whether two systems share *relational structure* rather than surface features (Gentner 1983), and whether that structure can be mined from text at scale (Hope et al. 2017).

We ask the structural question for quantitative models. Molecular-evolution and systems-biology groups both write models that assign a scalar to configurations of a system and read biological outcomes off its extrema. In evolution this is the fitness landscape, now commonly fitted with learned representations (Riesselman et al. 2018; Frazer et al. 2021; Meier et al. 2021; Notin et al. 2023). In systems biology it is Waddington's epigenetic landscape (Waddington, 1957; 2014 reissue), formalised as attractors of gene-regulatory dynamics (Huang et al. 2005; Huang et al. 2009; Wang et al. 2011) or estimated from single-cell data (La Manno et al. 2018; Schiebinger et al. 2019; Yeo et al. 2021; Qiu et al. 2022). The two communities rarely cite each other.

Two claims have to be kept apart:

- **Detection claim.** A procedure can surface pairs of papers that share computational structure more often than chance.
- **Correspondence claim.** A specific pair shares that structure, at a stated level of equivalence.

The first is statistical and needs nulls and a precision estimate. The second is a reading exercise and needs full texts and a rule for what counts as a match. An earlier draft of this work ran the two together: it reported aggregate rates as evidence of shared structure and described the worked example as detector output. Here we separate them. **The detector nominates pairs. Reading adjudicates them.**

**Contributions.** (i) A frozen, reproducible specification of a three-space detector, with every reported number regenerated from it (§2, Appendices 1–2). (ii) Null models, stratified controls and a 48-cell sensitivity grid, which together show the detector's aggregate rates are not above chance (§3). (iii) A full-text adjudication of one pair under a stated rejection rule, with the weak slots named (§4). (iv) A capacity test with fair baselines that locates the mathematical difference in the quadratic family, not in the Hopfield dynamics as such (§5). (v) Negative controls, including a pair the detector gets wrong (§6). (vi) A blind precision-study kit and a pre-registered real-data protocol, neither run (§7, Appendices 3–4).

## 2. Methods

### 2.1 Corpus

Records were retrieved from OpenAlex (Priem et al. 2022) by relevance search: ten evolution-ML queries (200 records each) and eight state-transition queries (100 records each), limited to 2015–2026 and to journal articles. The exact query strings are in `detector_spec.json`. Relevance search is not stable over time, so **the unit of reproducibility is the frozen corpus file, not the queries**. The exact retrieval date is **UNVERIFIED**; it was before 2026-07-04 according to the session log.

The evolution-ML side passed a co-occurrence gate (≥1 evolution term, ≥1 learning term, abstract >120 characters), a keyword-rule paradigm classifier with an off-topic blocklist, and a manual off-topic audit, leaving 404 papers. The state-transition side passed a rule requiring ≥1 environmental-signal term, ≥1 transition term, ≥2 modelling terms and an abstract of >120 characters, leaving 120 papers. Duplicates were removed by OpenAlex work ID. After an 80-character text floor the combined corpus has 522 papers (404 + 118). All are English according to OpenAlex's language field; this was checked afterwards, not used as a filter. Twenty-one records retrieved as articles are now labelled by OpenAlex as conference papers, preprints, reviews or an editorial. They are retained, and the drift is recorded. Classifier code is reproduced verbatim in the specification. The classifier is noisy per paper; we make no per-paper claims from it.

### 2.2 Three spaces

**Primitive (role) space.** Each role has a lexicon containing terms from both literatures (81 terms; Appendix 1). A paper's signature $s\in\mathbb N^6$ counts the *distinct* lexicon terms per role found as lowercase substrings of title + abstract. A role is *expressed* if its count is ≥1. Papers expressing at least 4 of 6 roles form the **rich subset**: 206 papers (39%), giving 135 × 71 = 9,585 cross-literature pairs. Primitive similarity is the cosine of square-root-transformed signatures.

**Concept (semantic) space.** Title + abstract were embedded with `all-MiniLM-L6-v2` (Reimers & Gurevych 2019; Wang et al. 2020): 384 dimensions, unit-normalised, default truncation at 256 word-pieces, pinned model snapshot. Concept similarity is the cosine.

**Citation space.** Jaccard overlap of OpenAlex `referenced_works` lists, re-fetched for all 522 papers (519 have non-empty lists). This is bibliographic coupling (Kessler 1963) normalised by union size.

### 2.3 Flagging rule — original and pre-registered

The **original rule**, as implemented, flagged pairs with primitive similarity ≥0.90 and concept similarity below the 90th percentile (0.396). Both cut points were chosen without justification, and the rule carried **no** citation condition, although the earlier prose described one. We report it with the citation condition added, as the prose intended. The **pre-registered rule** was fixed in this document before the sensitivity grid was computed: primitive ≥ P75 (0.816), concept ≤ P25 (0.187), and Jaccard = 0. The sensitivity grid (§3.3) varies all three thresholds.

### 2.4 Nulls

(1) **Within vs cross:** the primitive-similarity distribution of within-literature pairs from the same rich subset. (2) **Vocabulary shuffle:** the 81 lexicon terms are randomly reassigned to roles, keeping role sizes, and the whole pipeline is recomputed, including the richness gate (200 permutations). (3) **Role permutation:** each state-transition paper's six role counts are permuted independently, keeping each paper's total and the rich subset fixed (200 permutations). This tests whether *which* role a term fills matters. (4) **Stratification** by publication-year gap and by shared venue. The *p*-values are one-sided and empirical, with +1 smoothing.

## 3. Results — detector

### 3.1 Reproduction

All 16 summary numbers reported in earlier drafts reproduce exactly from the frozen specification (`reproducibility_log.csv`). Among them: cross-literature primitive mean 0.710; concept mean 0.259; citation Jaccard mean 0.0002, with 1.9% of pairs sharing any reference; Spearman ρ(primitive, concept) = 0.018 (*p* = 0.08); quadrant counts 109 / 627 / 850 / 7999; and 96 "seed" pairs. One definition changes. The earlier figure of 627 flagged pairs (6.54%) had no citation condition. With the condition it is **620 pairs (6.47%)**.

### 3.2 Nulls: the aggregate signal is not above chance

- **Within vs cross.** Mean primitive similarity is 0.734 within evolution-ML, 0.762 within the state-transition literature, and **0.710 across** them. The fraction of pairs with similarity ≥0.90 is 13.4%, 14.6% and 7.7% respectively. The high absolute value of the cross-literature mean is produced by the richness gate, not by cross-literature affinity (Fig. 1b).
- **Vocabulary shuffle.** The null flagged-pair rate is 10.2% (95% interval 6.4–14.9%). The observed rate of 6.47% is at the bottom of this range (one-sided *p*(null ≤ observed) = 0.040). Because role assignments are arbitrary under this null, the fixed lexicon does not concentrate flagged pairs above chance.
- **Role permutation.** The null rate is 7.7% (6.7–8.8%). The observed rate is below it (*p* = 0.010, Fig. 1c).
- **Year and venue.** The flagged rate is 6.35% for year-matched pairs (|Δ*y*| ≤ 2, *n* = 2915) and 6.52% for mismatched pairs. It is 7.34% for same-venue pairs (*n* = 218) and 6.45% for different-venue pairs. Year-matched pairs share at least one reference more often (3.2%), as expected. Neither stratification changes the flagged rate materially.

![Figure 1]({{artifact:art_85905f6e-f311-4e33-9173-7872c722f010}})

**Figure 1 | The detector's aggregate signal does not exceed its nulls.** **a**, Primitive vs concept similarity for all 9,585 rich cross-literature pairs (grey). Dashed lines: original cut points. Dotted lines: pre-registered cut points. Star: the adjudicated Ding–Fard pair, which falls outside both flagging regions. Open circles: false-friend controls rejected on reading. Diamond: a pair flagged as a false friend by the rule that reads as a plausible match (a detector error; §6). **b**, Primitive-similarity distributions within each literature and across them; cross-literature pairs are *less* similar. **c**, Observed flagged-pair rate (orange line) against 200 vocabulary-shuffle and 200 role-permutation draws.

### 3.3 Sensitivity

The grid crosses six primitive thresholds, four concept thresholds and two citation conditions (48 cells). Each cell has its own role-permutation null (100 draws; `sensitivity_table.csv`). The ratio of observed to null rate ranges from 0.84 to 1.21. 1 of 48 cells reach *p* < 0.05, about what chance predicts. The pre-registered cell flags 590 pairs (6.16%) against a null of 5.97% (ratio 1.03, *p* = 0.32). The cells with the lowest concept threshold show ratios slightly above 1 in every primitive row. This is the only pattern in the grid in the hypothesised direction, and it is not significant after the 48 comparisons.

**Interpretation.** With this lexicon and this corpus, the detector is **not evidence that the two literatures share computational structure more than chance**. It is at most a way to generate candidates for reading. Whether its candidates are better than random candidates is the precision question (§7), and it is unmeasured. We make no claim that any fraction of flagged pairs are genuine correspondences.

## 4. Results — one adjudicated correspondence

### 4.1 How the pair was chosen

The pair was **not** produced by the flagging rule. It was chosen by taking a landmark fitness-landscape paper (Ding et al. 2019) and hand-checking the concept-nearest state-transition papers for landscape content. Its detector scores are primitive 0.841 (P81) and concept 0.432 (P94.7). This places it in the region the original rule labels a *false friend*. It shares no references with the other paper: 0 in common out of 77 and 39, and neither cites the other. We report it as a hand-selected case study, and the adjudication below does not depend on the detector.

### 4.2 The two models, from full text

**Ding et al. 2019.** Sequences $x$ from a multiple sequence alignment are encoded by a variational autoencoder (Kingma & Welling 2013), $z=\phi(x)\sim q_\phi(z\mid x)$, trained on

$$\mathrm{ELBO}(\theta,\phi)=\mathbb E_{q_\phi(z\mid x)}[\log p_\theta(x\mid z)]-\mathrm{KL}\big(q_\phi(z\mid x)\,\|\,p(z)\big),\qquad p(z)=\mathcal N(0,I).\tag{1}$$

A Gaussian process (Rasmussen & Williams 2005) with an RBF kernel is then fitted to measured stability (T50) over the 2-D latent coordinate:

$$J(z)=f(z),\quad f\sim\mathcal{GP}(0,k_{\mathrm{RBF}}).\tag{2}$$

The paper reports 10-fold cross-validated Pearson 0.80 ± 0.06.

**Taherian Fard & Ragan 2017.** Gene-expression patterns $P\in\{-1,+1\}^n$ evolve under a Hopfield network whose weights are Pearson correlations between genes,

$$W_{ij}=\mathrm{PCC}(i,j),\ W_{ii}=0,\qquad P(t{+}1)=\mathrm{sgn}\big(P(t)W\big),\tag{3–4}$$

with Lyapunov energy

$$E[P]=-\tfrac12\,PWP^{\top}.\tag{5}$$

Attractors are local minima of $E$. The landscape is displayed by interpolating $E$ over the first two principal components. A separate $W$ is fitted per disease stage (Parkinson's disease, glioma, colorectal cancer). Hopfield (1982) gives the underlying formalism.

### 4.3 Six-role audit

**Rejection rule (fixed before rating).** A slot is *filled* only if the paper specifies a computable object for that role — an equation, update rule, algorithm, or fitted function that is used to produce a reported result. A slot is *empty* if the only candidate is (a) a verbal interpretation of results, (b) a visualisation device, or (c) the justification for a choice made in another slot. Ratings below are from the full texts (Ding et al. 2019; Taherian Fard & Ragan 2017), not abstracts.

| Role | Ding et al. 2019 — protein fitness | Component or re-description? | Taherian Fard & Ragan 2017 — disease attractors | Component or re-description? |
|---|---|---|---|---|
| **State** $x\in\mathcal S$ | protein sequence, one-hot over MSA columns | **Component** | gene-expression pattern $P$ (network state) | **Component** |
| **Representation** $z=\phi(x)$ | VAE encoder $q_\phi(z\mid x)$, 2-D latent, trained by ELBO | **Component** | none: dynamics run in gene space; PCs used only to draw the landscape | **Empty** (visualisation device, rule b) |
| **Objective** $J$ | GP regression $f(z)$, RBF kernel, fit to T50 stability | **Component** | Lyapunov energy $E[P]=-\tfrac12 PWP^\top$, $W_{ij}=\mathrm{PCC}(i,j)$ | **Component** |
| **Transition** $x_{t+1}=T(x_t,u_t)$ | "mutations move $x$, hence $z$" — no operator defined; mutations are data | **Re-description** (rule a) — *weak slot, flagged* | $P(t{+}1)=\mathrm{sgn}(P(t)W)$ | **Component** |
| **Search / trajectory** $\pi$ | "adaptive walk as ascent on $J$" — no walk implemented; ancestral sequences are *observed* near the latent origin | **Re-description** (rule a) | iterate the update until convergence; "trajectories trace the convergence of samples to their attractors" | **Component** |
| **Feedback** $F$ | "selection pressure" invoked to justify $p(x)$ as a fitness proxy | **Re-description** (rule c) — *weak slot, flagged* | "temporal rewiring": a separate $W$ fitted per disease stage; no in-model update of $W$ | **Re-description** (rule a) — *weak slot, flagged* |

**Tally.** Filled on both sides: **2 of 6** (State, Objective). Filled on one side only: **3** — Representation (Ding), Transition and Search (Fard). Filled on neither: **1** (Feedback).

**What this does to the claim.** The strict Level-2 claim — every role occupied by a real component on both sides — **fails**. What survives is narrower: the two models share the *load-bearing core* of the template (a scalar field $J$ over a state space $\mathcal S$, whose extrema are the biologically meaningful configurations) and fill the remaining slots *complementarily*. Ding supplies a learned representation and a flexible $J$ with no dynamics; Fard supplies explicit dynamics ($T$, $\pi$) with no learned representation and a fixed-capacity $J$. Neither implements feedback.

**The two weak slots, stated in public.**
- *Transition.* A mutation-induced displacement $\Delta z$ and a discrete sign-threshold update are different kinds of operator: the first is a change of the input to a static map; the second is an autonomous dynamical rule. Only the second is a component.
- *Feedback.* Population-level selection and stage-wise re-estimation of $W$ are different kinds of "feedback", and neither paper implements either inside its model. The feedback row is empty on both sides.

**Table 1.** This table replaces Table 1 of the earlier drafts, which listed all six slots as filled on both sides.

### 4.4 Three levels of equivalence

- **Level 1 — shared vocabulary.** Holds, trivially: both papers use "landscape", "state" and "energy/fitness".
- **Level 2 — shared role structure.** **Holds only in part.** The load-bearing core is shared: a state space and a scalar field over it whose extrema are the biologically meaningful configurations. The strict claim that all six roles are filled on both sides fails (2/6). The two models are *complementary*: Ding supplies $\phi$ and a flexible $J$ with no dynamics, and Fard supplies $T$ and $\pi$ with no learned $\phi$.
- **Level 3 — same mathematical object.** **Fails.** Eq. 2 is a nonparametric function class. Eq. 5 is a quadratic form in $P$. With $W_{ii}=0$ the matrix $W$ has zero trace and is therefore indefinite, so on continuous states the energy's only isolated stationary point is a saddle and it has no interior minimum. Section 5 tests whether this difference matters.

The paper's claim is therefore: **the two models share a six-role computational template in part and diverge as mathematical objects.** The claim is narrower than the one in our earlier drafts.

## 5. Capacity test

**Design.** A coupled double-well potential $U(s)=(s_1^2-1)^2+(s_2^2-1)^2-0.6\,s_1s_2$ on $[-1.8,1.8]^2$ has four interior minima by construction. Label-fitting routes receive 220 uniformly sampled states with noisy labels $-U$. The Hopfield route estimates $W$ from samples clustered in two of the four wells, mirroring Fard's use of samples grouped by disease stage. We report Spearman ρ against $U$ after aligning signs, and the count of interior minima.

| Route | ρ vs truth | Interior minima (truth = 4) |
|---|---|---|
| Gaussian process (Ding's route) | 1.000 | 4 |
| RBF interpolation (thin-plate) | 0.998 | 4 |
| Two-layer MLP potential, 5 seeds | 1.000 (seeds [1.0, 1.0, 1.0, 0.999, 1.0]) | 4 |
| **Full quadratic regression on the same labels** | **0.601** | **1** |
| Hopfield energy, continuous relaxation | 0.338 | 0 |
| Hopfield on $\{-1,+1\}^2$ (Fard's actual dynamics) | — | 2 (the two sampled wells) |

**What the test shows.** Any flexible function class recovers the four basins. A quadratic fitted to the *same labels* does not, so the limitation belongs to the quadratic family, not to the Hopfield learning rule or to the amount of data. The test is also **fair to Fard**. On the binary hypercube the model actually uses, the discrete Hopfield dynamics recover exactly the two sampled wells as attractors ($W_{12}$ = 0.97). The "no basins" result applies only to the continuous relaxation used to *draw* the landscape. A Hopfield network with more units, or with dense-associative-memory energies (Amit et al. 1985; Krotov & Hopfield 2016; Ramsauer et al. 2021), can store more attractors. So the difference is between a **quadratic energy over observed genes** and a **learned nonparametric field over a learned representation**, not between "landscape" and "no landscape".

**Sign alignment.** Fitness is maximised and energy minimised. Without aligning signs, the Gaussian-process field correlates at -1.000 with $U$, a spurious reversal. Every comparison above is sign-aligned.

**Limit.** The benchmark is synthetic. It shows a difference in representational capacity between function classes. **It says nothing about which class better describes any real protein or cell.**

![Figure 2]({{artifact:art_f8b3a910-1355-4b03-a29f-4928ed554b09}})

**Figure 2 | Capacity test.** All fields are drawn as potentials (fitness negated); yellow marks low potential. **a**, Ground truth. **b–c**, Flexible fields recover four basins. **d**, A quadratic fitted to the same labels recovers one minimum. **e**, The continuous Hopfield energy is a saddle whose lowest values run to the boundary; white points are the samples from two wells. **f**, On $\{-1,+1\}^2$ the discrete dynamics have exactly the two sampled wells as attractors.

## 6. Negative controls

A procedure that never rejects is not evidence. We chose false-friend candidates under the frozen specification: concept ≥ P90, primitive ≤ P10 and Jaccard = 0 gave 75 pairs, of which 70 have non-overlapping dominant roles. We read four of the eight with the highest concept similarity. The selection was **not blind**: we skipped ranks 3, 4, 6 and 7 because each repeats a state-transition paper already in the set (TENET twice, the LacI repressor paper once) or was passed over for paper diversity (rank 7). All eight are listed, with ranks, in `false_friends_evidence.csv`; the four skipped pairs have not been adjudicated. Earlier drafts reported three controls with primitive similarities from an unreproducible lexicon. Under the frozen specification those three score 0.68, 0.46 and 0.60, and no pair has both papers in the rich subset, so they are withdrawn.

| Pair (evolution-ML ∥ state transition) | Concept (pctile) | Primitive (pctile) | Reading | Verdict |
|---|---|---|---|---|
| GET transcription foundation model ∥ colorectal-metastasis trajectory maps | 0.561 (P99.6) | 0.373 (P1.4) | Static sequence→expression regression vs pseudotime trajectory inference; no $T$, $\pi$ or $F$ in GET | **Reject** |
| ProMEP zero-shot mutation effects ∥ scTIE temporal multiome integration | 0.525 (P99.3) | 0.485 (P8.2) | Both learn embeddings; ProMEP's scalar scores states, scTIE's is a transport cost between time points | **Reject** (one shared slot) |
| Evolutionary velocity with PLMs ∥ phage lysis/lysogeny plasticity | 0.497 (P98.5) | 0.338 (P0.5) | Descriptive flow over sequences vs optimised strategy under an environmental signal | **Reject**, with caveat: both are evolution papers |
| MULTI-evolve (PLM-guided directed evolution) ∥ coevolution-guided LacI repressor engineering | 0.516 (P99.1) | 0.365 (P1.0) | State, representation, objective, transition, search and selection all present on both sides | **Detector error** — plausible Level-2 match |

Three of the four are rejected on reading. The fourth shows the lexicon missing a real correspondence, because "fusion", "compatibility" and "design" are absent from the role terms. This is **one observed false negative** and supports no recall estimate. The controls show that reading can reject pairs the embedding calls similar. They say nothing about the detector's precision.

## 7. What would establish precision (not yet run)

We release a blind annotation sheet of 150 pairs, 50 each from the pre-registered flagged stratum (pool 590), a false-friend stratum (concept ≥ P75 = 0.331, primitive ≤ P25 = 0.623, Jaccard = 0; pool 546) and a low-low baseline stratum (pool 595). Pairs are sampled with a fixed seed, no paper appears more than twice per stratum, and paper order is randomised within each pair. The stratum key is held separately. Appendix 3 gives the codebook, the κ target (≥0.60) and the adjudication rule. The detector counts as informative only if its flagged stratum yields more L2-plausible labels than **both** comparison strata. **No precision number exists yet.**

The correspondence claim also has a decisive test that has not been run: fit one learned field to both fitness labels and state trajectories of a single system (Eq. 9, Appendix 4). The protocol names the result that would refute unification.

## 8. Related work

**Literature-based discovery** links literatures through shared intermediate terms (Swanson 1986) and, more recently, through models of who can read what (Sourati et al. 2023). Our target is a shared *model structure*, not a shared term. **Bibliographic coupling** (Kessler 1963) is the citation space used here. It serves as the disconnection criterion, not as a signal. **Analogy mining** separates relational from surface similarity (Gentner 1983) and has been scaled with learned purpose/mechanism representations (Hope et al. 2017). Our six-role lexicon is a hand-built, domain-specific and much weaker version of that idea, and §3 shows its weakness. **Landscape models:** the fitness side draws on deep generative and language-model fitness predictors (Riesselman et al. 2018; Frazer et al. 2021; Meier et al. 2021; Rives et al. 2021; Notin et al. 2023) and on time-varying landscapes (Mustonen & Lässig 2009). The state-transition side draws on attractor theory (Huang et al. 2005, 2009; Wang et al. 2011) and on single-cell dynamics (La Manno et al. 2018; Schiebinger et al. 2019; Yeo et al. 2021; Qiu et al. 2022). **Energy-based memory models** (Hopfield 1982; Amit et al. 1985; Krotov & Hopfield 2016; Ramsauer et al. 2021) explain why the capacity gap in §5 belongs to the classical quadratic energy and not to energy-based dynamics in general.

## 9. Limitations

1. The role lexicon is hand-built, has 81 terms and matches substrings. It produces keyword collisions and at least one observed false negative.
2. Abstracts are too short to describe most models. A detector working on full text might behave differently; this is untested.
3. The corpus comes from relevance search, so it inherits the search engine's ranking choices. Twenty-one records have changed OpenAlex type since retrieval.
4. Precision is unmeasured and recall is unmeasurable with this design.
5. Only one pair has been adjudicated from full text. That pair was selected by hand, and one author did the reading. Table 1 has not been independently re-rated.
6. The capacity test is synthetic and two-dimensional.
7. Eq. 9 has not been run on real data.

## 10. Conclusion

A three-space detector built from a fixed role lexicon, sentence embeddings and citation overlap does not, on this corpus, flag cross-literature pairs at a rate above chance. Its aggregate rates should not be read as evidence that the literatures share computational structure. Full-text reading of one hand-selected pair gives a narrower and defensible result. A protein fitness-landscape model and a disease attractor model share a state space and a scalar field over it, fill the other roles complementarily, and diverge as mathematical objects, because the attractor model's energy is quadratic. Whether this generalises is the precision study's question, and whether the two can be unified is Eq. 9's.

## Data and code availability

Frozen corpus (`combined_text.csv`), embeddings (`concept_embeddings.npy`), reference lists (`refset_v2.json`), specification (`detector_spec.json`, `detector.py`, `role_lexicon.tsv`), all pair scores (`pair_scores.csv.gz`), null draws, the sensitivity grid, benchmark results and the blind annotation kit accompany this manuscript. **Repository URL: [TO FILL — deposit on Zenodo/OSF before submission].**

## Funding, competing interests, author contributions

[TO FILL]

## References

- Amit et al. (1985). Storing Infinite Numbers of Patterns in a Spin-Glass Model of Neural Networks. *Physical Review Letters*. doi:10.1103/physrevlett.55.1530
- Ding et al. (2019). Deciphering protein evolution and fitness landscapes with latent space models. *Nature Communications*. doi:10.1038/s41467-019-13633-0
- Taherian Fard A, Ragan MA (2017). Modeling the Attractor Landscape of Disease Progression: a Network-Based Approach. *Frontiers in Genetics*. doi:10.3389/fgene.2017.00048
- Frazer et al. (2021). Disease variant prediction with deep generative models of evolutionary data. *Nature*. doi:10.1038/s41586-021-04043-8
- Gentner et al. (1983). Structure‐Mapping: A Theoretical Framework for Analogy*. *Cognitive Science*. doi:10.1207/s15516709cog0702_3
- Hope et al. (2017). Accelerating Innovation Through Analogy Mining. *Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*. doi:10.1145/3097983.3098038
- Hopfield (1982). Neural networks and physical systems with emergent collective computational abilities.. *Proceedings of the National Academy of Sciences*. doi:10.1073/pnas.79.8.2554
- Huang et al. (2005). Cell Fates as High-Dimensional Attractor States of a Complex Gene Regulatory Network. *Physical Review Letters*. doi:10.1103/physrevlett.94.128701
- Huang et al. (2009). Cancer attractors: A systems view of tumors from a gene network dynamics and developmental perspective. *Seminars in Cell and Developmental Biology*. doi:10.1016/j.semcdb.2009.07.003
- Kessler (1963). Bibliographic coupling between scientific papers. *American Documentation*. doi:10.1002/asi.5090140103
- Kingma DP, Welling M (2013). Auto-Encoding Variational Bayes. *UvA-DARE (University of Amsterdam)*. doi:10.48550/arxiv.1312.6114
- Krotov D, Hopfield JJ (2016). Dense Associative Memory for Pattern Recognition. *arXiv (Cornell University)*. doi:10.48550/arxiv.1606.01164
- La Manno et al. (2018). RNA velocity of single cells. *Nature*. doi:10.1038/s41586-018-0414-6
- Meier et al. (2021). Language models enable zero-shot prediction of the effects of mutations on protein function. *bioRxiv (Cold Spring Harbor Laboratory)*. doi:10.1101/2021.07.09.450648
- Mustonen V, Lässig M (2009). From fitness landscapes to seascapes: non-equilibrium dynamics of selection and adaptation. *Trends in Genetics*. doi:10.1016/j.tig.2009.01.002
- Notin et al. (2023). ProteinGym: Large-Scale Benchmarks for Protein Fitness Prediction and Design. *Advances in Neural Information Processing Systems 36*. doi:10.52202/075280-2810
- Priem et al. (2022). OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts. *arXiv / Zenodo preprint*. doi:10.5281/zenodo.6936227
- Qiu et al. (2022). Mapping transcriptomic vector fields of single cells. *Cell*. doi:10.1016/j.cell.2021.12.045
- Ramsauer et al. (2021). Hopfield Networks is All You Need. *International Conference on Learning Representations*.
- Rasmussen CE, Williams CKI (2005). Gaussian Processes for Machine Learning. *The MIT Press eBooks*. doi:10.7551/mitpress/3206.001.0001
- Reimers N, Gurevych I (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. *Proceedings of EMNLP-IJCNLP 2019*. doi:10.18653/v1/d19-1410
- Riesselman et al. (2018). Deep generative models of genetic variation capture the effects of mutations. *Nature Methods*. doi:10.1038/s41592-018-0138-4
- Rives et al. (2021). Biological structure and function emerge from scaling unsupervised learning to 250 million protein sequences. *Proceedings of the National Academy of Sciences*. doi:10.1073/pnas.2016239118
- Schiebinger et al. (2019). Optimal-Transport Analysis of Single-Cell Gene Expression Identifies Developmental Trajectories in Reprogramming. *Cell*. doi:10.1016/j.cell.2019.01.006
- Sourati et al. (2023). Accelerating science with human-aware artificial intelligence. *Nature Human Behaviour*. doi:10.1038/s41562-023-01648-z
- Swanson (1986). Fish Oil, Raynaud's Syndrome, and Undiscovered Public Knowledge. *Perspectives in Biology and Medicine*. doi:10.1353/pbm.1986.0087
- Waddington (1957 (Routledge reissue 2014)). The Strategy of the Genes. *Routledge*. doi:10.4324/9781315765471
- Wang et al. (2011). Quantifying the Waddington landscape and biological paths for development and differentiation. *Proceedings of the National Academy of Sciences*. doi:10.1073/pnas.1017017108
- Wang et al. (2020). MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers. *arXiv (Cornell University)*. doi:10.48550/arxiv.2002.10957
- Yeo et al. (2021). Generative modeling of single-cell time series with PRESCIENT enables prediction of cell trajectories with interventions. *Nature Communications*. doi:10.1038/s41467-021-23518-w

*All 30 references were resolved against OpenAlex (first author and year matched; DOIs where the record has one). Wright (1932) is not cited because it could not be resolved.*
