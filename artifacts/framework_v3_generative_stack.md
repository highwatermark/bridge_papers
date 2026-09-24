# Framework v3 — the generative stack

*Evolutionary Pressure → Harness Inputs → State Transitions → Biological Programs → Regulatory Networks → Capability*

This ordering is a real advance over v2 (the descent stack), for one reason: **it reads in the causal/generative direction.** v2 started at the observed capability and dug down to explain it. v3 starts at the pressure and flows forward to the expressed capability — the same direction evolution's search actually runs, and the direction an AI system that *generates* biology would have to run. Two layers are also sharper than before:

- **State Transitions** (new): the trajectory the system takes under repeated stimulus and feedback — the *Time + Feedback* terms of your input equation made into an explicit modeling target, rather than being folded into "search dynamics."
- **Harness Inputs**: the environment and repeated stimulus as an explicit conditioning input, separated from the pressure (the objective) it induces.

## The empirical finding this ordering exposes

When you score each layer by **how well the field currently models it as a learnable object** (1–5, domain judgment) against **how much corpus activity sits adjacent to it** (paper counts from the 404-paper classified set), a sharp pattern appears — see `fig5_generative_stack.png` and `generative_stack_layers.csv`:

| Layer | Modeled as learnable (1–5) | Adjacent corpus n |
|---|---|---|
| Evolutionary Pressure | 2 | 104 |
| Harness Inputs | 1 | ~0 |
| State Transitions | 2 | 144 |
| **Biological Programs** | **5** | 95 |
| Regulatory Networks | 3 | 29 |
| Capability | 4 | 134 |

**The field models the middle of the stack — the Programs and their expressed Capability — with high confidence, and the generative roots at the top barely at all.** ML reads the *products* of evolution's search (folds, functional sequences, phenotypes) but not the *process* that generates them (the pressure, the harness, the state transitions).

The mismatch between the two columns is the actionable part:

- **State Transitions: n≈144 adjacent, but modeled 2/5.** There is a large literature *near* this layer (forecasting, directed search) that publishes trajectories and dynamics without modeling the transition function itself as a learnable object. High activity, low depth — a layer ripe for a foundation-model treatment.
- **Harness Inputs: ~0 and 1/5.** The single biggest blind spot. Almost nothing in the corpus treats the environment/stimulus as an explicit, learnable input that conditions the search. Your input equation makes it a first-class term; the field has abstracted it into a fixed training set.
- **Evolutionary Pressure: n≈104 but 2/5.** Fitness is measured as scattered point-observations (deep mutational scans, resistance assays), never learned as a general scoring function that could be *reused* across systems.

## Why this matters for the thesis

Your thesis is that evolution's search generates **reusable** programs. The field has proven the *reusability* of the programs themselves — a protein language model trained on evolution's outputs transfers zero-shot across families. What it has **not** built is a learnable model of the **generative machinery** — the pressure, harness, and transition dynamics that *produce* new programs. That is precisely the top half of your v3 stack, and precisely where the 1s and 2s sit.

So the roadmap your own framework implies:
1. **Make the harness learnable** — an explicit, conditioning model of environment + stimulus (the emptiest layer).
2. **Make state transitions a foundation-model target** — learn the transition function under feedback, where activity is high but depth is low.
3. **Make pressure a reusable scoring function** — generalize fitness from point-measurements to a transferable objective.

Close those three and you have an AI system that runs the stack **top-down** — choose a pressure and harness, roll the transitions, emit a novel program — which is the generative capability your vision describes. Today's field runs it only bottom-up (observe a program, read it).

## Method & honesty notes
- Layer→capability mapping and the adjacent-n counts are in `generative_stack_layers.csv`; counts sum the on-target paper counts of the capabilities that engage each layer (transparent, unweighted, so a capability spanning two layers is counted in both).
- The 1–5 "modeled as learnable" scores are domain judgment, not corpus measurements — they encode where the modeling depth actually is and should be debated. The corpus-n column is measured.
- Built on the same 404-paper off-topic-filtered classified set as the pass-2 dossier; trend/growth claims use 2015–2024.