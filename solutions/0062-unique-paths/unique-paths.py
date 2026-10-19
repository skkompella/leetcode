class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def recurse(i, j):
            if i == m-1 and j == n-1:
                return 1
            if i > m-1 or j > n-1:
                return 0
            if (i, j) not in cache:
                cache[(i, j)] = recurse(i+1, j) + recurse(i, j+1)
            return cache[(i, j)]
        
        return recurse(0, 0)
