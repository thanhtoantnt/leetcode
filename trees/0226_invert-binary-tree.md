# 226 — Invert Binary Tree

## Problem

Mirror a binary tree: swap every node's left and right children.

**Example:**
```text
     4              4
   /   \          /   \
  2     7   →    7     2
 / \   / \      / \   / \
1   3 6   9    9   6 3   1
```

## Walkthrough

Swap children at every node — each swap is independent, so any traversal order works. The recursion swaps top-down, and the returned subtrees slot into the *opposite* side.

**[1] the tree, before**
```text
4
├─L 2
│  ├─L 1
│  └─R 3
└─R 7
   ├─L 6
   └─R 9
```

**[2] swap at the root**
```text
4
├─L 7
└─R 2
```

**[3] swap inside the 7 subtree**
```text
4
├─L 7
│  ├─L 9
│  └─R 6
└─R 2
```

**[4] swap inside the 2 subtree — done**
```text
4
├─L 7
│  ├─L 9
│  └─R 6
└─R 2
   ├─L 3
   └─R 1
```

**[5] the one-line core**
```text
root.left, root.right = invert(root.right), invert(root.left)
```

Why it works: mirroring = every node swaps its two children — n independent operations, so the traversal is irrelevant (DFS top-down, bottom-up, or a BFS queue all give the same tree). O(n) time, O(h) space. The famous "Homebrew author rejected by Google" problem; theBST mirror is also 0101's equality test target (symmetric tree = same as its invert).
