# 206 — Reverse Linked List

## Problem

Reverse a singly linked list, in place.

**Example:** `1→2→3→4→5` → `5→4→3→2→1`

## Walkthrough

Three pointers marching: `prev` (already-reversed part's head), `cur` (node being flipped), `next` (saved before the overwrite). Each iteration turns `cur.next` backward, then everything shifts one step right.

**[1] start — nothing reversed yet**
```text
[1, 2, 3, 4, 5]
 P  C  N
prev=null cur=1 next=2  about to flip 1's pointer
```

**[2] flip 1**
```text
[1, 2, 3, 4, 5]
 P  C  N     →  1 → null
 P=1 C=2  1 now points backward at null
```

**[3] flip 2**
```text
2 → 1 → null
P=2 C=3  the reversed prefix grows one node at a time
```

**[4] flip 3, 4**
```text
4 → 3 → 2 → 1 → null
P=4 C=5  one node left
```

**[5] flip 5 — done**
```text
5 → 4 → 3 → 2 → 1 → null
return prev (5) — the new head is the old tail
```

Why it works: the invariant is "prev heads the reversed prefix, cur heads the untouched suffix" — each flip moves exactly one node across the boundary without losing either side (that's `next`'s job: it's read *before* `cur.next` is overwritten). O(n) time, O(1) space. The recursive version (`rev(head) = rev(tail) + head at end`) is the same idea with the call stack holding the prefix.
