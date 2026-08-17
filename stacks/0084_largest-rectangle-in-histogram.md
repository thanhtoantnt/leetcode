# 84 — Largest Rectangle in Histogram

## Problem

Largest rectangle that fits under the histogram (width over consecutive bars, height = shortest bar inside).

**Example:** `heights = [2,1,5,6,2,3]` → `10` (bars 5,6 → 5-high, 2-wide)

## Walkthrough

Monotonic **increasing** stack of indices. When a bar shorter than the stack top arrives, the top's rectangle can't extend right any further — and its left boundary is the element beneath it on the stack. Pop, multiply height × width, repeat. A sentinel 0 at the end flushes everything.

**[1] stack builds: 2, then 1 pops 2**
```text
[2, 1, 5, 6, 2, 3, |0]
 S
bar 2 pushed; bar 1 < 2 → pop 2: left=-1, width=1-(-1)-1=1 → area 2; push 1
```

**[2] climb: 1, 5, 6 stack up**
```text
[2, 1, 5, 6, 2, 3, |0]
    S        T
increasing run 1,5,6 — nothing pops, heights rising
```

**[3] bar 2 arrives — 6 and 5 pop**
```text
[2, 1, 5, 6, 2, 3, |0]
pop 6: left=idx(5), width=4-2-1=1 → 6; pop 5: left=idx(1), width=4-1-1=2 → 10 ✓
```

**[4] continue: 2, 3 push**
```text
[2, 1, 5, 6, 2, 3, |0]
stack 1,2,3 — best so far 10
```

**[5] sentinel 0 flushes**
```text
[2, 1, 5, 6, 2, 3, |0]
pop 3: width 1 → 3; pop 2: width 3 → 6; pop 1: width 6 → 6 → return 10
```

Why it works: a bar's maximal rectangle extends exactly from the first shorter bar on its left (the stack element beneath after popping) to the first shorter bar on its right (the bar that triggered the pop) — the stack maintains precisely that "nearest smaller element" context. Each index pushed/popped once → O(n). The two-pass "nearest smaller left/right" arrays are the same algorithm unrolled; this is 0739's monotonic stack (this folder) in max-area clothing.
