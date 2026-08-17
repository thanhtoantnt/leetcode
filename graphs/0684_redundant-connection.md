# 684 — Redundant Connection

## Problem

A tree plus one extra edge — an edge per node count. Find the extra edge; if several candidates fit, return the **last** one in input order.

**Example:** `edges = [[1,2],[1,3],[2,3]]` → `[2,3]`

## Walkthrough

Union-Find, one pass: process edges in order; the first edge whose endpoints are **already in the same set** closes a cycle — that's the redundant one.

**[1] n=3 nodes, parents singleton**
```text
parent: 1 2 3
edges in order: (1,2) (1,3) (2,3)
```

**[2] edge (1,2) — union**
```text
parent: 1 1 3
roots differ → merge → components {1,2} {3}
```

**[3] edge (1,3) — union**
```text
parent: 1 1 1
roots differ → merge → one component {1,2,3}
```

**[4] edge (2,3) — same root!**
```text
parent: 1 1 1
find(2)=1 = find(3)=1 → cycle edge → return [2,3]
```

**[5] why "last in order" is automatic**
```text
edges = [[1,2],[2,3],[3,1]]
each union merges fresh roots until (3,1) meets same-set → returned —
the *first* edge that closes a cycle in input order is definitionally
the last one that can be removed while leaving a spanning tree
```

Why it works: a tree on n nodes has n−1 edges and no cycles; adding one edge creates exactly one cycle. An edge's endpoints being pre-connected means that edge lies on a cycle — removing it restores the tree (still connected: the union already joined those nodes another way). Path compression + union by rank make this near-linear (inverse-Ackermann); it's the cycle test from Kruskal's algorithm (CLRS Ch. 23.2) applied verbatim.
