# Review index — what exists, where it is, and what is publishable

Paths below are relative to this file (repository copy).

---

## TIER 1 — Manuscripts (drafts, not yet submittable)

**None of the three is submission-ready.** All are internally complete and
internally consistent, but all three share the same four gaps (see "Blocking
gaps" below). Ranked by how close each is.

### Variant A — narrow translation paper  ·  CLOSEST TO READY
1916 words · 3 figures · 8 equations · 12 references
- LaTeX: `../bridge2_paperA_translation.tex`
- Read:  `../html/paperA_translation.html`

### Variant B — translation + detection method
2334 words · 3 figures · 8 equations · 12 references
- LaTeX: `../bridge2_paperB_method.tex`
- Read:  `../html/paperB_method.html`

### Variant C — position paper
2230 words · 3 figures · 8 equations · 10 references
- LaTeX: `../bridge2_paperC_position.tex`
- Read:  `../html/paperC_position.html`

### Decide between them
- `../supporting/variant_comparison.md`

---

## Blocking gaps (apply to all three)

| Gap | Status | Who fixes it |
|---|---|---|
| **Author, affiliation, corresponding author** | `\author{}` is empty in all three | You — one line each |
| **Funding / competing interests** | Absent | You |
| **Data & code availability with a real link** | Section present in A and B, but no repository URL | You — deposit the CSV/NPZ and paste the DOI |
| **Real-data validation** | **Absent — the benchmark is synthetic** | This is scientific work, not editing |

The first three are an afternoon. The fourth is the real question: the paper
currently proves a *representational-capacity* difference on a constructed
double well, not its biological consequence. A methods or theory venue may
accept that for a translation note; a biology journal will ask for the
longitudinal fitness + expression-trajectory experiment the paper itself
proposes (Eq. 9).

**PDFs do not compile here** (no working TeX in the sandbox). The sources are
structurally validated — balanced environments, all citations resolving, no
undefined references. On your machine:
```
pdflatex <file>.tex && bibtex <file> && pdflatex <file>.tex && pdflatex <file>.tex
```
The three PNGs and the .bib must sit in the same directory.

---

## TIER 2 — Supporting evidence (publishable as supplement)

- Validation packet: `../findings/reports/bridge2_validation_packet.md`
- Extracted model definitions: `../supporting/bridge2_model_facts.json`
- Synthetic benchmark data: `../supporting/bridge2_synthetic.npz`
- Negative controls: `../supporting/false_friend_controls.csv`
- Shared manuscript core: `../supporting/bridge2_core.json`
- Bibliography: `../bridge2_references.bib`
- Bibliography verification: `../supporting/bridge2_bibliography_check.csv`

### Figures (300 dpi, publication-grade)
- Fig 1 shared template: `../figA_shared_template.png`
- Fig 2 synthetic benchmark: `../figB_synthetic_validation.png`
- Fig 3 negative controls: `../figC_false_friends.png`

---

## TIER 3 — Program documents (internal / founder-facing, not journal papers)

- Phase-0 wedge memo (3 bridges): `../findings/reports/phase0_validation_wedge.md`
- The three validated bridge pairs: `../findings/tables/phase0_validated_bridges.csv`
- Six-role translations: `../findings/tables/phase0_bridge_translations.csv`
- ResearchOS agent architecture: `../findings/reports/researchos_architecture.md`
- Whitepaper (six-stage arc): `../findings/reports/whitepaper_evolution_as_learnable_program.md`
- Deep-connectivity report: `../findings/reports/deep_connectivity_report.md`
- Connectivity matrix report: `../findings/reports/connectivity_matrix_report.md`
- Skill smoke test: `../supporting/bridge_skills_smoketest.json`

---

## What is genuinely finished

- **The four skills are published and working** — `bridge-extract`, `bridge-align`,
  `bridge-synthesize`, `bridge-controls`, all four loaded and exercised.
- **The bibliography is verified** — 12 references, each resolved against OpenAlex
  with a DOI. Wright 1932 was omitted because it would not resolve.
- **The zero-citation claim is measured**, not assumed: 0 shared references
  between the Bridge 2 pair (77 and 39 references respectively).
- **The Level-3 result reproduces** from the published skill: GP ρ=1.00 / 4 basins
  vs Hopfield ρ=0.34 / 0 basins.
