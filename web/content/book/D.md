Matrix algebra — the reference for Strassen (Ch. 4), LUP/Cholesky (Ch. 28), and the all-pairs "matrix multiplication" (Ch. 25).

## The basics with teeth

Matrix multiplication as defined: (AB)_{ij} = Σ_k a_{ik}b_{kj} — Θ(n³) by definition, and the definition *is* the triple loop. Noncommutativity (AB ≠ BA in general) but associativity — the property repeated-squaring exploits, both for ordinary powers (fast exponentiation, `maths/0050`) and for shortest-path products (Ch. 25.1: L^(2k) = L^(k)·L^(k)).

Identity, inverse (exists ⟺ nonsingular ⟖ nonzero determinant), transpose, and the identities worth knowing cold: (AB)ᵀ = BᵀAᵀ, (AB)⁻¹ = B⁻¹A⁻¹.

## Structured matrices

- Triangular: back-substitution solves in O(n²) — why LUP decomposes.
- Symmetric (A = Aᵀ) and positive definite (xᵀAx > 0 for x ≠ 0): SPD matrices have Cholesky, no pivoting, and are what least-squares normal equations produce.
- Determinants: nonzero ⟺ invertible; the volume interpretation; computable by LU in Θ(n³).

## Why it's an appendix and not a chapter

The main text borrows three things: the multiplication triple-loop (as the semiring template Floyd-Warshall and transitive closure re-instantiate with min/+ and ∨/∧), associativity for repeated squaring, and the transpose/inverse algebra identities the LP duality and least-squares derivations shuffle. Everything else is context for numerical methods texts.

For this repo: `matrix/` problems are index manipulation, but DP-over-pairs recurrences (edit distance, LCS-style) are morally triangular matrix fills — you compute table entries in an order that respects dependency, which is exactly solving a triangular system.
