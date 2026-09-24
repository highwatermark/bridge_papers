# Review index — what exists, where it is, and what is publishable

Workspace files are swept between sessions; these are the durable artifact-store paths.
Everything below is on your machine right now and opens directly.

---

## TIER 1 — Manuscripts (drafts, not yet submittable)

**None of the three is submission-ready.** All are internally complete and
internally consistent, but all three share the same four gaps (see "Blocking
gaps" below). Ranked by how close each is.

### Variant A — narrow translation paper  ·  CLOSEST TO READY
1916 words · 3 figures · 8 equations · 12 references
- LaTeX: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/a7e65715-207f-4356-b3b3-05b1c94b6f86/v62e828d6_bridge2_paperA_translation.tex`
- Read:  `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/aff38da0-4bae-4bd5-b9ca-fadd31424b21/ved33aee8_paperA_translation.html`

### Variant B — translation + detection method
2334 words · 3 figures · 8 equations · 12 references
- LaTeX: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/5687a069-2746-4c5a-86b1-5c1c7c7ce716/v695a05ce_bridge2_paperB_method.tex`
- Read:  `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/c4ae6359-5937-4018-b91b-f27a2420e804/v94eda5fe_paperB_method.html`

### Variant C — position paper
2230 words · 3 figures · 8 equations · 10 references
- LaTeX: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/2067bf54-f30a-4ac1-ab92-62c183403236/vaabd61e4_bridge2_paperC_position.tex`
- Read:  `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/8bf37156-5aff-4676-976c-c483bfb19730/v09e66542_paperC_position.html`

### Decide between them
- `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/bf6ca8d1-ae83-4fa2-9c80-adf69cdb6400/ve60cd844_variant_comparison.md`

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

- Validation packet: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/76e867cd-e73b-498a-9d1e-a56a5c8414fc/vf2fc9d1b_bridge2_validation_packet.md`
- Extracted model definitions: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/f8ae9dad-c0b5-435b-8c97-2141222eaea9/v61bfa06f_bridge2_model_facts.json`
- Synthetic benchmark data: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/6054eeac-2f04-4c6d-afd9-e414fdfdbcd0/ve199d848_bridge2_synthetic.npz`
- Negative controls: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/9fda636f-91ad-4cd0-aa38-c0f41e484e82/v3e268321_false_friend_controls.csv`
- Shared manuscript core: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/79b4cb15-5fc3-43df-9260-218e343d305c/v4844e9fd_bridge2_core.json`
- Bibliography: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/d023f6cd-222d-46d6-9de7-7ce6b459d7ca/v25a78a71_bridge2_references.bib`
- Bibliography verification: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/a57a12ef-a0c2-40fa-9980-c2000331250f/v4a15bd25_bridge2_bibliography_check.csv`

### Figures (300 dpi, publication-grade)
- Fig 1 shared template: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/db13018b-265d-4d39-976c-d08e1381d3c8/v91b6a913_figA_shared_template.png`
- Fig 2 synthetic benchmark: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/20ca702b-27ae-4575-a42a-c171e49cb7f5/vea3f4871_figB_synthetic_validation.png`
- Fig 3 negative controls: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/5d6b2111-eb59-4e09-bd86-257df6b883f8/ve236dd90_figC_false_friends.png`

---

## TIER 3 — Program documents (internal / founder-facing, not journal papers)

- Phase-0 wedge memo (3 bridges): `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/138a03f1-7207-44bc-9de2-e542c961a079/v181eccda_phase0_validation_wedge.md`
- The three validated bridge pairs: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/02b1a533-6bb2-4dbb-a75f-18f7bb98e263/v1d367e98_phase0_validated_bridges.csv`
- Six-role translations: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/ac5c56e6-a89c-4c6d-b842-ee6f62d6eded/v2f71d7da_phase0_bridge_translations.csv`
- ResearchOS agent architecture: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/742c8a44-e7e4-44d8-986a-a1cfa98b6901/vc4bbec63_researchos_architecture.md`
- Whitepaper (six-stage arc): `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/d2c4fdd7-f779-4276-9353-7a021f596f95/v72454df3_whitepaper_evolution_as_learnable_program.md`
- Deep-connectivity report: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/833f94e0-1d19-4d81-8851-ea618c4f9838/vf6686641_deep_connectivity_report.md`
- Connectivity matrix report: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/bdca0100-97b7-44a6-915c-61e2354c8746/ve550142a_connectivity_matrix_report.md`
- Skill smoke test: `~/.claude-science/orgs/40954c99-1d5e-452b-aa06-7e9d78458119/artifacts/proj_743a755ad2f5/85a3d9d5-93ee-4686-bd0e-89dcdf9e99aa/v9a5f971d_bridge_skills_smoketest.json`

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
