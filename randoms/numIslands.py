from typing import List

def numberOfIslands(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    
    def DFS(i: int, j: int):
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return
        
        if grid[i][j] == "0":
            return 
        
        grid[i][j] = "0"
        DFS(i+1, j)
        DFS(i-1, j)
        DFS(i, j + 1)
        DFS(i, j - 1)
    
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                count += 1
                DFS(i, j)

    return count

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(numberOfIslands(grid))

