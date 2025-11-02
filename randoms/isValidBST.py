# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkRange(self, root, minVal, right):
        if root == None:
            return True
        
        if root.val >= right or root.val <= minVal:
            return False
        
        if self.checkRange(root.left, minVal, root.val) == False:
            return False

        if self.checkRange(root.right, root.val, right) == False:
            return False
        
        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkRange(root, float("-inf"), float("inf"))