# 73 — Set Matrix Zeroes

## Problem

If a cell is 0, set its entire row and column to 0 — **in place**, ideally O(1) extra.

**Example:**
```text
1 1 1        1 0 1
1 0 1   →    0 0 0
1 1 1        1 0 1
```

## Walkthrough

The trick is **using row 0 and column 0 as the marker space**: first sweep finds zeros and marks their existence *in the border* (col0[j] = 0 for a zero in column j, etc.), keeping one flag for the `matrix[0][0]` overlap. A second sweep (skipping the borders) zeros cells based on markers. Last, the borders themselves are zeroed from the flags.

**[1] the zero at (1,1) — mark its row and column heads**
```text
1 1 1
1 0 1
1 1 1
row0 markers: [.,0,.]  col0 flag: rows 1 zero → matrix[1][0]=0
```

**[2] markers recorded (border cells darkened = "has a zero")**
```text
1 0 1
0 0 1
1 1 1
row 0's middle mark = column 1 must die;  (1,0)=0 = row 1 must die
```

**[3] interior pass — read markers, write zeros**
```text
1 0 1
0 0 0
1 0 1
for each cell (i,j), i,j ≥ 1: zero it if matrix[i][0]==0 or matrix[0][j]==0
```

**[4] border pass finishes**
```text
1 0 1
0 0 0
1 0 1
row 0 had a mark → zero row 0's cells (except marker col? no: whole row);  done ✓
```

Why two passes: zeroing while scanning would cascade — a freshly-written zero would nuke its own row/column, wrongly infecting the matrix. Marking first, writing second separates *detection* from *action*. O(1) extra comes from the border-as-scratch-space idea; the O(m+n) row/col-flag-array version is the same algorithm with explicit markers.
