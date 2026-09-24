# Appendix 2 — Pseudocode (frozen specification; implementation `detector.py`)

```
INPUT  corpus C (id, pillar ∈ {evo, har}, text = title + ". " + abstract, len > 80)
       embeddings E ∈ R^{|C|×384}  (all-MiniLM-L6-v2, normalised)
       refs: id → set of OpenAlex referenced_works
       lexicon L[role][pillar] → terms           # Appendix 1

1  for each paper i:  sig[i, r] = |{ t ∈ ∪_p L[r][p] : t ⊂ lower(text_i) }|        # r = 1..6
2  rich[i] = (#{r : sig[i, r] ≥ 1}) ≥ 4
3  Ev = {i : rich, pillar = evo};  Hv = {j : rich, pillar = har}
4  for (i, j) ∈ Ev × Hv:
       prim[i,j]    = cos( sqrt(sig[i]), sqrt(sig[j]) )
       concept[i,j] = E[i] · E[j]
       jac[i,j]     = |refs_i ∩ refs_j| / |refs_i ∪ refs_j|   (0 if either empty)
5  ORIGINAL   flag = prim ≥ 0.90  ∧  concept < Q90(concept)            [∧ jac = 0 as described]
   PRE-REG    flag = prim ≥ Q75(prim) ∧ concept ≤ Q25(concept) ∧ jac = 0
6  NULLS
   (a) within: same prim on Ev×Ev and Hv×Hv (upper triangle)
   (b) vocab shuffle ×200: permute term→role map (sizes fixed); redo 1–5 incl. richness gate
   (c) role permutation ×200: for j ∈ Hv permute sig[j, ·]; redo 4–5 (rich set fixed)
   report observed rate, null mean, 95% interval, one-sided empirical p with +1 smoothing
7  SENSITIVITY  τ_prim ∈ {0.80,0.85,0.90,0.95,Q75,Q90} × τ_concept ∈ {≤Q10,≤Q25,≤Q50,<Q90} × τ_jac ∈ {any, =0};
               per-cell role-permutation null ×100
OUTPUT pair_scores.csv.gz, nulls_summary.csv, sensitivity_table.csv
```

Nominated pairs are **candidates for reading**; adjudication uses Table 1's rejection rule and the Appendix 3 codebook.
