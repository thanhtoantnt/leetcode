# 155 — Min Stack

## Problem

A stack supporting `push`, `pop`, `top`, and `getMin` — all O(1).

**Example:** push 5, 3, 7 → `getMin()` = 3; pop (7), pop (3) → `getMin()` = 5

## Walkthrough

**Stack of pairs**: each entry carries its value *and* the minimum of everything below-or-including it. The min question at any depth is then just the top's second field — history frozen at push time.

**[1] push 5**
```text
(5, 5)
min-so-far 5  new pair: (value, min(5, below's 5))
```

**[2] push 3 — the min drops**
```text
(5, 5) (3, 3)
getMin = top.second = 3  ✓ O(1)
```

**[3] push 7 — min unchanged**
```text
(5, 5) (3, 3) (7, 3)
7 > 3 → pair records (7, 3)
```

**[4] pop 7, pop 3 — min restores automatically**
```text
(5, 5) (3, 3) (7, 3)
pop → (5,5)(3,3) → getMin 3;  pop → (5,5) → getMin 5 ✓
```

**[5] why not just one extra min variable?**
```text
a single min=3 dies when 3 is popped — 5 was already pushed
the pair-per-entry is the memo of "min of the world when I arrived"
```

Why it works: `getMin` at depth d only ever asks "minimum of the bottom d+1 values" — which each entry computed at push time from the entry below. Pops discard exactly the entry whose min it was; no recomputation. O(1) per op, O(n) space (a second parallel stack of running mins is the same idea split in two).
