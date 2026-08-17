# 104 — Maximum Depth of Binary Tree

## Problem

Height in nodes of the tree (root-only = 1).

**Example:** `[3,9,20,null,null,15,7]` → `3`

## Walkthrough

The archetypal tree recursion: depth = 1 + max(depth of each subtree). Nulls contribute 0.

**[1] root 3**
```text
3
├─L 9
└─R 20
depth(3) = 1 + max(depth 9, depth 20) — recurse both
```

**[2] 9 is a leaf**
```text
depth(9) = 1 + max(0, 0) = 1
```

**[3] 20's subtree**
```text
20
├─L 15
└─R 7
depth(20) = 1 + max(1, 1) = 2
```

**[4] combine at the root**
```text
depth(3) = 1 + max(1, 2) = 3 ✓
```

**[5] the BFS view (iterative twin)**
```text
level 0: 3    level 1: 9, 20    level 2: 15, 7
count levels = 3 — problem 102's level-walk, counted
```

Why it works: a tree's longest root-leaf path must pass through one of the root's subtrees — the max over children plus the root edge is exhaustive and disjoint (the divide-and-conquer template, CLRS Ch. 4). O(n) time — every node visited once — and O(h) recursion space (BFS costs O(w) for the widest level instead).
