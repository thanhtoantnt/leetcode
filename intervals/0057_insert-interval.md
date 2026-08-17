# 57 — Insert Interval

## Problem

Given **non-overlapping** intervals sorted by start, insert a new interval and merge what overlaps.

**Example:** `intervals = [[1,3],[6,9]]`, `new = [2,5]` → `[[1,5],[6,9]]`

## Walkthrough

Three phases over the sorted list: **before** (ends before the new one starts — copy), **overlap** (overlaps the new one — absorb by min/max), **after** (starts after the new one ends — copy). One linear pass, no re-sorting.

**[1] the incoming interval [2,5]**
```text
starts: 1 6
ends:   3 9
new=[2,5]  phase 1: does [1,3] end before 2?
```

**[2] [1,3] overlaps — merge**
```text
starts: 1 6
ends:   3 9
new=[1,5]  3 ≥ 2 → overlap: new = [min(1,2), max(3,5)] = [1,5]
```

**[3] [6,9] starts after 5 — phase 3**
```text
starts: 1 6
ends:   3 9
out=[[1,5]]  6 > 5 → no overlap: append new, then the rest
```

**[4] result**
```text
out=[[1,5],[6,9]]  done
```

**[5] the swallow case: new covers everything**
```text
intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]], new=[4,8]
every interval touching [4,8] is absorbed → out=[[1,2],[4,8],[12,16]]
```

Why it works: sorted order guarantees the three phases appear in sequence, so a single scan suffices — phase boundaries are `end < new.start` (safe before) and `start > new.end` (safe after); everything between must merge, and merging is just interval hull min/max. O(n). (Problem 56's flipbook in `intervals/` shows the general unsorted case: sort first, then the same walk.)
