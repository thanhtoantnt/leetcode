from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Solves the surrounded regions problem by capturing regions surrounded by X.
        
        Problem Understanding:
        - Given a 2D board with 'X' and 'O'
        - Capture all regions surrounded by X (replace O's with X's)
        - Regions that touch the border cannot be surrounded
        - Only O's that are completely surrounded by X's should be flipped
        
        Approach:
        - Use reverse thinking: find all O's that are NOT surrounded
        - O's on the border or connected to border O's cannot be surrounded
        - Start from border O's and use DFS/BFS to mark all connected O's as safe
        - Flip all remaining O's (not marked as safe) to X's
        - Keep safe O's as O's
        
        Time Complexity: O(M * N) where M and N are board dimensions
        Space Complexity: O(M * N) for the visited array and recursion stack
        
        Args:
            board: 2D board of 'X' and 'O' characters to be modified in-place
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        
        # Create a visited matrix to mark O's that are safe (not surrounded)
        visited = [[False] * n for _ in range(m)]
        
        def dfs(row, col):
            """DFS to mark all connected O's from border as safe"""
            if (row < 0 or row >= m or col < 0 or col >= n or 
                visited[row][col] or board[row][col] == 'X'):
                return
            
            visited[row][col] = True
            
            # Explore all 4 directions
            for dr, dc in directions:
                dfs(row + dr, col + dc)
        
        # Start DFS from all border O's
        # Check first and last rows
        for j in range(n):
            if board[0][j] == 'O' and not visited[0][j]:
                dfs(0, j)
            if m > 1 and board[m-1][j] == 'O' and not visited[m-1][j]:  # Avoid duplicate if only 1 row
                dfs(m-1, j)
        
        # Check first and last columns (skip corners to avoid duplicates)
        for i in range(1, m-1):
            if board[i][0] == 'O' and not visited[i][0]:
                dfs(i, 0)
            if n > 1 and board[i][n-1] == 'O' and not visited[i][n-1]:  # Avoid duplicate if only 1 col
                dfs(i, n-1)
        
        # Flip all O's that are not marked as safe to X's
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'

def run_surrounded_regions_test(board, expected, test_name):
    """
    Tests the solve function.
    
    Args:
        board: Input 2D board of 'X' and 'O' to be modified in-place
        expected: Expected result after modification
        test_name: Name/description of the test case
    """
    import copy
    board_copy = copy.deepcopy(board)
    
    solution = Solution()
    solution.solve(board_copy)
    
    print(f"{test_name}:")
    print(f"  Input: {board}")
    print(f"  Expected: {expected}")
    print(f"  Got: {board_copy}")
    print(f"  Pass: {board_copy == expected}")
    print()

# Run test cases
run_surrounded_regions_test(
    [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ],
    [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"]
    ],
    "Example 1: Mixed surrounded and border-connected regions"
)

run_surrounded_regions_test(
    [["X"]],
    [["X"]],
    "Example 2: Single X -> [['X']]"
)

run_surrounded_regions_test(
    [
        ["O","O","O"],
        ["O","O","O"],
        ["O","O","O"]
    ],
    [
        ["O","O","O"],
        ["O","O","O"],
        ["O","O","O"]
    ],
    "Edge case: All O's connected to border"
)

run_surrounded_regions_test(
    [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","O","O","X"],
        ["X","X","X","X"]
    ],
    [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"]
    ],
    "Edge case: Center surrounded region"
)

run_surrounded_regions_test(
    [
        ["O","X","X","X","X"],
        ["X","O","O","O","X"],
        ["X","O","O","O","X"],
        ["X","O","O","O","X"],
        ["X","X","X","X","O"]
    ],
    [
        ["O","X","X","X","X"],
        ["X","X","X","X","X"],
        ["X","X","X","X","X"],
        ["X","X","X","X","X"],
        ["X","X","X","X","O"]
    ],
    "Edge case: Border-connected regions with surrounded center"
)

run_surrounded_regions_test(
    [
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"]
    ],
    [
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"],
        ["O","O","O","O"]
    ],
    "Edge case: All O's on border -> all stay O"
)

run_surrounded_regions_test(
    [
        ["X","X","X"],
        ["X","O","X"],
        ["X","X","X"]
    ],
    [
        ["X","X","X"],
        ["X","X","X"],
        ["X","X","X"]
    ],
    "Edge case: Single surrounded O"
)

run_surrounded_regions_test(
    [
        ["O","X","O","O","X","X"],
        ["O","X","X","X","O","X"],
        ["X","O","O","X","O","O"],
        ["X","O","X","X","X","X"],
        ["O","O","X","O","X","O"],
        ["X","X","O","O","O","X"]
    ],
    [
        ["O","X","O","O","X","X"],
        ["O","X","X","X","X","X"],
        ["X","X","X","X","X","O"],
        ["X","X","X","X","X","X"],
        ["O","X","X","X","X","O"],
        ["X","X","O","O","O","X"]
    ],
    "Edge case: Complex mixed regions"
)