# 189 — Rotate Array

## Problem

Rotate the array right by `k`, **in place**.

**Example:** `nums = [1,2,3,4,5,6,7]`, `k = 3` → `[5,6,7,1,2,3,4]`

## Walkthrough

Rotation = block swap: the last `k` elements move to the front, keeping both blocks' internal order. Reversal does it in three passes: **reverse all**, then **reverse the first k**, then **reverse the rest** — each reversal destroys exactly the order that needs destroying, and the second pair restores it block-locally.

**[1] start**
```text
[1, 2, 3, 4, 5, 6, 7]
k=3 mod 7  blocks: A=[1,2,3,4] B=[5,6,7] → want B A
```

**[2] reverse everything**
```text
[7, 6, 5, 4, 3, 2, 1]
both blocks present, both backwards: B' A'
```

**[3] reverse the first k**
```text
[5, 6, 7, 4, 3, 2, 1]
B restored  A still reversed
```

**[4] reverse the rest**
```text
[5, 6, 7, 1, 2, 3, 4]
A restored → B A ✓ done, in place
```

Why it works: `(A B) = reverse(reverse(A) reverse(B))` with the outer reversal split into the two local ones — each element is swapped ~twice. O(n) time, O(1) space; the naive pop/insert loop is O(n·k), and the slicing version is O(n) but allocates. Same trick as 0048's transpose+reverse (rotate an image 90°), one dimension down.
