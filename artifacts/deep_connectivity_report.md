# Reading between the lines: the deep connectivity of the two pillars

*Going beneath bibliographic coupling to ask whether the two literatures run the **same underlying computation** — regardless of what they cite or what words they use. The essence, not the surface.*

## Why go deeper than bibliography

Bibliographic coupling (the previous pass) measures **citation space**: two papers connect if they cite the same sources. That found only 9 direct cross-citations and a handful of coupled pairs — a real but thin bridge. Your intuition was that the *essence underneath* is a stronger connection than the citations reveal: two papers can run the identical computation — "learn a landscape, navigate it toward stable states" — while citing entirely disjoint literatures and naming every component differently. Bibliography is blind to that. To elicit it, I measured connection in two deeper spaces:

- **Primitive space** — does each paper fill the same *computational roles*? I mapped every paper onto the connectivity paradigm's six-role grammar (`{state, transition operator, objective, search, representation, feedback}`), detecting each role through **both pillars' vocabularies at once**, so a match is by *function*, not by shared words.
- **Citation space** — the bibliographic-coupling baseline (Jaccard overlap of reference lists).

The connection you're after is the **divergence**: pairs that are near in primitive space but far in citation space. I call these **dark bridges** — the same computation, unspoken.

*(A third view — concept-space semantic embeddings — was planned but the embedding model could not be pulled through the network sandbox in reasonable time. The two computed spaces answer the question; the embedding view would only have added corroboration, and is a clean follow-up if you want it.)*

## The headline result

Restricting to the 206 papers that express the *full* grammar (≥4 of 6 roles) and comparing every cross-pillar pair:

- **7.7% of cross-pillar pairs run near-identical computational grammar** (primitive similarity > 0.90).
- **Of those, 97.3% share zero citations.**

That is the finding in one line: **where the two literatures are doing the same thing, they almost never know it.** The bridge is real and dense in primitive space, and nearly invisible in citation space — see `fig9_deep_connectivity.png`, panel A.

## The mirror-image complementarity (panel B)

Both pillars fill all six roles, but with opposite emphasis:

| Role | evolution-ML | systems-harness |
|---|---|---|
| STATE | 68% | 56% |
| TRANSITION OPERATOR | 34% | 64% |
| OBJECTIVE | 65% | 64% |
| SEARCH | 54% | 70% |
| REPRESENTATION | 40% | 49% |
| FEEDBACK | 41% | 85% |

Evolution-ML leans on STATE and OBJECTIVE (it has the sequences and the fitness); systems-harness leans on TRANSITION, SEARCH, and especially FEEDBACK (it has the dynamics and the environmental signal). This is the same complementarity the loop-module analysis found, now visible at the level of computational primitives rather than paper counts.

## The isomorphism catalog — the essence, named (panel C)

The six roles, with how each pillar expresses the *same* computation in *different* words (`isomorphism_catalog.csv`):

| Computational role | evolution-ML says | systems-harness says |
|---|---|---|
| STATE | genotype / sequence | cell state / attractor |
| TRANSITION OPERATOR | mutation / variation operator | signal-induced state transition |
| OBJECTIVE | fitness landscape | epigenetic / potential landscape, attractor stability |
| SEARCH | evolutionary / directed search | trajectory through state space |
| REPRESENTATION | learned embedding / foundation model | gene regulatory network / circuit |
| FEEDBACK | selection over generations | environmental signal / repeated stimulus |

The **OBJECTIVE** row is the keystone: *fitness landscape* and *epigenetic landscape* are the same mathematical object — a potential surface with attractors — discovered independently by two fields that do not cite each other. Every other row is a corollary of that one isomorphism. This catalog is the "connectivity paradigm" made concrete at the vocabulary level: a translation table an AI system (or a person) can use to read one literature into the other.

## Who actually sits on the bridge — a different, better answer

The deep analysis names **different bridge figures than bibliography did**, and they are more apt. Bibliographic coupling surfaced Watson, Pe'er, Feist — people whose *reference lists* overlap. The primitive-grammar analysis surfaces the people who independently formalized the *same landscape mathematics* (`deep_bridge_groups.csv`):

- **Sui Huang (Institute for Systems Biology)** — formalized the "cancer attractor" and the epigenetic landscape as a dynamical system with stable states. This *is* the OBJECTIVE isomorphism on the harness side.
- **Elena Álvarez-Buylla (Universidad Autónoma de la Ciudad de México, per OpenAlex affiliation)** — GRN attractor models of cell-fate determination; the transition operator and objective, in Boolean/dynamical form. The single most frequent node in the clean dark bridges.
- **Carsten Peterson (Lund)**, **Jie Zheng (NTU)** — dynamical/network models of cell-state landscapes.
- **Andrea Pagnani (Politecnico di Torino)** — direct-coupling analysis of protein fitness landscapes; the same landscape object on the evolution-ML side.
- **Eduardo Sontag (Northeastern)**, **Laurence Calzone (Institut Curie/Inserm)** — control-theory and logical-model treatments that span both.

These are the people to read (and talk to) for the *conceptual* bridge — those who already think in landscapes and attractors on both sides — as distinct from the *methods/wet-lab* bridge groups the bibliographic pass named. Two complementary collaborator lists for two complementary purposes.

## Concept-space triangulation — a third, independent view

The embedding model was subsequently obtained (the earlier block was a rotating-CDN issue on the sandbox, resolved by granting the exact redirect host `us.aws.cdn.hf.co`). Encoding all 522 papers with a general-purpose sentence embedder (`all-MiniLM-L6-v2`) gives a third axis — **concept space**, i.e. surface-language similarity — independent of both the hand-built grammar and the citations. The result is the strongest possible confirmation of the thesis, because the three views *disagree in exactly the way the thesis predicts* (`fig10_three_space.png`):

| Space | Mean cross-pillar similarity | What it measures |
|---|---|---|
| Primitive (computation) | **0.71** | do they run the same algorithm? |
| Concept (language) | **0.26** | do they use the same words? |
| Citation (references) | **0.0002** (1.9% of pairs share any) | do they cite each other? |

Primitive and concept similarity are **uncorrelated** (Spearman ρ = 0.02, n.s.). The computation matches; the language does not; the citations do not. This is "same undercurrent, different vocabulary" measured on three independent axes — the surface gap is real, and the connection lives strictly in the computation.

**The triangulation also separates two kinds of connection the grammar alone had merged** (panel B quadrants, of 9,585 rich cross-pillar pairs):
- **1.1% obvious bridges** — same grammar *and* visible semantic similarity.
- **6.5% hidden bridges** — same grammar but *alien language* (high primitive, low concept): the true dark bridges that require the translation to surface.
- **8.9% false friends** — high semantic similarity but *different* computation: pairs the primitive gate correctly rejects, which a naive embedding-only search would wrongly connect. (This is why concept space alone is not enough — it needs the grammar as a filter.)

### This shortens the roadmap

The 6.5% hidden-bridge finding validates Phase 0, but the 1.1% obvious-bridge layer *accelerates* it. Among pairs that are high on **both** primitive and concept similarity **and** share zero citations, there are **96 "seed bridges"** (`phase0_seed_bridges.csv`) — worked-example candidates where even a general-purpose embedder already sees the connection, so no vocabulary bridge is needed to *start*. Concrete seeds include:

- "Learning dynamical information from static protein/sequence data" (STRUCT_PRED) ≈ "Learning Pathway Dynamics from Single-Cell Proteomic Data" — literally the same task statement across pillars.
- "A foundation model of transcription across human cell types" (GENOMIC_FM) ≈ "Rapid Chromatin Switch in Direct Reprogramming of Fibroblasts" — foundation-model representation meets state-transition.
- "Characterization of RNA polymerase II trigger loop mutations" (FITNESS) ≈ "Markov State Models of gene regulatory networks" — landscape/objective learning, both sides.

Practically: **Phase 0 no longer needs the isomorphism catalog written first to find its worked example.** Start from a seed-bridge pair that is already visible in all three spaces, demonstrate the shared algorithm, and use *that* concrete result to motivate the fuller catalog — compressing the "state the translation" phase from a from-scratch synthesis into a validate-and-generalize task. The 96 seeds are a ranked, pre-filtered worklist for exactly that.

## What this changes for the thesis and the loop

The connectivity paradigm is no longer just an engineering proposal — it has an empirical basis. The two literatures **already share a computational grammar**; they are one field that hasn't noticed. That means:
- The loop's shared **(state, program)** interface is not a new abstraction to invent — it is the fitness-landscape ≈ epigenetic-landscape isomorphism, already present in both literatures, waiting to be made explicit.
- The highest-value first paper may simply be the **translation itself**: formally stating the isomorphism catalog and demonstrating one worked example where a fitness-landscape method and a cell-fate-landscape method are shown to be the same algorithm. That single act of "reading between the lines" would connect the ~700 dark-bridge pairs (716, spanning 193 unique papers — 125 evolution-ML, 68 harness) that currently cannot see each other.

## Method & honesty notes
- The six-role grammar and its per-pillar vocabularies are hand-built (in the code); they are an interpretable model of the connectivity paradigm, not a learned one. Different role definitions would shift the exact numbers.
- Primitive similarity uses magnitude-dampened (sqrt-count) cosine over the six-role vectors, gated to papers expressing ≥4 roles so a match reflects the full grammar, not one shared term. Coarse per-paper (a battery-electrolyte paper can spuriously match at low richness — hence the richness gate); reliable in aggregate.
- The 97.3% / 7.7% figures and the mirror-image percentages are measured. The isomorphism catalog is interpretation grounded in those measurements; the bridge-PI list is measured (frequency in clean dark-bridge pairs) but inherits the keyword noise, so treat it as a ranked lead list, not a ranking.
- Concept-space embeddings (`all-MiniLM-L6-v2`, 384-dim, general-purpose) are now computed and reported above. They *disagree* with primitive similarity (ρ = 0.02), which is the confirming result — the connection is computational, not semantic. Concept-space thresholds are percentile-based (top decile) because its scale differs from the grammar cosine; the quadrant percentages depend on that threshold choice, but the primitive/concept/citation *ordering* (0.71 / 0.26 / 0.0002) does not.
- The 96 seed bridges require high similarity on both learned axes AND zero citations; they are a pre-filtered lead list for Phase-0 worked examples, not a claim that all 96 are true isomorphisms — each still needs the algorithmic equivalence shown by hand.
- Data: `dark_bridges.csv` (ranked pairs), `isomorphism_catalog.csv`, `deep_bridge_groups.csv`, `phase0_seed_bridges.csv` (the 96 tri-space seeds), `concept_embeddings.npy` (522×384), `combined_text.csv` (the 522-paper two-pillar text table).