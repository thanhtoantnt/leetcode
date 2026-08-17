from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Finds the fewest number of coins needed to make up the given amount.
        
        Problem Understanding:
        - Given an integer array coins representing different denominations
        - Given an integer amount representing total amount of money
        - Return the fewest number of coins needed to make up that amount
        - If amount cannot be made up, return -1
        - Each coin can be used infinitely
        
        Approach:
        - Use dynamic programming with bottom-up approach
        - dp[i] = minimum number of coins needed to make amount i
        - For each amount i, try each coin denomination
        - If coin value <= i and dp[i - coin] is reachable, update dp[i]
        - Initialize dp array with amount+1 (impossible value) as default
        - dp[0] = 0 (0 coins needed to make amount 0)
        
        Time Complexity: O(amount * number of coins)
        Space Complexity: O(amount)
        
        Args:
            coins: List of coin denominations
            amount: Target amount to make
            
        Returns:
            Minimum number of coins needed, or -1 if impossible
        """
        if amount == 0:
            return 0
        
        # Initialize dp array with impossible value (amount+1)
        # We use amount+1 instead of infinity to avoid overflow issues
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # 0 coins needed to make amount 0
        
        # For each amount from 1 to target amount
        for i in range(1, amount + 1):
            # Try each coin denomination
            for coin in coins:
                # If coin value is not greater than current amount
                # and the remaining amount (i - coin) is reachable
                if coin <= i and dp[i - coin] != amount + 1:
                    # Update minimum coins needed
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Return result or -1 if impossible
        return dp[amount] if dp[amount] != amount + 1 else -1

def run_coin_change_test(coins, amount, expected, test_name):
    """
    Tests the coinChange function.
    
    Args:
        coins: List of coin denominations
        amount: Target amount to make
        expected: Expected minimum number of coins
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.coinChange(coins, amount)
    
    print(f"{test_name}:")
    print(f"  Input: coins = {coins}, amount = {amount}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_coin_change_test([1,3,4], 6, 2, "Example 1: [1,3,4], amount=6 -> 2 (3+3=6)")
run_coin_change_test([2], 3, -1, "Example 2: [2], amount=3 -> -1 (impossible)")
run_coin_change_test([1], 0, 0, "Example 3: [1], amount=0 -> 0")
run_coin_change_test([1,2,5], 11, 3, "Edge case: [1,2,5], amount=11 -> 3 (5+5+1=11)")
run_coin_change_test([2,5,10,1], 27, 4, "Edge case: [2,5,10,1], amount=27 -> 4 (10+10+5+2=27)")
run_coin_change_test([1], 1, 1, "Edge case: [1], amount=1 -> 1")
run_coin_change_test([1], 2, 2, "Edge case: [1], amount=2 -> 2")
run_coin_change_test([2,3], 1, -1, "Edge case: [2,3], amount=1 -> -1 (impossible)")
run_coin_change_test([1,2,3,4,5], 100, 20, "Edge case: [1,2,3,4,5], amount=100 -> 20 (20*5=100)")
run_coin_change_test([186,419,83,408], 6249, 20, "Edge case: Complex case -> 20")
run_coin_change_test([], 1, -1, "Edge case: No coins, amount=1 -> -1 (impossible)")
run_coin_change_test([1,2,3], 4, 2, "Edge case: [1,2,3], amount=4 -> 2 (2+2=4 or 1+3=4)")