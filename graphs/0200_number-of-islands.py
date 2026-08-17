from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Counts the number of islands in a 2D binary grid.
        
        Problem Understanding:
        - Given a 2D grid map of '1's (land) and '0's (water)
        - An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically
        - Count the total number of islands
        
        Approach:
        - Use DFS/BFS to traverse connected components of land ('1's)
        - For each unvisited land cell, start a new island count
        - During traversal, mark visited land cells to avoid counting them again
        - Continue until all cells are processed
        
        Time Complexity: O(M * N) where M and N are grid dimensions
        Space Complexity: O(M * N) in worst case for recursion stack (for a full grid of land)
        
        Args:
            grid: 2D grid of '1's (land) and '0's (water)
            
        Returns:
            Number of islands in the grid
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        island_count = 0
        
        def dfs(row, col):
            # Check bounds and if current cell is water or already visited
            if (row < 0 or row >= m or col < 0 or col >= n or 
                grid[row][col] == '0' or grid[row][col] == '2'):  # '2' marks visited
                return
            
            # Mark current cell as visited
            grid[row][col] = '2'
            
            # Explore all 4 directions
            for dr, dc in directions:
                dfs(row + dr, col + dc)
        
        # Traverse the entire grid
        for i in range(m):
            for j in range(n):
                # If we find unvisited land, it's a new island
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j)  # Mark all connected land as visited
        
        return island_count

def run_num_islands_test(grid, expected, test_name):
    """
    Tests the numIslands function.
    
    Args:
        grid: 2D grid of '1's (land) and '0's (water)
        expected: Expected number of islands
        test_name: Name/description of the test case
    """
    # Make a copy of the grid to avoid modifying the original
    import copy
    grid_copy = copy.deepcopy(grid)
    
    solution = Solution()
    result = solution.numIslands(grid_copy)
    
    print(f"{test_name}:")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_num_islands_test([
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
], 1, "Example 1: Single large island")

run_num_islands_test([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
], 3, "Example 2: Multiple islands")

run_num_islands_test([
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
], 1, "Edge case: Cross-shaped island")

run_num_islands_test([
    ["1","0","1"],
    ["0","1","0"],
    ["1","0","1"]
], 5, "Edge case: Diagonal pattern -> 5 islands")

run_num_islands_test([
    ["0","0","0","0"],
    ["0","0","0","0"],
    ["0","0","0","0"]
], 0, "Edge case: All water -> 0 islands")

run_num_islands_test([
    ["1","1","1","1"],
    ["1","1","1","1"],
    ["1","1","1","1"]
], 1, "Edge case: All land -> 1 island")

run_num_islands_test([["1"]], 1, "Edge case: Single land cell -> 1 island")

run_num_islands_test([["0"]], 0, "Edge case: Single water cell -> 0 islands")

run_num_islands_test([
    ["1","0","1","0"],
    ["0","1","0","1"],
    ["1","0","1","0"],
    ["0","1","0","1"]
], 8, "Edge case: Checkerboard pattern -> 8 islands")

run_num_islands_test([
    ["1","1","0","0"],
    ["0","0","1","1"],
    ["0","0","1","1"],
    ["1","1","0","0"]
], 4, "Edge case: Multiple separate islands -> 4 islands")