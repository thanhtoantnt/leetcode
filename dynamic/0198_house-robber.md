# 198 — House Robber

## Problem

You rob houses along a street. `nums[i]` is the cash in house `i`. Adjacent houses have linked alarms — you cannot rob two neighbors. Return the maximum you can rob.

**Example:** `nums = [2, 7, 9, 3, 1]` → `12` (houses `2 + 9 + 1`)

## Walkthrough

`dp[i] = max(dp[i-1], nums[i] + dp[i-2])` — skip this house, or rob it and take the best from two back. Unfilled cells shown as `.`.

**[1] base cases**
```text
houses:  2  7  9  3  1
dp:      2  7  .  .  .
         0  1
dp[0]=2   dp[1]=max(7, 2+0)=7
```

**[2] i=2**
```text
houses:  2  7  9  3  1
dp:      2  7 11  .  .
               i
rob  9 + dp[0]=2 → 11   |   skip dp[1]=7   → 11 wins
```

**[3] i=3**
```text
houses:  2  7  9  3  1
dp:      2  7 11 11  .
                  i
rob  3 + dp[1]=7 → 10   |   skip dp[2]=11  → 11 wins (skip!)
```

**[4] i=4**
```text
houses:  2  7  9  3  1
dp:      2  7 11 11 12
                     i
rob  1 + dp[2]=11 → 12  |   skip dp[3]=11  → 12 wins
```

**Result: 12** — rob houses 0, 2, 4: `2+9+1`. Note [3]: robbing house 3 looks fine alone but drags in dp[1]=7, so skipping wins. Each cell = best answer for the prefix up to that house.
