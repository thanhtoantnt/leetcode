# 141 — Linked List Cycle

## Problem

Given the head of a linked list, determine whether it contains a cycle (some node's `next` points back to an earlier node). Follow-up: O(1) space.

**Example:** `3 → 2 → 0 → -4`, tail connects to index 1 → `true`

## Walkthrough

Floyd's tortoise and hare: `slow` moves 1 step, `fast` moves 2. If there's no cycle, `fast` falls off the end. If there is, both get trapped on the loop and the gap between them shrinks by 1 each round — they must meet.

`3 → 2 → 0 → -4 ↺ back to 2`

**[1] both at head**
```text
[3, 2, 0, -4]
SF
slow=0 fast=0   start together
```

**[2] slow +1, fast +2**
```text
[3, 2, 0, -4]
    S     F
slow=1 fast=2   not equal, keep going
```

**[3] they cross — fast wraps via the cycle**
```text
[3, 2, 0, -4]
    F     S
slow=2 fast=1   fast already looped past -4 back to 2
```

**[4] meet — cycle proven**
```text
[3, 2, 0, -4]
             SF
slow=3 fast=3   slow == fast → return true ✓
```

Why it works: inside the loop, the gap `(fast − slow) mod L` drops by 1 every step, so a meeting is guaranteed in at most L rounds. Without a loop, `fast` hits `null` first. O(n) time, O(1) space — no visited set.

Bonus (problem 142): after they meet, reset one pointer to the head and advance both by 1; they meet again exactly at the cycle's entry.
