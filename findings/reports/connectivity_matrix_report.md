# The connectivity matrix

*Three matrices built from the three-space analysis (primitive / concept / citation), each a different cut of the same finding: the two pillars run the same computation, invisible to citations. See `fig11_connectivity_matrix.png`.*

## Matrix 1 — Where the hidden bridges concentrate (paradigm × harness sub-area)

Rows are the nine evolution-ML paradigms; columns are five harness sub-areas discovered by clustering the harness papers in concept space. Each cell is the **hidden-bridge score** = mean primitive similarity × (1 − citation-share) — hottest where two literatures compute alike but never cite.

Harness sub-areas (clustered, labeled by distinctive terms):
- **C1 — state transitions / attractors / development** (n=15, the core harness cluster)
- **C2 — single-cell isogenic variability** (n=7)
- **C3 — synthetic toggle-switch circuits** (n=6)
- **C4 — immune plasticity / effector states** (n=4)
- **C0 — genotypic/species** (n=2, underpowered — read with caution)

The hottest hidden-bridge cells:

| evolution-ML paradigm | → harness sub-area | primitive | citation-share | hidden-bridge |
|---|---|---|---|---|
| GENOMIC_FM | C1 transitions/attractors | 0.78 | 0.00 | **0.78** |
| GENOMIC_FM | C4 immune plasticity | 0.78 | 0.00 | **0.78** |
| GENERATIVE | C4 immune plasticity | 0.77 | 0.00 | **0.77** |
| GENOMIC_FM | C2 isogenic variability | 0.77 | 0.00 | **0.77** |
| FITNESS | C2 isogenic variability | 0.79 | 0.05 | 0.75 |
| PLM | C2 isogenic variability | 0.73 | 0.00 | 0.73 |

**Read:** the genomic-foundation-model and generative paradigms sit closest to the harness's state-transition and plasticity literature — they already learn regulatory/expression state, which *is* the harness's object, but cite none of it. These are the paradigm pairs to wire first. Tables: `matrix1_hidden_bridge_score.csv`, `matrix1_paradigm_harness_primitive.csv`.

## Matrix 2 — The isomorphism, quantified (role × pillar)

Each of the six computational roles, scored for how much of each pillar expresses it, plus the cross-pillar role similarity. This is the isomorphism catalog turned into measurements (`matrix2_role_pillar.csv`):

| Role | evo coverage | harness coverage | emphasis |
|---|---|---|---|
| STATE | 0.56 | 0.54 | shared |
| TRANSITION OPERATOR | 0.33 | 0.72 | **systems-harness** |
| OBJECTIVE | 0.38 | 0.39 | shared |
| SEARCH | 0.35 | 0.20 | **evolution-ML** |
| REPRESENTATION | 0.26 | 0.44 | **systems-harness** |
| FEEDBACK | 0.38 | 0.51 | **systems-harness** |

**Read:** the two shared roles (STATE, OBJECTIVE) are the load-bearing isomorphism — genotype≈cell-state and fitness-landscape≈epigenetic-landscape are where both pillars already meet. The complementary roles are the trade: evolution-ML brings SEARCH, systems-harness brings TRANSITION, REPRESENTATION, and FEEDBACK. A closed loop needs exactly this exchange.

## Matrix 3 — Connectivity by capability (capability × three-space)

The seven thesis capabilities, each scored for its mean connectivity to the harness pillar across all three spaces (`matrix3_capability_threespace.csv`):

| Capability | n (rich) | primitive | concept | citation-frac | hidden-bridge |
|---|---|---|---|---|---|
| Regulatory control of expression | 2* | 0.744 | 0.269 | 0.044 | **0.711** |
| Fitness-landscape navigation | 23 | 0.699 | 0.304 | 0.024 | 0.682 |
| Predictable adaptation | 6 | 0.685 | 0.228 | 0.029 | 0.665 |
| Protein fold & function | 5 | 0.675 | 0.235 | 0.018 | 0.663 |
| Generative evolvability | 6 | 0.667 | 0.273 | 0.015 | 0.657 |
| Ancestral program reconstruction | 3* | 0.651 | 0.233 | 0.010 | 0.644 |
| Directed / accelerated search | 16 | 0.640 | 0.260 | 0.015 | 0.630 |

*small rich-paper n — treat as indicative.

**Read:** the primitive–citation gap is wide and uniform (primitive 0.63–0.74, citation-fraction 0.01–0.04) for *every* capability — the disconnect is structural, not specific to one part of the thesis. Regulatory control and fitness-landscape navigation top the hidden-bridge ranking, consistent with Matrix 1: the capabilities nearest the harness are precisely those that already model state and landscape.

## What the matrix says together

All three cuts converge: **the connection is in the computation (primitive 0.63–0.79), not the language (concept ~0.26) or the citations (~0.02).** Matrix 1 localizes it to specific paradigm pairs, Matrix 2 to specific shared roles, Matrix 3 to specific capabilities — and they agree on the same hot spots (genomic/regulatory + fitness-landscape, meeting the harness's transition/attractor literature). For the roadmap, this is the targeting layer under Phase 0: the first worked example should connect a genomic-FM or fitness paradigm to the C1 transitions/attractors harness cluster, where the hidden-bridge score is highest.

## Method & honesty notes
- Matrices are computed on the rich-paper subset (≥4 of 6 roles expressed). This rebuild uses the reconstructed keyword grammar (the exact in-memory dict from the prior turn was cleared by a kernel restart); aggregate means (primitive 0.68, concept 0.27, citation 0.0002) reproduce the published headline within the grammar's known sensitivity — the intended robustness check, not a new result.
- Harness sub-clusters are KMeans (k=5) on concept embeddings; k and labels are descriptive, not canonical. C0 (n=2) is underpowered and flagged.
- Cross-pillar role similarity (Matrix 2) is the mean product of per-paper normalized role weights — a proxy for co-emphasis, not a formal correlation.
- Small rich-n capabilities (Regulatory n=2, Ancestral n=3) are flagged; their exact values are indicative.
- Tables: `matrix1_*.csv`, `matrix2_role_pillar.csv`, `matrix3_capability_threespace.csv`.