# 125 — Valid Palindrome

## Problem

Is the string a palindrome considering **only alphanumerics**, ignoring case?

**Example:** `s = "A man, a plan, a canal: Panama"` → `true`

## Walkthrough

Two pointers walking inward, skipping non-alphanumerics with a normalized comparison (`lower`). Meet in the middle without building a filtered copy.

**[1] L on 'A', R on 'a' (last char)**
```text
[A, m, a, n, …, P, a, n, a, m, a]
  L                           R
'A' vs 'a' → equal case-folded ✓ both move in
```

**[2] punctuation hops**
```text
[A, m, a, n, ',', …]
       L           R
',' skipped: R-- until it lands on 'n'  compare m vs n
```

**[3] pairs keep matching**
```text
[a, …, c, a, n, a, l]
          L   R
'a' vs 'a' ✓ … every inward pair folds equal
```

**[4] pointers cross — verdict**
```text
return True  all pairs matched
```

**[5] a false case: "race a car"**
```text
r … r ✓, a … a ✓, c … c ✓, then 'e' vs ' ' → skip → 'e' vs 'a' ✗ → False
```

Why it works: a palindrome is defined pairwise from the outside in — (first, last), (second, second-last)… — so two cursors inward test it directly, and skipping noise characters just re-defines "first/last *meaningful* character" at each step. O(n) time, O(1) space; the one-liner `clean = filter(isalnum, s.lower()); clean == clean[::-1]` is O(n) space instead.
