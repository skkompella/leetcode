class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = collections.deque()
        length = len(grid)
        length_0 = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
        res = 0
        while len(q) > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if 0 <= i+x < length and 0 <= j+y < length_0:
                        if grid[i+x][j+y] == 1:
                            grid[i+x][j+y] = 2
                            q.append((i+x, j+y))
            if len(q) > 0:
                res += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return res
