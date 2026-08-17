# 36 — Valid Sudoku

## Problem

A 9×9 board is valid if every row, every column, and every 3×3 box contains the digits 1–9 **at most once** (empty cells `.` are fine). Detect duplicates.

**Example board (contains a violation — row 0 has two 8s, and the top-left box gets two 8s):**

## Walkthrough

One pass over all 81 cells, tracking three families of seen-sets: `rows[9]`, `cols[9]`, `boxes[9]`. The box index is computed as `3·(r/3) + c/3`.

**[1] the board — the clash is at (2,3)**
```text
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
scanning  an 8 already sits at (0,2)
```

**[2] (0,2) = 8 recorded**
```text
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
rows[0]+={8}  cols[2]+={8}  box=3·0+2/3=0 → boxes[0]+={8}
```

**[3] the violator at (2,2) — wait for the scan to reach it**
```text
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
cell (2,2)=8  box index = 3·(2/3) + 2/3 = 0 — same box as (0,2)
```

**[4] duplicate detected**
```text
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
8 ∈ boxes[0] → return False
```

Why the box formula: `3·(r/3) + c/3` maps the nine 3×3 blocks to indices 0–8 row-major — `(0,2)` and `(2,2)` both land in box 0, while `(4,3)` lands in box 4. One pass, 27 sets, O(81) time. (Solving the board is a different problem — that's backtracking, problem 37.)
