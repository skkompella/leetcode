class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        length = len(matrix)
        height = len(matrix[0])
        memo = {}
        def DFS(x, y):
            if (x, y) not in memo:
                res = 1
                for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x_new, y_new = x+i, y+j
                    if 0 <= x_new < length and 0 <= y_new < height:
                        if matrix[x_new][y_new] > matrix[x][y]:
                            res = max(res, 1 + DFS(x_new, y_new))
                memo[(x, y)] = res
            return memo[(x, y)]
        
        max_len = 0
        for x in range(length):
            for y in range(height):
                max_len = max(max_len, DFS(x, y))

        return max_len
