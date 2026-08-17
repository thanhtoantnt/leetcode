from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Determines if the given edges make up a valid tree.
        
        Problem Understanding:
        - A valid tree has exactly n-1 edges and is fully connected without cycles
        - Need to check two conditions:
          1. Number of edges is exactly n-1
          2. All nodes are connected (no disconnected components)
          3. No cycles exist
        
        Approach:
        - First check if number of edges equals n-1 (necessary condition for tree)
        - Use Union-Find (Disjoint Set Union) to detect cycles and check connectivity
        - For each edge, if endpoints are already connected, a cycle exists
        - After processing all edges, all nodes should be in one connected component
        
        Time Complexity: O(E * α(n)) where E is number of edges, α is inverse Ackermann function
        Space Complexity: O(n) for parent and rank arrays
        
        Args:
            n: Number of nodes
            edges: List of edges where each edge connects two nodes
            
        Returns:
            True if edges form a valid tree, False otherwise
        """
        # A tree with n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False
        
        # Special case: 0 nodes (empty tree) or 1 node (single node tree)
        if n <= 1:
            return True
        
        # Union-Find data structure
        parent = list(range(n))  # Each node is its own parent initially
        rank = [0] * n  # Rank for union by rank optimization
        
        def find(x):
            """Find root of x with path compression"""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Union by rank - returns False if x and y are already connected (cycle)"""
            root_x, root_y = find(x), find(y)
            
            if root_x == root_y:
                return False  # Already connected, adding this edge creates a cycle
            
            # Union by rank
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            
            return True
        
        # Process each edge
        for a, b in edges:
            if not union(a, b):
                return False  # Cycle detected
        
        return True  # Valid tree: n-1 edges and no cycles

def run_valid_tree_test(n, edges, expected, test_name):
    """
    Tests the validTree function.
    
    Args:
        n: Number of nodes
        edges: List of edges
        expected: Expected result (True/False)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.validTree(n, edges)
    
    print(f"{test_name}:")
    print(f"  Input: n = {n}, edges = {edges}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_valid_tree_test(5, [[0,1],[0,2],[0,3],[1,4]], True, "Example 1: 5 nodes, valid tree -> True")
run_valid_tree_test(5, [[0,1],[1,2],[2,3],[1,3],[1,4]], False, "Example 2: 5 nodes, has cycle -> False")
run_valid_tree_test(1, [], True, "Edge case: 1 node, no edges -> True")
run_valid_tree_test(2, [[0,1]], True, "Edge case: 2 nodes, 1 edge -> True")
run_valid_tree_test(2, [], False, "Edge case: 2 nodes, no edges -> False")
run_valid_tree_test(3, [[0,1],[1,2]], True, "Edge case: 3 nodes, 2 edges -> True")
run_valid_tree_test(3, [[0,1],[0,2],[1,2]], False, "Edge case: 3 nodes, cycle -> False")
run_valid_tree_test(4, [[0,1],[2,3]], False, "Edge case: 4 nodes, disconnected components -> False")
run_valid_tree_test(4, [[0,1],[1,2],[2,3]], True, "Edge case: 4 nodes, linear tree -> True")
run_valid_tree_test(0, [], True, "Edge case: 0 nodes -> True")
run_valid_tree_test(3, [[0,1],[0,2],[1,2]], False, "Edge case: Triangle (cycle) -> False")
run_valid_tree_test(6, [[0,1],[0,2],[0,3],[1,4],[1,5]], True, "Edge case: Star-like tree -> True")