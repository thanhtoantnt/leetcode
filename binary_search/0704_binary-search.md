# 704 — Binary Search

## Problem

Find `target`'s index in a sorted array, or `-1`. The chapter-opener of every binary-search family problem in this folder.

**Example:** `nums = [-1,0,3,5,9,12]`, `target = 9` → `4`

## Walkthrough

Halve the search space each step: compare the middle element; equal → done, smaller → the answer lies right, larger → left. The `lo ≤ hi` invariant keeps every candidate inside `[lo, hi]`.

**[1] mid = 2: value 3 < 9**
```text
[-1, 0, 3, 5, 9, 12]
 L        M        H
lo=0 hi=5 mid=2  3 < 9 → lo=3
```

**[2] mid = 4: found**
```text
[-1, 0, 3, 5, 9, 12]
             L  H
mid=(3+5)//2=4  nums[4]=9 ✓ return 4
```

**[3] a miss: target=2**
```text
[-1, 0, 3, 5, 9, 12]
probes: mid=2 (3>2) → hi=1; mid=0 (−1<2) → lo=1; mid=1 (0<2) → lo=2 > hi
lo > hi → the interval is empty → return -1
```

Why it works: sortedness means one comparison against `mid` discards half the interval *safely* — everything left of mid is ≤ nums[mid] < target (or ≥, mirrored) — so the invariant "target, if present, is in [lo,hi]" survives every step. ⌈log₂ n⌉+1 probes; the same loop powers 0033 (rotated), 0074 (matrix), 0875 (on the answer), 0981 (timestamps) — all in this folder.
