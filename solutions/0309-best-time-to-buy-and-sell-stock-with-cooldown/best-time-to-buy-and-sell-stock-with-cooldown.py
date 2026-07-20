class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        n = len(prices)
        def recurse(i, prev): # prev can be buy, sell, cooldown
            if (i, prev) not in memo:
                if i == n:
                    return 0
                if prev == 'cooldown': # you can buy or cooldown next turn
                    memo[(i, prev)] = max(recurse(i+1, 'bought') - prices[i], recurse(i+1, 'cooldown'), )
                if prev == 'bought': # you can sell or cooldown next turn
                    memo[(i, prev)] = max(recurse(i+1, 'sell') + prices[i], recurse(i+1, 'bought'))
                if prev == 'sell': # you must cooldown next turn
                    memo[(i, prev)] = recurse(i+1, 'cooldown')
                # if prev == 'cant_buy': # you cant buy next turn
                #     memo[(i, prev)] = max(recurse(i+1, 'cant_buy') + prices[i], recurse(i+1, 'cooldown'), )
                # if prev == 'can_buy': # you can buy next turn
                #     memo[(i, prev)] = max(recurse(i+1, 'cant_buy') - prices[i], recurse(i+1, 'can_buy'))
            return memo[(i, prev)]
        return recurse(0, "cooldown")
