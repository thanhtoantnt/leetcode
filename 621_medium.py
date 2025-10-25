from typing import List
import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count task frequencies
        task_count = Counter(tasks)
        
        # Max-heap: store negative frequencies to simulate max-heap
        max_heap = [-count for count in task_count.values()]
        heapq.heapify(max_heap)
        
        # Queue for tasks in cooldown: (time_available, count)
        cooldown_queue = deque()
        
        time = 0
        
        while max_heap or cooldown_queue:
            time += 1
            
            # If max_heap has tasks, schedule the most frequent one
            if max_heap:
                count = heapq.heappop(max_heap) + 1  # +1 because we use negative counts
                if count < 0:  # If there are remaining occurrences
                    # This task will be available again at time + n
                    cooldown_queue.append((time + n, count))
            
            # Check if any tasks in cooldown are ready to be added back to heap
            if cooldown_queue and cooldown_queue[0][0] == time:
                ready_time, count = cooldown_queue.popleft()
                heapq.heappush(max_heap, count)
        
        return time

class SolutionYoutube:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count task frequencies
        task_count = Counter(tasks)

        # max_heap
        maxHeap = [-count for count in task_count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque() # pair of [-cnt, idleTime]

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt < 0:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

if __name__ == "__main__":
    sol = SolutionYoutube()

    # # Test 7: Mixed frequencies
    # tasks = ["A","A","A","A","B","B","C","C","D","D"], n = 2
    # # Output: 10

    # Test 8: Large cooldown
    tasks = ["A","A","B","B"]
    n = 5
    print(sol.leastInterval(tasks, n))
    # Output: 8

    # # Test 9: From Leetcode example
    # tasks = ["A","A","A","B","B","B"], n = 50
    # # Output: 104