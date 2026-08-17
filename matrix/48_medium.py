from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(0, n):
            for j in range(0, n):
                if i <= j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        print(matrix)
        mid = n // 2
        for i in range(0, n):
            for j in range(0, mid):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        
if __name__ == "__main__":
    sol = Solution()

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.rotate(matrix))

# 1 4 7
# 2 5 8
# 3 6 9