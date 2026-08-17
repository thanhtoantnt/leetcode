from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """Maximum sum along any path (any node to any node, no re-use).

        At each node the best path through it = val + best left gain +
        best right gain, with gains clamped at 0 (a negative subtree is
        walkable-but-ignored). The DFS returns only the single-side gain
        (val + max(left, right)) because a path may enter a node once.
        O(n) time, O(h) space.
        """
        best = -inf

        def gain(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            best = max(best, node.val + left + right)
            return node.val + max(left, right)

        gain(root)
        return best


if __name__ == "__main__":
    t = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert Solution().maxPathSum(t) == 42  # 15 + 20 + 7
    assert Solution().maxPathSum(TreeNode(-3)) == -3
    print("ok")
