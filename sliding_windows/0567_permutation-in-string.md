# 567 — Permutation in String

## Problem

Does `s2` contain a contiguous substring that is a permutation of `s1`?

**Example:** `s1 = "ab"`, `s2 = "eidbaooo"` → `true` (`"ba"`)

## Walkthrough

A permutation of `s1` is any same-length window with **identical letter counts**. Slide a fixed-size window of `len(s1)` over `s2`, maintaining its count array incrementally (add the entering char, subtract the leaving one) — compare against s1's counts per step, or count how many of the 26 slots match and react to matches flipping.

**[1] first window "ei" vs target "ab"**
```text
[e, i, d, b, a, o, o, o]
 L  R
win: e1 i1  matches=24/26  a and b slots differ
```

**[2] slide: +d, −e**
```text
[e, i, d, b, a, o, o, o]
    L  R
win: i1 d1  matches=24/26
```

**[3] slide: +b, −i**
```text
[e, i, d, b, a, o, o, o]
       L  R
win: d1 b1  a-slot still short
```

**[4] slide: +a, −d — all slots match**
```text
[e, i, d, b, a, o, o, o]
          L  R
win: b1 a1  matches=26/26 ✓ return True
```

Why it works: two strings are permutations iff their count vectors are equal — so the question is whether any length-|s1| window's vector equals the target's. The fixed-size slide updates the vector in O(1) per step (26-slot diff of matches tracks "how many letters have exactly the right count"), giving O(26 + n) total. Rolling-hash (Rabin-Karp, Ch. 32) is the alternative — probabilistic equality instead of exact counts.
