from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            
            # if visted
            if grid[i][j] == "0":
                return

            # marked as visited
            grid[i][j] = "0"
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in directions:
                dfs(i + dx, j+dy)

        islands = 0
        for i in range(rows):
            for j in range(cols):
                # print(f"grid = {grid[i][j]}")
                if grid[i][j] == "1":
                    islands = islands + 1
                    dfs(i, j)

        
        return islands

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Single Island
    grid1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
    ]
    # Expected: 1
    # print(sol.numIslands(grid1))

    # Test Case 2: Multiple Islands
    grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    # Expected: 3

    # Test Case 3: No Islands (All Water)
    grid3 = [
    ["0","0","0"],
    ["0","0","0"],
    ["0","0","0"]
    ]
    # Expected: 0

    # Test Case 4: All Land (One Big Island)
    grid4 = [
    ["1","1","1"],
    ["1","1","1"],
    ["1","1","1"]
    ]
    # Expected: 1
    print(sol.numIslands(grid4))

    # Test Case 5: Diagonal Islands (Should be separate)
    grid5 = [
    ["1","0","0","0","1"],
    ["0","1","0","1","0"],
    ["0","0","1","0","0"],
    ["0","1","0","1","0"],
    ["1","0","0","0","1"]
    ]
    # Expected: 5

    # Test Case 6: Single Cell Islands
    grid6 = [
    ["1","0","1","0","1"],
    ["0","0","0","0","0"],
    ["1","0","1","0","1"],
    ["0","0","0","0","0"],
    ["1","0","1","0","1"]
    ]
    # Expected: 9

    # Test Case 7: Empty Grid
    grid7 = []
    # Expected: 0

    # Test Case 8: 1x1 Grid with Land
    grid8 = [["1"]]
    # Expected: 1

    # Test Case 9: 1x1 Grid with Water
    grid9 = [["0"]]
    # Expected: 0

    # Test Case 10: Complex Shape
    grid10 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","1"],
    ["0","0","1","1","1"],
    ["0","0","0","0","0"],
    ["1","0","0","0","1"]
    ]
    # Expected: 4