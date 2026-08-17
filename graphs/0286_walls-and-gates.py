from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Fills each empty room with the distance to its nearest treasure.
        
        Problem Understanding:
        - Given a grid where:
          - -1 represents a wall or obstacle
          - 0 represents a treasure chest
          - 2147483647 (2^31 - 1) represents an empty room (Infinity)
        - Fill each empty room with the distance to its nearest treasure
        - If a room cannot reach any treasure, keep it as INF
        
        Approach:
        - Use Multi-source BFS starting from all treasures (0s) simultaneously
        - Add all treasure positions to queue initially
        - For each position in BFS, update adjacent rooms with distance + 1
        - Only process rooms that haven't been visited (still have INF value)
        - This ensures shortest distance to nearest treasure for each room
        
        Time Complexity: O(M * N) where M and N are grid dimensions
        Space Complexity: O(M * N) for the queue in worst case (all cells are treasures)
        
        Args:
            grid: 2D grid with -1 (walls), 0 (treasures), and 2147483647 (empty rooms)
        """
        if not grid or not grid[0]:
            return
        
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        # Queue for BFS - start with all treasure positions
        queue = deque()
        
        # Add all treasure positions to the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:  # Treasure found
                    queue.append((i, j))
        
        # Multi-source BFS
        while queue:
            row, col = queue.popleft()
            
            # Check all 4 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check bounds and if the cell is an unvisited empty room
                if (0 <= new_row < m and 0 <= new_col < n and 
                    grid[new_row][new_col] == 2147483647):  # INF means unvisited empty room
                    # Update distance to treasure
                    grid[new_row][new_col] = grid[row][col] + 1
                    # Add to queue for further exploration
                    queue.append((new_row, new_col))

def run_islands_and_treasure_test(grid, expected, test_name):
    """
    Tests the islandsAndTreasure function.
    
    Args:
        grid: Input 2D grid to be modified in-place
        expected: Expected result after modification
        test_name: Name/description of the test case
    """
    import copy
    grid_copy = copy.deepcopy(grid)
    
    solution = Solution()
    solution.islandsAndTreasure(grid_copy)
    
    print(f"{test_name}:")
    print(f"  Input: {grid}")
    print(f"  Expected: {expected}")
    print(f"  Got: {grid_copy}")
    print(f"  Pass: {grid_copy == expected}")
    print()

# Run test cases
run_islands_and_treasure_test(
    [
        [2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]
    ],
    [
        [3,-1,0,1],
        [2,3,4,-1],
        [1,-1,5,-1],
        [0,-1,6,7]
    ],
    "Example 1: Mixed grid with treasures, walls, and empty rooms"
)

run_islands_and_treasure_test(
    [[0]],
    [[0]],
    "Example 2: Single treasure -> [[0]]"
)

run_islands_and_treasure_test(
    [[2147483647]],
    [[2147483647]],
    "Example 3: Single empty room -> [[2147483647]]"
)

run_islands_and_treasure_test(
    [[-1]],
    [[-1]],
    "Example 4: Single wall -> [[-1]]"
)

run_islands_and_treasure_test(
    [
        [0,2147483647,2147483647,2147483647],
        [2147483647,2147483647,2147483647,2147483647],
        [2147483647,2147483647,2147483647,2147483647],
        [2147483647,2147483647,2147483647,0]
    ],
    [
        [0,1,2,3],
        [1,2,3,4],
        [2,3,4,5],
        [3,4,5,0]
    ],
    "Edge case: Treasures at opposite corners"
)

run_islands_and_treasure_test(
    [
        [2147483647,2147483647,2147483647],
        [2147483647,-1,2147483647],
        [2147483647,2147483647,2147483647]
    ],
    [
        [2147483647,2147483647,2147483647],
        [2147483647,-1,2147483647],
        [2147483647,2147483647,2147483647]
    ],
    "Edge case: Empty rooms surrounded by walls"
)

run_islands_and_treasure_test(
    [
        [0,-1,0],
        [-1,2147483647,-1],
        [0,-1,0]
    ],
    [
        [0,-1,0],
        [-1,2147483647,-1],
        [0,-1,0]
    ],
    "Edge case: Treasures with walls blocking some paths"
)

run_islands_and_treasure_test(
    [
        [0,0,0],
        [0,2147483647,0],
        [0,0,0]
    ],
    [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ],
    "Edge case: Multiple adjacent treasures"
)