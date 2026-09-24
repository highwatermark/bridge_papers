# ResearchOS — Bridge-Validation Harness & Agent Architecture
### The repeatable pipeline behind the Bridge 2 packet, generalized to the paper ecosystem

The Bridge 2 validation was done by hand this turn. Every step it required is a named, automatable module. This document specifies the harness (the pipeline + data contracts) and the agents (the autonomous workers) that turn "one validated bridge" into "a bridge-validation engine."

---

## The pipeline, as executed for Bridge 2

1. Two candidate papers + isomorphism hypothesis (from the three-space seed set).
2. Retrieve full text (not abstracts). → `fetch_article_fulltext` on both DOIs.
3. Extract the formal model: state, representation, objective, transition, search, feedback.
4. Populate the shared six-role template on both sides.
5. Adjudicate three equivalence levels (vocabulary / role structure / mathematical object).
6. Build a synthetic reimplementation that both formalisms are fit to; measure agreement.
7. Enumerate failure modes.
8. Run negative controls (false friends) through the same mapping; confirm rejection.
9. Emit the packet + the "what neither sees" synthesis experiment.

---

## The agents to build

Each agent is a scoped specialist with a typed input/output contract, so the pipeline runs unattended and every claim stays traceable.

**A1 · Bridge Scout.** Scans the corpus (three-space measure: primitive sim, concept sim, citation distance) and proposes candidate bridges. *Guardrail learned this session:* rank by concept-nearest with a hand-verifiable anchor, NOT raw primitive similarity — the latter surfaces keyword collisions (the Eucalyptus-genomics artifact). Output: ranked (evo_id, har_id, isomorphism, three-space scores).

**A2 · Paper Extractor.** Given a DOI, retrieves full text and extracts the formal model into the six-role schema (state / representation / objective / transition / search / feedback), quoting the methods. Output: structured model card per paper. *This is the highest-value agent* — it is what turns abstracts into equations.

**A3 · Template Aligner.** Maps two model cards onto the shared formal template and fills the correspondence table. Output: the six-role alignment.

**A4 · Equivalence Judge.** Adjudicates the three levels. Level 1 (vocabulary) and Level 2 (role structure) are text-reasoning tasks; **Level 3 (mathematical object) requires executable comparison** — it cannot be judged from prose, as Bridge 2 proved (GP vs quadratic form looked identical at Level 2). Output: L1/L2/L3 verdict + justification.

**A5 · Synthetic Reimplementer.** Writes runnable code that fits BOTH formalisms to a shared synthetic ground truth and measures agreement (correlation, recovered structure). This is the falsification engine. Output: figure + metrics + pass/fail on Level 3.

**A6 · Control Runner.** Pulls false-friend pairs (concept-high, primitive-low) and confirms the mapping rejects them. Output: negative-control table. *Without this the framework is not credible.*

**A7 · Packet Composer.** Assembles A2–A6 into the two-page memo and the "what neither paper sees" synthesis experiment. Output: the validation packet.

**Orchestration:** A1 feeds a queue; A2–A7 run per candidate; A4 and A5 form a loop (if Level-3 fails, A7 reframes the bridge as "partial equivalence + unification target," which is what happened for Bridge 2).

---

## The harness (data contracts)

- **Model card schema** (A2 output): `{paper_id, state, representation, objective, transition, search, feedback, quotes[], scalar_field:bool}`.
- **Alignment record** (A3): six rows, each `{role, evo_expr, har_expr, filled:bool}`.
- **Verdict record** (A4): `{L1, L2, L3, load_bearing_role, justification}`.
- **Synthetic result** (A5): `{ground_truth, metric_evo, metric_har, cross_metric, level3_pass:bool, figure}`.
- **Control record** (A6): `{pair, concept, primitive, evo_dom_role, har_dom_role, rejected:bool}`.

Every record is an artifact; the packet cites them by id. This is the audit trail that keeps the engine honest — the same trail that let this session's claims be checked and one ("verified zero-citation") be corrected.

---

## Skills to publish (so this is one call next time)

- **`bridge-extract`** — kernel helper `extract_model_card(doi)` : fetch full text + parse into the six-role schema.
- **`bridge-align`** — `align(card_a, card_b)` → template table + Level-1/2 reasoning scaffold.
- **`bridge-synthesize`** — `synthetic_equivalence_test(formalism_a, formalism_b)` → the A5 falsification harness with the double-well default.
- **`bridge-controls`** — `false_friends(evo_id, k=3)` → concept-high/primitive-low negative controls from the corpus.

Publishing these four turns the nine-step manual pipeline into `validate_bridge(evo_id, har_id)`.

---

## Status

- **Bridge 2 (formal paper):** validated this turn — Level 2 holds, Level 3 fails structurally, synthetic test confirms, controls reject. Ready to draft as the canonical paper.
- **Bridge 3 (demo):** next — DNA-LM scores regulatory perturbations → GRN/perturbation model ranks reprogramming levers.
- **Bridge 1 (visionary):** exploratory — critical-boundary behavior in sequence-embedding space.
