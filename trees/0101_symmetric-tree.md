# 101 — Symmetric Tree

## Problem

Is the tree a mirror of itself (left/right flipped)?

**Example:** `[1,2,2,3,4,4,3]` → `true`

## Walkthrough

Two coupled cursors: compare `(L.left, R.right)` and `(L.right, R.left)` — the mirrored pairs — recursively. The root's left and right subtrees must mirror each other.

**[1] the mirror test starts at the children of the root**
```text
1  ✓
├─L 2        2 R┐
│  ├─L 3     3  │
│  └─R 4     4  │
└───────────────┘
compare (2, 2): equal? recurse on (3, 3) and (4, 4)
```

**[2] mirrored pairs recurse**
```text
1  ✓
├─L 2 ✓
└─R 2 ✓
inner call: L=2's left (3) vs R=2's right (3) ✓
outer call: L=2's right (4) vs R=2's left (4) ✓
```

**[3] leaves line up — true**
```text
all paired comparisons equal (and nulls paired with nulls) → return True
```

**[4] an asymmetric tree**
```text
1
├─L 2
└─R 2
   └─R 3
L.left=null vs R.right=3 → mismatch → False
```

Why it works: mirroring is an involution — the tree equals its mirror iff for every pair of symmetric positions, the values (and nullness) agree. The simultaneous traversal `(a, b) → (a.left, b.right), (a.right, b.left)` visits exactly the symmetric position pairs. O(n) time, O(h) depth; iterative with a queue of pairs is identical.
