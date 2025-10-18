from typing import List

# naive solution, exceeded time limit in Leetcode
class SolutionNaive:
    def aux_coinChange(self, coins: List[int], amount: int) -> int:
        if coins == []:
            return -1
        
        if len(coins) == 1:
            if amount % coins[0] == 0:
                return amount // coins[0]
            else:
                return -1
        

        current_deno = coins[0]

        current_count = amount // current_deno
        # print(f"deno = {current_deno} with amount = {current_count}")
        current_min = -1

        while current_count >= 0:
            smaller_count = self.coinChange(coins[1:], amount - current_count * current_deno)
            if  smaller_count != -1:
                # print(f"deno: {current_deno} with small amount = {smaller_count} and current_count = {current_count}")
                if current_min == -1:
                    current_min = smaller_count + current_count
                else:
                    current_min = min(current_min, smaller_count + current_count)

            current_count = current_count - 1

        return current_min
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.aux_coinChange(sorted(coins, reverse=True), amount)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize DP array
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        for index in range(1, amount + 1):
            for coin in coins:
                if coin <= index:
                    dp[index] = min(dp[index], dp[index-coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    sol = Solution()
    # print(sol.coinChange([1,2,5], 11))  # Expected: 3
    # print(sol.coinChange([2], 3))       # Expected: -1
    # print(sol.coinChange([1], 0))       # Expected: 0
    # print(sol.coinChange([1], 1))       # Expected: 1
    # print(sol.coinChange([1], 2))       # Expected: 2
    print(sol.coinChange([186, 419, 83, 408], 6249))       # Expected: 2