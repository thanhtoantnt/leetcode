# 66 — Plus One

## Problem

The number as a big-endian digit array — add one.

**Example:** `[1,2,3]` → `[1,2,4]`; `[9,9]` → `[1,0,0]`

## Walkthrough

Grade-school carry, single addend: walk from the last digit; a digit < 9 just increments and stops; a 9 becomes 0 and the carry ripples left. If every digit was 9, a 1 is prepended.

**[1] [1,2,3] — no ripple**
```text
[1, 2, 3]
       +1 → 4 < 10 → [1,2,4] done
```

**[2] [1,2,9] — one ripple**
```text
[1, 2, 9] → 9→0 carry → 2+1=3 stop → [1,3,0]
```

**[3] [9,9] — full ripple**
```text
[9, 9] → [0,0] + leftover carry → [1,0,0]
```

**[4] the only growth case**
```text
all nines is the only input whose output is longer — the carry walks
off the left end, so prepend 1
```

Why it works: adding 1 can only produce carries where digits are 9 — the loop's early return encodes "first non-9 absorbs the carry," which is exactly the arithmetic. O(n) worst case (all nines), O(1) typical. The one-digit sibling of 0002's full adder (linked_list/) and 0043's multiplication (maths/).
