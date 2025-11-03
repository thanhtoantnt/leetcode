from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the kth largest element in the array.
        
        Problem Understanding:
        - Given an integer array and integer k
        - Return the kth largest element in the sorted order
        - Not necessarily the kth distinct element
        - Should be solved without sorting the entire array
        
        Approach:
        - Use min-heap of size k to keep track of k largest elements seen so far
        - For each element, if heap size < k, add element
        - If heap size == k and current element > smallest in heap, replace smallest
        - After processing all elements, the root of heap is the kth largest element
        - This maintains the k largest elements with the smallest among them at root
        
        Time Complexity: O(n * log k) where n is length of nums
        Space Complexity: O(k) for the heap
        
        Args:
            nums: List of integers
            k: Position of largest element to find (1-indexed)
            
        Returns:
            The kth largest element in the array
        """
        # Min-heap to store k largest elements
        min_heap = []
        
        for num in nums:
            if len(min_heap) < k:
                # If heap not full, add the number
                heapq.heappush(min_heap, num)
            else:
                # If heap is full and current number is larger than smallest in heap
                if num > min_heap[0]:
                    # Remove smallest and add current number
                    heapq.heapreplace(min_heap, num)
        
        # The root of min-heap is the kth largest element
        return min_heap[0]

def run_kth_largest_test(nums, k, expected, test_name):
    """
    Tests the findKthLargest function.
    
    Args:
        nums: List of integers
        k: Position of largest element to find
        expected: Expected kth largest element
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.findKthLargest(nums, k)
    
    print(f"{test_name}:")
    print(f"  Input: nums = {nums}, k = {k}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_kth_largest_test([3,2,1,5,6,4], 2, 5, "Example 1: [3,2,1,5,6,4], k=2 -> 5")
run_kth_largest_test([3,2,3,1,2,4,5,5,6], 4, 4, "Example 2: [3,2,3,1,2,4,5,5,6], k=4 -> 4")
run_kth_largest_test([1], 1, 1, "Edge case: Single element, k=1 -> 1")
run_kth_largest_test([1,2], 1, 2, "Edge case: [1,2], k=1 -> 2")
run_kth_largest_test([1,2], 2, 1, "Edge case: [1,2], k=2 -> 1")
run_kth_largest_test([3,2,1,5,6,4], 1, 6, "Edge case: [3,2,1,5,6,4], k=1 -> 6")
run_kth_largest_test([3,2,1,5,6,4], 6, 1, "Edge case: [3,2,1,5,6,4], k=6 -> 1")
run_kth_largest_test([7,10,4,3,20,15], 3, 10, "Edge case: [7,10,4,3,20,15], k=3 -> 10")
run_kth_largest_test([1,2,3,4,5,6,7,8,9,10], 5, 6, "Edge case: [1,2,3,4,5,6,7,8,9,10], k=5 -> 6")
run_kth_largest_test([-1,-2,-3,-4,-5], 2, -2, "Edge case: [-1,-2,-3,-4,-5], k=2 -> -2")
run_kth_largest_test([2,1], 1, 2, "Edge case: [2,1], k=1 -> 2")
run_kth_largest_test([2,1], 2, 1, "Edge case: [2,1], k=2 -> 1")