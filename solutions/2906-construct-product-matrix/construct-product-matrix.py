class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        running_product = 1
        res = [[0]*len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res[i][j] = running_product % 12345
                # running_product *= grid[i][j]
                running_product = (running_product * grid[i][j]) % 12345
        running_product = 1
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                res[i][j] = (res[i][j] * running_product) % 12345
                # running_product *= grid[i][j]
                running_product = (running_product * grid[i][j]) % 12345
        
        return res
