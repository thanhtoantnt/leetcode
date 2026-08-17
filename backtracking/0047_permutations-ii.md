# 47 — Permutations II

## Problem

Return all **unique** permutations of integers that may contain duplicates.

**Example:** `nums = [1,1,2]` → `[[1,1,2],[1,2,1],[2,1,1]]` — only 3, not 3! = 6.

## Walkthrough

Same backtracking skeleton as 46, but candidates come from a **Counter** instead of a used-list: iterate over the *distinct* values, and only those with count left. Duplicates can't produce identical branches because there's exactly one branch per distinct value — multiplicity is consumed via the counter, not by position.

**[1] counts: 1→2, 2→1**
```text
perm=
count={1:2, 2:1}  level 0: try value 1
```

**[2] 1, then 1 again**
```text
perm=1,1
count={1:0, 2:1}  using the second 1 decrements the same counter
```

**[3] leaf [1,1,2]**
```text
perm=1,1,2 ✓
[1,1,2] recorded  → backtrack, pop both 1s
```

**[4] 1, then 2**
```text
perm=1,2
count={1:1, 2:0}  level 1 picks value 2 instead
```

**[5] leaves [1,2,1] and the 2-first subtree**
```text
perm=2,1,1 ✓
[1,2,1] [2,1,1]  three distinct leaves total
```

Why it works: permuting *multiset counts* collapses the duplicate positions of 46's approach — value 1 is one candidate regardless of which physical copy is used, so identical permutations are generated exactly once. The popular alternative (sort + skip `nums[i] == nums[i-1]` when `i-1` wasn't used) achieves the same with an index loop. O(n·n!) worst case, fewer leaves with duplicates.
