# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Counts the number of 'good' nodes in a binary tree.
        
        Problem Understanding:
        - A node X is 'good' if in the path from root to X there are no nodes with a value greater than X
        - Root is always considered good (path contains only itself)
        - Need to track the maximum value seen so far in each path
        
        Approach:
        - Use depth-first search (DFS) with recursion
        - Keep track of the maximum value encountered in the current path
        - A node is good if its value is >= maximum value in the path to it
        - Update the maximum when traversing to children
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(h) where h is the height of the tree (recursion stack)
        
        Args:
            root: Root of the binary tree
            
        Returns:
            Number of good nodes in the tree
        """
        def dfs(node, max_so_far):
            if not node:
                return 0
            
            # Count current node if it's good (value >= max in path)
            good = 1 if node.val >= max_so_far else 0
            
            # Update max for children (current node's value if it's greater)
            new_max = max(max_so_far, node.val)
            
            # Recursively count good nodes in left and right subtrees
            good += dfs(node.left, new_max)
            good += dfs(node.right, new_max)
            
            return good
        
        # Start DFS with root's value as initial maximum (root is always good)
        return dfs(root, root.val) if root else 0

def run_good_nodes_test(root, expected, test_name):
    """
    Tests the goodNodes function.
    
    Args:
        root: Root of the binary tree to test
        expected: Expected number of good nodes
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.goodNodes(root)
    
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
run_good_nodes_test(create_tree_from_list([3,1,4,3,None,1,5]), 4, "Example 1: [3,1,4,3,null,1,5] -> 4 good nodes (3,4,3,5)")
run_good_nodes_test(create_tree_from_list([3,3,None,4,2]), 3, "Example 2: [3,3,null,4,2] -> 3 good nodes (3,3,4)")
run_good_nodes_test(create_tree_from_list([1]), 1, "Edge case: Single node -> 1 good node")
run_good_nodes_test(create_tree_from_list([1,2,3,4,5,6,7]), 7, "Edge case: All increasing -> 7 good nodes")
run_good_nodes_test(create_tree_from_list([7,5,6,4]), 3, "Edge case: [7,5,6,4] -> 3 good nodes (7,5,6)")
run_good_nodes_test(create_tree_from_list([9,5,6,4,10]), 4, "Edge case: [9,5,6,4,10] -> 4 good nodes (9,5,6,10)")
run_good_nodes_test(create_tree_from_list([2,2,2]), 1, "Edge case: All same values -> 1 good node (root only)")
run_good_nodes_test(create_tree_from_list([1,2,3,4,5,6,7,8,9,10]), 10, "Edge case: Strictly increasing path -> 10 good nodes")
run_good_nodes_test(create_tree_from_list([10,9,8,7,6,5,4]), 1, "Edge case: Strictly decreasing -> 1 good node (root only)")
run_good_nodes_test(create_tree_from_list([5,4,6,3,7,2,8]), 4, "Edge case: [5,4,6,3,7,2,8] -> 4 good nodes (5,6,7,8)")