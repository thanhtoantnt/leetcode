# 212 — Word Search II

## Problem

Find **all** dictionary words traceable in the letter grid (adjacent cells, each cell used once per word).

**Example:** the grid below, `words = ["oath","pea","eat","rain"]` → `["eat","oath"]`

## Walkthrough

Problem 0079 (word search, `backtracking/`) run for many words at once — the trie makes that affordable: the DFS carries a **trie node** instead of a word index, so all words sharing a prefix are searched in one sweep, and a dead letter kills every word in that prefix simultaneously.

```text
o a a n
e t a e
i h k r
i f l v
```

**[1] build the trie from the word list**
```text
root ─ o ─ a ─ t ─ h ✓        root ─ e ─ a ─ t ✓
      └─ p ─ e ─ a ✓ (dead)   root ─ r ─ a ─ i ─ n ✓ (dead)
```

**[2] scan start cells — only o/e/r have trie children**
```text
(0,0)='o' enters the trie's o-branch; cells with letters not under
root (most of the grid) exit at the first comparison
```

**[3] DFS from (0,0) with node-in-hand**
```text
o(0,0) → a(0,1) → t(1,1) → h(2,1) ✓ "oath" recorded
each step checks board letter against node.children — one lookup
covers all words passing through this prefix
```

**[4] DFS from the e at (1,0)? no child 'e'? — the e at (1,3)**
```text
e(1,3) → a(1,2) → t(1,1) ✓ "eat" recorded
```

**[5] dead branches die once**
```text
"pea" and "rain": no p or r on the board — pruned at step 2,
not by four independent searches
```

Why it works: the grid DFS state is (cell, prefix-node) — the trie summarizes "which words are still possible after this prefix," so the search never repeats work across words, and marking cells `#` enforces the no-reuse rule exactly as in 0079. Reporting words at flagged nodes (and nulling the flag) avoids duplicates. Worst case O(m·n·3^L); in practice the trie's pruning is decisive.
