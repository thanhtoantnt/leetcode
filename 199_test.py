# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        queue = deque()
        queue.append(root)

        # results = [root.val]
        result = []

        while queue:
            result.append(queue[0].val)

            # add the children
            size = len(queue)
            for _ in range(size):
                element = queue.popleft()
                if element.right != None:
                    queue.append(element.right)

                if element.left != None:
                    queue.append(element.left)
        
        return result