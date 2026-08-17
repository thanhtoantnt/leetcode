# 27 — Remove Element

## Problem

Remove every occurrence of `val` **in place**; return the length of the surviving prefix.

**Example:** `nums = [0,1,2,2,3,0,4,2]`, `val = 2` → length `5`, prefix `[0,1,3,0,4]` (any order).

## Walkthrough

0026's reader/writer pair (this folder) with the simplest test: `nums[r] != val` → keep. Survivors compact toward the front; the tail is garbage.

**[1] r=0,1 — kept**
```text
[0, 1, 2, 2, 3, 0, 4, 2]
 W  R
0 and 1 ≠ 2 → written, w advances with r
```

**[2] r=2,3 — the targets, skipped**
```text
[0, 1, 2, 2, 3, 0, 4, 2]
    W     R
2 == val → nothing written; w parked at index 2
```

**[3] r=4 — 3 fills the hole**
```text
[0, 1, 3, 2, 3, 0, 4, 2]
    W        R
nums[2]=3, w=3  compaction: survivors slide over the gaps
```

**[4] the rest**
```text
[0, 1, 3, 0, 4, 0, 4, 2]
          W           R
0 and 4 written → w=5
```

**[5] result**
```text
return 5  prefix [0,1,3,0,4] — order irrelevant, only the first 5 cells count
```

Why it works: every non-`val` element must appear exactly once in the prefix, and the writer places each there in first-encounter order — the swap-variant (`nums[w]=nums[r]` only on skip, then `w+=1` with tail-shrink) is the same compaction with fewer writes. O(n) one pass, O(1) space.
