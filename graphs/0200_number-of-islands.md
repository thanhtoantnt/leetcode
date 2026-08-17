# 200 — Number of Islands

## Problem

Given a 2D grid of `'1'`s (land) and `'0'`s (water), count the islands. An island is land connected horizontally or vertically.

**Example:**
```text
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```
→ `3`

## Walkthrough

Scan left-to-right, top-to-bottom. Each unvisited `'1'` starts a new island — flood-fill (sink) its whole connected component so it's never counted again.

**[1] scan finds land at (0,0) — island 1**
```text
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
islands=1  flood-fill all reachable land from (0,0), sinking it to 0
```

**[2] island 1 sunk**
```text
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 1 1
islands=1  the 2×2 block is consumed — no cell of it can start a new count
```

**[3] scan finds land at (2,2) — island 2**
```text
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 1 1
islands=2  single cell, no land neighbors → sink it
```

**[4] scan finds land at (3,3) — island 3**
```text
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
islands=3  last component: (3,3)–(3,4)
```

**[5] done**
```text
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
islands=3  return 3
```

Why it works: every land cell is visited exactly once — either by the scan (starts an island) or by the flood fill (joins one). Sinking instead of a visited set means O(1) extra state. O(m·n) time.
