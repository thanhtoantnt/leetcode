# 63 — Unique Paths II

## Problem

Unique Paths (problem 62) with obstacles: cells marked `1` are blocked; count right/down paths from corner to corner avoiding them.

**Example:**
```text
0 0 0
0 1 0
0 0 0
```
→ `2` (`RRDD` and `DDRR` — the only two ways around the center block)

## Walkthrough

Same addition recurrence as 62 — `paths[r][c] = up + left` — with one amendment: a blocked cell is hard-forced to **0**, and a 0 upstream poisons every cell that would route through it.

**[1] seed row 0 and column 0**
```text
1 1 1
1 . .
1 . .
row 0 and col 0: exactly one straight-line way each, no obstacles yet
```

**[2] the blocked cell becomes 0**
```text
1 1 1
1 0 .
1 . .
(1,1) is the obstacle → its count is 0; paths may not enter
```

**[3] its right neighbor routes around**
```text
1 1 1
1 0 1
1 . .
(1,2) = up(1) + left(0) = 1  the only route: along row 0 then down
```

**[4] below the block, same story**
```text
1 1 1
1 0 1
1 1 .
(2,1) = up(0) + left(1) = 1  the only route: down col 0 then right
```

**[5] corner merges the two surviving routes**
```text
1 1 1
1 0 1
1 1 2
(2,2) = up(1) + left(1) = 2  return 2
```

Why it works: obstacles break the recurrence locally — 0 in, 0 out — and everything else flows as in 62, so the table computes exactly the paths that never step on a blocked cell. Edge cases: an obstacle **at the start or the goal** makes the answer 0 (the seed 1 never gets written / never reaches the corner). O(m·n), with a rolling 1-D row for O(n) space.
