# 20 — Valid Parentheses

## Problem

Given a string of `()[]{}`, determine if it's valid: brackets closed in the right order, properly nested.

**Example:** `"([)]"` → `false` — `]` closes nothing open, because `(` is still waiting inside.

## Walkthrough

Push openers on a stack. Every closer must match the **most recent unmatched opener** — exactly the top of the stack. Empty stack at the end means everything got closed.

`s = "([)]"`

**[1] `(` — push**
```text
[(, [, ), )]
 i
stack=(  openers pile up
```

**[2] `[` — push**
```text
[(, [, ), )]
    i
stack=(,[  two open, nothing closed yet
```

**[3] `)` — top is `[`, wrong type**
```text
[(, [, ), )]
       i
stack=(,[  ')' expects '(' but '[' is on top → return False
```

The violation in one line: the *most recent* opener must be honored first — LIFO. `"( )"` interleaved with `"[ ]"` across each other can never work, though `"([])"` and `"()[]"` both do.

**[4] what a valid trace looks like — `"([])"`**
```text
[(, (, [, ), )]
 i
stack=(  then ( [ … then ) pops [, ] pops ( → empty → True
```

Two other failure modes to check: closer with empty stack (`")("`) and leftover openers at the end (`"("`). All three reduce to: match the top, and demand an empty stack at the end. O(n) time, O(n) worst-case space.
