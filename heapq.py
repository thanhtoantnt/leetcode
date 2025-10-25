import heapq

# Create a heap from a list
nums = [3, 1, 4, 1, 5, 9, 2]
heapq.heapify(nums)  # Convert list to heap in-place
print(nums)  # [1, 1, 2, 3, 5, 9, 4] - min-heap order

