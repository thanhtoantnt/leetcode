# 136 — Single Number

## Problem

Every element appears twice except one. Find the single one — O(1) space, no set allowed.

**Example:** `nums = [4,1,2,1,2]` → `4`

## Walkthrough

Fold **XOR** across the array. Pairs annihilate (`a ^ a = 0`), and XOR commutes/associates, so all duplicates vanish regardless of order — the accumulator ends holding the singleton.

**[1] start: acc = 0**
```text
[4, 1, 2, 1, 2]
 i
acc=0  0 ^ 4 = 4
```

**[2] fold in 1, 2**
```text
[4, 1, 2, 1, 2]
     i
acc=4^1^2  order is irrelevant — commutative
```

**[3] the second 1 cancels**
```text
[4, 1, 2, 1, 2]
           i
acc = 4^1^2^1 = 4^2  the 1s annihilated
```

**[4] the second 2 cancels**
```text
[4, 1, 2, 1, 2]
              i
acc = 4^2^2 = 4 ✓
```

Why it works: XOR is its own inverse (`a ^ a = 0`, `a ^ 0 = a`), so the multiset's paired elements contribute nothing, leaving the odd one out — a group-theoretic way of saying "parity". O(n), O(1). The set-based version is O(n) space; the sort-and-scan is O(n log n). Siblings: 0191/0190/0338 (this folder) count and reverse bits; 0268 (arrays) is the same idea with sums.
