# 190 — Reverse Bits

## Problem

Reverse the 32 bits of an unsigned integer.

**Example:** input `0b00000010100101000001111010011100` → output `0b00111001011110000010100101000000`

## Walkthrough

Peel-and-append, 32 rounds: shift the accumulator left, OR in the input's lowest bit, drop that bit. The accumulator is the reversed prefix of bits processed so far.

**[1] round 1 — lowest bit 0**
```text
n=…100
acc=0  acc = (0<<1) | 0 = 0  n >>= 1
```

**[2] rounds 2–3 — bits 0,1,1 arrive**
```text
n=…11100 → …1110 → …111
acc=0 → 1 → 11  the reversed tail builds up left-aligned
```

**[3] after k rounds**
```text
acc holds the last k bits of n, reversed — appended from the right
```

**[4] 32 rounds later**
```text
acc = first bit becomes last, last becomes first — full mirror ✓
```

**[5] the fast path (optional)**
```text
mask-and-shift dance: swap adjacent bits, then pairs, nibbles, bytes,
halfwords — 5 steps instead of 32 (O(log w) via divide and conquer)
```

Why it works: `(acc << 1) | (n & 1)` is exactly "append n's current last bit to acc's end" — after 32 appends the bits are in mirror order. Fixed 32 iterations → O(1). Sibling: 0191 (popcount) walks bits the same way without the accumulator; byte-reversal lookup tables trade memory for speed in real hash functions (FNV, MurmurHash use these ops).
