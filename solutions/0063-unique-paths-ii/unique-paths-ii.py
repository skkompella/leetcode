class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)-1
        n = len(obstacleGrid[0])-1
        memo = {}
        def recurse(m, n):
            if m < 0 or n < 0:
                return 0
            if obstacleGrid[m][n] == 1:
                return 0
            if m == 0 and n == 0:
                return 1
            if (m, n) not in memo:
                memo[(m, n)] = recurse(m-1, n) + recurse(m, n-1)
            return memo[(m, n)]
        return recurse(m, n)
