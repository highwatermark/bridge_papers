# Appendix 1 — Role lexicon (frozen, 81 terms)

Matching: lowercase substring on title + '. ' + abstract; each distinct term counts once per paper. Source: `role_lexicon.tsv`.

| Role | evolution-ML terms | systems-harness terms |
|---|---|---|
| STATE | genotype, sequence, variant, genome, allele, protein, population state | cell state, expression state, phenotype state, attractor, stable state, cell type, configuration |
| TRANSITION_OPERATOR | mutation, recombination, variation operator, substitution, genetic operator, crossover | state transition, cell fate transition, reprogramming, differentiation, signal-induced, perturbation response, switch |
| OBJECTIVE | fitness, selection, fitness landscape, adaptive, objective, selective pressure | attractor stability, robustness, canalization, landscape, potential, stability, optimal response |
| SEARCH | evolutionary search, directed evolution, optimization, genetic algorithm, exploration, evolve | trajectory, dynamics, navigation, path, flow, dynamical, evolve toward |
| REPRESENTATION | embedding, language model, representation, latent, foundation model, encoder, learned | gene regulatory network, grn, regulatory network, network model, circuit, topology, inference |
| FEEDBACK | generation, iterative, selection cycle, adaptation over, feedback, repeated | signal, stimulus, environment, induction, condition, exposure, input, feedback loop |

**Known failure modes.** Substring matching collides (`state` in `statement`, `protein` in any protein paper); design-type operations (`fusion`, `design`, `compatib*`) are absent, producing at least one observed false negative (§6).
