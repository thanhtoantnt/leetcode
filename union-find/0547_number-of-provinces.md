# 547 — Number of Provinces

## Problem

`n` cities, matrix `isConnected[i][j] = 1` means `i` and `j` are directly connected. A province is a group of directly or indirectly connected cities. Count provinces.

**Example:** `isConnected = [[1,1,0],[1,1,0],[0,0,1]]` → `2` (cities 0+1 form one province, city 2 alone)

## Walkthrough

Union-Find. `parent[i]` names each city's component root; start with `n` singleton components. Every edge `(u,v)` that joins two different roots merges them and decrements the count.

**[1] init — every city its own root**
```text
parent: 0 1 2
provinces=3  scan the matrix for edges
```

**[2] edge (0,1) = 1 — union**
```text
parent: 0 1 2
        u v
provinces=3→2  find(1)=1 ≠ find(0)=0 → parent[1]=0
```

**[3] after union(0,1)**
```text
parent: 0 0 2
provinces=2  0 and 1 now share the root 0
```

**[4] edge (0,2) = 0, (1,2) = 0 — nothing to do**
```text
parent: 0 0 2
provinces=2  no more edges; 2 is still its own root
```

**[5] done — count surviving roots**
```text
parent: 0 0 2
provinces=2  roots: 0 and 2 → return 2
```

Why it works: each successful union shrinks the component count by exactly one, so the answer is `n − (number of merges)`. With path compression + union by rank, `find` is nearly O(1) amortized (inverse-Ackermann, CLRS Ch. 21). Same machinery as Kruskal's MST (Ch. 23).
