# 1695 — Maximum Erasure Value

## Problem

Erase exactly one subarray of **distinct** values; score is its sum. Maximize the score.

**Example:** `nums = [4,2,4,5,6]` → `17` (`[2,4,5,6]`)

## Walkthrough

Problem 3's no-repeat window, but maximizing **sum** instead of length: the same left/right pointers, a set (or last-seen map) enforcing distinctness, and a running window sum.

**[1] window [4]**
```text
[4, 2, 4, 5, 6]
 L  R
sum=4 best=4  distinct ✓
```

**[2] window [4,2]**
```text
[4, 2, 4, 5, 6]
 L     R
sum=6 best=6
```

**[3] second 4 — duplicate: shrink**
```text
[4, 2, 4, 5, 6]
    L     R
sum=2+4=6  old 4 evicted (L=1), then distinct again
```

**[4] extend through 5, 6**
```text
[4, 2, 4, 5, 6]
    L        R
sum=17 best=17  [2,4,5,6] all distinct ✓
```

**[5] done**
```text
return 17
```

Why it works: every candidate answer is a distinct-valued subarray, and the sliding window enumerates each maximal such subarray — L only moves when forced, so the best window is fully scanned. Sum updates in O(1) (add on enter, subtract on leave). O(n) with the last-seen map (which jumps L directly past the duplicate instead of stepping). One window template: condition = "all distinct", objective = "sum" — swap either without touching the skeleton.
