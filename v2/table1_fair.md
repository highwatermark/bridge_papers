### Table 1 — Six-role template, with each slot audited as component or re-description

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

This table supersedes Table 1 of Variants A–C, which listed all six slots as filled on both sides.
