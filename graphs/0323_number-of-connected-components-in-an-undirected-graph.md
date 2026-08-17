# 323 — Number of Connected Components in an Undirected Graph

## Problem

Count connected components of an undirected graph on `n` labeled nodes.

**Example:** `n = 5`, `edges = [[0,1],[1,2],[3,4]]` → `2`

## Walkthrough

Two textbook solutions — pick either. **DFS sweep**: every scan-visit of a white node discovers exactly one new component. **Union-Find**: start at n components; each edge joining two different roots decrements the count (the 0547 flipbook's exact mechanics).

**[1] the edges, as adjacency**
```text
0 ─ 1 ─ 2        3 ─ 4
components=2 (by eye)  now prove it by algorithm
```

**[2] DFS version — launch from 0**
```text
0 ✓ 1 ✓ 2 ✓   sweep: unvisited 0 → flood {0,1,2} → count=1
```

**[3] scan continues — node 3 is white**
```text
0 ✓ 1 ✓ 2 ✓   3 ✓ 4 ✓   second flood {3,4} → count=2
```

**[4] Union-Find version — parents start singleton**
```text
parent: 0 1 2 3 4
count=5  process edges
```

**[5] unions fire**
```text
edge (0,1): roots differ → union → count=4
edge (1,2): roots differ → union → count=3
edge (3,4): roots differ → union → count=2
return 2
```

Why it works: DFS floods cover components exactly (reachability = same component, CLRS Ch. 22.3), each launched from an unvisited node — one launch per component. Union-Find counts merges for the same reason (CLRS Ch. 21; this is also Kruskal's cycle test). Both O(V+E). Union-Find wins when edges stream in incrementally; DFS wins on dense static graphs.
