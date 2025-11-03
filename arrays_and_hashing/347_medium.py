from typing import List
import heapq


class SolutionOpt:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Returns the k most frequent elements from the input array.
        
        Problem Understanding:
        - Given an integer array and integer k
        - Find the k elements that appear most frequently
        - Return them in any order (frequency-based ranking)
        
        Approach:
        - Count frequencies of each element using a hash map
        - Use a min-heap of size k to keep track of top k elements
        - For each unique element, add to heap and remove smallest if size exceeds k
        - Extract elements from heap as result
        
        Time Complexity: O(n log k) where n is length of nums
        Space Complexity: O(n) for frequency map + O(k) for heap = O(n)
        
        Args:
            nums: List of integers
            k: Number of top frequent elements to return
            
        Returns:
            List of k most frequent elements
        """
        # Handle empty input case
        if not nums:
            return []

        # Count frequencies of each number - O(n)
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Use min-heap to track top k elements - O(n log k)
        # Store as (frequency, number) tuples
        min_heap = []
        for num, count in freq_map.items():
            # Add current (frequency, number) to heap
            heapq.heappush(min_heap, (count, num))
            # If heap size exceeds k, remove the smallest frequency element
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Remove element with smallest frequency

        # Extract the numbers from heap - O(k log k)
        # Since it's a min-heap, we get elements in increasing frequency order
        result = []
        while min_heap:
            # Pop and extract the number (second element of tuple)
            result.append(heapq.heappop(min_heap)[1])
        
        return result

def run_top_k_test(nums, k, expected, test_name):
    """
    Tests the topKFrequent function with set-based comparison.
    
    Args:
        nums: Input list of integers
        k: Number of top frequent elements to return
        expected: Expected list of k most frequent elements
        test_name: Name/description of the test case
    """
    solution = SolutionOpt()
    result = solution.topKFrequent(nums, k)
    
    # Convert to sets for order-independent comparison
    result_set = set(result)
    expected_set = set(expected)
    
    print(f"{test_name}:")
    print(f"  Input: nums = {nums}, k = {k}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result_set == expected_set}")
    print()

# Run test cases
run_top_k_test([1,1,1,2,2,3], 2, [1,2], "Example 1: [1,1,1,2,2,3], k=2 -> [1,2]")
run_top_k_test([1], 1, [1], "Example 2: Single element")
run_top_k_test([1,2,3,4,5], 3, [1,2,3], "Edge case: All elements same frequency")
run_top_k_test([4,1,-1,2,-1,2,3], 2, [-1,2], "Edge case: Negative numbers")
run_top_k_test([1,1,1,2,2,2,3,3,3], 3, [1,2,3], "Edge case: All same frequency")
run_top_k_test([1,2,3,4,5,6,7,8,9], 1, [1], "Edge case: All unique, k=1")
run_top_k_test([1,1,2,2,3,3,4,4], 4, [1,2,3,4], "Edge case: Multiple with same frequency")
run_top_k_test([], 0, [], "Edge case: Empty array")
run_top_k_test([5,5,5,5,5], 1, [5], "Edge case: All same elements")
run_top_k_test([1,2,3,1,2,3,1,2], 2, [1,2], "Edge case: Two most frequent tied")