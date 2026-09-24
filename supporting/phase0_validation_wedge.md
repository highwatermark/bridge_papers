# Phase 0 — The Validation Wedge
### Three disconnected papers running the same computation: from hidden bridge to worked example

*The unlock: we built a method that detects candidate computational isomorphisms across disconnected literatures. This is the next step — algorithm-level validation on three concrete bridges. Each pair is real, drawn from the 522-paper two-pillar corpus, selected as concept-nearest across the pillars, with **zero shared citations**. The shared algorithm is the credibility wedge; "what neither paper sees" is the discovery each bridge suggests.*

**The wedge format, applied three times:** *Here are two papers that appear to be solving the same computational problem → here is the shared algorithm → here is the translation → here is the experiment or model the bridge suggests.*

---

## The load-bearing isomorphisms

From the deep-connectivity analysis, two computational roles carry the bridge: **STATE** (genotype/sequence ≈ cell state/attractor) and **OBJECTIVE** (fitness landscape ≈ epigenetic/potential landscape). The three seed bridges below are chosen to instantiate the highest-value isomorphisms one at a time — STATE, OBJECTIVE, and REPRESENTATION — so each worked example is narrow, formal, and hard to dismiss.

---

## Bridge 1 — STATE · genotype/sequence ≈ cell state/attractor

**Two papers, no shared citation, concept similarity 0.44:**
- **Evolution-ML:** "Evolutionary velocity with protein language models predicts evolutionary dynamics of diverse proteins" (PLM, https://openalex.org/W4210494137)
- **Systems-harness:** "Cell Fate Decision as High-Dimensional Critical State Transition" (systems-harness, https://openalex.org/W2952938648)

**The shared algorithm.** Both learn a **vector field over a high-dimensional state manifold and read out the direction of motion.** The protein language model computes an "evolutionary velocity" — the likelihood gradient that points from a sequence toward its probable descendants. The cell-fate model treats a differentiation decision as a **critical state transition** — a trajectory crossing a boundary in expression-state space. Same object: a state, a potential, and a predicted trajectory on it.

| Role | Evolution-ML reads it as | Systems-harness reads it as |
|---|---|---|
| STATE **(load-bearing)** | protein sequence as a point in embedding space | cell as a point in expression state space |
| Transition operator | mutational move → embedding displacement | signal/noise → displacement across the critical boundary |
| Objective | LM likelihood gradient (velocity field) | potential/stability gradient of the attractor basin |
| Search | predicted evolutionary trajectory | cell-fate trajectory through the transition |
| Representation | protein language-model embedding | low-dimensional critical-state manifold |
| Feedback | selection filters realized substitutions | developmental signal commits the decision |

**What neither paper sees.** The PLM side has no notion of a *critical boundary* where the dynamics become singular; the cell-fate side has no *generative sequence prior*. **The experiment the bridge suggests:** use the language-model velocity field to locate the sequence-space analog of a saddle/critical point — the mutations sitting at a fold-or-fate tipping edge — and test whether they are the ones with maximal phenotypic leverage.

---

## Bridge 2 — OBJECTIVE · fitness landscape ≈ epigenetic/potential landscape

**Two papers, no shared citation, concept similarity 0.43:**
- **Evolution-ML:** "Deciphering protein evolution and fitness landscapes with latent space models" (ML_DE, https://openalex.org/W2995361046)
- **Systems-harness:** "Modeling the Attractor Landscape of Disease Progression: a Network-Based Approach" (systems-harness, https://openalex.org/W2606991676)

**The shared algorithm.** Both **fit a scalar potential over a learned latent state and treat trajectories as descent/transition on that surface.** The fitness-landscape model learns a latent coordinate in which height = fitness; the disease-attractor model learns a latent coordinate in which depth = attractor stability. The mathematics — a scalar field over a latent manifold, with dynamics as motion on it — is identical.

| Role | Evolution-ML reads it as | Systems-harness reads it as |
|---|---|---|
| State | genotype in a latent fitness coordinate | network state in a latent disease coordinate |
| Transition operator | mutation moves genotype on the surface | perturbation moves the network between attractors |
| OBJECTIVE **(load-bearing)** | scalar fitness = height of the surface | scalar potential = attractor depth |
| Search | adaptive walk = ascent | disease progression = descent between basins |
| Representation | latent-variable fitness-landscape model | network-inferred potential landscape |
| Feedback | selection re-weights the population | microenvironment reshapes attractor depths |

**What neither paper sees.** Fitness landscapes are fit to *populations at equilibrium*; disease attractor landscapes are fit to *single trajectories in time*. Neither models both. **The model the bridge suggests:** a **time-resolved fitness surface (a "seascape") whose minima are inferred as network attractors** — directly testable where longitudinal deep-mutational-scan data and expression-state trajectories exist for the same system.

---

## Bridge 3 — REPRESENTATION · sequence→regulatory readout ≈ GRN/cell-fate program

**Two papers, no shared citation, concept similarity 0.46:**
- **Evolution-ML:** "Species-aware DNA language models capture regulatory elements and their evolution" (GENOMIC_FM, https://openalex.org/W4393433029)
- **Systems-harness:** "Dissecting cell identity via network inference and in silico gene perturbation" (systems-harness, https://openalex.org/W4319591822)

**The shared algorithm.** Both **learn the map from regulatory input to expression state and use it to predict the effect of perturbing that input.** The DNA language model decodes regulatory elements from sequence context; the in-silico perturbation model dissects cell identity by perturbing a gene regulatory network. Both are learned regulatory-input → state readouts with a perturbation operator on top.

| Role | Evolution-ML reads it as | Systems-harness reads it as |
|---|---|---|
| State | DNA/regulatory sequence context | expression state defining cell identity |
| Transition operator | sequence edit → regulatory-activity change | in-silico TF perturbation → state change |
| Objective | likelihood of regulatory element given species | identity/GRN-consistency score of the state |
| Search | scan variants for regulatory effect | scan perturbations for reprogramming effect |
| REPRESENTATION **(load-bearing)** | DNA-LM embedding of regulatory grammar | inferred gene regulatory network |
| Feedback | cross-species conservation constrains grammar | perturbation outcome updates the GRN |

**What neither paper sees.** The DNA-LM knows the *evolutionary* grammar of regulatory elements but never runs a perturbation; the GRN model runs perturbations but has no *sequence-level, cross-species* prior. **The pipeline the bridge suggests:** use the DNA-LM to propose which sequence-encoded regulators are perturbable reprogramming levers, then score those candidates with the in-silico perturbation engine — a sequence-grounded reprogramming-target finder.

---

## Why this is the wedge

Each bridge is a **falsifiable equivalence claim**, not an analogy: it states that two models share a six-role computational structure, and it names a specific experiment that only becomes visible once you hold both papers in the same grammar. Validate one end-to-end and it becomes, in order:

1. **A short translation paper** — the cleanest of the three (Bridge 2, the OBJECTIVE isomorphism, is the most formal and hardest to dismiss).
2. **A demo** — the shared-grammar view rendered live for any paper pair.
3. **A founder memo** — this document.
4. **A collaborator-outreach artifact** — sent to the conceptual-bridge group (Sui Huang, Elena Álvarez-Buylla, Andrea Pagnani) whose own work already straddles both sides.
5. **The first module of ResearchOS** — the bridge-discovery engine, seeded by the three-space measure (primitive similarity, concept similarity, citation distance) that surfaced these pairs.

**The cascade:** translation becomes modeling (the harness operator H), modeling becomes simulation (the closed loop), simulation becomes discovery (recurring programs across organisms), and discovery becomes intervention design (state-transition drift as the disease frame).

---

## Method & honesty

The three pairs were selected by embedding each paper with a sentence-transformer, computing cross-pillar cosine similarity, and taking the concept-nearest systems-harness partner for a recognizable evolution-ML anchor in each target paradigm — then confirming by hand that the harness abstract genuinely concerns the target concept (cell-state transition, attractor/potential landscape, cell-fate GRN). This screens out the keyword-collision artifacts that pure primitive-similarity ranking produces. Because these three pairs were re-selected by concept-nearest partner (not drawn from the primitive-ranked 96-seed set), the zero-citation property was checked directly for them: reference lists for all six papers were re-fetched from OpenAlex and the pairwise overlap computed — **each pair shares 0 of its (71/54, 77/39, 60/92) references and neither paper cites the other.** Concept-similarity values are the measured cross-pillar cosines. The six-role translations are authored mappings grounded in the isomorphism catalog and the two abstracts; they are the *hypotheses to validate*, not yet validated equivalences. The next step — algorithm-level validation — is the actual scientific work these three wedges set up.

*Data: `phase0_validated_bridges.csv`, `phase0_bridge_translations.csv`, `phase0_seed_bridges.csv`. Figure: `fig13_phase0_bridges.png`.*
