# Evolution's search process generates reusable biological programs

*A capability dossier reframing the field's ML-on-evolution literature around a single thesis: the outputs of evolutionary search are **reusable programs**, and the current wave of AI is, in effect, learning to read and rerun them.*

Built from the 404 on-target, off-topic-filtered papers classified in pass 1 (OpenAlex, 2015–2024 trend window). Corpus metrics per capability are in `capability_metrics.csv`; the rating matrix is in `capability_ladder_matrix.csv`.

---

## The two lenses

**The input equation (what the search operates on):**

> Genome + Environment + Time + Repeated stimulus + Feedback → **Capability**

Evolution is a search process whose substrate is the genome, whose scoring function is the environment, and whose optimizer is mutation-plus-selection iterated over time. The "program" is the reusable solution the search converges on; a capability is that program expressed. This is `fig4_causal_stack.png`.

**The causal descent (how to explain any capability):**

CAPABILITY → MECHANISMS → REGULATORY PROGRAMS → ENVIRONMENTAL HARNESS → EVOLUTIONARY PRESSURE → SEARCH DYNAMICS

Read **down** to explain a capability (what implements it, what controls it, what scored it, what pressure shaped it, how the space was searched). Read **up** to generate one (choose the pressure and harness, run the search, get the program). ML has climbed this ladder unevenly — it reads the top two layers well and the bottom two barely at all, which is the central gap this dossier surfaces.

**The epistemic ladder (how sure we are), rated 1–5 per capability** — `fig3_capability_ladder.png`:
Mechanism understood · Transferability · Overall confidence (judgment), beside Evidence density · Recent momentum · Citation impact (corpus-derived).

---

## Capability dossiers

Each capability is traced through six fields in the order you specified — **Capability → Known mechanisms → Open questions → Unknowns → Transferability → Confidence** — with the corpus signal and the causal-stack reading noted.

### 1. Protein fold & function  *(PLM + structure prediction; n=62, 5.4× growth, conf 5/5)*
- **Capability**: recover 3D structure and functional constraint from sequence alone.
- **Known mechanisms**: coevolution across homologs encodes spatial contacts; self-supervised language modeling over UniRef/BFD internalizes the constraints selection preserved. Anchors: ESM-1b, ESMFold, AlphaFold-family, ESM3.
- **Open questions**: conformational ensembles and allostery, not just ground-state folds; disordered regions; how much "function" beyond structure the embeddings actually carry.
- **Unknowns**: whether the model has learned the *folding process* or only the fold distribution — a mechanism-vs-outcome question the field cannot yet answer.
- **Transferability**: very high — embeddings transfer zero-shot to variant effect, binding, design across unseen families. This is the reusable-program story at its strongest.
- **Confidence**: **5/5**. The clearest case that an evolutionary search product is a learnable, reusable program.
- **Stack reading**: ML reads MECHANISMS cleanly; it does not touch the ENVIRONMENTAL HARNESS or PRESSURE that produced the fold.

### 2. Regulatory control of expression  *(genomic FMs; n=29, 1.4× growth, conf 3/5)*
- **Capability**: predict expression / regulatory activity from raw genomic sequence.
- **Known mechanisms**: long-range sequence-to-activity models learn cis-regulatory grammar (Enformer); genome-scale LMs extend to design (Evo). Highest citation impact per paper in the corpus (median 21/yr).
- **Open questions**: trans effects, cell-type specificity, 3D genome context; causal vs correlational motif use.
- **Unknowns**: whether the learned "grammar" corresponds to the regulatory logic evolution actually selected, or a predictive shortcut.
- **Transferability**: low-to-moderate — models are often organism- and assay-specific and transfer poorly across cell types.
- **Confidence**: **3/5**. High-impact anchors but flat growth and weak transfer; the program is real but only partially readable.
- **Stack reading**: this is the REGULATORY PROGRAMS layer itself — the one the thesis most directly names, and the one ML reads least reliably.

### 3. Fitness-landscape navigation  *(fitness learning; n=64, 8.7× growth, conf 3/5)*
- **Capability**: predict variant fitness / effect and navigate epistasis.
- **Known mechanisms**: supervised and semi-supervised regression on deep mutational scans; increasingly built on protein-LM priors.
- **Open questions**: higher-order epistasis, generalization off the training landscape, extrapolation beyond a few mutations.
- **Unknowns**: the global geometry of real landscapes (ruggedness, connectivity) — sampled locally, never seen whole.
- **Transferability**: low — a landscape learned for one protein rarely transfers; the fastest-growing capability (8.7×) but the lowest per-paper impact (7/yr), a fragmented, benchmark-poor area.
- **Confidence**: **3/5**. High activity, low consolidation.
- **Stack reading**: directly probes EVOLUTIONARY PRESSURE (fitness = the objective) but only as sampled point-measurements, not as a learned scoring function.

### 4. Generative evolvability  *(generative design; n=33, 15.0× growth, conf 4/5)*
- **Capability**: generate novel, functional sequences/structures evolution never sampled.
- **Known mechanisms**: diffusion, autoregressive, and inverse-folding models learn the manifold of viable variants, then sample beyond it. Anchor: ProteinMPNN and applications.
- **Open questions**: functional (not just structural) validity; controllable design to spec; wet-lab hit rates.
- **Unknowns**: whether generated proteins occupy regions evolution avoided for good reason (unseen constraints) vs. genuinely new viable space.
- **Transferability**: high — the design machinery generalizes across targets and scaffolds.
- **Confidence**: **4/5**. Fastest-growing capability in the corpus (15×) and high impact; the most active realization of *reusing* an evolutionary program to produce new instances.
- **Stack reading**: reads the stack **upward** — the generative direction the thesis points to.

### 5. Predictable adaptation  *(evolutionary forecasting; n=40, 2.3× growth, conf 2/5)*
- **Capability**: forecast evolutionary trajectories — resistance, viral/immune escape, strain frequencies.
- **Known mechanisms**: predictive models of allele/strain dynamics from current state plus selection.
- **Open questions**: contingency and historical path-dependence; how far ahead prediction stays valid; rare large-effect events.
- **Unknowns**: the limits of predictability itself — how much of adaptation is forecastable in principle vs. irreducibly stochastic.
- **Transferability**: low — highly system-specific (a flu model does not transfer to bacteria).
- **Confidence**: **2/5**. The capability where "predict evolution" is most literally the goal and least solved.
- **Stack reading**: the only capability that engages SEARCH DYNAMICS over time directly — and it is the weakest, which locates the field's true frontier.

### 6. Directed / accelerated search  *(ML-guided directed evolution + evolutionary computation; n=104, 2.2× growth, conf 4/5)*
- **Capability**: make the search itself faster and smarter — propose better variants per round; run open-ended/quality-diversity search.
- **Known mechanisms**: surrogate models + active learning / Bayesian optimization close the design loop; evolutionary algorithms, MAP-Elites, novelty search on the computation side. Largest capability by volume (n=104).
- **Open questions**: sample efficiency in real wet-lab loops; open-endedness that keeps producing novelty; marrying biological priors to the search operators.
- **Unknowns**: whether learned search policies generalize across objectives or overfit one campaign.
- **Transferability**: moderate — methods transfer; tuned policies less so.
- **Confidence**: **4/5**. Mature methods, strong volume; the operational form of "evolution as a learnable search."
- **Stack reading**: this capability *is* the SEARCH DYNAMICS layer made controllable — but the biological (ML-DE) and computational (open-endedness) halves barely cite each other.

### 7. Ancestral program reconstruction  *(ML phylogenetics; n=72, 1.6× growth, conf 4/5)*
- **Capability**: reconstruct evolutionary history, ancestral sequences, and rates.
- **Known mechanisms**: likelihood and neural inference of trees and ancestral states; the mature, foundational layer.
- **Open questions**: scaling to genome-wide data; integrating with foundation-model representations.
- **Unknowns**: deep-time reconstruction accuracy where signal is saturated.
- **Transferability**: moderate — well-established methods, broadly applicable.
- **Confidence**: **4/5**. Mature and reliable, but slow-growing and largely separate from the foundation-model wave.
- **Stack reading**: the historical record of past SEARCH DYNAMICS — the empirical trace of the programs evolution already found.

---

## The synthesis for your thesis

1. **The reusable-program claim is strongest at the top of the stack and weakest at the bottom.** ML confidently reads MECHANISMS (protein fold, function) and generates from them (evolvability). It reads REGULATORY PROGRAMS partially, EVOLUTIONARY PRESSURE only as sampled points, and SEARCH DYNAMICS barely at all. The capabilities closest to your thesis's core — regulatory programs and the search dynamics that generate them — are exactly where confidence is lowest (3, 3, 2).

2. **Momentum and confidence are anti-correlated in an informative way.** Generative evolvability and fitness-landscape navigation have the highest growth (15×, 8.7×) but middling confidence — the field is rushing at *generation* faster than it is securing *understanding*. Ancestral reconstruction and structure prediction have high confidence but low momentum — solved enough to stop crowding.

3. **The field's biggest structural gap is the missing link between the two halves of "search."** Biological directed evolution (ML-DE) and computational open-endedness (evolution-as-search) occupy the same SEARCH DYNAMICS layer of your stack but form nearly disjoint literatures. Bridging them — learned search operators carrying biological priors, evaluated in real evolutionary settings — is the most direct path to your vision of AI that models and accelerates the discovery of biological programs.

4. **"Environmental harness" is the field's blind spot.** Almost no capability models the environment as an explicit, learnable scoring function. Evolution's search is defined by its harness; ML has mostly abstracted it away into a fixed training set. Making the harness itself learnable is an open, high-value direction implied directly by your input equation.

## Method & honesty notes
- Capability groupings map the 9 pass-1 paradigms onto 7 capabilities (`capability_metrics.csv` shows the mapping).
- The three **judgment** columns (mechanism, transferability, confidence) are domain-reasoned ratings, not corpus measurements — they encode expert priors and should be debated, not treated as data. The three **corpus-derived** columns are normalized from paper counts, growth, and citation rates.
- Growth ratios use 2015–19 vs 2020–24; 2025–26 is under-indexed and excluded from trend claims. Paradigm labels are keyword-derived (reliable in aggregate, noisy per paper).