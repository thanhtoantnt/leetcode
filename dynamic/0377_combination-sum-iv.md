# 377 — Combination Sum IV

## Problem

Count the sequences (order matters — really *compositions*) of `nums` summing to `target`, elements reusable.

**Example:** `nums = [1,2,3]`, `target = 4` → `7` — `(1,1,1,1), (1,1,2), (1,2,1), (2,1,1), (2,2), (1,3), (3,1)`

## Walkthrough

The last element of any valid sequence is some `coin ∈ nums` — so `dp[t] = Σ_coins dp[t−coin]`, built amounts-outer. That loop order is the entire difference from 0518 (this folder): iterating coins **inside** each amount counts every ordering of the same multiset separately.

**[1] seed dp[0] = 1 — the empty sequence**
```text
t:  0 1 2 3 4
dp: 1 . . . .
```

**[2] t=1**
```text
dp[1] = dp[0] (coin 1) = 1   (coins 2,3 too big)
```

**[3] t=2**
```text
dp[2] = dp[1] + dp[0] = 2   (1+1, 2)
```

**[4] t=3**
```text
dp[3] = dp[2] + dp[1] + dp[0] = 4
```

**[5] t=4**
```text
dp[4] = dp[3] + dp[2] + dp[1] = 4+2+1 = 7 ✓ return 7
```

Why it works: sequences are classified exhaustively by their last element — dp[t−coin] already counts every prefix, so the sum covers every sequence ending in that coin, and different orders emerge because each amount is finalized before all coins get a chance to extend it (versus 0518's coins-outer, which freezes each coin's usage frontier and counts multisets once). The tribonacci-style fill visible in frames 2–5 is the composition recurrence. O(target·n); memoized top-down is identical.
