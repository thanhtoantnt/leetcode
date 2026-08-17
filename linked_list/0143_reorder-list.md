# 143 — Reorder List

## Problem

Reorder `L0→L1→…→Ln` into `L0→Ln→L1→Ln−1→…` — in place, no value copies.

**Example:** `1→2→3→4→5` → `1→5→2→4→3`

## Walkthrough

Three textbook moves chained: (1) slow/fast pointers **split** at the middle, (2) **reverse** the back half (0206's flipbook), (3) **interleave** the two halves stitch by stitch.

**[1] split — slow lands at 3**
```text
front: 1 → 2 → 3
back:  4 → 5
slow/fast: fast hops 2 for slow's 1 — slow is at the middle when fast ends
```

**[2] reverse the back half**
```text
front: 1 → 2 → 3
back:  5 → 4
prev-walk from 4: null←4←5
```

**[3] interleave — first stitch**
```text
1 → 5    then 5 → 2 (hold a.next), 2 → 4 …
a=1 b=5: 1.next=5, 5.next=2, advance a=2 b=4
```

**[4] remaining stitches**
```text
1 → 5 → 2 → 4    a=2 b=4: 2.next=4, 4.next=3, a=3 b=null
```

**[5] done**
```text
1 → 5 → 2 → 4 → 3  odd length leaves middle node 3 as the tail ✓
```

Why it works: the target order is exactly "front half and reversed back half, zipped" — each step is a problem already solved in this folder (0141's slow/fast, 0206's reversal), and the zip is two pointer-hops per stitch. O(n) time, O(1) space; the naive array-of-nodes version is O(n) space.
