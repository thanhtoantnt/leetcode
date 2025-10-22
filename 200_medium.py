from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Step 1: Handle edge case - empty grid
        if not grid or not grid[0]:
            return 0
        
        # Step 2: Get grid dimensions
        rows, cols = len(grid), len(grid[0])
        islands = 0
        
        # Step 3: Define DFS helper function
        def dfs(i, j):
            """
            Depth-First Search to mark all connected land cells as visited
            """
            # Base case 1: Check if out of bounds
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            
            # Base case 2: Check if current cell is water or already visited
            if grid[i][j] != "1":
                return
            
            # Step 4: Mark current cell as visited by changing "1" to "0"
            grid[i][j] = "0"
            
            # Step 5: Recursively explore all 4 directions
            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left
        
        # Step 6: Main loop - scan through every cell in the grid
        for i in range(rows):
            for j in range(cols):
                # If we find unvisited land, we found a new island
                if grid[i][j] == "1":
                    islands += 1
                    # Step 7: Use DFS to mark all connected land as visited
                    dfs(i, j)
        
        return islands

def test_num_islands():
    sol = Solution()
    
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(sol.numIslands(grid1))  # Expected: 1
    
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(sol.numIslands(grid2))  # Expected: 3
    
    grid3 = [["1"]]  # Expected: 1
    print(sol.numIslands(grid3))
    
    grid4 = [["0"]]  # Expected: 0
    print(sol.numIslands(grid4))

test_num_islands()