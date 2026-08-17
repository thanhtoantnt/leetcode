from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """Is subRoot an exact subtree (structure + values) of root?

        0100's same-tree check applied at every node of root.
        O(m·n) worst case; serialization + substring (KMP, Ch. 32) is
        the linear alternative.
        """

        def same(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True
            if not a or not b or a.val != b.val:
                return False
            return same(a.left, b.left) and same(a.right, b.right)

        if not root:
            return False
        return same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


if __name__ == "__main__":
    big = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    small = TreeNode(4, TreeNode(1), TreeNode(2))
    assert Solution().isSubtree(big, small)
    assert not Solution().isSubtree(big, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(9))))
    print("ok")
