# 202 — Happy Number

## Problem

Replace the number by the sum of squared digits, repeatedly. Does it reach 1 (happy), or cycle forever (unhappy)?

**Example:** `19` → `1²+9²=82 → 68 → 100 → 1` → happy. `2` → cycles.

## Walkthrough

The iteration is a **functional graph** `x → step(x)` — either it hits 1 or enters a cycle (values are bounded: a d-digit number maps below 81d, so the orbit can't escape). Cycle detection is Floyd's: slow steps once, fast twice; equal-but-not-1 means a cycle.

**[1] 19: 82, 68, 100, 1 — happy**
```text
19 → 82 → 68 → 100 → 1 ✓ fast reaches 1 → True
```

**[2] 2 enters the famous cycle**
```text
2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 (cycle!)
```

**[3] tortoise/hare on the unhappy orbit**
```text
slow: 2, 4, 16, 37 …
fast: 4, 16, 37, 89 …  they meet inside the cycle, never at 1 → False
```

**[4] why bounded orbits guarantee termination of the test**
```text
every value above 999 maps below 243 → the orbit lives in a finite
set → pigeonhole forces either 1 or a repeat (cycle)
```

**[5] the alternative**
```text
a seen-set answers the same question in O(n) memory; Floyd does it
with two integers — the linked-list-cycle trick (0141, linked_list/)
applied to an implicit list
```

Why it works: any deterministic iteration on a finite state space is eventually periodic — reaching 1 is the only absorbing happy state, so the question reduces to "which cycle?", which tortoise/hare answers in O(1) space. Same machinery as 0287's duplicate hunt (find the cycle entry) — here only membership in the 1-cycle matters.
