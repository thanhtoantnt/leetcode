# 252 — Meeting Rooms

## Problem

Given meeting intervals, can one person attend them all (no overlaps)?

**Example:** `[[0,30],[5,10],[15,20]]` → `false`; `[[7,10],[2,3]]` → `true`

## Walkthrough

Sort by start; then a single question per adjacent pair — does the next meeting begin before the previous one ends? Any overlap anywhere kills attendance.

**[1] the clashing schedule, sorted**
```text
starts: 0  5  15
ends:   30 10 20
[0,30] vs [5,10]: 5 < 30 ✗ overlap → False
```

**[2] the workable schedule**
```text
starts: 2  7
ends:   3  10
[2,3] then [7,10]: 7 ≥ 3 ✓ → True
```

**[3] touching is fine**
```text
[2,3] and [3,5]: start 3 ≥ end 3 ✓ back-to-back is allowed
```

Why it works: after sorting by start, any conflict must involve **adjacent** meetings — if meeting k overlaps a later one, it also overlaps its immediate neighbor (starts are ordered), so the adjacent-pair scan is exhaustive. O(n log n). The warm-up for 0253 (minimum rooms, this folder), which counts exactly these overlaps instead of merely detecting one.
