# 286 — Walls and Gates

## Problem

A grid of rooms (`INF`), walls (`-1`), and gates (`0`). Fill each room with the distance to its **nearest** gate.

**Example:**
```text
INF  -1   0  INF        3  -1   0   1
INF INF INF  -1   →     2   2   1  -1
INF  -1 INF  -1         1  -1   2  -1
0    -1 INF INF         0  -1   3   4
```

## Walkthrough

Multi-source BFS from **all gates at once** — the same trick as 0542 (01-Matrix) and 994 (rotting oranges): first arrival = nearest gate. Queue the gates at distance 0, expand ring by ring, write each room's distance on first visit.

**[1] gates seeded**
```text
.  -1  0   .
.  .   .  -1
.  -1  .  -1
0  -1  .  .
queue=(0,2),(3,0)  both gates at distance 0
```

**[2] first ring around each gate**
```text
.  -1  0   1
.  .   1  -1
.  -1  .  -1
0  -1  .  .
(0,3)=1, (1,2)=1, (2,0)=1  neighbors of gates
```

**[3] second ring**
```text
.  -1  0   1
.  .   1  -1
.  -1  2  -1
0  -1  .  .
(2,2)=2; (1,1)=min(1+1)=2
```

**[4] rings meet — the corner races**
```text
3  -1  0   1
2   2   1  -1
1  -1   2  -1
0  -1   3   4
(0,0)=3, (3,2)=3, (3,3)=4  first arrival wins each
```

Why it works: BFS levels = distance-from-nearest-gate because all sources share the clock — level k contains exactly rooms whose closest gate is k steps away. Marking visited on enqueue ensures no room is improved twice. O(m·n); the naive per-room BFS (one flood per room) is O((mn)²).
