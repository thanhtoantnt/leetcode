# 279 — Perfect Squares

## Problem

Sum `n` using perfect squares (1, 4, 9, … reused freely). Fewest squares needed?

**Example:** `n = 12` → `3` (`4+4+4`)

## Walkthrough

Coin change (0322, this folder) with coins = the squares ≤ n. `dp[a] = 1 + min(dp[a−s²])` over squares that fit — each amount tries every square as its last coin.

**[1] seed dp[0] = 0**
```text
a:  0 1 2 3 4 5 6 7 8 9 10 11 12
dp: 0 . . . . . . . . . .  .  .
coins: 1, 4, 9
```

**[2] amounts 1–3: only 1s available**
```text
a:  0 1 2 3 4 5 6 7 8 9 10 11 12
dp: 0 1 2 3 . . . . . . .  .  .
dp[3] = dp[2]+1 = 3 (1+1+1)
```

**[3] amount 4: a single square**
```text
a:  0 1 2 3 4 5 6 7 8 9 10 11 12
dp: 0 1 2 3 1 . . . . . .  .  .
dp[4] = dp[0]+1 = 1 (just 4)
```

**[4] amounts 5–8: 4s plus 1s**
```text
a:  0 1 2 3 4 5 6 7 8 9 10 11 12
dp: 0 1 2 3 1 2 3 4 2 . .  .  .
dp[8] = dp[4]+1 = 2 (4+4)
```

**[5] 9 lands, 12 answers**
```text
a:  0 1 2 3 4 5 6 7 8 9 10 11 12
dp: 0 1 2 3 1 2 3 4 2 1 2  3  3
dp[12] = dp[8]+1 = 3 (4+4+4) → return 3
```

Why it works: the last square of any optimal decomposition leaves a smaller solved amount — the same last-coin argument as 0322. O(n·√n). Lagrange's four-square theorem bounds every answer by 4 (and Legendre: 3 unless n = 4^a(8b+7)) — a BFS over the "subtract a square" graph reaches depth ≤ 4 as well.
