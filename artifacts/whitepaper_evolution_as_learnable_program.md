# Evolution's search process generates reusable biological programs
### A meta-analysis, a formal framework, and an operational roadmap for closing the gap between evolutionary search and biological state-transition modeling

*Whitepaper compiled from a six-stage analysis of 524 on-target papers (OpenAlex, 2015–2024). All figures, data tables, and per-stage reports are cited inline and available as artifacts.*

---

## Executive summary

The thesis of this work is that **evolution is a search process whose outputs are reusable programs**, and that modern AI is, in effect, learning to read and rerun those programs. Six stages of analysis, each grounded in a real literature corpus, lead to one actionable conclusion:

1. The field modeling evolution splits into two families — those learning evolution's **outputs** (protein/genomic foundation models, generative design) and those learning its **process** (forecasting, evolutionary search). Growth and impact concentrate in the outputs family.
2. Reorganized around **capabilities**, the evidence is strongest at the top of a causal stack (mechanisms, programs) and weakest at the generative roots (pressure, harness, search dynamics).
3. Promoted to a generative ordering — **Pressure → Harness → State Transitions → Programs → Networks → Capability** — the field models the middle with confidence and the generative roots barely at all.
4. But that apparent blind spot is a **vocabulary artifact**: the harness *is* modeled to precision — in a **systems-biology literature that overlaps the evolution literature by only 2%**. The gap is not "unmodelable," it is "unconnected."
5. The two literatures are **complementary by module**: each owns exactly what the other lacks. A closed-loop system wiring them together — the **connectivity paradigm** — is the operational path to an AI that models and accelerates the discovery of biological programs. Citation-network analysis names the specific groups already closest to that wiring.
6. Beneath the citations, the two literatures **already share a computational grammar**: reading their *primitives* rather than their references, 7.7% of cross-pillar pairs run near-identical computation and **97.3% of those share no citations at all.** A third, independent semantic-embedding view confirms it — cross-pillar similarity is **0.71 in computation, 0.26 in language, 0.0002 in citations** (only 1.9% of pairs share any reference; computation and language uncorrelated). *Fitness landscape* and *epigenetic landscape* are the same mathematical object, discovered independently. They are one field that has not noticed — and the highest-value first act is the translation itself, seeded by 96 pre-identified worked-example pairs.
7. A **connectivity matrix** localizes that first act: cutting the shared-computation data by paradigm, by computational role, and by capability, all three agree on the same hot spot — **genomic-foundation-model and fitness paradigms meeting the harness's state-transition / attractor literature**. That coordinate is where the roadmap starts.

---

## Stage 1 — The landscape: two families, one phrase

A corpus of 1,766 unique works (2,000 records, 10 themed OpenAlex queries, filtered to 458 on-target) shows the field borrowing "evolution as a learnable program" for two opposite purposes. **Evolution's outputs as the learnable object** — natural sequences/structures/fitness as a training corpus — is where growth concentrates: generative sequence design (11× growth vs pre-2020) and protein language models (8×) are the fastest-rising paradigms. **Evolution's process as the learnable object** — phylogenetics, forecasting, evolutionary computation — is larger but flatter.

![Paradigm landscape: growth and recent impact by paradigm]({{artifact:art_9f54c339-d37d-460f-879f-414487f39e48}})

*Full detail: `meta_analysis_report.md`, `classified_corpus.csv`, `landmark_papers.csv`.*

---

## Stage 2 — The capability reframe

Reorganizing the 9 paradigms into 7 **capabilities** and rating each on an epistemic ladder (mechanism understood, transferability, confidence — beside corpus-derived evidence density, momentum, impact) exposes the first structural finding: confidence is highest for **protein fold & function** (5/5) and lowest for the process-oriented capabilities. Momentum and confidence are anti-correlated — the field rushes at *generation* faster than it secures *understanding*.

![Capability reframe, before vs after the embedding pass]({{artifact:art_633bcd4c-6bd1-45a2-aa49-8d5d0fc97146}})

The matrix is shown **before and after the Stage-6 embedding pass**, because the embedding work changed the reading of this exact table. *Before* (left, iteration 2): each capability is rated on expert judgment and corpus counts computed **inside the evolution-ML literature** — on that reading, regulatory control of expression and predictable adaptation score lowest confidence and look like the thesis's weak link. *After* (right): a third lens, computed over 524 papers spanning **both** pillars — a six-role computational grammar (shared computation) and a 384-d semantic embedding (shared language), scored against citation overlap — measures each capability's connectivity to the systems-biology harness literature. The flip is the finding: **the three lowest-confidence capabilities hold the top-3 bridge-opportunity scores — regulatory control ranks #1 (0.71).** Their weakness was a within-literature artifact; their evidence is not absent, it is un-cited next door — which is exactly what Stage 6 quantifies and the roadmap acts on.

The causal descent that structures each capability's dossier — read down to explain, up to generate:

![Causal stack: explaining vs generating a capability]({{artifact:art_b3645449-d842-4af6-a445-5c3c095660fd}})

*Full detail: `thesis_capability_dossier.md`, `capability_ladder_matrix.csv`, `matrix3_capability_threespace.csv` (connectivity block).*

---

## Stage 3 — The generative stack

Promoting the "read up = generate" direction to the primary framing gives the stack its causal ordering: **Evolutionary Pressure → Harness Inputs → State Transitions → Biological Programs → Regulatory Networks → Capability**, fed by the input equation *Genome + Environment + Time + Repeated stimulus + Feedback*. Scoring each layer by how well the field models it as a learnable object against how much corpus activity sits adjacent reveals the pattern: **the middle is modeled with confidence; the generative roots barely at all.** State Transitions has high adjacent activity (n≈144) but low modeling depth — a layer publishing trajectories without modeling the transition function itself.

![Generative stack: field reads the products, not the roots]({{artifact:art_fd192954-53d4-4f6a-a193-0eb642cb8ec0}})

*Full detail: `framework_v3_generative_stack.md`, `generative_stack_layers.csv`.*

---

## Stage 4 — The harness is modeled next door

The critical correction. Formalizing capability as a state function — **C = f(Biological State, Environment, History, Time)** — and the harness as a transition operator — **H: (state, environmental signal) → state′** — turns the vague "environment" term into a computational object. Testing the claim that the harness is "inferable to precision" by re-querying with **state-transition vocabulary** (GRN attractors, cell-fate reprogramming, Waddington trajectories) surfaced **120 substantive harness-modeling papers** that the evolution-vocabulary queries never retrieved. The harness *is* modeled to precision — but the two literatures overlap by only **2%**. The blind spot was a vocabulary artifact; the real problem is disconnection, and that disconnection *is* the evolutionary-algorithm ↔ biological-evolution gap.

![Harness as transition operator; the EA↔biology correspondence]({{artifact:art_4f8b175d-2de5-485b-a3ef-797a1c0128b2}})

*Full detail: `harness_operator_report.md`, `harness_state_transition_corpus.csv`.*

---

## Stage 5 — The connectivity paradigm and the auto-research loop

Scoring seven closed-loop modules by presence in each corpus shows they **split almost perfectly by literature** — each side owns what the other lacks. The Harness operator is the largest asymmetry in the entire analysis (+41 points to systems-biology, the exact layer evolution-ML lacks); Search, Pressure, and Representation tilt the other way. This complementarity is the design principle: **the loop closes only if every module is wired across both literatures**, through a shared **(state, program)** interface — the connectivity paradigm.

![Auto-research loop: modules wired across the two literatures]({{artifact:art_f4f5e9cf-3dce-4dcd-9f22-1ffaa320a1f0}})

*Full detail: `auto_research_loop_spec.md`, `loop_module_connectivity.csv`.*

---

## Stage 6 — Reading between the lines: the deep connectivity

The module analysis and the citation network both measure the *surface* — what papers cite. But the essence is deeper: two papers can run the identical computation while citing disjoint literatures and naming every component differently. To elicit that, each paper was mapped onto the connectivity paradigm's six-role **computational grammar** (`state, transition operator, objective, search, representation, feedback`), detecting each role through *both* pillars' vocabularies at once — a match by function, not by shared words. Comparing proximity in this **primitive space** against proximity in **citation space** exposes the real connection: **7.7% of cross-pillar pairs run near-identical computational grammar, and 97.3% of those share zero citations** (`fig9_deep_connectivity.png`, panel A). Where the two literatures do the same thing, they almost never know it.

![Deep connectivity: same computation, no shared citations, and the isomorphism catalog]({{artifact:art_353419ff-81bd-4fce-8ad0-8dd991c3768d}})

The keystone is the **isomorphism catalog** (panel C): *fitness landscape* (evolution-ML) and *epigenetic / potential landscape* (systems-harness) are the same mathematical object — a surface with attractors — discovered independently by two fields that do not cite each other. Every other role is a corollary: genotype ≈ cell state, mutation operator ≈ signal-induced transition, directed search ≈ trajectory through state space, foundation-model embedding ≈ gene regulatory network, selection over generations ≈ environmental signal. This catalog is the connectivity paradigm's shared **(state, program)** interface made concrete — a translation table, not a new abstraction to invent. It reframes the whole roadmap: the loop's shared interface already exists in both literatures, latent in the landscape isomorphism, waiting to be stated explicitly.

**A third, independent view confirms it.** Encoding all papers with a general-purpose semantic embedder adds a *concept space* (surface language) alongside the primitive (computation) and citation (reference) spaces. The three disagree exactly as the thesis predicts (`fig10_three_space.png`): mean cross-pillar similarity is **0.71 in computation, 0.26 in language, 0.0002 in citations** (only 1.9% of pairs share any reference), and computation and language are uncorrelated (ρ = 0.02). Same undercurrent, different vocabulary — measured on three axes. The triangulation also separates two connection types the grammar alone had merged: **6.5% hidden bridges** (same computation, alien language — the true dark bridges) versus **8.9% "false friends"** (similar language, different computation — correctly rejected). This is why concept space alone is insufficient; it needs the grammar as a filter.

![Three-space triangulation: computation matches, language and citations do not]({{artifact:art_fcb0379a-63a5-4ad0-9f52-ace29e80e5c2}})

### The connectivity matrix — the targeting layer

The three-space finding says the bridge exists; the connectivity matrix says *where to build it first*. Cutting the same cell-level data three ways — paradigm × harness sub-area, computational role × pillar, and capability × three-space — localizes the hidden bridges to specific coordinates (`connectivity_matrix_report.md`, `fig11_connectivity_matrix.png`):

![The connectivity matrix: three cuts localize where to wire first]({{artifact:art_b56c95c4-eb2d-4e64-b6de-174a9fd115aa}})

- **By paradigm (panel A):** the hidden bridges are hottest for **genomic foundation models** and **fitness-landscape** paradigms meeting the harness's **state-transition / attractor** and **isogenic-variability** clusters (hidden-bridge score 0.77–0.79, zero shared citations). These already learn regulatory/expression state — the harness's object — without citing it.
- **By role (panel B):** the two *shared* roles — **STATE** (genotype ≈ cell state) and **OBJECTIVE** (fitness landscape ≈ epigenetic landscape) — are the load-bearing isomorphism; the complementary roles are the trade (evolution-ML brings SEARCH; systems-harness brings TRANSITION, REPRESENTATION, FEEDBACK).
- **By capability (panel C):** the primitive–citation gap is wide and *uniform* across all seven capabilities (primitive 0.63–0.74 vs citation-fraction 0.01–0.04) — the disconnect is structural, not local to one part of the thesis.

All three cuts agree on the same hot spot, which becomes the roadmap's targeting statement: **the first worked example should connect a genomic-FM or fitness paradigm to the transitions/attractors harness cluster.**

*Full detail: `deep_connectivity_report.md`, `connectivity_matrix_report.md`, `isomorphism_catalog.csv`, `dark_bridges.csv`, `deep_bridge_groups.csv`, `phase0_seed_bridges.csv`, `matrix1_*.csv`, `matrix2_role_pillar.csv`, `matrix3_capability_threespace.csv`.*

---

## The Phase-1 collaborators: who is already closest to the bridge

Citation-network analysis over 519 papers with full reference lists confirms the disconnection is even starker than the ID overlap suggested: **only 9 direct cross-citation edges** exist between the two corpora, and just **1 direct M2↔M4 edge**. Direct citation is too sparse to name collaborators, so bibliographic coupling (shared references = intellectual adjacency) identifies the groups whose work already straddles the gap.

![Citation network: the gap and the bridge groups]({{artifact:art_acd6c5ef-3d3b-48d2-b383-bd14d365d13b}})

**Candidate Phase-1 groups** (ranked by methodological closeness to the M2↔M4 wiring; full table in `phase1_candidate_groups.csv`):

1. **Richard A. Watson (University of Southampton)** — the standout. Publishes on *both* sides: "How evolution learns to generalise" (search-side, evolution-as-learning) and "the learning principles of cellular networks" (harness-side). A same-author bridge already framing both evolution and cellular networks as learning — the single closest group to the M2↔M4 wiring.
2. **Adam Feist / Michael Jensen (Novo Nordisk Foundation Center, DTU)** — couple ML search with mechanistic dynamical models of metabolic adaptation and enzyme promiscuity; the exact hybrid the loop needs, with a working wet-lab design-build-test cycle.
3. **Dana Pe'er (Memorial Sloan Kettering)** — premier cell-fate/state-transition modeling; the harness operator in its most data-rich form, with multiple couplings to search-side papers.
4. **Qing Nie (UC Irvine) / Madhav Mani (Northwestern)** — formal dynamical-systems models of single-cell transitions; directly supply H as a learnable object.
5. **José Onuchic (Rice, CTBP)** — physics-of-living-systems treatment of GRN state space; theory backbone for the harness operator.

*(Faruck Morcos, UT Dallas, scores highest on raw bibliographic coupling but the score is inflated by a shared review bibliography; his coevolution-driven repressor-engineering work is nonetheless a genuine fitness-landscape↔regulatory-circuit bridge.)*

The deep-connectivity analysis (Stage 6) names a **second, complementary list** — the people who independently formalized the *same landscape mathematics*, invisible to citations (full table in `deep_bridge_groups.csv`):

1. **Sui Huang (Institute for Systems Biology)** — formalized the "cancer attractor" / epigenetic landscape as a dynamical system; this *is* the objective isomorphism on the harness side.
2. **Elena Álvarez-Buylla (Universidad Autónoma de la Ciudad de México, per OpenAlex)** — GRN attractor models of cell fate; the most frequent node in the clean dark bridges.
3. **Andrea Pagnani (Politecnico di Torino)** — direct-coupling analysis of protein fitness landscapes; the same landscape object on the evolution-ML side.
4. **Eduardo Sontag (Northeastern) / Laurence Calzone (Institut Curie–Inserm)** — control-theory and logical-model treatments spanning both.

The two lists serve different purposes: the bibliographic list above is the **methods / wet-lab** bridge (groups whose references already overlap); this list is the **conceptual** bridge (groups who already think in landscapes and attractors on both sides). Approach the first to *build* the loop, the second to *frame* the translation.

---

## The roadmap

**Phase 0 — State the translation (0–3 mo, and shorter than it first appeared).** The lowest-cost, highest-leverage act: demonstrate one worked example where a fitness-landscape method and a cell-fate-landscape method are shown to be the *same algorithm*, then generalize it into the isomorphism catalog. The three-space triangulation **shortens this**: rather than synthesizing the catalog from scratch, start from the **96 pre-identified "seed bridges"** (`phase0_seed_bridges.csv`) — pairs already high in *both* computation and language similarity yet sharing zero citations, so the equivalence is demonstrable without first building the vocabulary bridge (e.g. "Learning dynamical information from static sequence data" ≈ "Learning Pathway Dynamics from Single-Cell Proteomic Data"). Validate one seed, use it to motivate the fuller catalog, and connect the ~700 dark-bridge pairs (716, spanning 193 unique papers) that currently cannot see each other. The connectivity matrix names the target: **pick the seed from a genomic-FM or fitness paradigm meeting the transitions/attractors harness cluster**, where the hidden-bridge score peaks. *Approach the conceptual-bridge group — Huang, Álvarez-Buylla, Pagnani.*

**Phase 1 — Formalize the Harness operator (0–6 mo).** Learn H on a data-rich system (cell-fate reprogramming: dense single-cell data, known TF inputs, existing GRN models). Deliverable: a perturbation-validated transition operator. *Approach Watson, Pe'er, or Nie/Mani.*

**Phase 2 — Make pressure and harness reusable (6–18 mo).** Turn both from bespoke per-system fits into transferable modules, pointing foundation-model methods at learning a transferable H and scoring function. *Approach Feist/Jensen for the mechanistic+ML hybrid.*

**Phase 3 — Close the EA↔biology correspondence (18–36 mo).** Instantiate an evolutionary algorithm whose fitness evaluation *is* the learned Harness and whose genotype→phenotype map *is* learned state-transition dynamics. Test the core claim: does the loop, driven only by data and its own error signal, **rediscover the reusable programs biological evolution actually found** (validated against ancestral reconstruction and real adaptation) and generate viable new ones?

**Cross-cutting:** every phase deliberately cites across the 2% gap — systems-biology transition models as mechanism, evolution-ML foundation models as the reusable representation. The bridge is the contribution.

---

## Method, scope, and honesty notes

- **Corpora**: evolution-ML (1,766 unique → 458 on-target → 404 after off-topic filtering) and systems-biology harness (758 unique → 120 harness-modeling), both from OpenAlex 2015–2026, trend claims capped at 2024 (2025–26 under-indexed).
- **Classification** is deterministic keyword logic — transparent and reproducible, but noisy per-paper; treat paradigm/capability aggregates as the finding, not any single row.
- **Two kinds of numbers**: measured (paper counts, growth ratios, citation rates, the 2% overlap, the 9 cross-citation edges, per-module ownership %) and judgment (the 1–5 epistemic-ladder scores, the loop architecture, the group rankings). These are labeled as such throughout and the judgment scores are meant to be debated.
- **The citation network** uses OpenAlex `referenced_works`; the 2% overlap is an ID-level lower bound on disconnection. Bridge groups are identified by bibliographic coupling (≥2 shared references), with review-bibliography artifacts flagged.
- **The loop architecture and roadmap** are engineering proposals grounded in the measured complementarity, not an implemented system.
- **The deep-connectivity analysis (Stage 6)** measures primitive-space similarity via a hand-built six-role grammar (interpretable, not learned; different role definitions shift the exact percentages but not the direction), gated to papers expressing ≥4 of 6 roles. The 7.7% / 97.3% figures and the mirror-image percentages are measured; the isomorphism catalog is interpretation grounded in them; the conceptual-bridge PI list is measured frequency but inherits keyword noise — a ranked lead list, not a ranking. The third view (concept-space semantic embeddings, `all-MiniLM-L6-v2`) was computed: the 0.71 / 0.26 / 0.0002 ordering and the ρ = 0.02 primitive–concept independence are measured; concept-space quadrant thresholds are percentile-based, so those percentages depend on the cutoff while the ordering does not. The 96 seed bridges are a pre-filtered worklist, not 96 confirmed isomorphisms — each still needs the algorithmic equivalence shown by hand.

*Component reports: `meta_analysis_report.md`, `thesis_capability_dossier.md`, `framework_v3_generative_stack.md`, `harness_operator_report.md`, `auto_research_loop_spec.md`, `deep_connectivity_report.md`, `connectivity_matrix_report.md`. Data tables and all figures are available as artifacts.*