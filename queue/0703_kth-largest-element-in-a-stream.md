# 703 — Kth Largest Element in a Stream

## Problem

A class wrapping a stream: on `add(val)`, return the k-th largest among everything seen so far.

**Example:** `k = 3`, stream `[4,5,8,2]` then adds `3,5,10,9,4` → `4,5,5,8,8`

## Walkthrough

Problem 215's heap, made **persistent**: initialize a min-heap with the first k elements, then every `add` is push-and-maybe-pop. The top is always the running k-th largest.

**[1] init: heapify [4,5,8,2], keep k=3**
```text
heap=[4,5,8]  2 evicted — top 4 = 3rd largest of {4,5,8,2}
```

**[2] add(3) — below top**
```text
heap=[4,5,8]  3 < 4 → return 4
```

**[3] add(5) — enters, 4 leaves**
```text
heap=[5,5,8]  push 5 (size 4) → pop 4 → return 5
```

**[4] add(10), add(9) — big values keep rising top**
```text
heap=[5,8,10] → [8,9,10]  return 5, then 8
```

**[5] add(4) — rejected**
```text
heap=[8,9,10]  4 < 8 → return 8
```

Why it works: same invariant as 215 — "the k largest so far, min on top" — but maintained incrementally, so each query is O(log k) instead of re-scanning O(n log k). The lazy variant (push everything, pop only when size > k) is the same bounds; the eager guard `if val > top` skips heap work for small values.
