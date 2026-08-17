# 115 — Distinct Subsequences

## Problem

Count the subsequences of `s` that equal `t` (occurrences counted by position).

**Example:** `s = "babgbag"`, `t = "bag"` → `5`

## Walkthrough

`dp[i][j]` = ways to build `t[:j]` from `s[:i]`. When trailing letters match, the last t-letter may be served by this s-letter (`diagonal`) **or** the s-letter skipped (`above`); mismatch → only skip. Empty `t` column is all 1s (delete everything).

**[1] seed row: empty t formable one way**
```text
      t:  b  a  g
 ε:      1  0  0
```

**[2] consume s = b, a**
```text
b:  1  1  0  0     match b: 0 + 1
a:  1  1  1  0     match a: 0 + 1
```

**[3] second b — the branching begins**
```text
b:  1  2  1  0     'b' now formable 2 ways (either b)
```

**[4] g locks a subcount**
```text
g:  1  2  1  1     'bag' × 1: b(first) a g
```

**[5] tail: b, a, g — totals accumulate**
```text
b:  1  3  1  1     'b' ×3
a:  1  3  4  1     'ba' ×4 = every b × this a
g:  1  3  4  5     'bag' ×5 ✓ each earlier 'ba' pairs with this g
```

Why it works: every occurrence assigns t's letters to distinct, order-preserving s-positions — classifying by whether s's last letter serves t's last letter splits the count exhaustively; the empty-t column seeds the deletion base case. Same table geometry as 1143 LCS (this folder), counting instead of maximizing. The reverse inner loop rolls one row: O(m·n) time, O(n) space.
