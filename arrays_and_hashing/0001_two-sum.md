# 1 — Two Sum

## Problem

Given `nums` and a `target`, return the indices of the two numbers that add up to `target`. Exactly one solution exists.

**Example:** `nums = [2,7,11,15]`, `target = 9` → `[0,1]`

## Walkthrough

One pass with a hash map: for each number, check whether its **complement** (`target − num`) was already seen. If not, record `num → index` and move on.

**[1] i=0, value 2**
```text
[2, 7, 11, 15]
  i
need=7 seen={}  9−2=7 not seen yet → store 2→0
```

**[2] i=1, value 7 — complement found**
```text
[2, 7, 11, 15]
     i
need=2 seen={2:0}  9−7=2 is in seen → return [0, 1]
```

Why it works: the map answers "does the needed partner exist to my left?" in O(1), so each element is examined once — O(n) total, versus the brute-force O(n²) pair scan. Storing *after* the check also handles the case where the pair uses the same value twice (e.g. `[3,3]`, target 6) without reusing one index.
