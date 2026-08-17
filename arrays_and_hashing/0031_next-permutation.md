# 31 — Next Permutation

## Problem

Rearrange `nums` into the **next** lexicographically greater permutation. If it's already the max arrangement, roll over to the lowest.

**Example:** `nums = [1,5,8,4,7,6,5,3,1]` → `[1,5,8,5,1,3,4,6,7]`

## Walkthrough

Three moves, all in place. (1) Scan from the right for the **pivot**: the first element smaller than its successor — everything right of it is a descending suffix, the max arrangement of those digits. (2) Swap the pivot with the **rightmost successor** — the smallest suffix element that still beats it. (3) Reverse the suffix into ascending order, the *smallest* arrangement.

**[1] find the pivot**
```text
[1, 5, 8, 4, 7, 6, 5, 3, 1]
          P        ← ← ←  suffix 7,6,5,3,1 descends; 4 < 7 → pivot = 4
```

**[2] rightmost element greater than pivot**
```text
[1, 5, 8, 4, 7, 6, 5, 3, 1]
          P           S     1,3 < 4; 5 > 4 → swap with 5
```

**[3] swap pivot with successor**
```text
[1, 5, 8, 5, 7, 6, 4, 3, 1]
          P↔S done  prefix 1,5,8,5 now exceeds the old permutation
```

**[4] reverse the suffix**
```text
[1, 5, 8, 5, 1, 3, 4, 6, 7]
suffix ascending  7,6,4,3,1 → 1,3,4,6,7 → the answer
```

**[5] done — in place, no allocation**
```text
[1, 5, 8, 5, 1, 3, 4, 6, 7]
return [1,5,8,5,1,3,4,6,7]
```

Why it works: the descending suffix is the largest possible tail for that prefix, so no bigger permutation exists without touching the pivot; raising the pivot as little as possible (smallest qualifying successor) and then minimizing the suffix yields exactly the next permutation. O(n) time. If no pivot exists (whole array descending, like `[3,2,1]`), it's the maximum — reversing everything gives `[1,2,3]`.
