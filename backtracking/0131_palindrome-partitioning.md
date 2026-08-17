# 131 — Palindrome Partitioning

## Problem

Split a string into substrings, each of which is a palindrome. Return every possible partition.

**Example:** `s = "aab"` → `[["a","a","b"],["aa","b"]]`

## Walkthrough

Backtracking over **cut positions**: at each start index, try every prefix `s[start..end]` — if it's a palindrome, recurse from `end+1` with it appended; when `start` reaches the end, the collected pieces form one complete partition.

**[1] from index 0 — prefix "a" is a palindrome**
```text
s=aab part=a
├─R a ✓  recurse from index 1
```

**[2] then "a" again, then "b"**
```text
s=aab part=a,a,b ✓
├─L a
│  ├─R a ✓
│  │  └─R b ✓ → ["a","a","b"] recorded
```

**[3] prefix "aa" from the top — also a palindrome**
```text
s=aab part=aa
├─R aa ✓  jump start to 2 in one cut
```

**[4] finish the second partition**
```text
s=aab part=aa,b ✓
├─L aa
│  └─R b ✓ → ["aa","b"] recorded
```

**[5] prefix "aab" — rejected**
```text
s=aab
aab ✗  not a palindrome → no branch, done: 2 partitions
```

Why it works: every partition is a sequence of palindrome prefixes — the tree enumerates each choice of first piece, then recursively the rest — so leaves are exactly the valid partitions. O(n · 2ⁿ) worst case (all-distinct letters → every prefix passes, 2^(n−1) partitions). Precomputing a `is_pal[i][j]` table with interval DP turns each palindrome check into O(1).
