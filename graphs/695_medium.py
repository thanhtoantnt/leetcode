from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Finds the maximum area of an island in a binary matrix.
        
        Problem Understanding:
        - Given a binary matrix where 1 represents land and 0 represents water
        - An island is a group of 1's connected 4-directionally
        - Find the maximum area among all islands
        - If no islands exist, return 0
        
        Approach:
        - Use DFS to explore each island and calculate its area
        - For each unvisited land cell (value 1), start a new island exploration
        - During DFS, count the cells in the current island and mark them as visited
        - Keep track of the maximum area found so far
        - Continue until all cells are processed
        
        Time Complexity: O(M * N) where M and N are grid dimensions
        Space Complexity: O(M * N) in worst case for recursion stack (for a full grid of land)
        
        Args:
            grid: 2D binary grid where 1 represents land and 0 represents water
            
        Returns:
            Maximum area of an island in the grid
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        max_area = 0
        
        def dfs(row, col):
            # Check bounds and if current cell is water or already visited
            if (row < 0 or row >= m or col < 0 or col >= n or 
                grid[row][col] == 0 or grid[row][col] == 2):  # 2 marks visited
                return 0
            
            # Mark current cell as visited
            grid[row][col] = 2
            
            # Start with area of 1 for current cell
            area = 1
            
            # Explore all 4 directions and add their areas
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            
            return area
        
        # Traverse the entire grid
        for i in range(m):
            for j in range(n):
                # If we find unvisited land, calculate the area of this island
                if grid[i][j] == 1:
                    current_area = dfs(i, j)
                    max_area = max(max_area, current_area)
        
        return max_area

def run_max_area_test(grid, expected, test_name):
    """
    Tests the maxAreaOfIsland function.
    
    Args:
        grid: 2D binary grid where 1 represents land and 0 represents water
        expected: Expected maximum area
        test_name: Name/description of the test case
    """
    # Make a copy of the grid to avoid modifying the original
    import copy
    grid_copy = copy.deepcopy(grid)
    
    solution = Solution()
    result = solution.maxAreaOfIsland(grid_copy)
    
    print(f"{test_name}:")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_max_area_test([
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
], 6, "Example 1: Complex grid -> max area 6")

run_max_area_test([[0,0,0,0,0,0,0,0]], 0, "Example 2: All water -> max area 0")

run_max_area_test([
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]
], 4, "Edge case: Two equal islands -> max area 4")

run_max_area_test([[1]], 1, "Edge case: Single land cell -> max area 1")

run_max_area_test([[0]], 0, "Edge case: Single water cell -> max area 0")

run_max_area_test([
    [1,1,1],
    [0,1,0],
    [1,1,1]
], 7, "Edge case: Cross-shaped island -> max area 7")

run_max_area_test([
    [1,0,1,0],
    [0,1,0,1],
    [1,0,1,0],
    [0,1,0,1]
], 1, "Edge case: Diagonal pattern -> max area 1")

run_max_area_test([
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]
], 16, "Edge case: All land -> max area 16")

run_max_area_test([
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,1,0,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
], 9, "Edge case: Donut-shaped island -> max area 9")

run_max_area_test([
    [1,0,0,0,0,0,0],
    [0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0],
    [0,0,0,1,0,0,0],
    [0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0],
    [0,0,0,0,0,0,1]
], 1, "Edge case: Diagonal of single cells -> max area 1")