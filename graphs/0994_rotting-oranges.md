# 994 — Rotting Oranges

## Problem

A grid has fresh oranges (`1`), rotten oranges (`2`), and empty cells (`0`). Every minute, oranges adjacent (4-directional) to a rotten one rot. Return the minutes until no fresh orange remains, or `-1` if some can never rot.

**Example:**
```text
2 1 1        2 2 2        2 2 2        2 2 2        2 2 2
1 1 0   →    2 1 0   →    2 2 0   →    2 2 0   →    2 2 0
0 1 1        0 1 1        0 1 1        0 2 1        0 2 2
```
→ `4`

## Walkthrough

**Multi-source BFS**: all rotten oranges enter the queue at minute 0 — the infection spreads one ring per level, like the 01-Matrix walk (problem 542, same folder pattern).

**[1] minute 0 — seeds in the queue**
```text
2 1 1
1 1 0
0 1 1
minutes=0 fresh=6  queue: (0,0)
```

**[2] minute 1 — first ring**
```text
2 2 1
2 1 0
0 1 1
minutes=1 fresh=4  (0,1) and (1,0) rot — neighbors of the seed
```

**[3] minute 2 — diagonal spread**
```text
2 2 2
2 2 0
0 1 1
minutes=2 fresh=2  (0,2) and (1,1) rot
```

**[4] minute 3 — down the left column**
```text
2 2 2
2 2 0
0 2 1
minutes=3 fresh=1  (2,1) rots
```

**[5] minute 4 — last one**
```text
2 2 2
2 2 0
0 2 2
minutes=4 fresh=0  queue drains → return 4
```

Why multi-source: starting all rotten cells at distance 0 makes BFS levels = elapsed minutes — each level of the queue is exactly one minute's new infections. If the queue empties while fresh oranges remain (an isolated one), return `-1`. O(m·n), every cell enqueued once.
