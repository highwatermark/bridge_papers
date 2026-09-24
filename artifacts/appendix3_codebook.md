# Appendix 3 — Annotation codebook for the precision study (one page)

**Task.** For each pair of papers (A, B) in `rater_sheet_N150_BLIND.csv`, decide whether the two papers implement the same *computational role structure*. You see titles and abstracts only; open full texts only when the label would otherwise be **cannot tell**. You are not told which stratum a pair came from, which literature each paper belongs to, or any similarity score. Paper order is randomised.

**Step 1 — Fill the six slots for each paper, from its own text.** For each slot write the component in ≤8 words, or `—` if absent.

| Slot | Question |
|---|---|
| State $x$ | What is a single configuration of the modelled system? |
| Representation $z=\phi(x)$ | In what coordinates is the state encoded for computation? |
| Objective $J$ | What scalar is defined over states and used? |
| Transition $T$ | What rule or operator changes the state? |
| Search / trajectory $\pi$ | What procedure moves through states using $J$ or $T$? |
| Feedback $F$ | What updates $J$, $T$ or the population in response to outcomes or environment? |

**Rejection rule (same as Table 1).** A slot counts as filled only if the paper specifies a computable object for it (an equation, update rule, algorithm or fitted function used to produce a reported result). Verbal interpretations, visualisation devices, and justifications for another slot do **not** count.

**Step 2 — Assign one label.**

| Label | Assign when |
|---|---|
| **L2-plausible** | State **and** Objective are filled on both sides, **and** at least 4 of 6 slots are filled on both sides, **and** each shared slot plays the same part (e.g. both $J$ are scalar fields over states whose extrema are the outcome of interest). |
| **L1-only** | The papers share topic words or domain but fail the L2 rule — e.g. only one or two slots are shared, or $J$ is present on one side only. |
| **mismatch** | The papers compute different kinds of thing (e.g. a static regression vs a dynamical model) with ≤1 shared slot. |
| **cannot tell** | The abstract does not describe the model well enough to fill State and Objective on both sides, even after opening the full text. |

Also record `slots_filled_both` (0–6). A short note is required for every **L2-plausible** and every **cannot tell**.

**Worked examples (from the paper; not in the sample).**
- *L2-plausible (partial):* Ding et al. 2019 vs Taherian Fard & Ragan 2017 — State and Objective shared; 2/6 filled on both sides under the strict rule. Under this codebook it is **L1-only** by count (2 < 4). This is deliberate: the codebook is stricter than the paper's own claim, and the paper reports that.
- *mismatch:* GET (sequence→expression regression) vs colorectal-metastasis trajectory inference.
- *L2-plausible:* MULTI-evolve (PLM-guided directed evolution) vs coevolution-guided LacI repressor engineering.

**Procedure.** Two raters label independently; target Cohen's κ ≥ 0.60 on the four-way label (computed before adjudication). Disagreements are resolved by a third rater who sees both notes; the third rater's label is final. If κ < 0.60, revise this codebook once using the disagreements, relabel a fresh random 30 pairs, and report both κ values.

**Outcomes to report.**
- **Precision** := (hidden-bridge-stratum pairs labelled L2-plausible) / (hidden-bridge pairs not labelled cannot-tell), with a Wilson 95% interval.
- The same rate in the false-friend and low-low strata. The detector is informative only if the hidden-bridge rate exceeds **both**; the low-low stratum is the base rate.
- **Recall is not measured** by this design and must not be claimed.

**Time budget.** 150 pairs × ~3 min ≈ 7.5 h per rater — one working day.
