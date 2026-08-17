# 1046 — Last Stone Weight

## Problem

Each turn, smash the two heaviest stones: weights `x ≤ y`. If `x ≠ y`, the fragment `y − x` survives; if equal, both are destroyed. Return the weight of the last stone (or 0).

**Example:** `stones = [2,7,4,1,8,1]` → `1`

## Walkthrough

A max-heap gives the two heaviest in O(log n): pop twice, push the fragment back. (Python's `heapq` is a min-heap, so negate everything.)

**[1] heapify — two heaviest on top**
```text
[8, 7, 4, 2, 1, 1]
 X  Y
heap=[8,7,4,2,1,1]  pop 8 and 7
```

**[2] smash 8,7 → push 1**
```text
[4, 2, 1, 1, 1]
 X  Y
heap=[4,2,1,1,1]  8−7=1 survives, sifted back in
```

**[3] smash 4,2 → push 2**
```text
[2, 1, 1, 1]
 X  Y
heap=[2,1,1,1]  4−2=2
```

**[4] smash 2,1 → push 1**
```text
[1, 1, 1]
 X  Y
heap=[1,1,1]  2−1=1
```

**[5] smash 1,1 → both destroyed**
```text
[1]
heap=[1]  equal weights vanish → one stone left
```

**[6] done**
```text
[1]
return 1  the last stone
```

Why it works: each turn is two pops + maybe one push = O(log n), and there are at most n−1 turns → O(n log n). The heap keeps "heaviest two" at the top without re-sorting after every smash.
