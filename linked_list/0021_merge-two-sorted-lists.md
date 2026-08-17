# 21 — Merge Two Sorted Lists

## Problem

Merge two sorted linked lists into one sorted list.

**Example:** `1→2→4` + `1→3→4` → `1→1→2→3→4→4`

## Walkthrough

The array-merge half of merge sort, in node form: a **dummy head** anchors the output, a `tail` pointer appends the smaller front node each round, and whichever list remains at the end is linked wholesale.

**[1] both heads at 1 — tie goes left**
```text
L: [1, 2, 4]
R: [1, 3, 4]
tail: dummy  take L's 1 → out: dummy → 1
```

**[2] L=2 vs R=1 — take right's**
```text
L: [2, 4]
R: [1, 3, 4]
out: dummy → 1 → 1
```

**[3] L=2 vs R=3**
```text
L: [2, 4]
R: [3, 4]
out: dummy → 1 → 1 → 2
```

**[4] L exhausts — splice the rest**
```text
L: []
R: [4]
out: dummy → 1 → 1 → 2 → 3 → 4 (R's remainder linked in one step)
```

**[5] final**
```text
return dummy.next → 1 → 1 → 2 → 3 → 4 → 4 ✓
```

Why it works: both inputs are sorted, so the global next-smallest node is always one of the two heads — comparing heads and detaching the winner is inductive and exhaustive. The dummy head exists so the first comparison has something to append to (no special-casing the head). O(n+m) time, O(1) space beyond the reused nodes — exactly the MERGE step of CLRS Ch. 2.3's merge sort, one list at a time.
