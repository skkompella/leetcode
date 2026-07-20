class Solution:
    from itertools import permutations
    def minimumMoves(self, grid: List[List[int]]) -> int:
        sources = []
        sinks = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 1:
                    for k in range(grid[i][j]-1):
                        sources.append((i, j))
                if grid[i][j] == 0:
                    sinks.append((i, j))
        
        min_moves = float('inf')

        for p in permutations(sources):
            moves = 0
            for i in range(len(p)):
                moves += abs(p[i][0] - sinks[i][0]) + abs(p[i][1] - sinks[i][1])
            if moves < min_moves:
                min_moves = moves
        return min_moves
