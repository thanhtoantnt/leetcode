# 89 — Gray Code

## Problem

List all `2ⁿ` numbers of n bits so consecutive numbers (including last→first) differ in **exactly one bit**.

**Example:** `n = 2` → `[0,1,3,2]` — 00→01→11→10→00, each step flips one bit.

## Walkthrough

Reflect-and-prefix. The sequence for n is: the sequence for n−1 (prefix 0), then that same sequence **reversed** (prefix 1). Mirroring guarantees the join in the middle flips exactly the new bit.

**[1] base: n = 0 → [0]**
```text
0
seq=[0]  one element, nothing to flip — trivially valid
```

**[2] n = 1 — reflect [0]**
```text
0 1
seq=[0,1]  0 | reversed([0]) +2⁰ → [0, 1]  one flip at the join
```

**[3] n = 2 — reflect [0,1]**
```text
0 1 3 2
00 01 11 10
seq=[0,1,3,2]  old [0,1] | reversed+2¹ [3,2]
```

**[4] n = 3 — reflect again**
```text
0 1 3 2 6 7 5 4
000 001 011 010 110 111 101 100
seq=8 values  [0,1,3,2] | reversed+2² [6,7,5,4]
```

**[5] check the wrap-around**
```text
0 1 3 2 6 7 5 4 → back to 0
100 vs 000  last 4 = 100 vs first 0 = 000 → one bit differs ✓ cycle closes
```

Why it works: the mirror join flips only the new high bit (prefix 0→1 with the low bits identical), inside each half single-bit steps hold by induction, and the wrap-around 2^(n−1)…0 also differs in one bit by construction. O(2ⁿ) output; closed form `i ^ (i >> 1)` gives element i directly — XOR with the right shift is exactly "prefix-parity encoding".
