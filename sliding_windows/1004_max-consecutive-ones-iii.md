# 1004 — Max Consecutive Ones III

## Problem

Binary array; flip at most `k` zeros. Longest run of 1s achievable.

**Example:** `nums = [1,1,1,0,0,0,1,1,1,1,0]`, `k = 2` → `6`

## Walkthrough

Longest window containing **at most k zeros** — grow right; when zeros in the window exceed k, shrink left until one zero leaves. The zero count is the only state.

**[1] window of 1s — free**
```text
[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
 L        R
zeros=0 best=3  all ones so far
```

**[2] first two zeros — budget spent**
```text
[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
 L           R
zeros=2 best=5  1,1,1,0,0 with both zeros flipped
```

**[3] third zero — over budget, shrink**
```text
[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
          L     R
zeros=2  left moves past three 1s and one 0 — one zero expelled
```

**[4] ride the run of 1s**
```text
[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
          L           R
zeros=2 best=6  window [0,0,1,1,1,1] — 4 ones + 2 flipped zeros
```

**[5] last zero: shrink again, no gain**
```text
[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
              L           R
return 6
```

Why it works: any valid window has ≤ k zeros; the two-pointer sweep visits each maximal such window (never shrinking past the optimum — L moves only under constraint violation). O(n), O(1). The non-shrinking variant (window only grows, tracks max size) also works here since the answer only needs "at most k": if the window can't grow, L++ with R++ slides it monotonically.
