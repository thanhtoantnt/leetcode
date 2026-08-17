# 76 — Minimum Window Substring

## Problem

Smallest window in `s` containing all characters of `t` (with multiplicity), or `""`.

**Example:** `s = "ADOBECODEBANC"`, `t = "ABC"` → `"BANC"`

## Walkthrough

The canonical two-phase window. **Expand right** until the window covers t; then **contract left** as far as coverage allows, recording the best. `have`/`need` counters make coverage O(1) to test.

**[1] grow to the first cover**
```text
[A, D, O, B, E, C, O, D, E, B, A, N, C]
 L           R
have=3/3 ✓  "ADOBEC" covers A,B,C → start contracting
```

**[2] contract — dropping the A breaks it**
```text
[A, D, O, B, E, C, O, D, E, B, A, N, C]
    L        R
best=6  s[0]=A leaves → have=2 ✗ → grow again
```

**[3] regrow to A at index 10**
```text
[A, D, O, B, E, C, O, D, E, B, A, N, C]
    L                          R
have=3/3 ✓  "DOBECODEBA" — covered (B and C inside)
```

**[4] contract through the filler**
```text
[A, D, O, B, E, C, O, D, E, B, A, N, C]
                              L  R
D,O,B(no—B(9) still covers),E,C… left stops at B(9): window "BANC"? —
step-by-step: drop D,O (unneeded), B(3) (B(9) remains), E, C(5) ✗ →
stop at L=5, window "CODEBA" (6) — no improvement, keep growing
```

**[5] final C at 12 enables the hard contraction**
```text
[A, D, O, B, E, C, O, D, E, B, A, N, C]
                              L     R
C(12) doubles the C count → C(5) dropable → sweep left to B(9):
window "BANC" (4) ✓ best=4 → done, return "BANC"
```

Why it works: every minimal window is tight on both sides — expand finds a right edge that admits a cover, contract finds the leftmost edge that keeps it, so each cover's tight form is visited. `have` counts letters meeting required multiplicity, so both phases are O(1) per step → O(|s| + |t|) overall. The deque-free twin of problem 3's fixed-condition window (same folder).
