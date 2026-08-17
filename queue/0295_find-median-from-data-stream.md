# 295 — Find Median from Data Stream

## Problem

A stream of numbers: report the median of everything seen so far, efficiently per insert.

**Example:** add 1, 2, 3 → median `2`; add 4 → median `2.5`

## Walkthrough

**Two heaps split the data in half**: a max-heap `lo` holding the smaller half, a min-heap `hi` the larger half, sizes balanced (lo may hold one extra). The median lives at the heap tops — both sides' extreme elements, O(1) to read.

**[1] add 1 → goes to lo**
```text
lo=[1]  hi=[]
new value always enters lo first, then the balancing shuffles
```

**[2] the two-step pipeline: push to lo, move lo's max to hi**
```text
lo=[]  hi=[1]
every insert crosses lo→hi once — guarantees the order invariant
```

**[3] rebalance: hi too big → move hi's min back**
```text
lo=[1]  hi=[]
sizes: lo gets the extra when odd — median candidate is lo's top
```

**[4] after 2 and 3 land**
```text
lo=[2,1?]  hi=[3]   (lo as max-heap: top=2)
median = 2.0 ✓ — lo's top, the middle element
```

**[5] add 4 — even count**
```text
lo top = 2, hi top = 3 → (2+3)/2 = 2.5 ✓
```

Why it works: the median only ever needs the middle one-or-two elements — heaps maintain exactly those extremes as tops, while the size invariant fixes which side owns the middle. Insert = O(log n) (three heap ops), median = O(1). The one-shot version is 0215-style quickselect (queue/); this is the streaming upgrade. A balanced BST with order statistics (CLRS Ch. 14) does the same at O(log n) with more machinery.
