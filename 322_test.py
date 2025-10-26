from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        dp = [-1] * (amount + 1)
        dp[0] = 0

        for num in range(1, amount + 1):
            for coin in coins:
                if num - coin >= 0:
                    if dp[num-coin] == -1:
                        continue

                    if dp[num] == -1:
                        dp[num] = 1 + dp[num - coin]
                    else:
                      dp[num] = min(dp[num], 1 + dp[num - coin])

        return dp[amount]

class SolutionOpt:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize with a large number (infinity)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for num in range(1, amount + 1):
            for coin in coins:
                if num - coin >= 0:
                    dp[num] = min(dp[num], 1 + dp[num - coin])
        
        return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    sol = Solution()
    # print(sol.coinChange([1, 2, 5], 11))
    print(sol.coinChange([2], 3))