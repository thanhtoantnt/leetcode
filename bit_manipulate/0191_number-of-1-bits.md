# 191 — Number of 1 Bits

## Problem

Count the set bits (Hamming weight) of a 32-bit integer.

**Example:** `n = 0b00000000000000000000000000001011` → `3`

## Walkthrough

**Kernighan's trick**: `n & (n−1)` clears the *lowest set bit* — subtracting 1 flips the low 1 and every 0 below it, and the AND keeps everything above intact. Loop until zero; each iteration retired exactly one set bit.

**[1] n = 1011₂**
```text
n = 1011
count=0  bits set: three (8, 2, 1)
```

**[2] first kill — the 1**
```text
n = 1011 & 1010 = 1010
count=1  n−1 = 1010: low 1 flipped, zeros below flipped
```

**[3] second kill — the 2**
```text
n = 1010 & 1001 = 1000
count=2
```

**[4] third kill — the 8**
```text
n = 1000 & 0111 = 0
count=3 ✓ done in 3 iterations, not 32
```

**[5] why n & (n−1) targets the lowest set bit**
```text
n     = …x 1 0 0 0
n−1   = …x 0 1 1 1   (borrow flips the low block)
n&(n−1)= …x 0 0 0 0   the 1 vanishes, higher bits untouched
```

Why it works: subtraction's borrow flips precisely the lowest set bit and the zeros beneath it — the AND masks those out, leaving n minus its lowest 1. Iterations = popcount, O(k) not O(32). Python's `int.bit_count()` (3.10+) and CPU `POPCNT` do it in hardware; this is the classic software version (CLRS Ch. 2 exercises / Hacker's Delight).
