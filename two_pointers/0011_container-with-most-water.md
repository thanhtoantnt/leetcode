# 11 — Container With Most Water

## Problem

Vertical lines of height `h[i]`; pick two forming a container with the most water (area = width × min height).

**Example:** `height = [1,8,6,2,5,4,8,3,7]` → `49` (lines at index 1 and 8: width 7 × min(8,7) = 49)

## Walkthrough

Two pointers at the extremes; always move the **shorter** side inward. The shorter line caps the area, so keeping it while shrinking width can only lose — discarding it costs nothing and explores the only candidates that could improve.

**[1] widest, capped by 1**
```text
[1, 8, 6, 2, 5, 4, 8, 3, 7]
 L                       R
area=8×1=8  left is shorter → L++
```

**[2] capped by 7**
```text
[1, 8, 6, 2, 5, 4, 8, 3, 7]
    L                    R
area=7×7=49 best=49  tie (8 vs 7): move either — say R stays, L++
```

**[3] narrower — min height must beat 7**
```text
[1, 8, 6, 2, 5, 4, 8, 3, 7]
       L                 R
area=6×6=36 < 49  shorter side (6) moves
```

**[4] sweep continues**
```text
[1, 8, 6, 2, 5, 4, 8, 3, 7]
             L     R
widths shrink; every remaining container needs min-height > 7 at width < 7 — impossible to beat 49 unless an 8 pairs… 8@1 vs 8@6? width 5 × 8 = 40 < 49
```

**[5] pointers meet — answer stands**
```text
return 49
```

Why it works: for the pair (L, R), the area is capped by the shorter line — every *inner* pair keeping the shorter line has strictly less width and no more min-height, so the shorter side's only useful move is to leave. Following that rule visits exactly the pairs that could be optimal: O(n), O(1), no area re-checks. A clean exchange argument, cousin to the greedy proofs in CLRS Ch. 15/16.
