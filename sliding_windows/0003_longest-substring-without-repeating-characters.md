# 3 — Longest Substring Without Repeating Characters, visualized

Mirrors `SolutionOpt.lengthOfLongestSubstring` in the `.py` next to this file.
Input `s = "abcba"`. Window `[left, right]` stays duplicate-free; `char_map` remembers each char's last index.

**[1] right=0 'a' — new char, window grows**
```text
[a  b  c  b  a]
 LR
left=0 right=0   map={a:0}                max=1
```

**[2] right=1 'b' — new char, window grows**
```text
[a  b  c  b  a]
 L  R
left=0 right=1   map={a:0,b:1}            max=2
```

**[3] right=2 'c' — new char, window grows**
```text
[a  b  c  b  a]
 L     R
left=0 right=2   map={a:0,b:1,c:2}        max=3
```

**[4] right=3 'b' — DUPLICATE: b was at 1, inside window → jump left past it**
```text
[a  b  c  b  a]
       L  R
left=2 right=3   map={a:0,b:3,c:2}        max=3   window="cb"
```

**[5] right=4 'a' — 'a' at 0 exists in map, but 0 < left → NOT in window, no jump**
```text
[a  b  c  b  a]
       L     R
left=2 right=4   map={a:4,b:3,c:2}        max=3   window="cba"
```

**Result: 3** (`"abc"` or `"cba"`).

The two cases everyone trips on: [4] duplicate *inside* window → jump `left`; [5] stale index *outside* window → ignore. That's the `char_map[char] >= left` check.
