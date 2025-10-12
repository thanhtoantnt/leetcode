from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}  # a hash table of unique elements
        for num in nums:
            if num in seen:
                return True
            else:
                seen[num] = True
        return False

# Test the solution
if __name__ == "__main__":
    sol = Solution()
        # Test cases
    print(sol.containsDuplicate([1,2,3,1]))    # Expected: True
    print(sol.containsDuplicate([1,2,3,4]))    # Expected: False
    print(sol.containsDuplicate([1,1,1,1]))    # Expected: True
    print(sol.containsDuplicate([]))           # Expected: False
    print(sol.containsDuplicate([1]))          # Expected: False