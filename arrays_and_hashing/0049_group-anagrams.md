# 49 — Group Anagrams

## Problem

Group the words that are anagrams of each other. Return the groups in any order.

**Example:** `["eat","tea","tan","ate","nat","bat"]` → `[["eat","tea","ate"],["tan","nat"],["bat"]]`

## Walkthrough

Two anagrams become identical when their letters are sorted — so the sorted word is the bucket key. One pass over the words, each dropped into its key's bucket.

**[1] the words**
```text
[eat, tea, tan, ate, nat, bat]
 i
key(eat)=aet  sort the letters → aet
```

**[2] words 2–3 — two more keys**
```text
[eat, tea, tan, ate, nat, bat]
          i
keys so far: aet aet ant  tea lands in the same bucket as eat
```

**[3] word 4 joins bucket aet**
```text
[eat, tea, tan, ate, nat, bat]
               i
aet=[eat,tea,ate]  ant=[tan]
```

**[4] word 5 joins bucket ant**
```text
[eat, tea, tan, ate, nat, bat]
                    i
ant=[tan,nat]  5 of 6 words bucketed
```

**[5] last word — own bucket**
```text
[eat, tea, tan, ate, nat, bat]
aet=[eat,tea,ate]  ant=[tan,nat]  abt=[bat]  → 3 groups
```

Why it works: sorting is a canonical form — equal multisets of letters produce equal sorted strings — so the map groups exactly the anagram classes. O(n · k log k) for n words of length k; the count-26 signature alternative makes it O(n · k).
