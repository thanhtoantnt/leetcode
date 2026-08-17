# 140 — Word Break II

## Problem

All ways to segment `s` into dictionary words (the sentences).

**Example:** `s = "catsanddog"`, dict `[cat,cats,and,sand,dog]` → `["cats and dog","cat sand dog"]`

## Walkthrough

0139's cut logic (this folder), but *collecting* instead of just testing: from each start, every dictionary word that prefixes `s` branches the search — append it to the live sentence, recurse on the remainder, and joins happen when the remainder returns its completions.

**[1] from 0 — two prefixes match**
```text
catsanddog
cat ✓   cats ✓  (sand? no)  → two branches
```

**[2] the "cat" branch needs a word at index 3**
```text
s[3:] = sanddog → sand ✓ (s,san,sand… only sand in dict)
```

**[3] reach the end**
```text
cat + sand + dog ✓ → "cat sand dog"
```

**[4] the "cats" branch mirrors**
```text
s[4:] = anddog → and + dog ✓ → "cats and dog"
```

**[5] both sentences assembled**
```text
["cat sand dog", "cats and dog"] ✓
```

Why it works: a sentence is a sequence of dictionary words covering s — enumerating the *first word* of each suffix recursively generates each exactly once (the recursion tree's leaves ↔ segmentations). Worst case exponential ("aaaa…" with [a,aa,aaa]) — 0139's feasibility dp pre-check cuts hopeless inputs; memoizing suffix→completions avoids re-deriving shared remainders. The enumerate-vs-decide sibling of 0131's partition tree (backtracking/).
