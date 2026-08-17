# 51 — N-Queens

## Problem

Place `n` queens on an n×n board, none attacking another (no shared row, column, or diagonal). Return all distinct boards.

**Example:** `n = 4` → 2 solutions.

## Walkthrough

One queen per row (forced), so the search is: for each row, try each column not attacked. Three sets kill conflicts in O(1): occupied `cols`, occupied **↗ diagonals** (`r−c` constant), occupied **↘ diagonals** (`r+c` constant). Dead row → backtrack.

**[1] row 0: try column 0**
```text
row: 0 1 2 3
cols={0} d1={0} d2={0}
```

**[2] row 1: column 2 survives (0,1 blocked)**
```text
cols={0,2} d1={0,3} d2={−1,3}
```

**[3] row 2: every column dies**
```text
c=1: d1 hit (1+1=2? blocked via col 1∈cols? col1 free but 2+1=3 ∈ d1 ✗)
c=3: col 3 free, 2+3=5 ∉ d1, 2−3=−1 ∈ d2 ✗ → backtrack
```

**[4] pop back — row 0 tries column 1**
```text
the 0-start subtree is exhausted; the surviving first queen is col 1
(or 2 by symmetry) — the search continues to the two known boards
```

**[5] a solution, rendered**
```text
.Q..
...Q
Q...
..Q.
```

Why it works: rows partition the placement (exactly one queen each), so the choice per level is just the column — and the three integer sets are complete certificates of safety, since two cells share a diagonal iff their `r+c` or `r−c` matches. Sets update in O(1) and restore on backtrack — the include/exclude discipline of 0046's permutations (this folder) with geometry as the pruning oracle. Exponential search tamed by early pruning; n=4 → 2 boards, n=8 → 92.
