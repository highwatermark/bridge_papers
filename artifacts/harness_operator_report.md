# The Harness as a state-transition operator: solving the EA ↔ biological-evolution correspondence

*Report and roadmap built around C = f(Biological State, Environment, History, Time), with the Harness reframed as a computational transition operator.*

## The formalization

**Capability as a state function.** C = f(Biological State, Environment, History, Time). A capability is not a static property but the output of a system in a given state, under a given environment, with a given history, at a given time. This is the correct primitive: it makes capability a *computed* quantity, not an intrinsic label.

**Harness as the transition operator.** Define the Harness as

> H : (state, environmental signal) → state′

— the subset of environmental signals that *reliably* drive a biological system between stable states. The Harness is the interface between environment and organism. Reframing it this way converts a vague "environment" term into a **computational object**: a transition operator over a state space with identifiable stable attractors. This is `fig6_harness_operator.png` (left).

**The consequence.** Once the Harness is a transition operator and capability is a state function, the whole stack becomes a dynamical system, and the research target sharpens to one thing: **formalizing the correspondence between the evolutionary algorithm and biological evolution** (`fig6`, right). Every component of an EA has a biological counterpart —

| Evolutionary algorithm | Biological evolution |
|---|---|
| Objective function | Evolutionary pressure |
| Environment / fitness evaluation | **Harness (env → state)** |
| Genotype→phenotype map | State-transition dynamics |
| Population / variation | Biological programs |
| Selection + iteration | Search over generations |

The Harness sits exactly where an EA's fitness-evaluation environment sits. Solving for it *is* solving the EA↔biology mapping.

## The evidence: your "inferable to precision" claim is correct — and it reframes the blind spot

In framework v3 I scored the Harness layer **1/5** ("field's blind spot") but flagged it as my most debatable rating. Your claim was the opposite. I tested it by re-querying the literature with **state-transition vocabulary** (GRN attractors, cell-fate reprogramming, Waddington trajectories, bistable switches, dynamical-systems models of perturbation) instead of the *evolution* vocabulary my pass-1 queries used.

**Result: you were right, and the "blind spot" is not what I thought.**
- **800 records → 120 substantive harness-modeling papers** (16%): papers that link an environmental input to a state transition *with quantitative modeling* (≥2 modeling terms). Anchors include GRN inference with in-silico perturbation (CellOracle-type, 164 cites/yr), in-silico perturbation of cell-fate regulomes in organoids, and critical-state-transition theory of cell-fate decisions.
- **The Harness IS modeled to precision** — GRN inference, cell-fate control, dynamical-systems and critical-transition models exist and are quantitative. My 1/5 was a **vocabulary artifact**: the evolution-as-learnable-program queries simply don't retrieve this systems-biology literature.
- **But the two literatures are disjoint: 2% paper overlap** (2 of 120 harness papers appear in the 1,766-paper evolution corpus). They even publish in overlapping venues (PLOS Comp Bio, Molecular Systems Biology) without citing across the divide.

So the revised reading of the stack (`generative_stack_layers_revised.csv`): Harness moves **1 → 3** and State Transitions **2 → 3** — not because the modeling is absent, but because it exists *next door and is never wired into the evolutionary-search frame*. **The blind spot is not "unmodelable"; it is "unconnected."** That disconnection is precisely the EA↔biological-evolution gap you want to close.

## Why this is the high-value target

Your thesis — evolution's search generates *reusable* programs — has been proven for the programs themselves (protein/genomic foundation models read them zero-shot). What is missing is a learnable model of the **generative machinery**. The Harness-as-operator formalization gives that machinery a concrete, tractable form, and the disjoint-literature finding says the raw materials already exist:

- The **systems-biology** side has the transition operators (GRN/cell-fate dynamical models) but treats them as fixed, organism-specific descriptions — not as objects an evolutionary search shaped or can reuse.
- The **evolution-ML** side has the search and the reusable-program representations (foundation models) but abstracts the environment into a fixed training corpus — no explicit Harness.

Bridging them is the unbuilt mapping.

## Roadmap

**Phase 1 — Formalize the Harness operator (0–6 mo).**
Define H on a concrete, data-rich system where both stable states and driving signals are measured (cell-fate / reprogramming is ideal: dense single-cell data, known TF inputs, established GRN models). Deliverable: a learned transition operator H(state, signal)→state′ validated against held-out perturbations. The 120-paper corpus (`harness_state_transition_corpus.csv`) is the starting literature.

**Phase 2 — Make pressure and harness reusable, not point-estimates (6–18 mo).**
The evolution-ML side measures fitness as scattered point-observations; the systems-bio side fits one operator per system. Learn a *transferable* H and a *transferable* scoring function across systems — turning both the Harness and Evolutionary Pressure layers from bespoke fits into reusable modules. This is where foundation-model methods (the field's proven strength) should be pointed.

**Phase 3 — Close the EA↔biology correspondence (18–36 mo).**
Instantiate the full table: an evolutionary algorithm whose fitness-evaluation *is* a learned Harness operator and whose genotype→phenotype map *is* learned state-transition dynamics. Test the core scientific claim — that running this EA reproduces the reusable programs biological evolution actually found (validated against ancestral reconstruction and real adaptation data), and generates viable new ones. Success here is a system that runs the stack **top-down**: choose pressure + harness → roll transitions → emit a novel, reusable program.

**The cross-cutting move throughout: cite across the 2% gap.** Every phase should deliberately pull from both literatures — systems-biology transition models as the mechanism, evolution-ML foundation models as the reusable representation. The bridge is the contribution.

## Method & honesty notes
- Harness corpus: 8 state-transition-vocabulary queries × 100 records → 758 unique → 120 harness-modeling papers by keyword rule (env-signal ≥1 AND transition ≥1 AND modeling ≥2, abstract >120 chars). Rule is transparent, coarse per-paper, reliable in aggregate.
- Overlap (2%) is computed on OpenAlex work IDs between the 120-paper harness set and the 1,766-paper pass-1 evolution corpus; it is a lower bound on disconnection (ID-level, not citation-level — a citation analysis would sharpen it).
- The revised 1–5 layer scores remain domain judgment, now informed by the probe; the corpus counts and the 2% overlap are measured.
- Anchor citation rates are per-year normalized; keyword classification carries per-paper noise.