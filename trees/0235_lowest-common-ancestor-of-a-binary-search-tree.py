# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Finds the lowest common ancestor (LCA) of two given nodes in a binary search tree.
        
        Problem Understanding:
        - Given a BST and two nodes p and q
        - Find the lowest node that has both p and q as descendants
        - A node can be a descendant of itself
        
        Approach:
        - Use the properties of BST: left subtree < root < right subtree
        - If both p and q are less than root, LCA is in left subtree
        - If both p and q are greater than root, LCA is in right subtree
        - If p and q are on different sides of root, or one equals root, then root is LCA
        - Iterative approach is efficient and intuitive
        
        Time Complexity: O(h) where h is the height of the tree
        Space Complexity: O(1) for iterative approach
        
        Args:
            root: Root of the binary search tree
            p: First target node
            q: Second target node
            
        Returns:
            The lowest common ancestor node
        """
        # Start from root and navigate based on BST properties
        current = root
        
        while current:
            # If both p and q are smaller than current, go left
            if p.val < current.val and q.val < current.val:
                current = current.left
            # If both p and q are greater than current, go right
            elif p.val > current.val and q.val > current.val:
                current = current.right
            # If p and q are on different sides, or one equals current, current is LCA
            else:
                return current
        
        return None  # This should not happen given the constraints

def run_lca_test(root, p_val, q_val, expected_val, test_name):
    """
    Tests the lowestCommonAncestor function.
    
    Args:
        root: Root of the binary search tree
        p_val: Value of first target node
        q_val: Value of second target node
        expected_val: Expected value of LCA
        test_name: Name/description of the test case
    """
    # Find nodes p and q in the tree
    def find_node(root, val):
        if not root:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return find_node(root.left, val)
        else:
            return find_node(root.right, val)
    
    p = find_node(root, p_val)
    q = find_node(root, q_val)
    
    solution = Solution()
    result = solution.lowestCommonAncestor(root, p, q)
    
    result_val = result.val if result else None
    
    print(f"{test_name}:")
    print(f"  Input: root with p={p_val}, q={q_val}")
    print(f"  Expected: {expected_val}")
    print(f"  Got: {result_val}")
    print(f"  Pass: {result_val == expected_val}")
    print()

# Helper function to create BST
def create_bst_from_list(nodes):
    """Creates a BST from level-order list representation (None for missing nodes)"""
    if not nodes or nodes[0] is None:
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
run_lca_test(create_bst_from_list([6,2,8,0,4,7,9,None,None,3,5]), 2, 8, 6, "Example 1: BST [6,2,8,0,4,7,9,null,null,3,5], p=2, q=8 -> 6")
run_lca_test(create_bst_from_list([6,2,8,0,4,7,9,None,None,3,5]), 2, 4, 2, "Example 2: BST [6,2,8,0,4,7,9,null,null,3,5], p=2, q=4 -> 2")
run_lca_test(create_bst_from_list([2,1]), 2, 1, 2, "Edge case: [2,1], p=2, q=1 -> 2")
run_lca_test(create_bst_from_list([6,2,8,0,4,7,9,None,None,3,5]), 3, 5, 4, "Edge case: Same subtree, p=3, q=5 -> 4")
run_lca_test(create_bst_from_list([6,2,8,0,4,7,9,None,None,3,5]), 0, 9, 6, "Edge case: Farthest nodes, p=0, q=9 -> 6")
run_lca_test(create_bst_from_list([1]), 1, 1, 1, "Edge case: Single node, p=1, q=1 -> 1")
run_lca_test(create_bst_from_list([2,1,3]), 1, 3, 2, "Edge case: [2,1,3], p=1, q=3 -> 2")
run_lca_test(create_bst_from_list([5,3,6,2,4,None,None,1]), 1, 4, 3, "Edge case: Deep left subtree, p=1, q=4 -> 3")