# 239 — Sliding Window Maximum

## Problem

For every window of size k, report its maximum.

**Example:** `nums = [1,3,-1,-3,5,3,6,7]`, `k = 3` → `[3,3,5,5,6,7]`

## Walkthrough

A **monotonic decreasing deque**: front is always the window's max. On each new element: pop smaller values off the back (they can never be a max again — newer and bigger), push it; drop the front if it slid out of range. Same deque discipline as problem 739's stack (in `stacks/`), but served from the front too.

**[1] window [1,3,−1] — 1 evicted by 3**
```text
[1, 3, -1, -3, 5, 3, 6, 7]
 L     R
deque: [3, -1]  max=3
```

**[2] window slides to [3,−1,−3]**
```text
[1, 3, -1, -3, 5, 3, 6, 7]
    L     R
deque: [3, -1, -3]  max=3  −3 enters at the back
```

**[3] window [−1,−3,5] — 5 cleans up**
```text
[1, 3, -1, -3, 5, 3, 6, 7]
       L     R
deque: [5]  −3, −1, (3 out of range) all popped — 5 is max
```

**[4] window [−3,5,3]**
```text
[1, 3, -1, -3, 5, 3, 6, 7]
          L     R
deque: [5, 3]  max=5
```

**[5] window [5,3,6] and [3,6,7]**
```text
[1, 3, -1, -3, 5, 3, 6, 7]
                L     R
deque: [7]  6 evicts 5,3? 6 evicts 3,5 → [6]; then 7 evicts 6 → [7]
```

**[6] the collected maxes**
```text
output: [3, 3, 5, 5, 6, 7]
```

Why it works: an element smaller than a newer one is dominated — the newer one will outlive it *and* beat it, so it can be discarded the moment the newer one arrives. The deque therefore holds only candidates in decreasing order; the front survives until it exits the window. Each index enters and leaves the deque once → O(n).
