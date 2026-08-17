# 46 — Permutations

## Problem

Return all permutations of distinct integers.

**Example:** `nums = [1,2,3]` → `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

## Walkthrough

Backtracking: build a permutation one slot at a time. At each level, try every not-yet-used number, recurse, then undo the choice (`pop`) so the next candidate starts clean. Used elements are tracked live in `perm` itself.

**[1] level 0 — try 1 first**
```text
perm=1
├─R 1 chosen  2 candidates left
```

**[2] level 1 — then 2**
```text
perm=1,2
├─L 1
│  ├─R 2 chosen
```

**[3] level 2 — 3 completes a leaf**
```text
perm=1,2,3 ✓
├─L 1
│  ├─R 2
│  │  └─R 3 → [1,2,3] recorded
```

**[4] backtrack — pop back to level 1**
```text
perm=1
├─L 1
│  ├─R 2 ✗ undone
│  └─R 3 next  → then 2 → [1,3,2]
```

**[5] back to level 0 — swap in candidate 2**
```text
perm=2
├─R 2 chosen  whole subtree of 1 exhausted (2 permutations)
```

**[6] the full tree — 3! = 6 leaves**
```text
[1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]
✓ all 6  each level picks from the remaining values
```

Why it works: the recursion enumerates exactly the sequences of distinct choices — length n over n options = n! leaves — and the pop after each recursive call restores state so siblings explore their own branches. O(n·n!) time (n! permutations, n work to copy each). Same skeleton as the combination-sum flipbook in this folder.
