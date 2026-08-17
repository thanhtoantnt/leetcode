# 42 — Trapping Rain Water

## Problem

After rain, how much water sits between the bars?

**Example:** `height = [0,1,0,2,1,0,1,3,2,1,2,1]` → `6`

## Walkthrough

Water above a bar = `min(tallest bar to its left, tallest to its right) − its own height` — capped by the **shorter** wall. Two pointers from both ends with running maxes: always advance the side with the smaller bar; its water level is already decided, because a taller wall certainly exists on the other side.

**[1] walls start at the edges**
```text
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
 L                                R
lmax=0 rmax=1  left smaller → resolve L: water += 0−0; L++
```

**[2] bar 1 becomes lmax**
```text
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    L                            R
lmax=1  dip ahead: bar 0 will trap 1
```

**[3] the dip at index 2 traps**
```text
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
       L                         R
lmax=1 water += 1−0 = 1 ✓  advance
```

**[4] middle dips fill the same way**
```text
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
index 5 (bar 0, lmax=2) traps 2; index 6 traps 1 … running total 6
```

**[5] pointers meet — done**
```text
water=6  every dip resolved against its nearer (binding) wall ✓
```

Why it works: advancing the smaller-bar side is safe — its cap is that side's running max, and the other side's max is already ≥ it (the pointer stopped there for a reason), so `min(lmax, rmax)` is known without scanning. Each bar visited once: O(n) time, O(1) space. The DP version (precomputed left/right max arrays) is the same formula at O(n) memory — sibling: 0023's heap, 0011's two pointers (this folder).
