# 124 — Binary Tree Maximum Path Sum

## Problem

A path is any sequence of nodes joined by edges, each node visited at most once. Maximize the path sum (values may be negative; a single node counts).

**Example:** `[-10,9,20,null,null,15,7]` → `42` (`15 → 20 → 7`)

## Walkthrough

Two different quantities per node: the best path **through** it (left gain + node + right gain — that's a candidate answer) and the best path **anchored** at it going down one side (what a parent may use — a path can't fork twice). The DFS returns the anchored gain; the through-sum feeds a running max.

**[1] the tree**
```text
-10
├─L 9
└─R 20
   ├─L 15
   └─R 7
```

**[2] leaves report their gains**
```text
-10
├─L 9
└─R 20
   ├─L 15  gain=15
   └─R 7   gain=7
```

**[3] node 20: through-path candidate**
```text
-10
├─L 9
└─R 20 ✓
   ├─L 15
   └─R 7
best = 20 + 15 + 7 = 42  anchored gain returned: 20 + max(15,7) = 35
```

**[4] node 9 and the root**
```text
-10 ✓
├─L 9   gain=9
└─R 20  gain=35
best = max(42, -10 + 9 + 35 = 34) = 42  root returns -10 + 35 = 25
```

**[5] answer survives the negative root**
```text
return 42  the root's through-path (34) never beat the inner one
```

Why it works: clamping gains at 0 encodes "skip this subtree" — a negative branch can only lower a through-path, and an anchored path may ignore one child entirely. Returning `val + max(l, r)` enforces the no-fork rule upward, while `val + l + r` captures the one legal fork at the node itself. Every node is processed once: O(n) time, O(h) space. The gain-clamp trick generalizes 053's Kadane (this repo): "extend or restart" in tree form.
