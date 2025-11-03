from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        Calculates the number of combinations that make up a given amount using coins.
        
        Problem Understanding:
        - Given an integer array coins representing different denominations
        - Given an integer amount representing total amount of money
        - Return the number of combinations that make up that amount
        - Different sequences are considered the same combination
        - Each coin can be used infinitely
        
        Approach:
        - Use dynamic programming with 1D array
        - dp[i] = number of ways to make amount i
        - For each coin, update dp array for all amounts from coin value to target amount
        - dp[0] = 1 (one way to make amount 0: use no coins)
        - For each coin, iterate through amounts and add ways to make (amount - coin)
        
        Time Complexity: O(amount * number of coins)
        Space Complexity: O(amount)
        
        Args:
            amount: Target amount to make
            coins: List of coin denominations
            
        Returns:
            Number of combinations that make up the amount
        """
        # dp[i] = number of ways to make amount i
        dp = [0] * (amount + 1)
        dp[0] = 1  # One way to make amount 0: use no coins
        
        # For each coin denomination
        for coin in coins:
            # Update dp array for all amounts from coin value to target amount
            for current_amount in range(coin, amount + 1):
                # Add number of ways to make (current_amount - coin)
                dp[current_amount] += dp[current_amount - coin]
        
        return dp[amount]

def run_coin_change_2_test(amount, coins, expected, test_name):
    """
    Tests the change function.
    
    Args:
        amount: Target amount to make
        coins: List of coin denominations
        expected: Expected number of combinations
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.change(amount, coins)
    
    print(f"{test_name}:")
    print(f"  Input: amount = {amount}, coins = {coins}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_coin_change_2_test(5, [1,2,5], 4, "Example 1: amount=5, coins=[1,2,5] -> 4 ([5], [2,2,1], [2,1,1,1], [1,1,1,1,1])")
run_coin_change_2_test(3, [2], 0, "Example 2: amount=3, coins=[2] -> 0 (impossible)")
run_coin_change_2_test(10, [10], 1, "Example 3: amount=10, coins=[10] -> 1")
run_coin_change_2_test(0, [1], 1, "Edge case: amount=0 -> 1 (one way: use no coins)")
run_coin_change_2_test(1, [1], 1, "Edge case: amount=1, coins=[1] -> 1")
run_coin_change_2_test(4, [1,2], 3, "Edge case: amount=4, coins=[1,2] -> 3 ([1,1,1,1], [1,1,2], [2,2])")
run_coin_change_2_test(6, [1,2,3], 7, "Edge case: amount=6, coins=[1,2,3] -> 7")
run_coin_change_2_test(7, [2,3,5], 0, "Edge case: amount=7, coins=[2,3,5] -> 0")
run_coin_change_2_test(10, [2,5,3,6], 5, "Edge case: amount=10, coins=[2,5,3,6] -> 5")
run_coin_change_2_test(0, [], 1, "Edge case: amount=0, no coins -> 1")
run_coin_change_2_test(1, [], 0, "Edge case: amount=1, no coins -> 0")
run_coin_change_2_test(100, [1], 1, "Edge case: amount=100, coins=[1] -> 1")