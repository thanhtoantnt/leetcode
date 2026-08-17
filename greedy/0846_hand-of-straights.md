# 846 — Hand of Straights

## Problem

Split the multiset of card values into groups of exactly `groupSize` **consecutive** values. Possible?

**Example:** `hand = [1,2,3,6,2,3,4,7,8]`, `groupSize = 3` → `true` (`1,2,3` + `2,3,4` + `6,7,8`)

## Walkthrough

Greedy from the smallest: any run containing the minimum card **must start there** — so peel `count[min]` runs starting at min, checking all `groupSize` consecutive values have enough copies. Sorted order guarantees runs are extracted bottom-up without conflicts.

**[1] counts: 1¹ 2² 3² 4¹ 6¹ 7¹ 8¹**
```text
min = 1, need = 1 run
```

**[2] peel run 1-2-3**
```text
1:1✓ 2:2✓→1 3:2✓→1   counts now 2¹ 3¹ 4¹ 6¹ 7¹ 8¹
```

**[3] next min = 2, need = 1**
```text
run 2-3-4 ✓ → counts 6¹ 7¹ 8¹
```

**[4] final runs**
```text
min = 6 → run 6-7-8 ✓  → True
```

**[5] the failure shape**
```text
[1,2,3,4,5], k=4: min 1 needs 2,3,4 ✓; then min 5 needs 6,7,8 ✗ → False
— the remainder is the wrong shape
```

Why it works: the smallest remaining card has only one possible role — the *start* of its run (nothing smaller exists to precede it), so the greedy choice is forced, not heuristic; subtracting `need` copies per run consumes cards exactly once. Sorting + counting gives O(n log n); a heap of (value, count) peels the same runs lazily (0703-style, queue/). The interval-scheduling cousin: 1296 (divide array in sets of k consecutive) is this problem verbatim.
