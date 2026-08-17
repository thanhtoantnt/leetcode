# 253 — Meeting Rooms II

## Problem

Minimum number of rooms so all meetings can run (overlaps share rooms)?

**Example:** `[[0,30],[5,10],[15,20]]` → `2`

## Walkthrough

The answer is the **peak concurrency** — the max number of meetings alive at one instant. Sweep: walk starts and ends in order; each start occupies a room (+1), each end frees one (−1); on a start==end tie, process the end first (back-to-back reuses the room). Track the max.

**[1] sorted starts and ends**
```text
starts: 0  5  15
ends:   10 20 30
```

**[2] t=0: meeting opens**
```text
rooms=1 best=1
```

**[3] t=5: second opens before first ends**
```text
starts[1]=5 < ends[0]=10 → rooms=2 best=2 ✓
```

**[4] t=10 frees, t=15 opens**
```text
rooms=1 … then 2 — the peak stays 2 → return 2
```

**[5] the heap view (same answer, different bookkeeping)**
```text
sort by start; a min-heap of end-times = rooms in use; when a new
meeting starts after the earliest end, pop (reuse) — heap size peaks
at 2 here
```

Why it works: concurrency changes only at interval endpoints, so the sorted-event sweep sees every distinct configuration; the running counter is exact at each event, and its max is the global peak. Two-pointer form shown, heap form equivalent — both O(n log n). This is the "how many platforms" family (railway, elevator) — and 0056's merging (this folder) is the complementary "what overlaps" question.
