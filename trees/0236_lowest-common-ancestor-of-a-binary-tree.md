# 236 — Lowest Common Ancestor of a Binary Tree

## Problem

LCA of two nodes in a **general** binary tree (no ordering). A node may be its own ancestor.

**Example:** tree below, `p = 4`, `q = 5`? — canonical: `p = 5`, `q = 4` → LCA `5` (5 is an ancestor of 4 and of itself); `p = 5`, `q = 1` → LCA `3`.

## Walkthrough

Post-order search for both nodes: each call returns "the node found in this subtree" (p, q, an LCA already found, or null). When **both sides return non-null**, the current node is where they split — the LCA.

**[1] the tree, targets 5 and 4**
```text
3
├─L 5
│  ├─L 6
│  └─R 2
│     ├─L 7
│     └─R 4
└─R 1
   ├─L 0
   └─R 8
```

**[2] search the left subtree**
```text
under 5: finds 6? no; finds 2's children 7 and 4 → 4 ✓ (right side of 2)
5's subtree returns 5 itself (root of the subtree is p) — 4 rides along inside
```

**[3] search the right subtree**
```text
under 1: neither 5 nor 4 → returns null
```

**[4] at the root: both sides reported**
```text
left = 5 (found p — 4 was deeper inside it), right = null
one-sided → return left → the answer 5 ✓ (4 lives inside 5's subtree)
```

**[5] the split case: p = 5, q = 1**
```text
left = 5, right = 1 — both non-null at the root → LCA = 3 ✓
```

Why it works: the LCA is the unique node with both targets in its subtree *and* neither child containing both — the post-order flow bubbles each target up, and the first junction where the two bubbles meet is exactly that node (self-ancestry handled by the `root is p` early return). O(n) time, O(h) space — compare 0235's O(h) walk (BST ordering, this folder).
