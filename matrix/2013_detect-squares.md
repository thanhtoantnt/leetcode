# 2013 — Detect Squares

## Problem

Support `add(point)` and `count(point)` — how many axis-aligned squares formed entirely from added points contain the query point as a **corner**?

**Example:** add (3,10), (11,2), (3,2) → `count([11,10])` = `1`; adding (11,2) again makes it `2`.

## Walkthrough

A square containing query `p` has its **diagonal corner** `(x,y)` at equal taxicab offsets: `|x−px| = |y−py| > 0`. Each stored point that qualifies fixes the whole square — the other two corners are `(x, py)` and `(px, y)`, and counting them is a pair of map lookups multiplied together.

**[1] the three stored points**
```text
(3,10)  (11,2)  (3,2)      query p = (11,10)
```

**[2] scan for diagonal candidates**
```text
(3,10): |3−11| = 8 ≠ |10−10| = 0 ✗ (same row)
(11,2): same column ✗
(3,2):  |3−11| = 8 = |2−10| = 8 ✓ diagonal!
```

**[3] the fixed square's other corners**
```text
corner3 = (3, 10) = (x, py) → cnt 1
corner4 = (11, 2) = (px, y) → cnt 1
contribution = 1 × 1 = 1 ✓
```

**[4] duplicates multiply**
```text
add (11,2) again → cnt[(11,2)] = 2 → (3,2)'s square counts twice,
and (11,2) as diagonal… (same column, skipped) → count = 2 ✓
```

**[5] why every candidate is independent**
```text
each diagonal point specifies a DISTINCT square; products combine
multiplicities of the two fill-in corners — sum over diagonals = total
```

Why it works: a square is determined by one diagonal — two points at equal |Δx| = |Δy| — so enumerating stored points as potential diagonals and *computing* (never searching for) the other two corners covers every square exactly once, with the count map absorbing duplicates. add O(1), count O(n) per query. Geometry as hashing: no plane sweep needed at this scale.
