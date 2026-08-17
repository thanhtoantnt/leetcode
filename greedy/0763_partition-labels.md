# 763 — Partition Labels

## Problem

Cut the string into as many parts as possible so **each letter appears in exactly one part**; return part sizes.

**Example:** `s = "ababcbacadefegdehijhklij"` → `[9,7,8]`

## Walkthrough

Precompute each letter's **last occurrence**. Sweep with a running frontier `reach = max(last[ch])` — the current part cannot close before `i` catches up to the frontier, because some letter inside still reappears later. The moment `i == reach`, close the part.

**[1] last occurrences (abridged)**
```text
a→8  b→5  c→7  d→14  e→15  …  h→19  i→22  j→23
```

**[2] sweep — frontier climbs to 8**
```text
ababcbac…
reach starts at last[a]=8; the b's and c's inside end earlier (5, 7)
```

**[3] i = 8 — frontier met, part closes**
```text
|ababcbaca|  size 9 — no letter in it occurs past 8 ✓
```

**[4] next part — d/e push the frontier**
```text
defegde  reach = max(14, 15, …) = 15 → closes at 15, size 7
```

**[5] the tail**
```text
hijhklij  reach = 23 = last index → closes, size 8 → [9, 7, 8] ✓
```

Why it works: a part is closable at i iff every letter seen in it has its last occurrence ≤ i — `reach` is exactly the max of those lasts, so the equality test is the complete closability check, and closing at the first such i maximizes the count (any later close only merges parts). Merge-intervals (0056) in disguise: each letter is the interval [first, last], parts are the merged gaps. O(n).
