# Appendix 4 — Protocol for the unification experiment (Eq. 9) — FUTURE WORK, NOT RUN

$$x_{t+1} = x_t - \eta\,\nabla J_\psi(x_t) + \sigma\,\xi_t,\qquad \xi_t\sim\mathcal N(0,I)$$

**Hypothesis.** One learned scalar field $J_\psi$ can simultaneously (i) predict fitness-like labels on states and (ii) generate the observed state trajectories as noisy gradient flow — i.e. Ding's learned $J$ and Fard's explicit $T,\pi$ are two views of one object. **No result for this experiment exists; no number below is a result.**

## 1. Data — a system with both a fitness side and a state-trajectory side

Requirement: the same (or a tightly coupled) molecular system with (a) many variants with measured function, and (b) time-resolved or single-cell state data showing multistable behaviour.

| Candidate | Fitness / variant side | State-transition side | Status |
|---|---|---|---|
| **1. *E. coli lac* system** | ~4,000 LacI substitutions with repression phenotypes — Markiewicz et al. 1994, *J Mol Biol*, 10.1006/jmbi.1994.1458 | Multistability of lac induction, single-cell distributions — Özbudak et al. 2004, *Nature*, 10.1038/nature02298 | Papers verified. **Raw-data access TO-LOOK-UP.** Best-matched pairing: same regulator, same circuit. |
| **2. Yeast GAL network** | Variant-effect data for Gal4/Gal80/Gal3 — **TO-LOOK-UP** in MaveDB (Esposito et al. 2019, 10.1186/s13059-019-1845-6) / ProteinGym (Notin et al. 2023) | Cellular memory and stochastic transitions in GAL — Açar et al. 2005, *Nature*, 10.1038/nature03524 | Trajectory paper verified; variant side **TO-LOOK-UP**. |
| **3. Sequence-space trajectories only** | SARS-CoV-2 RBD deep mutational scan — Starr et al. 2020, *Cell*, 10.1016/j.cell.2020.08.012 | Observed lineage trajectories in sequence space (surveillance data) | Paper verified; trajectory data source **TO-LOOK-UP**. Tests the Ding half with sequence-state dynamics, not expression. |

Search criteria if none of these is usable: a protein with a published DMS (MaveDB/ProteinGym) whose downstream circuit has published time-resolved expression or single-cell data showing ≥2 stable states under a controlled input.

## 2. What is trained

- **State space.** Candidate 1: $x$ = (LacI variant embedding $z=\phi(\text{seq})$ from a frozen protein language model, reporter expression level, inducer concentration $u$).
- **$J_\psi$ families (one per arm, same data):** (A) Gaussian process with RBF kernel; (B) two-layer MLP potential; (C) input-convex neural network (ICNN) as a *negative* arm, since convexity forbids multiple basins; (D) quadratic form $-\tfrac12 x^\top W x$ fit by the Hopfield correlation route, as the Fard baseline.
- **Loss.** $\mathcal L = \lambda_1\,\text{MSE}(J_\psi(x_i), -y_i) + \lambda_2\,\text{NLL}_{\text{traj}}(x_{t+1}\mid x_t;\eta,\sigma,J_\psi)$ with $\eta,\sigma$ learned. Fix $\lambda_1/\lambda_2$ on the validation split before looking at test data.

## 3. Held out

- **Variants:** 20% of LacI variants, split by position (whole positions held out), not at random.
- **Trajectories:** all trajectories under one held-out inducer concentration.
- **No test-set tuning.** Hyperparameters are chosen on validation only; the split is committed to the repository before training.

## 4. Success metrics (all three required)

1. **Fitness recovery:** Spearman correlation between $-J_\psi$ and measured phenotype on held-out variants, compared against a fitness-only model with the same architecture ($\lambda_2=0$).
2. **Trajectory fit:** held-out trajectory NLL and dynamic-time-warping distance to held-out expression paths, compared against a dynamics-only model ($\lambda_1=0$).
3. **Attractor agreement:** let $M_J$ be the set of local minima of $J_\psi$ in the observed range, and $M_H$ the attractors of the Hopfield baseline (arm D, discrete dynamics). Report a set-matching score: Hungarian matching under a distance threshold fixed in advance, with precision and recall of matched minima. Not "visual agreement".

## 5. The result that would kill the unification hypothesis

The hypothesis is **rejected** if the jointly trained $J_\psi$ is worse than *both* single-objective controls on their own metric (joint fitness Spearman < fitness-only, **and** joint trajectory NLL > dynamics-only), for arms A and B, on the held-out split. That would mean one field cannot serve both roles without cost, and the Level-2 correspondence does not extend to a shared object. A weaker negative: the minima of $J_\psi$ do not match the observed stable states (set-matching recall < 0.5 at the pre-set threshold).

## 6. Minimal prototype that may be run first (optional)

Reuse the synthetic double well of the capacity benchmark: simulate trajectories by Euler–Maruyama under the known $U$, add fitness labels, and check that arms A/B recover both the minima and the trajectory statistics while arms C/D fail. This is a software test of the pipeline, not evidence for the hypothesis, and it must be reported as such.
