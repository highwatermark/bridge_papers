# Review of `landscape_field_map.html` against the Paper B evidence

The map widens the opportunity space from two literatures to four substrate clusters: sequence→fitness, expression→fate, conformation→energy, and parameters→loss. It also lists six candidate transfers between them. This review checks its references, reconciles its role ratings with the audited Table 1, tests one of its two headline claims against citation data, and sorts the six transfers by how much is already known.

## 1. References (15) — checked against OpenAlex

| Status | Papers |
|---|---|
| Verified as cited (DOI, first author, year match) | Ding 2019, Riesselman 2018, Frazer 2021, Mustonen & Lässig 2009, Huang 2005, Wang 2011, Taherian Fard & Ragan 2017, Qiu 2022 (dynamo), **Cislo 2025** (PNAS, "Reconstructing Waddington's landscape from data", 10.1073/pnas.2521762122), Hopfield 1982, Onuchic 1997 |
| **Correction** | #10 is **Taherian Fard, Srihari, Mar & Ragan 2016**, "Not just a colourful metaphor: modelling the landscape of cellular development using Hopfield networks", *npj Syst Biol Appl*. It is not Maetschke & Ragan; the DOI in the map resolves to this author list. |
| Minor | Li et al. is arXiv 2017 / NeurIPS 2018 — cite the NeurIPS version. Waddington 1957: only the 2014 Routledge reissue is indexed, so the original needs a hand-checked citation (Allen & Unwin, 1957 — UNVERIFIED here). |
| Unresolvable | Wright 1932 (congress proceedings, not indexed). Cite it as a classic and mark it unverified, as Paper B already does. |

## 2. Role ratings that conflict with the audited Table 1

The map rates slots by what each paper *discusses*. Table 1 uses a fixed rejection rule: a slot counts as filled only if the paper specifies a computable object that produces a reported result. That rule gives stricter ratings:

- **Fard, φ**: the map gives ◐, but its own note says "PCA for viz only". Under the rule this is **empty**.
- **Fard, F**: the map gives ● for "stage-wise rewiring of W". Table 1 rates it a **re-description**: a separate W is fitted per stage, and the model never updates W itself.
- **Ding, T/π/F**: ◐ in the map, re-description in Table 1. These agree in direction.
- **Cislo 2025**: rated ● in all six slots. This rating is unadjudicated. If it survives a full-text read, Cislo becomes the strongest available specimen, and the closest existing object to Eq. 9 on the fate side.

Recommendation: rate all 15 papers under the Table 1 rule before the table goes into a manuscript. The map's own closing line already warns against reading it as "everyone runs the same algorithm".

## 3. The two headline claims

**"Citation graphs are not [common]" — supported on this set.** Using OpenAlex reference lists for 14 of the papers (Waddington has none indexed):
- **9 of the 12** direct citations stay within a cluster.
- **All 3** cross-cluster citations go to one shared ancestor, Hopfield 1982, from Fard 2017, Taherian Fard 2016 and Onuchic 1997.
- Pairs sharing at least one reference: **11/28 within clusters vs 3/63 across**. All three cross pairs share one reference with Onuchic 1997.

Two caveats. The set is hand-picked (n = 14). And a partition like this is expected between any two fields, so it does not by itself show a missed connection.

**"The six-role template is common" — not established by this evidence.** It rests on hand ratings of 15 curated papers. On the 522-paper corpus the keyword detector found cross-literature role similarity (0.710) *below* within-literature similarity (0.734 / 0.762), and a nominated-pair rate at chance. The map's footer says the 0.71 / 0.26 / 6.5% numbers "still need nulls". That is now out of date: the nulls have been run, and those numbers do not survive them.

## 4. The six transfers, sorted

| Transfer | Status | Next action |
|---|---|---|
| **2 ↔ 4** Fard's quadratic energy → modern Hopfield | **Tested now** (below) | Fold into Paper B's Level-3 section |
| **1 ↔ 2 via u** Mustonen seascape ↔ morphogen-parameterised landscape (Cislo) | Open; strongest candidate | Full-text adjudication of Cislo 2025 with the bridge-extract and bridge-align skills. This is the concrete version of the harness input *u* in C = f(state, environment, history, time). |
| **1 → 2** learned J (EVE/Ding) + explicit T (dynamo) | Open | This is Eq. 9. It needs one system with both variant-effect labels and trajectories (see Appendix 4 candidates). |
| **1 ↔ 3** fitness as a readout of folding energy | Probably not missing | Search the biophysical fitness-model literature before calling it a gap |
| **1 ↔ 4** adaptive walk ↔ SGD | Unchecked | Citation search first |
| **3 ↔ 4** folding funnel ↔ loss basin | **Already made** | Cite Ballard et al. 2017, *PCCP*, "Energy landscapes for machine learning" (10.1039/c7cp01108c), and Choromanska et al. 2014, "The loss surfaces of multilayer networks". Not a gap. |

### 2 ↔ 4, run on the capacity benchmark

The test uses the same four-well ground truth. Samples of "observed cells" are drawn around the wells, and each energy is built from those samples alone. No fitness labels are used.

| Samples drawn from | Quadratic Hopfield −½xᵀWx | Modern Hopfield, log-sum-exp (β = 2) |
|---|---|---|
| 2 wells (the setting used before) | 0 interior minima, ρ = 0.34 | 2 minima (the two sampled wells), ρ = 0.51 |
| all 4 wells | **0** minima, ρ = -0.338 | **4** minima, ρ = 0.717 |

The modern energy places a basin at every sampled stable state, which the quadratic energy cannot do. So swapping in the modern energy fixes the basin-count failure behind the Level-3 verdict. It does **not** recover the full potential shape (ρ ≈ 0.7, against 1.00 for label-fitted GP/MLP fields), and the result depends on β: β = 1 merges everything into 1 minimum, while β = 4–8 keeps 4 minima but ρ falls. The fair reading is that modern Hopfield changes the *object* on the fate side, closing part of the Level-3 gap. It remains a density model of observed states, not a fitted landscape. This is still a synthetic capacity test with no biological consequence.

## 5. What this changes for Paper B

- Add the four-cluster frame as a **related-work and scope** paragraph, labelled a curated reading. It is not evidence that the template is common.
- Add the modern-Hopfield result to §5 (the capacity test) as the natural repair of the Fard-side object, and cite Ramsauer 2021 and Krotov & Hopfield 2016 (both already in `references_v2.bib`).
- Add Ballard 2017 and Choromanska 2014 so no one mistakes 3 ↔ 4 for a new gap.
- List Mustonen × Cislo and EVE × dynamo as **nominated, not adjudicated**. Mustonen × Cislo is the next full-text case.

*Data: `fieldmap_reference_check.csv`, `fieldmap_citation_check.json`, `modern_hopfield_benchmark.csv`.*
