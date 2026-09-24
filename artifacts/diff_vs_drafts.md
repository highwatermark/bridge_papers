# A. Diff against the drafts (Variants A–C → Paper B v2)

Every change is either a correction of a false or unsupported statement (**C**), a new result (**N**), or a scope change (**S**). Numbers are from `manuscript_numbers.json`.

| # | Type | Draft said | v2 says | Evidence |
|---|---|---|---|---|
| 1 | C | Title (A): "Fitness landscapes and epigenetic landscapes are the same algorithm"; B: "the two literatures have independently built the same algorithm." | The two models "share a six-role computational template in part and diverge as mathematical objects." Phrase "same algorithm" removed everywhere (grep = 0). | Table 1 |
| 2 | C | B: "The pair analysed above was not chosen by hand. It was surfaced by a procedure that measures, for every cross-literature pair of papers in a corpus, three quantities that are usually conflated." | The pair was hand-selected from a landmark anchor via concept-nearest neighbours; the flagging rule did **not** nominate it (primitive 0.841, P81; concept 0.432, P94.7 — the rule's *false-friend* region). | `ding_fard_position.json` |
| 3 | C | "6.5% of pairs are hidden bridges … no shared citations." | The 627 pairs (6.54%) had **no** citation condition. With it: 620 (6.47%). No claim that any fraction are true correspondences. | `reproducibility_log.csv` |
| 4 | N | Cross-literature primitive mean 0.71 presented as evidence of shared structure. | Within-literature means are higher (0.734, 0.762) than cross (0.710); the 0.71 comes from the ≥4-role gate. | `null_within_vs_cross.csv` |
| 5 | N | (no nulls) | Flagged rate 6.47% vs vocabulary-shuffle 10.2% and role-permutation 7.7%; pre-registered rule 6.16% vs 5.97% (p = 0.32); 1/48 sensitivity cells p<0.05. | `nulls_summary.csv`, `sensitivity_table.csv` |
| 6 | C | Table 1: all six roles filled on both sides ("instantiate the same six-role computational template"). | Under a stated rejection rule: 2/6 on both sides (state, objective), 3 complementary, feedback empty on both. Weak slots named. | `table1_fair.md` |
| 7 | C | Three false-friend controls with primitive 0.24 / 0.00 / 0.23; "all three have higher surface similarity … all three are rejected." | Those values came from a rebuilt lexicon that differs from the original; under the frozen spec they are 0.68 / 0.46 / 0.60 and no pair is rich. Withdrawn. Replaced by four frozen-spec candidates: 3 rejected on reading, **1 detector error** (plausible match). Selection not blind; disclosed. | `false_friends_evidence.csv` |
| 8 | C/N | "A quadratic form … cannot represent two separated minima"; benchmark GP 1.00 vs Hopfield 0.34. | Kept, with fair baselines: RBF 0.998, MLP 1.000 (4 basins); **quadratic regression on the same labels 0.601 (1 minimum)** → limitation is the quadratic family. Discrete Hopfield on {−1,+1}² recovers the 2 sampled wells: the continuous "0 basins" is a property of the relaxation used for display. | `benchmark_results.csv` |
| 9 | C | Sign-convention spurious correlation reported as −0.34 (A/B core). | Stated for the GP field (-1.000 unaligned); Hopfield continuous field is ρ = 0.338 regardless. | `benchmark_results.csv` |
| 10 | S | 96 "seed bridges" presented as a Phase-0 shortlist. | Reported only as a reproduced count (96); not used as evidence. | §3.1 |
| 11 | N | (no precision) | Blind N=150 stratified sheet + codebook; precision explicitly unmeasured. | Appendix 3 |
| 12 | N | Eq. 9 as "the decisive experiment", no protocol. | Pre-registered protocol with data candidates (papers verified, data access TO-LOOK-UP), held-out design, kill criterion. | Appendix 4 |
| 13 | N | 12 references. | 30, all OpenAlex-verified (first author + year); related-work section added. | `bibliography_check_v2.csv` |
| 14 | C | Corpus methods: counts only. | Query strings, date range, gates, dedup rule, language (all en, post hoc), type drift (21 records), retrieval date UNVERIFIED. | `detector_spec.json` |
| 15 | S | A, B, C as three candidate papers. | B is the paper; A's core becomes §4–5; C becomes the companion talk track. | this document |
