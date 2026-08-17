# 130 — Surrounded Regions

## Problem

Flip every `'O'` to `'X'` unless it's connected to the **border** — border-touching regions (and everything linked to them) survive.

**Example:**
```text
X X X X      X X X X
X O O X  →   X X X X
X X O X  →   X X X X
X O X X      X O X X
```

## Walkthrough

Invert the question: instead of finding doomed regions, find **safe** ones — any `'O'` reachable from a border `'O'`. Flood-fill from all border `'O'`s, mark them safe (temporary `'T'`), then sweep: `T → O` (kept), everything else `O → X` (captured).

**[1] the board — two doomed regions, one safe chain**
```text
X X X X
X O O X
X X O X
X O X X
border O at (3,1) is the anchor of the safe region
```

**[2] flood-fill from border O's, mark T**
```text
X X X X
X O O X
X X O X
X T X X
DFS/BFS from (3,1): (2,1)? it's X → nothing else spreads; only the anchor marks
```

Wait — (3,1) has no O neighbors here, so the safe region is just itself. The center chain (1,1)→(1,2)→(2,2) never touches a border and is doomed:

**[3] the sweep — T survives, isolated O's flip**
```text
X X X X
X X X X
X X X X
X T X X
unmarked O's captured → X;  T → O restores
```

**[4] final board**
```text
X X X X
X X X X
X X X X
X O X X
return  the border-linked O lives, the enclosed blob dies
```

Why it works: doom is exactly "no border connection" — reaching any border cell via 4-directional O-links is a certificate of escape. Border-rooted flood fill marks precisely those certificates in one pass over the seeds. O(m·n): every cell is visited a constant number of times.
