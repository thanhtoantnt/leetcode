# 778 — Swim in Rising Water

## Problem

An n×n elevation grid; you can move between adjacent cells only when the water level (time) reaches both cells' elevations. Minimum time to reach the bottom-right corner — i.e., minimize the **maximum** elevation along a path.

**Example:** `grid = [[0,2],[1,3]]` → `3` (path 0→1→3: max elevation 3)

## Walkthrough

Dijkstra with the sum replaced by a **max**: the "cost" of a path is its highest cell. A min-heap pops the cell reachable at the lowest time so far; neighbors enter with cost `max(time, neighbor elevation)`.

**[1] start at (0,0), time = 0**
```text
0 2
1 3
heap=[(0,0,0)]  pop it: neighbors (0,1) at max(0,2)=2, (1,0) at max(0,1)=1
```

**[2] pop (1, (1,0))**
```text
0 2
1 3
time=1  push (1,1) at max(1,3)=3
```

**[3] pop (2, (0,1))**
```text
0 2
1 3
time=2  (1,1) already has a better entry (3)? max(2,3)=3 — equal, skip or push
```

**[4] pop (3, (1,1)) — corner**
```text
0 2
1 3
time=3 = the destination → return 3 ✓ every route needs a 3
```

Why it works: nonnegative elevations make the max-path cost monotone along paths — popping the smallest heap time finalizes that cell's minimal-max exactly as Dijkstra finalizes distance (CLRS Ch. 24.3 with ⊕ = max, still a valid "shortest path" semiring). Alternatives: binary search the answer + BFS reachability (0875-style on the answer, `binary_search/`), or union-find joining cells in elevation order (0x-swim variant). O(n² log n).
