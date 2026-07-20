class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary search on weights
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            cap = (lo+hi)//2
            proposed_days = 1
            buf = 0
        
            for w in weights:
                if buf + w > cap:
                    proposed_days += 1
                    buf = w
                else:
                    buf += w
            #     print(buf)
            # print(cap, proposed_days)
            # print("--")
            if proposed_days > days:
                lo = cap + 1
            else:
                hi = cap
        return lo
