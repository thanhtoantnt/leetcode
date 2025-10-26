from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(curSet: List[int], start: int):
            # Append a COPY of the current subset
            result.append(curSet.copy())
            
            for i in range(start, len(nums)):
                # Include nums[i] in the subset
                curSet.append(nums[i])
                # Recursively generate subsets starting from next index
                backtrack(curSet, i + 1)
                # Backtrack: remove nums[i] from subset
                curSet.pop()
        
        backtrack([], 0)
        return result

def test_subsets():
    solution = Solution()
    
    # Test Case 1
    nums1 = [1,2, 3]
    result1 = solution.subsets(nums1)
    # expected1 = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    print(f"Test 1 - Input: {nums1}")
    # print(f"Expected: {expected1}")
    print(f"Got: {result1}")
    # print(f"Length match: {len(result1) == len(expected1)}")
    # print()
    
    # # Test Case 2
    # nums2 = [0]
    # result2 = solution.subsets(nums2)
    # expected2 = [[],[0]]
    # print(f"Test 2 - Input: {nums2}")
    # print(f"Expected: {expected2}")
    # print(f"Got: {result2}")
    # print(f"Length match: {len(result2) == len(expected2)}")
    # print()
    
    # # Test Case 3
    # nums3 = [1,2]
    # result3 = solution.subsets(nums3)
    # expected3 = [[],[1],[2],[1,2]]
    # print(f"Test 3 - Input: {nums3}")
    # print(f"Expected: {expected3}")
    # print(f"Got: {result3}")
    # print(f"Length match: {len(result3) == len(expected3)}")
    # print()
    
    # # Test Case 4
    # nums4 = [4,5,6]
    # result4 = solution.subsets(nums4)
    # expected_length4 = 8  # 2^3 = 8 subsets
    # print(f"Test 4 - Input: {nums4}")
    # print(f"Expected length: {expected_length4}")
    # print(f"Got length: {len(result4)}")
    # print(f"Contains empty set: {[] in result4}")
    # print(f"Contains full set: {nums4 in result4}")

# Run tests
test_subsets()
