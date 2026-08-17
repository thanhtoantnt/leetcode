# 133 — Clone Graph

## Problem

Deep-copy an undirected graph given a starting node (neighbors are mutual). Return the clone's corresponding node.

**Example:** diamond: 1 — 2, 1 — 4, 2 — 3, 3 — 4 → a new diamond, same shape.

## Walkthrough

DFS/BFS with a **visited map `old → new`** — the copy of each node is created *once*, before recursing into neighbors, so cycles terminate. The map doubles as the visited set: "already cloned" ⟺ "already processed".

**[1] start at node 1 — create its clone first**
```text
old→new: {1 → 1′}
1′ has no neighbors yet  neighbors will be wired as they're cloned
```

**[2] recurse into neighbor 2 — clone, wire back**
```text
old→new: {1→1′, 2→2′}
1′.neighbors += [2′]   2′.neighbors += [1′]  undirected: wire both ways
```

**[3] from 2, visit 3**
```text
old→new: {1→1′, 2→2′, 3→3′}
2′ ↔ 3′ wired
```

**[4] from 3, neighbor 4; from 4, back to 1 — already mapped**
```text
old→new: {1→1′, 2→2′, 3→3′, 4→4′}
3′ ↔ 4′ wired;  4′.neighbors += [1′] (no recursion — 1 is in the map)
```

**[5] the cycle closed safely**
```text
old→new: {1→1′, 2→2′, 3→3′, 4→4′}
4′ → 1′ edge exists; 1 was not re-cloned  return 1′
```

Why it works: inserting the clone into the map **before** iterating neighbors breaks infinite regress on cycles — seeing an old node in the map means its clone exists and the edge can be attached immediately, no deeper traversal. Every node and edge is touched once → O(V+E) time and space. This is exactly CLRS Ch. 22.3's DFS with an extra "on first visit, allocate the copy" line.
