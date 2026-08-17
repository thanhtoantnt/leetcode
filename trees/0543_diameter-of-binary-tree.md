# 543 — Diameter of Binary Tree

## Problem

The diameter: longest path (in **edges**) between any two nodes, possibly bending through ancestors.

**Example:** `[1,2,3,4,5]` → `3` (`4 → 2 → 5`)

## Walkthrough

At each node, the best path **through** it has length `leftDepth + rightDepth`; the DFS returns only `1 + max(depths)` upward — a path may enter and leave a node at most once. Same skeleton as 0124's path sum (this folder), with counts instead of values.

**[1] the tree**
```text
1
├─L 2
│  ├─L 4
│  └─R 5
└─R 3
```

**[2] leaves report depth 1**
```text
1
├─L 2
│  ├─L 4  depth=1
│  └─R 5  depth=1
└─R 3
```

**[3] node 2: through-path candidate**
```text
1
├─L 2 ✓
│  ├─L 4
│  └─R 5
best = 1+1 = 2 (4→2→5)  node 2 returns depth 2
```

**[4] node 3 and the root**
```text
1 ✓
├─L 2   depth 2
└─R 3   depth 1
best = max(2, 2+1 = 3) = 3 ✓  root returns depth 3
```

**[5] answer**
```text
return 3  path 4→2→1→3 also has 3 edges — tied, same count
```

Why it works: every path has a unique highest node where it "turns" — and at that node it consumes one downward chain per side, so its length is exactly l+r depths there; scanning all nodes covers all turn points. O(n) time, O(h) space. Swap `l+r` for `val+l+r` and depth for gain and this is 0124 verbatim.
