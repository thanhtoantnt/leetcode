from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        Calculates the number of unique paths from top-left to bottom-right in a grid with obstacles.
        
        Problem Understanding:
        - Robot starts at top-left corner (0,0) of m x n grid
        - Robot can only move right or down
        - Grid contains obstacles (marked as 1) and free spaces (marked as 0)
        - Find number of unique paths to reach bottom-right corner (m-1, n-1)
        - Cannot move through obstacles or outside the grid
        
        Approach:
        - Use dynamic programming with 2D array
        - dp[i][j] = number of ways to reach cell (i,j) from (0,0)
        - If cell contains obstacle (obstacleGrid[i][j] == 1), dp[i][j] = 0
        - Base case: dp[0][0] = 1 if no obstacle, 0 if obstacle
        - For first row/column, continue only if no obstacle blocks the path
        - Recurrence: dp[i][j] = dp[i-1][j] + dp[i][j-1] (if no obstacle)
        - Return dp[m-1][n-1]
        
        Time Complexity: O(m * n) where m and n are grid dimensions
        Space Complexity: O(m * n) for the DP table
        
        Args:
            obstacleGrid: 2D grid where 1 represents obstacle, 0 represents free space
            
        Returns:
            Number of unique paths from top-left to bottom-right avoiding obstacles
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If start or end is blocked, no paths possible
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        # Create DP table: dp[i][j] = number of paths to reach (i,j)
        dp = [[0] * n for _ in range(m)]
        
        # Base case: one way to be at starting position if no obstacle
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        # Fill first row: can only come from left
        for j in range(1, n):
            # Can reach (0,j) only if no obstacle and path exists from left
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = 0  # Obstacle blocks this path
        
        # Fill first column: can only come from top
        for i in range(1, m):
            # Can reach (i,0) only if no obstacle and path exists from top
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0  # Obstacle blocks this path
        
        # Fill the rest of the table using recurrence relation
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:  # No obstacle at current cell
                    # Can reach (i,j) from (i-1,j) [from top] or (i,j-1) [from left]
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:  # Obstacle at current cell
                    dp[i][j] = 0  # No paths through obstacle
        
        # Return number of paths to bottom-right corner
        return dp[m-1][n-1]

def run_unique_paths_with_obstacles_test(obstacleGrid, expected, test_name):
    """
    Tests the uniquePathsWithObstacles function.
    
    Args:
        obstacleGrid: 2D grid with obstacles (1) and free spaces (0)
        expected: Expected number of unique paths
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.uniquePathsWithObstacles(obstacleGrid)
    
    print(f"{test_name}:")
    print(f"  Input: {obstacleGrid}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_unique_paths_with_obstacles_test([[0,0,0],[0,1,0],[0,0,0]], 2, "Example 1: [[0,0,0],[0,1,0],[0,0,0]] -> 2 paths")
run_unique_paths_with_obstacles_test([[0,1],[0,0]], 1, "Example 2: [[0,1],[0,0]] -> 1 path")
run_unique_paths_with_obstacles_test([[0,0],[0,0]], 2, "Edge case: [[0,0],[0,0]] -> 2 paths (no obstacles)")
run_unique_paths_with_obstacles_test([[0,0,0],[0,0,0],[0,0,0]], 6, "Edge case: 3x3 grid, no obstacles -> 6 paths")
run_unique_paths_with_obstacles_test([[1,0],[0,0]], 0, "Edge case: Start blocked -> 0 paths")
run_unique_paths_with_obstacles_test([[0,0],[0,1]], 0, "Edge case: End blocked -> 0 paths")
run_unique_paths_with_obstacles_test([[1]], 0, "Edge case: Single cell with obstacle -> 0 paths")
run_unique_paths_with_obstacles_test([[0]], 1, "Edge case: Single cell, no obstacle -> 1 path")
run_unique_paths_with_obstacles_test([[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]], 7, "Edge case: Multiple obstacles")
run_unique_paths_with_obstacles_test([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]], 35, "Edge case: 4x5 grid, no obstacles -> 35 paths")