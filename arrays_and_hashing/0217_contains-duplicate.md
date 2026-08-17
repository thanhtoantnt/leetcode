# 217 — Contains Duplicate

## Problem

Return `true` if any value appears at least twice in the array.

**Example:** `nums = [1,2,3,1]` → `true`

## Walkthrough

Stream into a set; the first value already present is the duplicate.

**[1] i=0**
```text
[1, 2, 3, 1]
  i
seen={1}  1 is new → add
```

**[2] i=1**
```text
[1, 2, 3, 1]
     i
seen={1,2}  2 is new → add
```

**[3] i=2**
```text
[1, 2, 3, 1]
        i
seen={1,2,3}  3 is new → add
```

**[4] i=3 — repeat caught**
```text
[1, 2, 3, 1]
           i
1 ∈ {1,2,3} → return True
```

Why it works: a set makes the membership test O(1), so O(n) time / O(n) space. The sort-then-scan-duplicates variant is O(n log n) time but O(1) extra space if in-place sorting is allowed.
