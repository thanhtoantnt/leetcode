from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Structural and value equality of two binary trees.

        Compare nodes pairwise in lockstep: both null (equal leaf-gap),
        exactly one null, or values differ -> false; else recurse both sides.
        O(n) time, O(h) space.
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    a = TreeNode(1, TreeNode(2), TreeNode(3))
    b = TreeNode(1, TreeNode(2), TreeNode(3))
    assert Solution().isSameTree(a, b)
    assert not Solution().isSameTree(a, TreeNode(1, TreeNode(3), TreeNode(2)))
    print("ok")
