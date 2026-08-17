# 249 — Group Shifted Strings

## Problem

A string's "shift" moves every letter down the alphabet by the same amount (wrapping): `abc → bcd → … → zab`. Group strings belonging to the same shift family.

**Example:** `["abc","bcd","acef","xyz","az","ba","a","z"]` → `[["abc","bcd","xyz"],["acef"],["az","ba"],["a","z"]]`

## Walkthrough

The signature is the **sequence of circular differences** between adjacent letters, mod 26: `abc → (1,1)`, `bcd → (1,1)`, `acef → (2,2,3)`, `az → (25)`, `ba → (25)`. Same signature ⟺ same family — group by it.

**[1] compute abc's signature**
```text
[abc]
sig=(1,1)  b−a=1, c−b=1
```

**[2] bcd and xyz match**
```text
[abc, bcd, xyz]
sig=(1,1) (1,1) (1,1)  one bucket
```

**[3] the wrap-around bucket: az and ba**
```text
[az, ba]
az: (z−a)=25  ba: (a−b)=−1 ≡ 25 (mod 26)  same signature ✓
```

**[4] singles**
```text
[a, z]
sig=() — empty tuple, length-1 strings all shift trivially → one bucket
```

**[5] the map**
```text
(1,1) → [abc,bcd,xyz]   (2,2,3) → [acef]   (25) → [az,ba]   () → [a,z]
```

Why it works: two strings are shift-equivalent iff some k adds to every letter — subtracting adjacent characters cancels the unknown k exactly, and mod 26 handles the alphabet wrap (`zab → (25,1)`… careful: `zab` is NOT `(1,1)` — it's `(a−z)=−25≡1, (b−a)=1` → actually `(1,1)` ✓ it does match `abc`). One O(total chars) pass with a dict of tuples; problem 49 (anagram grouping, `arrays_and_hashing/`) is the same canonical-form trick with sorted letters instead of differences.
