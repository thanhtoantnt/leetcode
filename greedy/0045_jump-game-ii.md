# 45 — Jump Game II

## Problem

Each `nums[i]` is the maximum jump length from index `i`. You start at index 0 and always reach the last index. Return the **minimum number of jumps**.

**Example:** `nums = [2,3,1,1,4]` → `2` (jump 0→1, then 1→4)

## Walkthrough

Think BFS on indices: each jump's reachable range is one BFS layer. Slide a window `[L, R]` across the array — everything in the window is one jump away — and extend to the furthest index reachable from that layer.

`nums = [2, 3, 1, 1, 4]`

**[1] layer 0: just the start**
```text
[2, 3, 1, 1, 4]
 L
res=0 window=[0,0]  from i=0 we reach up to 0+2=2
```
Furthest reachable from the current layer = 2 → the next layer is indices `[1, 2]`, `res = 1`.

**[2] layer 1: indices 1–2**
```text
[2, 3, 1, 1, 4]
    L  R
res=1 window=[1,2]  reach = max(1+3, 2+1) = 4
```
Best reach from this layer is index 4 → next layer `[3, 4]`, `res = 2`.

**[3] layer 2 touches the last index**
```text
[2, 3, 1, 1, 4]
             L   R
res=2 window=[3,4]  R reached n-1 → done, return 2
```

Why it works: the window `[L, R]` is exactly the set of indices reachable in `res` jumps (BFS level), and `furthest` is the next level's boundary. Each index is visited once → O(n), no inner double loop (compare the O(n²) DP also in the solution file).
