# 122 — Best Time to Buy and Sell Stock II

## Problem

Unlimited transactions (buy before selling each time). Maximize total profit.

**Example:** `prices = [7,1,5,3,6,4]` → `7` (buy 1 sell 5, buy 3 sell 6)

## Walkthrough

The greedy collapse: since you may trade as often as you like, every **up-day's gain** is collectable — and no strategy can beat the sum of all rises, because any profitable trade spans only rises and skips falls. Sum the positive daily diffs.

**[1] daily diffs**
```text
[7, 1, 5, 3, 6, 4]
    -6 +4 -2 +3 -2
```

**[2] keep the rises**
```text
+4 (1→5) and +3 (3→6) → total 7
```

**[3] why skipping falls is free**
```text
holding through 5→3 loses 2; selling at 5 and rebuying at 3 keeps
both the +4 and dodges the −2 — unlimited trades make this legal
```

**[4] monotone climb**
```text
[1,2,3,4,5]: diffs +1+1+1+1 = 4 — equals buy-first-sell-last, of course
```

**[5] monotone fall**
```text
[7,6,4,3,1]: all diffs negative → 0 (never trade)
```

Why it works: profit telescopes — any schedule's total is a sum of (sell − buy) over disjoint intervals, each interval's gain being the sum of its daily rises; so max total ≤ sum of all positive diffs, and the day-trade-every-rise schedule achieves it exactly. O(n), O(1). The middle of the trilogy: 0121 (one trade), this, 0309 (cooldown, `dynamic/`), 0714 (fee).
