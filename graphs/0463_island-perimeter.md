# 463 — Island Perimeter

## Problem

Perimeter of the (single, no-holes) island in a binary grid.

**Example:**
```text
0 1 0 0
1 1 1 0
0 1 0 0
1 1 0 0
```
→ `16`

## Walkthrough

Each land cell starts with 4 exposed sides; every pair of adjacent land cells **hides 2 edges total** (one from each). Count cells, subtract 2 per neighbor-pair — checking only up and left avoids double-counting pairs.

**[1] count the land: 7 cells → 28 naive sides**
```text
0 1 0 0
1 1 1 0
0 1 0 0
1 1 0 0
```

**[2] shared edges: count adjacent pairs**
```text
pairs: (0,1)-(1,1), (1,0)-(1,1), (1,1)-(1,2), (1,1)-(2,1),
(3,0)-(3,1), (2,1)-(3,1)? no — (2,1)-(3,1) yes … total 6 pairs
```

**[3] subtract**
```text
28 − 6·2 = 16 ✓
```

**[4] why up-left only**
```text
each unordered pair is seen exactly once when the later cell (by row
order) checks its up and left neighbors — right/down would recount
```

**[5] the DFS alternative**
```text
walk the island (0200's flood): +4 per cell, −2 per land neighbor —
same arithmetic, or +1 per water/out-of-bounds edge seen from land
```

Why it works: perimeter is the number of land–non-land boundaries — `4·cells − 2·sharedEdges` counts them by inclusion-exclusion over cells and pairs, exact for any polyomino (holes would still work: interior lake edges count). O(m·n), no traversal needed — the arithmetic cousin of 0200/0695's flood fills (this folder).
