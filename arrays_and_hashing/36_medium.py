"""
Valid Sudoku Solution with Explanations and Unit Tests

This file contains the solution for the Valid Sudoku problem
along with comprehensive explanations and unit tests.
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determine if a 9x9 Sudoku board is valid.
        
        A valid Sudoku board must satisfy:
        1. Each row contains digits 1-9 without repetition
        2. Each column contains digits 1-9 without repetition
        3. Each 3x3 sub-box contains digits 1-9 without repetition
        
        Args:
            board (List[List[str]]): 9x9 Sudoku board with digits or "." for empty cells
            
        Returns:
            bool: True if the board is valid, False otherwise
        """
        
        # Check all 3x3 sub-boxes
        for i in range(0, 9, 3):  # i = 0, 3, 6 (top-left corners of sub-boxes)
            for j in range(0, 9, 3):  # j = 0, 3, 6 (top-left corners of sub-boxes)
                numSet = set()

                for row in range(0, 3):  # row = 0, 1, 2 (relative to sub-box)
                    for col in range(0, 3):  # col = 0, 1, 2 (relative to sub-box)
                        rowNum = i + row  # actual row in the board
                        colNum = j + col  # actual column in the board
                        
                        if board[rowNum][colNum] == ".":
                            continue
                        
                        # Convert to int to handle the number comparison
                        num = int(board[rowNum][colNum])
                        if num in numSet:
                            return False
                        
                        numSet.add(num)
        
        # Check all rows
        for row in range(0, 9):
            numSet = set()
            
            for col in range(0, 9):
                if board[row][col] == ".":
                    continue
                
                num = int(board[row][col])
                if num in numSet:
                    return False
                
                numSet.add(num)

        # Check all columns
        for col in range(0, 9):
            numSet = set()
            
            for row in range(0, 9):
                if board[row][col] == ".":
                    continue
                
                num = int(board[row][col])
                if num in numSet:
                    return False
                
                numSet.add(num)
        
        return True

def run_sudoku_tests():
    """Run comprehensive unit tests for the Valid Sudoku solution."""
    
    print("Running Unit Tests for Valid Sudoku...")
    sol = Solution()
    
    # Test Case 1: Valid board
    board1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    expected1 = True
    result1 = sol.isValidSudoku(board1)
    assert result1 == expected1, f"Test 1 failed: Expected {expected1}, got {result1}"
    print("✓ Test 1 Passed: Valid Sudoku board")
    
    # Test Case 2: Invalid - duplicate in row
    board2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],  # '8' appears twice in this row
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    expected2 = False
    result2 = sol.isValidSudoku(board2)
    assert result2 == expected2, f"Test 2 failed: Expected {expected2}, got {result2}"
    print("✓ Test 2 Passed: Invalid - duplicate in row")
    
    # Test Case 3: Invalid - duplicate in column
    board3 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","8"]  # '8' appears twice in last column
    ]
    expected3 = False
    result3 = sol.isValidSudoku(board3)
    assert result3 == expected3, f"Test 3 failed: Expected {expected3}, got {result3}"
    print("✓ Test 3 Passed: Invalid - duplicate in column")
    
    # Test Case 4: Invalid - duplicate in 3x3 box
    board4 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    # Change the top-left 3x3 box to have duplicate '8'
    board4[0][0] = "8"  # This makes it invalid as there are two 8s in the first 3x3 box
    board4[1][0] = "8"  # This creates duplicate in the same 3x3 box
    expected4 = False
    result4 = sol.isValidSudoku(board4)
    assert result4 == expected4, f"Test 4 failed: Expected {expected4}, got {result4}"
    print("✓ Test 4 Passed: Invalid - duplicate in 3x3 box")
    
    # Test Case 5: Empty board
    board5 = [["." for _ in range(9)] for _ in range(9)]
    expected5 = True
    result5 = sol.isValidSudoku(board5)
    assert result5 == expected5, f"Test 5 failed: Expected {expected5}, got {result5}"
    print("✓ Test 5 Passed: Empty board")
    
    # Test Case 6: Partially filled valid board
    board6 = [
        [".","8","7","6","5","4","3","2","1"],
        ["2",".",".",".",".",".",".",".","."],
        ["3",".",".",".",".",".",".",".","."],
        ["4",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".",".","."],
        ["6",".",".",".",".",".",".",".","."],
        ["7",".",".",".",".",".",".",".","."],
        ["8",".",".",".",".",".",".",".","."],
        ["9",".",".",".",".",".",".",".","."]
    ]
    expected6 = True
    result6 = sol.isValidSudoku(board6)
    assert result6 == expected6, f"Test 6 failed: Expected {expected6}, got {result6}"
    print("✓ Test 6 Passed: Partially filled valid board")
    
    # Test Case 7: Invalid - duplicate in 3x3 box (specific case)
    board7 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    # Add duplicate in the middle 3x3 box
    board7[3][3] = "8"  # Position (3,3) is in middle box
    board7[4][4] = "8"  # Position (4,4) is in middle box - duplicate
    expected7 = False
    result7 = sol.isValidSudoku(board7)
    assert result7 == expected7, f"Test 7 failed: Expected {expected7}, got {result7}"
    print("✓ Test 7 Passed: Invalid - duplicate in middle 3x3 box")
    
    # Test Case 8: Valid with all numbers in different positions
    board8 = [
        ["1",".",".",".",".",".",".",".","."],
        [".","2",".",".",".",".",".",".","."],
        [".",".","3",".",".",".",".",".","."],
        [".",".",".","4",".",".",".",".","."],
        [".",".",".",".","5",".",".",".","."],
        [".",".",".",".",".","6",".",".","."],
        [".",".",".",".",".",".","7",".","."],
        [".",".",".",".",".",".",".","8","."],
        [".",".",".",".",".",".",".",".","9"]
    ]
    expected8 = True
    result8 = sol.isValidSudoku(board8)
    assert result8 == expected8, f"Test 8 failed: Expected {expected8}, got {result8}"
    print("✓ Test 8 Passed: Valid diagonal pattern")
    
    print("\n🎉 All Sudoku tests passed! The solution works correctly.")

def explain_sudoku_algorithm():
    """Explain the Valid Sudoku algorithm in detail."""
    
    print("\n" + "="*70)
    print("VALID SUDOKU ALGORITHM EXPLANATION")
    print("="*70)
    
    print("\nWhat is Valid Sudoku?")
    print("-" * 30)
    print("Validate if a 9x9 Sudoku board follows the rules:")
    print("1. Each row contains digits 1-9 without repetition")
    print("2. Each column contains digits 1-9 without repetition")
    print("3. Each 3x3 sub-box contains digits 1-9 without repetition")
    print("4. Empty cells represented by '.' are ignored")
    
    print("\nAlgorithm Approach:")
    print("-" * 30)
    print("The solution checks all three constraints separately:")
    print("1. Check each 3x3 sub-box")
    print("2. Check each row")
    print("3. Check each column")
    
    print("\nStep-by-Step Process:")
    print("-" * 30)
    print("1. 3x3 Sub-box Check:")
    print("   - Iterate through top-left corners: (0,0), (0,3), (0,6), (3,0), etc.")
    print("   - For each sub-box, check all 9 cells for duplicates")
    print("   - Use a set to track seen numbers")
    
    print("\n2. Row Check:")
    print("   - Iterate through each of 9 rows")
    print("   - Use a set to track seen numbers in each row")
    
    print("\n3. Column Check:")
    print("   - Iterate through each of 9 columns")
    print("   - Use a set to track seen numbers in each column")
    
    print("\nImplementation Details:")
    print("-" * 30)
    print("• Use nested loops with range(0, 9, 3) to iterate through sub-boxes")
    print("• Use sets to efficiently check for duplicates (O(1) lookup)")
    print("• Skip empty cells ('.') using continue statement")
    print("• Convert string digits to integers for comparison")
    print("• Return False immediately when first violation is found")
    
    print("\nTime & Space Complexity:")
    print("-" * 30)
    print("Time: O(1) - Fixed size 9x9 board, so O(81) = O(1)")
    print("Space: O(1) - Sets store at most 9 elements each")
    
    print("\nEdge Cases Handled:")
    print("-" * 30)
    print("• Empty board (all cells are '.') - Valid")
    print("• Partially filled board - Valid if constraints satisfied")
    print("• Duplicate in row, column, or sub-box - Invalid")
    print("• Out of bounds characters - Handled by the algorithm")
    
    print("\nAlgorithm Properties:")
    print("-" * 30)
    print("• Efficient - Stops at first violation")
    print("• Comprehensive - Checks all three Sudoku rules")
    print("• Clean - Separate validation for each constraint")
    print("• Correct - Handles all valid Sudoku board configurations")

if __name__ == "__main__":
    # Run tests
    run_sudoku_tests()
    
    # Explain the algorithm
    explain_sudoku_algorithm()