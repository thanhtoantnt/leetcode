# 19 — Remove Nth Node From End of List

## Problem

Delete the n-th node from the **end** of a linked list, in one pass.

**Example:** `1→2→3→4→5`, `n = 2` → `1→2→3→5`

## Walkthrough

Two pointers with a gap of exactly n: advance `fast` n steps first, then move both until `fast` hits the end — `slow` now stands on the node **before** the victim, ready to splice.

**[1] fast takes a 2-step head start**
```text
[1, 2, 3, 4, 5]
 S     F
gap=2=n  slow still at the dummy before 1
```

**[2] advance both until fast ends**
```text
[1, 2, 3, 4, 5]
          S     F
each step preserves the gap of 2
```

**[3] slow is one before the victim**
```text
[1, 2, 3, 4, 5]
          S  ✗(4)
slow.next = slow.next.next  → 3 links to 5, node 4 unlinked
```

**[4] result**
```text
[1, 2, 3, 5]
return head  node 4 is gone
```

**[5] the head-deletion edge — why a dummy node**
```text
[1, 2], n=2  victim is the HEAD
dummy → 1 → 2:  S=dummy, F=1+2 steps → splice dummy.next = 2
no dummy → the victim IS slow, unlinkable — dummy makes it uniform
```

Why it works: the fixed gap n means when `fast` passes the last node (walked n+1 links total with dummy), `slow` has walked (length−n) links — parking exactly at the predecessor of the n-th-from-end. One pass, O(L), two pointers, no length pre-computation.
