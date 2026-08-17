from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        """LCA in a general binary tree (no BST property).

        Post-order: the LCA is the node where p and q split into
        different subtrees (or one equals the node itself). Return the
        non-null hit upward; two hits at one node = that node is the LCA.
        O(n).
        """
        if not root or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root  # p and q found in different subtrees — split point
        return left or right


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, TreeNode(0), TreeNode(8)))
    p, q = root.left, root.left.right.right  # 5 and 4
    assert Solution().lowestCommonAncestor(root, p, q).val == 5
    assert Solution().lowestCommonAncestor(root, root.left, root.right).val == 3
    print("ok")
