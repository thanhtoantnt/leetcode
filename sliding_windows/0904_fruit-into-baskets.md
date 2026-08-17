# 3-family — 904 — Fruit Into Baskets

## Problem

Rows of fruit trees, each one type; two baskets, each holds **one type** unlimited. Walk a contiguous row and collect from every tree — max row length with at most 2 distinct types.

**Example:** `fruits = [1,2,3,2,2]` → `4` (`[2,3,2,2]`)

## Walkthrough

This is "longest substring with at most 2 distinct characters" — problem 3's window mechanics with the dict capped at size 2. Grow the right edge; when a third type appears, shrink from the left until one type is fully gone.

**[1] window [1]**
```text
[1, 2, 3, 2, 2]
 L  R
count={1:1}  one type — fine
```

**[2] window [1,2]**
```text
[1, 2, 3, 2, 2]
 L     R
count={1:1, 2:1}  two types — still legal
```

**[3] 3 arrives — a third type: shrink**
```text
[1, 2, 3, 2, 2]
       L  R
count={2:1, 3:1}  evict 1 (count 0 → gone), 3 enters — window [2,3]
```

**[4] extend through the 2s**
```text
[1, 2, 3, 2, 2]
       L     R
count={2:3, 3:1}  best = 4
```

**[5] answer**
```text
best=4  return 4 — the run [2,3,2,2]
```

Why it works: the window invariant "≤ 2 distinct types" defines exactly the legal rows, and right-edge-advance + left-shrink repairs it minimally — each index enters and leaves the window at most once, O(n). The counter dict is problem 3's flipbook (in this folder) with `k=2`; generalizing to k types is 340.
