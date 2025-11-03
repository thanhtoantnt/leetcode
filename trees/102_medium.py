from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        Returns the level order traversal of a binary tree's nodes' values.
        
        Problem Understanding:
        - Level order traversal visits nodes level by level from left to right
        - Each level's nodes should be grouped in a separate list
        - Return a list of lists containing the values at each level
        
        Approach:
        - Use breadth-first search (BFS) with a queue
        - Process nodes level by level
        - For each level, process all nodes currently in queue
        - Add their children to queue for next level processing
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(w) where w is the maximum width of the tree (queue storage)
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List of lists containing level order traversal
        """
        if not root:
            return []
        
        result = []
        queue = [root]  # Use list as queue (for simplicity)
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.pop(0)  # Dequeue
                current_level.append(node.val)
                
                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add current level to result
            result.append(current_level)
        
        return result

from typing import List, Optional

def run_level_order_test(root, expected, test_name):
    """
    Tests the levelOrder function.
    
    Args:
        root: Root of the binary tree to test
        expected: Expected level order traversal
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.levelOrder(root)
    
    print(f"{test_name}:")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Helper function to create trees
def create_tree_from_list(nodes):
    """Creates a binary tree from level-order list representation (None for missing nodes)"""
    if not nodes:
        return None
    
    from collections import deque
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(nodes):
        node = queue.popleft()
        
        # Left child
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    
    return root

# Run test cases
run_level_order_test(create_tree_from_list([3,9,20,None,None,15,7]), [[3],[9,20],[15,7]], "Example 1: [3,9,20,null,null,15,7] -> [[3],[9,20],[15,7]]")
run_level_order_test(create_tree_from_list([1]), [[1]], "Example 2: [1] -> [[1]]")
run_level_order_test(None, [], "Edge case: Empty tree -> []")
run_level_order_test(create_tree_from_list([1,2,3,4,5,6,7]), [[1],[2,3],[4,5,6,7]], "Edge case: Complete binary tree")
run_level_order_test(create_tree_from_list([1,2,None,3,None,4]), [[1],[2],[3],[4]], "Edge case: Left-skewed tree")
run_level_order_test(create_tree_from_list([1,None,2,None,3,None,4]), [[1],[2],[3],[4]], "Edge case: Right-skewed tree")
run_level_order_test(create_tree_from_list([1,2,3,4,None,None,5]), [[1],[2,3],[4,5]], "Edge case: Asymmetric tree")
run_level_order_test(create_tree_from_list([1,2,3,4,5,None,6,7,None,None,8]), [[1],[2,3],[4,5,6],[7,8]], "Edge case: Complex tree")
run_level_order_test(create_tree_from_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]), [[1],[2,3],[4,5,6,7],[8,9,10,11,12,13,14,15]], "Edge case: Full binary tree")
run_level_order_test(create_tree_from_list([1,None,2,None,3,None,4,None,5]), [[1],[2],[3],[4],[5]], "Edge case: Single path right")