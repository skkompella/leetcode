class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        memo = {}
        def recurse(n):
            if l - n == 0:
                return 0
            if l - n == 1:
                return cost[n]
            if l - n == 2:
                return cost[n]
            n_str = str(n)
            if n_str not in memo:
                memo[n_str] = cost[n] + min(recurse(n+1), recurse(n+2))
            return memo[n_str]
        return min(recurse(0), recurse(1))
            
