# 43 — Multiply Strings

## Problem

Multiply two non-negative integers given as strings (no built-in bignum).

**Example:** `"123" × "456"` = `"56088"`

## Walkthrough

Grade-school multiplication, indexed: digit `i` (from the right) × digit `j` contributes to positions `i+j` and `i+j+1` of the result array. All n·m digit products drop into an array of size n+m, then carries ripple through once at the end.

**[1] the grid of partial products**
```text
        1   2   3
    ×   4   5   6
-----------------
6:      6  12  18
5:      5  10  15
4:      4   8  12
each cell: (a[i]·b[j]) lands at result[i+j] (+carry into i+j+1)
```

**[2] accumulate into the result slots**
```text
pos: 0 1 2 3 4 5
acc: 4 13 28 27 18 0
pos0: 4·1  pos1: 4·2+5·1=13  pos2: 4·3+5·2+6·1=28 …
```

**[3] carry pass, right to left**
```text
pos: 0 1 2 3 4 5
res: 5 6 0 8 8
18→8 c1; 27+1=28→8 c2; 28+2=30→0 c3 … final carry 5 lands at pos0
```

**[4] strip leading zeros → string**
```text
"56088" ✓  123 × 456 = 56088
```

Why it works: writing numbers as Σ dᵢ·10ⁱ, the product's coefficient of 10^k is exactly Σ dᵢ·eⱼ over i+j = k — the slot rule — and one carry pass normalizes every coefficient to a digit. O(m·n) digit multiplications, O(m+n) space. (Karatsuba/FFT — CLRS Ch. 4/30 — beat this for huge inputs; schoolbook wins at interview scale.)
