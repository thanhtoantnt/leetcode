# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkSubtree(self, root: Optional[TreeNode], minVal, maxVal):
        if root == None:
            return True
        
        if root.val <= minVal or root.val >= maxVal:
            return False

        return self.checkSubtree(root.left, minVal, root.val) and self.checkSubtree(root.right, root.val, maxVal)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkSubtree(root, -float('inf'), float('inf'))
        