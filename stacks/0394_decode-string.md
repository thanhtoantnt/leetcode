# 394 — Decode String

## Problem

`k[encoded]` means the encoded string repeats k times. Decode the whole thing. (`s = "3[a2[c]]"` → `"accaccacc"`)

## Walkthrough

One pass with two stacks — a **string stack** and a **count stack**: on `[`, freeze the string built so far and its multiplier; on `]`, pop both and append the repetition to the thawed prefix. Multi-digit numbers accumulate digit by digit.

**[1] scan "3" then "["**
```text
[3, [, a, 2, [, c, ], ]]
k=3 cur=''  on '[': push (cur='') and k=3 → cur resets
```

**[2] inside: "a2" then "["**
```text
[3, [, a, 2, [, c, ], ]]
k=2 cur='a'  on '[': push ('a', 2) → cur=''
```

**[3] "c" then "]"**
```text
[3, [, a, 2, [, c, ], ]]
cur='c'  on ']': pop ('a',2) → cur='a'+'c'·2 = 'acc'
```

**[4] outer "]"**
```text
[3, [, a, 2, [, c, ], ]]
on ']': pop ('', 3) → cur = '' + 'acc'·3 = 'accaccacc'
```

**[5] done**
```text
return "accaccacc" ✓
```

Why it works: brackets nest, and the stack holds exactly the suspended outer contexts (prefix string + pending multiplier) in nesting order — the machine-level version of recursion, where `]` is the return from a recursive call that builds the repeated unit. O(output length) time; digits build via `k = k·10 + d` for multi-digit counts like `12[ab]`.
