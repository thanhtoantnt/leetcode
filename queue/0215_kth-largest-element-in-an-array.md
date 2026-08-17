# 215 — Kth Largest Element in an Array

## Problem

Find the k-th largest element (by rank, not distinct value).

**Example:** `nums = [3,2,1,5,6,4]`, `k = 2` → `5`

## Walkthrough

Keep a **min-heap of size k**: the heap holds the k largest seen so far, and its *top* is the weakest of them — the current k-th largest. Push each number; when the heap exceeds k, evict the smallest.

**[1] heapify first k=2 elements**
```text
[3, 2, 1, 5, 6, 4]
heap=[2,3]  min on top: 2
```

**[2] 1 arrives — smaller than top, ignored**
```text
[3, 2, 1, 5, 6, 4]
heap=[2,3]  1 < 2 → would be evicted immediately; skip (push+pop or guard)
```

**[3] 5 arrives — evicts 2**
```text
[3, 2, 1, 5, 6, 4]
heap=[3,5]  push 5 → size 3 → pop 2; top now 3
```

**[4] 6 arrives — evicts 3**
```text
[3, 2, 1, 5, 6, 4]
heap=[5,6]  top 5 — the two largest so far are 6 and 5
```

**[5] 4 arrives — too small; answer on top**
```text
[3, 2, 1, 5, 6, 4]
heap=[5,6]  4 < 5 → rejected; return top = 5 ✓
```

Why it works: the heap invariant is "exactly the k largest elements seen, smallest of them on top" — each new candidate either beats the top (it belongs, the old #k leaves) or doesn't (discard). After the scan, top = k-th largest overall. O(n log k) time, O(k) space. Alternatives: full sort O(n log n); Quickselect partitioning averages O(n) (worst O(n²), or O(n) guaranteed with median-of-medians, CLRS Ch. 9).
