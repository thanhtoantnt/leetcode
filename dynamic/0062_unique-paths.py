class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Calculates the number of unique paths from top-left to bottom-right in a grid.
        
        Problem Understanding:
        - Robot starts at top-left corner (0,0) of m x n grid
        - Robot can only move right or down
        - Find number of unique paths to reach bottom-right corner (m-1, n-1)
        - Cannot move outside the grid
        
        Approach:
        - Use Dynamic Programming with 2D array
        - dp[i][j] = number of ways to reach cell (i,j) from (0,0)
        - Base case: dp[0][0] = 1 (one way to be at start)
        - First row: dp[0][j] = 1 (only one way - keep going right)
        - First column: dp[i][0] = 1 (only one way - keep going down)
        - Recurrence: dp[i][j] = dp[i-1][j] + dp[i][j-1]
          (can come from top or left)
        - Return dp[m-1][n-1]
        
        Time Complexity: O(m * n) where m and n are grid dimensions
        Space Complexity: O(m * n) for the DP table
        
        Args:
            m: Number of rows in the grid
            n: Number of columns in the grid
            
        Returns:
            Number of unique paths from top-left to bottom-right
        """
        # Create DP table: dp[i][j] = number of paths to reach (i,j)
        dp = [[0] * n for _ in range(m)]
        
        # Base case: one way to be at starting position
        dp[0][0] = 1
        
        # Fill first row: can only come from left
        for j in range(1, n):
            dp[0][j] = 1  # Only one way to reach any cell in first row
        
        # Fill first column: can only come from top
        for i in range(1, m):
            dp[i][0] = 1  # Only one way to reach any cell in first column
        
        # Fill the rest of the table using recurrence relation
        for i in range(1, m):
            for j in range(1, n):
                # Can reach (i,j) from (i-1,j) [from top] or (i,j-1) [from left]
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Return number of paths to bottom-right corner
        return dp[m-1][n-1]

def run_unique_paths_test(m, n, expected, test_name):
    """
    Tests the uniquePaths function.
    
    Args:
        m: Number of rows in the grid
        n: Number of columns in the grid
        expected: Expected number of unique paths
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.uniquePaths(m, n)
    
    print(f"{test_name}:")
    print(f"  Input: m = {m}, n = {n}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_unique_paths_test(3, 7, 28, "Example 1: 3x7 grid -> 28 paths")
run_unique_paths_test(3, 2, 3, "Example 2: 3x2 grid -> 3 paths (RRD, RDR, DRR)")
run_unique_paths_test(1, 1, 1, "Edge case: 1x1 grid -> 1 path (stay at start)")
run_unique_paths_test(1, 3, 1, "Edge case: 1x3 grid -> 1 path (RRR)")
run_unique_paths_test(3, 1, 1, "Edge case: 3x1 grid -> 1 path (DDD)")
run_unique_paths_test(2, 2, 2, "Edge case: 2x2 grid -> 2 paths (RD, DR)")
run_unique_paths_test(2, 3, 3, "Edge case: 2x3 grid -> 3 paths (RDR, RRD, DRR)")
run_unique_paths_test(4, 4, 20, "Edge case: 4x4 grid -> 20 paths")
run_unique_paths_test(1, 5, 1, "Edge case: 1x5 grid -> 1 path (RRRR)")
run_unique_paths_test(5, 1, 1, "Edge case: 5x1 grid -> 1 path (DDDD)")
run_unique_paths_test(2, 4, 4, "Edge case: 2x4 grid -> 4 paths")
run_unique_paths_test(4, 2, 4, "Edge case: 4x2 grid -> 4 paths")