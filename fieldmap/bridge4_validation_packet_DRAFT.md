# Bridge 4 — Validation packet (DRAFT, half-complete)
## Fitness seascapes ↔ morphogen-parameterised Waddington landscapes: is the shared control *u* the same object?

**Status.** The Cislo side is read in full. The Mustonen–Lässig side is **pending**: the 2009 *Trends Genet* review is closed-access, and the 2010 *PNAS* paper that formalises the seascape could not be downloaded automatically (PNAS and PMC return 403). Nothing below says what the seascape papers contain beyond their abstracts. The seascape half is written as **questions the full text must answer**, fixed before reading.

**Why this pair.** The field map names the control variable *u* as "the cheapest unification": drug dose or environment on the fitness side, morphogen dose on the fate side. In Paper B's template *u* is the input to the transition, $x_{t+1}=T(x_t,u_t)$. It is also the harness input in the program's framing $C=f(\text{state},\text{environment},\text{history},\text{time})$. Among the eight papers re-rated under the Table 1 rule, only the two fate-side papers (dynamo, Cislo) fill *u* as a computable component. Whether a fitness-side paper does is the open question.

**Selection disclosure.** This pair was nominated by the field map (hand-curated), not by the detector. It is a hand-selected case, like Ding–Fard.

---

### A. Cislo et al. 2025 — model card (full text, PNAS, doi:10.1073/pnas.2521762122)

| Role | Computable object in the paper | Rule verdict |
|---|---|---|
| **x** state | Single-cell expression vector (multicolour flow cytometry of a TF code; scRNA-seq), represented as a point cloud $\hat M=\{x_i\}$ in feature space | Component |
| **φ** representation | None used for computation. Dynamics run directly on the point cloud; the diffusion map is used only to *display* density | **Empty** (rule b) |
| **J** scalar field | $U_D(x\mid\theta)=U_B(x)+U_I(x)$, with base potential $U_B=-\log p_B$ (KDE on the manifold) and $U_I$ the minimiser of the squared-Laplacian energy (Eq. 8) under fixed-point height constraints $h^*_i$ (Eqs. 9–10) | Component |
| **T** transition | Langevin dynamics $\dot x=-g^{-1}(x,t\mid\theta)\nabla U(x,t\mid\theta)+\eta$, $\langle\eta\eta'\rangle=2D\delta$ (Eqs. 1–2); discretised as a transfer operator on $\hat M$: $P(x_i,t_{k+1})\propto V(x_i)\sum_j\exp[-\lVert x_i-x_j-\epsilon v(x_j)\rVert^2/4D\epsilon]\,P(x_j,t_k)$ (Eq. 6) | Component |
| **π** trajectory rule | Forward evolution of the state *distribution*. Fate proportions are read off as basin probabilities; fixed points, saddles and unstable manifolds come from topological extrema detection | Component |
| **u** exogenous input | Morphogen dose θ (SAG). One potential is fitted per dose; untested doses come from linear barycentric interpolation; dose *histories* come from chaining potentials (irreversibility after transient exposure) | **Component** |
| **F** feedback | None. θ(t) is imposed from outside; the cell state never changes the landscape | **Empty** |

**Fitting.** Adjust $\{h^*\}$, $g$ and $D$ to minimise the relative entropy between observed and simulated snapshot distributions $P(x_i,T_K\mid\theta)$ (Table 1, Steps 1–4). The effective potential is $U_{\text{eff}}=-gD\log p_{\text{eq}}(\theta)$.

**Validation reported.** On synthetic data the method recovers a known heteroclinic-flip potential and extrapolates a bifurcation diagram from three fitted parameter sets. On mESC ventral neural-tube differentiation it reproduces observed fate proportions, interpolates to untested SAG doses, and predicts outcomes for time-varying SAG protocols.

**Assumptions stated by the paper.** Morse–Smale (gradient-like, structurally stable) dynamics, no cell–cell coupling in vitro, and a spatially uniform metric $g=gI$ in the fitting pipeline.

### B. Mustonen & Lässig — questions fixed before reading

For a Level-2 or Level-3 correspondence with Cislo, the seascape formalism would need all of the following. Each is answered from the full text **or marked unanswered**, never from memory.

1. **x**: is the state a genotype, or a *population* (allele-frequency vector)? If it is a population, the analogue of Cislo's point cloud is a distribution over populations, not over genotypes.
2. **J**: is fitness $F(x,t)$ a scalar over the same state that the dynamics act on?
3. **T**: are the population dynamics written as a diffusion with drift given by a fitness *gradient* in some metric, with noise set by population size? If so, what are the metric and the effective $D$?
4. **u**: is the time dependence of $F$ exogenous (environment-driven) or endogenous (frequency-dependent)? Only exogenous time dependence corresponds to Cislo's θ(t). Endogenous time dependence would be a feedback term F, which Cislo lacks.
5. **Fitting**: does either paper *infer* a seascape from data, or only posit one and derive consequences (the fitness-flux theorem)? The abstract of the 2010 paper points to the second.

### C. Verdict — deferred

- **Level 1 (shared vocabulary):** yes, trivially ("landscape", "time-dependent").
- **Level 2 (role structure):** *provisional* on Cislo alone. x, J, T, π and u are filled; φ and F are empty.
- **Level 3 (same mathematical object):** **not assessed.** The candidate claim is that both are overdamped Langevin / Fokker–Planck dynamics under an exogenously time-dependent scalar potential. That candidate depends entirely on Q3 and Q4 above.

### D. Failure modes to check once both sides are read

- **Different state spaces.** Cislo's x is one cell. If the seascape's x is a population frequency vector, the two potentials live on different objects, and a correspondence would have to be population-of-cells ↔ population-of-genotypes, not cell ↔ genotype.
- **Inference vs theory.** Cislo fits U from data; the seascape work may only posit F. If so, the bridge is methods transfer (Cislo's inference applied to evolution data), not an equivalence.
- **Feedback smuggled in as u.** Frequency-dependent selection or niche construction would make the seascape's time dependence endogenous. That fills F, not u, and breaks the analogy with morphogen dose.

### E. Proposed synthetic test (to run after B is answered — not run)

Simulate Wright–Fisher populations (two loci, multiple replicates) under a known **exogenously switching** fitness seascape. Collect allele-frequency snapshots across replicates at fixed times. Fit them with a Cislo-style pipeline (heights by relative entropy on snapshot distributions, one potential per environment, chaining across the switch).

- **Pass:** the fitted potential recovers the seascape's optima and the post-switch transient.
- **Fail:** it does not, or it needs a non-gradient drift term. That tells us whether Cislo's inference machinery transfers to evolution data.
- **Negative control:** the same pipeline on a *frequency-dependent* (endogenous-feedback) seascape. This should fail the gradient-like assumption.

*Data: `fieldmap_rerated_15.csv`. Full texts read: `articles/10.1073_pnas.2521762122.txt`.*
