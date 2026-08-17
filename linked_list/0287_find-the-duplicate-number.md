# 287 — Find the Duplicate Number

## Problem

`n+1` integers in range `[1, n]`: exactly one value repeats (maybe several times). Find it — array read-only, O(1) space.

**Example:** `nums = [1,3,4,2,2]` → `2`

## Walkthrough

**Floyd's cycle detection on a hidden graph**: read `i → nums[i]` as a linked-list "next" function. Two indices holding the same value = two pointers at one node = a cycle, and the cycle's **entry node is labeled by the duplicate value**. Phase 1: tortoise/hare meet inside the cycle. Phase 2: walk from the start and the meeting point in lockstep — they collide at the entry.

```text
next: 0→1, 1→3, 2→4, 3→2, 4→2
path: 0 → 1 → 3 → 2 → 4 → 2 → 4 …  (cycle {2,4}, entry = 2)
```

**[1] phase 1 — speeds 1 vs 2**
```text
[1, 3, 4, 2, 2]
    S     F
t1: s=1 f=3   t2: s=3 f=4   t3: s=2 f=4? no — f jumps 4→2→4: s=2, f=4
```

**[2] meet at node 4**
```text
[1, 3, 4, 2, 2]
t4: s=4 f=4 ✓ meet — somewhere inside the cycle
```

**[3] phase 2 — reset one walker to the start**
```text
[1, 3, 4, 2, 2]
 S        M
s=0 m=4   both move one step per round now
```

**[4] lockstep walk**
```text
[1, 3, 4, 2, 2]
s: 0 → 1 → 3 → 2
m: 4 → 2 → 4 → 2
after 3 steps both stand on node 2
```

**[5] entry = duplicate**
```text
return 2  nodes 3 and 4 both point here — their shared value 2 is the duplicate
```

Why it works: let the start be `a` steps from the entry, and the meeting point `b` past it. Phase 1 gives 2(a+b) ≡ a+b (mod L), so a ≡ −b (mod L) — walking a steps from the start and b steps *backward* from the meeting point end at the same node, the entry. And the entry is the duplicate because only a duplicated value can receive two in-edges. O(n) time, O(1) space, input untouched — the same machinery as problem 141's flipbook in this folder.
