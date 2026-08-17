# 146 — LRU Cache

## Problem

Design a fixed-capacity cache: `get` and `put` both O(1); when full, `put` evicts the **least recently used** key.

**Example:** capacity 2: put 1, put 2, get 1 (recent: 1,2), put 3 → evicts **2**.

## Walkthrough

Two structures, one job each: a **hash map** (key → node) for O(1) lookup, and a **doubly linked list** in recency order (head = newest, tail = oldest) for O(1) reorder and evict. Dummy head/tail anchors remove all edge cases.

**[1] put 1, put 2**
```text
recency: head ⇄ 1 ⇄ 2 ⇄ tail
map={1:node, 2:node}  2 is now the LRU (nearest tail)
```

**[2] get 1 — touch moves it to the head**
```text
recency: head ⇄ 1 ⇄ 2 ⇄ tail
get(1)=1  unlink 1, push at front: head ⇄ 1 ⇄ 2 ⇄ tail → 2 becomes LRU
```

**[3] put 3 — capacity exceeded, evict tail.prev**
```text
recency: head ⇄ 3 ⇄ 1 ⇄ tail
2 evicted (unlink tail.prev, delete map[2])  O(1) both ops
```

**[4] get 2 — gone**
```text
get(2) = -1  the map lookup fails; the node is unlinked
```

**[5] why doubly linked**
```text
unlinking a node needs node.prev in O(1) — a singly linked list
would force a tail-to-node walk; the back-pointers are the whole trick
```

Why it works: recency is a total order under every operation — get and put both mean "this key is now the most recent" — and the list maintains that order with O(1) surgery at both ends while the map pays the O(1) addressing cost. This is CLRS Ch. 10's composition of hash table + list, and the ancestor of real caches (memcached LRU, page replacement).
