# 269 — Alien Dictionary (premium)

## Problem

Words are sorted by an unknown alphabet. Reconstruct a valid letter order (or `""` if the ordering is contradictory). *Paraphrased from LeetCode 269, which is premium.*

**Example:** `["wrt","wrf","er","ett","rftt"]` → `"wertf"`

## Walkthrough

Each adjacent word pair yields **one constraint**: at their first differing character, the left word's letter precedes the right's (characters before the difference are useless — equal prefixes say nothing). Build the letter graph, then Kahn's topological sort (0210's flipbook, `graphs/`).

**[1] extract edges**
```text
wrt|wrf → t before f
wrt|er  → w before e
er|ett  → r before t
er…rftt → e before r
```

**[2] indegrees**
```text
indeg: w=0 e=1 r=1 t=2 f=1
queue=[w]  only w is free to start
```

**[3] peel w → e**
```text
out=w  e drops to 0 → queue=[e]
```

**[4] peel e → r → t → f**
```text
out=wertf  r drops when e pops, t when r pops, f when t pops
```

**[5] done — and the failure modes**
```text
len(out)=5=len(letters) → "wertf" ✓
cycle ["z","x","z"]: edges z→x, x→z → peel stalls → ""
prefix case ["abc","ab"]: "abc" longer but same prefix → invalid → ""
```

Why it works: the sort order of the word list is fully explained by the first-difference constraints (later characters only matter when earlier ones tie — dictionary order); any topological order of that letter graph satisfies every pair, and Kahn detects cycles exactly. O(total letters) — 0207/0210's machinery with a constraint-extraction prelude.
