from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Finds the total number of provinces (connected components) in a graph of cities.
        
        Problem Understanding:
        - Given an n x n matrix 'isConnected' where isConnected[i][j] = 1 means city i is directly connected to city j
        - A province is a group of directly or indirectly connected cities
        - Return the total number of provinces
        
        Approach:
        - Treat the matrix as an adjacency matrix of an undirected graph
        - Use Union-Find (Disjoint Set Union) data structure to efficiently find connected components
        - Initially, each city is its own component (n components)
        - For each direct connection (edge), union the two cities
        - Each successful union reduces the total component count by 1
        - Path compression and union by rank optimizations for efficiency
        
        Time Complexity: O(n^2 * α(n)) where α is inverse Ackermann function (nearly constant)
        Space Complexity: O(n) for parent and rank arrays
        
        Args:
            isConnected: Adjacency matrix representing city connections
            
        Returns:
            Total number of provinces
        """
        n = len(isConnected)
        
        # Union-Find data structure
        parent = list(range(n))  # Each node is its own parent initially
        rank = [0] * n  # Rank for union by rank optimization
        components = n  # Initially n components (each city is its own province)
        
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
        
        # Process each edge in the adjacency matrix
        for i in range(n):
            for j in range(i + 1, n):  # Only check upper triangle to avoid duplicates
                if isConnected[i][j] == 1:
                    if union(i, j):
                        components -= 1  # Successfully merged two components
        
        return components

def run_find_circle_test(isConnected, expected, test_name):
    """
    Tests the findCircleNum function.
    
    Args:
        isConnected: Adjacency matrix representing city connections
        expected: Expected number of provinces
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.findCircleNum(isConnected)
    
    print(f"{test_name}:")
    print(f"  Input: {isConnected}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_find_circle_test(
    [[1,1,0],[1,1,0],[0,0,1]],
    2,
    "Example 1: [[1,1,0],[1,1,0],[0,0,1]] -> 2 provinces"
)
run_find_circle_test(
    [[1,0,0],[0,1,0],[0,0,1]],
    3,
    "Example 2: [[1,0,0],[0,1,0],[0,0,1]] -> 3 provinces (no connections)"
)
run_find_circle_test(
    [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]],
    1,
    "Example 3: Fully connected graph -> 1 province"
)
run_find_circle_test(
    [[1]],
    1,
    "Edge case: Single city -> 1 province"
)
run_find_circle_test(
    [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],
    1,
    "Edge case: All cities connected -> 1 province"
)
run_find_circle_test(
    [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
    4,
    "Edge case: No connections -> 4 provinces"
)
run_find_circle_test(
    [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]],
    2,
    "Edge case: Two separate groups -> 2 provinces"
)
run_find_circle_test(
    [[1,1,0,0,0],[1,1,1,0,0],[0,1,1,0,0],[0,0,0,1,1],[0,0,0,1,1]],
    2,
    "Edge case: Three connected, two connected -> 2 provinces"
)