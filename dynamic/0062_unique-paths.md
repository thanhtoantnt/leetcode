# 62 — Unique Paths

## Problem

A robot starts at the top-left of an `m × n` grid and wants the bottom-right corner. It only moves **right or down**. Count the distinct paths.

**Example:** `m = 3, n = 7` → `28`

## Walkthrough

`paths[r][c]` = ways to reach cell (r,c) = ways from above + ways from the left. First row and column: exactly 1 way (straight line). Fill the rest; the answer lands in the corner. (`.` = not computed yet.)

**[1] seed the first row — one way to slide right**
```text
1 1 1 1 1 1 1
. . . . . . .
. . . . . . .
row 0: only "keep moving right" → all 1s
```

**[2] seed the first column — one way to drop down**
```text
1 1 1 1 1 1 1
1 . . . . . .
1 . . . . . .
col 0: only "keep moving down" → all 1s
```

**[3] fill row 1**
```text
1 1 1 1 1 1 1
1 2 3 4 5 6 7
. . . . . . .
row 1: each cell = up (1) + left (running sum) → 2,3,4…
```

**[4] fill row 2**
```text
1 1 1 1 1 1 1
1 2 3 4 5 6 7
1 3 6 10 15 21 28
row 2: e.g. 21 = up(6) + left(15) → corner = 28
```

**[5] answer in the corner**
```text
1 1 1 1 1 1 1
1 2 3 4 5 6 7
1 3 6 10 15 21 28
paths[2][6] = 28  return 28
```

Why it works: the last move into (r,c) is either from (r−1,c) or (r,c−1) — those path sets are disjoint and exhaustive, so they add. O(m·n) table, or closed form C(m+n−2, m−1) — choose which of the m+n−2 moves are "down" — computable in O(min(m,n)).
