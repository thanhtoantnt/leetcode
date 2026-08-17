# 70 — Climbing Stairs

## Problem

Climb `n` stairs taking 1 or 2 steps at a time. How many distinct ways to the top?

**Example:** `n = 5` → `8`

## Walkthrough

Think about the **last move**: it's a 1-step from stair n−1 or a 2-step from n−2 — two disjoint cases covering everything. `ways(n) = ways(n−1) + ways(n−2)`: Fibonacci, seeded by 1 way to stand at 0 and 1 way to reach 1.

**[1] seeds**
```text
n:  0 1 2 3 4 5
dp: 1 1 . . . .
one way to be at 0 (do nothing); one way to reach 1 (single step)
```

**[2] n=2**
```text
n:  0 1 2 3 4 5
dp: 1 1 2 . . .
1+1 or 2 → 2 = dp[1]+dp[0]
```

**[3] n=3**
```text
n:  0 1 2 3 4 5
dp: 1 1 2 3 . .
111, 12, 21 → 3
```

**[4] n=4, n=5**
```text
n:  0 1 2 3 4 5
dp: 1 1 2 3 5 8
dp[4]=3+2=5, dp[5]=5+3=8 → return 8
```

Why it works: partitioning by the last move is exhaustive and disjoint — the two option sets share no path and cover all of them — exactly the 0/1 recurrence shape of decode-ways (0091, this folder) and the Fibonacci analysis of Euclid's worst case (CLRS Ch. 31). Two rolling scalars suffice: O(n) time, O(1) space.
