from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        # Step 1: Handle edge case - empty grid
        if not grid or not grid[0]:
            return 0
        
        # Step 2: Get grid dimensions
        rows, cols = len(grid), len(grid[0])
        islands = 0

        colors = [[0] * cols for _ in range(rows)]
        
        # count during the DFS instead of using a second pass
        def dfsOpt(i, j, color):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 0
            colors[i][j] = color
            
            # Return 1 (current cell) + sum of all connected cells
            return (1 + dfs(i+1, j, color) + dfs(i-1, j, color) + 
                    dfs(i, j+1, color) + dfs(i, j-1, color))

        # Step 3: Define DFS helper function
        def dfs(i, j, color):
            """
            Depth-First Search to mark all connected land cells as visited
            """
            # Base case 1: Check if out of bounds
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            
            # Base case 2: Check if current cell is water or already visited
            if grid[i][j] != 1:
                return
            
            # Step 4: Mark current cell as visited by changing "1" to "0"
            grid[i][j] = 0
            colors[i][j] = color
            # print(f"color = {color} at i, j = {i}, {j}")
            
            # Step 5: Recursively explore all 4 directions
            dfs(i + 1, j, color)  # Down
            dfs(i - 1, j, color)  # Up
            dfs(i, j + 1, color)  # Right
            dfs(i, j - 1, color)  # Left
        
        # Step 6: Main loop - scan through every cell in the grid
        for i in range(rows):
            for j in range(cols):
                # If we find unvisited land, we found a new island
                if grid[i][j] == 1:
                    # Step 7: Use DFS to mark all connected land as visited
                    islands += 1
                    # print(f"dfs({i}, {j}, {islands})")
                    dfs(i, j, islands)

        cells = [0] * (islands + 1)
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                cells[colors[i][j]] += 1

        for index in range(1, islands + 1):
            max_area = max(max_area, cells[index])
        
        return max_area

def test_max_area():
    sol = Solution()
    
    grid1 = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    print(sol.maxAreaOfIsland(grid1))  # Expected: 6
    
    grid2 = [[0,0,0,0,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid2))  # Expected: 0
    
    grid3 = [[1]]  # Expected: 1
    print(sol.maxAreaOfIsland(grid3))
    
    grid4 = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]
    ]
    print(sol.maxAreaOfIsland(grid4))  # Expected: 4

test_max_area()