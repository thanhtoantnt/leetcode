# 91 — Decode Ways

## Problem

Digits map to letters (`1→A`, `2→B`, …, `26→Z`). Count the decodings of a digit string. Leading-zero singles (`0` alone) are invalid; `10`/`20` are valid pairs.

**Example:** `s = "226"` → `3` (`BZ`, `VF`, `BBF`)

## Walkthrough

Fibonacci-style DP: `dp[i]` = decodings of the first i digits. The last letter is either one digit (`s[i-1]`) or two (`s[i-2..i-1]`) — so `dp[i]` pulls from `dp[i-1]` and `dp[i-2]`, each gated by validity.

**[1] dp[0]=1 (empty), dp[1]: '2' is valid**
```text
[2, 2, 6]
dp: 1 1 .
'2' → B  single digit 2 in range → dp[1] = 1
```

**[2] i=2: second '2'**
```text
[2, 2, 6]
dp: 1 1 2
single '2' ✓ → +dp[1]=1;  pair '22' ✓ → +dp[0]=1 → dp[2] = 2
```

**[3] i=3: '6'**
```text
[2, 2, 6]
dp: 1 1 2 3
single '6' ✓ → +dp[2]=2;  pair '26' ✓ → +dp[1]=1 → dp[3] = 3
```

**[4] the zero gates — "10"**
```text
[1, 0]
dp: 1 1 . .
i=2: single '0' ✗;  pair '10' ✓ → dp[2] = dp[0] = 1  one way: J
```

**[5] a string that dies — "30"**
```text
[3, 0]
i=2: single '0' ✗, pair '30' ✗ (>26) → dp[2] = 0  undecodable
```

Why it works: every decoding ends with a 1- or 2-digit letter — partitioning by the last letter is exhaustive and disjoint, and validity of that last letter depends only on the trailing digits. `dp[i-1]`/`dp[i-2]` means only two rows are live → O(n) time, O(1) space (the Fibonacci shape is no accident: "1111…"-style strings give 1,2,3,5,8…).
