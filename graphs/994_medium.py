from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Finds the minimum number of minutes until all fresh oranges become rotten.
        
        Problem Understanding:
        - Given a grid where:
          - 0 represents an empty cell
          - 1 represents a fresh orange
          - 2 represents a rotten orange
        - Every minute, any fresh orange adjacent to a rotten orange becomes rotten
        - Return the minimum time until no fresh oranges remain
        - If impossible, return -1
        
        Approach:
        - Use Multi-source BFS starting from all initially rotten oranges
        - Add all rotten oranges to queue initially with time 0
        - For each position in BFS, rot adjacent fresh oranges and add to queue with time+1
        - Track total fresh oranges and check if all were rotted
        - Return the maximum time taken to rot any orange
        
        Time Complexity: O(M * N) where M and N are grid dimensions
        Space Complexity: O(M * N) for the queue in worst case (all cells are oranges)
        
        Args:
            grid: 2D grid with 0 (empty), 1 (fresh), and 2 (rotten)
            
        Returns:
            Minimum minutes until all oranges are rotten, or -1 if impossible
        """
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        # Count fresh oranges and add rotten oranges to queue
        fresh_count = 0
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i, j, 0))  # (row, col, time)
        
        # If no fresh oranges initially, return 0
        if fresh_count == 0:
            return 0
        
        max_time = 0
        
        # Multi-source BFS
        while queue:
            row, col, time = queue.popleft()
            max_time = max(max_time, time)
            
            # Check all 4 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check bounds and if the cell is a fresh orange
                if (0 <= new_row < m and 0 <= new_col < n and 
                    grid[new_row][new_col] == 1):
                    # Rot the fresh orange
                    grid[new_row][new_col] = 2
                    fresh_count -= 1
                    # Add to queue with updated time
                    queue.append((new_row, new_col, time + 1))
        
        # If there are still fresh oranges remaining, return -1
        return -1 if fresh_count > 0 else max_time

def run_rotting_oranges_test(grid, expected, test_name):
    """
    Tests the orangesRotting function.
    
    Args:
        grid: Input 2D grid of oranges
        expected: Expected minimum minutes or -1
        test_name: Name/description of the test case
    """
    import copy
    grid_copy = copy.deepcopy(grid)
    
    solution = Solution()
    result = solution.orangesRotting(grid_copy)
    
    print(f"{test_name}:")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_rotting_oranges_test(
    [
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ],
    4,
    "Example 1: [2,1,1],[1,1,0],[0,1,1] -> 4 minutes"
)

run_rotting_oranges_test(
    [
        [2,1,1],
        [0,1,1],
        [1,0,1]
    ],
    -1,
    "Example 2: [2,1,1],[0,1,1],[1,0,1] -> -1 (impossible)"
)

run_rotting_oranges_test(
    [[0,2]],
    0,
    "Example 3: [0,2] -> 0 (no fresh oranges)"
)

run_rotting_oranges_test(
    [
        [2,1,1],
        [1,1,1],
        [0,1,2]
    ],
    2,
    "Edge case: Multiple rotten oranges initially"
)

run_rotting_oranges_test(
    [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ],
    -1,
    "Edge case: All fresh oranges, no initial rotten ones"
)

run_rotting_oranges_test(
    [
        [2,2,2],
        [2,2,2],
        [2,2,2]
    ],
    0,
    "Edge case: All rotten oranges initially"
)

run_rotting_oranges_test(
    [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ],
    0,
    "Edge case: All empty cells"
)

run_rotting_oranges_test(
    [
        [1,2,0,1],
        [0,1,0,2],
        [0,0,1,0],
        [2,0,0,1]
    ],
    3,
    "Edge case: Complex grid with multiple fresh and rotten oranges"
)

run_rotting_oranges_test(
    [[1]],
    -1,
    "Edge case: Single fresh orange"
)

run_rotting_oranges_test(
    [[2]],
    0,
    "Edge case: Single rotten orange"
)

run_rotting_oranges_test(
    [[1,1,1,1,1,1,1,1,1,1]],
    -1,
    "Edge case: Row of fresh oranges, no rotten ones"
)

run_rotting_oranges_test(
    [
        [0,1,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ],
    1,
    "Edge case: Fresh orange next to rotten orange"
)