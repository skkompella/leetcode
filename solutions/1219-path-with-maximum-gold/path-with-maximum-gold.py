class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        length = len(grid)
        width = len(grid[0])
        def recurse(grid, x, y):
            if (0 <= x < length and 0 <= y < width):
                if grid[x][y] == 0 or grid[x][y] == -1:
                    return 0
            else:
                return 0
            jon = grid[x][y]
            grid[x][y] = -1
            out = jon + max(recurse(grid, x+1, y), recurse(grid, x-1, y), recurse(grid, x, y-1), recurse(grid, x, y+1))
            grid[x][y] = jon
            return out
        
        max_gold = 0
        for i in range(length):
            for j in range(width):
                ron = recurse(grid, i, j)
                if ron > max_gold:
                    max_gold = ron

        return max_gold
