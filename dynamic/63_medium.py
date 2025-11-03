from typing import List

# accepted by Leetcode
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid) # rows
        assert(m >= 1)
        n = len(obstacleGrid[0]) # collums

        dp = [[0] * n for _ in range(m)]

        for index_i in range(m):
            for index_j in range(n):
                go_down = 0
                if index_i >= 1:
                    go_down = dp[index_i - 1][index_j]
                go_right = 0
                if index_j >= 1:
                    go_right = dp[index_i][index_j - 1]

                if obstacleGrid[index_i][index_j] == 0:
                    # special case
                    if index_i == 0 and index_j == 0:
                        dp[0][0] = 1
                        continue
                    dp[index_i][index_j] =  go_down + go_right
            
        return dp[m-1][n-1]

class SolutionOpt:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        # Initialize first cell
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue  # Leave as 0 for obstacles
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
        
        return dp[m-1][n-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))  # Expected: 2
    print(sol.uniquePathsWithObstacles([[0,1],[0,0]]))              # Expected: 1
    print(sol.uniquePathsWithObstacles([[0,0],[1,1],[0,0]]))        # Expected: 0
    print(sol.uniquePathsWithObstacles([[1]]))                      # Expected: 0
    print(sol.uniquePathsWithObstacles([[0]]))                      # Expected: 1