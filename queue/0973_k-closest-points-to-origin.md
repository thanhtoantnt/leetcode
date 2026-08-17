# 973 — K Closest Points to Origin

## Problem

Return the k points nearest the origin.

**Example:** `points = [[1,3],[-2,2]]`, `k = 1` → `[[-2,2]]` (dist² 8 < 10)

## Walkthrough

Max-heap of size k keyed on squared distance: the heap's top is the *worst* (farthest) of the kept points; any newcomer closer than the top evicts it. Squared distances avoid `sqrt` — monotone, and exact in integers.

**[1] seed the heap with the first point**
```text
[(1,3)] heap dist²=9  k=1: heap=[9:(1,3)]
```

**[2] (−2,2): dist² 8 beats top 9**
```text
[(-2,2)] heap dist²=8  8 < 9 → push, size 2 > 1 → pop the 9
```

**[3] heap holds the winner**
```text
[(-2,2)] return [(-2,2)] ✓
```

**[4] bigger example, k=2, points (3,3)(5,-1)(-2,4)**
```text
heap after (3,3): [18:(3,3)]
after (5,-1): [18:(3,3), 26:(5,-1)]
after (-2,4): 20 < 26 → evict (5,-1) → [(3,3),(-2,4)]
```

**[5] answer**
```text
return [(3,3),(-2,4)]  the two smallest dist²: 18 and 20
```

Why it works: keeping the k smallest distances in a **max**-heap puts the current borderline (largest kept) at the top for instant comparison — symmetric to 215's min-heap for k-th largest. O(n log k) time, O(k) space. Alternative: sorting by dist² is O(n log n); Quickselect on distances averages O(n).
