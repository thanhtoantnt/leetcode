# 494 — Target Sum

## Problem

Assign each number `+` or `−`; count the ways to hit `target`.

**Example:** `nums = [1,1,1,1,1]`, `target = 3` → `5`

## Walkthrough

Every assignment splits nums into a `+` group (sum P) and a `−` group (sum N): P − N = target and P + N = total — so **P = (total + target)/2**. Counting assignments = counting subsets summing to P: the same reachable-set DP as 416, but counting ways instead of existence.

**[1] total = 5, P = (5+3)/2 = 4**
```text
sums: 0 1 2 3 4
ways: 1 . . . .
counting subsets of [1,1,1,1,1] that sum to 4
```

**[2] first 1**
```text
sums: 0 1 2 3 4
ways: 1 1 . . .
each sum's ways: old ways (skip this 1) + ways[sum−1] (take it)
```

**[3] second 1**
```text
sums: 0 1 2 3 4
ways: 1 2 1 . .
ways[1] = 1+1 = 2; ways[2] = 0+1 = 1
```

**[4] third 1**
```text
sums: 0 1 2 3 4
ways: 1 3 3 1 .
the binomial row builds — identical items, positions distinct
```

**[5] fifth 1 completes Pascal's triangle**
```text
sums: 0 1 2 3 4
ways: 1 5 10 10 5
ways[4] = 5 → answer 5
```

Why it works: the algebra converts sign assignment into subset selection, and the ways-table recurrence is the 0/1 knapsack count — each element extends every reachable sum by exactly one new path per old path. O(n · P) time. Edge cases: `(total+target)` odd or `|target| > total` → 0. The DP is pseudo-polynomial (subset-sum in disguise, Ch. 34→35).
