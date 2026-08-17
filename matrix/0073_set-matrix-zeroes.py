from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Sets the entire row and column to 0's if an element is 0.
        Modifies the matrix in-place.
        
        Problem Understanding:
        - Given an m x n integer matrix
        - If an element is 0, set its entire row and column to 0's
        - Must do it in-place with O(1) space complexity
        
        Approach:
        - Use the first row and first column as markers to indicate which rows/columns to zero
        - Use additional variables to handle the special case where first row/column originally had zeros
        - First pass: mark which rows/columns need to be zeroed using first row/column
        - Second pass: apply zeroing based on markers
        - Handle first row/column separately at the end
        
        Time Complexity: O(m * n) where m and n are matrix dimensions
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            matrix: 2D list of integers to be modified in-place
        """
        m, n = len(matrix), len(matrix[0])
        
        # Check if first row originally contains zeros
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        
        # Check if first column originally contains zeros
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # First pass: mark rows and columns that need to be zeroed
        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    # Mark the corresponding position in first row and first column
                    matrix[i][0] = 0  # Mark row i to be zeroed
                    matrix[0][j] = 0  # Mark column j to be zeroed
        
        # Second pass: apply zeroing based on markers (excluding first row/column)
        for i in range(1, m):
            for j in range(1, n):
                # If row i or column j was marked, set matrix[i][j] to 0
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Handle first row: zero it if it originally contained zeros
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Handle first column: zero it if it originally contained zeros
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

def run_set_zeroes_test(matrix, expected, test_name):
    """
    Tests the setZeroes function.
    
    Args:
        matrix: Input matrix to be modified
        expected: Expected matrix after setting zeros
        test_name: Name/description of the test case
    """
    # Make a copy to avoid modifying original for comparison
    original = [row[:] for row in matrix]
    solution = Solution()
    solution.setZeroes(matrix)
    
    print(f"{test_name}:")
    print(f"  Input: {original}")
    print(f"  Expected: {expected}")
    print(f"  Got: {matrix}")
    print(f"  Pass: {matrix == expected}")
    print()

# Run test cases
run_set_zeroes_test([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]], "Example 1: [[1,1,1],[1,0,1],[1,1,1]] -> [[1,0,1],[0,0,0],[1,0,1]]")
run_set_zeroes_test([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]], "Example 2: [[0,1,2,0],[3,4,5,2],[1,3,1,5]] -> [[0,0,0,0],[0,4,5,0],[0,3,1,0]]")
run_set_zeroes_test([[1,2,3,4],[5,0,7,8],[0,10,11,12]], [[0,0,3,4],[0,0,0,0],[0,0,0,0]], "Edge case: Multiple zeros")
run_set_zeroes_test([[1,2],[3,4]], [[1,2],[3,4]], "Edge case: No zeros")
run_set_zeroes_test([[0]], [[0]], "Edge case: Single zero element")
run_set_zeroes_test([[1]], [[1]], "Edge case: Single non-zero element")
run_set_zeroes_test([[0,0,0,0]], [[0,0,0,0]], "Edge case: Row of all zeros")
run_set_zeroes_test([[0],[0],[0],[0]], [[0],[0],[0],[0]], "Edge case: Column of all zeros")
run_set_zeroes_test([[1,0,1],[1,1,1],[1,1,0]], [[0,0,0],[1,0,0],[0,0,0]], "Edge case: Zeros in first row/column")
run_set_zeroes_test([[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]], "Edge case: 2x3 matrix, no zeros")
run_set_zeroes_test([[0,1],[1,0]], [[0,0],[0,0]], "Edge case: 2x2 with zeros at corners")
run_set_zeroes_test([[1,2,0],[0,4,5],[7,8,9]], [[0,0,0],[0,0,0],[0,8,0]], "Edge case: Complex pattern")