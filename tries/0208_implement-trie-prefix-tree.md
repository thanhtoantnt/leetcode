# 208 — Implement Trie (Prefix Tree)

## Problem

Build a trie: `insert`, `search` (whole word), `startsWith` (any word with this prefix).

**Example:** insert `"apple"` → `search("app")` false, `startsWith("app")` true; insert `"app"` → `search("app")` true.

## Walkthrough

Nodes hold a children map (one per letter) and an **end flag** marking "a word terminates here." Walking a word's letters descends the trie; search additionally requires the last node's flag, startsWith doesn't.

**[1] insert "apple" — build the path**
```text
root
└─ a ─ p ─ p ─ l ─ e ✓(end)
each letter takes one hop, creating nodes as needed
```

**[2] search "app" — path exists, no flag**
```text
walk a→p→p: nodes exist, but end=false at the second p
→ False ("app" is only a prefix of the stored word)
```

**[3] startsWith "app" — path exists, that's enough**
```text
same walk, flag irrelevant → True
```

**[4] insert "app" — flag flips**
```text
root
└─ a ─ p ─ p ✓(end) ─ l ─ e ✓(end)
the existing path is reused; sharing prefixes is the whole point
```

**[5] search "app" again**
```text
walk ends on a flagged node → True ✓
```

Why it works: the trie stores the *set of words as paths* — shared prefixes share structure, so prefix queries cost only the prefix's length: insert/search/startsWith all O(L) regardless of dictionary size (vs a hash set, which handles search in O(L) but cannot answer startsWith without scanning everything). The engine behind autocomplete and 0212/0211 (this folder). CLRS doesn't cover tries in depth; they're the classic string-tree structure of Ch. 12-style search trees keyed by characters.
