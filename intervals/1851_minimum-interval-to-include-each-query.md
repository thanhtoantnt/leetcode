# 1851 — Minimum Interval to Include Each Query

## Problem

For each query point `q`, find the length of the **shortest** interval `[l,r]` with `l ≤ q ≤ r`, or −1.

**Example:** `intervals = [[1,4],[2,4],[3,6],[4,4]]`, `queries = [2,3,4,5]` → `[3,3,1,4]`

## Walkthrough

Sort intervals by start and queries ascending; sweep left to right. For query `q`: **admit** every interval that has started (push length, end to a heap), **evict** every interval already ended (`end < q`), then the heap top is the shortest live interval — dedup queries first so each is answered once.

**[1] q=2 — admit the starters ≤ 2**
```text
live: (4,[1,4]) (3,[2,4])   → shortest 3 ✓
```

**[2] q=3 — admit [3,6]**
```text
live: 4, 3, 4 → top 3 ✓
```

**[3] q=4 — admit [4,4]**
```text
live: 4, 3, 4, 1 → top 1 ✓
```

**[4] q=5 — evict the ended**
```text
[4,4] ends at 4 < 5 → pop; [1,4],[2,4] also dead → pop
live: (4,[3,6]) → top 4 ✓
```

**[5] all queries answered**
```text
[3, 3, 1, 4] ✓  each interval enters/leaves the heap once
```

Why it works: processing queries in sorted order makes the admitted set monotone (start ≤ q grows) and the eviction check total (end < q) — so the heap holds exactly the intervals containing q, min-heap on length answering in O(1). O((n+q) log(n+q)); offline sorting is what makes the sweep valid (online would need an interval tree, CLRS Ch. 14.3).
