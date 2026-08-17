# 746 — Min Cost Climbing Stairs

## Problem

Climb from step 0 or 1 (free choice of start) to beyond the last step; leaving step `i` costs `cost[i]`. Minimum total.

**Example:** `cost = [10,15,20]` → `15` (start on step 1, pay 15, step off the top)

## Walkthrough

0070's recurrence with prices: to reach step `i` you left step `i−1` or `i−2` — pay that step's cost plus the best cost of having reached it. Two rolling scalars; "the top" is one past the array.

**[1] reach costs start free**
```text
step:  0  1  2  3(top)
best:  0  0  .  .
standing on step 0 or 1 costs nothing yet
```

**[2] step 2 — both routes priced**
```text
step:  0  1  2  3(top)
best:  0  0  10  .
via step 0: 0+10 = 10;  via step 1: 0+15 = 15 → best(2) = 10
```

**[3] the top**
```text
step:  0  1  2  3(top)
best:  0  0  10  15
via step 1: 0+15 = 15;  via step 2: 10+20 = 30 → best(top) = 15 ✓
```

**[4] the routing shown on the array**
```text
[10, 15, 20]
 ✗       ✗   skip both 10 and 20: land free on 1, pay 15, step off
```

**[5] the free start needs no special case**
```text
best(0) = best(1) = 0 encodes "begin on either step"; the loop runs
to len(cost)+1, treating beyond-the-end as one more landing
```

Why it works: identical partition to 0070 (last move from i−1 or i−2) with the leaving-fee attached to each option — the Fibonacci machine with weights. O(n) time, O(1) space.
