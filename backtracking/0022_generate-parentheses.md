# 22 — Generate Parentheses

## Problem

Generate all strings of `n` pairs of parentheses that are **well-formed**.

**Example:** `n = 3` → `["((()))","(()())","(())()","()(())","()()()"]`

## Walkthrough

Build character by character, tracking two counters: `open` (used `(`) and `close` (used `)`). Two rules generate *only* valid strings — no filtering later: you may add `(` while `open < n`, and you may add `)` only while `close < open` (a closer must have an opener to match).

**[1] only one choice at the start**
```text
s=(
open=1 close=0  close<open fails (0<0) → must open
```

**[2] both choices available**
```text
s=((
open=2 close=0  open<3 and close<2 → branch both ways
```

**[3] leftmost path — close, close, close**
```text
s=(((
├─L (
│  ├─L (
│  │  └─R ) → open=3, then ))) forced → ((()))
```

**[4] a middle path — open the third, then close thrice**
```text
s=(()())
├─L (
│  ├─R )
│  │  ├─R ( → then ) ) → (()())
```

**[5] all five leaves**
```text
((())) (()()) (())() ()(()) ()()()
✓ 5 = Catalan(3)  every leaf is valid by construction
```

Why it works: the two guards make invalid strings *unreachable* — `close < open` prevents closing something never opened, `open ≤ n` prevents surplus openers — so every completed string of length 2n is well-formed. The count of such strings is the Catalan number C_n = (2n choose n)/(n+1); O(4ⁿ/√n) strings, O(n) work each.
