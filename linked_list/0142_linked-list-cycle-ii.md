# 142 — Linked List Cycle II

## Problem

Return the node where the cycle begins, or `None` if no cycle.

**Example:** `3 → 2 → 0 → -4 ↺ back to 2` → node `2`

## Walkthrough

Phase 1 is 0141 (this folder): tortoise/hare meet inside the loop. Phase 2 exploits the algebra: with the head `a` steps from the entry and the meeting point `b` past it, 2(a+b) ≡ a+b (mod L) gives `a ≡ −b (mod L)` — so walking `a` from the head and `b` backward from the meeting point lands both on the entry. In practice: reset one walker to the head, step both singly, collide at the entry.

**[1] the list — cycle of length 3, entry = 2**
```text
3 → 2 → 0 → −4
    ↑__________|
```

**[2] phase 1 — meet at −4**
```text
slow: 2 0 −4   fast: 0 2? step by 2: 0, −4, 0, −4 — meet at −4
```

**[3] phase 2 — one walker resets to 3**
```text
slow: 3   fast: −4   (both now step by 1)
```

**[4] lockstep to the entry**
```text
slow: 3 → 2   fast: −4 → 2   collide at node 2 ✓
```

**[5] the no-cycle case**
```text
fast hits None in phase 1 (the while-else) → return None
```

Why it works: the phase-1 meeting guarantees `a ≡ −b (mod L)` — every step the head-walker takes toward the entry is matched by the meeting-point walker orbiting toward it from the other side, so the first common node is the entry itself. O(n) time, O(1) space; the same math drives 0287's duplicate hunt (find the hidden cycle's entry in an array).
