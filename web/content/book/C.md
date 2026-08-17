Counting and probability — the appendix behind Chapter 5 (probabilistic analysis) and every randomized argument in the book.

## Counting

Rules of sum, product, permutation, and the combinations C(n,k) = n!/(k!(n−k)!) — binomial coefficients, Pascal's identity (the DP recurrence of `dynamic/0062`-style grid walking and Pascal's-triangle problems), the binomial distribution. Stars and bars for compositions — the counting behind "distribute n among k" DP states.

## Axioms and the useful consequences

Discrete probability: events, independence, conditional probability, Bayes's theorem. The workhorse corollaries:

- **Union bound**: Pr[A ∪ B] ≤ Pr[A] + Pr[B] — the sloppy-but-valid upper bound in every randomized-algorithm error analysis (Miller-Rabin's error rate, Ch. 31).
- **Independence means multiply**; conditional independence chains into the analysis of random shuffles and hashing.

## Random variables and expectation

Expected value, linearity of expectation (dependent or not — the property that makes indicator-variable arguments work), variance, and the standard distributions: Bernoulli, binomial, geometric (expected trials until first success = 1/p — the analysis of randomized quickselect and polling-style loops).

The tail bounds that matter:

- **Markov**: Pr[X ≥ t] ≤ E[X]/t — weak, assumption-free.
- **Chebyshev**: Pr[|X−E[X]| ≥ t] ≤ Var(X)/t² — variance version.
- **Chernoff-style bounds** (via binomial tails): exponentially small tails for sums of independent indicators — why sampling and hashing concentrate hard around their means and "with high probability" statements are honest.

The mental habit this appendix trains: when an algorithm's cost is a sum of events, write it as indicators, take expectations linearly, and only then ask what the probabilities are — Chapter 5's hiring analysis, quicksort's E[X], bucket sort's E[n_i²], all of them.
