
# accepted by Leetcode
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Your code here
        dp = [[1] * n for _ in range(m)]

        for index_i in range(m):
            for index_j in range(n):
                go_down = 0
                if index_i >= 1:
                    go_down = dp[index_i - 1][index_j]
                go_right = 0
                if index_j >= 1:
                    go_right = dp[index_i][index_j - 1]

                # special case
                if index_i == 0 and index_j == 0:
                    dp[0][0] = 1
                    continue

                dp[index_i][index_j] =  go_down + go_right
            
        return dp[m-1][n-1]

class SolutionOpt:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]
        
        # start from 1 because for left-most column or first row, there is only one way
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

# optimizing space
class SolutionOpt2:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        
        return dp[n-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePaths(3, 2))   # Expected: 3
    print(sol.uniquePaths(3, 7))   # Expected: 28
    print(sol.uniquePaths(1, 1))   # Expected: 1
    print(sol.uniquePaths(1, 5))   # Expected: 1
    print(sol.uniquePaths(5, 1))   # Expected: 1