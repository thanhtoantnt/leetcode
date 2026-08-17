# 1448 — Count Good Nodes in Binary Tree

## Problem

A node is **good** if no ancestor has a larger value. Count them.

**Example:** `[3,1,4,3,null,1,5]` → `4` (3, 3, 4, 5; the two 1s are shadowed)

## Walkthrough

DFS threading the **max-so-far along the path**: a node is good iff its value ≥ that running max. Update the max for the children's descent.

**[1] root 3 — good, path max = 3**
```text
3  ✓
├─L 1
└─R 4
count=1 max=3
```

**[2] descend left: 1 shadowed, but its child 3**
```text
3  ✓
├─L 1  ✗ (1 < 3)
│  └─L 3  ✓ (3 ≥ 3 — ties count)
└─R 4
count=2 max going down left was 3
```

**[3] descend right: 4 leads, 1 shadows, 5 shines**
```text
3  ✓
├─L 1 ✗
│  └─L 3 ✓
└─R 4 ✓ (4 ≥ 3)
   ├─L 1 ✗ (1 < 4)
   └─R 5 ✓ (5 ≥ 4)
count=4
```

**[4] done**
```text
return 4  good nodes: {3, 3, 4, 5}
```

Why it works: "no ancestor larger" depends only on the maximum of the path above — a single scalar summarizes the whole ancestor set, so carrying `pathMax` through the DFS answers each node in O(1). Every node visited once → O(n) time, O(h) depth. The mirror trick of problem 98's bounds: there min/max bracketed the subtree; here only the max matters, only comparisons against the path.
