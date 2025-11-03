from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the right side view of a binary tree.
        
        Problem Understanding:
        - Imagine standing on the right side of the tree
        - Return the values of the nodes you can see from top to bottom
        - For each level, only the rightmost node is visible
        
        Approach:
        - Use level-order traversal (BFS)
        - For each level, process all nodes and record the last (rightmost) node
        - Add the value of the rightmost node at each level to result
        - Process nodes level by level using queue
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(w) where w is the maximum width of the tree
        
        Args:
            root: Root of the binary tree
            
        Returns:
            List of values visible from the right side
        """
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            level_size = len(queue)
            
            # Process all nodes at current level
            for i in range(level_size):
                node = queue.pop(0)
                
                # If this is the last node in current level, it's visible from right
                if i == level_size - 1:
                    result.append(node.val)
                
                # Add children for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result

def run_right_side_view_test(root, expected, test_name):
    """
    Tests the rightSideView function.
    
    Args:
        root: Root of the binary tree to test
        expected: Expected right side view
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.rightSideView(root)
    
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
run_right_side_view_test(create_tree_from_list([1,2,3,None,5,None,4]), [1,3,4], "Example 1: [1,2,3,null,5,null,4] -> [1,3,4]")
run_right_side_view_test(create_tree_from_list([1,None,3]), [1,3], "Example 2: [1,null,3] -> [1,3]")
run_right_side_view_test(None, [], "Edge case: Empty tree -> []")
run_right_side_view_test(create_tree_from_list([1,2,3,4]), [1,3,4], "Edge case: [1,2,3,4] -> [1,3,4]")
run_right_side_view_test(create_tree_from_list([1,2,3,None,5,6,None,7]), [1,3,6,7], "Edge case: Complex tree -> [1,3,6,7]")
run_right_side_view_test(create_tree_from_list([1]), [1], "Edge case: Single node -> [1]")
run_right_side_view_test(create_tree_from_list([1,2]), [1,2], "Edge case: Root with left child -> [1,2]")
run_right_side_view_test(create_tree_from_list([1,None,2]), [1,2], "Edge case: Root with right child -> [1,2]")
run_right_side_view_test(create_tree_from_list([1,2,3,4,5,6,7]), [1,3,7], "Edge case: Complete binary tree -> [1,3,7]")
run_right_side_view_test(create_tree_from_list([1,2,None,3,None,None,None,4]), [1,2,3,4], "Edge case: Left-skewed tree -> [1,2,3,4]")