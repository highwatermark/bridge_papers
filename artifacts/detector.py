"""Three-space cross-literature detector — frozen specification (recovered verbatim
from the original analysis cells). Import and call run_detector()."""
import numpy as np, pandas as pd

# ---- Six-role lexicon: each role lists terms from BOTH literatures ----------
SCHEMA = {
 "STATE": {
   "evolution-ML": ["genotype","sequence","variant","genome","allele","protein","population state"],
   "systems-harness": ["cell state","expression state","phenotype state","attractor","stable state","cell type","configuration"]},
 "TRANSITION_OPERATOR": {
   "evolution-ML": ["mutation","recombination","variation operator","substitution","genetic operator","crossover"],
   "systems-harness": ["state transition","cell fate transition","reprogramming","differentiation","signal-induced","perturbation response","switch"]},
 "OBJECTIVE": {
   "evolution-ML": ["fitness","selection","fitness landscape","adaptive","objective","selective pressure"],
   "systems-harness": ["attractor stability","robustness","canalization","landscape","potential","stability","optimal response"]},
 "SEARCH": {
   "evolution-ML": ["evolutionary search","directed evolution","optimization","genetic algorithm","exploration","evolve"],
   "systems-harness": ["trajectory","dynamics","navigation","path","flow","dynamical","evolve toward"]},
 "REPRESENTATION": {
   "evolution-ML": ["embedding","language model","representation","latent","foundation model","encoder","learned"],
   "systems-harness": ["gene regulatory network","grn","regulatory network","network model","circuit","topology","inference"]},
 "FEEDBACK": {
   "evolution-ML": ["generation","iterative","selection cycle","adaptation over","feedback","repeated"],
   "systems-harness": ["signal","stimulus","environment","induction","condition","exposure","input","feedback loop"]},
}
ROLES = list(SCHEMA)

def role_terms(schema=SCHEMA):
    return {r: [t for p in schema[r].values() for t in p] for r in schema}

def signatures(texts, schema=SCHEMA):
    """sig[i,j] = number of DISTINCT lexicon terms of role j present in text i
    (case-insensitive substring match; each term counted at most once)."""
    terms = role_terms(schema)
    roles = list(schema)
    sig = np.zeros((len(texts), len(roles)))
    for i, t in enumerate(texts):
        t = str(t).lower()
        for j, r in enumerate(roles):
            sig[i, j] = sum(1 for x in terms[r] if x in t)
    return sig

def primitive_cosine(sig):
    """sqrt(counts) -> L2 normalise -> cosine."""
    S = np.sqrt(sig)
    return S / (np.linalg.norm(S, axis=1, keepdims=True) + 1e-9)

def jaccard(ra, rb):
    ra, rb = set(ra or []), set(rb or [])
    return len(ra & rb) / len(ra | rb) if ra and rb else 0.0

def run_detector(comb, emb, refs, schema=SCHEMA, min_roles=4, texts=None):
    """Returns dict with rich-subset indices and the three cross-literature matrices."""
    texts = comb["text"].values if texts is None else texts
    sig = signatures(texts, schema)
    rich = (sig > 0).sum(1) >= min_roles
    evo = np.where((comb.pillar.values == "evolution-ML") & rich)[0]
    har = np.where((comb.pillar.values == "systems-harness") & rich)[0]
    Sn = primitive_cosine(sig)
    prim = Sn[evo] @ Sn[har].T
    En = emb / (np.linalg.norm(emb, axis=1, keepdims=True) + 1e-9)
    concept = En[evo] @ En[har].T
    ids = comb["id"].values
    cit = np.array([[jaccard(refs.get(ids[a]), refs.get(ids[b])) for b in har] for a in evo])
    return dict(sig=sig, rich=rich, evo=evo, har=har, prim=prim, concept=concept, cit=cit)

def quadrants(prim, concept, cit, p_hi=0.90, c_q=0.90, require_zero_cit=False):
    """Original definition: P = prim >= p_hi ; C = concept >= quantile(c_q).
    hidden = P & ~C  (optionally & cit==0)."""
    C = concept >= np.quantile(concept, c_q)
    P = prim >= p_hi
    Z = (cit == 0) if require_zero_cit else np.ones_like(P, bool)
    return {"both_high": P & C, "hidden": P & ~C & Z, "false_friend": C & ~P, "neither": ~P & ~C}
