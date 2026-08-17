# 72 — Edit Distance

## Problem

Minimum number of insert / delete / replace operations to transform `word1` into `word2`.

**Example:** `word1 = "horse"`, `word2 = "ros"` → `3` (horse → rorse → rose → ros)

## Walkthrough

2-D table: `dp[i][j]` = distance between the first i letters of "horse" (rows) and first j of "ros" (cols; col 0 = empty). Matching letters take the diagonal free; a mismatch costs 1 + the best of left (insert), up (delete), diagonal (replace).

**[1] seeds: transforming to/from empty**
```text
:  0 1 2 3
h: 1 . . .
o: 2 . . .
r: 3 . . .
s: 4 . . .
e: 5 . . .
cols = r o s (col 0 = empty)  row i seed = i deletes; col j = j inserts
```

**[2] row h — h vs r mismatches**
```text
:  0 1 2 3
h: 1 1 2 3
o: 2 . . .
r: 3 . . .
s: 4 . . .
e: 5 . . .
dp[1][1] = 1+min(1,1,0) = 1: replace h→r
```

**[3] rows o, r — a diagonal freebie appears**
```text
:  0 1 2 3
h: 1 1 2 3
o: 2 2 1 2
r: 3 2 2 2
s: 4 . . .
e: 5 . . .
h-vs-o matched o at dp[2][2] = dp[1][1] = 1 (no cost)
```

**[4] rows s, e**
```text
:  0 1 2 3
h: 1 1 2 3
o: 2 2 1 2
r: 3 2 2 2
s: 4 3 3 2
e: 5 4 4 3
dp[5][3] = dp[4][2]+1 = 3 → answer 3
```

**[5] read back the ops**
```text
horse → rorse (replace h) → rose (delete r) → ros (delete e) = 3 ops
```

Why it works: the last alignment of word1[i−1] and word2[j−1] is either a match (pay nothing, shrink both) or one of three edits (each shrinking one or both) — exhaustive and disjoint cases, the LCS-family recurrence (1143, this folder) with costs attached. O(m·n).
