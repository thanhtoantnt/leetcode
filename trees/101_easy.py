# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        Checks if a binary tree is symmetric (mirror of itself).
        
        Problem Understanding:
        - A binary tree is symmetric if the left subtree is a mirror reflection of the right subtree
        - Two trees are mirror reflections if:
          1. Their roots have the same value
          2. The right subtree of each tree is a mirror reflection of the left subtree of the other
        
        Approach:
        - Use recursive comparison of left and right subtrees
        - Compare left.left with right.right and left.right with right.left
        - Base cases: both nodes are None (symmetric) or one is None (not symmetric)
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree (recursion stack)
        
        Args:
            root: Root of the binary tree
            
        Returns:
            True if the tree is symmetric, False otherwise
        """
        def is_mirror(left, right):
            # Both nodes are None - symmetric
            if not left and not right:
                return True
            
            # One node is None, the other is not - not symmetric
            if not left or not right:
                return False
            
            # Check if current nodes have same value and subtrees are mirrors
            return (left.val == right.val and 
                    is_mirror(left.left, right.right) and 
                    is_mirror(left.right, right.left))
        
        # Handle empty tree case
        if not root:
            return True
        
        # Check if left and right subtrees are mirrors of each other
        return is_mirror(root.left, root.right)

def run_symmetric_test(root, expected, test_name):
    """
    Tests the isSymmetric function.
    
    Args:
        root: Root of the binary tree to test
        expected: Expected result (True/False)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.isSymmetric(root)
    
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
run_symmetric_test(create_tree_from_list([1,2,2,3,4,4,3]), True, "Example 1: [1,2,2,3,4,4,3] -> True (symmetric)")
run_symmetric_test(create_tree_from_list([1,2,2,None,3,None,3]), False, "Example 2: [1,2,2,null,3,null,3] -> False (not symmetric)")
run_symmetric_test(create_tree_from_list([1]), True, "Edge case: Single node -> True")
run_symmetric_test(None, True, "Edge case: Empty tree -> True")
run_symmetric_test(create_tree_from_list([1,2,3]), False, "Edge case: [1,2,3] -> False (asymmetric)")
run_symmetric_test(create_tree_from_list([1,2,2,2,None,2]), False, "Edge case: [1,2,2,2,null,2] -> False")
run_symmetric_test(create_tree_from_list([2,3,3,4,5,5,4,None,None,8,9,9,8]), True, "Edge case: Complex symmetric tree")
run_symmetric_test(create_tree_from_list([1,2]), False, "Edge case: Root with only left child -> False")
run_symmetric_test(create_tree_from_list([1,None,2]), False, "Edge case: Root with only right child -> False")
run_symmetric_test(create_tree_from_list([1,2,2,3,3,3,3]), True, "Edge case: [1,2,2,3,3,3,3] -> True")