# 39 — Combination Sum

## Problem

Given distinct integers `candidates` and a `target`, return every unique combination that sums to `target`. A number may be chosen unlimited times. Order does not matter (`[2,3]` and `[3,2]` are the same).

**Example:** `candidates = [2, 3, 5]`, `target = 8` → `[[2,2,2,2], [2,3,3], [3,5]]`

## Walkthrough

Each frame grows the decision tree one node. Children may only use candidates at or after the current index (no looking back → no duplicate combos). `rem` = remaining target. The `.py` next door solves it with a dp-table variant — this tree is the canonical backtracking view.

**[1] root**
```text
[] rem=8
```

**[2] try 2**
```text
[] rem=8
└─ 2 rem=6
```

**[3] go deeper: 2→2→2→2 hits 0 ✓**
```text
[] rem=8
└─ 2 rem=6
   └─ 2 rem=4
      └─ 2 rem=2
         └─ 2 rem=0 ✓ [2,2,2,2]
```

**[4] backtrack, siblings of the deepest 2: 3, 5 both overshoot ✗**
```text
[] rem=8
└─ 2 rem=6
   └─ 2 rem=4
      └─ 2 rem=2
         ├─ 2 rem=0 ✓ [2,2,2,2]
         ├─ 3 rem=-1 ✗
         └─ 5 rem=-3 ✗
```

**[5] backtrack two levels: 2→2→3 and 2→2→5**
```text
[] rem=8
└─ 2 rem=6
   └─ 2 rem=4
      ├─ 2 rem=2
      │  ├─ 2 rem=0 ✓ [2,2,2,2]
      │  ├─ 3 rem=-1 ✗
      │  └─ 5 rem=-3 ✗
      ├─ 3 rem=1          (no candidate ≤ 1 → dead end)
      └─ 5 rem=-1 ✗
```

**[6] full tree — all solutions found**
```text
[] rem=8
├─ 2 rem=6
│  ├─ 2 rem=4
│  │  ├─ 2 rem=2
│  │  │  ├─ 2 rem=0 ✓ [2,2,2,2]
│  │  │  ├─ 3 rem=-1 ✗
│  │  │  └─ 5 rem=-3 ✗
│  │  ├─ 3 rem=1   dead
│  │  └─ 5 rem=-1  ✗
│  ├─ 3 rem=3
│  │  └─ 3 rem=0 ✓ [2,3,3]
│  └─ 5 rem=1      dead
├─ 3 rem=5
│  ├─ 3 rem=2      dead
│  └─ 5 rem=0 ✓ [3,5]
└─ 5 rem=3
   └─ 5 rem=-2 ✗
```

**Result: `[[2,2,2,2], [2,3,3], [3,5]]`**

The invariant: `rem` decreases at every edge; once negative, the whole subtree is cut (sorted candidates → every deeper node is worse). Backtrack = pop, try next sibling.
