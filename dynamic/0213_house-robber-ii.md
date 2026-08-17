# 213 — House Robber II

## Problem

House Robber on a **circle**: first and last houses are neighbors — can't rob both.

**Example:** `nums = [2,3,2]` → `3` (rob middle only)

## Walkthrough

Break the circle into two ordinary rows: **exclude the first house** (rob houses 1..n−1) or **exclude the last** (rob 0..n−2). The linear Robber (problem 198's flipbook) solves each; the answer is the max. Every legal circular selection misses at least one end, so it appears in one of the two rows.

**[1] the circle — 2,3,2 with ends adjacent**
```text
[2, 3, 2]
 S     E
2 and 2 are neighbors → robbing both is off the table
```

**[2] case A: skip house 0 → rob [3,2] linearly**
```text
[2, 3, 2]
 ✗  take=3
skip 3? no — linear best of [3,2] = 3
```

**[3] case B: skip house 2 → rob [2,3] linearly**
```text
[2, 3, 2]
 take → best of [2,3] = 3
```

**[4] combine**
```text
return max(3, 3) = 3
```

**[5] sanity on [1,2,3,1]**
```text
A: rob [2,3,1] → 3;  B: rob [1,2,3] → 4 → answer 4 (1+3, non-adjacent even on the circle)
```

Why it works: a valid selection on the circle is valid on at least one of the two linear views (it can't contain both end houses), and both views only allow valid circular selections — so the max over both is exact. Two runs of the linear O(n) recurrence (skip or take, see the 0198 flipbook) → O(n) total, O(1) space each. Edge cases n=1 (rob it) and n=2 (the max of the two) fall out with care in slicing.
