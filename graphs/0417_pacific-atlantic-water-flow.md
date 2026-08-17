# 417 — Pacific Atlantic Water Flow

## Problem

Rain falls on an island grid; water flows to a **strictly smaller-or-equal** neighbor. Which cells can reach both the Pacific (top/left edges) and the Atlantic (bottom/right edges)?

**Example:**
```text
1 2 2 3 5
3 2 3 4 4
2 4 5 3 1
6 7 1 4 5
5 1 1 2 4
```
→ the 7 highlighted cells (corners + the ridge)

## Walkthrough

Invert the flow: instead of asking "where does this cell drain", start **from each ocean** and climb — a cell drains to the Pacific iff the Pacific can climb *up* to it. Two reachability floods (pacific, atlantic), then intersect.

**[1] seeds: pacific touches top row + left col**
```text
P P P P P
P . . . .
P . . . .
P . . . .
P . . . .
water climbs from the ocean inward (height must not decrease going up)
```

**[2] pacific flood climbs**
```text
P P P P P
P P P P P
P P P . .
P P . . .
P . . . .
from (1,3)=4 climb to (2,3)=3? 3 ≤ 4 → no. Climb rule: neighbor ≥ current
```

**[3] atlantic flood from bottom/right edges**
```text
. . . . A
. . . A A
. . . . A
. A A A A
A A A A A
```

**[4] intersect the two reachability sets**
```text
P P P P P
P P P P P   ∩   atlantic set
P P P . .
P P . . .
P . . . .
→ cells reachable both ways: the ridge cells and corners
```

**[5] answer**
```text
(0,0) (0,4) (1,3) (2,2)? (3,0) (3,1)? (4,0) (4,4)…
return [[0,0],[0,4],[1,3],[3,1],[4,0],[3,0],[4,4]] per intersection
```

Why it works: "cell c drains to ocean O" ⟺ "O's edge cells can reach c by non-decreasing climbs" — reversing every edge turns flow into reachability, and multi-source BFS/DFS from the ocean edges computes it in one pass each. Intersection = both-ocean cells. O(m·n), same skeleton as 286 and 0542: seed all borders, flood once.
