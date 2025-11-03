from typing import List
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Calculates the minimum number of intervals required to complete all tasks.
        
        Problem Understanding:
        - Given an array of CPU tasks and a cooling interval n
        - Same tasks must be separated by at least n intervals
        - Each interval can complete one task
        - Return the minimum number of intervals needed
        
        Approach:
        - Use max-heap to always process the most frequent remaining task
        - Use a queue to track tasks that are waiting due to cooling period
        - At each interval, process one task from heap and schedule its next occurrence
        - If no task can be processed, it's an idle interval
        - Continue until all tasks are processed
        
        Time Complexity: O(total_tasks * log(unique_tasks)) 
        Space Complexity: O(unique_tasks) for heap and queue
        
        Args:
            tasks: List of task names (A-Z)
            n: Cooling interval between same tasks
            
        Returns:
            Minimum number of intervals required to complete all tasks
        """
        # Count frequency of each task
        task_counts = Counter(tasks)
        
        # Create max-heap (using negative values for min-heap behavior)
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        # Queue to store (count, next_available_time) for tasks in cooldown
        cooldown_queue = []
        
        time = 0
        
        while max_heap or cooldown_queue:
            time += 1
            
            # If there are tasks available to process
            if max_heap:
                # Get the most frequent remaining task
                count = heapq.heappop(max_heap)
                count += 1  # Process one instance of this task
                
                # If more instances of this task remain, put it in cooldown
                if count < 0:
                    cooldown_queue.append((count, time + n))
            
            # Check if any tasks have finished their cooldown
            while cooldown_queue and cooldown_queue[0][1] <= time:
                # Move task back to heap when cooldown is over
                count, _ = cooldown_queue.pop(0)
                heapq.heappush(max_heap, count)
        
        return time

def run_task_scheduler_test(tasks, n, expected, test_name):
    """
    Tests the leastInterval function.
    
    Args:
        tasks: List of task names
        n: Cooling interval
        expected: Expected minimum intervals
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.leastInterval(tasks, n)
    
    print(f"{test_name}:")
    print(f"  Input: tasks = {tasks}, n = {n}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_task_scheduler_test(["A","A","A","B","B","B"], 2, 8, "Example 1: ['A','A','A','B','B','B'], n=2 -> 8")
run_task_scheduler_test(["A","C","A","B","D","B"], 1, 6, "Example 2: ['A','C','A','B','D','B'], n=1 -> 6")
run_task_scheduler_test(["A","A","A","B","B","B"], 3, 10, "Example 3: ['A','A','A','B','B','B'], n=3 -> 10")
run_task_scheduler_test(["A"], 0, 1, "Edge case: Single task, n=0 -> 1")
run_task_scheduler_test(["A"], 1, 1, "Edge case: Single task, n=1 -> 1")
run_task_scheduler_test(["A","A"], 2, 4, "Edge case: Two same tasks, n=2 -> 4")
run_task_scheduler_test(["A","A","B","B"], 2, 6, "Edge case: ['A','A','B','B'], n=2 -> 6")
run_task_scheduler_test(["A","A","A","B","B","C","C"], 1, 7, "Edge case: Mixed tasks, n=1 -> 7")
run_task_scheduler_test(["A","A","A","A","A","A","B","C","D","E","F","G"], 2, 16, "Edge case: Many A's, n=2 -> 16")
run_task_scheduler_test(["A","B","C","D","E","F"], 2, 6, "Edge case: All different tasks, n=2 -> 6")