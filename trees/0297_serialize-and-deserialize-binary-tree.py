from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    """Serialize/deserialize a binary tree via preorder with null markers.

    "1,2,#,4,#,#,3,#,#" — '#' for nulls makes the preorder unambiguous
    (each parser step consumes exactly one token). O(n) both ways.
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        out = []

        def walk(node: Optional[TreeNode]) -> None:
            if not node:
                out.append("#")
                return
            out.append(str(node.val))
            walk(node.left)
            walk(node.right)

        walk(root)
        return ",".join(out)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = iter(data.split(","))

        def build() -> Optional[TreeNode]:
            val = next(tokens)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()


if __name__ == "__main__":
    t = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    c = Codec()
    s = c.serialize(t)
    r = c.deserialize(s)
    assert r.val == 1 and r.left.val == 2 and r.right.left.val == 4
    assert c.deserialize(c.serialize(None)) is None
    print("ok")
