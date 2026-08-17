# 230 — Kth Smallest Element in a BST

## Problem

Return the k-th smallest value in a BST (1-indexed).

**Example:** tree `[5,3,6,2,4,null,null,1]`, `k = 3` → `3`

## Walkthrough

A BST's **inorder walk is sorted** — so it's "k-th element of a sorted list", generated lazily. Walk inorder, counting; the k-th visited node is the answer, no full traversal needed.

**[1] inorder starts at the leftmost**
```text
5
├─L 3
│  ├─L 2
│  │  └─L 1
│  └─R 4
└─R 6
first visit: 1 (the minimum) — count=1
```

**[2] unwind: 2, then 3**
```text
visit 2 → count=2
visit 3 → count=3 = k ✓ return 3
```

**[3] (walk would continue, but stops)**
```text
remaining: 4, 5, 6 — never visited, saving work on big trees
```

**[4] the iterative form — explicit stack**
```text
stack: push 5, 3, 2, 1 → pop 1 (count 1) → pop 2 (2) → pop 3 (3) ✓
early exit the moment count hits k
```

Why it works: inorder = left, self, right and the BST invariant make the visit sequence ascending — the k-th visit is definitionally the k-th smallest. Lazy early-exit makes it O(h + k) instead of O(n); if the tree were augmented with subtree counts (order-statistic trees, CLRS Ch. 14), each query would be O(h) with no walk at all.
