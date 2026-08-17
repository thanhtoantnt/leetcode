# 875 — Koko Eating Bananas

## Problem

Piles of bananas, `h` hours. Eating at speed `k` bananas/hour, Koko finishes each pile over `ceil(pile/k)` hours (one pile per hour at most). Find the **minimum k** that finishes all piles within `h`.

**Example:** `piles = [3,6,7,11]`, `h = 8` → `4`

## Walkthrough

**Binary search on the answer, not the array.** The feasibility function — "can speed k finish in h hours?" — is monotone (faster ⇒ never slower to finish), so the answer space is [1, max(pile)] and binary search finds its first `true`.

**[1] hours needed, as a function of k**
```text
[3, 6, 7, 11]
k=1 → 3+6+7+11 = 27h  too slow for h=8
```

**[2] probe the middle, k=6**
```text
[3, 6, 7, 11]
 L        H  M(k=6)
hours=1+1+2+2=6 ≤ 8  feasible → but maybe smaller works → hi=6
```

**[3] probe k=3**
```text
[3, 6, 7, 11]
hours=1+2+3+4=10 > 8  infeasible → lo=4
```

**[4] probe k=4 — the boundary**
```text
[3, 6, 7, 11]
 L  H
hours=1+2+2+3=8 ≤ 8  feasible → hi=4 → lo==hi
```

**[5] converged on the first feasible speed**
```text
[3, 6, 7, 11]
return 4  k=3 gives 10h ✗, k=4 gives 8h ✓
```

Why it works: monotone feasibility makes the answer space a block of `false` followed by `true` — binary search locates the boundary in O(log max(pile)) probes, each probe O(n). This "binary search the answer" pattern applies whenever a threshold-like property is monotone (capacity, size, speed).
