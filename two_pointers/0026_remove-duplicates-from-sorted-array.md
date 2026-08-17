# 26 — Remove Duplicates from Sorted Array

## Problem

Remove duplicates **in place** from a sorted array; return the length of the deduplicated prefix.

**Example:** `nums = [0,0,1,1,1,2,2,3,3,4]` → length `5`, prefix `[0,1,2,3,4]`

## Walkthrough

Read/write two pointers: `w` marks where the next unique value belongs, `r` scans. Sorted order puts all copies of a value adjacent, so "new value ≠ last written" is the complete novelty test.

**[1] w=1, r=1 — 0 is a repeat**
```text
[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    W  R
nums[r]==nums[w-1] → skip
```

**[2] r hits 1 — write it**
```text
[0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
    W  R
1 ≠ 0 → nums[w]=1, w++
```

**[3] 1s and 2s**
```text
[0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
       W        R
repeats skipped; 2 written at w=2
```

**[4] sweep to the end**
```text
[0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
             W           R
3 and 4 written; the tail beyond w is garbage, ignored
```

**[5] result**
```text
return w=5  prefix [0,1,2,3,4] ✓
```

Why it works: sortedness ⟹ equal values are contiguous ⟹ first-occurrence-of-a-run is the only cell that must survive — and the write pointer's compare-against-last-written (`nums[w−1]`) detects exactly run boundaries. Every element is read once, each unique value written once: O(n), O(1) space. The array-fold sibling: 27 (remove-by-value) uses the same reader/writer pair with a value test instead.
