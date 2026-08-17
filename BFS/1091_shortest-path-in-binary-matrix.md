# 1091 — Shortest Path in Binary Matrix

## Problem

In an n×n grid, find the shortest **clear** path from top-left to bottom-right moving 8-directionally (cells with `1` are blocked). Return its length (cell count), or `-1`.

**Example:**
```text
0 0 0
1 1 0
1 1 0
```
→ `4` (`(0,0)→(0,1)→(1,2)→(2,2)`)

## Walkthrough

Plain BFS — an unweighted grid, so first arrival = shortest path. Each queue level is one extra step of path length; the diagonal move makes distances Chebyshev-ish.

**[1] level 1 — just the corner**
```text
0 0 0
1 1 0
1 1 0
len=1 queue=(0,0)  start counts as one cell
```

**[2] level 2 — east and southeast**
```text
0 0 0
1 1 0
1 1 0
len=2  (0,0)'s clear neighbors: (0,1) and (1,1)? (1,1)=1 blocked → only (0,1)
```

**[3] level 3 — spreading from (0,1)**
```text
0 0 0
1 1 0
1 1 0
len=3  (0,2) and (1,2) enqueue — 8 directions checked, walls ignored
```

**[4] level 4 — corner reached**
```text
0 0 0
1 1 0
1 1 0
len=4  (2,2) dequeued → it's the target → return 4
```

Why it works: BFS explores paths in increasing length, so the first time any cell is dequeued, its distance is final — marking visited **on enqueue** (not dequeue) prevents the same cell entering the queue twice. O(n²) cells, constant work each. This is the single-source unweighted shortest-path property (CLRS Ch. 22.2); the 0542 01-Matrix flipbook in this folder is the multi-source version of the same idea.
