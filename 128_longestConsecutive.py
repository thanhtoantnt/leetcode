from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        hash_table = {}
        for num in nums:
            hash_table[num] = True

        longest = 0
        while hash_table:
            value, _ = hash_table.popitem()
            length = 1
            increment = value + 1
            decrement = value - 1
            while increment in hash_table:
                hash_table.pop(increment)
                length = length + 1
                increment = increment + 1
            
            while decrement in hash_table:
                hash_table.pop(decrement)
                length = length + 1
                decrement = decrement - 1

            if length > longest:
                longest = length
            
        return longest


class Solution2:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:  # More Pythonic than nums == []
            return 0

        num_set = set(nums)  # More memory efficient than dict
        longest = 0
        
        while num_set:
            num = next(iter(num_set))  # Get any element
            num_set.remove(num)
            length = 1
            
            # Expand right
            right = num + 1
            while right in num_set:
                num_set.remove(right)
                length += 1
                right += 1
            
            # Expand left  
            left = num - 1
            while left in num_set:
                num_set.remove(left)
                length += 1
                left -= 1
            
            longest = max(longest, length)
            
        return longest

if __name__ == "__main__":
    # Test cases
    sol = Solution()
    sol2 = Solution2()
    print(sol.longestConsecutive([100,4,200,1,3,2]))        # Expected: 4
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))   # Expected: 9  
    print(sol.longestConsecutive([]))                       # Expected: 0
    print(sol.longestConsecutive([1]))                      # Expected: 1
    print(sol.longestConsecutive([1, 3, 5, 7, 9]))         # Expected: 1

    # print(sol2.longestConsecutive([100,4,200,1,3,2]))        # Expected: 4
    # print(sol2.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))   # Expected: 9  
    # print(sol2.longestConsecutive([]))                       # Expected: 0
    # print(sol2.longestConsecutive([1]))                      # Expected: 1
    # print(sol2.longestConsecutive([1, 3, 5, 7, 9]))         # Expected: 1
