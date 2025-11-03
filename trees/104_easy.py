# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        Finds the maximum depth of a binary tree.
        
        Problem Understanding:
        - Maximum depth is the number of nodes along the longest path 
          from the root node down to the farthest leaf node
        - A leaf node is a node with no children
        
        Approach:
        - Use recursive depth-first search
        - For each node, calculate the maximum depth of left and right subtrees
        - Return 1 (current node) + maximum of left and right subtree depths
        - Base case: if node is None, depth is 0
        
        Time Complexity: O(n) where n is the number of nodes (visit each node once)
        Space Complexity: O(h) where h is the height of the tree (recursion stack)
        
        Args:
            root: Root of the binary tree
            
        Returns:
            Maximum depth of the binary tree
        """
        # Base case: empty tree has depth 0
        if not root:
            return 0
        
        # Recursively find the depth of left and right subtrees
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # Return 1 (current node) + maximum of left and right depths
        return 1 + max(left_depth, right_depth)

def run_max_depth_test(root, expected, test_name):
    """
    Tests the maxDepth function.
    
    Args:
        root: Root of the binary tree to test
        expected: Expected maximum depth
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.maxDepth(root)
    
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
run_max_depth_test(create_tree_from_list([3,9,20,None,None,15,7]), 3, "Example 1: [3,9,20,null,null,15,7] -> 3")
run_max_depth_test(create_tree_from_list([1,None,2]), 2, "Example 2: [1,null,2] -> 2")
run_max_depth_test(None, 0, "Edge case: Empty tree -> 0")
run_max_depth_test(create_tree_from_list([1]), 1, "Edge case: Single node -> 1")
run_max_depth_test(create_tree_from_list([1,2]), 2, "Edge case: Root with left child -> 2")
run_max_depth_test(create_tree_from_list([1,None,2]), 2, "Edge case: Root with right child -> 2")
run_max_depth_test(create_tree_from_list([1,2,3,4]), 3, "Edge case: [1,2,3,4] -> 3")
run_max_depth_test(create_tree_from_list([1,2,None,3,None,4]), 4, "Edge case: Skewed left -> 4")
run_max_depth_test(create_tree_from_list([1,None,2,None,3,None,4]), 4, "Edge case: Skewed right -> 4")
run_max_depth_test(create_tree_from_list([1,2,3,4,5,6,7]), 3, "Edge case: Complete binary tree -> 3")
run_max_depth_test(create_tree_from_list([1,2,3,4,None,None,7,8]), 4, "Edge case: Unbalanced tree -> 4")
run_max_depth_test(create_tree_from_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]), 4, "Edge case: Full binary tree -> 4")