# 48 — Rotate Image

## Problem

Rotate an `n × n` matrix 90° clockwise, **in place**.

**Example:**
```text
1 2 3      7 4 1
4 5 6  →   8 5 2
7 8 9      9 6 3
```

## Walkthrough

Two moves, both in place: **transpose** (flip across the main diagonal, `i ↔ j`), then **reverse each row**. Check it on the corner: 1 at top-left ends top-right; transposed it's still top-left, reversing the row sends it top-right. ✓

**[1] start**
```text
1 2 3
4 5 6
7 8 9
rotate 90° clockwise, in place
```

**[2] transpose — swap matrix[i][j] with matrix[j][i] for i ≤ j**
```text
1 4 7
2 5 8
3 6 9
swapped pairs: (2,4), (3,7), (6,8) — the diagonal 1,5,9 never moves
```

**[3] reverse each row**
```text
7 4 1
8 5 2
9 6 3
each row flipped in place → done, rotated 90° clockwise
```

Why it works: transpose maps `(i, j) → (j, i)`; row reversal maps `(j, i) → (j, n−1−i)`. Composed: `(i, j) → (j, n−1−i)` — exactly the clockwise-rotation map. O(n²) time (every cell touched twice), O(1) extra space. For counter-clockwise: transpose then reverse each *column* instead.
