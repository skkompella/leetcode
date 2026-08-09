class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        height = len(matrix)
        width = len(matrix[0])
        max_val = 0
        for i in range(height-1, -1, -1):
            for j in range(width-1, -1, -1):
                matrix[i][j] = int(matrix[i][j])
                if max_val == 0 and matrix[i][j] == 1:
                    max_val = max(max_val, 1)
                if i != height-1 and j != width-1:
                    if matrix[i][j]>0 and matrix[i+1][j]>0 and matrix[i][j+1]>0 and matrix[i+1][j+1]>0:
                        matrix[i][j] = min(matrix[i+1][j], matrix[i][j+1], matrix[i+1][j+1]) + 1
                        max_val = max(max_val, matrix[i][j])
        # print(matrix)
        return max_val**2
