# 297 — Serialize and Deserialize Binary Tree

## Problem

Encode a binary tree to a string and rebuild the exact tree from it.

**Example:** `[1,2,3,null,null,4,5]` → `"1,2,#,#,3,4,#,#,5,#,#"` → the same tree.

## Walkthrough

**Preorder with null markers**: node, then left, then right, writing `#` for every empty child. The markers make preorder self-delimiting — deserialization consumes one token per recursive step and never needs lookahead or bounds.

**[1] serialize the left subtree**
```text
1
├─L 2       → "1,2,#,#" (2's two null children written)
└─R 3
```

**[2] serialize the right subtree**
```text
└─R 3
   ├─L 4     → "3,4,#,#,5,#,#"
   └─R 5
```

**[3] the full string**
```text
"1,2,#,#,3,4,#,#,5,#,#"
```

**[4] deserialize — rebuild in the same order**
```text
read 1 → read 2 → read # (2.left=null) → read # (2.right=null) → back up
read 3 → read 4 → ## → read 5 → ## — tree restored exactly ✓
```

**[5] why markers are mandatory**
```text
plain preorder "1,2,3" is ambiguous (many trees share it) — the #
count pins every missing child, making the encoding a bijection
```

Why it works: preorder + explicit nulls is a bijective encoding — each recursive call consumes a fixed prefix of the token stream (value + two complete subtree encodings), so the rebuild mirrors the write deterministically. O(n) both directions. BFS level-order works too; 0105's preorder+inorder reconstruction is the marker-free cousin that needs a second sequence. Tries (208) serialize the same way over words.
