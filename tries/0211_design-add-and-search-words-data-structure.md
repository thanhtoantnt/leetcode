# 211 — Design Add and Search Words Data Structure

## Problem

A word dictionary: `addWord` inserts; `search` matches with `'.'` wildcards (any single letter).

**Example:** add `bad`, `dad` → `search(".ad")` → `true`; `search("b..")` → `true`; `search("pad")` → `false`

## Walkthrough

0208's trie (this folder) with one addition: on a `.`, **fan out** — try every child of the current node and succeed if any branch completes the word. On a letter, descend as usual.

**[1] the trie after adds**
```text
root
├─ b ─ a ─ d ✓
├─ d ─ a ─ d ✓
└─ m ─ a ─ d ✓
```

**[2] search ".ad" — wildcard fans at level 0**
```text
'.' tries b, d, m — each walks a→d→flag ✓ → True
```

**[3] search "b.." — wildcard mid-word**
```text
b fixed, then '.' tries a → then '.' tries d → ✓ True
```

**[4] search "pad" — p has no node**
```text
root.children has no p → False immediately
```

**[5] cost of the fan-out**
```text
k wildcards × branching ≤ 26^k paths — fine at word lengths ≤ 25;
the trie prunes to real branches only, so it's far from worst case
```

Why it works: `.` denotes "any letter here" — exactly the union over the node's children of "continue matching there", which is the DFS recurrence. The trie shares prefixes, so the wildcard fan-out only visits letters that actually exist at that depth. addWord O(L); search O(L) without dots, up to 26^k in the worst case with k dots (the bound people quote, rarely hit).
