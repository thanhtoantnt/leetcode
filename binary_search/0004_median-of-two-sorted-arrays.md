# 4 — Median of Two Sorted Arrays

## Problem

Median of two sorted arrays in O(log(m+n)).

**Example:** `nums1 = [1,3]`, `nums2 = [2]` → `2.0`; `[1,2]` + `[3,4]` → `2.5`

## Walkthrough

A median **partitions** the union into equal halves (left half ≤ right half). Binary-search the cut in the shorter array `a`: cut `i` forces cut `j = half − i` in `b`; the partition is valid when `a's left ≤ b's right` and `b's left ≤ a's right` — then the median reads off the boundary elements.

`a = [1,3]`, `b = [2]` (half = 2):

**[1] cut i=1 → j=1**
```text
a: 1 | 3
b: 2 |
left={1,2} right={3}  aL=1 ≤ bR=inf ✓ but bL=2 > aR=3? no: 2 ≤ 3 ✓ valid
```

**[2] valid partition — odd total**
```text
a: 1 | 3
b: 2 |
left = {1,2}, right = {3}  median = max-left = 2.0 ✓
```

**[3] even case [1,2]+[3,4], cut i=1, j=1**
```text
a: 1 | 2
b: 3 | 4
left = {1,3}, right = {2,4}  3 ≤ 2? ✗ invalid → aL too small → i++
```

**[4] cut i=2, j=0**
```text
a: 1 2 |
b:   | 3 4
left = {1,2}, right = {3,4}  valid → median = (2+3)/2 = 2.5 ✓
```

**[5] invalid-cut repair rule**
```text
aL > bR  →  a's cut too far right → hi = i−1
bL > aR  →  a's cut too far left  → lo = i+1
```

Why it works: a valid partition exists for any sorted union, and the validity test is monotone in `i` — bigger `i` moves large elements left, breaking `bL ≤ aR` first. Binary search over the shorter array: O(log min(m,n)). ±∞ sentinels at the edges make boundary cuts (empty side) compare naturally.
