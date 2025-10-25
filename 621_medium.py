from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # hash
        htbl = {}
        for task in tasks:
            htbl[task] = htbl.get(task, 0) + 1

        # waiting htbl
        waiting = {}
        for key in htbl.keys():
            waiting[key] = 1

        intervals = 0
        
        while htbl:
            # decreasing waiting time
            for task, value in htbl.items():
                if waiting[task] >= 1:
                    waiting[task] = waiting.get(task) - 1
                    # print(f"waiting[{task}] = {waiting[task]}")

            # choose the first task to run, or idel
            is_run = False
            for task, value in htbl.items():
                # run this task
                # print(f"is_run = {is_run} and value = {value}")
                if not is_run and waiting[task] == 0:
                    htbl[task] = htbl.get(task) - 1
                    intervals += 1
                    is_run = True
                    print(f"run = {task}")
                    if htbl[task] == 0:
                        htbl.pop(task)
                        waiting.pop(task)              
                    else:
                        waiting[task] = n + 1
                    break

            if not is_run:
                intervals += 1
                print("run = idle")
            
        return intervals

if __name__ == "__main__":
    sol = Solution()

    # # Test case 1
    # tasks1 = ["A","A","A","B","B","B"]
    # n1 = 2
    # print(sol.leastInterval(tasks1, n1))  # Expected: 8
    
    # # Test case 2 - no cooldown
    # tasks2 = ["A","A","A","B","B","B"]
    # n2 = 0
    # print(sol.leastInterval(tasks2, n2))  # Expected: 6

    # # Test case 3 - one task type
    # tasks3 = ["A","A","A","A","A","A"]
    # n3 = 2
    # print(sol.leastInterval(tasks3, n3))  # Expected: 16
    
    # Test case 4 - mixed tasks
    # tasks4 = ["A","A","A","B","B","B","C","C","C","D","D","E"]
    tasks4 = ["B","C","D","A","A","A","A","G"]
    n4 = 1
    print(sol.leastInterval(tasks4, n4))  # Expected: 12