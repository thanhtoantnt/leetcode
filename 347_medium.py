from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = Counter(nums)
        max_queue = []

        for element, value in frequent.items():
            heapq.heappush(max_queue, (-value, element))

        results = []

        for _ in range(k):
            _, element = heapq.heappop(max_queue)
            results.append(element)

        return results


class SolutionOpt:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = Counter(nums)
        min_heap = []
        
        for element, count in frequent.items():
            heapq.heappush(min_heap, (count, element))
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Remove least frequent
        
        return [element for count, element in min_heap]

def test_top_k_frequent():
    sol = Solution()
    
    # Test case 1
    nums1 = [1,1,1,2,2,3]
    k1 = 2
    print(sol.topKFrequent(nums1, k1))  # Expected: [1,2]
    
    # Test case 2 - single element
    nums2 = [1]
    k2 = 1
    print(sol.topKFrequent(nums2, k2))  # Expected: [1]
    
    # Test case 3 - all unique
    nums3 = [1,2,3,4,5]
    k3 = 3
    print(sol.topKFrequent(nums3, k3))  # Expected: any 3 elements
    
    # Test case 4 - negative numbers
    nums4 = [-1,-1,-1,2,2,3,3,3,3]
    k4 = 2
    print(sol.topKFrequent(nums4, k4))  # Expected: [3,-1]
    
    # Test case 5 - ties
    nums5 = [1,1,2,2,3,3]
    k5 = 2
    result = sol.topKFrequent(nums5, k5)
    print(result)  # Expected: any 2 of [1,2,3]

test_top_k_frequent()