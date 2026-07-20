class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def recurse(i, amt):
            if amt == 0:
                return 0
            if i < 0:
                return 2**31
            r2, r1 = 0, 0
            if coins[i] > amt:
                if (i-1, amt) not in memo:
                    memo[(i-1, amt)] = recurse(i-1, amt)
                return memo[(i-1, amt)]
            if (i-1, amt) not in memo:
                memo[(i-1, amt)] = recurse(i-1, amt)
            if (i, amt-coins[i]) not in memo:
                memo[(i, amt-coins[i])] = recurse(i, amt-coins[i])
            return min(memo[(i-1, amt)], 1+memo[(i, amt-coins[i])])
        jon = recurse(len(coins)-1, amount)
        if jon == 2**31:
            return -1
        return jon
