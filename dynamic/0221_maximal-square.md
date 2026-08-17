# 221 — Maximal Square

## Problem

Largest square of 1s in a binary matrix — return its **area**.

**Example:**
```text
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```
→ `4` (the 2×2 block in the middle-right)

## Walkthrough

`dp[r][c]` = side length of the biggest **all-1s square whose bottom-right corner is (r,c)**. A 1-cell grows its neighbors' squares: `dp = 1 + min(up, left, up-left)` — three squares must all be big enough to surround the new corner. The answer is the max side, squared.

**[1] first row/column: squares of side 1**
```text
1 0 1 0 0
1 . . . .
1 . . . .
1 . . . .
every '1' with no room above/left is a 1×1
```

**[2] the (1,3) corner: neighbors are 0,0,1**
```text
dp(1,3) = 1 + min(0,0,1) = 1  a square needs ALL three sides
```

**[3] the (1,4) corner: 0,1,1 → still 2**
```text
dp(1,4) = 1 + min(0,1,1) = 1  the 0 above caps it
```

**[4] row 2: the real square forms**
```text
row2: dp(2,3) = 1 + min(dp(1,2)=1, dp(1,3)=1, dp(2,2)=1) = 2 ✓
      dp(2,4) = 1 + min(dp(1,3)=1, dp(1,4)=1, dp(2,3)=2) = 2
best side = 2 → area 4
```

**[5] the three-neighbor rule, visually**
```text
■ ■        ■ ■        ■ ■ ■
■ ?   +    ■ ■   →    ■ ■ ■   the corner extends only if all three
                          ■   adjacent squares can back it up
```

Why it works: a k×k square ending at (r,c) exists iff its three overlapping (k−1)-predecessors exist (up, left, diagonal) and the cell is 1 — exactly the min recurrence. Each cell computed once: O(m·n); one rolling row gives O(n) space. Compare 0063/0062 (path counting, this folder): same table geometry, min instead of sum. The maximal-**rectangle** variant is 0084's stack (stacks/).
