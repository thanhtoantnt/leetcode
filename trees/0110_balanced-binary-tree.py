from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """Is the tree height-balanced (subtree heights differ ≤ 1 everywhere)?

        Post-order DFS returning -1 as a "unbalanced" sentinel: compute
        child heights once, check |Δ|, propagate. O(n), no re-computation
        (the naive top-down version is O(n²) on a degenerate tree).
        """
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lh = height(node.left)
            if lh == -1:
                return -1
            rh = height(node.right)
            if rh == -1:
                return -1
            if abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)

        return height(root) != -1


if __name__ == "__main__":
    ok = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    bad = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
    assert Solution().isBalanced(ok)
    assert not Solution().isBalanced(bad)
    print("ok")
