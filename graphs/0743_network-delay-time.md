# 743 — Network Delay Time

## Problem

A signal leaves node `k` along directed edges with travel times. How long until **every** node has received it? (−1 if some node is unreachable.)

**Example:** `times = [[2,1,1],[2,3,1],[3,4,1]]`, `n = 4`, `k = 2` → `2`

## Walkthrough

Single-source shortest paths with **Dijkstra**: a min-heap of (distance, node), seeded with (0, k). Pop the closest node — with nonnegative weights that distance is final — and relax each outgoing edge. The answer is the max finalized distance; if fewer than n nodes finalized, someone is unreachable.

**[1] adjacency: 2→(1,1),(3,1); 3→(4,1)**
```text
heap=[(0,2)]
pop (0,2): dist[2]=0  push (1,1) (1,3)
```

**[2] first min-dist pop**
```text
heap=[(1,1),(1,3)]
pop (1,1): dist[1]=1  no out-edges
```

**[3] node 3 finalizes**
```text
heap=[(1,3)]
pop (1,3): dist[3]=1  push (2,4)
```

**[4] node 4 finalizes**
```text
heap=[(2,4)]
pop (2,4): dist[4]=2  all 4 reached
```

**[5] answer**
```text
dist = {2:0, 1:1, 3:1, 4:2} → max 2 ✓
```

Why it works: with nonnegative weights, distances only grow along paths — when the heap pops the smallest tentative distance, no unprocessed path can beat it (everything still in the heap is ≥, and extensions only add). So each node finalizes exactly once: O(E log V). This is CLRS Ch. 24.3, the weighted twin of BFS (1091/0542's first-arrival rule); Prim (1584, this folder) is the same loop minimizing edge weight instead of path length.
