# 139 — Word Break

## Problem

Can `s` be segmented into a space-separated sequence of dictionary words (reused freely)?

**Example:** `s = "leetcode"`, `wordDict = ["leet","code"]` → `true`

## Walkthrough

`dp[i]` = the first `i` chars can be segmented. It's `true` if some earlier `dp[j]` is true **and** `s[j..i)` is a dictionary word — every segmentation has a *last word*, and cutting it off leaves a valid prefix.

**[1] dp[0] = true — the empty prefix**
```text
[leetcode]
dp: ✓ . . . . . . . .
dp[0]=1  nothing consumed, vacuously segmentable
```

**[2] j=0, word "leet" → dp[4]**
```text
[leetcode]
dp: ✓ . . . ✓ . . . .
s[0:4]='leet' ∈ dict and dp[0] ✓ → dp[4] = true
```

**[3] nothing else reachable from 0 or 4… scan continues**
```text
[leetcode]
dp: ✓ . . . ✓ . . . .
s[0:8]='leetcode' ∉ dict; 'lee','le' ∉ dict → no other j fires
```

**[4] j=4, word "code" → dp[8]**
```text
[leetcode]
dp: ✓ . . . ✓ . . . ✓
s[4:8]='code' ∈ dict and dp[4] ✓ → dp[8] = true → done
```

**[5] a false case: "catsandog", dict [cats,dog,sand,and,cat]**
```text
dp reaches: ✓ .. cats(4) .. sand(8) and(8) — but 'og' ∉ dict
dp[11]=0  every last-word split of the full string fails → False
```

Why it works: the last word of any segmentation ends exactly at the cut i — checking all j < i covers all possible last words. O(n² · k) with substring checks against the dict (a set makes membership O(1), substring hashing O(k)); memoized DFS over start positions is the same computation shaped recursively. For the *count/all* variants (140), store parent lists at each dp cell and backtrack.
