# 268 — Missing Number

## Problem

`n` distinct numbers taken from `[0, n]` — exactly one value of the range is absent. Find it.

**Example:** `nums = [3,0,1]` → `2`

## Walkthrough

Gauss's formula: the full range sums to `n(n+1)/2`; subtract the array's actual sum — the difference is the missing value.

**[1] n = 3, full sum**
```text
[3, 0, 1]
expected = 3·4/2 = 6
```

**[2] actual sum**
```text
3 + 0 + 1 = 4
```

**[3] the gap is the answer**
```text
6 − 4 = 2 ✓ — the value that never arrived
```

**[4] the XOR twin**
```text
acc = 0; for i, v in enumerate(nums): acc ^= i ^ v; answer = acc ^ n
pairs cancel (0136's flipbook, bit_manipulate/) — same O(1) space,
immune to overflow
```

Why it works: the array is a full range minus one element, so any injective summary of the range (sum, XOR, product) reveals the hole when compared against its complete-range value. O(n) time, O(1) space; sorting (O(n log n)) or a seen-set (O(n) space) are strictly worse here.
