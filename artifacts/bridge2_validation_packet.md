# Bridge 2 — Validation Packet
## Fitness landscapes ≈ epigenetic/potential landscapes: are they the same computational object?

**The claim under test.** Two papers with zero shared citations and cross-pillar concept similarity 0.43 appear to solve the same problem — represent a biological system as a **scalar field over a latent state, with trajectories interpreted as motion across that field.** This packet reads both papers in full, extracts their actual mathematics, and adjudicates the equivalence at three levels.

- **Evolution-ML:** Deciphering protein evolution and fitness landscapes with latent space models — Xinqiang Ding, Zhengting Zou, Charles L. Brooks, *Nature Communications* 2019 (10.1038/s41467-019-13633-0)
- **Systems-harness:** Modeling the Attractor Landscape of Disease Progression: a Network-Based Approach — Atefeh Taherian Fard, Mark A. Ragan, *Frontiers in Genetics* 2017 (10.3389/fgene.2017.00048)

Both full texts were retrieved and parsed (88k and 53k characters); model definitions below are quoted/paraphrased from the methods, not the abstracts.

---

## 1. The two models, extracted

### Ding et al. — latent-space fitness model
- **State** x: a protein sequence, one-hot over MSA columns.
- **Representation** z = φ(x): a **variational autoencoder** encoder q_φ(z|x) compressing the sequence to a 2-D latent point. Trained by maximizing the **ELBO**: `E_q[log p(x|z)] − KL(q(z|x)‖p(z))`, with prior p(z)=N(0,I).
- **Objective / scalar field** J(z): a **Gaussian-process regression** f(z) with an RBF kernel over the latent coordinate, fit to experimental fitness/stability labels. Predicts a continuous scalar (protein melting temperature T50) with Pearson 0.80 ± 0.06 from the 2-D latent alone.
- **Transition / search**: mutations move x, hence z; an adaptive walk is motion on J(z).

### Taherian Fard & Ragan — attractor-landscape model
- **State** P(t): a gene-expression pattern vector (network state).
- **Representation**: a **Hopfield network** whose weight matrix W is the gene–gene Pearson correlation (w_ij = PCC(i,j), w_ii = 0) — explicitly "inspired by Conrad Waddington's epigenetic landscape."
- **Objective / scalar field** E: the **Lyapunov energy** `E[P] = −½ P W Pᵀ`. Attractors are local minima; the landscape is visualized by interpolating E over the first two principal components.
- **Transition / search**: the discrete Hopfield update `P(t+1) = sgn(P(t) W)`; disease progression is the trajectory converging to an attractor.

---

## 2. The shared formal template

Both models populate the same six-slot template:

| Symbol | Role | Ding (fitness) | Fard (attractor) |
|---|---|---|---|
| x ∈ 𝒮 | state | protein sequence | expression pattern P |
| z = φ(x) | representation | VAE latent (2-D) | Hopfield state on W |
| J(x) | **scalar field** | GP fitness f(z) | Lyapunov energy E[P] |
| x_{t+1} = T(x_t,u_t) | transition | mutation → Δz | P(t+1)=sgn(PW) |
| π | search/trajectory | adaptive walk (ascent) | convergence to attractor (descent) |
| F | feedback | selection re-weights population | microenvironment rewires W over stages |

At this level the mapping is exact and every slot is filled on both sides. **The role structure is genuinely shared.**

---

## 3. The hard question: three levels of equivalence

**Level 1 — same vocabulary after translation?** Yes, trivially. Both talk about "landscapes," "trajectories," "states." This is the weakest claim and not sufficient.

**Level 2 — same algorithmic role structure?** **Yes.** Both fit a scalar field over a learned latent state and read dynamics as motion (ascent/descent) on that field toward extrema that are the biologically meaningful states. Every role in the template is occupied by a real, non-trivial component in each paper. This is the substantive finding: two disconnected literatures independently built the same six-role algorithm.

**Level 3 — same mathematical object?** **No — and this is the load-bearing result.** Ding's J(z) is a **Gaussian process**: a nonparametric, universal function approximator that can represent an arbitrary multi-well surface. Fard's E[P] = −½PWPᵀ is a **fixed quadratic form** parameterized by a single correlation matrix W; it is a paraboloid (up to the sign pattern of W's eigenvalues) and **cannot represent two separated minima in a single basin structure without additional machinery.** The two are the same *type* of construct (a scalar potential) but not the same *object*.

---

## 4. Synthetic reimplementation — the falsifiable test

I built a ground-truth **double-well potential** U(s) over a 2-D state (two attractors: "normal" and "disease"), sampled cells near each well plus intermediate transient states, and independently fit **both** formalisms to the same data:

- **Ding path**: GP regression of scalar fitness = −U over the state → **Spearman 1.00** with ground truth; **recovers all basins.**
- **Fard path**: Hopfield energy from the samples' correlation network → **Spearman 0.34**; **finds 0 interior minima** — the quadratic form collapses the double well into a single saddle.

*(figure: fig14_bridge2_validation.png; data: bridge2_synthetic.npz)*

**Interpretation.** The synthetic test confirms Level 2 and refutes Level 3, quantitatively. Both models are correctly described as "scalar field over latent state, trajectories as motion" — but the Hopfield energy is a **structurally limited special case** of the general potential that the GP can represent. This is not a defect of the bridge; it is the bridge's most valuable output: it tells you exactly what to build next.

---

## 5. Failure modes

1. **Equilibrium vs trajectory.** Ding fits a *static* surface to populations at equilibrium; Fard's is a *dynamical* system with an explicit time-update. Neither models both — the fitness surface has no dynamics, the Hopfield model has no learned surface shape.
2. **Representational capacity mismatch (Level-3 failure).** GP: universal; Hopfield energy: quadratic. Any bridge that treats them as interchangeable will over-claim.
3. **What "latent" means differs.** Ding's z is *learned* (VAE); Fard's state lives on a *fixed* PCA/correlation basis. The learning is on opposite sides — Ding learns the representation and fixes the objective family; Fard fixes the representation and reads off the objective.
4. **Direction convention.** Fitness is maximized (ascent), energy is minimized (descent); the sign flip is trivial but must be stated or cross-correlations invert (observed: raw cross-Spearman −0.45 before sign alignment).

---

## 6. The canonical-paper synthesis

The bridge suggests a model **neither paper contains**: a **time-resolved fitness surface ("seascape") whose minima are inferred as network attractors** — i.e., replace Fard's fixed quadratic energy with a Ding-style *learned* potential (GP or normalizing-flow), and give Ding's static surface Fard's *dynamical* update. The result is a single object: a learned scalar field with an explicit transition operator, fit jointly to longitudinal deep-mutational-scan + expression-trajectory data. That unification is the canonical paper — and the Level-3 gap found here is precisely its motivation.

---

## 7. Negative controls — the mapping rejects false friends

To show the six-role mapping discriminates rather than pattern-matches on vocabulary, I drew three **false-friend** pairs from the deep-connectivity analysis: high concept similarity, low primitive similarity. In each the **dominant computational role differs**, and the mapping rejects the pair:

- **OBJECTIVE vs STATE** (concept 0.756, primitive 0.239): *Generative modeling of single-cell time series with …* ‖ *FateNet: an integration of dynamical systems and dee…*\n  Both about single-cell time-series / cell fate (concept 0.76). But PRESCIENT is a generative model — its weight is on OBJECTIVE+REPRESENTATION (fit a probability flow); FateNet's weight is on STATE+TRANSITION (classify where a cell sits and where it goes). Dominant role OBJECTIVE vs STATE: the mapping rejects — they occupy different roles in the shared algorithm.
- **STATE vs REPRESENTATION** (concept 0.63, primitive 0.0): *Effective gene expression prediction from sequence b…* ‖ *TENET: gene network reconstruction using transfer en…*\n  Both 'gene expression from sequence/network' (concept 0.63). Enformer is a pure STATE readout (sequence→expression, one shot); TENET reconstructs a network — a REPRESENTATION built from transfer entropy. STATE vs REPRESENTATION dominant: same words, different computational job. Rejected.
- **REPRESENTATION vs SEARCH** (concept 0.651, primitive 0.226): *Prediction of protein–ligand binding affinity from s…* ‖ *Learning Pathway Dynamics from Single‐Cell Proteomic…*\n  Both 'predict from proteomic/sequencing data' (concept 0.65). Binding-affinity prediction is a static REPRESENTATION→scalar map; pathway-dynamics learning is a SEARCH over TRANSITION trajectories in time. REPRESENTATION vs SEARCH dominant: one is static, one is dynamical. Rejected.

These are the control that makes Bridge 2 credible: the same procedure that accepts fitness≈attractor at Level 2 **rejects** these three at the role level, despite their higher surface (concept) similarity. A bridge is only interesting when the negative controls fail.

---

*Artifacts: fig14_bridge2_validation.png · bridge2_model_facts.json · bridge2_synthetic.npz · false_friend_controls.csv · phase0_validated_bridges.csv (citation-overlap verified: 0 shared references).*
