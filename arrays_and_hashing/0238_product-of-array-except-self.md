# 238 — Product of Array Except Self

## Problem

Given `nums`, return an array `answer` where `answer[i]` is the product of all elements except `nums[i]` — **no division allowed**, O(n).

**Example:** `nums = [1,2,3,4]` → `[24,12,8,6]`

## Walkthrough

Two passes. `pre[i]` = product of everything left of `i`; `suf[i]` = product of everything right of `i`. The answer is their pointwise product — each cell needs "left side × right side", never itself.

**[1] prefix pass, left to right**
```text
nums: 1 2 3 4
pre:  1 1 . .
suf:  . . . .
pre=1  pre[i] = product before i: start with 1, multiply as you go
```

**[2] prefix complete**
```text
nums: 1 2 3 4
pre:  1 1 2 6
suf:  . . . .
pre=6  pre = [1, 1·1, 1·2, 1·2·3]
```

**[3] suffix pass, right to left**
```text
nums: 1 2 3 4
pre:  1 1 2 6
suf:  . 2 1 1
suf=2  suf[i] = product after i, building up from 1 on the right
```

**[4] suffix complete**
```text
nums: 1 2 3 4
pre:  1 1 2 6
suf:  24 12 4 1
suf=24  suf = [2·3·4, 3·4, 4, 1]
```

**[5] multiply pointwise**
```text
nums: 1 2 3 4
pre:  1 1 2 6
suf:  24 12 4 1
ans:  24 12 8 6
ans=[24,12,8,6]  e.g. ans[2] = pre[2] · suf[2] = 2 · 4 = 8
```

Why it works: for index i, everything except nums[i] is exactly (all before i) × (all after i). Two linear scans, no division — which also makes it safe for zeros. In practice `pre` is written into the output array and `suf` kept as a running scalar → O(1) extra space.
