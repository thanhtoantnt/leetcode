# 435 — Non-overlapping Intervals

## Problem

Remove the **minimum** number of intervals so the rest don't overlap. (Touching endpoints don't overlap.)

**Example:** `[[1,2],[2,3],[3,4],[1,3]]` → `1` (remove `[1,3]`)

## Walkthrough

Flip it: keep the **maximum** non-overlapping set — the classic activity-selection greedy, sorted by **earliest end**. Scan sorted intervals; whenever one starts before the last kept end, it's removed (dropping the later-ending of two clashing intervals always keeps at least as many options open).

**[1] sorted by end: [1,2] [2,3] [1,3] [3,4]**
```text
end:   2  3  3  4
keep [1,2]  lastEnd=2
```

**[2] [2,3] starts at the last end — compatible**
```text
end:   2  3  3  4
    ✓  ✓
keep, lastEnd=3  touching at 2/3 is allowed
```

**[3] [1,3] starts before 3 — clash**
```text
end:   2  3  3  4
    ✓  ✓  ✗
1 < 3 → remove [1,3], removed=1  (keep the earlier-ending one — [2,3] frees the room sooner)
```

**[4] [3,4] fits**
```text
end:   2  3  3  4
    ✓  ✓  ✗  ✓
3 ≥ 3 → keep, lastEnd=4
```

**[5] done**
```text
removed=1  return 1 — the kept set {[1,2],[2,3],[3,4]} is maximum
```

Why it works: among clashing intervals, dropping the one that **ends later** can never cost more — any interval compatible with the later ender is also compatible with the earlier one. Sorting by end and greedily keeping is the activity-selection algorithm (CLRS Ch. 16.1), proven optimal by the exchange argument: the earliest-finishing interval belongs to *some* maximum set. O(n log n). Sibling flipbook: 56 (merging, `intervals/`) and 452/646-style scheduling.
