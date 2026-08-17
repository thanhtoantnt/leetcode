Summations — the appendix every chapter's analysis quietly leans on. If a proof in the main chapters manipulated a Σ and you took it on faith, this is where it's justified.

## The three sums that cover 90% of use

- **Arithmetic series**: Σ_{k=1}^{n} k = n(n+1)/2 = Θ(n²). The cost of insertion sort's inner loop, of triangular pairwise scans, of building adjacency matrices.
- **Geometric series**: Σ_{k=0}^{n} x^k = (x^{n+1}−1)/(x−1) = Θ(x^n) for x > 1 — bounded by a constant times its last term. The recursion-tree levels of T(n)=2T(n/2)+Θ(n) (each level Θ(n), lg n levels... via the next one), the BUILD-HEAP O(n) proof (Σ n/2^{h+1}·h), amortized table doubling.
- **Harmonic series**: Σ_{k=1}^{n} 1/k = ln n + O(1). Quickselect pivots (Ch. 9), hiring (Ch. 5), log^2 bucket analyses.

## Techniques the book actually uses

Bounding sums by integrals (Σ 1/k ≈ ∫dx/x), splitting sums into dominant and negligible parts (drop the first/last terms where a series is small), substitution of variables (k = j−i in quicksort's analysis). Stirling's approximation for lg(n!) = Θ(n lg n) — the sorting lower bound (Ch. 8) and decision-tree leaves in one line.

Fibonacci closed forms and the golden ratio φ ≈ 1.618 show up here too — the worst cases of Euclid's algorithm and the Fibonacci-heap degree bound are both "because Fibonacci grows like φⁿ."

Read it as a toolbox, not a chapter: when an analysis needs "how big is this Σ", the answer is almost always one of the three series above with a substitution.
