from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        htbl = {}

        for num in nums:
            htbl[num] = htbl.get(num, 0) + 1

        min_heap = []

        for num in htbl:
            heapq.heappush(min_heap, (htbl[num], num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = []
        while min_heap:
            _, num = heapq.heappop(min_heap)
            result.append(num)

        return result


class SolutionOpt:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        # Count frequencies - O(n)
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Use min-heap to track top k elements - O(n log k)
        min_heap = []
        for num, count in freq_map.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # Remove smallest frequency

        # Extract results - O(k log k)
        result = []
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        
        return result