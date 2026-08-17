# 105 — Construct Binary Tree from Preorder and Inorder Traversal

## Problem

Rebuild the unique tree from its preorder and inorder sequences.

**Example:** `preorder = [3,9,20,15,7]`, `inorder = [9,3,15,20,7]` → the tree `[3,9,20,null,null,15,7]`

## Walkthrough

Two facts do everything: preorder's first element is the **root**; that root splits inorder into left-subtree letters (before it) and right-subtree letters (after it). Recurse on both slices — an inorder index map makes each split O(1).

**[1] root = 3, splits inorder**
```text
pre:  [3, 9, 20, 15, 7]
in:   [9, | 3 |, 15, 20, 7]
left = [9]  right = [15,20,7]
```

**[2] left subtree: pre [9], in [9]**
```text
3
├─L 9  single node — done
```

**[3] right subtree: pre [20,15,7], in [15,20,7]**
```text
3
├─L 9
└─R 20  root 20 splits in: [15] | 20 | [7]
```

**[4] 20's children**
```text
3
├─L 9
└─R 20
   ├─L 15
   └─R 7
```

**[5] done — and why it's unique**
```text
each recursion consumes one preorder head and one inorder span —
the shape is forced at every step, so the tree is unique
```

Why it works: preorder = root, then left, then right; inorder = left, root, right — so the root is over-determined (head of the preorder run) and its inorder position is the only place the left/right boundary could be. Slicing both sequences accordingly restarts the same problem on smaller inputs. O(n) with the hash map (the naive index scan inside would make it O(n²)); recursion depth up to h.
