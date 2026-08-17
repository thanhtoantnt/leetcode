# 424 — Longest Repeating Character Replacement

## Problem

Change at most `k` characters in a substring. Longest substring that can be made **all one letter**?

**Example:** `s = "AABABBA"`, `k = 2` → `5` (`"AABAB"` → `"AAAAA"`)

## Walkthrough

A window is fixable iff `windowLen − count(mostFreqChar) ≤ k` — the non-majority letters are exactly the ones you'd rewrite. Slide: grow the right edge, update counts; when the inequality breaks, advance the left edge too. The window never needs to shrink — only to slide at its record size.

**[1] window "AA"**
```text
[A, A, B, A, B, B, A]
 L  R
len=2 maxFreq=2 fix=0 ✓  all majority already
```

**[2] window "AAB"**
```text
[A, A, B, A, B, B, A]
 L     R
len=3 maxFreq=2 fix=1 ✓ best=3  rewrite the B
```

**[3] window "AABA"**
```text
[A, A, B, A, B, B, A]
 L        R
len=4 maxFreq=3 fix=1 ✓ best=4
```

**[4] window "AABAB" — full budget**
```text
[A, A, B, A, B, B, A]
 L           R
len=5 maxFreq=3 fix=2 ✓ best=5  both B's rewritten → AAAAA
```

**[5] window "AABABB" — over budget, slide**
```text
[A, A, B, A, B, B, A]
    L           R
len=6 maxFreq=3 fix=3 ✗ → L++ (window slides, size stays 6)
no len-6 window is legal: maxFreq never exceeds 3 in any 6-span
```

**[6] done**
```text
return 5
```

Why it works: the fix count `len − maxFreq` is precisely the letters needing rewrite, so the invariant is a complete legality test. A subtlety: `maxFreq` may go stale (not decremented when the left edge passes the old majority letter) — that's fine, because a stale-high maxFreq only makes the test *more permissive* for windows no larger than the current record, and only larger windows can improve the answer. O(n) time, O(26) counts.
