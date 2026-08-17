# 90 — Subsets II

## Problem

Return all unique subsets of integers **that may contain duplicates**.

**Example:** `nums = [1,2,2]` → `[[],[1],[1,2],[1,2,2],[2],[2,2]]` — not the 8 of problem 78.

## Walkthrough

Sort first, then reuse the include/exclude tree with one guard: **when skipping duplicates, skip the whole run** — if you're at `nums[i]` and it equals `nums[i-1]`, you may only start a new branch from the *first* copy. Sorting puts equal values adjacent so the guard is a one-line check.

**[1] sorted: [1,2,2] — take 1, take first 2**
```text
perm=1,2
├─L 1
│  ├─R take 2(1st)  second 2 still available below
```

**[2] the deepest path uses both 2s**
```text
perm=1,2,2 ✓
├─L 1
│  ├─L 2(1st)
│  │  ├─R take 2(2nd) → [1,2,2]
```

**[3] skip the second 2 — but only via its own branch**
```text
perm=1
├─L 1
│  ├─R 2(2nd) ✗ blocked: nums[i]==nums[i-1]
```

The block matters: branching from the *second* 2 would rebuild `[1,2]` and `[1,2,2]` — the exact subsets the first 2's subtree already owns.

**[4] the 2-first subtree, same rule inside**
```text
perm=2,2 ✓
├─R 2(1st)
│  ├─R take 2(2nd) → [2,2]; skip → [2]
```

**[5] the six unique subsets**
```text
[] [1] [1,2] [1,2,2] [2] [2,2]
✓ 6 not 8  duplicates pruned at the branch point, not filtered after
```

Why it works: with equal values adjacent, "first copy may branch, later copies may not" makes each distinct *multiset* reachable by exactly one path. Pruning during generation beats deduplicating 2ⁿ results afterwards — output size is ~2^(distinct runs) instead of 2ⁿ.
