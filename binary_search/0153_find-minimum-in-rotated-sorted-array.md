# 153 — Find Minimum in Rotated Sorted Array

## Problem

A sorted array of distinct values rotated between 1 and n times. Find the minimum in O(log n).

**Example:** `nums = [4,5,6,7,0,1,2]` → `0` (at index 4)

## Walkthrough

Compare `mid` against `nums[hi]` — the element at the right edge tells you which side the rotation point is on. **mid > hi ⇒ the cliff (minimum) is right of mid. mid < hi ⇒ mid itself or something left of it is the minimum** — the right span is sorted and safe to drop.

**[1] mid=3: nums[3]=7 vs nums[6]=2**
```text
[4, 5, 6, 7, 0, 1, 2]
 L        M        H
lo=0 hi=6 mid=3  7 > 2 → minimum lies strictly right of mid → lo=4
```

**[2] mid=5: nums[5]=1 vs nums[6]=2**
```text
[4, 5, 6, 7, 0, 1, 2]
             L  M  H
lo=4 hi=6 mid=5  1 < 2 → right span sorted → minimum at mid or left → hi=5
```

**[3] mid=4**
```text
[4, 5, 6, 7, 0, 1, 2]
             LM  H
lo=4 hi=5 mid=4  0 < 1 → hi=4 → lo==hi, stop
```

**[4] converged**
```text
[4, 5, 6, 7, 0, 1, 2]
             LMH
nums[4]=0  return 0
```

Why it works: in a rotated array exactly one "cliff" exists (the minimum); comparing mid to hi decides which half is cliff-free and discards it. Never compare to `lo` — with a non-rotated array, `nums[mid] > nums[lo]` is true everywhere and tells you nothing. O(log n), the warm-up for problem 33 in this folder.
