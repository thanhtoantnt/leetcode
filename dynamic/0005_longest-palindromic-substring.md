# 5 — Longest Palindromic Substring

## Problem

Return the longest palindromic substring of `s`.

**Example:** `s = "babad"` → `"bab"` (`"aba"` is equally valid)

## Walkthrough

**Expand around centers.** Every palindrome mirrors around its center — a single letter (odd length) or the gap between two letters (even length). Try all 2n−1 centers; from each, expand outward while the letters match. Track the best span seen.

**[1] center at a(1), odd — expands once**
```text
[b, a, b, a, d]
     C
L/R spread to (0,2): b…b ✓ → "bab", len 3
```

**[2] center at b(2), odd — blocked**
```text
[b, a, b, a, d]
        C
a ≠ a on the outside? (1,3) = a,a ✓ → "aba" len 3; next (0,4): b ≠ d ✗ stop
```

**[3] center between a(1) and b(2)? — even centers on "aa" type gaps**
```text
[b, a, b, a, d]
    C C
a ≠ b ✗ length 0 — this word has no even palindrome
```

**[4] best span recorded**
```text
[b, a, b, a, d]
 ✓bab
best=(0,2)  start = C − (len−1)/2, computed as the max over all centers
```

Why it works: palindromes are determined by their center — s[i..j] is one iff s[i+1..j−1] is one and s[i]==s[j] — so expanding from each center visits each candidate exactly once. 2n−1 centers × O(n) expansion = O(n²) time, O(1) space. (Manacher's algorithm reaches O(n); DP tables also give O(n²) but with O(n²) memory.)
