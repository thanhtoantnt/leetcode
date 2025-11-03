from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Counts the number of connected components in an undirected graph.
        
        Problem Understanding:
        - Given n nodes labeled from 0 to n-1 and a list of undirected edges
        - Count how many separate connected components exist in the graph
        - A connected component is a subgraph where all nodes are connected to each other
        
        Approach:
        - Use Union-Find (Disjoint Set Union) data structure
        - Initially, each node is its own component (n components)
        - For each edge, union the two nodes it connects
        - Each successful union reduces the component count by 1
        - Path compression and union by rank optimizations for efficiency
        
        Time Complexity: O(E * α(n)) where E is number of edges, α is inverse Ackermann function
        Space Complexity: O(n) for parent and rank arrays
        
        Args:
            n: Number of nodes in the graph
            edges: List of undirected edges where each edge connects two nodes
            
        Returns:
            Number of connected components in the graph
        """
        # Union-Find data structure
        parent = list(range(n))  # Each node is its own parent initially
        rank = [0] * n  # Rank for union by rank optimization
        components = n  # Initially n components (each node is its own component)
        
        def find(x):
            """Find root of x with path compression"""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Union by rank - returns True if union was performed (components reduced)"""
            root_x, root_y = find(x), find(y)
            
            if root_x == root_y:
                return False  # Already in same component
            
            # Union by rank
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            
            return True  # Components were merged
        
        # Process each edge
        for a, b in edges:
            if union(a, b):
                components -= 1  # Successfully merged two components
        
        return components

def run_count_components_test(n, edges, expected, test_name):
    """
    Tests the countComponents function.
    
    Args:
        n: Number of nodes
        edges: List of edges
        expected: Expected number of connected components
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.countComponents(n, edges)
    
    print(f"{test_name}:")
    print(f"  Input: n = {n}, edges = {edges}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_count_components_test(5, [[0,1],[1,2],[3,4]], 2, "Example 1: 5 nodes, [[0,1],[1,2],[3,4]] -> 2 components")
run_count_components_test(5, [[0,1],[1,2],[2,3],[3,4]], 1, "Example 2: 5 nodes, all connected -> 1 component")
run_count_components_test(4, [[2,3],[1,2],[1,3]], 2, "Edge case: 4 nodes, 3 edges forming triangle + 1 node -> 2 components")
run_count_components_test(1, [], 1, "Edge case: 1 node, no edges -> 1 component")
run_count_components_test(2, [], 2, "Edge case: 2 nodes, no edges -> 2 components")
run_count_components_test(2, [[0,1]], 1, "Edge case: 2 nodes, 1 edge -> 1 component")
run_count_components_test(3, [[0,1],[1,2]], 1, "Edge case: 3 nodes, 2 edges -> 1 component")
run_count_components_test(3, [[0,1],[0,2],[1,2]], 1, "Edge case: 3 nodes, 3 edges (triangle) -> 1 component")
run_count_components_test(4, [[0,1],[2,3]], 2, "Edge case: 4 nodes, 2 edges, 2 separate pairs -> 2 components")
run_count_components_test(0, [], 0, "Edge case: 0 nodes -> 0 components")
run_count_components_test(5, [], 5, "Edge case: 5 nodes, no edges -> 5 components")
run_count_components_test(6, [[0,1],[2,3],[4,5]], 3, "Edge case: 6 nodes, 3 separate pairs -> 3 components")