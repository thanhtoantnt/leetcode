# 322 — Coin Change

## Problem

Fewest coins summing to `amount` (repetition allowed), or `-1`.

**Example:** `coins = [1,2,5]`, `amount = 11` → `3` (`5+5+1`)

## Walkthrough

`dp[a]` = fewest coins for amount `a`. Base `dp[0] = 0` (no coins for nothing); each amount tries **every coin** as its last coin: `dp[a] = 1 + min(dp[a−coin])` over coins that fit. Greedy (biggest first) fails on e.g. `[1,3,4]`, amount 6 — greedy gives 4+1+1 = 3 coins, optimal is 3+3 = 2. (`.` = ∞ / unreachable.)

**[1] dp[0] seeded**
```text
a:  0 1 2 3 4 5 6 7 8 9 10 11
dp: 0 . . . . . . . . . .  .
coins=[1,2,5]  target 11
```

**[2] small amounts fill — one coin where possible**
```text
a:  0 1 2 3 4 5 6 7 8 9 10 11
dp: 0 1 1 2 2 1 . . . . .  .
dp[3]=1+dp[2]=2 (via 1) or 1+dp[1]=2 (via 2); dp[5]=1 via coin 5 ✓
```

**[3] amounts 6–8**
```text
a:  0 1 2 3 4 5 6 7 8 9 10 11
dp: 0 1 1 2 2 1 2 2 3 . .  .
dp[6]=1+dp[5]=2 (5+1); dp[7]=1+dp[5]=2 (5+2); dp[8]=1+dp[6]=3
```

**[4] amounts 9–11**
```text
a:  0 1 2 3 4 5 6 7 8 9 10 11
dp: 0 1 1 2 2 1 2 2 3 3 2  3
dp[10]=1+dp[5]=2; dp[11]=1+dp[10]=3 → answer 3
```

**[5] the greedy trap side by side**
```text
a:  0 1 2 3 4 5 6
dp: 0 1 2 1 2 3 2   ← coins [1,3,4]: dp[6]=2 (3+3)
greedy would say 4+1+1=3 ✗
```

Why it works: the last coin of any optimal solution leaves a smaller amount already solved optimally — trying each coin as last is exhaustive, so the table converges to true optima bottom-up. O(amount · |coins|) time, O(amount) space. Unreachable cells stay ∞ → return −1.
