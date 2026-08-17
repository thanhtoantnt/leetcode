# 50 — Pow(x, n)

## Problem

Implement `pow(x, n)` — compute xⁿ in O(log n) multiplications.

**Example:** `x = 2`, `n = 13` → `8192`

## Walkthrough

Binary exponentiation (square-and-multiply). 13 = `1101`₂ = 8+4+1, so x¹³ = x⁸·x⁴·x¹. The loop consumes `n` one bit at a time (LSB first), squaring a running base; whenever the bit is 1, fold that power into the result.

**[1] bit 0 of 13 = 1 — fold in x¹**
```text
[1, 1, 0, 1]
          B
res=1→2 sq=2→4  n=13 odd → res *= 2, then sq = 2², n = 6
```

**[2] bit = 0 — square only**
```text
[1, 1, 0, 1]
       B
res=2 sq=4→16  n=6 even → res untouched, sq = 4², n = 3
```

**[3] bit = 1 — fold in x⁴**
```text
[1, 1, 0, 1]
    B
res=2→32 sq=16→256  n=3 odd → res *= 16, sq = 16², n = 1
```

**[4] last bit = 1 — fold in x⁸**
```text
[1, 1, 0, 1]
 B
res=32→8192 sq=256  n=1 odd → res *= 256 → 2·16·256 = 2¹³, n = 0
```

**[5] done**
```text
[1, 1, 0, 1]
res=8192  return 8192 — 4 iterations instead of 12 multiplications
```

Why it works: after k iterations `sq = x^(2^k)` — exactly the place value of the bit just consumed — so the res product assembles precisely the set bits of n. Negative `n`: invert `x` first. Same square-and-multiply as modular exponentiation in CLRS Ch. 31 (RSA's workhorse).
