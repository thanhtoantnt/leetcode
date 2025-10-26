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

from collections import deque

class SolutionOpt:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            # The first node in the current level is the rightmost visible node
            result.append(queue[0].val)
            
            # Process all nodes in the current level
            for _ in range(level_size):
                node = queue.popleft()
                
                # Add right child first, then left (ensures rightmost node is first in next level)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return result