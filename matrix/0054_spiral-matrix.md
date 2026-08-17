# 54 — Spiral Matrix

## Problem

Walk an m×n matrix in spiral order (right, down, left, up, repeat).

**Example:**
```text
1 2 3
4 5 6
7 8 9
```
→ `[1,2,3,6,9,8,7,4,5]`

## Walkthrough

**Shrinking boundaries**: maintain `top/bottom/left/right` fences. Each lap peels the top row, right column, bottom row (reversed), left column (reversed) — then the fences move inward. Stop when fences cross.

**[1] the fences open at the edges**
```text
T ─────────
L  1 2 3  R
   4 5 6
   7 8 9
B ─────────
out: take top row 1,2,3 → T=1
```

**[2] right column, top to bottom**
```text
   1 2 3 ✓
L  4 5 6  R
   7 8 9
out += 6, 9 → R=1
```

**[3] bottom row, right to left (only if B > T)**
```text
   1 2 3 ✓
   4 5 6 ✓
   7 8 9 ←
out += 8, 7 → B=1
```

**[4] left column upward (only if L < R)**
```text
   1 2 3 ✓
L→ 4 5 ✓
   7 8 9 ✓
out += 4 → L=1;  inner pass begins
```

**[5] inner cell — fences collapse**
```text
   ✓ ✓ ✓
   ✓ 5 ✓
   ✓ ✓ ✓
out += 5 → done: [1,2,3,6,9,8,7,4,5]
```

Why the two guards: single rows/columns at the end of odd dimensions would otherwise be walked **twice** (once as "top", again as "bottom") — `if top <= bottom` on the leftward walk and `if left <= right` on the upward walk prevent the double-count. O(m·n), each cell visited once.
