class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # construct the adjacency list
        gridlen = len(grid)
        gridheight = len(grid[0])
        queue = collections.deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        time = 0
        while len(queue) != 0:
            flag = 0
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in ((0, 1), (0, - 1), (1, 0), (-1, 0)):
                    if 0 <= i+x < gridlen and 0 <= j+y < gridheight:
                        if grid[i+x][j+y] == 1:
                            grid[i+x][j+y] = 2
                            flag = 1
                            queue.append((i+x, j+y))
                            fresh -= 1
            if flag == 1:
                time += 1
        
        if fresh != 0:
            return -1
        return time
