# 976 — Largest Perimeter Triangle

## Problem

Pick 3 sticks forming a non-degenerate triangle (strict triangle inequality); maximize the perimeter. 0 if none.

**Example:** `[2,1,2]` → `5`; `[1,2,1,10]` → `0` (10 dwarfs everything)

## Walkthrough

Sort descending; scan consecutive triples `a ≥ b ≥ c`. The triangle condition reduces to `b + c > a` (the other inequalities are free). The **first** triple that passes is the maximum perimeter.

**[1] sorted: [10, 2, 1, 1]**
```text
try (10, 2, 1): 2 + 1 = 3 > 10? ✗
```

**[2] slide the window**
```text
try (2, 1, 1): 1 + 1 = 2 > 2? ✗ (degenerate — collinear)
no triples left → return 0
```

**[3] a working case [3,3,2,4] → sorted [4,3,3,2]**
```text
try (4, 3, 3): 3 + 3 = 6 > 4 ✓ → perimeter 10 — first hit wins
```

**[4] why consecutive triples suffice**
```text
given a ≥ b ≥ c failing (b + c ≤ a), any other triple containing a is
no better: its other two sides are ≤ b, c — swap-in only shrinks the
sum → skip a entirely, move the window
```

**[5] why the first pass is maximal**
```text
scanning in descending order of the largest side: any later triple has
a smaller maximum side and thus a perimeter ≤ 3a' < a + b + c… any
passing triple later is dominated by the earlier one's parts
```

Why it works: for sorted sides the binding constraint is one inequality (`b + c > a`), and the exchange argument above shows the greedy window never skips a feasible better answer — sort, then first-fit. O(n log n). The classic two/three-pointer geometry shape; compare 0334's increasing-triplet scan (arrays).
