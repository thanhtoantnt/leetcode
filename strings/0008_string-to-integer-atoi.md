# 8 — String to Integer (atoi)

## Problem

Implement `atoi`: parse a leading integer from a string — optional whitespace, optional `+`/`−` sign, then digits. Return 0 if no valid number parses; clamp the result to `[−2³¹, 2³¹−1]`.

**Example:** `s = " -42"` → `-42`

## Walkthrough

A four-state scan: skip spaces, read the sign, accumulate digits, stop at the first non-digit. (`.` marks a space.)

**[1] skip leading whitespace**
```text
[., -, 4, 2]
 i
stage=spaces num=0  advance while the char is ' '
```

**[2] read the sign**
```text
[., -, 4, 2]
     i
sign=-1 num=0  '-' → sign = -1, consume exactly one
```

**[3] accumulate digits**
```text
[., -, 4, 2]
        i
sign=-1 num=4  num = 0·10 + 4
```

**[4] next digit**
```text
[., -, 4, 2]
           i
sign=-1 num=42  num = 4·10 + 2
```

**[5] end of string — apply sign and clamp**
```text
[., -, 4, 2]
sign=-1 num=42  → -42, within 32-bit range → return -42
```

Clamping: after the loop, `num` may exceed 2³¹−1 (Python never wraps). Return `max(−2³¹, min(2³¹−1, sign·num))`. Signs like `"+-12"` parse as 0 (only one sign allowed), and `"words"` stops with num=0 before any digit.
