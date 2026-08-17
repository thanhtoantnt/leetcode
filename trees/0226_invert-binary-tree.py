from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Invert a binary tree (mirror it): swap every node's children.

        Top-down swap; recursion order doesn't matter since each node's
        swap is independent of its descendants'.
        O(n) time, O(h) space.
        """
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


if __name__ == "__main__":
    t = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    r = Solution().invertTree(t)
    assert r.left.val == 7 and r.right.val == 2 and r.left.left.val == 9
    print("ok")
