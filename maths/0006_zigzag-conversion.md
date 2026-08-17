# 6 — Zigzag Conversion

## Problem

Write a string in zigzag rows, then read **row by row**. Rows bounce between top and bottom.

**Example:** `s = "PAYPALISHIRING"`, `numRows = 3` → `"PAHNAPLSIIGYIR"`

## Walkthrough

Simulate the pen: walk the string once, tracking `row` and `step` (+1 going down, −1 bouncing up). Append each char to its row's bucket; **reverse step at the rails** (row 0 and row n−1).

```text
P   A   H   N        row 0
A P L S I I G        row 1
Y   I   R            row 2
```

**[1] descending: P→A→Y**
```text
row=0 P  row=1 A  row=2 Y
step=+1  hit row 2 = bottom rail → step = −1
```

**[2] bounce: P, A, L back at top**
```text
row=1 P  row=0 A
step=−1  hit row 0 → step = +1;  L drops to row 1
```

**[3] second descent**
```text
row=2 I  row=1 S  …  row=2 I? recount below in buckets
```

Buckets by row after the full walk: row0 `PAHN`, row1 `APLSIIG`, row2 `YIR`.

**[4] concatenate rows**
```text
PAHN + APLSIIG + YIR → PAHNAPLSIIGYIR ✓
```

**[5] the numRows=2 sanity check**
```text
A C E
B D F  → ACEBDF — pure alternation, step flips every character
```

Why it works: the zigzag assigns characters to rows in a fixed period of 2·(n−1); the row/step simulation reproduces it in one O(len) pass without computing any index arithmetic (the closed form: char i lands on row `min(i mod 2(n−1), 2(n−1) − i mod 2(n−1))` — the simulation is easier to read than the formula).
