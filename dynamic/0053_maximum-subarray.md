# 53 — Maximum Subarray

## Problem

Find the contiguous subarray with the largest sum and return that sum.

**Example:** `nums = [-2,1,-3,4,-1,2,1,-5,4]` → `6` (`[4,-1,2,1]`)

## Walkthrough

Kadane's algorithm. Walk once; `cur` is the best sum **ending here** — either extend the previous run or restart at this element, whichever is larger. `best` tracks the global max.

**[1] i=0 — running sum starts negative**
```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
  i
cur=-2 best=-2  first element initializes both
```

**[2] i=1 — restart**
```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
     i
cur=1 best=1  max(1, -2+1) = 1 → a negative prefix is dead weight, drop it
```

**[3] i=3 — the winning run begins**
```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
              i
cur=4 best=4  -3 dragged cur to -2, so restart at 4
```

**[4] i=4,5 — extend**
```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
                  i
cur=5 best=5  4-1=3, then 3+2=5 — climbing
```

**[5] i=6 — peak**
```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
                       i
cur=6 best=6  the run [4,-1,2,1] reaches its maximum
```

**[6] i=7 — tail dips, best survives**
```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
                           i
cur=1 best=6  extending through -5 hurts, but best is already locked in
```

**[7] done**
```text
[-2, 1, -3, 4, -1, 2, 1, -5, 4]
                              i
cur=5 best=6  return 6
```

Why it works: the best subarray ending at i either is nums[i] alone or extends the best one ending at i−1 — no third option. One pass, O(n) time, O(1) space. (CLRS Ch. 4 shows the O(n log n) divide-and-conquer version too; Kadane is the linear refinement.)
