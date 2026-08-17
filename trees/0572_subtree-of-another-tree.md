# 572 — Subtree of Another Tree

## Problem

Is `subRoot` an exact subtree of `root` — same structure and values starting at some node?

**Example:** `root = [3,4,5,1,2]`, `subRoot = [4,1,2]` → `true`

## Walkthrough

Two nested recursions: at every node of `root`, ask "is the tree here **identical** to subRoot?" — the identity test is 0100's lockstep compare (this folder). First match wins.

**[1] the pair**
```text
root:  3            subRoot: 4
      / \                    / \
     4   5                  1   2
    / \
   1   2
```

**[2] test at the root (3 vs 4)**
```text
same(3-tree, 4-tree)?  3 ≠ 4 ✗ → recurse left and right
```

**[3] test at node 4**
```text
same(4-subtree, subRoot):  4=4 ✓, 1=1 ✓, 2=2 ✓, nulls align ✓
```

**[4] true**
```text
return True — an exact match hanging at root's left child
```

**[5] a near miss**
```text
subRoot' = 4(1, 2(9,)):  the 2 nodes differ (2 has a child, the other doesn't)
same() fails everywhere → False — values alone aren't enough, shape must match
```

Why it works: "subtree" decomposes into "∃ node : identical(node, subRoot)" — an existential over root's nodes of a pairwise equality, both easy recursions. O(m·n) worst case (no early structural pruning); the O(m+n) version serializes both trees with null markers (`#`) and does a substring search — Rabin-Karp or KMP (Ch. 32), which is exactly what the null markers make sound.
