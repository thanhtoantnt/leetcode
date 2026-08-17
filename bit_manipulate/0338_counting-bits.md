# 338 — Counting Bits

## Problem

Return an array of the popcount (number of 1-bits) of every integer `0..n` — O(n), no per-number bit loops.

**Example:** `n = 5` → `[0,1,1,2,1,2]`

## Walkthrough

Reuse the Kernighan fact from 0191: `i & (i−1)` is `i` with its lowest set bit removed — a *smaller, already-solved* number. `bits[i] = bits[i & (i−1)] + 1` counts the bit we just stripped.

**[1] seed bits[0] = 0**
```text
i:  0 1 2 3 4 5
b:  0 . . . . .
zero has no set bits
```

**[2] i=1: 1 & 0 = 0**
```text
i:  0 1 2 3 4 5
b:  0 1 . . . .
bits[1] = bits[0] + 1 = 1
```

**[3] i=2: 10 & 01 = 0; i=3: 11 & 10 = 2**
```text
i:  0 1 2 3 4 5
b:  0 1 1 2 . .
bits[2] = 0+1;  bits[3] = bits[2]+1 = 2
```

**[4] i=4, i=5**
```text
i:  0 1 2 3 4 5
b:  0 1 1 2 1 2
bits[4] = bits[0]+1 (100→000);  bits[5] = bits[4]+1 (101→100)
```

**[5] the alternative recurrence**
```text
bits[i] = bits[i >> 1] + (i & 1)  — "popcount of i = popcount of i/2
plus the dropped last bit"; both work, same O(n)
```

Why it works: each i reduces to a strictly smaller index by one cheap bit operation — the DP dependency graph is a DAG rooted at 0, so one upward pass computes everything exactly once. O(n) total versus O(n log n) for per-number Kernighan. (Same i&(i−1) fact as 0191's flipbook, this folder.)
