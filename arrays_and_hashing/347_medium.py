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