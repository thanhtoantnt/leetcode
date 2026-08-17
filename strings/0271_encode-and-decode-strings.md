# 271 — Encode and Decode Strings (premium)

## Problem

Encode a list of strings to a single string, then decode it losslessly — any characters allowed, empty strings included. *Paraphrased from LeetCode 271 (premium).*

**Example:** `["hello","world:","3:#nested"]` → `"5:hello6:world:8:3:#nested"` → decoded identical.

## Walkthrough

**Length-prefix framing**: write `len:` before each payload. The decoder reads digits up to the first `:`, takes exactly that many characters, repeats — the count makes the payload self-delimiting, so `:` or `#` inside strings can't confuse the parse.

**[1] encode "hello"**
```text
"5:hello"   header = decimal length + ':'
```

**[2] encode a hostile payload "3:#nested"**
```text
"8:3:#nested"   the inner "3:#" is inert — the outer 8 already fixed
the byte count
```

**[3] the full frame stream**
```text
5:hello 6:world: 8:3:#nested 0:   (0: marks the empty string)
```

**[4] decode — read header, jump payload**
```text
i=0: ':' at 1, len 5 → take chars 2..6 "hello", i=7
i=7: len 6 → "world:", i=15 …  headers consumed, payloads skipped verbatim
```

**[5] why naive join + split fails**
```text
"hello#world".split("#") can't tell payload delimiters from data —
lengths restore the information the delimiter loses
```

Why it works: the length header is a complete specification of each record's extent — decoding never inspects payload bytes, only counts them, making the code injective on lists. This is TCP-style framing (TLV without the type), the same self-delimiting idea as 0297's null-marker serialization (trees/). O(total) both directions.
