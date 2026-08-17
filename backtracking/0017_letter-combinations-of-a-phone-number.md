# 17 — Letter Combinations of a Phone Number

## Problem

Map digits 2–9 to phone keypad letters (`2→abc, 3→def, …`) and return all strings spelled by a digit sequence.

**Example:** `digits = "23"` → `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

## Walkthrough

A pure product tree: one tree level per digit, one branch per letter of that digit's key. DFS writes one letter per level; leaves are the answers.

**[1] level 0 — key 2 = abc**
```text
s=a
2: a b c  choosing a; b and c are sibling subtrees
```

**[2] level 1 — key 3 = def**
```text
s=ad
├─L a
│  └─R d  first leaf reached
```

**[3] sweep d, e, f under a**
```text
s=af
├─L a
│  ├─R d ✗ done
│  ├─R e ✗ done
│  └─R f ✗ done → pop, next letter of key 2
```

**[4] siblings b and c repeat the pattern**
```text
s=bd…cf
├─L b → bd be bf
└─L c → cd ce cf
```

**[5] all 9 leaves**
```text
ad ae af bd be bf cd ce cf
✓ 9 = 3·3  product of key sizes
```

Why it works: every combination picks exactly one letter per digit, and the tree makes exactly that choice at each level — the leaves are in bijection with the letter choices. Output size is the product of key sizes (up to 4ⁿ for 7/9). Iterative equivalent: fold a list with `for old in acc: for ch in key: append(old+ch)`.
