from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Your code here
        if amount == 0:
            return 1
        
        dp = [0] * (amount + 1)

        for coin in coins:
            # use different numbers of coins
            for num in range(coin, amount + 1):
                if num == coin:
                    dp[num] += 1
                else:
                    dp[num] += dp[num - coin]
        
        return dp[amount]

if __name__ == "__main__":
    sol = Solution()

    # print(sol.change(5, [1,2,5]))    # Expected: 4
    # print(sol.change(3, [2]))        # Expected: 0
    
    # # Test case 3: Amount is 0 (empty combination)
    print(sol.change(0, [1,2,5]))    # Expected: o
    
    # # Test case 4: Single coin type
    print(sol.change(10, [5]))       # Expected: 1
    
    # # Test case 5: Multiple coin types
    print(sol.change(10, [1,2,5]))   # Expected: 10
    
    # # Test case 6: Large amount with small coins
    print(sol.change(100, [1,5,10,25]))  # Expected: 242
    
    # # Test case 7: No coins available
    # print(sol.change(5, []))         # Expected: 0