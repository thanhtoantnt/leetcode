# 150 — Evaluate Reverse Polish Notation

## Problem

Evaluate an expression in postfix notation: operands first, operator after (`"2,1,+,3,*"` = `(2+1)*3` = 9).

## Walkthrough

The stack rule: number → push; operator → pop two (second pop is the **left** operand), apply, push result. At the end the single stack item is the answer.

**[1] "2 1 +"**
```text
2 1
 S
stack=[2,1]  + arrives: pop 1, pop 2 → 2+1=3
```

**[2] after +**
```text
3
stack=[3]  push 3
```

**[3] "3" then "\*"**
```text
3 3
 S
stack=[3,3]  * arrives: 3×3=9
```

**[4] final**
```text
9
return 9 ✓ (2+1)*3
```

**[5] the operand-order trap: "1 2 −"**
```text
stack=[1,2]  − arrives: right=2, left=1 → 1−2 = −1 (not 1!)
```

Why it works: postfix places each operator immediately after its two operands, so by induction every sub-expression is a completed value sitting on the stack when its operator arrives — no precedence, no parentheses, no parsing grammar. O(n) with each value pushed/popped once. (The operator-precedence infix version is the shunting-yard algorithm; division truncates toward zero here, worth a `int(a/b)` in Python.)
