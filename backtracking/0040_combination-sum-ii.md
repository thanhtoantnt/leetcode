# 39 vs 40 — Combination Sum I & II

## Problem

**39:** candidates may be reused unlimited times; find combos summing to target. **40:** each candidate used at most once, input may contain duplicates.

**Example:** 39: `candidates = [2,3,6,7]`, `target = 7` → `[[2,2,3],[7]]`

## Walkthrough (39)

DFS with remainder tracking. Two choices per step produce the tree: **extend** with the current candidate again (allowed — unlimited reuse), or **move on** to the next candidate. Remainder 0 → leaf; negative → dead branch.

**[1] take 2**
```text
rem=5
├─R take 2  7−2=5 ≥ 0 → recurse deeper
```

**[2] 2,2**
```text
rem=3
├─L 2
│  ├─R take 2  5−2=3 ≥ 0 → continue
```

**[3] 2,2,2 — remainder 1, everything below is dead**
```text
rem=1
├─L 2
│  ├─L 2
│  │  ├─R take 2  1−2 < 0 ✗ prune; take 3/6/7 also < 0 ✗
```

**[4] back up one level — 2,2,3 hits zero**
```text
rem=0 ✓
├─L 2
│  ├─L 2
│  │  └─R take 3  3−3=0 → [2,2,3] recorded
```

**[5] skip 2 entirely — straight to 7**
```text
rem=0 ✓
└─R take 7  7−7=0 → [7] recorded → done
```

## What changes in 40

Sort + the skip rule from Subsets II: `candidates[i] == candidates[i-1]` at the same tree level → skip, or duplicate combos come out. And the recursion advances to `i+1` — each copy usable once. 39's recursion *stays at i* for reuse; that one line is the whole difference between the problems.

Why pruning works: candidates are positive, so remainders only shrink — a negative remainder's entire subtree is negative, and cutting it keeps the finite-despite-reuse tree small.
