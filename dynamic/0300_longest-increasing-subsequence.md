# 300 — Longest Increasing Subsequence

## Problem

Given an integer array, return the length of the longest **strictly increasing subsequence** (elements in order, not necessarily contiguous).

**Example:** `nums = [10,9,2,5,3,7,101,18]` → `4` (`[2,3,7,18]` or `[2,5,7,101]`)

## Walkthrough

`dp[i]` = length of the best increasing subsequence **ending at** `i`. It's `1 + max(dp[j])` over all `j < i` with `nums[j] < nums[i]` — or just 1 if nothing smaller precedes it. (`.` = not computed yet.)

**[1] i=0,1,2 — each starts alone**
```text
nums: 10 9 2 5 3 7 101 18
dp:    1 1 1 . . . .   .
i=2  nothing smaller before 2/9/10 → all dp = 1
```

**[2] i=3 (value 5) — builds on 2**
```text
nums: 10 9 2 5 3 7 101 18
dp:    1 1 1 2 . . .   .
i=3  j=2 (2<5): dp[3] = dp[2]+1 = 2
```

**[3] i=4 (value 3) — also builds on 2**
```text
nums: 10 9 2 5 3 7 101 18
dp:    1 1 1 2 2 . .   .
i=4  3 beats only 2 → dp[4] = 2
```

**[4] i=5 (value 7) — best of [2,5,3]**
```text
nums: 10 9 2 5 3 7 101 18
dp:    1 1 1 2 2 3 .   .
i=5  7 > 5 (dp 2) → dp[5] = 3
```

**[5] i=6,7 — the tail**
```text
nums: 10 9 2 5 3 7 101 18
dp:    1 1 1 2 2 3 4   4
i=7  101 extends dp 3 → 4; 18 also extends dp 3 → 4
```

Answer = `max(dp)` = `4`.

Why it works: an increasing subsequence ending at i must have a previous element nums[j] < nums[i] as its second-to-last — so checking every smaller predecessor is exhaustive. O(n²) here; patience sorting / binary search over tails gets O(n log n) (CLRS Ex. 15.4-6 territory).
