# 121 — Best Time to Buy and Sell Stock

## Problem

One buy and one sell (buy first): max profit, or 0.

**Example:** `prices = [7,1,5,3,6,4]` → `5` (buy 1, sell 6)

## Walkthrough

One pass tracking `minSoFar`: the best sale **ending today** is `price − minSoFar`. Update the min, keep the best difference — sell-day DP where only one variable of history matters.

**[1] day 0: min = 7**
```text
[7, 1, 5, 3, 6, 4]
  i
min=7 best=0  profit vs 7 is ≤ 0 everywhere; nothing to do
```

**[2] day 1: a cheaper buy**
```text
[7, 1, 5, 3, 6, 4]
     i
min=1 best=0  1 < 7 → new buying opportunity
```

**[3] day 2: sell at 5**
```text
[7, 1, 5, 3, 6, 4]
        i
min=1 best=4  5−1 = 4
```

**[4] day 4: sell at 6**
```text
[7, 1, 5, 3, 6, 4]
              i
min=1 best=5  6−1 = 5 ✓ the answer
```

**[5] day 5 — nothing better**
```text
[7, 1, 5, 3, 6, 4]
min=1 best=5  return 5
```

Why it works: for each potential sell day, the optimal buy is the cheapest price before it — exactly `minSoFar`. One pass, O(n), O(1). Kadane-shaped: `best = max(best, price − min)` is "max subarray sum" on the daily-difference array (problem 53's flipbook in `dynamic/`).
