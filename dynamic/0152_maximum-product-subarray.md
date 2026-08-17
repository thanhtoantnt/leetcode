# 152 — Maximum Product Subarray

## Problem

Find the contiguous subarray with the **largest product**.

**Example:** `nums = [2,3,-2,4]` → `6` (`[2,3]`)

## Walkthrough

Kadane (problem 53) has a twist here: a negative number flips the game — today's most-negative run can become tomorrow's maximum. So track **both** `curMax` and `curMin` ending at each index, and on each new element try all three candidates: the element alone, it times the old max, it times the old min.

**[1] i=0 — solo**
```text
[2, 3, -2, 4]
  i
curMax=2 curMin=2 best=2  2 initializes both extremes
```

**[2] i=1 — products grow**
```text
[2, 3, -2, 4]
     i
curMax=6 curMin=3 best=6  3 vs 3·2=6 / 3·2=3
```

**[3] i=2 — sign flip: extremes swap**
```text
[2, 3, -2, 4]
        i
curMax=-2 curMin=-12 best=6  -2 vs 6·(−2)=−12 vs 3·(−2)=−6 → max −2, min −12
```

**[4] i=3 — the sleeping min wakes up… almost**
```text
[2, 3, -2, 4]
           i
curMax=4 curMin=-48 best=6  4 vs (−2)·4=−8 vs (−12)·4=−48
```

**[5] done — and the case that proves min-tracking**
```text
[2, 3, -2, 4, -1]
           i  (appended)
curMax=48  (−12)·(−1)=48 — the old *minimum* becomes the new maximum
best=48
```

Why it works: the product of a run ending at i either starts fresh at nums[i] or extends a previous run — and since an extension by a negative swaps max↔min, the best future may hang off either extreme, so both must be carried. One pass, O(n) time, O(1) space. Zeros reset naturally: the "element alone" candidate always survives.
