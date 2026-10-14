class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        # BFS from start to end
        # cache stores distance from 0 to that node for each node
        # build a queue that goes from (0, 0) to (length-1, length-1), starting with (0, 0)
        # queue and process neighbors in order. Replace a node only if a cheaper cost is found

        # dists = copy.deepcopy(grid)
        visited = {}
        q = collections.deque()
        q.append((1, 0,0))
        length = len(grid)
        if not grid or grid[0][0] == 1:
            return -1

        while len(q) != 0:
            d, i, j =q.popleft()
            if (i, j) in visited:
                continue
            # print(i, j)
            visited[(i, j)] = d
            for x, y in [(1, 1), (1, 0), (1, -1), (0, 1), (-1, 1), (0, -1), (-1, 0), (-1, -1)]:
                ni, nj = i+x, j+y
                if 0 <= ni < length and 0 <= nj < length:
                    if grid[ni][nj] == 0:
                        q.append((1+d, ni, nj))
        if (length-1, length-1) in visited: return visited[(length-1, length-1)]
        else: return -1
