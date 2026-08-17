# 102 — Binary Tree Level Order Traversal

## Problem

Return the values of a binary tree level by level, top to bottom, left to right.

**Example:** tree `[3,9,20,null,null,15,7]` → `[[3],[9,20],[15,7]]`

## Walkthrough

BFS with a queue — but snapshot the queue's size *before* each round: that count is exactly one level's worth of nodes. Process that many, enqueuing children as you go.

**[1] level 0 — the root alone**
```text
3  ✓
├─L 9
└─R 20
   ├─L 15
   └─R 7
queue=3  out=[[3]]  size=1 → one node = one level
```

**[2] level 1 — root's children**
```text
3  ✓
├─L 9  ✓
└─R 20  ✓
   ├─L 15
   └─R 7
queue=9,20  out=[[3],[9,20]]  3's children enqueue behind the level marker
```

**[3] level 2 — the leaves**
```text
3  ✓
├─L 9  ✓
└─R 20  ✓
   ├─L 15  ✓
   └─R 7  ✓
queue=15,7  out=[[3],[9,20],[15,7]]  queue empties → done
```

Why the size snapshot matters: without it, the queue mixes the tail of one level with the head of the next and level boundaries blur. Grab `size = len(queue)` at the top of each round, loop exactly that many pops — the children enqueued during the round belong to the *next* level automatically. O(n) time, O(w) space for the widest level w.
