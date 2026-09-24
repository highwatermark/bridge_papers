# Companion talk track (formerly Variant C) — ~10 minutes, 8 slides

*Speaker notes. The talk carries the program vision; every empirical claim in it is one that Paper B supports. Where the vision goes beyond the evidence, the notes say so out loud.*

**1. The question (1 min).** Evolution-ML groups and systems-biology groups both build models that put a number on configurations of a living system and read outcomes off its peaks and valleys. They almost never cite each other. Is anyone losing a result because of that? Swanson showed in 1986 that two literatures can jointly imply something neither states.

**2. Two claims to keep apart (1 min).** Can a machine *find* such pairs better than chance? And is a *given* pair really computing the same thing? The first is statistics; the second is reading. Our earlier drafts ran them together, and this talk separates them. *Line to land: the detector nominates, reading adjudicates.*

**3. The detector (1 min).** Three views of every cross-field pair: a six-role signature from a fixed lexicon, a sentence-embedding similarity, and citation overlap. Flag pairs that look alike in role, unalike in words, and share no references. 522 papers, 9,585 pairs in the rich subset.

**4. The honest result (2 min) — Fig. 1.** Cross-field pairs are *less* alike than within-field pairs (0.71 vs 0.73/0.76). The flagged rate, 6.5%, sits at or below two null models. Under a rule fixed in advance it equals chance: 6.2% vs 6.0%. *Say it plainly: with this lexicon, the detector is not evidence that the fields share structure. It is a candidate generator with unknown precision.* This slide earns the audience's trust for the next three.

**5. One pair, read in full (2 min) — Table 1.** A protein-fitness model (VAE latent + Gaussian process) and a disease-attractor model (Hopfield energy). Under a strict rule they share two of six roles: a state space and a scalar field over it. They fill three others complementarily: one has the learned representation, the other has the dynamics. Neither implements feedback. *They share a template in part and diverge as mathematical objects.* Note that the detector did not pick this pair; we did.

**6. Where they diverge (1 min) — Fig. 2.** On a four-well toy potential, any flexible function recovers four basins, and a quadratic fitted to the same labels recovers one. The Hopfield energy is quadratic. To be fair to it, its binary dynamics recover exactly the two wells it was shown. The difference is function class, not "landscape vs no landscape". *Synthetic: capacity, not biology.*

**7. What would make this real (1 min).** (a) Precision: 150 blind pairs, two raters, three strata. If flagged pairs are not more often plausible matches than random ones, the detector idea is dead at this resolution. (b) Unification: fit one learned field to fitness data *and* state trajectories in one system (the *lac* operon is the candidate). The protocol states in advance the result that would kill the idea.

**8. The program, labelled as vision (1 min).** *Say explicitly: this slide is a direction, not a finding.* If reading-adjudicated correspondences accumulate, they form a translation layer between fields. That layer becomes testable models: environment as an input that moves a state, capability as the outcome of those moves. The route there runs through slide 7, not around it.

**Q&A preparation.**
- *"Isn't 6.5% interesting on its own?"* No. Chance gives 6–10% (slide 4).
- *"Why not use an LLM to score roles?"* That is the obvious next detector, and it has to face the same nulls and the same precision study.
- *"Is one pair a result?"* It is a worked example of the adjudication method. Its generality is exactly what the precision study measures.
