from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Finds the redundant connection that creates a cycle in a tree.
        
        Problem Understanding:
        - Given a connected undirected graph that started as a tree with one extra edge
        - Return the redundant edge that can be removed to make it a tree again
        - If multiple answers exist, return the one that appears last in the input
        
        Approach:
        - Use Union-Find (Disjoint Set Union) to detect when adding an edge creates a cycle
        - Process edges in order, for each edge check if endpoints are already connected
        - If they are connected, this edge creates a cycle (redundant)
        - Otherwise, union the endpoints
        - Return the first edge that creates a cycle
        
        Time Complexity: O(E * α(n)) where E is number of edges, α is inverse Ackermann function
        Space Complexity: O(n) for parent and rank arrays
        
        Args:
            edges: List of edges in the graph
            
        Returns:
            The redundant edge that should be removed
        """
        n = len(edges)
        parent = list(range(n + 1))  # Node labels are 1-indexed, so size n+1
        rank = [0] * (n + 1)
        
        def find(x):
            """Find root of x with path compression"""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x, y):
            """Union by rank - returns False if x and y are already connected"""
            root_x, root_y = find(x), find(y)
            
            if root_x == root_y:
                return False  # Already connected, this edge creates a cycle
            
            # Union by rank
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            
            return True
        
        # Process each edge in order
        for a, b in edges:
            if not union(a, b):
                return [a, b]  # This edge creates a cycle, so it's redundant
        
        return []  # Should not reach here given problem constraints

def run_redundant_connection_test(edges, expected, test_name):
    """
    Tests the findRedundantConnection function.
    
    Args:
        edges: List of edges in the graph
        expected: Expected redundant edge
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.findRedundantConnection(edges)
    
    print(f"{test_name}:")
    print(f"  Input: {edges}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_redundant_connection_test([[1,2],[1,3],[2,3]], [2,3], "Example 1: [[1,2],[1,3],[2,3]] -> [2,3]")
run_redundant_connection_test([[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4], "Example 2: [[1,2],[2,3],[3,4],[1,4],[1,5]] -> [1,4]")
run_redundant_connection_test([[1,2],[1,3],[3,4],[2,4]], [2,4], "Edge case: Multiple possible redundant edges -> [2,4]")
run_redundant_connection_test([[1,2],[2,3],[1,5],[3,4],[1,4]], [1,4], "Edge case: More complex tree + edge -> [1,4]")
run_redundant_connection_test([[1,2],[1,3],[1,4],[3,4]], [3,4], "Edge case: Star with cycle -> [3,4]")
run_redundant_connection_test([[1,2],[2,3],[3,1]], [3,1], "Edge case: Triangle -> [3,1] (last edge)")
run_redundant_connection_test([[1,2],[2,3],[1,5],[1,4],[3,4]], [3,4], "Edge case: Another configuration -> [3,4]")
run_redundant_connection_test([[1,2],[1,3],[2,4],[3,5],[4,6],[5,6]], [5,6], "Edge case: Path with extra connection -> [5,6]")