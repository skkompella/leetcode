class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        memo = {}
        price_map = {(h, w): p for h, w, p in prices}

        def area(h, w):
            if (h, w) not in memo:
                max_price = price_map[(h, w)] if (h, w) in price_map else 0
                for y in range(1, h):
                    max_price = max(max_price, area(y, w) + area(h-y, w))
                for x in range(1, w):
                    max_price = max(max_price, area(h, x) + area(h, w-x))
                memo[(h, w)] = max_price
            return memo[(h, w)]


        # def area(h, w):
        #     if (h, w) not in memo:
        #         max_price = 0
        #         for y, x, p in prices:
        #             newj, newi = h-y, w-x
        #             if newi >= 0 and newj >= 0:
        #                  max_price = max(max_price, p + area(h-y, w) + area(y, w-x))
        #                 max_price = max(max_price, p + area(h-y, x) + area(h, w-x))
        #         memo[(h, w)] = max_price
        #     return memo[(h, w)]
        area(m, n)
        return memo[(m, n)]
