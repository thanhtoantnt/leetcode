# 97 — Interleaving String

## Problem

Is `s3` an interleaving of `s1` and `s2` — formed by merging them while preserving each one's internal order?

**Example:** `s1 = "aab"`, `s2 = "axy"`, `s3 = "aaxaby"` → `true`

## Walkthrough

2-D DP over consumed prefixes: `dp[i][j]` = can the first `i` chars of s1 and first `j` of s2 weave the first `i+j` of s3? Each cell pulls from its **left** (s1 supplied the next char) or **above** (s2 did), gated by character match.

**[1] seeds: empty prefixes**
```text
s2:    a  x  y
   1  .  .  .
a  .  .  .  .
a  .  .  .  .
b  .  .  .  .
dp[0][0]=1  empty+empty = empty ✓
```

**[2] first row/column: single-source prefixes**
```text
s2:    a  x  y
   1  1  1  1
a  1  .  .  .
a  1  .  .  .
b  1  .  .  .
dp[0][j]=1 while s2[j-1]==s3[j-1] — same down the column for s1
```

**[3] interior cell dp[1][1] — either source**
```text
s2:    a  x  y
   1  1  1  1
a  1  2  .  .
a  1  .  .  .
b  1  .  .  .
s3='a' next: s1 'a' matches (from above ✓) or s2 'a' matches (from left ✓)
```

**[4] propagate reachable cells (✓ = reachable)**
```text
s2:    a  x  y
   ✓  ✓  ✓  ✓
a  ✓  ✓  ✓  ✓
a  ✓  ✓  ✓  ✓
b  ✓  ✓  ✓  ✓
all reachable — dp[3][3]=1 → True
```

**[5] a false case: s3="abyxaa"**
```text
s2:    a  x  y
   ✓  ✓  ✗  ✗
a  ✓  ✓  ✗  ✗
a  ✓  ✓  ✗  ✗
b  ✓  ✓  ✗  ✗
s3 wants 'y' at position 3; neither s1 nor s2 offers it there → False
```

Why it works: an interleaving consumes s3 one char at a time, each char attributable to s1 or s2 — so (i, j) states with i+j consumed are exactly the reachable positions, and edges are the character-match gates. O(m·n) cells, O(n) space with a rolling row. Greedy matching fails: equal leading letters must sometimes be charged to the *other* string.
