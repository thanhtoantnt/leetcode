from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return matrix
        
        rows = len(matrix)
        cols = len(matrix[0])

        zero_in_first_row = any(matrix[0][j] == 0 for j in range(cols))
        zero_in_first_col = any(matrix[i][0] == 0 for i in range(rows))

        # use the first row and first col to store the marking

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if zero_in_first_row:
            for i in range(cols):
                matrix[0][i] = 0
        
        if zero_in_first_col:
            for i in range(rows):
                matrix[i][0] = 0

# matrix = [[1,1,1],[1,0,1],[1,1,1]]
# matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix = [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]

if __name__ == "__main__":
    sol = Solution()
    print(matrix)
    print(sol.setZeroes(matrix))