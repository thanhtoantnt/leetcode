# 371 — Sum of Two Integers

## Problem

Compute `a + b` without the `+` or `-` operators.

**Example:** `a = 3`, `b = 5` → `8`

## Walkthrough

Two bit operations split addition apart: **XOR** is per-bit sum ignoring carries (0+0=0, 1+0=1, 1+1=0 "write 0"); **AND shifted left** is exactly the carries (both 1 → carry into the next column). Repeat: add the carries back the same way until no carries remain.

**[1] 3 + 5 in binary: 011 + 101**
```text
a = 011
b = 101
xor = 110  (per-bit sums: 1+0, 1+0? per column: 1^1=0? see below)
```

Column by column: `011 ^ 101 = 110` (right: 1^1=0, middle: 1^0=1, left: 0^1=1). Carries: `011 & 101 = 001`, shifted = `010`.

**[2] fold the carry back in: 110 + 010**
```text
a = 110
b = 010  (the carry)
xor = 100  carries: (110 & 010)<<1 = 100
```

**[3] again: 100 + 100**
```text
a = 100
b = 100
xor = 000  carries: (100 & 100) << 1 = 1000
```

**[4] last round: 000 + 1000**
```text
a = 1000
b = 0000  no carries left → done
```

**[5] result**
```text
1000₂ = 8 ✓
```

Why it works: `a + b = (a XOR b) + ((a AND b) << 1)` is an algebraic identity — splitting sum and carry — and each round moves the carries strictly left (they eventually fall off or vanish). O(1) for fixed-width ints. The Python 32-bit mask + final sign-flip works around unbounded ints (negatives are two's-complement only within the mask) — a hardware adder's ripple, in software.
