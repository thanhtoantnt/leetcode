# 739 — Daily Temperatures

## Problem

Given daily temperatures, return an array where `answer[i]` is how many days you wait after day `i` until a warmer day. If none ever comes, `answer[i] = 0`.

**Example:** `temperatures = [73,74,75,71,69,72,76,73]` → `[1,1,4,2,1,1,0,0]`

## Walkthrough

Monotonic **decreasing** stack of `(day, temp)`. When a warm day arrives, it resolves every colder day on the stack — pop and record the distance.

**[1] day 0, temp 73**
```text
T:     73 74 75 71 69 72 76 73
       i
ans:   0 0 0 0 0 0 0 0
stack: 73
stack empty → push (0, 73)
```

**[2] day 1, temp 74**
```text
T:     73 74 75 71 69 72 76 73
          i
ans:   1 0 0 0 0 0 0 0
stack: 74
74 > 73 → pop day 0, ans[0] = 1-0 = 1, push
```

**[3] day 2, temp 75**
```text
T:     73 74 75 71 69 72 76 73
             i
ans:   1 1 0 0 0 0 0 0
stack: 75
75 > 74 → pop day 1, ans[1] = 1
```

**[4] days 3–4, cooling off**
```text
T:     73 74 75 71 69 72 76 73
                   i
ans:   1 1 0 0 0 0 0 0
stack: 75 71 69
71 and 69 are colder → nobody pops, just stack up
```

**[5] day 5, temp 72**
```text
T:     73 74 75 71 69 72 76 73
                      i
ans:   1 1 0 2 1 0 0 0
stack: 75 72
72 > 69 → ans[4]=1; 72 > 71 → ans[3]=2; 72 < 75 → stop
```

**[6] day 6, temp 76 — the big one**
```text
T:     73 74 75 71 69 72 76 73
                         i
ans:   1 1 4 2 1 1 0 0
stack: 76
76 pops 72 (ans[5]=1) and 75 (ans[2]=4)
```

**[7] day 7, done**
```text
T:     73 74 75 71 69 72 76 73
                            i
ans:   1 1 4 2 1 1 0 0
stack: 76 73
73 < 76 → push. Days left on the stack never see warmer → stay 0
```

Why it works: each day is pushed once and popped at most once → O(n) total, versus the naive O(n²) rescan for every day.
