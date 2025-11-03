from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Constructs a binary tree from its preorder and inorder traversals.
        
        Problem Understanding:
        - Given preorder and inorder traversal arrays of the same tree
        - Preorder: Root, Left, Right
        - Inorder: Left, Root, Right
        - Build and return the binary tree
        
        Approach:
        - First element in preorder is always the root
        - Find root position in inorder to separate left and right subtrees
        - Elements to the left of root in inorder form left subtree
        - Elements to the right of root in inorder form right subtree
        - Recursively build left and right subtrees
        - Use hash map for O(1) lookup of root positions in inorder
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) for hash map and recursion stack
        
        Args:
            preorder: Preorder traversal of the binary tree
            inorder: Inorder traversal of the binary tree
            
        Returns:
            Root of the constructed binary tree
        """
        # Create a hash map to quickly find positions in inorder
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(pre_start, pre_end, in_start, in_end):
            # Base case: invalid range
            if pre_start > pre_end:
                return None
            
            # Root is the first element in current preorder range
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            
            # Find root position in inorder to separate left and right subtrees
            root_idx = inorder_map[root_val]
            
            # Calculate size of left subtree
            left_size = root_idx - in_start
            
            # Recursively build left and right subtrees
            root.left = build(
                pre_start + 1,           # Left subtree starts after root
                pre_start + left_size,   # Left subtree ends after left_size elements
                in_start,                # Left subtree starts at beginning of inorder range
                root_idx - 1             # Left subtree ends before root in inorder
            )
            
            root.right = build(
                pre_start + left_size + 1,  # Right subtree starts after left subtree
                pre_end,                    # Right subtree ends at end of preorder range
                root_idx + 1,               # Right subtree starts after root in inorder
                in_end                      # Right subtree ends at end of inorder range
            )
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

def run_build_tree_test(preorder, inorder, expected_inorder, test_name):
    """
    Tests the buildTree function by comparing inorder traversal of result.
    
    Args:
        preorder: Preorder traversal input
        inorder: Inorder traversal input
        expected_inorder: Expected inorder traversal of constructed tree
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.buildTree(preorder, inorder)
    
    # Helper function to get inorder traversal
    def get_inorder(root):
        if not root:
            return []
        return get_inorder(root.left) + [root.val] + get_inorder(root.right)
    
    result_inorder = get_inorder(result)
    
    print(f"{test_name}:")
    print(f"  Input: preorder = {preorder}, inorder = {inorder}")
    print(f"  Expected inorder: {expected_inorder}")
    print(f"  Got inorder: {result_inorder}")
    print(f"  Pass: {result_inorder == expected_inorder}")
    print()

# Run test cases
run_build_tree_test([3,9,20,15,7], [9,3,15,20,7], [9,3,15,20,7], "Example 1: [3,9,20,15,7], [9,3,15,20,7] -> tree with inorder [9,3,15,20,7]")
run_build_tree_test([-1], [-1], [-1], "Example 2: [-1], [-1] -> single node")
run_build_tree_test([1,2,3], [3,2,1], [3,2,1], "Edge case: Left-skewed tree")
run_build_tree_test([1,2,3], [1,2,3], [1,2,3], "Edge case: Right-skewed tree")
run_build_tree_test([1,2,4,5,3,6,7], [4,2,5,1,6,3,7], [4,2,5,1,6,3,7], "Edge case: Complex tree")
run_build_tree_test([1], [1], [1], "Edge case: Single node")
run_build_tree_test([1,2], [2,1], [2,1], "Edge case: Root with left child only")
run_build_tree_test([1,2], [1,2], [1,2], "Edge case: Root with right child only")
run_build_tree_test([3,1,2,4], [1,2,3,4], [1,2,3,4], "Edge case: Mixed tree")