# 200-family — Number of Islands' siblings: 695 — Max Area of Island

## Problem

Same grid as problem 200, but return the **area** of the largest island instead of the count.

**Example:**
```text
1 1 0 0 0
1 1 0 0 0
0 0 0 1 1
0 0 0 1 1
```
→ `4`

## Walkthrough

Identical scan-and-flood loop; the only change is what the flood returns — the **size** of the component it sinks, taken as a running max instead of incrementing a counter.

**[1] scan hits (0,0) — flood fill it**
```text
1 1 0 0 0
1 1 0 0 0
0 0 0 1 1
0 0 0 1 1
area=4 best=4  the 2×2 block sinks; DFS returns its size
```

**[2] block consumed**
```text
0 0 0 0 0
0 0 0 0 0
0 0 0 1 1
0 0 0 1 1
best=4  scan continues from where it stopped
```

**[3] second island — same size**
```text
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
area=4 best=4  second 2×2 sinks; max stays 4
```

**[4] the counter difference, in one line**
```text
counting: islands += 1 per flood   (problem 200)
area:     best = max(best, flood)  (this problem)
```

Why it works: the flood fill visits each cell of its component exactly once, so counting visits *is* measuring area — the same traversal answers count, area, perimeter (1295-adjacent 463), or shape questions depending only on what you accumulate. O(m·n).
