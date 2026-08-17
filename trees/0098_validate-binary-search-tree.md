# 98 — Validate Binary Search Tree

## Problem

Is the tree a valid BST — every node's left subtree strictly smaller, right subtree strictly larger?

**Example:** `[5,1,4,null,null,3,6]` → `false` (3 sits in 5's right subtree)

## Walkthrough

The trap: comparing each node only against its children misses violations deeper down. The fix is to thread a **(min, max) bound** down the recursion — arriving at a node, its entire subtree must fit inside the interval its ancestors carved out.

**[1] root 5 — no constraints yet**
```text
5  [(-∞,+∞)]
├─L 1
└─R 4
```

**[2] bounds propagate**
```text
5  ✓
├─L 1  [(-∞,5)]
└─R 4  [(5,+∞)]
1's subtree must stay below 5;  4's must stay above 5
```

**[3] the violation appears at 3**
```text
5  ✓
├─L 1  [(-∞,5)] ✓
└─R 4  [(5,+∞)] ✓
   ├─L 3  [(5,4)] — empty interval!  3 < 5 violates the grandparent bound
   └─R 6
```

**[4] verdict**
```text
return False  node 3 vs its local-parent 4 passes (3 < 4) —
only the inherited bound (must exceed 5) exposes it
```

**[5] the alternative view — inorder must ascend**
```text
inorder: 1, 3, 4, 5, 6? — with the bad tree: 1,5,3,4,6 → 5 > 3 exposes it
a BST's inorder walk is strictly increasing; one scan decides
```

Why it works: the BST property is *global* — each node constrains its whole subtree, not just its children. Threading (min,max) carries exactly the accumulated ancestor constraints (the inorder view is the same fact re-read as a sortedness check). O(n) time, O(h) recursion depth.
