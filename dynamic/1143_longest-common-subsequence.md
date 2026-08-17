# 1143 — Longest Common Subsequence

## Problem

Given two strings, return the length of their longest common **subsequence** — the longest sequence appearing in both, in order, not necessarily contiguous.

**Example:** `text1 = "abcde"`, `text2 = "ace"` → `3` (`"ace"`)

## Walkthrough

2D DP: `dp[i][j]` = LCS length of the first `i` chars of `abcde` (rows) vs the first `j` chars of `ace` (columns; column 0 = empty prefix). Match → take diagonal + 1; else max of above and left.

Cells fill row by row; a match cell lights up when the two current letters agree.

**[1] row a — matches the first column**
```text
a: 0 1 1 1
b: . . . .
c: . . . .
d: . . . .
e: . . . .
cols = a c e (col 0 = empty)   dp[1][1] = dp[0][0]+1 = 1: 'a' == 'a'
```

**[2] row b — no matches, inherit max**
```text
a: 0 1 1 1
b: 0 1 1 1
c: . . . .
d: . . . .
e: . . . .
cols = a c e (col 0 = empty)   'b' matches nothing → copy best of up/left
```

**[3] row c — matches the 'c' column**
```text
a: 0 1 1 1
b: 0 1 1 1
c: 0 1 2 2
d: . . . .
e: . . . .
cols = a c e (col 0 = empty)   dp[3][2] = dp[2][1]+1 = 2: 'c' == 'c'
```

**[4] row d — carry through**
```text
a: 0 1 1 1
b: 0 1 1 1
c: 0 1 2 2
d: 0 1 2 2
e: . . . .
cols = a c e (col 0 = empty)   no matches → values flow right
```

**[5] row e — final match**
```text
a: 0 1 1 1
b: 0 1 1 1
c: 0 1 2 2
d: 0 1 2 2
e: 0 1 2 3
cols = a c e (col 0 = empty)   dp[5][3] = dp[4][2]+1 = 3: 'e' == 'e' → answer 3
```

Why it works: each cell only needs the row above and the cell to the left, so one pass over an m×n table suffices — O(m·n). Reading matches backward from the corner recovers the subsequence itself.
