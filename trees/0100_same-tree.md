# 100 — Same Tree

## Problem

Are two binary trees identical in structure and values?

**Example:** `[1,2,3]` vs `[1,2,3]` → `true`; `[1,2,3]` vs `[1,3,2]` → `false`

## Walkthrough

Walk both trees **in lockstep** — one recursion carrying a node from each. The three base cases decide everything: both null (matching gaps ✓), exactly one null or different values ✗, else recurse into both child pairs.

**[1] roots match**
```text
p: 1  [q: 1]
├─L 2     ├─L 2
└─R 3     └─R 3
compare (1,1) ✓ → recurse (2,2) and (3,3)
```

**[2] left pair matches**
```text
p: 1 ✓   [q: 1 ✓]
├─L 2 ✓     ├─L 2 ✓
└─R 3       └─R 3
both children null-null ✓ — leaf pairs agree
```

**[3] right pair matches — true**
```text
all pairs agreed → return True
```

**[4] a mismatch case**
```text
p: 1      q: 1
├─L 2     ├─L 3 ✗
└─R 3     └─R 2
values 2 vs 3 → False immediately, subtrees never compared
```

Why it works: equality is a conjunction over all symmetric position pairs (value and nullness) — the simultaneous DFS visits exactly those pairs, short-circuiting at the first disagreement. O(n) time, O(h) depth. The sibling of 0101 (symmetric tree, same folder): there the paired cursors walk *within* one tree, mirrored.
