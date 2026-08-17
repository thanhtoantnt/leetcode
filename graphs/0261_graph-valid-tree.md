# 261 — Graph Valid Tree

## Problem

Do the edges form one tree over all `n` nodes? Tree ⟺ connected + exactly n−1 edges + acyclic — any two imply the third.

**Example:** `n = 5`, `edges = [[0,1],[0,2],[0,3],[1,4]]` → `true`

## Walkthrough

Check the cheap condition first: a tree needs exactly n−1 edges. Then one DFS/BFS from node 0 must reach all n nodes — with n−1 edges, full connectivity implies the acyclicity for free.

**[1] edge count passes**
```text
0 ─ 1 ─ 4
│
2
│
3
edges=4 = n−1 ✓  proceed to connectivity
```

**[2] BFS from 0 — wave 1**
```text
0 ✓  1, 2, 3
visited={0,1,2,3}  wave: 0's neighbors enqueue
```

**[3] wave 2 reaches 4**
```text
0 ✓  1 ✓  4
│
2 ✓
│
3 ✓
visited={0,1,2,3,4}  5 = n → connected ✓
```

**[4] verdict**
```text
return True  n−1 edges + all reachable = tree
```

**[5] failure modes, both cheap to catch**
```text
[[0,1],[2,3]] with n=4:  edges=2 < 3 → False immediately
[[0,1],[1,2],[2,0]] n=3:  edges=3 > 2 → False (cycle)
[[0,1],[1,2],[0,2],[3,4]] n=5:  edges=4 ✓ but BFS from 0 reaches {0,1,2} ≠ 5 → False
```

Why it works: a connected graph on n nodes needs ≥ n−1 edges, and acyclicity caps it at ≤ n−1 — trees sit exactly at the boundary. So with n−1 edges confirmed, connectivity alone pins down the tree (and symmetrically, connectivity + acyclicity pins n−1 edges — CLRS Appendix B's characterizations). Union-Find (merge per edge, watch for a same-set union = cycle) is the equally valid alternative: n−1 successful unions with no re-merge = tree.
