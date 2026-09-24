# Auto-research loop & the connectivity paradigm

*An operational design for a closed-loop system that wires the "modeled-next-door" systems-biology literature into the evolutionary-search frame — closing the 2% gap and turning C = f(Biological State, Environment, History, Time) into a running machine.*

## The core idea

The two literatures are complementary, not competing. When I score each loop module by keyword presence in the evolution-ML corpus (1,766 papers) vs. the systems-biology state-transition corpus (758 papers), the modules **split almost perfectly by literature** — each side owns exactly what the other lacks (`loop_module_connectivity.csv`):

| Module | evolution-ML % | systems-bio % | Owner | Asymmetry |
|---|---|---|---|---|
| M1 Observe / ingest | 27.1 | 34.3 | shared | −7 |
| **M2 Harness operator H** | 6.7 | 47.4 | **systems-bio** | **−41** |
| M3 Pressure / objective | 28.6 | 11.7 | evolution-ML | +17 |
| M4 Evolutionary search | 38.7 | 10.9 | evolution-ML | +28 |
| M5 Program representation | 20.0 | 6.9 | evolution-ML | +13 |
| M6 Capability prediction | 46.6 | 39.7 | shared | +7 |
| M7 Validate / feedback | 19.3 | 21.2 | shared | −2 |

The Harness (M2) is the largest asymmetry in the entire analysis — **+41 points to systems-biology, the exact layer evolution-ML is missing.** Search, Pressure, and Representation (M3–M5) tilt the other way. This complementarity *is* the design principle: **the loop only closes if every module is wired across both literatures.** That shared wiring is the connectivity paradigm.

## The connectivity paradigm

A single **shared interface** that both literatures plug into: the **(state, program) pair**.

- A **biological state** is a point systems-biology models (a cell's expression/regulatory configuration; an attractor).
- A **program** is a reusable object evolution-ML models (a sequence/structure encoded in a foundation model).
- The Harness operator H is the map between them under an environmental signal: `H: (state, signal) → state′`, and a program is what makes H's landscape what it is.

Both fields already compute on one half of this pair. The connectivity paradigm is the commitment to a **common representation of the (state, program) interface** so that a systems-biology transition model and an evolution-ML foundation model read and write the *same* object. Everything below is how the loop enforces that.

## The seven modules (each wired across the gap)

**M1 — Observe / ingest** *(shared)*
Ingest paired data: state-transition measurements (single-cell time courses, perturbation screens) *and* evolutionary data (homolog families, DMS). Wiring: the same samples must carry both a state label and a program (sequence) label — the join key of the whole loop.

**M2 — Harness operator H** *(systems-bio owns; the critical import)*
Learn `H: (state, signal) → state′` from perturbation data using the systems-biology toolkit (GRN inference, dynamical-systems / critical-transition models). Wiring: expose H's inputs/outputs in the connectivity paradigm's (state, program) representation so the evolutionary search (M4) can call H as its fitness-evaluation environment.

**M3 — Pressure / objective** *(evolution-ML owns)*
Infer the objective the observed transitions optimize — the selection pressure. Wiring: instead of a hand-set fitness function, *learn* pressure as a reusable scoring function over states reached through H (the "make pressure transferable" goal from the prior roadmap).

**M4 — Evolutionary search** *(evolution-ML owns; the engine)*
Run an evolutionary algorithm whose **fitness evaluation is H** and whose objective is M3's learned pressure. This is the literal instantiation of the EA↔biology table: the EA proposes programs, H+pressure score them by the states they induce. Wiring: search operates in M5's program representation, scored by M2's systems-biology operator — both literatures in one loop step.

**M5 — Program representation** *(evolution-ML owns)*
Encode candidate programs in a reusable foundation-model latent (protein/genomic LM). Wiring: the latent must be decodable to a state via H — i.e. the representation is trained to be *compatible with* the transition operator, not independent of it.

**M6 — Capability prediction** *(shared)*
Forward-simulate `C = f(state, environment, history, time)` — roll H under a stimulus schedule and read out the capability. Wiring: this is where the state function is actually evaluated; it consumes M2 (H), M5 (program), and the environment/history inputs jointly.

**M7 — Validate / feedback** *(shared; closes the loop)*
Test predictions in silico or wet-lab. **The discrepancy between predicted and observed state transitions is the loop's error signal** (red arc in `fig7_auto_research_loop.png`): it refines H (M2), the pressure model (M3), and the search (M4). Wiring: active-learning selection of the next experiment maximizes information about the *worst-connected* part of the (state, program) interface — the loop preferentially repairs its own weakest wiring.

## Why this closes the gap rather than restating it

The 2% overlap means these modules are currently built in isolation: systems-biology builds M2 with no M4 to call it; evolution-ML builds M4/M5 with a fixed training set standing in for M2. The loop forces them into one object:

- **M2 becomes callable by M4** — a transition operator used as a fitness environment, which neither field does today.
- **M5 is trained to be H-compatible** — a program representation that decodes to a state, not an abstract embedding.
- **M7's error signal updates both sides** — one gradient flows through systems-biology (H) and evolution-ML (search/representation) components simultaneously.

The scientific test is the one from the prior roadmap, now runnable: does the loop, driven only by data and its own error signal, **rediscover the reusable programs biological evolution actually found** (validated against ancestral reconstruction / real adaptation), and generate viable new ones? If yes, the EA↔biological-evolution correspondence is not just formalized but *operational*.

## Build order (minimal viable loop first)

1. **Single system, full loop, small** — pick cell-fate reprogramming (dense data, known signals, existing GRN models). Build M1→M2→M6→M7 first: ingest, learn H, predict C, validate. This proves the state-function backbone without the search.
2. **Add the search arm** — M3→M4→M5: learn pressure, run the EA with H as fitness, represent programs. Now the loop *generates*.
3. **Close and iterate** — turn on M7's error signal to all three of H, pressure, search. Measure whether closed-loop iteration improves rediscovery/generation over open-loop.
4. **Transfer** — repeat on a second system; test whether H, pressure, and representation modules transfer (the reusability claim at the module level).

## Method & honesty notes
- Module ownership is measured by keyword presence per corpus (`loop_module_connectivity.csv`); keyword lists are transparent and in the code. Percentages are the fraction of each corpus whose title+abstract contains any module keyword — a coarse but honest proxy for "which literature works on this module."
- The architecture is a design proposal grounded in the corpus complementarity, not an implemented system. Module data sources (single-cell, DMS, GRN models) are named from the anchor papers in the two corpora, not benchmarked here.
- The 2% overlap and the per-module percentages are measured; the loop design and build order are engineering judgment.