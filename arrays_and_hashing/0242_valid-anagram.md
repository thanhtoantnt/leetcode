# 242 — Valid Anagram

## Problem

Return `true` if `t` is an anagram of `s` — same letters, same counts.

**Example:** `s = "anagram"`, `t = "nagaram"` → `true`

## Walkthrough

Count letters in `s` (up), subtract letters in `t` (down). Anagrams ⟺ every counter ends at 0.

**[1] scan s — counts build**
```text
[a, n, a, g, r, a, m]
   i
scanning s  a→3, n→1, g→1, r→1, m→1
```

**[2] scan t — counts drain**
```text
[n, a, g, a, r, a, m]
   i
scanning t  each letter decrements its counter
```

**[3] all counters zero**
```text
[a, n, a, g, r, a, m]
counters: a=0 n=0 g=0 r=0 m=0  → return True
```

Failure modes: different lengths → reject immediately; some counter negative (t uses a letter s doesn't have) or positive (s has leftovers) → `false`. 26-slot array for lowercase letters (or a dict for general alphabets): O(n) time, O(1) space. Sorting both strings and comparing is the O(n log n) alternative.
