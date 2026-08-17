# 2 — Add Two Numbers

## Problem

Two non-negative numbers stored as reversed digit lists (head = least significant). Return their sum the same way.

**Example:** `(2 → 4 → 3) + (5 → 6 → 4)` = `342 + 465 = 807` → `(7 → 0 → 8)`

## Walkthrough

Grade-school addition, exactly as taught: digit by digit with a **carry**. Both lists plus the carry feed each position; the carry ripples rightward (into more significant digits).

**[1] units: 2 + 5**
```text
[2, 4, 3]
[5, 6, 4]
sum=7 carry=0  out: 7 →
```

**[2] tens: 4 + 6 = 10 — carry!**
```text
[2, 4, 3]
[5, 6, 4]
    i  j
sum=0 carry=1  out: 7 → 0 →
```

**[3] hundreds: 3 + 4 + carry 1**
```text
[2, 4, 3]
[5, 6, 4]
       i  j
sum=8 carry=0  out: 7 → 0 → 8
```

**[4] lengths equal, carry zero — done**
```text
out: 7 → 0 → 8  = 807 ✓ return head
```

**[5] the spill case: [5] + [5]**
```text
sum=0 carry=1  both lists exhausted but carry lives
out: 0 → 1  = 10 — the loop must continue while carry > 0
```

Why it works: reversed storage puts the least significant digit at the head, so addition's natural right-to-left order becomes a simple simultaneous head-to-tail walk. One position per iteration, O(max(m,n)) nodes. The carry check after both lists end is the only edge case people forget.
