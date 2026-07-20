class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # memo = {}
        # n = len(prices)
        # def recurse(i, prev):
        #     if (i, prev) not in memo:
        #         if i == n:
        #             return 0
        #         if prev == 'bought': # you can sell or wait but cant buy
        #             memo[(i, prev)] = max(recurse(i+1, 'sold') + prices[i], recurse(i+1, 'bought'))
        #         if prev == 'sold': # you can buy (on same day) or wait
        #             memo[(i, prev)] = max(recurse(i, 'bought') - prices[i], recurse(i+1, 'sold'))
        #     return memo[(i, prev)]
        # return recurse(0, 'sold')
        min_price = prices[0]
        res = 0
        for i in prices:
            if i > min_price:
                res += i - min_price
            min_price = i
        return res
