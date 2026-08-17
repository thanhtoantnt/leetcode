from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while max_heap:
            largest = heapq.heappop(max_heap)

            if not max_heap:
                return -largest
        
            second = heapq.heappop(max_heap)

            if not max_heap:
                return second - largest
            else:
                heapq.heappush(max_heap, largest - second)


def lastStoneWeightOpt(self, stones: List[int]) -> int:
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)
    
    while len(max_heap) > 1:
        largest = -heapq.heappop(max_heap)  # Convert to positive
        second = -heapq.heappop(max_heap)   # Convert to positive
        
        if largest != second:
            new_stone = largest - second
            heapq.heappush(max_heap, -new_stone)  # Push negative
    
    return -max_heap[0] if max_heap else 0