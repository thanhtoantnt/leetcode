from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Longest path (edges) between any two nodes.

        Same shape as 0124 (max path sum): the DFS returns single-side
        depth; the through-node candidate left+right updates a global.
        O(n).
        """
        best = 0

        def depth(node: Optional[TreeNode]) -> int:
            nonlocal best
            if not node:
                return 0
            l = depth(node.left)
            r = depth(node.right)
            best = max(best, l + r)
            return 1 + max(l, r)

        depth(root)
        return best


if __name__ == "__main__":
    t = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert Solution().diameterOfBinaryTree(t) == 3  # 4→2→5 or 4→2→1→3
    print("ok")
