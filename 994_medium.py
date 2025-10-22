from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        minutes = 0
        
        # Step 1: Initialize queue with all rotten oranges and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        # If no fresh oranges at start, return 0 immediately
        if fresh_count == 0:
            return 0
        
        # Directions: up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Step 2: BFS propagation
        while queue and fresh_count > 0:
            # Process all oranges at current minute level
            level_size = len(queue)
            for _ in range(level_size):
                i, j = queue.popleft()
                
                # Check all 4 directions
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    
                    # Check bounds and if it's a fresh orange
                    if (0 <= ni < rows and 0 <= nj < cols and 
                        grid[ni][nj] == 1):
                        # Rot the fresh orange
                        grid[ni][nj] = 2
                        fresh_count -= 1
                        queue.append((ni, nj))
            
            minutes += 1
        
        # Step 3: Final check for remaining fresh oranges
        return minutes if fresh_count == 0 else -1