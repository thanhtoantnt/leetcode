# 37 — Sudoku Solver

## Problem

Fill the 9×9 board in place so every row, column, and 3×3 box holds 1–9 exactly once. (0036 checked validity; this completes the board.)

**Example:** the classic puzzle → its unique solution.

## Walkthrough

Backtracking over the **empty cells only** (pre-listed), with 0036's three set families (`rows`, `cols`, `boxes` with `3·(r/3) + c/3`) as an O(1) safety oracle: try a digit, mark it in the three sets, recurse; contradiction → unmark and try the next.

**[1] the sets from the givens**
```text
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
rows[0]={5,3,7} … boxes[0]={5,3,6,9,8} … empties=[(0,2), (0,3), …]
```

**[2] first empty cell (0,2) — candidates**
```text
row 0 missing {1,2,4,6,8,9}; col 2 has {8}; box 0 has {5,3,6,9,8}
→ try 4 first (order doesn't matter, solution unique)
```

**[3] dive or backtrack**
```text
place 4: rows/cols/boxes updated, recurse to (0,3) …
a dead cell (no candidate) → unwind to the last choice, next digit
```

**[4] the completion test**
```text
i == len(empties) — all 51 holes filled with no conflict → True
bubbles up through every frame, board left fully written ✓
```

**[5] cost**
```text
worst case exponential (constraint satisfaction is NP-hard in general),
but the three-set oracle prunes so hard that 9×9 solves in milliseconds
```

Why it works: each assignment's safety is checkable locally (row/col/box), so DFS over digits with immediate pruning explores exactly the consistent prefixes — completeness comes from trying all nine digits at every hole. Pre-listing empties skips the givens entirely; the sets make each test O(1) versus rescanning 27 units. The design pattern behind every "fill the grid" CSP (eight queens 0051, this folder, is the same skeleton without the box sets).
