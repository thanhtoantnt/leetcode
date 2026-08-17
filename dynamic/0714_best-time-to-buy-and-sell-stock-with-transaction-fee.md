# 714 — Best Time to Buy and Sell Stock with Transaction Fee

## Problem

Unlimited trades; each **sell** pays a flat `fee`. Maximize profit.

**Example:** `prices = [1,3,2,8,4,9]`, `fee = 2` → `8` (buy 1 sell 8 → +5; buy 4 sell 9 → +3)

## Walkthrough

0309's state machine (this folder), cooldown edge swapped for a fee on the sell: `hold` = best profit while owning, `cash` = best while free. Buy moves `cash − p` into hold; sell moves `hold + p − fee` back.

**[1] day 0: price 1**
```text
hold=-1 cash=0  buy at 1
```

**[2] day 1: price 3**
```text
hold=-1 cash=0  selling nets 3−1−2=0 — no gain, stay
```

**[3] day 3: price 8 — sell**
```text
hold=-1 cash=5  8−1−2=5 > 0 → sell ✓
```

**[4] day 4: price 4 — rebuy**
```text
hold=1 cash=5  5−4=1: buy with the banked profit
```

**[5] day 5: price 9 — final sale**
```text
hold=1 cash=1+9−2=8 ✓ return 8
```

Why it works: the two states summarize everything the future depends on (owning or not); every transition is either forced or dominated, so the running maxima are optimal — the fee simply lowers the sell edge, and pairs of trades only fire when the spread clears it. O(n) time, O(1) space. The trilogy complete: 0122 (no constraints), 0309 (cooldown), this.
