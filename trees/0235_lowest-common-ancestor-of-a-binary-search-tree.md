# 235 — Lowest Common Ancestor of a BST

## Problem

Given a binary search tree and two nodes `p` and `q`, find their lowest common ancestor — the deepest node that has both as descendants (a node counts as its own descendant).

**Example:** BST from `[6,2,8,0,4,7,9]` with `p=3`, `q=5` → the LCA is `4`.

## Walkthrough

No recursion needed. Walk down from the root using the BST ordering: both values smaller → go left, both bigger → go right, **split** (or equal) → you're standing on the LCA.

**[1] at 6 — both smaller**
```text
6  [cur]
├─L 2
│  ├─L 0
│  └─R 4
│     ├─L 3
│     └─R 5
└─R 8
   ├─L 7
   └─R 9
p=3 q=5   3 < 6 and 5 < 6 → both live left → descend
```

**[2] at 2 — both bigger**
```text
6  ✓
├─L 2  [cur]
│  ├─L 0
│  └─R 4
│     ├─L 3
│     └─R 5
└─R 8
   ├─L 7
   └─R 9
3 > 2 and 5 > 2 → both live right → descend
```

**[3] at 4 — they split**
```text
6  ✓
├─L 2  ✓
│  ├─L 0
│  └─R 4  [cur] = LCA ✓
│     ├─L 3
│     └─R 5
└─R 8
   ├─L 7
   └─R 9
3 < 4 < 5 → p and q are on different sides → 4 is the answer
```

Why it works: the LCA is the first node where the path to `p` and the path to `q` diverge. Above it both values sit on one side; below it they separate. BST ordering finds it in one O(h) walk — no parent pointers, no path lists.
