# 110 — Balanced Binary Tree

## Problem

Is the tree height-balanced — at every node, subtree heights differ by at most 1?

**Example:** `[3,9,20,null,null,15,7]` → `true`; `[1,2,2,3,3,null,null,4,4]` → `false`

## Walkthrough

Post-order DFS that returns height — or a **−1 sentinel** the moment any subtree is unbalanced, short-circuiting everything above it. Each node's height is computed exactly once.

**[1] the balanced tree**
```text
3
├─L 9        height 1
└─R 20
   ├─L 15    height 2 for node 20 (children height 1)
   └─R 7
|1 − 2| ≤ 1 ✓ at the root → True
```

**[2] the unbalanced tree — violation at node 2 (left)**
```text
1
├─L 2
│  ├─L 3
│  │  ├─L 4
│  │  └─R 4
│  └─R 3
└─R 2
node 3: children heights 1,1 ✓ its height = 2
```

**[3] the sentinel fires at node 2**
```text
node 2's children: left height 3, right height 1 → |3−1| = 2 > 1 ✗
return −1 upward — no further comparisons anywhere
```

**[4] root sees −1**
```text
−1 != a height → return False ✓
```

**[5] why not check heights top-down**
```text
calling height() at every node re-descends subtrees — O(n²) on a
chain; the post-order sentinel visits each node once — O(n)
```

Why it works: balance is a predicate over (left height, right height) at every node — post-order computes both before the visit, and the sentinel turns "false anywhere" into an early exit, the standard trick for AND-over-all-nodes tree recursions. O(n) time, O(h) space.
