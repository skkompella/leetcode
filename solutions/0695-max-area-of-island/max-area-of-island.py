class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])
        def area_of_island(i, j):
            area = 0
            if grid[i][j] == 1:
                area += 1
                grid[i][j] = 0
                area += area_of_island(i, j)
            if i+1 >= 0 and i+1 < height and j >= 0 and j < width:
                if grid[i+1][j] == 1:
                    area += 1
                    grid[i+1][j] = 0
                    area += area_of_island(i+1, j)
            if i >= 0 and i < height and j+1 >= 0 and j+1 < width:
                if grid[i][j+1] == 1:
                    area += 1
                    grid[i][j+1] = 0
                    area += area_of_island(i, j+1)
            if i-1 >= 0 and i-1 < height and j >= 0 and j < width:
                if grid[i-1][j] == 1:
                    area += 1
                    grid[i-1][j] = 0
                    area += area_of_island(i-1, j)
            if i >= 0 and i < height and j-1 >= 0 and j-1 < width:
                if grid[i][j-1] == 1:
                    area += 1
                    grid[i][j-1] = 0
                    area += area_of_island(i, j-1)
            return area


        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(area_of_island(i, j), max_area)
        return max_area
