# 309 — Best Time to Buy and Sell Stock with Cooldown

## Problem

Buy/sell one share at a time; after **selling** you must cool down one day. Maximize profit.

**Example:** `prices = [1,2,3,0,2]` → `3` (buy 1, sell 2 — cooldown — buy 0, sell 2)

## Walkthrough

State machine, one state per day: `hold` (own stock), `sold` (just sold — cooling), `rest` (free to buy). Transitions: hold ← keep holding or buy from rest; sold ← sell from hold; rest ← stay resting or exit cooldown.

**[1] day 0: price 1**
```text
[1, 2, 3, 0, 2]
  i
hold=-1 sold=0 rest=0  buy at 1 → hold = −1
```

**[2] day 1: price 2**
```text
[1, 2, 3, 0, 2]
     i
hold=-1 sold=1 rest=0  sell → profit 1
```

**[3] day 2: price 3 — cooldown bites**
```text
[1, 2, 3, 0, 2]
        i
hold=-1 sold=2 rest=1  selling again needs a buy first; rest exits cooldown
```

**[4] day 3: price 0 — rebuy the dip**
```text
[1, 2, 3, 0, 2]
           i
hold=1 sold=2 rest=2  buy at 0 from rest: rest−0 = 2 → hold = 2
```

**[5] day 4: price 2 — final sale**
```text
[1, 2, 3, 0, 2]
              i
hold=2 sold=4 rest=2  sell: 2+2 = 4 → return 4
```

Why it works: the three states capture everything the future is allowed to depend on (owning, cooling, free) — the cooldown is simply the *missing* edge from sold straight back to hold/buy. Each day is O(1) work over the states → O(n) total, O(1) space (three rolling scalars). The classic trilogy: 122 (no cooldown, greedy adjacent diffs), this, and 714 (with fees) all share this machine.
