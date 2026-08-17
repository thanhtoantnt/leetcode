# 647 — Palindromic Substrings

## Problem

Count all palindromic substrings (occurrences count separately for each start/end pair).

**Example:** `s = "aaa"` → `6` (`a`, `a`, `a`, `aa`, `aa`, `aaa`)

## Walkthrough

Same expand-around-center engine as problem 5, but **counting** instead of tracking the best: each successful expansion step of each center is one more palindrome. Odd centers count single-letter cores; even centers count matching pairs.

**[1] center a(0) — one palindrome**
```text
[a, a, a]
  C
count=1  core "a"; (−1,1) out of bounds → stop
```

**[2] center a(1) — expands twice**
```text
[a, a, a]
     C
count=3  "a" ✓, then (0,2): a==a → "aaa" ✓
```

**[3] center a(2) — one**
```text
[a, a, a]
        C
count=4  "a" only; nothing to the right
```

**[4] even center (0,1)**
```text
[a, a, a]
  C C
count=5  a==a → "aa" ✓; outside: out of bounds → stop
```

**[5] even center (1,2)**
```text
[a, a, a]
     C C
count=6  "aa" ✓ → total 6
```

Why it works: every palindrome has exactly one center (a letter, or a gap); expansion enumerates each palindrome precisely at its center, step by step from shortest outward — so the sum of successful steps over all centers equals the palindrome count. O(n²) time, O(1) space; interval DP (`dp[i][j] = s[i]==s[j] and dp[i+1][j-1]`) gets the same count in O(n²) time and space.
