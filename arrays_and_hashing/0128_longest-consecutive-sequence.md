# 128 — Longest Consecutive Sequence

## Problem

Return the length of the longest run of consecutive integers (values, not positions) that can be formed from `nums`. Must be O(n).

**Example:** `nums = [100,4,200,1,3,2]` → `4` (`1,2,3,4`)

## Walkthrough

Put everything in a set. A run **starts** at `x` only when `x−1` is absent — otherwise wait for the true start. From each start, walk upward while the next value exists.

**[1] build the set**
```text
[100, 4, 200, 1, 3, 2]
  i
set={1,2,3,4,100,200}  order in the array is irrelevant
```

**[2] 100 starts a run — nobody above**
```text
[100, 4, 200, 1, 3, 2]
  i
99 ∉ set → 100 is a start; 101 ∉ set → run length 1
```

**[3] 4 is not a start — skip entirely**
```text
[100, 4, 200, 1, 3, 2]
     i
3 ∈ set → 4 is mid-run, skip: its run is measured from 1
```

**[4] 1 starts the real run**
```text
[100, 4, 200, 1, 3, 2]
              i
0 ∉ set → start: 1→2→3→4, then 5 ∉ set → length 4
```

**[5] done**
```text
[100, 4, 200, 1, 3, 2]
best=4  200 only makes a run of 1 → return 4
```

Why it works: the skip guard means each consecutive run is walked exactly once (from its smallest element), so the total work across all walks is O(n) despite the nested loop — sorting would be O(n log n), a set membership test is O(1).
