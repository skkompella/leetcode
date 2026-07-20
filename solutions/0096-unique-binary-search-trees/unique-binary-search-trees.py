class Solution:
    def numTrees(self, n: int) -> int:
        memo = defaultdict(int)
        def recurse(n):
            if n == 1 or n == 0:
                return 1
            if n not in memo:
                for k in range(n):
                    memo[n] += recurse(k) * recurse(n-k-1)
            return memo[n]   
        return recurse(n)             
