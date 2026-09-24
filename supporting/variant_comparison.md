# Choosing between the three Bridge 2 variants

All three are built from the same verified core: the two extracted models, the six-role template, the three-level
equivalence verdict (Level 2 holds, Level 3 fails), the synthetic double-well benchmark, and the three false-friend
negative controls. They differ in **what the paper claims to contribute**, which changes the referee you get.

| | **A · Narrow translation** | **B · Translation + method** | **C · Position** |
|---|---|---|---|
| **Title claim** | These two models are the same algorithm with different capacity | Here is a detector for such pairs, plus a worked adjudication | Disconnected literatures converge on the same computation |
| **Core contribution** | One correspondence, fully adjudicated | Detector **and** adjudication | An argument, evidenced by one case |
| **Length** | Shortest | Longest | Middle |
| **What a referee checks** | The equations and the benchmark — both checkable in an afternoon | Also: does the detector generalise? what is its recall? | Whether one example supports a general claim |
| **Main risk** | "Interesting, but it's two papers — so what?" | "Two contributions; split it" | "Speculative" — the risk you named wanting to avoid |
| **Strongest sentence** | Level 3 fails, and the failure specifies the unification | The three spaces are uncorrelated (ρ=0.02) across 522 papers | Reading by topic systematically misses this class of correspondence |
| **Sets up next** | The unification paper (Eq. 9) | ResearchOS as method infrastructure | The whole program, including Bridges 1 and 3 |

## The honest read

**A is the hardest to dismiss.** Every claim is checkable against two published papers and one runnable benchmark. There is no unverified generalisation anywhere in it. If the goal is credibility first — the wedge strategy — this is the one, and its weakness ("so what?") is answered by the unification target in Eq. 9, which is a concrete next experiment rather than a gesture.

**B is the highest-value if the detector holds up.** It claims priority on the method, not just the translation. But it makes a claim the current work does not yet support: the detector's **recall is uncharacterised**, and a referee will ask. B is the right paper *after* two or three more bridges have been adjudicated — at that point the detector has a track record and the method section is evidence rather than description.

**C is the one you said you did not want.** It is the most exciting to read and the easiest to reject, because the general claim rests on a single worked example. It becomes the right paper once Bridges 1 and 3 are also validated — three worked examples across three different isomorphisms (STATE, OBJECTIVE, REPRESENTATION) would carry a position paper that one cannot.

## Recommendation

Publish **A** now; hold **B** until the skills have produced two or three more adjudicated bridges; write **C** last, as the program paper. That ordering also matches the artifact cascade already planned — A is the credibility wedge, B is the ResearchOS methods paper, C is the founder-facing argument.

One caveat that applies to all three: the benchmark is synthetic. It establishes a difference in representational capacity, not its biological consequence. Whichever variant goes first should keep that limitation in the Discussion, where it currently sits, rather than in a footnote.
