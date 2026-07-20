class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        length = len(grid)-1
        width = len(grid[0])-1
        def dfs(i, j):
            if (0 <= i <= length) and (0 <= j <= width):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    dfs(i+1, j)
                    dfs(i, j+1)
                    dfs(i-1, j)
                    dfs(i, j-1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    cnt += 1
                    dfs(i, j)
        return cnt
        
