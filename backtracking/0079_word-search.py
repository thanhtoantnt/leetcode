from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Checks if a word exists in the given 2D character grid.
        
        Problem Understanding:
        - Given a 2D board of characters and a word
        - Find if the word exists in the grid
        - The word can be constructed from letters of sequentially adjacent cells
        - Adjacent cells are horizontally or vertically neighboring
        - Same cell cannot be used more than once
        
        Approach:
        - Use backtracking with DFS
        - For each cell that matches the first character, start DFS
        - Mark visited cells temporarily to avoid reuse in current path
        - Explore all 4 directions (up, down, left, right)
        - Backtrack by restoring the cell after exploration
        - Early termination when word is found
        
        Time Complexity: O(M * N * 4^L) where M,N are board dimensions, L is word length
        Space Complexity: O(L) for recursion stack (excluding board space)
        
        Args:
            board: 2D grid of characters
            word: Word to search for
            
        Returns:
            True if word exists in board, False otherwise
        """
        if not board or not board[0] or not word:
            return False
        
        m, n = len(board), len(board[0])
        
        def dfs(row, col, word_index):
            # Base case: if we've matched all characters
            if word_index == len(word):
                return True
            
            # Check bounds and character match
            if (row < 0 or row >= m or col < 0 or col >= n or 
                board[row][col] != word[word_index]):
                return False
            
            # Mark current cell as visited by temporarily changing its value
            temp = board[row][col]
            board[row][col] = "#"  # Use a special character to mark visited
            
            # Explore all 4 directions
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                if dfs(row + dr, col + dc, word_index + 1):
                    # Restore the cell before returning
                    board[row][col] = temp
                    return True
            
            # Backtrack: restore the cell
            board[row][col] = temp
            return False
        
        # Try starting from each cell
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False

def run_word_search_test(board, word, expected, test_name):
    """
    Tests the exist function.
    
    Args:
        board: 2D grid of characters
        word: Word to search for
        expected: Expected result (True/False)
        test_name: Name/description of the test case
    """
    # Make a copy of the board to avoid modifying the original
    import copy
    board_copy = copy.deepcopy(board)
    
    solution = Solution()
    result = solution.exist(board_copy, word)
    
    print(f"{test_name}:")
    print(f"  Input: word = '{word}'")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_word_search_test([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True, "Example 1: Board with word 'ABCCED' -> True")
run_word_search_test([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True, "Example 2: Board with word 'SEE' -> True")
run_word_search_test([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False, "Example 3: Board with word 'ABCB' -> False")
run_word_search_test([["A"]], "A", True, "Edge case: Single cell with matching letter -> True")
run_word_search_test([["A"]], "B", False, "Edge case: Single cell with non-matching letter -> False")
run_word_search_test([["A","B"],["C","D"]], "ABCD", False, "Edge case: 2x2 grid, impossible path -> False")
run_word_search_test([["A","B"],["C","D"]], "ABDC", True, "Edge case: 2x2 grid, valid path -> True")
run_word_search_test([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB", True, "Edge case: Complex board with word 'AAB' -> True")
run_word_search_test([], "A", False, "Edge case: Empty board -> False")
run_word_search_test([["A","B","C"]], "ABC", True, "Edge case: Single row -> True")
run_word_search_test([["A"],["B"],["C"]], "ABC", True, "Edge case: Single column -> True")
run_word_search_test([["A","A","A","A"],["A","A","A","A"],["A","A","A","A"]], "AAAAAAAAAAAAA", False, "Edge case: All same letters, longer word -> False")