class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        gridLen = len(grid)-1
        gridWid = len(grid[0])-1
        def recurse(i, j):
            if i > gridLen or j > gridWid:
                return float('inf')
            if i == gridLen and j == gridWid:
                return grid[i][j]
            if (i, j) not in memo:
                memo[(i, j)] = grid[i][j] + min(recurse(i+1, j), recurse(i, j+1))
            return memo[(i, j)]
        return recurse(0, 0)
