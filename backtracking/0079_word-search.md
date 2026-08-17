# 79 — Word Search

## Problem

Given an `m × n` grid of letters, can the word be traced as a path of adjacent (up/down/left/right) cells, using each cell **at most once**?

**Example:** grid below, `word = "ABCCED"` → `true`

## Walkthrough

Try every cell as the start; from each, DFS matching one letter at a time. The visited-cell constraint is handled by **temporarily overwriting the cell** with `#` — no separate visited set, and the restore on backtrack undoes it.

```text
A B C E
S F C S
A D E E
```

**[1] start at the A at (0,0)**
```text
A B C E
S F C S
A D E E
k=0  A matches word[0] → mark (0,0) and look for B among neighbors
```

**[2] B found right**
```text
# B C E
S F C S
A D E E
k=1  (0,1)=B ✓ → mark, look for C
```

**[3] C at (0,2)**
```text
# # C E
S F C S
A D E E
k=2  (0,2)=C ✓ → next C must be adjacent: (1,2)
```

**[4] second C dives down**
```text
# # # E
S F # S
A D E E
k=3  (1,2)=C ✓ → E next: (2,2)
```

**[5] E, then D — word complete**
```text
# # # E
S F # S
A # # #
k=5  (2,2)=E ✓ then (2,1)=D ✓ → return True
```

Why it works: `#` marks make the current path unwalkable for deeper cells (each cell used once), and un-marking on the way out lets sibling branches reuse the cells differently. Worst case O(m·n · 3^L) — 3 because you never walk back onto the cell you came from (unless marks force it). This is DFS path-finding (CLRS Ch. 22) with an exact-match constraint.
