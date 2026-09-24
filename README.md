# Evolution as a learnable program — literature analysis and Paper B

This repository holds a literature analysis of how machine learning is used to model evolution. The analysis runs from a corpus landscape to cross-literature correspondence detection and one full-text adjudicated case. **Paper B (`v2/manuscript_v2.md`) is the current manuscript.** Everything else is its provenance.

## Current status of the main claims

| Claim | Status | Where |
|---|---|---|
| A three-space detector (role signature × semantic embedding × citation overlap) finds cross-literature computational correspondences above chance | **Not supported.** Cross-literature role similarity 0.710 < within-literature 0.734 / 0.762. Nominated rate 6.47% vs vocabulary-shuffle null 10.2% and role-permutation null 7.7%. Pre-registered rule: 6.16% vs 5.97% (p = 0.32) | `v2/manuscript_v2.md` §3, `v2/data/nulls_summary.csv`, `v2/data/sensitivity_table.csv` |
| All earlier summary numbers are reproducible | **Yes** — 16/16 reproduce from the frozen spec; one definition corrected | `v2/data/reproducibility_log.csv`, `v2/data/detector.py` |
| Ding et al. 2019 (protein fitness, VAE + GP) and Taherian Fard & Ragan 2017 (Hopfield disease attractors) share a six-role computational template | **In part.** 2/6 roles on both sides (state, scalar objective), 3 complementary, feedback empty on both. The pair was hand-selected, not detector-nominated | `v2/table1_fair.md` |
| The two differ as mathematical objects | **Yes, on a synthetic capacity test.** Flexible fields (GP/RBF/MLP) recover 4 basins; a quadratic fitted to the same labels recovers 1. Discrete Hopfield dynamics recover the 2 wells they were shown. Synthetic only — no biological consequence claimed | `v2/fig_capacity_benchmark.png`, `v2/data/benchmark_results.csv` |
| Detector precision | **Unmeasured.** Blind 150-pair annotation kit released; not yet run | `v2/rater_kit/`, `v2/appendix3_codebook.md` |
| One learned field unifies fitness labels and state trajectories (Eq. 9) | **Not tested.** Pre-registered protocol, including the result that would refute it | `v2/appendix4_eq9_protocol.md` |

Earlier documents in `findings/` and the Variant A–C drafts at the top level were written **before** the null models. Their aggregate statements (e.g. "0.71 in computation", "6.5% hidden bridges", "same algorithm") are superseded; `v2/diff_vs_drafts.md` lists every correction.

## Layout

```
v2/                     Paper B v2 — manuscript, appendices 1–4, diff vs drafts, submission checklist, talk track
  data/                 frozen corpus, embeddings, reference lists, detector spec + code, all pair scores, nulls, sensitivity, benchmark
  rater_kit/            blind 150-pair sheet for the precision study (key withheld — see below)
bridge2_paper{A,B,C}_*.tex, html/, fig{A,B,C}_*.png   earlier drafts (superseded; kept for the record)
supporting/             Bridge 2 validation packet, Phase-0 wedge memo, ResearchOS architecture, review index
artifacts/              every project artifact (latest version of each; 106 files) + ARTIFACT_MANIFEST.csv with artifact/version ids and SHA-256
                        raw export: markdown here may contain {{artifact:…}} links; read the edited copies in v2/ and findings/ instead
notebook/
  session_notebook.ipynb  all 325 python/bash cells run in the analysis, in order, with truncated outputs (credentials redacted)
findings/
  reports/              stage reports + whitepaper (landscape → capability reframe → generative stack → harness operator → auto-research loop → deep connectivity → connectivity matrix)
  figures/              fig1–fig14
  tables/               stage tables (classified corpus, capability matrices, bridges, isomorphism catalog, scenario simulation, …)
  review/               self-contained HTML report and slide deck (earlier framing)
```

## Precision-study blinding

`rater_key_N150_DO_NOT_SHARE.csv` maps each pair in `v2/rater_kit/rater_sheet_N150_BLIND.csv` to its stratum. It is **deliberately not in this repository**. Its SHA-256, committed here before any labelling, is:

```
17fcb1027919dab73ea55cfa2eba7662c87bdad5351cfb765f10f65a714ce07b
```

After labelling, publish the key; anyone can check it against this hash.

## What is deliberately not in this repository

- **Credentials.** The OpenAlex API key is read from the `OPENALEX_API_KEY` environment variable and never written to disk. Every file was scanned for the key value before commit. The notebook and artifacts also have contact emails passed as `mailto=` replaced with `<REDACTED_EMAIL>`, and home-directory paths replaced with `~`. The email addresses that remain are authors' corresponding addresses inside public paper abstracts and full texts.
- **The precision-study key** (`rater_key_N150_DO_NOT_SHARE.csv`) — see the hash above.
- **Personal onboarding notes** and **machine-local copy scripts** (`copy_papers*.sh`, which only contain absolute paths on one machine).
- **Notebook re-runnability.** Cells ran in stateful kernels across several environments; the reproducible entry points are `v2/data/detector.py` and the frozen data files.

## Reproducing Paper B numbers

```python
import json, numpy as np, pandas as pd, sys
sys.path.insert(0, "v2/data"); import detector as D
comb = pd.read_csv("v2/data/combined_text.csv")
emb  = np.load("v2/data/concept_embeddings.npy")
refs = json.load(open("v2/data/refset_v2.json"))
R = D.run_detector(comb, emb, refs)          # prim, concept, cit on the rich subset
```

Every number in the manuscript is templated from `v2/data/manuscript_numbers.json`. The corpus retrieval date is recorded as UNVERIFIED (before 2026-07-04). OpenAlex relevance search drifts, so the frozen `combined_text.csv` is the unit of reproducibility, not the queries.

## Caveats that apply throughout

- Paradigm and role labels come from keyword rules: noisy per paper, used only in aggregate.
- Judgment-scored matrices in `findings/` (mechanism/transfer/confidence ratings, scenario projections) are author priors, not measurements.
- Trend claims in the landscape stage use 2015–2024 only.

**Author:** Hari Lakshmanan — Independent researcher (no institutional affiliation). Contact: hariase@gmail.com. No external funding; no competing interests.

Licence: **not yet chosen** — until one is added, default copyright applies and others may not reuse the material.
