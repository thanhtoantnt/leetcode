# 518 — Coin Change II

## Problem

**Count** the combinations (order irrelevant) of coins summing to `amount`.

**Example:** `coins = [1,2,5]`, `amount = 5` → `4` (`5`, `2+2+1`, `2+1+1+1`, `1+1+1+1+1`)

## Walkthrough

Same table as 322 but counting, and the **loop order is the whole problem**: coins outer, amounts inner. Processing one coin at a time means each combination is counted once, ordered by which coins it uses — `1+2` and `2+1` are the same combination, generated only as "the 1s first, then the 2s".

**[1] dp[0] = 1 — one way to make nothing**
```text
a:  0 1 2 3 4 5
dp: 1 . . . . .
coin 1:  dp[a] += dp[a-1]
```

**[2] after coin 1 — only all-1s combos**
```text
a:  0 1 2 3 4 5
dp: 1 1 1 1 1 1
every amount: exactly one way (1+1+…+1)
```

**[3] coin 2 folds in — combos using 2s after 1s**
```text
a:  0 1 2 3 4 5
dp: 1 1 2 2 3 3
dp[2] += dp[0] → 2 (11, 2); dp[5] += dp[3] → 3
```

**[4] coin 5 folds in**
```text
a:  0 1 2 3 4 5
dp: 1 1 2 2 3 4
dp[5] += dp[0] → 4 → answer 4
```

**[5] what coin-inner order would do (the bug)**
```text
amounts outer, coins inner → 1+2 and 2+1 both counted
dp[3]=3 (111,12,21) — that's permutations, problem 377, not combinations
```

Why it works: with coins outer, dp[a] after processing coins c₁…c_k counts combinations using only those coins, each exactly once — a new coin only *extends* old combinations by prepending more copies of itself, never reordering. Swap the loops and you count ordered sequences instead. O(amount · |coins|).
