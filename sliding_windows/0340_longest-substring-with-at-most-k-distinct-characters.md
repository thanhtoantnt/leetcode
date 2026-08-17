# 340 — Longest Substring with At Most K Distinct Characters (premium)

## Problem

Longest substring containing at most `k` distinct letters. *Paraphrased from LeetCode 340 (premium).*

**Example:** `s = "eceba"`, `k = 2` → `3` (`"ece"`)

## Walkthrough

The k-generalization of 0904 (two fruit types) and 0003 (one-of-each): the window holds a count dict; whenever `len(count)` exceeds k, evict from the left until a letter's count drops to zero and leaves the dict.

**[1] window "e"**
```text
[e, c, e, b, a]
 L  R
count={e:1} k=2 ✓ best=1
```

**[2] window "ece" — the peak**
```text
[e, c, e, b, a]
 L        R
count={e:2, c:1} best=3
```

**[3] b arrives — third distinct, shrink**
```text
[e, c, e, b, a]
       L     R
drop e (2→1→gone at L=2? left walks: e=1, c gone) → count={e:1, b:1}
```

**[4] a arrives — shrink again**
```text
[e, c, e, b, a]
             L  R
e evicted → count={b:1, a:1} best stays 3
```

**[5] done**
```text
return 3  "ece"
```

Why it works: "≤ k distinct" is the window's invariant — the right edge explores, the left edge restores minimally, and every maximal legal window is scanned; each index enters and leaves once → O(n). One template, three problems: k=1 is 0003's uniqueness? (no — distinct=∞ there; 0003 is k=all-unique), 0904 is k=2 exactly. With an ordered dict (LRU-style, 0146) the left jump is O(1) instead of stepping.
