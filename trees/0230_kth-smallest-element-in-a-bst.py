# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        """
        Finds the kth smallest element in a binary search tree.
        
        Problem Understanding:
        - Given a BST and integer k, return the kth smallest value (1-indexed)
        - In-order traversal of BST gives elements in sorted order
        
        Approach:
        - Use in-order traversal to visit nodes in ascending order
        - Keep count of visited nodes
        - When count reaches k, return that node's value
        - Can use iterative or recursive approach
        
        Time Complexity: O(H + k) where H is the height of the tree
        Space Complexity: O(H) for the recursion/stack space
        
        Args:
            root: Root of the binary search tree
            k: 1-indexed position of desired smallest element
            
        Returns:
            The kth smallest value in the BST
        """
        def inorder(node):
            if not node:
                return None
            
            # Visit left subtree
            left_result = inorder(node.left)
            if left_result is not None:
                return left_result
            
            # Process current node
            nonlocal count
            count += 1
            if count == k:
                return node.val
            
            # Visit right subtree
            return inorder(node.right)
        
        count = 0
        return inorder(root)

def run_kth_smallest_test(root, k, expected, test_name):
    """
    Tests the kthSmallest function.
    
    Args:
        root: Root of the binary search tree to test
        k: 1-indexed position of desired smallest element
        expected: Expected kth smallest value
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.kthSmallest(root, k)
    
    print(f"{test_name}:")
    print(f"  Input: k = {k}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Helper function to create trees
def create_tree_from_list(nodes):
    """Creates a BST from level-order list representation (None for missing nodes)"""
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
run_kth_smallest_test(create_tree_from_list([3,1,4,None,2]), 1, 1, "Example 1: [3,1,4,null,2], k=1 -> 1")
run_kth_smallest_test(create_tree_from_list([5,3,6,2,4,None,None,1]), 3, 3, "Example 2: [5,3,6,2,4,null,null,1], k=3 -> 3")
run_kth_smallest_test(create_tree_from_list([1]), 1, 1, "Edge case: Single node, k=1 -> 1")
run_kth_smallest_test(create_tree_from_list([2,1,3]), 2, 2, "Edge case: [2,1,3], k=2 -> 2")
run_kth_smallest_test(create_tree_from_list([5,3,6,2,4,1]), 1, 1, "Edge case: [5,3,6,2,4,1], k=1 -> 1")
run_kth_smallest_test(create_tree_from_list([5,3,6,2,4,1]), 6, 6, "Edge case: [5,3,6,2,4,1], k=6 -> 6")
run_kth_smallest_test(create_tree_from_list([1,2,3,4,5,6,7,8,9,10]), 5, 5, "Edge case: Sequential, k=5 -> 5")
run_kth_smallest_test(create_tree_from_list([10,5,15,3,7,12,18,1,4,6,8]), 4, 4, "Edge case: Larger BST, k=4 -> 4")
run_kth_smallest_test(create_tree_from_list([3,1,4,None,2]), 3, 3, "Edge case: [3,1,4,null,2], k=3 -> 3")
run_kth_smallest_test(create_tree_from_list([3,1,4,None,2]), 4, 4, "Edge case: [3,1,4,null,2], k=4 -> 4")