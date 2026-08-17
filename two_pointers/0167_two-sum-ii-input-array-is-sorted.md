# 167 — Two Sum II (sorted array)

## Problem

Given a 1-indexed **sorted** array `numbers` and a `target`, find the two numbers that add up to `target`. Return their 1-indexed positions. Exactly one solution; you may not use the same element twice.

**Example:** `numbers = [2, 7, 11, 15]`, `target = 9` → `[1, 2]` because `2 + 7 = 9`

## Walkthrough

Two pointers from both ends. Sum too big → move `right` left. Sum too small → move `left` right.

**[1] start**
```text
[2, 7, 11, 15]
 L           R
L=0 R=3   sum = 2 + 15 = 17 > 9 → too big, R--
```

**[2] shrink right**
```text
[2, 7, 11, 15]
 L       R
L=0 R=2   sum = 2 + 11 = 13 > 9 → still big, R--
```

**[3] shrink right again**
```text
[2, 7, 11, 15]
 L   R
L=0 R=1   sum = 2 + 7 = 9 ✓
```

**[4] found — return 1-indexed**
```text
[2, 7, 11, 15]
 L   R
return [1, 2]
```

Why it works: sum > target can only be fixed by a smaller R; sum < target only by a bigger L. Each step discards one element for good → O(n).
