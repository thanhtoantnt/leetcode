from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Searches for a value in a sorted matrix where each row is sorted in ascending order
        from left to right and the first integer of each row is greater than the last 
        integer of the previous row.
        
        Problem Understanding:
        - Matrix is sorted both row-wise and column-wise in a specific way
        - Each row is sorted in ascending order
        - First element of each row is greater than last element of previous row
        - Need to find target in O(log(m * n)) time
        
        Approach:
        - Treat the 2D matrix as a flattened 1D sorted array
        - Use binary search on the virtual 1D array
        - Convert 1D index to 2D coordinates: row = index // cols, col = index % cols
        - Perform standard binary search logic
        
        Time Complexity: O(log(m * n)) where m and n are matrix dimensions
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            matrix: 2D matrix with sorted properties
            target: Value to search for
            
        Returns:
            True if target exists in matrix, False otherwise
        """
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Convert 1D index to 2D coordinates
            mid_row = mid // cols
            mid_col = mid % cols
            mid_val = matrix[mid_row][mid_col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False

def run_search_matrix_test(matrix, target, expected, test_name):
    """
    Tests the searchMatrix function.
    
    Args:
        matrix: 2D matrix to search in
        target: Value to search for
        expected: Expected result (True/False)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.searchMatrix(matrix, target)
    
    print(f"{test_name}:")
    print(f"  Input: target = {target}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_search_matrix_test([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True, "Example 1: Matrix with target 3 -> True")
run_search_matrix_test([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False, "Example 2: Matrix with target 13 -> False")
run_search_matrix_test([[1]], 1, True, "Edge case: Single element matrix, target=1 -> True")
run_search_matrix_test([[1]], 2, False, "Edge case: Single element matrix, target=2 -> False")
run_search_matrix_test([[1,2,3],[4,5,6],[7,8,9]], 5, True, "Edge case: 3x3 matrix, target=5 -> True")
run_search_matrix_test([[1,2,3],[4,5,6],[7,8,9]], 10, False, "Edge case: 3x3 matrix, target=10 -> False")
run_search_matrix_test([[1,3,5]], 3, True, "Edge case: Single row matrix, target=3 -> True")
run_search_matrix_test([[1],[3],[5]], 3, True, "Edge case: Single column matrix, target=3 -> True")
run_search_matrix_test([[1,3,5,7,9],[11,13,15,17,19],[21,23,25,27,29]], 15, True, "Edge case: Larger matrix, target=15 -> True")
run_search_matrix_test([[1,3,5,7,9],[11,13,15,17,19],[21,23,25,27,29]], 16, False, "Edge case: Larger matrix, target=16 -> False")
run_search_matrix_test([], 0, False, "Edge case: Empty matrix -> False")
run_search_matrix_test([[]], 0, False, "Edge case: Matrix with empty row -> False")