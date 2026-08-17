# 1584 — Min Cost to Connect All Points

## Problem

Connect all 2-D points with minimum total edge cost, where cost between two points is **Manhattan distance** `|x₁−x₂| + |y₁−y₂|`. (A minimum spanning tree on the complete distance graph.)

**Example:** `[[3,12],[-2,5],[-4,1]]` → `18` (edges 3↔−2 cost 12, −2↔−4 cost 6)

## Walkthrough

**Prim's algorithm**, visit-flavored: grow one tree from any start. A min-heap holds frontier edges; pop the cheapest, skip it if its endpoint is already in the tree, else absorb the vertex and push its edges to all unvisited vertices.

**[1] start at (3,12) — push edges to both others**
```text
visited={} heap=[(0,S)]
pop (0,S): visit S  push (12,M) (18,L)  where M=(-2,5), L=(-4,1)
```

**[2] cheapest frontier edge wins**
```text
visited={S} heap=[(12,M),(18,L)]
pop (12,M): visit M  push (6,L)  — M to L is cheap
```

**[3] the heap now offers L twice**
```text
visited={S,M} heap=[(6,L),(18,L)]
pop (6,L): visit L  total = 0+12+6 = 18 ✓ all connected
```

**[4] stale edge cleanup**
```text
the older (18,L) pops later and is skipped — visited check
```

**[5] done**
```text
return 18 — the MST uses edges SM and ML
```

Why it works: Prim's cut property (CLRS Ch. 23) — at every step the cheapest edge crossing the visited/unvisited cut belongs to some MST, so committing it greedily is safe. The heap gives O(E log V); with a complete distance graph E = n², computed on the fly. Kruskal (0684's union-find, `graphs/`) is the alternative — sort all n² pairs and union. Same skeleton: 0743 (Dijkstra, this folder) is Prim with distances-from-source instead of edge weights.
