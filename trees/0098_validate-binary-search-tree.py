# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Determines if a binary tree is a valid Binary Search Tree (BST).
        
        Problem Understanding:
        - A valid BST satisfies the following properties:
          1. Left subtree of a node contains only nodes with keys less than node's key
          2. Right subtree of a node contains only nodes with keys greater than node's key
          3. Both left and right subtrees must also be binary search trees
        - No duplicate values allowed in a BST
        
        Approach:
        - Use recursive validation with bounds
        - For each node, check if its value is within valid range (min, max)
        - When going left, update max bound to current node's value
        - When going right, update min bound to current node's value
        - Start with (-inf, +inf) as initial bounds
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree (recursion stack)
        
        Args:
            root: Root of the binary tree
            
        Returns:
            True if the tree is a valid BST, False otherwise
        """
        def validate(node, min_val, max_val):
            # Empty tree is valid
            if not node:
                return True
            
            # Check if current node violates BST property
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively validate left and right subtrees with updated bounds
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))

def run_bst_test(root, expected, test_name):
    """
    Tests the isValidBST function.
    
    Args:
        root: Root of the binary tree to test
        expected: Expected result (True/False)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.isValidBST(root)
    
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
run_bst_test(create_tree_from_list([2,1,3]), True, "Example 1: [2,1,3] -> True (valid BST)")
run_bst_test(create_tree_from_list([5,1,4,None,None,3,6]), False, "Example 2: [5,1,4,null,null,3,6] -> False (right subtree has smaller value)")
run_bst_test(create_tree_from_list([1]), True, "Edge case: Single node -> True")
run_bst_test(None, True, "Edge case: Empty tree -> True")
run_bst_test(create_tree_from_list([2,2,2]), False, "Edge case: All same values -> False (duplicates not allowed)")
run_bst_test(create_tree_from_list([1,2,3]), False, "Edge case: [1,2,3] -> False (left child > root)")
run_bst_test(create_tree_from_list([5,4,6,None,None,3,7]), False, "Edge case: [5,4,6,null,null,3,7] -> False (right subtree has smaller value)")
run_bst_test(create_tree_from_list([10,5,15,3,7,13,18]), True, "Edge case: Valid BST with multiple levels")
run_bst_test(create_tree_from_list([1,1]), False, "Edge case: Two same values -> False")
run_bst_test(create_tree_from_list([5,4,6,3,7,None,None,2,8]), False, "Edge case: [5,4,6,3,7,null,null,2,8] -> False (8 is too large for left subtree)")
run_bst_test(create_tree_from_list([0,-1]), True, "Edge case: Negative and zero -> True")
run_bst_test(create_tree_from_list([0,None,-1]), True, "Edge case: Root 0, right -1 -> False (should be False, right < root)")