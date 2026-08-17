# 74 — Search a 2D Matrix

## Problem

An m×n matrix where each row is sorted and each row's first element exceeds the previous row's last. Search for `target` efficiently.

**Example:** matrix below, `target = 16` → `true`

## Walkthrough

Flattened, the matrix is one sorted array — so binary search works directly, with index math mapping a virtual 1D index to `(row, col)`: `row = idx // n`, `col = idx % n`.

```text
1  3  5  7
10 11 16 20
23 30 34 60
```

**[1] virtual array of 12, mid = 5**
```text
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
 L        M                           H
lo=0 hi=11 mid=5  flat[5]=row 1, col 1 = 11 < 16 → lo=6
```

**[2] mid = 8**
```text
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
                       L    M              H
lo=6 hi=11 mid=8  flat[8]=row 2 col 0 = 23 > 16 → hi=7
```

**[3] mid = 6 — found**
```text
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
                       LM  H
lo=6 hi=7 mid=6  flat[6]=row 1 col 2 = 16 ✓ return True
```

Why it works: the row-major flattening is sorted (row-sorted rows, rows in increasing ranges), so the virtual index space has full ordering — one binary search, O(log(m·n)), no allocation. Two-search variant (binary search the row by first elements, then within the row) is the same complexity with more code.
