# 199 — Binary Tree Right Side View

## Problem

The values you'd see standing to the right of the tree: the last node of every level.

**Example:** `[1,2,3,null,5,null,4]` → `[1,3,4]`

## Walkthrough

Level-order walk (problem 102's queue snapshot); at each level, record the **last** dequeued node — the rightmost by the queue's left-to-right order.

**[1] level 0**
```text
1  ✓
├─L 2
└─R 3
   ├─R? no — 2 has right child 5, 3 has right child 4
out=[1]  last of level = root
```

**[2] level 1: nodes 2, 3 — rightmost is 3**
```text
1  ✓
├─L 2  ✓
└─R 3  ✓ last
out=[1,3]
```

**[3] level 2: 5 (under 2), 4 (under 3)**
```text
1  ✓
├─L 2 ✓
│  └─R 5
└─R 3 ✓
   └─R 4  last
out=[1,3,4]
```

**[4] done**
```text
return [1,3,4] ✓
```

Why it works: the right-side view is exactly one node per depth — the rightmost — and BFS's level snapshots isolate precisely one node per level, in left-to-right order, so the last of each is the visible one. O(n). The DFS variant (`node.right` first, record the first node visited at each new depth) is the same answer from the other direction.
