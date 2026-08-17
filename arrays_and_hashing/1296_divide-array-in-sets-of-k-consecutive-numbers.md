# 1296 — Divide Array in Sets of K Consecutive Numbers

## Problem

Can the array be partitioned into groups of exactly `k` **consecutive** integers?

**Example:** `nums = [1,2,3,3,4,4,5,6]`, `k = 4` → `true` (`1,2,3,4` + `3,4,5,6`)

## Walkthrough

Identical engine to 0846 (`greedy/`): the smallest remaining value has no choice but to **start** its run — so scan values ascending, peel `count[min]` runs of length k, and fail the moment a needed value is short.

**[1] counts: 1¹ 2¹ 3² 4² 5¹ 6¹, k=4**
```text
min = 1, need = 1 run of 1-2-3-4
```

**[2] peel 1,2,3,4**
```text
counts → 3¹ 4¹ 5¹ 6¹
```

**[3] min = 3, need 1**
```text
run 3-4-5-6 ✓ → True
```

**[4] the failure shape**
```text
[1,2,4,5,6,7] k=3: min 1 needs 2,3 — count[3]=0 → False
the run breaks at the first missing value
```

**[5] the modulo gate**
```text
len(nums) % k ≠ 0 → False before any counting
```

Why it works: same forced-greedy lemma as 0846 — the minimum card's run must begin at it — with identical Counter arithmetic; the problems differ only in naming (cards vs sets). O(n log n) for the sorted keys; a heap peels runs identically. Run-length grouping with duplicates handled by *multiplicity*, not by sorting the raw array.
