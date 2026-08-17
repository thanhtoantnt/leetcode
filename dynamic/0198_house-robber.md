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
dp[0]=2 dp[1]=7
```

**[2] i=2 — rob 9+2=11 vs skip 7 → 11**
```text
houses:  2  7  9  3  1
dp:      2  7 11  .  .
               i
```

**[3] i=3 — rob 3+7=10 vs skip 11 → skip wins**
```text
houses:  2  7  9  3  1
dp:      2  7 11 11  .
                  i
```

**[4] i=4 — rob 1+11=12 vs skip 11 → 12**
```text
houses:  2  7  9  3  1
dp:      2  7 11 11 12
                     i
```

**Result: 12** — rob houses 0, 2, 4: `2+9+1`. At i=3, robbing house 3 looks fine alone but only yields 10, so skipping wins. Each cell = best answer for the prefix up to that house.
