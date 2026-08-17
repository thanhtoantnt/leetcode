# 33 — Search in Rotated Sorted Array

## Problem

A sorted array has been rotated at an unknown pivot, e.g. `[0,1,2,4,5,6,7]` becomes `[4,5,6,7,0,1,2]`. Given the rotated array and a `target`, return its index or `-1`. Must run in O(log n).

**Example:** `nums = [4,5,6,7,0,1,2]`, `target = 0` → `4`

## Walkthrough

Binary search still works — the trick is that at every midpoint, **at least one half is properly sorted**. Check which half, then check whether the target lies inside that sorted range.

`nums = [4,5,6,7,0,1,2]`, `target = 0`

**[1] lo=0 hi=6, mid=3**
```text
[4, 5, 6, 7, 0, 1, 2]
 L        M        H
lo=0 hi=6 mid=3  nums[mid]=7
```
Left half `[4..7]` is sorted, but 0 is not in `[4,7]` → the target must be right: `lo = mid+1 = 4`.

**[2] lo=4 hi=6, mid=5**
```text
[4, 5, 6, 7, 0, 1, 2]
             L  M  H
lo=4 hi=6 mid=5  nums[mid]=1
```
Left half `[0..1]` is sorted, and 0 **is** in `[0,1]` → go left: `hi = mid-1 = 4`.

**[3] lo=4 hi=4, mid=4 — found**
```text
[4, 5, 6, 7, 0, 1, 2]
             LMH
lo=4 hi=4 mid=4  nums[4]=0 = target ✓ return 4
```

Why it works: a rotated array is two sorted runs; whichever side of `mid` has `nums[lo] <= nums[mid]` is one clean sorted run, so a plain range check tells you whether the target could live there. Each step still halves the range → O(log n).
