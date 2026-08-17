# 78 — Subsets

## Problem

Return all subsets (the power set) of distinct integers.

**Example:** `nums = [1,2,3]` → `[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]`

## Walkthrough

The classic include/exclude recursion. At each index there's one binary decision — take `nums[i]` or skip it — so every subset corresponds to exactly one path down a binary tree. Recording `perm` at **every** node (not just leaves) collects them all.

**[1] at index 0 — include 1**
```text
perm=1
├─R take 1  ✗ = skip 1 (right subtree later)
```

**[2] under 1 — include 2**
```text
perm=1,2
├─L 1
│  ├─R take 2
```

**[3] deepest left path**
```text
perm=1,2,3 ✓
├─L 1
│  ├─L 2
│  │  ├─R take 3 → [1,2,3] recorded
```

**[4] skip branches peel values off**
```text
perm=1,3
├─L 1
│  ├─R 2 ✗ skipped
│  │  └─R take 3 → [1,3]
```

**[5] recorded along the way — every node is an answer**
```text
[] [1] [1,2] [1,2,3] [1,3] [2] [2,3] [3]
✓ 8 subsets = 2³  skip-0 leaves the empty path as []
```

Why it works: each element is independently in or out — 2^n binary decisions, each path one subset — so recording on entry into every node captures the whole power set exactly once. O(n·2ⁿ) time. Iterative variant: start with `[]` and for each number, double the list by appending it to copies of everything so far.
