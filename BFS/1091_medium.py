from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Finds the length of the shortest clear path in a binary matrix.
        
        Problem Understanding:
        - Given an n x n binary matrix grid where 0 represents a clear path and 1 represents an obstacle
        - Find the shortest path from top-left cell (0, 0) to bottom-right cell (n-1, n-1)
        - Path can move in 8 directions (including diagonals)
        - Return the length of the path, or -1 if no path exists
        
        Approach:
        - Use BFS (Breadth-First Search) to find the shortest path
        - Start from (0, 0) if it's clear (value 0), otherwise return -1
        - Use a queue to explore cells level by level
        - Mark visited cells by changing their value to 1 to avoid revisiting
        - For each cell, explore all 8 directions
        - Return path length when destination is reached
        
        Time Complexity: O(n^2) where n is the dimension of the grid
        Space Complexity: O(n^2) for the queue in worst case (all cells are visited)
        
        Args:
            grid: Binary matrix where 0 represents clear path, 1 represents obstacle
            
        Returns:
            Length of shortest path from (0,0) to (n-1,n-1), or -1 if no path exists
        """
        n = len(grid)
        
        # Check if start or end is blocked
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        # Special case: single cell grid
        if n == 1:
            return 1
        
        # Directions for 8 possible moves (up, down, left, right, and 4 diagonals)
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        # Queue for BFS: (row, col, path_length)
        queue = deque([(0, 0, 1)])
        
        # Mark starting cell as visited by changing its value
        grid[0][0] = 1
        
        while queue:
            row, col, path_length = queue.popleft()
            
            # Explore all 8 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check if new position is within bounds and is a clear path
                if (0 <= new_row < n and 0 <= new_col < n and 
                    grid[new_row][new_col] == 0):
                    
                    # If we reached the destination
                    if new_row == n - 1 and new_col == n - 1:
                        return path_length + 1
                    
                    # Mark as visited and add to queue
                    grid[new_row][new_col] = 1
                    queue.append((new_row, new_col, path_length + 1))
        
        # No path found
        return -1

def run_shortest_path_test(grid, expected, test_name):
    """
    Tests the shortestPathBinaryMatrix function.
    
    Args:
        grid: Binary matrix to search in
        expected: Expected shortest path length or -1
        test_name: Name/description of the test case
    """
    import copy
    grid_copy = copy.deepcopy(grid)
    
    solution = Solution()
    result = solution.shortestPathBinaryMatrix(grid_copy)
    
    print(f"{test_name}:")
    print(f"  Input: {grid}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_shortest_path_test(
    [[0,1],[1,0]],
    2,
    "Example 1: [[0,1],[1,0]] -> 2"
)
run_shortest_path_test(
    [[0,0,0],[1,1,0],[1,1,0]],
    4,
    "Example 2: [[0,0,0],[1,1,0],[1,1,0]] -> 4"
)
run_shortest_path_test(
    [[1,0,0],[1,1,0],[1,1,0]],
    -1,
    "Example 3: [[1,0,0],[1,1,0],[1,1,0]] -> -1 (start blocked)"
)
run_shortest_path_test(
    [[0]],
    1,
    "Edge case: Single cell [[0]] -> 1"
)
run_shortest_path_test(
    [[1]],
    -1,
    "Edge case: Single cell [[1]] -> -1"
)
run_shortest_path_test(
    [[0,0,0,0],[1,1,1,0],[0,0,0,0],[0,1,1,0]],
    7,
    "Edge case: Complex path -> 7"
)
run_shortest_path_test(
    [[0,0,1,0,0],[0,1,0,1,0],[1,0,0,0,1],[0,1,0,1,0],[0,0,1,0,0]],
    7,
    "Edge case: More complex path -> 7"
)
run_shortest_path_test(
    [[0,0,0],[0,1,0],[0,0,0]],
    4,
    "Edge case: [[0,0,0],[0,1,0],[0,0,0]] -> 4"
)