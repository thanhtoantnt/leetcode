# 7 — Reverse Integer

## Problem

Reverse the digits of a signed 32-bit integer. If the result overflows the 32-bit range `[−2³¹, 2³¹−1]`, return `0`.

**Example:** `x = 123` → `321`

## Walkthrough

Pop digits off the back with `x % 10`, push onto `rev` with `rev = rev·10 + digit`. The only real work is the overflow check — done **before** the push.

`x = 123`

**[1] start**
```text
[1, 2, 3]
    i
rev=0 x=123  pop the last digit
```

**[2] pop 3**
```text
[1, 2, 3]
       i
rev=3 x=12  rev = 0·10 + 3, digit consumed with x //= 10
```

**[3] pop 2**
```text
[1, 2, 3]
    i
rev=32 x=1  digits so far: 32
```

**[4] pop 1 — done**
```text
[1, 2, 3]
 i
rev=321 x=0  return 321
```

**[5] the overflow guard**
```text
[4, 6, 3, 8, 4, 7, 4, 1, 2]
rev=146384741  next push would make 1463847412 > 2³¹−1 = 2147483647 → return 0
```

Why the check *before* pushing: in languages with fixed ints, `rev·10 + digit` itself may already overflow and wrap — unrepresentable garbage you can't test afterwards. Compare `rev > (2³¹−1 − digit) / 10` first (and the negative mirror for `INT_MIN`). Python's big ints survive the wrap, but the algorithm must still enforce the 32-bit contract.
