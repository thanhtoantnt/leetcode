# 138 — Copy List with Random Pointer

## Problem

Deep-copy a linked list whose nodes have `next` **and** a `random` pointer to any node (or null).

**Example:** `1 → 2` with 1.random→2, 2.random→1 → a new list with the same shape, zero shared nodes.

## Walkthrough

The map-free trick — **interleave clones**: insert a clone right after each original. Then every original's random target has its clone sitting *next to it*, so wiring `clone.random = original.random.next` needs no lookup. Finally unzip.

**[1] pass 1 — clone after each node**
```text
1 → 1′ → 2 → 2′
clones (′) carry values; randoms still unset
```

**[2] pass 2 — wire the randoms**
```text
1 → 1′ → 2 → 2′
1.random = 2  →  1′.random = 2.next = 2′  ✓
2.random = 1  →  2′.random = 1.next = 1′  ✓
```

**[3] pass 3 — unzip next pointers**
```text
originals: 1 → 2      clones: 1′ → 2′
cur.next = clone.next restores originals; clone.next = clone.next.next builds the copy
```

**[4] result**
```text
return 1′ → 2′ with randoms mirroring the original — no shared nodes ✓
```

**[5] the alternative**
```text
hash map {old → new}: two passes, random lookups via the map —
O(n) extra space; the interleave trades the map for pointer surgery
```

Why it works: adjacency encodes the mapping — `original.next` *is* its clone and `original.random.next` is the clone of what random pointed at — so all indirections resolve in O(1) with zero bookkeeping. Same goal as 0133 (clone graph, `graphs/`): there cycles forced a visited map; here the linear structure allows the interleave. O(n) time, O(1) extra.
