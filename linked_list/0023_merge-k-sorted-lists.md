# 23 — Merge k Sorted Lists

## Problem

Merge `k` sorted linked lists into one sorted list.

**Example:** `[1→4→5, 1→3→4, 2→6]` → `1→1→2→3→4→4→5→6`

## Walkthrough

A **min-heap of the k current heads**: the global smallest remaining node is always one of the heads. Pop it, append to the output, push its successor. The heap size stays k.

**[1] seed the heap with the three heads**
```text
L1: 1 → 4 → 5
L2: 1 → 3 → 4
L3: 2 → 6
heap=[(1,L1),(1,L2),(2,L3)]  pop 1 from L1
```

**[2] append 1, push its next (4)**
```text
out: 1 → …
heap=[(1,L2),(2,L3),(4,L1)]  pop 1 from L2
```

**[3] append 1, push 3**
```text
out: 1 → 1 → …
heap=[(2,L3),(3,L2),(4,L1)]  pop 2
```

**[4] the sweep continues**
```text
out: 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6
each pop advances exactly one list by one node
```

**[5] done**
```text
return the dummy-headed merged list ✓
```

Why it works: pairwise merging k lists left-to-right is O(N·k); the heap keeps "which head is smallest" in O(log k) per node instead of O(k) — total O(N log k). Divide-and-conquer pairwise merging hits the same bound (merge in rounds, CLRS Ch. 2.3 style — that's how merge sort itself is a k=2 instance). Problem 0355's feed (queue/) is this heap applied to design.
