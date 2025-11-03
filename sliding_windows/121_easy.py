from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit from buying and selling a stock once.
        
        Problem Understanding:
        - Given array of stock prices where prices[i] is price on day i
        - Buy on one day and sell on a different day in the future
        - Find the maximum profit possible
        - If no profit possible, return 0
        
        Approach:
        - Track the minimum buying price seen so far
        - For each day, calculate profit if sold today (current price - min buy price)
        - Update maximum profit if current profit is higher
        - Update minimum buy price if current price is lower
        
        This is the optimal solution as it:
        - Uses O(1) space (no extra data structures)
        - Makes one pass through the array O(n) time
        - Handles all edge cases efficiently
        
        Time Complexity: O(n) where n is the length of prices array
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            prices: List of stock prices for consecutive days
            
        Returns:
            Maximum profit possible from one buy-sell transaction
        """
        # Initialize maximum profit to 0 (no transaction = no profit)
        maxP = 0
        
        # Initialize minimum buying price to first day's price
        # This represents the best buying opportunity seen so far
        minBuy = prices[0]

        # Iterate through each day's price starting from second day
        # Each day is a potential selling day
        for i in range(1, len(prices)):
            # Calculate profit if we sell on day i
            # Profit = current price - best buying price seen so far
            current_profit = prices[i] - minBuy
            
            # Update maximum profit if current profit is higher
            maxP = max(maxP, current_profit)
            
            # Update minimum buying price if current day's price is lower
            # This represents a better buying opportunity for future sales
            minBuy = min(minBuy, prices[i])

        return maxP

def run_profit_test(prices, expected, test_name):
    """
    Tests the maxProfit function.
    
    Args:
        prices: List of stock prices
        expected: Expected maximum profit
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.maxProfit(prices)
    
    print(f"{test_name}:")
    print(f"  Input: {prices}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run comprehensive test cases
run_profit_test([7,1,5,3,6,4], 5, "Example 1: [7,1,5,3,6,4] -> 5 (buy at 1, sell at 6)")
run_profit_test([7,6,4,3,1], 0, "Example 2: [7,6,4,3,1] -> 0 (prices only decrease)")
run_profit_test([1,2,3,4,5], 4, "Edge case: Strictly increasing prices")
run_profit_test([5,4,3,2,1], 0, "Edge case: Strictly decreasing prices")
run_profit_test([1], 0, "Edge case: Single price")
run_profit_test([2,4,1], 2, "Edge case: [2,4,1] -> 2 (buy at 2, sell at 4)")
run_profit_test([3,2,6,5,0,3], 4, "Edge case: [3,2,6,5,0,3] -> 4 (buy at 2, sell at 6)")
run_profit_test([1,2], 1, "Edge case: Two prices, increasing")
run_profit_test([2,1], 0, "Edge case: Two prices, decreasing")
run_profit_test([2,2,2,2,2], 0, "Edge case: All same prices")
run_profit_test([1,5,3,6,4,7], 6, "Edge case: [1,5,3,6,4,7] -> 6 (buy at 1, sell at 7)")
run_profit_test([6,1,3,2,4,7], 6, "Edge case: [6,1,3,2,4,7] -> 6 (buy at 1, sell at 7)")
run_profit_test([2,1,2,0,1], 1, "Edge case: [2,1,2,0,1] -> 1 (buy at 0, sell at 1)")
run_profit_test([2,1,2,1,0,1,2], 2, "Edge case: [2,1,2,1,0,1,2] -> 2 (buy at 0, sell at 2)")