# Modeling evolution as a learnable program — a meta-analysis of the field

*A structured survey of how the literature operationalizes the idea that evolutionary and adaptive biological processes can be learned, predicted, and accelerated by machine-learning systems.*

## Scope and method

- **Source**: OpenAlex, 10 themed queries spanning protein/genomic language models, ML-guided directed evolution, fitness-landscape learning, generative sequence design, ML phylogenetics, evolutionary computation / open-endedness, and evolutionary forecasting.
- **Corpus**: 2,000 records → 1,766 unique works (2015–2026) → **458 on-target** works after a two-stage filter (a concept co-occurrence gate requiring both an *evolution/adaptation* and a *learning/model* signal, then a keyword rule-classifier with an off-topic blocklist that removed generic databases, tool papers, and unrelated ML surveys).
- **Classification** into 9 paradigms is deterministic and keyword-based (an LLM pass was attempted but the per-frame token budget was exhausted). This is transparent and reproducible but coarse: individual paper assignments carry noise, so treat the paradigm *aggregates* as the finding, not any single row.

Artifacts: `classified_corpus.csv` (all 458 with paradigm labels), `paradigm_summary.csv`, `landmark_papers.csv`, `learnable_program_synthesis.csv`, and two figures.

## The central finding

The field is not converging on one definition of "evolution as a learnable program" — it is **splitting into two families** that borrow the phrase for opposite reasons:

1. **Evolution's *outputs* as the learnable object** (warm colors in the figures). Natural sequences, structures, and fitness measurements are treated as a training corpus; the model internalizes the constraints that selection left behind. Protein language models, genomic foundation models, evolutionary-coupling structure prediction, generative design, and fitness-landscape learning all sit here. This family is where the **growth and recent impact are concentrated**.

2. **Evolution's *process* as the learnable object** (cool colors). ML is applied to the dynamics of evolution itself — reconstructing history (phylogenetics), forecasting trajectories (resistance, viral escape), or using evolution *as* an adaptive search algorithm (evolutionary computation, quality-diversity, open-endedness). This family is larger in raw count but flatter in growth.

## Quantitative landscape

| Paradigm | n | Growth (2020–24 vs pre-2020) | Median cites/yr | Median year |
|---|---|---|---|---|
| Generative sequence/structure design | 37 | **11.0×** | 17.5 | 2022 |
| Protein language models | 36 | **8.0×** | 16.8 | 2024 |
| Fitness-landscape learning | 67 | 6.6× | 7.0 | 2023 |
| Structure prediction (evo-coupling) | 28 | 4.2× | 15.0 | 2023 |
| Evolutionary forecasting | 46 | 2.5× | 12.8 | 2021 |
| Evolution-as-search (EC / open-ended) | 67 | 2.1× | 13.3 | 2020 |
| ML-guided directed evolution | 58 | 1.8× | 15.9 | 2021 |
| ML phylogenetics / ancestral | 85 | 1.7× | 13.3 | 2020 |
| Genomic foundation models | 34 | 1.1× | 21.1 | 2020 |

Reading the table: **generative design and protein language models are the fastest-rising paradigms**, both with a median publication year of 2022–2024 — they are new *and* accelerating. Genomic foundation models show the highest median citation rate but flat growth in this sample, reflecting a smaller number of very heavily-cited anchor papers (Enformer, Evo) rather than a broad wave. The classical process-oriented paradigms (phylogenetics, evolution-as-search) are large, mature, and growing modestly.

## How each paradigm makes evolution "learnable"

| Paradigm | The learnable "program" | Learning signal | The core move |
|---|---|---|---|
| Protein LMs | Sequences across evolution | Self-supervised masked-token | Evolution's outcomes *are* the training set |
| Genomic FMs | DNA / regulatory genomes | Next-token on nucleotides | The genome is a language; grammar is learned |
| Structure prediction | MSAs / evolutionary couplings | Supervised on PDB + coevolution | Coevolution encodes preserved 3D constraints |
| Generative design | Sequence/structure manifold | Diffusion / autoregressive / inverse folding | Learn the manifold, sample *beyond* evolution |
| ML-guided directed evolution | Experimental fitness (active loop) | Surrogate + Bayesian optimization | Directed evolution as a learnable search policy |
| Fitness-landscape learning | Genotype–phenotype maps | Supervised on DMS / fitness assays | The landscape is a function with epistatic structure |
| Evolutionary forecasting | Time-resolved populations | Predictive dynamics models | Evolution is forecastable from state + selection |
| ML phylogenetics | Homolog sets, trees | Likelihood / NN inference | History is a reconstructable inference target |
| Evolution-as-search | Candidate solutions | EA / quality-diversity / neuroevolution | Evolution *is* the algorithm; make it open-ended |

## Landmark anchors (by citations/year within paradigm)

- **Protein LMs**: ESM-1b — *Biological structure and function emerge from scaling unsupervised learning* (2021); ESM3 — *Simulating 500 million years of evolution with a language model* (2025).
- **Structure prediction**: AlphaFold 3 (2024); ESMFold — *Evolutionary-scale prediction of atomic-level protein structure* (2023).
- **Genomic FMs**: Enformer — *Effective gene expression prediction from sequence* (2021); Evo — *Sequence modeling and design from molecular to genome scale* (2024).
- **Generative design**: ProteinMPNN (2022) and its function/stability applications.
- **Fitness / directed evolution**: dominated by variant-effect predictors built *on top of* protein LMs (e.g. CADD v1.7 integrating protein-LM scores), which is itself the key trend — see below.

## Three cross-cutting signals

1. **Convergence onto foundation-model substrates.** The fastest-growing paradigms increasingly *depend on* protein/genomic language models rather than competing with them. Variant-effect and fitness predictors now consume LM embeddings; directed-evolution loops use LM priors to propose libraries. The "learnable program" is collapsing toward a shared pretrained representation of sequence space.

2. **The generate-vs-understand axis is where the money is moving.** Both figures show the upward drift toward *design* (top of Fig. 2). Learning evolution's constraints well enough to *predict* has matured into learning them well enough to *generate* novel, functional sequences that evolution never sampled.

3. **A re-emerging bridge between the two families.** An emerging line of work uses large models as the *variation operator* inside evolutionary search (LLM-driven program/sequence evolution). This would reconnect the "outputs" family (learned models) with the "process" family (evolution-as-search) — arguably the most direct realization of the framing: evolution *as a search process* driven by a *learned program*. Note: this bridge is under-represented in the present OpenAlex corpus (which is weighted toward biological-sequence venues) and is flagged here as a direction to probe, not a quantified trend.

## Gaps and open directions

- **Weak coupling between open-endedness/QD and biological foundation models.** The evolution-as-search literature (mature, in ML venues) and the protein/genomic-LM literature (exploding, in bio venues) barely cite each other in this corpus. The bridge in signal (3) is the frontier.
- **Fitness-landscape learning is high-volume but low per-paper impact** (median 7.0 cites/yr) — a fragmented, application-driven area that has not yet consolidated onto shared benchmarks the way structure prediction did.
- **Evolutionary forecasting** remains empirically hard and modestly cited despite obvious stakes (resistance, pandemic escape); it is the paradigm where "predict evolution" is most literally the goal and least solved.

## Caveats

- Counts are **sampled** (top-200 relevance per theme), not exhaustive; absolute volumes understate the true literature and 2025–26 is under-indexed (trend figure capped at 2024).
- Paradigm labels are keyword-derived — reliable in aggregate, noisy per-paper.
- Citation-rate favors older papers slightly even after per-year normalization; median year is reported alongside to contextualize.
