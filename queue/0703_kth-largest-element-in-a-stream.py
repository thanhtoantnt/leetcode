import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        # Add all initial numbers
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Push to heap
        heapq.heappush(self.min_heap, val)
        
        # If heap size exceeds k, remove smallest (maintain only k largest)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        # The root is the Kth largest
        return self.min_heap[0]

