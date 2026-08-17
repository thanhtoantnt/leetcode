# 678 — Valid Parenthesis String

## Problem

String of `(`, `)`, and `*`, where `*` may stand for `(`, `)`, or the empty string. Can it be a valid parentheses string?

**Example:** `"(*)"` → `true`; `"(*))"` → `true` (`*` = `(`); `"((*)"` → `false` — actually **true** (`*` = `)` gives `(())`); a real false: `"("*"` or `")*"`.

## Walkthrough

Track the **range** `[lo, hi]` of possible open-paren counts: `(` raises both bounds, `)` lowers both, `*` widens (lo−1, hi+1). The string dies if even the most generous reading goes negative (`hi < 0`); it succeeds iff the count can land exactly on 0 (`lo == 0` at the end).

**[1] scan "(*)" — char `(`**
```text
lo=1 hi=1   one open paren, certainly
```

**[2] char `*`**
```text
lo=0 hi=2   as ')': 0; as '(': 2 — anywhere between
```

**[3] char `)` — then end**
```text
lo=−1→0 (clamp)  hi=1   end: range [0,1] contains 0 ✓ → True
(the * was empty: "()" )
```

**[4] the false cases, both caught by the range**
```text
")*" : ) → hi=−1 < 0 → False at once (nothing rescues a leading closer)
"("  : end with lo=1 > 0 → no assignment closes it → False
```

**[5] "(*))" — the greedy reading**
```text
( [1,1]  * [0,2]  ) [−1→0,1]  ) [−1→0,0]  end lo=0 ✓ → True
the * must be '(' — "(( ))"
```

Why it works: the reachable open-counts after each prefix form a contiguous integer range (each step shifts or widens by ±1), so two scalars summarize all `3^k` wildcard assignments — `hi` is the most optimistic reading, `lo` the most conservative. `hi < 0` kills hopelessness early; `lo == 0` at the end means some assignment balances exactly. O(n) time, O(1) space — the wildcard-DP over counts collapsed to its min/max envelope.
