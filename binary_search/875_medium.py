from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Finds the minimum eating speed k such that Koko can eat all bananas within h hours.
        
        Problem Understanding:
        - Koko can choose an eating speed k (bananas per hour)
        - Each hour, she chooses a pile and eats k bananas
        - If pile has < k bananas, she finishes the pile and stops for the hour
        - Find minimum k such that she can eat all piles within h hours
        
        Approach:
        - Use binary search on the eating speed k
        - Lower bound: 1 (minimum possible speed)
        - Upper bound: max(piles) (speed to finish any pile in 1 hour)
        - For each mid speed, calculate total hours needed
        - If hours <= h, try a smaller speed (right = mid)
        - If hours > h, need a larger speed (left = mid + 1)
        
        Time Complexity: O(n * log(max_pile)) where n is number of piles
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            piles: List of integers representing bananas in each pile
            h: Maximum hours available
            
        Returns:
            Minimum eating speed k
        """
        def can_finish(speed):
            """Helper function to check if Koko can finish all piles at given speed"""
            hours_needed = 0
            for pile in piles:
                # Calculate hours needed for this pile (ceiling division)
                hours_needed += math.ceil(pile / speed)
                # Early termination if already exceed h
                if hours_needed > h:
                    return False
            return hours_needed <= h
        
        # Binary search bounds
        left = 1  # Minimum possible speed
        right = max(piles)  # Maximum possible speed (finish any pile in 1 hour)
        
        while left < right:
            mid = (left + right) // 2
            
            if can_finish(mid):
                # If we can finish with speed mid, try a smaller speed
                right = mid
            else:
                # If we can't finish with speed mid, need a larger speed
                left = mid + 1
        
        return left

def run_koko_test(piles, h, expected, test_name):
    """
    Tests the minEatingSpeed function.
    
    Args:
        piles: List of banana counts in each pile
        h: Maximum hours available
        expected: Expected minimum eating speed
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.minEatingSpeed(piles, h)
    
    print(f"{test_name}:")
    print(f"  Input: piles = {piles}, h = {h}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_koko_test([3,6,7,11], 8, 4, "Example 1: [3,6,7,11], h=8 -> 4")
run_koko_test([30,11,23,4,20], 5, 30, "Example 2: [30,11,23,4,20], h=5 -> 30")
run_koko_test([30,11,23,4,20], 6, 23, "Example 3: [30,11,23,4,20], h=6 -> 23")
run_koko_test([312884470], 312884469, 2, "Edge case: Large pile, almost same hours -> 2")
run_koko_test([1,1,1,1], 4, 1, "Edge case: Small piles, exact hours -> 1")
run_koko_test([1,1,1,1], 3, 2, "Edge case: Small piles, tight hours -> 2")
run_koko_test([1000000000], 2, 500000000, "Edge case: Very large pile, small hours -> 500000000")
run_koko_test([1,2,3,4,5,6,7,8,9,10], 15, 4, "Edge case: Sequential piles, h=15 -> 4")
run_koko_test([10,10,10,10], 4, 10, "Edge case: Equal piles, exact hours -> 10")
run_koko_test([10,10,10,10], 3, 14, "Edge case: Equal piles, tight hours -> 14")
run_koko_test([1], 1, 1, "Edge case: Single pile, single hour -> 1")
run_koko_test([1,2], 2, 2, "Edge case: Two piles, h=2 -> 2")