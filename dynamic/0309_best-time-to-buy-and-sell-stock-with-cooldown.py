from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Finds the maximum profit with the restriction that after selling, there's a cooldown period.
        
        Problem Understanding:
        - Given an array of stock prices where prices[i] is price on day i
        - Can buy/sell multiple times but must cooldown for one day after selling
        - After selling on day i, cannot buy on day i+1
        - Can hold at most one share at a time
        
        Approach:
        - Use dynamic programming with three states:
          - hold: max profit when holding a stock
          - sold: max profit when just sold a stock (in cooldown)
          - rest: max profit when not holding and not in cooldown
        - State transitions:
          - hold = max(hold, rest - price) (keep holding or buy from rest)
          - sold = hold + price (sell the stock we're holding)
          - rest = max(rest, sold) (stay in rest or come out of cooldown)
        - Initialize: hold = -infinity (can't hold initially), sold = 0, rest = 0
        
        Time Complexity: O(n) where n is length of prices
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            prices: List of stock prices for consecutive days
            
        Returns:
            Maximum profit achievable with cooldown constraint
        """
        if not prices:
            return 0
        
        # Initialize states
        # hold: max profit when holding a stock
        hold = -prices[0]  # Buy on first day
        # sold: max profit when just sold (in cooldown)
        sold = 0
        # rest: max profit when not holding and not in cooldown
        rest = 0
        
        for i in range(1, len(prices)):
            price = prices[i]
            
            # Store previous values before updating
            prev_hold = hold
            prev_sold = sold
            prev_rest = rest
            
            # Update states based on transitions
            # Can keep holding or buy from rest state
            hold = max(prev_hold, prev_rest - price)
            # Must sell from hold state
            sold = prev_hold + price
            # Can stay in rest or come out of cooldown from sold state
            rest = max(prev_rest, prev_sold)
        
        # The maximum profit is either in rest state or sold state
        # (can't end with holding a stock for maximum profit)
        return max(sold, rest)

def run_stock_cooldown_test(prices, expected, test_name):
    """
    Tests the maxProfit function with cooldown constraint.
    
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

# Run test cases
run_stock_cooldown_test([1,2,3,0,2], 3, "Example 1: [1,2,3,0,2] -> 3 (buy at 1, sell at 3, cooldown, buy at 0, sell at 2)")
run_stock_cooldown_test([1], 0, "Example 2: [1] -> 0 (can't buy and sell)")
run_stock_cooldown_test([1,2,4], 3, "Edge case: [1,2,4] -> 3 (buy at 1, sell at 4)")
run_stock_cooldown_test([2,1,4], 3, "Edge case: [2,1,4] -> 3 (buy at 1, sell at 4)")
run_stock_cooldown_test([1,2,3,4,5], 4, "Edge case: [1,2,3,4,5] -> 4 (buy at 1, sell at 5)")
run_stock_cooldown_test([5,4,3,2,1], 0, "Edge case: [5,4,3,2,1] -> 0 (decreasing prices)")
run_stock_cooldown_test([1,2,1,2,1,2], 3, "Edge case: [1,2,1,2,1,2] -> 3")
run_stock_cooldown_test([2,1,2,0,1], 2, "Edge case: [2,1,2,0,1] -> 2")
run_stock_cooldown_test([1,2,4,2,5,7,2,4,9,0], 13, "Edge case: Complex pattern -> 13")
run_stock_cooldown_test([], 0, "Edge case: Empty array -> 0")
run_stock_cooldown_test([1,2], 1, "Edge case: Two elements [1,2] -> 1")
run_stock_cooldown_test([2,1], 0, "Edge case: Two elements [2,1] -> 0")