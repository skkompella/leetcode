class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        buy = 0
        sell = 1
        memo = [-10e4] * length
        for i in range(1, length):
            prev = memo[i-1]
            jon = prices[i] - prices[buy]
            prev_sell = sell
            print(jon, prev)
            if jon > prev:
                sell = i
                memo[i] = jon
            ron = prices[i] - prices[i-1]
            if ron > jon:
                buy = i-1
                memo[i] = ron
        return max(max(memo), 0)

