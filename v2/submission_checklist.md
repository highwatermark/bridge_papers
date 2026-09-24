# G. Submission checklist — what remains, and who does it

| Item | Status | Owner | Effort |
|---|---|---|---|
| Author line, affiliations, corresponding author | **Done** | **You** | minutes |
| Funding, competing interests, CRediT contributions | **Done** (sole author, no funding, no competing interests) | **You** | minutes |
| Deposit data/code (Zenodo or OSF) and insert DOI | Files ready (`v2/data/`) | **You** (account needed) | 1 h |
| **Precision study**: two raters label `rater_sheet_N150_BLIND.csv`; κ; third-rater adjudication; unblind with key | Kit ready, **not run** | Two domain raters + one adjudicator | ~1 day per rater |
| Independent re-rating of Table 1 by a second reader | Not done | One reader with both PDFs | 1–2 h |
| Adjudicate the four skipped false-friend candidates (ranks 3, 4, 6, 7) | Not done | Reader | 1 h |
| Retrieval date of the corpus | UNVERIFIED | **You** (if recorded elsewhere) or state as unknown | — |
| Eq. 9 real-data experiment | Protocol only; data access TO-LOOK-UP | Compute + a collaborator with lac/GAL data | weeks |
| Compile PDF (`pandoc manuscript_v2.md -o manuscript_v2.pdf` or port to LaTeX) | Not compiled here (no TeX in sandbox) | **You** | minutes |
| Choose venue | See below | **You** | — |

**Venue fit, given the honest result.** (1) A methods/negative-results venue in scientometrics or computational science (e.g. *Quantitative Science Studies*, *PLOS ONE*) will take the detector-vs-null result as the main contribution. (2) A computational-biology venue (*PLOS Computational Biology*, *Bioinformatics* methods note) will want the precision study done and will value §4–5 more than §3. (3) A workshop paper (ML-for-science) fits the current state best if the precision study cannot be done soon. Recommendation: run the precision study first. If the flagged stratum beats both comparison strata, submit to (2); if not, submit to (1) as a negative result with the adjudicated case.

**Style rules enforced before save (grep):** 'same algorithm' → 0 occurrences; every number traced to `manuscript_numbers.json` or labelled UNVERIFIED / TO-LOOK-UP / TO FILL.
