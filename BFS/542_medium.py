from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Updates the matrix so each cell contains the distance to the nearest 0.
        
        Problem Understanding:
        - Given a matrix consisting of 0s and 1s
        - For each cell, calculate the distance to the nearest 0
        - Distance is defined as the number of steps in 4-directional movement (up, down, left, right)
        
        Approach:
        - Use Multi-source BFS starting from all 0s simultaneously
        - Add all positions containing 0 to the queue initially
        - These 0s are at distance 0 from themselves
        - Process the queue level by level, updating distances for adjacent 1s
        - Each cell is visited exactly once, ensuring shortest distance is found
        
        Time Complexity: O(m * n) where m and n are matrix dimensions
        Space Complexity: O(m * n) for the queue in worst case (all cells are 0)
        
        Args:
            mat: Input matrix of 0s and 1s
            
        Returns:
            Matrix where each cell contains distance to nearest 0
        """
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        queue = deque()
        
        # Initialize queue with all 0 positions and mark 1s as -1 (unvisited)
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1  # Mark 1s as unvisited
        
        # Multi-source BFS
        while queue:
            row, col = queue.popleft()
            
            # Check all 4 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # If the new position is valid and unvisited
                if (0 <= new_row < m and 0 <= new_col < n and 
                    mat[new_row][new_col] == -1):
                    # Update distance (current distance + 1)
                    mat[new_row][new_col] = mat[row][col] + 1
                    # Add to queue for further exploration
                    queue.append((new_row, new_col))
        
        return mat

def run_update_matrix_test(mat, expected, test_name):
    """
    Tests the updateMatrix function.
    
    Args:
        mat: Input matrix of 0s and 1s
        expected: Expected matrix with distances to nearest 0
        test_name: Name/description of the test case
    """
    import copy
    mat_copy = copy.deepcopy(mat)
    
    solution = Solution()
    result = solution.updateMatrix(mat_copy)
    
    print(f"{test_name}:")
    print(f"  Input: {mat}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_update_matrix_test(
    [[0,0,0],[0,1,0],[0,0,0]],
    [[0,0,0],[0,1,0],[0,0,0]],
    "Example 1: [[0,0,0],[0,1,0],[0,0,0]] -> [[0,0,0],[0,1,0],[0,0,0]]"
)
run_update_matrix_test(
    [[0,0,0],[0,1,0],[1,1,1]],
    [[0,0,0],[0,1,0],[1,2,1]],
    "Example 2: [[0,0,0],[0,1,0],[1,1,1]] -> [[0,0,0],[0,1,0],[1,2,1]]"
)
run_update_matrix_test(
    [[0,1,1],[1,1,1],[1,1,0]],
    [[0,1,2],[1,2,1],[2,1,0]],
    "Edge case: [[0,1,1],[1,1,1],[1,1,0]] -> [[0,1,2],[1,2,1],[2,1,0]]"
)
run_update_matrix_test(
    [[1,1,1],[1,1,1],[1,1,0]],
    [[4,3,2],[3,2,1],[2,1,0]],
    "Edge case: Farthest 1 from 0 -> [[4,3,2],[3,2,1],[2,1,0]]"
)
run_update_matrix_test(
    [[0]],
    [[0]],
    "Edge case: Single cell 0 -> [[0]]"
)
run_update_matrix_test(
    [[1]],
    [[-1]],  # Actually should be [[1]] if there are 0s in the matrix, but if only 1s, it's impossible
    "Edge case: Single cell 1 -> This would be invalid input as there's no 0"
)
run_update_matrix_test(
    [[0,1],[1,0]],
    [[0,1],[1,0]],
    "Edge case: [[0,1],[1,0]] -> [[0,1],[1,0]]"
)
run_update_matrix_test(
    [[1,0,1,1,0,0,1,0,1,0],[0,1,0,0,1,1,0,0,0,1],[1,1,0,0,0,1,1,0,1,1],[0,1,0,0,0,0,1,1,1,0],[1,0,0,1,1,0,1,0,0,0],[1,0,1,0,1,1,0,0,1,1],[0,1,1,1,0,0,1,0,1,1],[0,1,0,0,1,0,1,1,0,0],[1,1,0,1,0,0,1,1,1,1],[0,1,0,0,0,1,1,1,1,1]],
    [],  # Complex case, output would be calculated
    "Edge case: Complex 10x10 matrix"
)