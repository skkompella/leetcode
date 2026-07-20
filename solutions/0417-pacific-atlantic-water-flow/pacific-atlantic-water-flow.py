class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = {}
        atlantic = {}
        sol = []
        height = len(heights)
        width = len(heights[0])
        for i in range(height):
            for j in range(width):
                if i == 0 or j == 0:
                    pacific[(i, j)] = heights[i][j]
                if i == height-1 or j == width-1:
                    atlantic[(i, j)] = heights[i][j]
        q = collections.deque()
        for x in pacific:
            q.append(x)
        
        while len(q) != 0:
            jon = q.popleft()
            i, j = jon[0], jon[1]
            if (0 <= i+1 < height and 0 <= j < width):
                if (i+1, j) not in pacific:
                    if heights[i][j] <= heights[i+1][j]:
                        pacific[(i+1, j)] = heights[i+1][j]
                        q.append((i+1, j))
            if (0 <= i < height and 0 <= j+1 < width):
                if (i, j+1) not in pacific:
                    if heights[i][j] <= heights[i][j+1]:
                        pacific[(i, j+1)] = heights[i][j+1]
                        q.append((i, j+1))
            if (0 <= i-1 < height and 0 <= j < width):
                if (i-1, j) not in pacific:
                    if heights[i][j] <= heights[i-1][j]:
                        pacific[(i-1, j)] = heights[i-1][j]
                        q.append((i-1, j))
            if (0 <= i < height and 0 <= j-1 < width):
                if (i, j-1) not in pacific:
                    if heights[i][j] <= heights[i][j-1]:
                        pacific[(i, j-1)] = heights[i][j-1]
                        q.append((i, j-1))
        
        for x in atlantic:
            q.append(x)

        while len(q) != 0:
            jon = q.popleft()
            i, j = jon[0], jon[1]
            if (0 <= i-1 < height and 0 <= j < width):
                if (i-1, j) not in atlantic:
                    if heights[i][j] <= heights[i-1][j]:
                        atlantic[(i-1, j)] = heights[i-1][j]
                        q.append((i-1, j))
            if (0 <= i < height and 0 <= j-1 < width):
                if (i, j-1) not in atlantic:
                    if heights[i][j] <= heights[i][j-1]:
                        atlantic[(i, j-1)] = heights[i][j-1]
                        q.append((i, j-1))
            if (0 <= i+1 < height and 0 <= j < width):
                if (i+1, j) not in atlantic:
                    if heights[i][j] <= heights[i+1][j]:
                        atlantic[(i+1, j)] = heights[i+1][j]
                        q.append((i+1, j))
            if (0 <= i < height and 0 <= j+1 < width):
                if (i, j+1) not in atlantic:
                    if heights[i][j] <= heights[i][j+1]:
                        atlantic[(i, j+1)] = heights[i][j+1]
                        q.append((i, j+1))

        for i in pacific.keys():
            if i in atlantic:
                sol.append(i)
        return sol
