# The field map's 15-paper table, re-rated under the Table 1 rule

**Rule (fixed before rating).** A slot is *filled* (●) only if the paper specifies a computable object for that role that is used to produce a reported result. It is *empty* (○) if the only candidate is a verbal interpretation, a visualisation device, or a justification for a choice made in another slot. ◐ marks a slot the paper describes but does not use (re-description). A **u** column (exogenous input or condition) is added and kept separate from **F** (in-model feedback), because the map's F column mixed the two.

Ratings come from full texts only. Seven papers are not yet rated: five need PDFs you are providing, and two are books or proceedings.

| # | Paper | Cluster | x | φ | J | T | π | u | F |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Wright 1932 | 1 fitness | n/r | n/r | n/r | n/r | n/r | n/r | n/r |
| 2 | Ding, Zou & Brooks 2019 | 1 fitness | ● | ● | ● | ◐ re-descr. | ◐ re-descr. | ○ | ◐ re-descr. |
| 3 | Riesselman, Ingraham & Marks 2018 (DeepSequence) | 1 fitness | ● | ● | ● | ◐ re-descr. | ○ | ○ | ○ |
| 4 | Frazer et al. 2021 (EVE; read from bioRxiv version) | 1 fitness | ● | ● | ● | ○ | ○ | ○ | ○ |
| 5 | Mustonen & Lässig 2009 | 1 fitness | pending | pending | pending | pending | pending | pending | pending |
| 6 | Waddington 1957 | 2 fate | n/r | n/r | n/r | n/r | n/r | n/r | n/r |
| 7 | Huang et al. 2005 | 2 fate | pending | pending | pending | pending | pending | pending | pending |
| 8 | Wang et al. 2011 | 2 fate | pending | pending | pending | pending | pending | pending | pending |
| 9 | Taherian Fard & Ragan 2017 | 2 fate | ● | ○ | ● | ● | ● | ○ | ◐ re-descr. |
| 10 | Taherian Fard, Srihari, Mar & Ragan 2016 (map listed as 'Maetschke & Ragan') | 2 fate | ● | ○ | ● | ◐ re-descr. | ◐ re-descr. | ○ | ○ |
| 11 | Qiu et al. 2022 (dynamo) | 2 fate | ● | ● | ● | ● | ● | ● | ○ |
| 12 | Cislo et al. 2025 | 2 fate | ● | ○ | ● | ● | ● | ● | ○ |
| 13 | Hopfield 1982 | 4 ML | pending | pending | pending | pending | pending | pending | pending |
| 14 | Onuchic, Luthey-Schulten & Wolynes 1997 | 3 folding | pending | pending | pending | pending | pending | pending | pending |
| 15 | Li, Xu, Taylor, Studer & Goldstein 2018 | 4 ML | ● | ○ | ● | ● | ● | ○ | ○ |

**Column totals over the 8 rated papers.** x 8/8 · J 8/8 · φ 4/8 · T 4/8 · π 4/8 · **u 2/8** (both on the fate side) · **F 0/8**.

**Differences from the map.** 12 of the 48 comparable cells differ. In 11 the map is more generous; dynamo's J is the one place it is stricter. The largest corrections:
- Taherian Fard 2016's T and π are description only: E is computed on observed patterns, and the network is never run to convergence.
- Cislo's φ and F are empty: the diffusion map is for display, and morphogen is an input, not feedback.
- The F column is empty across all eight rated papers.

**What this means for the map's claims.** Only two slots are universal among the rated papers: a state and a scalar field. The map's own caveat, that it is not evidence that everyone runs the same algorithm, is confirmed. The shared template is state + scalar field. The dynamics, the representation and especially feedback are where these literatures actually differ.

Per-cell evidence: `fieldmap_rerated_15.csv`.
