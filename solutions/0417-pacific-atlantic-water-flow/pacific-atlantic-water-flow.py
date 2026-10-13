class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # memoized bfs 
        # if neighbor is ocean or in ocean set, add it to respective set
        # 
        pacific_cache = set()
        atlantic_cache = set()
        visited = set()
        height = len(heights)
        length = len(heights[0])

        pacific_cache.update((0, i) for i in range(length))
        pacific_cache.update((j, 0) for j in range(height))
        atlantic_cache.update((height-1, i) for i in range(length))
        atlantic_cache.update((j, length-1) for j in range(height))

        def ispacific(i, j):
            pacific_cache.add((i, j))
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = i+x, j+y
                if (nx, ny) not in pacific_cache:
                    if 0 <= nx < height and 0 <= ny < length:
                        if heights[nx][ny] >= heights[i][j]:
                            ispacific(nx, ny)


        def isatlantic(i, j):
            atlantic_cache.add((i, j))
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = i+x, j+y
                if (nx, ny) not in atlantic_cache:
                    if 0 <= nx < height and 0 <= ny < length:
                        if heights[nx][ny] >= heights[i][j]:
                            isatlantic(nx, ny)
        
        for i, j in list(pacific_cache):
            ispacific(i, j)
        for i, j in list(atlantic_cache):
            isatlantic(i, j)
        
        res = []
        for entry in pacific_cache:
            if entry in atlantic_cache:
                res.append(entry)
        return res

        # def isboth(i, j):
        #     visited.add((i, j))
        #     if i < 0 or j < 0:
        #         pacific_cache.add(i, j)
        #         return (1, 0)
        #     if i >= height or j >= length:
        #         atlantic_cache.add(i, j)
        #         return (0, 1)
            
        #     pacific, atlantic = 0, 0
        #     for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #         nx, ny = i+x, j+y
        #         if 0 <= nx < height and 0 <= ny < length:
        #             if height[nx][ny] <= height[i][j]:
        #                 pacific, atlantic += isboth(nx, ny)
        #         else:
        #             pacific, atlantic += isboth(nx, ny)
        #     if pacific > 0 and atlantic > 0:
        #         visited.add((i, j))
        #     return (pacific, atlantic)



        #     for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #         nx, ny = i+x, j+y
        #         if (nx, ny) not in visited:
        #             tmp = heights[i][j]
        #             heights[i][j] = float('inf')
        #             isboth(nx, ny)
        #             heights[i][j] = tmp
        #         if (nx, ny) in pacific_cache and heights[nx][ny] <= heights[i][j]:
        #             pacific_cache.add(i, j)
        #         elif ny < 0 or nx < 0:
        #             pacific_cache.add(i, j)
        #         if (nx, ny) in atlantic_cache and heights[nx][ny] <= heights[i][j]:
        #             atlantic_cache.add(i, j)
        #         elif nx >= height or ny >= length:
        #             atlantic_cache.add(i, j)
        
        # for i in range(height):
        #     for j in range(length):
        #         isboth(i, j)
        
        # res = []
        # for entry in pacific_cache:
        #     if entry in atlantic_cache:
        #         res.append(entry)
        
        # return res
